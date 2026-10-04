"""
ct_executor.py — minimal PGC reference execution contract for capability transforms.

Vendored into the platform snapshot so the reference CT implementations are self-contained
(no pgs_* dependency). The PGC runtime re-exports / binds to this contract at execution time.
"""

from __future__ import annotations


class CTExecutionError(Exception):
    """Raised by a capability transform when its inputs violate its declared contract."""
