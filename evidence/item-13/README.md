# Item 13 baseline dungeon quality

Status: IN PROGRESS. Item 14 is UNSTARTED.

## Authorized method and delivery boundary

On 2026-09-09 the user authorized starting Item 13, superseding the old handoff's
wait instruction. In the same session the user separately selected:
"Authorize the separate modeled/inspection scope" in response to the explicit
proposal to use validated playable topology, modeled traversal/combat estimates
and source-supported quality assessments, with human times and realized
encounters left NOT MEASURED. This decision applies only to Item 13. It does not
silently extend the Items 10/11 amendment or Item 12 authorization.

The [protocol](protocol.md) records the method boundary and definitions before
scoring. A numerical model must state its inputs and assumptions; authorization
for modeling is not permission to invent calibrated player outcomes or substitute
piece counts for rooms. The intake is an availability index; the first quality results are in the
[small-dungeon representative](pilot/report.md).

Startup fetched refs and tags, inspected branch/upstream, both diffs, graph and
relevant path history. The clean previous branch was identical in tree to fetched
main `3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf`. GitHub confirms PR40 merged
head `356384ba` at 2026-09-09 14:17:41 UTC, after PR39's accepted Item 12 head
`4fc7e605`. Work starts from that main on `codex/item13-dungeon-quality`.
Dependencies are the delivered Item 9 classification, Item 10 density/custody,
Item 11 routes and Item 12 discoverability. Their closure records and the delivered
[cross-item audit](../item-10/cross-item-audit.md) are reused, not rerun.

## Requirement map

| Requirement | Existing evidence available | Concrete missing measurement or assessment |
| --- | --- | --- |
| Every significant family | Item 8's 448 canonical families, Item 9 roles/flags/ambiguities | Complete [intake](intake.json) includes 192, excludes 256; [material coverage](coverage.md) resolves variants incrementally and sample all included designs, including non-Overworld content |
| Room count | Packaged templates, custom generator source and accepted saved worlds | Delineate playable spaces and validate room boundaries against blocks and connections |
| Branching | Pool links and piece envelopes | Actual room/connector graph, junctions, dead ends and loops; pool branches are not playable branches |
| Vertical progression | Source vertical designs and Item 12 placement context | Reachable floor changes and their traversal order |
| Dungeon depth | Source placement offsets and saved envelopes | Entry-to-objective graph depth, route distance and burial depth, separately |
| Traversal time | Item 5 duration categories, Item 11 transport assumptions | Route-based modeled time with explicit actor, terrain, navigation and uncertainty; human time NOT MEASURED |
| Combat time | Authored entities, spawners and generator logic | Explicit encounter-workload and combat model with supported inputs; no fabricated realized encounter duration |
| Enemy count | Source entity/spawner potential | Per-sample authored residents, spawner parameters and conditional populations, separately; realized enemies NOT MEASURED |
| Enemy diversity | Exact source IDs and ambiguity | Distinct hostile types and conditional alternatives per sample, excluding objects/civilians |
| Meaningful hazards | Template palettes/markers and generator code | Function and route relevance of actual hazard mechanisms, distinguished from mere ingredients |
| Chokepoints | Source doors, corridors and stairs | Narrow playable connections and alternate paths; no claim about live AI behavior |
| Dead/empty rooms | Source furnishings, loot and encounter ingredients | Room-level content/objective/connectivity coding with explicit denominator |
| Loot distribution | Source tables/markers, known ineffective assignments | Container/other reward positions by room/depth; potential versus generated contents versus acquired items kept separate |
| Final-room quality | Source boss/objective/reward architecture | Explicit finale identification or absence, access, payoff and bypass assessment |
| Bypass opportunities | Source geometry, block materials, Item 12 access limits | Alternative route, capability and avoided objectives/rooms; no ban or tuning |
| External-access vulnerabilities | Source exterior/roof/underground architecture | Boundary-to-reward/goal access and bypass costs on sampled geometry |
| Expected replay value | Source layout alternatives, Item 11 repetition limits | Supported assessment of layout/objective/encounter variation and persistence limitations, not player enjoyment |
| Visually large but shallow | All Item 9 S/O flags and Item 12 architecture | Compare external form with validated internal topology/content, never volume alone |

## Input availability and remaining coverage

[intake.py](intake.py) directly reuses the accepted readers and POSIX world lock.
It verifies each restored world's complete inventory against its archive-bound
backup manifest, verifies each accepted census hash, and joins existing occurrence
rows across all eleven strata. This does not regenerate or reprocess density,
routes or discoverability. No new evidence validator or archive class is introduced.

The first inspection passed all sixteen restored inventories: 6,806,284,224 world
bytes and 1,784,216,273 census bytes. It took 20.745 seconds and observed
42,464,829,440 free bytes. That original intake is preserved in commit `67003da1`.

The integrated second inspection also reads existing Item 8 geometry captures.
Each decoded chunk stream and run record is hash-bound to its committed archive
manifest, whose hash matches the restore receipt. Runtime/configuration preflight
identities match the frozen baseline. This is an index of existing saved starts,
not a new world decode, archive restore, or assertion that all archived blocks
have been consumed. Full-envelope chunk coverage is a prerequisite for block
inspection, not proof of correct room topology or complete authored assembly.

