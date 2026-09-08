# Mountainous repetition-1 baseline

Status: BASELINE-WORLD ACCEPTANCE PASS. Five of sixteen worlds are individually
accepted. Protocol: `item10-full-v1`, coverage correction `item10-observer-coverage-v2`.
Seed: `6671238423019257953`; generation source:
`ee0a82b8350221d4e434e3603aa455d5cc7b83aa`.

The unchanged [run receipt](run.json) records all eleven selections, readiness,
correlated save flush and clean stop with Java exit 0 after 611.564 seconds.
Compared with ordinary repetition-2 baseline, `run.preflight` differs only in
`seed` and `seed_role`; `probe` and lifecycle `selections` are equal. All 228
frozen files and eleven declared Chunky files pass capture. This does not prove
full occurrence coverage or the selected saved-chunk denominator.

## Raw custody

The stopped world backup contains 501 files totaling 436,845,509 bytes.
`world.tar.gz` is 172,652,056 bytes, SHA-256
`75ccb3e089119d5ebca970c83cecfeddbd5b37425c9f4acce41c62403046f1e1`.
The [world restore](world-restore.json) verified all 501 files into a new world.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-mountainous-r1-baseline-ee0a82b8)
contains the outer archive and [manifest](archive-manifest.json). Its fetched tag
resolves to the generation source above. Archive size is 173,171,024 bytes,
SHA-256 `5106e752030685c31e5f5b28433b8bc40d6ff91909e8f95b7e2d6d2525aa0db8`;
312 files total 199,944,401 uncompressed bytes. [Local](local-restore.json) and
[downloaded](download-restore.json) restores verified all members; the downloaded
manifest matches byte-for-byte. No server restart was required for offline restore.

## Missing gateway capture

Comparing archive `files[].relative_path` sets against ordinary repetition-2
baseline finds exactly one absent raw member and no new member:
`trace.jsonl.classes/com/yungnickyoung/minecraft/betterendisland/world/feature/BetterEndGatewayFeature.class`.
There are 49 captured target classes. Calling the existing `collection_attempts`
with manifest-bound class/trace hashes and `require_complete_observer=True`
rejects with `collection does not bind the complete declared observer class set`.
The same iterator in diagnostic mode consumes 32,822 complete attempts and passes
its installation, hash, event pairing and healthy-shutdown checks. That diagnostic
pass does not waive the frozen 50-class requirement or establish zero gateways.
No full census was launched after this early rejection.

The frozen observer's `premain` registers a transformer whose `islandFeature`
predicate includes this exact class. It writes incoming bytes and an installation
event on targeted class definition; its exception path emits installation_failed.
The retained [provider source](../../item-8/sources/better-end-island-platform-gateway/README.md)
shows the custom gateway is invoked conditionally from a vanilla feature mixin.
An unexercised/lazily loaded class is therefore plausible, but full acceptance
requires resolving this distinction without silently weakening coverage or
hunting for a positive gateway in another world. The protocol and reader are
unchanged at that rejection. Further experiments were paused at this coverage question.

### Bounded class-loading check

The existing `test_island_templates_and_route_context` now records the JVM's
`-Xlog:class+load=info` output as well as the observer trace. In the four normal
fixture routes, the Gateway route loads and captures `BetterEndGatewayFeature`;
Podium, SpawnPlatform and Spike do neither, despite the common fixture referring
to all four classes. Each case asserts that the observer JAR equals the frozen
`d2051d5d5eb38aeda3dfc5c1d61d11ebf2e18a1fb3222ac46c12863556c5a782`.
The full 24-case island fixture also preserves original outputs, route context,
write outcomes, exception recovery and completed attempts.

Command: `uv run --no-sync pytest -q tests/item10/test_placement_probe.py -k island_templates_and_route_context`.
Result: 24 passed, 53 deselected in 24.88 seconds. The first Ruff check found one
overlong added string; splitting that literal fixes formatting only.

This reproduces a false premise in requiring every observer target to load in
every world. It does not supply a JVM class-load log for this preserved world,
and does not by itself change its rejection or prove a gateway zero. The next
correction must bind the frozen observer and distinguish an unexercised target
from a missing capture or installation. Keep hash, event and healthy-shutdown
checks strict; document any coverage-rule revision before accepting this census.

### Corrected coverage rule and validation

