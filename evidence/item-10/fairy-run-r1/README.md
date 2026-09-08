# Fairy diagnostic r1: installed hook, no helper calls

Source `9121683c1462c16e13b6f018f4629a3091e71f61`; ordinary seed 42 and the
[predeclared 6,852-chunk frame](../protocol.md#fairy-natural-diagnostic-r1).
[Diagnostic](diagnostic.json) records all four selections, readiness, correlated
save, clean stop and exit 0 in 253.19 seconds. No terrain, placement or tuning
commands ran. This elapsed time is not a paired observer-overhead measurement.

Archived trace.jsonl contains the FairyRingGenerator installation with incoming
class SHA-256 3a30145aaad2e116ab762a6c090659a3f02f125dfd98972c3df72f4319691a74,
matching the retained class. There are no fairy feature/helper attempts or flower
records. Positive fairy capture fails. Outer generateChunk calls rejected before
spawnFairyRing are outside the declared trace population; neither their count
nor the cause of rejection is inferred. Do not expand or switch seeds for a
positive result. No density estimate is accepted from this diagnostic.

Direct event inspection finds 4,306 Monster Box, 270 Nether spike, 72 spiral-part
and 14 BuildingListFeature attempts (4,662 total). The 16,605 write records
comprise 111 Monster Box and 16,494 spike writes. All 14 BetterEnd returns are
false. Shutdown reports zero unfinished attempts. These counts retain the full
mixed population; the mixed-trace integrity check now passes (see below), while saved-content
and density acceptance remain separate. No positive spiral writes occurred either.

The trace is 3,043,293 bytes, SHA-256
`45ab23b9edf2e7b1a5dfe481284baaefb4b70c5251d07351e7d1b65e092ae006`.
Inspect its feature, write, end and shutdown records after the verified restore;
the immutable trace is the authority, not these summary counts.

## Verified custody

[Release](https://github.com/copeugne/mcpack/releases/tag/item-10-fairy-run-2026-09-08-r1).
The fetched tag resolves to the source above. Archive
item10-fairy-run-r1-9121683c.tar.gz is 76,943,807 bytes, SHA-256
`53db66484a7bda655d97339c53fe928f84999f560a0b69418a9fb607590b2768`.
[Manifest](archive-manifest.json) binds 260 files totaling 81,693,301 bytes.
The downloaded manifest matches byte for byte; [download restore](download-restore.json)
verifies every member. The archive root has no wrapper directory.

[World backup](world-backup.json) binds 158 files and nested archive SHA-256
`250bd4d5e7abb24bc6131f63dcf72f6c0541242a7169a28bed6f1aac1629beea`.
[World restore](world-restore.json) was compared against every sorted manifest
path, size and hash without booting. Reuse the existing archive/world restore
commands and these identities with local custody root
`evidence/raw/item10/fairy-run-r1-custody/{downloaded,restored,restored-world}`.

Item 10 remains incomplete. No Item 11 workflow ran.

## Archive-bound mixed-trace integrity

[Trace validation](trace-validation.json) binds the complete trace and every
required incoming class to the immutable archive. Each spiral attempt requires
one part event, a correctly typed destination, the End dimension and a void
generator completion. Source keys are grouped without treating them as
successful locations. BetterEnd false returns retain their ground observations.
The fairy diagnostic requires its installed class even though no helper call
occurred. These bounded zero-write paths do not accept hypothetical successful
spiral or fairy records. Positive capture and saved-content gates remain unmet.

Reproduce without a server:

```sh
uv run --no-sync python -m tools.validate_item10_trace --fairy-r1 evidence/raw/item10/fairy-run-r1-custody/restored
```

Focused regressions reject missing/repeated part events, wrong attempt binding,
malformed coordinates, unexpected writes, omitted spiral attempts and missing
fairy installation. Existing BOP, Monster Box and Nether trace reports reproduce
byte for byte. No raw archive revision was created for this reader-only change.

Validation: all 350 Item 7/10 tests pass in 65.27 seconds. Changed-reader/test
Ruff and basedpyright checks pass. No Item 11 workflow ran.

## Reviewed delivery

PR29 merged the collector and retained diagnostic as
`3b50c59a1504f6cca7240bb4ef99c67569caf5b7`. Fetched `origin/main` contains
reviewed head `6aa2713d7e16ef66cabd3f114f8317b68797184b`.
The [clean review](https://github.com/copeugne/mcpack/pull/29#issuecomment-5580397624)
completed on 2026-09-08 at 06:33:42 UTC with no inline or review findings;
the Codex bot added a thumbs-up to the pull request at 06:33:45 UTC.
This delivery preserves the failed positive-capture gate, not Item 10 completion.
The archive-bound reader extension above is a separate subsequent milestone.
