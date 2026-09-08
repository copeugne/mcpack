# BetterEnd r5: actual ground position observed

The [trace](trace.jsonl) records the commanded origin and the actual returned
ground as `[8,81,8]`, followed by false return without template invocation.
This rules out an incorrect ground height in this run. The saved chunk has
`minecraft:end_stone` at `[8,80,8]` and `minecraft:air` at `[8,81,8]`.
These saved states were inspected in restored `DIM1/region/r.0.0.mca`, chunk
`[0,0]`, section Y=5, block-state indices 136 and 392 respectively. They are
post-run observations, not direct reads at predicate execution.

Accepted Item 8 `betterend-feature-scope` BuildingListFeature.canSpawn requires
even chunk parity, Y above 58, air at the ground position, and TERRAIN membership
below it. Parity and height pass. Given unchanged platform states, terrain-tag
membership is the remaining candidate rejection. This is an inference, not a
captured runtime tag result. WorldWeaver CommonBlockTags defines TERRAIN through
`makeWorldWeaverTag("surfaces/terrain")`; its effective membership still needs
verification. No additional experiment should assume vanilla end stone belongs.
No template placement or density counts are accepted.

Source `3079920fa5dc2baff416bcb6055ab48eb2425c6d`. The [receipt](diagnostic.json) records clean
lifecycle completion in 89.996 seconds. The new
single-call-site ground hook passes the existing synthetic preservation and exact
packaged transformation tests, including isolated classloading. It neither
re-evaluates getGround nor changes its returned reference.

## Custody

[Release](https://github.com/copeugne/mcpack/releases/tag/item-10-betterend-ground-2026-09-08-r5).
Archive size 5221756 bytes, SHA-256 `4eb81b9f4383c9641fc2377d0c0e32bf59720d1d748d6d6808e14be999b66a94`.
[Download restore](download-restore.json) verifies all 254 raw files and its
manifest is byte-identical. [Nested world restore](world-restore.json) matches
all 97 paths, sizes and hashes from [world backup](world-backup.json), without
booting it. Existing archive tools used root `evidence/raw/item10/betterend-ground-r5`
and revision `3079920f`; restore the downloaded archive with [manifest](archive-manifest.json),
then its nested world archive with SHA-256 `0faad36bdb38564a468044a767372422d3cf63d805ad79d1410b6c9af492a6ad`.