The current deterministic intake is 806,285 bytes, SHA-256
`1f2f117214c1daa9d20a48f08e855405be63db86ee192e4b20f242869be46873`.
The second inspection took 27.817 seconds and observed 42,485,305,344 free bytes.
The [intake](intake.json) retains per-world census identities and per-family root,
dimension and baseline/control counts, plus prior capture references and exact
saved-envelope chunk denominators. To avoid duplicating the raw streams, it keeps
one best-coverage reference per root/dimension, breaking coverage ties by full
start status then original manifest/line order. This is an availability index,
not selection on gameplay quality or the final sampling matrix.

There are 357 registry roots within the 192 included canonical families. Of those
families, 73 have at least one accepted Item 10 occurrence in any arm/dimension;
119 have none. Among those 119, Item 8's separate geometry captures contain starts
for 49. Thirteen have at least one candidate with full saved chunk coverage of its
envelope; the other 36 have only incomplete-envelope candidates. For example,
Integrated Stronghold is missing 143 envelope chunks in its existing capture,
and WDA Foundry's best indexed candidate is missing 75. These gaps cannot be
closed with the previously accepted piece-envelope measurement.

The common Item 7 world-bounds disposition is integrated below; root presence
is not full material-variant coverage. Absence in a finite frame
is not insignificance or generation failure. Controls remain separate from baseline.

The complete inclusion/exclusion record cites the exact existing family rationale,
ambiguity, dimension evidence and variant record. It does not change Item 9 roles.
The conservative supplement covers smaller built interiors, vertical/arena cases
and hostile variants of mixed settlements that could otherwise be incorrectly
excluded. Ordinary single caches, isolated huts, environmental formations and
civilian venues without an established dungeon variant remain outside dungeon
sampling. Source evidence, rather than observed frequency, controls inclusion.

## Smallest complete deliverable and definition of done

One protocol, one complete family/variant coverage record, one sample-level raw
observation set and its deterministic reproduction logic, and one authoritative
report with per-family judgments. Reuse existing raw custody and tooling. Add new
world custody only for an actual additional experiment, with an immutable archive,
manifest, durable delivery and tested restore through the existing path.

Done requires every included family and material variant to have an adequate
sample or a resolved, evidence-supported inapplicability disposition. Every
requirement above must have a result under the authorized method; unknowns are
retained and cannot conceal missing required work. Validate playable topology on
the representative before scaling, retain failures and conditional conclusions,
record model identities/inputs, and provide explicit uncertainty. Run affected
checks, the full applicable final gate and a manual result-surface review. Push
coherent milestones, obtain a completed clean Codex PR review with thumbs-up,
resolve findings, merge and verify fetched main before COMPLETE. No Item 14 work.

## Reproduction

Executed from repository root with the locked environment:

```sh
uv run --no-sync python -m evidence.item-13.intake --output /tmp/item13-intake-v2-compact.json
```

The output must be absent. Compare the result with the committed intake.json. For comparison in a clean tracked export, run there
with the documented Item 10 raw restore layout, then compare intake.json bytes.
The local operational timing/free-space line varies and is not part of that file.
The same accepted census can be reused without repeating upstream measurements.

Initial read-only jq probes incorrectly treated keyed census strata as an array;
they failed without changing inputs. Initial lint found formatting, unused names
and a missing annotation in the intake script; those are corrected before delivery.
No server experiment has run. The first representative now has geometric and
modeled quality results, as recorded below.

## Common Item 7 coverage disposition

Direct inspection of the existing Item 8 world-bounds record resolves the remaining
common-index check for families absent from Item 10. The exact references below
address `observations[index]` in `evidence/item-8/sources/world-bounds.json.gz`.
Its input list binds the original decoded streams to the Item 7 core archive.

| Family | Existing observation indexes | Disposition |
| --- | --- | --- |
| adorabuild_structures:prison | 200, 597 | Both start chunks non-full; not adequate topology evidence |
| betterjungletemples:jungle_temple | 372, 752 | Both non-full; use the separately indexed Item 8 capture instead |
| idas:apothecary_abode | 261, 650 | Both non-full; separate Item 8 candidates also have incomplete envelopes |
| mes:starlight_voyager | 242, 632 | Both full starts; all four envelope chunks are full in each original stream; candidates for block inspection |
| mss:leaf_hollow | 96, 499 | Both start chunks non-full; not adequate topology evidence |
| mvs:mine_with_campsite | 94, 497 | Both non-full; separate Item 8 candidates also have incomplete envelopes |
| towns_and_towers:ocean_outpost | 63, 466 | Both start chunks non-full; not adequate topology evidence |

