"""
store_lock.py — one writer at a time per store, across threads, processes and hosts.

A capability that reads a store, decides, and writes it back is correct only if no other writer
acts between the read and the write. A lock held inside one process says nothing to another process,
and nothing to a worker on another host sharing the store over a network filesystem — which is where
`LOCAL_MULTI_WORKER` and `FEDERATED_NODE` place writers.

The lock is a POSIX record lock (`fcntl.lockf`) on a sidecar file beside the store. NFSv4 carries
these locks to the server, so they exclude writers on every host that mounts the store. The sidecar
is locked rather than the store itself because stores are saved by replacing the file, and a lock on
a replaced file guards nothing. POSIX locks belong to a process, not a thread, so threads of one
process are serialized first by a thread lock on the same path.

Readers take no lock. Every mutation either replaces the store whole or appends to it under this
lock, so a reader sees a store before or after a write, never during one.
"""

import fcntl
import os
import threading
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

_thread_locks: dict[str, threading.Lock] = {}
_thread_locks_guard = threading.Lock()


def _thread_lock(key: str) -> threading.Lock:
    with _thread_locks_guard:
        return _thread_locks.setdefault(key, threading.Lock())


@contextmanager
def store_lock(store_path: Path | str) -> Iterator[None]:
    """Hold exclusive write access to one store for the duration of the block."""
    store_path = Path(store_path)
    lock_path = store_path.with_name(f".{store_path.name}.lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with _thread_lock(str(lock_path.resolve())):
        fd = os.open(lock_path, os.O_RDWR | os.O_CREAT, 0o644)
        try:
            fcntl.lockf(fd, fcntl.LOCK_EX)
            try:
                yield
            finally:
                fcntl.lockf(fd, fcntl.LOCK_UN)
        finally:
            os.close(fd)
