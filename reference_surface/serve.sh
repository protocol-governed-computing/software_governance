#!/usr/bin/env bash
#
# PGC Reference Surface — composition launcher.
#
# PURPOSE: a stable, externally observable surface for exercising and demonstrating the
# COMPLETE PGC reference implementation against a KNOWN warm-boot snapshot (Reference
# Platform Snapshot V0). It is bound to that snapshot by design — it is not a production
# application and does not dynamically generalize across snapshots.
#
#   Reference Platform Snapshot V0
#         |
#         +-- Collatz surface   (reference workload)
#         +-- PI surface        (platform-native inspection; cut #2)
#
# This script is where platform-resident knowledge lives: it points the DOMAIN-NEUTRAL
# transport HTTP adapter at platform roots — workload + surface boundary declarations,
# the web client, the shell, and the HTTP binding table.
#
set -euo pipefail
SURFACE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"    # platform/reference_surface
PLATFORM="$(cd "$SURFACE/.." && pwd)"                      # platform/
UMBRELLA="$(cd "$PLATFORM/.." && pwd)"                     # protocol-governed-computing/

export PGC_RUNTIME_ROOT="$UMBRELLA/protocol_runtime"
export PGC_IMPL_ROOTS="$PLATFORM"                          # reference_workloads.*.implementation.*
# TI/TE boundary contracts are read from the sealed snapshot (compiled TI_/TE_ kinds).
export PGC_HTTP_BINDINGS="$SURFACE/bindings/http.json"
export PGC_SNAPSHOT_ROOT="${PGC_SNAPSHOT_ROOT:-$UMBRELLA/snapshot}"   # Reference Platform Snapshot V0
export PGC_DATA_ROOT="${PGC_DATA_ROOT:-$UMBRELLA/data/reference_surface}"
# Static mounts (all READ-ONLY, config-driven). Three roots:
#   /          the web client (shell + all screens)
#   /traces    live per-run evidence from the instance data root (transient)
#   /snapshot  live inspection of the Reference Platform Snapshot (compiled artifacts, PNGs)
# Live means never stale; a missing artifact fails soft via the adapter's friendly 404.
export PGC_STATIC_MOUNTS="/=$SURFACE/client/web;/traces=$PGC_DATA_ROOT/traces;/snapshot=$PGC_SNAPSHOT_ROOT"
export PGC_HTTP_PORT="${PGC_HTTP_PORT:-8000}"

echo "PGC reference surface (stable, snapshot-bound)"
echo "  surface  : $SURFACE"
echo "  snapshot : $PGC_SNAPSHOT_ROOT"
echo "  data     : $PGC_DATA_ROOT"
echo "  port     : $PGC_HTTP_PORT"
echo

exec "$UMBRELLA/transport/run_http.sh"
