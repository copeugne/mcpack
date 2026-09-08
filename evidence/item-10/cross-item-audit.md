# Items 2 through 10 identity and narrative consistency audit

Date: 2026-09-08. Audited delivery: `d507573ead2c2740657129e9ee57a1410f420ed9`
(fetched main after PR35). Result: **PASS locally with the explicit snapshot
erratum below; review and main delivery of this audit remain pending.**
Item 10 itself is COMPLETE through the reviewed main delivery recorded in its
[report](README.md#reviewed-main-delivery). No Item 11 workflow was implemented,
run, repaired or linted during this audit.

## Scope and method

This is a consistency audit of accepted identities, requirements, evidence
boundaries and delivery records. It reuses the completed Items 2 through 10
results. It does not repeat Item 8 discovery, Item 9 classification, world
collection, runtime admission or history consolidation. No new schema, validator,
archive revision or measurement framework is needed.

Direct inspection compared the item reports and their cited machine-readable
inputs. SHA-256 inspection matched the input table below. Each Item 7 protocol
reference was compared with the referenced file's bytes. Every one of the
sixteen accepted and two failed Item 10 `run.json` preflights was compared with
those same retained-manifest, configuration-manifest, configuration-audit and
seed-suite hashes, Java build, declared instrument count and arm. All eighteen
agree. These are inspections of existing immutable records, not replacement
empirical measurements. Earlier review/restore/test records retain their original
scope; this audit does not claim to have rerun them.

## Item-by-item disposition

| Item | Evidence inspected | Identity and narrative disposition |
| --- | --- | --- |
| 2 | [Platform report](../../docs/items/Item-2-Frozen-Technical-Baseline.md), [execution record](../item-2/baseline-execution-record.json) | Zero third-party mods is the pristine platform control, not the retained gameplay set. Minecraft 1.21.1, NeoForge 21.1.249, Temurin 21.0.12.1+1-LTS and construction heap `-Xms1G -Xmx4G` agree with later controls. Its proof seed is explicitly separate from the later four-seed suite. No client or capacity approval is inferred. |
| 3 | [Admission report](../../docs/items/Item-3-Exact-Version-and-Dependency-Audit.md), [final matrix](../item-3/final-compatibility-matrix.json), [retained manifest](../item-3/runtime/retained-server-candidates.txt) | 190 audited candidates, 136 retained and 54 disabled/quarantined are different populations. Chunky and Spark are `disabled_not_required_on_server`, not retained gameplay dependencies. Later instrumentation is explicitly separate. Excluded runtime failures remain excluded; no admission change is needed. |
| 4 | [Environment closure](../../docs/items/Item-4-Controlled-Test-Environment-Closure.md), [runtime record](../item-4/runtime-validation.json), [seed suite](../../test-environment/seed-suite.json) | The 136-JAR environment and four seed values agree. Isolation, lifecycle and backup/restore are bounded proofs, not terrain, gameplay or load-capacity acceptance. The preserved watchdog attempt remains a failed historical attempt. |
| 5 | [Methodology closure](../../docs/items/Item-5-Measurement-Methodology-Closure.md), [accepted pilot](../item-5/pilots/accepted.json), [scope amendment](methodology-amendment.md) | The 137-JAR Spark pilot is an explicit 136+1 instrumented runtime. Its short capture and dirty source state are limitations, not a performance baseline. PR22 supersedes the human-session/player-case matrix for automated Items 10/11 only. The original protocol and accepted/rejected pilots remain unchanged; no 75-hour human workload is required for Item 10. |
| 6 | [Configuration report](../../docs/items/Item-6-Baseline-Configuration-Audit.md), [manifest](../item-6/generated-config-manifest.json), [audit snapshot](../item-6/config-audit.json), [materialization](../item-6/materialization.json) | 228 frozen paths and their exact configuration identity agree. One credential sentinel is documented sanitization, not tuning. The Chunky status label is corrected below; absence of a Chunky config does not prove it was installed. Actual runtime/configuration identities are unaffected. |
| 7 | [Worldgen report](../../docs/items/Item-7-Baseline-Worldgen-Audit.md), [protocol](../item-7/protocol/worldgen-audit-v1.json), [completion](../item-7/completion.json) | Exact Item 6 and seed identities agree. Its 54,816 selected chunks are its own sample, not Item 10's denominator. Chunky is an explicit generation instrument. Semantic nondeterminism, confirmed Better Caves failure, warning unknowns and limited provider observations remain stated. The missing final clean GitHub review is the explicit user continuation exception recorded in ledger section 5.7, not an inferred review. |
| 8 | [Accepted inventory and delivery](../item-8/README.md), [inventory](../item-8/inventory.json) | The accepted population remains 448 active canonical families: 408 registry and 40 nonregistry. Eighteen other groups, 887 runtime roots and 136 providers are separate counts. PR18/19 delivery and the unchanged inventory hash are retained. Item 10 location grouping does not create new canonical families or count every component as a family. |
| 9 | [Classification and rubric](../item-9/README.md), [classification](../item-9/classification.md) | The exact completed 448-family classification is reused unchanged. C/T1/T2/T3/T4 are provisional source-supported categories. Item 10 uses exclusive T2/T3, separate T4 and the declared overlapping comparison groups. A T1 site is not necessarily a fight; village membership is not a new exclusive tier. |
| 10 | [Complete result](README.md), [protocol](protocol.md), all eighteen linked attempt reports | Sixteen accepted worlds, eight matched pairs, 176 strata and 720,896 full selected chunks are complete. Both failed control attempts remain in the attempt denominator. Controls omit only Sparse Structures. Raw archives/restores, observer identity, exclusions, zeroes, unavailable biomes and censoring remain linked. PR35 has a completed clean review, bot thumbs-up and verified main merge. |

## Exact shared inputs

| Input | Observed SHA-256 |
| --- | --- |
| Item 3 retained manifest | `78e5bdc0697299782a535400ad5b313c088e8db10cfe075085ae4c8a531e30cb` |
| Item 6 configuration manifest | `2e0aaeb0f84747a3cb17146eb435d34cc7d6703b9372211e8fc8cff2df2b436f` |
| Item 6 captured audit snapshot | `181e0c299f44ded319d93c84f7b983738364b4090286251b00421fa041b989dd` |
| Item 4 seed suite | `de5e5e89bd04b6f75dac4eab2e84524956f46faa91660b5315c8eade269d39ae` |
| Item 7 completion | `0ef7c83438ab2a2cfe67eadc858e806ada9c9eecc213d883649ae3e8493cb1d3` |
| Item 8 inventory | `4f7853b7b6531f99d3f0592b2129291d2e0cf24b4ad5d1381b3883dbdcfbc52d` |
| Item 9 classification | `dc78d81691401bad9fc646f1fe790b14bbf1341f595db5e6cbec9a4f1111b710` |
| Preserved Item 5 protocol | `96e6e373886a1f2e5d470801b04345d2c2f82fa64d72dff3fe49a9fc7c0d93e0` |

The Item 2 and Item 6 records pin the same Temurin archive
`ce79869e1307ed8ee1e2baa86a412b1eb5b75d10a01006d788a6f968bcfaee94`.
All eighteen Item 10 preflights bind retained-runtime identity
`4062d6179218916c703269f113663b1e078adebbf6d43a691e692d972e07ac50`.
Baseline+Chunky is 137 JARs, identity
`e2dab4c80cff137d747bd035588882797f85fa8d4d5b6ccb98a5d717fa0749c8`;
omit-Sparse+Chunky is 136, identity
`84a884f99e4ac48defb9ea0b2c9e45bf3d0f4f6e881a4be4d8968dc2be14d4da`.
Chunky 1.4.23 is pinned separately at
`d72f235cf1f56f2c374f52c00bdda5034524b28142305a84cfc123a3f92ad274`.
All eighteen observer source/JAR pairs match the frozen protocol:
`b07ebcacb9043ee7d1fb187a7d93e5b788d890ccd8edc3decc07060609a74396` /
`d2051d5d5eb38aeda3dfc5c1d61d11ebf2e18a1fb3222ac46c12863556c5a782`.
The older Spark pilot's different runtime hash is expected and explicitly bound
in its receipt; it is not an Item 10 runtime.

## Conflicts, corrections and reopened claims

1. **Item 6 Chunky attribution: reopened and resolved.** The captured audit's
   `systems` entry named `Chunky` says `retained-but-no-config-generated`. The
   retained manifest excludes Chunky and Item 3's exact candidate row says
   `disabled_not_required_on_server`. Current disposition is **not retained;
   no configuration generated in Item 6**. The empty file list is correct.
   The [Item 6 report erratum](../../docs/items/Item-6-Baseline-Configuration-Audit.md#post-item-10-snapshot-erratum)
   explicitly supersedes that erroneous label. The captured machine-readable
   snapshot remains immutable because downstream receipts bind its original hash;
   its old label is a preserved error, not an active membership claim. Membership
   must come from the unchanged Item 3 manifest/matrix. Actual Item 6 materialization
   and Item 7/10 instrument counts agree, so no world or configuration rerun is
   required. The affected attribution and downstream consistency gate are resolved.
2. **Item 10 inspection-command dimensions: corrected.** The optional PR35 trace
   verification command listed `ad_astra` names instead of the actual
   `creatingspace` dimensions. The sampler and accepted censuses already used
   the correct identities. The command now imports the existing
   `ITEM10_SELECTIONS` rather than copying names. Re-execution passed all sixteen
   archive-bound traces with the same attempt and 41-Scarecrow counts. This changes
   neither the collector nor measurements; no planet-dimension attempt had been
   accepted through the incorrect namespace list.
3. **Status and historical narrative: reconciled.** The ledger's Item 10
   IN PROGRESS/reconstruction instructions are superseded by the completed PR35
   result. Item 5's old session matrix is versioned history under PR22, not an
   active Item 10 gate. The Item 7 review exception remains explicit. Old closure
   statements about next items describe their completion-time checkpoint; current
   continuation is in the ledger and active handoff. Lost historical Item 10 raw
   evidence has not been recreated from summaries or counted as current data.

The ocean-heavy control heap failure and Aether save failure are additional
bounded failure observations. Item 3 approves admission/lifecycle only; Item 4
approves environment/restore; Item 6 approves untuned configuration capture;
Item 7 explicitly rejects a clean-worldgen or deterministic-stack conclusion.
Thus the new failures do not contradict those accepted claims. Their causes and
production implications are not silently resolved by a successful third attempt.
The save diagnostic identifies Aether `LargeAercloudChunk.addAdditionalSaveData`
and `ConcurrentModificationException`; the exact mutating thread remains UNKNOWN.
No general stability, acceptable peak-player capacity, loot correctness, observed
combat, exploration pacing or enjoyment is established by Items 2 through 10.

## Gate and validation

All nine item scopes are reconciled. The one erroneous historical membership
label has an explicit current correction; no unresolved identity conflict requires
new runtime work. No frozen file, inventory family or classification row changed.
The audit uses direct artifact inspection and reviewer judgment, with the already
passing 581-test Item 7/10 review-fix gate retained rather than rerun for prose.
The corrected existing trace-inspection invocation passes all sixteen worlds.
Only documentation, the ledger and this evidence report change in this audit.
Final audit review and main delivery are required before treating this cross-item
gate as durably delivered. Item 11 execution is not part of this task.
