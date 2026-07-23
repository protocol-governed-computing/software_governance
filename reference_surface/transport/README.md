# reference_surface/transport

Boundary declarations (`TI_`/`TE_`) for **surface-native operations** — platform
interactions that are *not* reference workloads (they have no governed `WF`).

Unlike a reference workload (which owns its boundary declaration under
`reference_workloads/<name>/transport/`), a surface operation queries or observes
platform-resident material directly. Each operation lives in its own subdirectory
holding exactly one `TI_` and one `TE_`:

```
transport/
└── pi/                       # Protocol Inspector (cut #2)
    ├── TI_PI_QUERY_V0.md      # handler.kind: SNAPSHOT_QUERY (reads the warm-boot snapshot / PPS)
    └── TE_PI_QUERY_V0.md
```

These declarations are loaded by the transport resolver's registry (pointed here via
`PGC_OPERATIONS_ROOTS`) and are bound to the Reference Platform Snapshot V0.
