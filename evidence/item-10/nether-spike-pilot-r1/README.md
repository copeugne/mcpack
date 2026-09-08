# Nether spike natural pilot r1: mixed trace and saved blocks corroborated

Source `d31d7d912ef4023dd350ea1e0e48b5752276d103`, fresh ordinary seed 42,
unchanged frozen configuration and the [predeclared 324-chunk pilot](../protocol.md#nether-spike-natural-pilot-r1).
[Diagnostic](diagnostic.json) records all four selections, correlated save,
clean stop and exit 0 in 88.346 seconds. No terrain or placement commands ran.

The [archive-bound trace check](trace-validation.json) finds 202 Monster Box calls, nine
ObsidianSpikeGenerator calls and one BuildingListFeature attempt. The first two
classes have 211 paired generator_end events; the BetterEnd attempt has ground
and false end records. All 212 attempts are finished. There are 269 successful
minecraft:obsidian writes from the spike method and seven quark:monster_box writes,
with no refused writes. The trace is 81,663 bytes. These capture counts are not density measurements, full coverage or gameplay observations.
Large-spike reward/spawner paths were not positively exercised in this run.

The existing checker validates every lifecycle event and all ten incoming class
bindings. The runtime ObsidianSpikeGenerator hash matches its retained source
identity. The inherited BuildingListFeature consumer maps to the instrumented
NBTFeature class; its ground event and false return are mandatory for this
bounded failed-template observation. Generator endings cannot substitute for
that boolean return. Each feature is checked against its recorded dimension.

The [saved-block crosscheck](saved-block-crosscheck.json) corroborates all 276
successful block IDs at distinct dimension/coordinate keys. Two writes are in
full chunks, 233 in initialize_light and 41 in carvers neighbors. These incomplete
chunks are not admitted to completed-chunk exposure. All 212 attempts remain in
the report, including zero-write calls and the false BetterEnd return. No block
state property equality or observer-free equivalence is claimed.

The existing inspector now keys region reads, coordinates and repeat handling by
dimension. It fails after printing any saved-block mismatch. Reproduce using the
same restored roots, with no server run:

```sh
uv run --no-sync python -m tools.validate_item10_trace --spike-r1 evidence/raw/item10/nether-spike-pilot-r1-custody/restored
uv run --no-sync python -c "import runpy; runpy.run_path('evidence/item-10/scarecrow-probe-r3/inspect-writes.py')" --spike-r1
```

All 340 Item 7/10 tests pass in 60.23 seconds. Mixed-trace regressions reject wrong
dimensions and endings, omitted/repeated ground events, an unsupported true
BetterEnd return, refused-only spike writes and malformed shutdown type. Existing
corrupt trace/manifest/region/block tests also cover the new mode. BOP and Monster
Box trace reports still reproduce byte for byte. Changed-file Ruff and validator/
test basedpyright checks pass. No extra measurement or raw archive revision was needed.

## Verified custody

[Release](https://github.com/copeugne/mcpack/releases/tag/item-10-nether-spike-pilot-2026-09-08-r1).
The fetched tag resolves to the source above. Archive
`item10-nether-spike-pilot-r1-d31d7d91.tar.gz` is 5,791,162 bytes with SHA-256
`6861e7fb69939ae6619da60f81dc14d6ae80127780dbd9fd2feb4e8e79cbcd30`.
[Manifest](archive-manifest.json) binds 258 files, and [download restore](download-restore.json)
verifies every member. Downloaded and committed manifests match byte for byte.
The raw root has no wrapper directory.

[World backup](world-backup.json) binds 103 files to nested archive SHA-256
`48af7e6ca10eddef321f22eae986efd8a7fa6e71e67c3961fbe7e2a529656546`.
[World restore](world-restore.json) was compared against every manifest path,
size and SHA-256 without booting. Local custody uses
`evidence/raw/item10/nether-spike-pilot-r1-custody/{downloaded,restored,restored-world}`.
Reuse the existing archive and world restore commands with these hashes.

No Item 11 work ran. Item 10 full sampling remains gated on occurrence coverage,
collector validation and measured observer/storage cost.

## Reviewed delivery

[PR27](https://github.com/copeugne/mcpack/pull/27) merged as
`9bad3862a5c7a7eb137a689b0030ae73fc172667`, verified in fetched main.
The [final review](https://github.com/copeugne/mcpack/pull/27#issuecomment-5580117138)
completed on `7e1d3b7bc2889ef6d534cdcc9cf08491a3a1e78a` with no new findings
and a Codex bot thumbs-up. The reviewed head is an ancestor of main.
The earlier request to split commits was invalid: implementation, protocol, raw
custody, validation and delivery bookkeeping were already separate commits.
[Disposition](https://github.com/copeugne/mcpack/pull/27#issuecomment-5580055921)
records the five commit boundaries. No history rewrite or raw change was needed.
This closes the Nether diagnostic review, not Item 10.
