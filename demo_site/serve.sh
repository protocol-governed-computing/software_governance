#!/usr/bin/env bash
#
# Platform demo-site composition. This is where platform-resident knowledge lives: it
# points the DOMAIN-NEUTRAL transport HTTP adapter at platform roots — workload boundary
# declarations (TI/TE), workload screens, the demo shell, and the HTTP binding table.
#
# The demo showcases only platform-resident material: reference workloads (Collatz) and,
# later, the Protocol Inspector (pi) over the platform-resident PPS/snapshot.
#
set -euo pipefail
DEMO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"   # platform/demo_site
PLATFORM="$(cd "$DEMO_DIR/.." && pwd)"                     # platform/
UMBRELLA="$(cd "$PLATFORM/.." && pwd)"                     # protocol-governed-computing/
COLLATZ="$PLATFORM/reference_workloads/collatz"

export PGC_RUNTIME_ROOT="$UMBRELLA/protocol_runtime"
export PGC_IMPL_ROOTS="$PLATFORM"                          # reference_workloads.collatz.implementation.*
export PGC_OPERATIONS_ROOTS="$COLLATZ/transport"          # TI_/TE_ boundary declarations
export PGC_STATIC_MOUNTS="/=$DEMO_DIR;/collatz=$COLLATZ/static"
export PGC_HTTP_BINDINGS="$DEMO_DIR/http_bindings.json"
export PGC_SNAPSHOT_ROOT="${PGC_SNAPSHOT_ROOT:-$UMBRELLA/snapshot}"
export PGC_DATA_ROOT="${PGC_DATA_ROOT:-$UMBRELLA/data/demo_site}"
export PGC_HTTP_PORT="${PGC_HTTP_PORT:-8000}"

echo "PGC platform demo-site"
echo "  shell    : $DEMO_DIR"
echo "  collatz  : $COLLATZ"
echo "  snapshot : $PGC_SNAPSHOT_ROOT"
echo "  data     : $PGC_DATA_ROOT"
echo "  port     : $PGC_HTTP_PORT"
echo

exec "$UMBRELLA/transport/run_http.sh"
