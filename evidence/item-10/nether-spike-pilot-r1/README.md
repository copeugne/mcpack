# Nether spike natural pilot r1: positive writes, validation pending

Source `d31d7d912ef4023dd350ea1e0e48b5752276d103`, fresh ordinary seed 42,
unchanged frozen configuration and the [predeclared 324-chunk pilot](../protocol.md#nether-spike-natural-pilot-r1).
[Diagnostic](diagnostic.json) records all four selections, correlated save,
clean stop and exit 0 in 88.346 seconds. No terrain or placement commands ran.

Direct inspection of retained trace.jsonl finds 202 Monster Box calls, nine
ObsidianSpikeGenerator calls and one BuildingListFeature attempt. The first two
classes have 211 paired generator_end events; the BetterEnd attempt has ground
and false end records. All 212 attempts are finished. There are 269 successful
minecraft:obsidian writes from the spike method and seven quark:monster_box writes,
with no refused writes. The trace is 81,663 bytes. These provisional event counts
are not accepted density measurements, full coverage or gameplay observations.
Large-spike reward/spawner paths were not positively exercised in this run.

Next validate the complete mixed trace and incoming identities, then corroborate
saved blocks by dimension. Retain the unsuccessful BetterEnd attempt and all
zero-write calls. The existing single-dimension Monster Box inspector is not an
acceptance path for this mixed run without extending its existing dimension map.
Do not regenerate for these checks; use the restored artifacts.

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
