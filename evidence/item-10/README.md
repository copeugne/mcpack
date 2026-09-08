# Item 10 baseline density

Status: IN PROGRESS, 2026-09-08.
The [fresh registry diagnostic](pilot-r1/README.md) measured 24 starts in 3,969
full Overworld chunks and reproduced exactly from restored raw evidence. This
is a limited diagnostic, not the full baseline. No tuning has been performed.
The separately requested player servers generated operational smoke-test worlds.
The [sampling protocol](protocol.md) is under reassessment. The user rejected
long recorded play and the proposed combat logger. No human workload is scheduled.
The static census remains the primary deliverable; the Item 5 combat contract
conflict must be resolved explicitly, not hidden by a proxy or a shorter session.

## Verified dependencies and delivery

Fetched main is `edd1dcf9f210097934b17aaa0e054d954077feb4`.
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
The rejected Item 10 session proposal does not supersede that contract.
[protocol.md](protocol.md) records the unresolved scope conflict. `combat_encounters_per_1000_chunks` explicitly
requires ground-truthed combat encounters. A hostility label or spawner count
cannot replace that metric. Proper dungeons are Tier 2+ and major expeditions
Tier 3+ in this protocol; report exclusive tiers separately to avoid ambiguity.

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
   Integrate the required ground-truthed encounter evidence under Item 5.
4. Finish Sparse Structures attribution, final analysis, archive restore and
   clean-checkout reproduction. Push the coherent milestones, open the main PR,
   complete Codex review/fix cycles, merge and verify delivered main.
5. Audit Items 2 through 10 for identity and narrative consistency. Do not touch
   Item 11 workflows. Its two-blind-human requirement remains separate.

The proposed spatial method uses the reconstructed nested rectangles, with
dimension results kept separate. Reuse Item 7's Overworld, Nether, central End
and outer End strata; expansion must prevent overlap between the End strata.
Count each non-INVALID start once by dimension, registry ID and authoritative
start chunk. Validate every target slot at `minecraft:full` with matching saved
coordinates. Do not use generated halo chunks to inflate target denominators.
Map starts to existing canonical families without changing their classification.

Report category numerators and denominators by seed and dimension; biome
comparisons must use an explicitly matched biome exposure denominator.
Use horizontal start-anchor nearest neighbors, censoring distances whose search
circle crosses the sampled boundary. Retain coincident distinct starts.
Use fixed spatial cells for count dispersion and empty-cell fraction, and
report the largest fully observed empty area with its boundary limitations.
Freeze cell sizes, biome sampling height and uncertainty resampling units before
looking at new density results. These choices are still pending, not hidden defaults.

Done means every Item 10 bullet has a measured result or a specification-approved
disposition, source-bound deterministic processing, retained raw evidence with
hashes and tested restore, explicit uncertainty and failure dispositions, clean
final review, merged delivery and the subsequent cross-item audit. A static
proxy cannot close observed combat density under the current requirements.

## Resource estimate and unresolved gates

Read-only host inspection on 2026-09-08 found 1.8 GiB free on the 465 GiB
persistent workspace filesystem. `/tmp` is a 13 GiB RAM-backed filesystem with
about 11 GiB free; it is not durable evidence storage. Available RAM was about
8.7 GiB with 11 GiB swap already used. Those are initial observations, not current
capacity. Authorized duplicate cleanup and player-client setup subsequently left
about 15 GiB free. See [operational setup](server-setup/README.md). The [pilot](pilot-r1/README.md) now supplies measured generation and storage
costs. Recheck free space and RAM before each experiment.

The [r14 run-a world manifest](../item-7/archive/r14/run-a-worlds-manifest.json)
records 484,774,742 raw bytes and 291,011,199 compressed bytes for four seeds.
Its protocol selects `4 * (3969 + 961 + 961 + 961) = 27,408` chunks.
The ratio, 17,687 bytes per selected chunk, includes generated halo data and is
only a planning proxy. A conservative scenario retaining three repetitions over
four seeds and four strata at 32,768 chunks is 1,572,864 selected chunks.
Linear extrapolation gives 25.9 GiB raw, or 67.4 GiB for original, compressed
archive and a simultaneous restore, before runtimes, logs, decoded data or a
Sparse Structures control. This is not a measured Item 10 storage requirement.
Sequential custody may lower peak use; the pilot must measure actual costs.

Eight original run receipts, individually rehashed against the r14 core
manifest, report 228.205 to 332.567 seconds per 6,852 selected chunks on their
original host. Linear scaling of the scenario above is 14.6 to 21.2 hours,
excluding extra passes, analysis, restoration and controls. Different current
host pressure makes this an estimate, not a promised completion time.
The original Item 5 observation matrix implies 60 runs and 75 server-hours,
before discarded warm-up replicates. The user rejected both that burden and the
subsequent proposed recorded-play approach. No replacement human schedule or
methodology amendment is accepted. Resolve the specific contract conflict.

Material pending inputs:

- Bound peak experiment storage to current capacity with verified sequential
  custody, or obtain another persistent location. The authorized duplicate
  cleanup is complete; it does not authorize removing additional artifacts.
- Resolve the combat metric and methodology conflict without assuming a
  recorded-play workload or silently substituting static hostility.
- Complete the nonregistry occurrence method and Sparse Structures attribution
  design using existing evidence. No new generic framework is justified yet.

No implementation should expand around unresolved measurement semantics.
The next work is protocol resolution, not configuration tuning or Item 11.

[Decoder preparation validation](decoder.md) records the custom-dimension
identification fix and validated authoritative-start-coordinate extraction.
