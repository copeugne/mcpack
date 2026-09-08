# BetterEnd diagnostic r1: rejected identity and insufficient placement evidence

Source revision: `be0f21c0c1cfb5dee4b8398ef9c0fd2e7ca6abfb`. The predeclaration
is in [the protocol](../protocol.md#betterend-runtime-diagnostic-r1).
The [raw diagnostic receipt](diagnostic.json) records the agent identity, exact
frozen preflight, four completed selections, unchanged configuration gate and
correlated save-flush/clean exit (code 0), taking 335.299 seconds.

The [trace](trace.jsonl) contains 27 paired feature attempts, including 24
BetterEnd feature entries (23 building-list and one ship), 15 direct scarecrow
writes, four new-class installation
records, the scarecrow installation and final shutdown with no unfinished attempts.
There are no `template_begin`, `template_end` or template content-write records.
These counts are direct counts by the trace's `kind` field; they are not accepted
density measurements. Zero template calls is INSUFFICIENT for the real-placement
capture gate and cannot validate the BetterEnd count method.

Three incoming BetterEnd class hashes match Item 8. The incoming Minecraft
`StructureTemplate` hash is
`579560f5341cba7e3a23064fdc7d1938922dd14e18a1ca4ecab434f57379a2bd`,
which differs from the packaged input predeclared in the protocol. This fails
the runtime identity gate. Incoming class bytes were not retained by this agent;
the cause of the difference remains UNKNOWN. The follow-up code preserves such
bytes, but it cannot retroactively supply missing evidence for this run.

The [stopped-world manifest](world-backup.json) retains 154 files and an
89,095,578-byte archive with SHA-256
`130a10de9173deaeb08dc41e5c5924453d7c6c033d42877f4fb5a745ca8ef0ce`.
No proof world, frozen configuration or prior evidence was replaced. The [raw release](https://github.com/copeugne/mcpack/releases/tag/item-10-betterend-rejected-2026-09-08-r1)
is bound to the launch revision by the fetched tag. Its 89,261,160-byte archive
has SHA-256 `9d83c6eb411e8f0082319a1531c261c7ee85f696a9cc61da146b457810dae83a`.
The [download/restore receipt](download-restore.json) verifies all 249 raw members;
the downloaded manifest is byte-identical. The [nested world restore](world-restore.json)
contains exactly the 154 manifest paths, each with matching size and SHA-256.
These checks used the existing archive and world-restore tools; no restored world
was booted. Item 10 remains IN PROGRESS.

```sh
gh release download item-10-betterend-rejected-2026-09-08-r1 --repo copeugne/mcpack --dir RESTORE_INPUT
uv run --no-sync python -m tools.archive_item7_evidence restore --archive RESTORE_INPUT/item10-betterend-rejected-r1-be0f21c0.tar.gz --manifest evidence/item-10/betterend-probe-r1/archive-manifest.json --target RESTORED_RAW --receipt RESTORE_RECEIPT.json
uv run --no-sync python -m tools.manage_item4_environment restore --archive RESTORED_RAW/world.tar.gz --sha256 130a10de9173deaeb08dc41e5c5924453d7c6c033d42877f4fb5a745ca8ef0ce --target RESTORED_WORLD
```

The large generated manifest diff is isolated with this raw diagnostic's custody
records. Archive creation used the existing implementation:

```sh
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/betterend-probe-r1 --archive evidence/raw/item10/betterend-r1-custody/item10-betterend-rejected-r1-be0f21c0.tar.gz --manifest evidence/item-10/betterend-probe-r1/archive-manifest.json --revision be0f21c0c1cfb5dee4b8398ef9c0fd2e7ca6abfb
```