No other family absent from Item 10 has an observation index in its accepted
Item 8 `world_observations` field. This is a direct keyed inventory inspection,
not a new population audit. It adds one family with complete-envelope candidates
to the thirteen from the separate Item 8 captures. Consequently 105 of the 119
Item 10-absent families lack a complete-envelope candidate in these start-based
references. The non-registry central-End input below must also be considered
before declaring a new experiment necessary. Some have partial saved starts; do not replace that distinction with
an assertion of no evidence. All 14 candidates still require hash-verified block
inspection and material-variant assessment. No new world experiment has run.

For Starlight Voyager, both decoded lines are 7848. The envelope is
`[1752,122,64,1767,145,95]`, so the required chunk coordinates are X 109 and 110,
Z 4 and 5. Each appears as `full=true` in the corresponding hash-verified stream:

- `run-a/ocean-heavy/chunks.jsonl`, SHA-256
  `5fcf9c91553eedcef7b454c4aa29f1be88e4af69f28a4d8c22031cde740f33f9`.
- `run-b/ocean-heavy/chunks.jsonl`, SHA-256
  `dc2889d8325e17330e5eef765376b5ba205b256be478b4acfbd49070d5d537e4`.

Those exact inputs were read from the restored core target in
`evidence/item-7/archive/r14/core-restore.json`. This is an explicit derivation
from four immutable chunk records per stream. A new validator or rerun is not
needed to establish it. Identical coordinates across these repeated worlds do
not imply independent layouts, semantic determinism or player observations.

## Representative quality results

The [small-dungeon report](pilot/report.md) integrates every required quality
dimension for two natural samples of `betterdungeons:small_dungeon`. Both are
validated single chambers with no separate finale. Exact blocks, manual topology
coding, conditional routes, nominal combat inputs and deterministic results are
retained together. Extraction and reproduction pass the declared resource bounds.
Human times, realized encounters and generated/acquired loot remain NOT MEASURED.

This establishes the compact representative path only. It does not resolve the
remaining family/variant sampling matrix or authorize broad processing. Full
coverage still requires every one of 192 included families and their material
variants, including dimensions and missing generated-world evidence. No Item 14
work has started.

## Non-registry variants and reference correction

Variant mapping exposed a concrete intake-link defect: slash-containing family IDs
were not JSON Pointer escaped, and non-registry families do not have the referenced
`grouping_decision` field. The producer now escapes keys and points non-registry
rows to their existing contribution records. Exactly 50 references changed across
448 rows. Every resulting pointer was directly resolved against the accepted
inventory; all other intake fields compare equal. This correction does not reopen
classification or change the 192/256 inclusion decision. The reproduced intake
ran in 42.010 seconds with 41,945,993,216 free bytes. Earlier intake bytes remain
in Git. No new evidence schema or validator was needed.

These three included non-registry families require explicit feature/lifecycle
handling, not invented registry IDs. Their existing contribution records establish
the following variant scope before dependent measurements:

| Family | Material design scope and dimension | Generated evidence disposition |
| --- | --- | --- |
| `betterend:shadow_forest_mansion` | End, one `biome/shadow_forest/small_mansion.nbt` design, nominal 17x24x16. Offset -1 with OBJECT terrain merging; rotation/mirroring and terrain interaction remain placement conditions. No second authored design is listed | No exact saved candidate identified by the start census. A feature-specific saved-block search or a narrowly declared placement is needed before topology claims |
| `yungsextras:swamp_church` | Overworld, one `swamp/misc/swamp_church` design, nominal 13x13x5. Four corner support checks, randomized masonry/stair processing and downward support columns require generated validation. Candle color alone is not a separate dungeon design | No exact saved candidate identified. Ordinary root `/place structure` is inapplicable; preserve the configured-feature invocation and support conditions if an additional experiment is required |
| `betterendisland:dragon_arena` | End lifecycle assembly. Initial versus respawn guarded/broken pillar states; indices 1 through 9 with index 9 reused in the ten-spike layout. Full initial/broken podium versus bottom-only, and active/inactive portal states materially affect access and objective state. Pillars are components, not 27 additional dungeon families | Existing central-End raw world must be inspected before requesting new generation. Initial-state source intent does not prove podium placement, dragon state or respawn variant coverage |

Sources: `inventory.json#/non_registry_content/contributions/` keys
`betterend:biome_buildings` (`designs/betterend:shadow_forest_mansion`),
`yungsextras:feature_entrypoints` (family `yungsextras:swamp_church` and
`swamp_generation`), and `betterendisland:platform_gateway`
(`spike_podium_generators`). These are the accepted Item 8 records and their bound
source references, not new player observations. Remaining families still need
material-variant mapping; these rows do not predeclare a full experiment matrix.

The existing [central-End projection](../item-8/world-observations/central-end/README.md)
is hash-verified at `10836fec936f904a0fedaf38304b7f0e4aabeb747433d8b176a861d346202730`.
Its 64 chunk rows, X/Z -4 through 3, are all `minecraft:full`, each retaining section
counts for Y 0 through 15. This is available saved coverage around the source spike
ring, separate from the structure-start index. Exact block positions, podium
location and lifecycle state are not retained in that projection and must be read
from its existing Item 7 hash-verified world. Therefore 105 is a start-index gap
count, not proof that 105 new worlds or placements are necessary.
