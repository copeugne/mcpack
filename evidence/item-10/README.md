# Item 10 baseline density

Status: IN PROGRESS, 2026-09-08.
The [sampling protocol](protocol.md) is frozen as `item10-full-v1`, with
`item10-observer-coverage-v2`: sixteen fresh worlds covering four seeds, two
repetitions and baseline/control arms. Nine worlds have individual census and
raw-custody acceptance. The [current handoff](../../MCPACK-NEW-SESSION-HANDOFF.md#current-full-sample-block)
links their authoritative records and identifies the active run. Final combined
biome, seed, repetition and spatial synthesis, review, main delivery and the
Items 2 through 10 consistency audit remain incomplete. No tuning was performed.

The [authorized automated scope](methodology-amendment.md) removes human phases
from Items 10 and 11. No playing workload or recording is required. Provisional
encounter-site density is not observed fights or exploration pacing. The Item 5
methodology amendment passed clean review and main delivery through
[PR22](https://github.com/copeugne/mcpack/pull/22). Earlier diagnostics below retain
their original limited scope and cannot substitute for the full sample.

## Verified dependencies and delivery

Initial dependency inspection used main `edd1dcf9f210097934b17aaa0e054d954077feb4`.
PR22 subsequently delivered the preparation to main at `0a1d9f8f6e0df266eb1f9e1080611c648babf2de`.
GitHub metadata confirms PR18, PR19, PR20 and PR21 are MERGED, respectively at
`326979dd2eee7da3f881f1316eb845fb16e8ea6b`,
`be64d458fee3539e5132049d871d1c32ebc3655b`,
`7cbe06c7d8b074fa6121c1143432d28d02996712` and that main commit.
The pushed `3f758cb2114c9e4880e43307e74ca3ddf4df9977` is not a main ancestor;
its single change is the historical archive reference filename.

Items 5 through 9 supply accepted methodology, configuration, worldgen,
inventory and classification. Reuse their evidence, without redoing their gates.
The existing Item 7 missing-final-review exception remains as recorded in the
execution ledger section 5.7. No missing review is inferred to have occurred.

Direct SHA-256 inspection matched these accepted inputs:

| Input | SHA-256 |
| --- | --- |
| `../item-3/runtime/retained-server-candidates.txt` | `78e5bdc0697299782a535400ad5b313c088e8db10cfe075085ae4c8a531e30cb` |
| `../item-6/generated-config-manifest.json` | `2e0aaeb0f84747a3cb17146eb435d34cc7d6703b9372211e8fc8cff2df2b436f` |
| `../item-6/config-audit.json` | `181e0c299f44ded319d93c84f7b983738364b4090286251b00421fa041b989dd` |
| `../../test-environment/seed-suite.json` | `de5e5e89bd04b6f75dac4eab2e84524956f46faa91660b5315c8eade269d39ae` |
| `../item-8/inventory.json` | `4f7853b7b6531f99d3f0592b2129291d2e0cf24b4ad5d1381b3883dbdcfbc52d` |
| `../item-9/classification.md` | `dc78d81691401bad9fc646f1fe790b14bbf1341f595db5e6cbec9a4f1111b710` |

Runtime pins remain Minecraft 1.21.1, NeoForge 21.1.249, Temurin
21.0.12.1+1-LTS, archive SHA-256
`ce79869e1307ed8ee1e2baa86a412b1eb5b75d10a01006d788a6f968bcfaee94`,
and `-Xms1G -Xmx4G`. Item 7's 136-JAR retained runtime digest is
`4062d6179218916c703269f113663b1e078adebbf6d43a691e692d972e07ac50`.
Its hash-verified Chunky overlay uses `Chunky-NeoForge-1.4.23.jar`, SHA-256
`d72f235cf1f56f2c374f52c00bdda5034524b28142305a84cfc123a3f92ad274`;
the instrumented 137-JAR digest is
`e2dab4c80cff137d747bd035588882797f85fa8d4d5b6ccb98a5d717fa0749c8`.
These are accepted source identities, not verification of a new runtime tree.
Each future materialization must verify its actual files and Java executable.

## Available evidence versus missing measurements

The [Item 5 protocol](../../measurement/item5/protocol-v1.json) defines
denominators, repetitions, retained failures and uncertainty. Its original density
contracts use player cases, 900-second warm-up and 3,600-second observations.
The later [authorized amendment](methodology-amendment.md) supersedes those
collection contracts for Items 10 and 11. The original observed-combat metric
remains historical; the active automated metric is provisional encounter-site
density. Exclusive T2 and T3 categories supply proper-dungeon and
major-expedition counts, with T4 objectives reported separately.

The [reconstructed stage geometry](../../measurement/structure-density-v0.1.json)
is a proposal scaffold, not accepted raw evidence. Its four nested rectangles
have 4,096, 8,192, 16,384 and 32,768 chunks per seed, stopping at 30 observations
per category or the ceiling with sparse categories retained. Historical Item 10
counts and its claimed absent Sparse Structures runtime are not reusable results.

The accepted [Item 7 protocol](../item-7/protocol/worldgen-audit-v1.json), r14
archives, Anvil/NBT decoder, frozen-config materializer and archive/restore tools
are reusable. Its selections and targeted provider-gap observations were designed
for worldgen inspection, not Item 10's density stopping rule. They can inform
cost and methods, but cannot be silently relabeled as new Item 10 experiments.
The old density counter accepts a caller-supplied denominator and has no spatial
analysis; it cannot establish Item 10's exit gate as written.

The accepted inventory and classification need integration, not reinvestigation:
448 active canonical families, comprising 408 registry and 40 nonregistry
families. The latter have empty `structure_ids`; saved structure-start counting
cannot observe them. Their existing provider evidence must determine a separate
occurrence method before claiming all-family location or encounter density.
Pieces, references, pools and aliases must not become additional starts.

Sparse Structures is present in the retained manifest, artifact SHA-256
`5aca0b33c0c83154810bbdd8ddc0d3e6a3e4591577274e2d27c10de0b45f2a45`.
Its [untouched configuration](../item-6/frozen/config/sparsestructures.json5)
has `spreadFactor: 2`, `idBasedSalt: true` and a mansion override of 2.
These facts resolve presence and configured intent only. Actual composition,
affected placements and contribution to observed distribution remain unmeasured.
Do not infer a fourfold density reduction or a zero contribution.

Direct reuse of the accepted disassemblies resolves the mutation mechanism.
The three disassembly files below were hash-checked against
[existing identities](../item-8/sources/sparsestructures-provider/identities.json)
on 2026-09-08. Their parent is
`../item-8/sources/sparsestructures-provider/sparsestructures-neoforge-1.21.1-3.0.jar/`:

- `io.github.maxencedc.sparsestructures.mixin.MakeStructuresSparse.txt`,
  `loadElementFromResource` offsets 0 to 59: only resource-loaded
  `worldgen/structure_set` JSON enters this path; `minecraft:concentric_rings`
  returns before any change. Offsets 100 to 202 multiply present spacing and
  separation by the selected factor, truncate to Java integers, and repair
  separation greater than or equal to spacing by setting spacing to at least 1
  and separation to spacing minus 1. Missing fields initially use 1. This is
  a JSON-load intervention, not evidence that every runtime-generated placement
  traverses it.
- `io.github.maxencedc.sparsestructures.SparseStructuresConfig.txt`,
  `getSpreadFactor` offsets 0 to 116: the first custom entry matching the set ID
  or any member structure replaces the global factor. It does not multiply the
  global factor. The mansion override of 2 therefore remains 2, not 4.
- `io.github.maxencedc.sparsestructures.mixin.MakeStructuresSparse.txt`,
  offsets 205 to 235, and `io.github.maxencedc.sparsestructures.IdBasedSalt.txt`,
  `getSalt` offsets 0 to 10: enabled ID-based salt replaces the salt with Java
  `Math.abs(setId.hashCode()) % 2147483647`. Reproduction must preserve Java
  signed-integer behavior, not substitute a Python hash or unsigned hash.

Consequently, a factor-1 configuration with ID-based salt still enabled would
not isolate the mod's total contribution. No such control has been run. The
smallest sufficient next attribution step is to bind loaded placement values to
these source rules and the actual sampled starts. If a causal difference in
realized counts is required beyond that attribution, it needs a separately
predeclared matched control that isolates both interventions. Do not label a
candidate-grid prediction, source derivation or cross-biome comparison as that
unmeasured causal difference. This establishes the mechanism only; observed
whole-stack contribution remains unresolved.

The accepted [dimension capture](../item-8/runtime/dimension-r3/dimension-biomes.json)
also contains Aether and CreatingSpace dimensions. The draft four-stratum
scenario below omits those and is not a complete sampling frame. Reuse each
family's existing dimension eligibility and nonregistry provider evidence to
include relevant strata or give an explicit supported out-of-population
reason. Do not infer zero occurrences from an unmeasured dimension.

## Exit-gate reassessment (2026-09-08)

The user paused new experiments and PR creation and directed one consolidated
remaining Item 10 delivery after the existing reviews. SPECS Item 10 requires
representative regions across the four selected seeds, all declared category
densities, category distances, clustering, empty regions, biome/seed comparisons
and Sparse Structures attribution. Identity, complete denominators, retained raw
observations, failure/censoring/uncertainty, deterministic processing, durable
restore, review/merge and the subsequent Items 2 through 10 audit remain required.

Natural positive capture for every generator is not a specification requirement.
The separate positive-pilot gates were implementation choices. Their failed or
unmet outcomes remain unchanged, but they do not require further searches for
positive examples before the full fixed sample. What is required is evidence that
every applicable occurrence mechanism is observable, preserves behavior and is
attributed correctly. A completed trace with correctly installed hooks can record
no calls; a failed hook, unavailable event stream or unhandled failure cannot be
reported as zero. Corroborate representative actual writes when observed. Do not
invent a positive example, extrapolate from static density or erase uncertainty.

| Remaining requirement | Why existing evidence is insufficient | Smallest remaining work |
| --- | --- | --- |
| Complete occurrence observation | Registry starts omit the 40 accepted nonregistry families. Existing hooks and source records cover many mechanisms, but procedural pillars, BetterEnd post-template effects and applicable End routes are not fully integrated. | Finish only the missing writer boundaries in the existing observer. Integrate accepted lifecycle applicability and report lifecycle observations separately; the specification does not require a new campaign to trigger every possible lifecycle event. |
| Accepted location numerators | Traces contain block writes, template parts, failed attempts and halo activity. Their totals are not distinct selected-area locations. | Implement the existing family join, occurrence identity/inclusion and last-write/anchor interpretation in the existing processing path. Preserve zeroes, refusals and uncertainty. |
| Full comparative measurements | The small pilots are not the declared four-seed, two-arm sample. Existing static analysis works for registry pilots but does not supply the missing populations or matched control. | Freeze the complete collector/control identities and sampling protocol, run the full sample, then apply deterministic category/spatial/biome analysis. |
| Sparse Structures contribution | Packaged placement rules explain a mechanism but are not the matched observed distribution. | Materialize the exact omit-only-Sparse-Structures control and retain matched repetitions without claiming observer-free causal certainty. |
| Storage, final report and delivery | Current capacity cannot hold full collection. No complete result or cross-item audit exists. | Resolve storage, retain and restore raw evidence, write the complete report, finish the existing PR33/34 obligations, then use one remaining delivery PR with coherent intermediate commits and the required audit. |

The 4,096 chunks per stratum, two repetitions and 16 total worlds are
sampling-design choices, not numbers mandated by SPECS. They are retained in
the frozen `item10-full-v1` protocol; this reassessment does not reduce the measurement scope.
No additional tiny per-generator pilots, new evidence framework or tooling-only
PR is authorized by this reassessment. Synthetic preservation checks and immutable
source inspection address collector correctness; the full declared sample supplies
the missing measurement. Existing diagnostics and their limitations remain intact.

The implementation portion of the table above is now integrated: the existing
collector covers the remaining writers, the reader joins actual locations and
saved biomes, and the runner materializes the exact Sparse Structures control.
The [frozen observer gate](protocol.md#frozen-observer-and-full-trace-gate) pins
source/JAR identity and requires all 50 incoming classes for full analysis.
All 535 Item 7/10 tests passed in 152.60 seconds. Storage and prior reviews are
resolved. The next missing evidence is the first full ordinary baseline world,
including actual installed hooks, saved-chunk coverage, custody and measured
resource use. These runtime acceptance results cannot be inferred from tests.

### Storage decision before collection

The current check reports 3,949,314,048 free bytes (about 3.7 GiB). The existing
r3-based estimate is 10.71 generation hours and 13.50 GiB of original worlds.
As a second retained proxy, the [fairy world backup](fairy-run-r1/world-backup.json)
has 127,859,839 world bytes; its [raw manifest](fairy-run-r1/archive-manifest.json)
has 81,693,301 raw member bytes and a 76,943,807-byte archive for 6,852 selected chunks. Scaling by
720,896 / 6,852 gives 12.53 GiB of original worlds, or 56.14 GiB if every original,
raw copy, archive, downloaded archive, restored raw tree and restored world is
kept locally. Those are planning proxies, not measured full-collector costs.

Avoid retaining redundant new verification workspaces indefinitely. Plan roughly
30 GiB of persistent free space for original worlds, one local raw archive set,
published redundant copies and sequential verification workspace, with the first
complete ordinary-seed run confirming actual cost before continuing. Remove only
new explicitly temporary download/restore copies after successful verification;
all preexisting evidence, worlds, backups and protected artifacts remain intact.
The user has been asked for a persistent location or additional free space.
Full collection is paused until the storage decision and capacity check resolve.

## Smallest complete deliverable and batches

1. Resolve measurement semantics and storage, then freeze the Item 10 protocol
   before collection. Record exact geometry, population, dimension strata,
   occurrence rules, endpoints, repetitions and Sparse Structures attribution.
2. Complete one ordinary-seed stage end to end: fresh verified materialization,
   generation, marker-correlated flush, clean stop, offline slot verification,
   raw preservation and deterministic category/spatial analysis. Preserve any
   failure without silently replacing it. Use this to validate costs and method.
3. Apply the frozen stages across all four seeds. Retain every denominator,
   failure, missing slot, invalid start, nonregistry limitation and sparse result.
   Apply the authorized automated category definitions; do not claim observed fights.
4. Finish Sparse Structures attribution, final analysis, archive restore and
   clean-checkout reproduction. Push the coherent milestones, open the main PR,
   complete Codex review/fix cycles, merge and verify delivered main.
5. Audit Items 2 through 10 for identity and narrative consistency. Do not touch
   Item 11 workflows before the audit. Neither item requires human sessions.

The [protocol](protocol.md) selects one fixed 4,096-chunk rectangle in each of
four seeds and eleven strata, with two fresh repetitions in each of two arms.
It defines coordinate inclusion, spatial cells, biome attribution, boundary
censoring, sparse-category limits and a control omitting only Sparse Structures.
This supersedes the inherited nested-stage draft. Full collection remains gated
on complete occurrence capture and exact experiment identities; no full-frame
results are accepted yet.

Done means every Item 10 bullet has a measured result or a specification-approved
disposition, source-bound deterministic processing, retained raw evidence with
hashes and tested restore, explicit uncertainty and failure dispositions, clean
final review, merged delivery and the subsequent cross-item audit. The authorized
scope does not require observed combat or human sessions in Items 10 or 11.

## Resource estimate and unresolved gates

Use the [protocol resource estimate](protocol.md#runtime-and-storage-estimate)
as the current planning authority: 720,896 selected chunks across 16 worlds,
about 11.05 automated generation hours and 13.92 GiB cumulative uncompressed
world data, using the measured r3 proxy and including the requested generation
edge outside the census. Sequential custody has a provisional
5 GiB workspace floor that still needs collector-specific validation. Recheck
capacity before each experiment; these are estimates, not promised runtimes.
The human collection matrix is superseded by the delivered
[methodology amendment](methodology-amendment.md).

Material pending inputs:

- Bound peak experiment storage to current capacity with verified sequential
  custody, or obtain another persistent location. The authorized duplicate
  cleanup is complete; it does not authorize removing additional artifacts.
- Keep provisional encounter-site counts separate from unobserved fights under
  the reviewed, delivered automated methodology amendment.
- Complete the nonregistry occurrence method and validate the selected Sparse
  Structures control using existing evidence. No new generic framework is justified yet.

No implementation should expand around unresolved measurement semantics.
The next work is protocol resolution, not configuration tuning or Item 11.

[Decoder preparation validation](decoder.md) records the custom-dimension
identification fix and validated authoritative-start-coordinate extraction.