The [protocol correction](../protocol.md#coverage-correction-item10-observer-coverage-v2)
now admits only the demonstrated unexercised gateway case. It verifies the actual
frozen JAR and its archive binding, rejects other missing targets, undeclared
gateway bytes and unmatched installation events, and records the coverage set in
the result. Original rejection and raw bytes remain unchanged.

The full command `uv run --no-sync pytest -q tests/item7 tests/item10` passed
548 tests in 173.38 seconds. Two subsequently added archive-binding cases and the
affected collection/saved-content checks passed together: 41 tests in 10.63
seconds. Focused Ruff and test-file basedpyright passed after adding explicit
types for the new fixture containers. No Item 11 checks ran.

The corrected all-strata census completed on the restored world, execution
session `22204`, exit 0. Its command is:

```sh
uv run --no-sync python -m tools.analyze_structure_density evidence/raw/item10/full-mountainous-r1-baseline-custody/restored-world/world evidence/raw/item10/full-mountainous-r1-baseline-analysis/all-strata.json --all-strata --dimension-geometry evidence/item-10/dimension-geometry.json --trace-root evidence/raw/item10/full-mountainous-r1-baseline-custody/restored-local --trace-manifest evidence/item-10/full-mountainous-r1-baseline/archive-manifest.json
```

## Full census and first seed comparison

The analysis implementation is `760aa2f5`. Analysis completed in 10m38.455s
(user 10m29.764s, system 0m1.644s), including overlap with the test suite.
Output size: 110,506,948 bytes; SHA-256:
`bb0f1eeb9f638f050541bf1cb1ee88b4abbbba51ead99264bb77b7962a50f149`.
Timing is preserved beside it in `all-strata-runtime.txt`. All eleven strata
contain 4,096 complete chunks, totaling 45,056. Archive-bound class, complete
trace and saved-world checks pass under coverage-v2. `observer_coverage` retains
49 captured targets and the single unexercised gateway target explicitly.

This table directly projects `strata[label].total_starts` and
`classification.categories[category].count`. Density is count times `1000/4096`.
Categories retain Item 9's provisional confidence and ambiguity.

| Stratum | Registry starts | Classified locations | T0 | C | T1 | T2 | T3 | T4 | Villages |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| aether | 30 | 3 | 0 | 0 | 0 | 3 | 0 | 0 | 0 |
| earth-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| mars-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon-orbit | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| moon | 12 | 12 | 12 | 0 | 0 | 0 | 0 | 0 | 0 |
| venus | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| overworld | 43 | 4039 | 23 | 8 | 4000 | 6 | 2 | 0 | 3 |
| end-central | 1 | 3 | 2 | 0 | 0 | 0 | 0 | 1 | 0 |
| end-outer | 13 | 19 | 19 | 0 | 0 | 0 | 0 | 0 | 0 |
| nether | 55 | 426 | 36 | 2 | 380 | 7 | 1 | 0 | 0 |

The 27 Aether cloud starts remain excluded terrain. Central End includes the
arrival platform and dragon arena as lifecycle sites. No custom gateway location
was observed. This is scoped to the captured generation, not universal absence.
The arena is the sole observed nonregistry location with NO_LOCATION_HEIGHT and
no biome attribution; the other 4,374 have biome attribution. Per-category spatial
results retain boundary censoring, nearest observed versus uncensored means,
cell dispersion and empty rectangles. Raw biome exposure remains in each stratum.

The 32,822 attempts yield 25,380 NO_CONSTRUCTIVE_CONTENT, 2,858 OUTSIDE_FRAME,
4,375 OBSERVED_LOCATION and two CONTENT_NOT_PRESERVED location dispositions.
The latter are cave-urn candidates 20368 at Overworld (191,24,389) and 21261 at
(223,-40,27), each with one saved-content mismatch. Neither enters the numerator.
Attempts and grouped location dispositions have distinct denominators.

Compared with the [ordinary repetition-1 baseline](../full-ordinary-r1-baseline/README.md),
Overworld classified locations rise from 955 to 4,039 while T2 falls from seven
to six; T3 rises from zero to two and villages from one to three. The mountainous
Overworld's accepted nonregistry locations comprise 3,784 cave-urn caches, 208
monster boxes, three scarecrows and one fairy ring. These are direct counts of
`locations` joined by candidate ID to OBSERVED_LOCATION dispositions. High total
location density therefore does not imply a similar increase in proper dungeons,
observed fights or enjoyable exploration. The remaining seeds and repetitions
are still required; this single contrast is not a population estimate.

The current world, original raw, custody copies, analysis and outer archive use
2,126,249,984 allocated bytes (about 1.98 GiB). This `du -s -B1` accounting lists
the shared candidate, pristine and prior instance directories first so shared
inodes are not charged twice. About 35.5 GiB was free during analysis. The observed
working footprint remains near the roughly 30 GiB plan for sixteen worlds.

## Reproduction

Use the existing [custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this run's name, revision, archive and world hash. Parents must exist and
outputs must be absent. Executed generation and archive commands:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-mountainous-r1-baseline --mode probe --preset item10 --role mountainous --arm baseline --repetition 1
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-mountainous-r1-baseline --archive evidence/raw/item10/item10-full-mountainous-r1-baseline-ee0a82b8.tar.gz --manifest evidence/item-10/full-mountainous-r1-baseline/archive-manifest.json --revision ee0a82b8350221d4e434e3603aa455d5cc7b83aa
```

The direct trace check derives class names by stripping `trace.jsonl.classes/`
and `.class` from manifest members, takes their SHA-256 values and the manifest's
trace SHA-256, and consumes `collection_attempts` completely with the ten protocol
dimensions. Run the complete-observer mode and diagnostic mode separately; do not
present the latter as acceptance. Existing Java fixture tests in
`tests/item10/test_placement_probe.py` and `probe-fixture/IslandFixture.java` are
available for a bounded investigation of the class-loading distinction.
