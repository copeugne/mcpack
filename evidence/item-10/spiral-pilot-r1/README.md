# Spiral pilot r1: source parts captured, no positive writes

Source `6f3e50c3fdfbef97ed52b87d5cd510711d15bb73`; ordinary seed 42 and the
[predeclared pilot](../protocol.md#spiral-natural-pilot-r1). The [diagnostic](diagnostic.json)
records all four selections, correlated save, clean stop and exit 0 in 89.532
seconds. No terrain or placement commands ran.

Direct inspection of archived trace.jsonl finds spiral attempts 212 through 217.
Each contains begin, feature, part and generator_end, with no writes. All share
source [1616,0,-48] in minecraft:the_end; their destination anchors are
[1600,0,-64], [1600,0,-48], [1600,0,-32], [1616,0,-32], [1616,0,-48] and
[1616,0,-64], in attempt order. This is one source and six contribution attempts,
not six sites. The source is outside the selected rectangle and must remain
boundary-censored even if a future reader finds successful contributions.

The trace also retains 202 Monster Box and nine Nether spike attempts, seven
Monster Box writes and 261 spike writes. Shutdown reports zero unfinished
attempts. These are direct event counts, not accepted density numerators.
The trace is 82,322 bytes, SHA-256
`a73335cbf792c939a2b05058feee383c7ba2c28463f13d5625939272213394f5`.
Positive spiral capture fails; there are no recorded successful spiral writes
to corroborate.
Mixed-trace validator integration remains pending. Do not expand the sample in
response to this result. Inspect the existing biome/terrain rejection conditions
before proposing another experiment. No cause of these early returns is inferred.

## Verified custody

[Release](https://github.com/copeugne/mcpack/releases/tag/item-10-spiral-pilot-2026-09-08-r1).
The fetched tag resolves to the source above. Archive
item10-spiral-pilot-r1-6f3e50c3.tar.gz is 5,579,251 bytes, SHA-256
`6e69ba837e6c1af357e4b5d84dac5340e1b6c803802a891504d86dc976e7aa2e`.
[Manifest](archive-manifest.json) binds 259 files. The downloaded manifest matches
byte for byte and [download restore](download-restore.json) verifies every file.
The archive root has no wrapper directory.

[World backup](world-backup.json) binds 103 files with nested archive SHA-256
`d76a35ec6493bafa78d9ecbcf54a2b60c91e342331f70be545e0af2b189fc264`.
[World restore](world-restore.json) was compared against every sorted manifest
path, size and digest without booting. Use the existing archive and world restore
commands with these hashes and local custody root
`evidence/raw/item10/spiral-pilot-r1-custody/{downloaded,restored,restored-world}`.

No Item 11 workflow ran. Item 10 remains incomplete.
