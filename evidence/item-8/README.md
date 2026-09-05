# Item 8 evidence plan

Status: IN PROGRESS. No family count or completion claim is accepted yet.

Current working inventory regenerated at `4b1e33a`, SHA-256
`759e4b2149d0fb7e2b33b8a06d9152a7c90983035761979c7e50f936379fc6dc`.
All 887 registered roots are assigned once in 421 working groups. This is not
the final accepted canonical family count. The dimension field now joins each
root's biome constraints to captured live dimension memberships. Three unresolved
IDAS constraints stay unknown, and nine roots have no overlap. Remaining family
attributes, provider reconciliation and the final review/delivery gate are open.

## Historical increments

The working deliverable is `inventory.json`, initially assembled by `f2eaf2b`
and updated through `fd9705a` using attribute support from `bf153ea`.
SHA-256: `83f56c9ecaa8f76f853ffd0081a12537849489e4a30dea3edae099caf298250d`.
It is explicitly incomplete. It joins Better Mineshafts, CTOV size groups,
WDA layouts, Seven Seas vessels, Integrated Stronghold, Integrated Villages design groups
and Explorations families
to biome constraints, potential template content
and saved-world observation references. It lists every unassigned registry ID
and keeps unresolved attributes marked `UNKNOWN`. CTOV's broader design
relationships and non-registry content remain unresolved. These rows are not
an accepted canonical total or a substitute for completing each attribute.

The complete registry capture now has durable raw custody, delivered through
`63cb1f8`. See `raw-custody/README.md` for the published archive and verified
downloaded restore. This resolves registry raw retention, not the remaining
inventory, gameplay-attribute or review requirements.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-reproduction1.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-reproduction1.json
```

The committed-source reproduction matched its pilot byte for byte. Three
focused grouping/assembly tests and scoped quality checks passed. The generated
inventory is isolated as the specification's required machine deliverable, not
a new evidence framework. Source hashes bind all five existing inputs. Content
references preserve packaged-versus-effective limitations, and saved piece
envelopes are not promoted to physical dimensions. Continue resolving groups and
attributes in this deliverable before replacing the obsolete narrative report.

Better Mineshafts now records source-supported hostile-room intent, authored
cave-spider and zombie-villager spawners, the base abandoned-mineshaft loot
constant, authored versus natural spawning distinctions, and its underground
generation setup. Each claim identifies its generation classes and limitations;
the decision binds the preserved disassembly identities and frozen config hash.
This does not resolve effective loot injections, physical dimensions or actual
surface visibility. The updated committed-source output reproduced
`evidence/raw/item8/inventory-mineshaft-attributes-pilot1.json` byte for byte at
`evidence/raw/item8/inventory-mineshaft-attributes-reproduction1.json`.
Three focused tests and scoped quality checks passed. Attribute updates cannot
overwrite completion status, family membership or observation references.

Source `eef10dd` assigns all five registered WDA Seven Seas vessel designs:
Corsair Corvette, Pirate Junk, Small Yacht, Unicorn Galleon and Victory Frigate.
Each has its own start pool and main hull template. Subordinate spawner pools
and templates remain components, not additional families. The source-supported
hostile encounter intent is recorded, while effective attributes remain open.
The existing trace retains Small Yacht's missing
`dungeons_arise_seven_seas:small_yacht/small_yacht_spawner_3` reference; no absent
template is invented. Four focused grouping/assembly checks passed. Output
`evidence/raw/item8/inventory-seven-seas-r1.json` reproduced byte for byte at
`evidence/raw/item8/inventory-seven-seas-reproduction1.json`.

Source `7100c21` adds the five vessels' main template extents, authored spawner
entity types, container loot references and ocean-surface generation setup.
These extents include stored air and are not assembled occupied dimensions.
Effective loot injections, observed spawner counts and visual discoverability
remain unresolved. The direct source checks caught an omitted skeleton entry
for Victory Frigate during preparation; the corrected list matches both initial
spawner data and positive-weight potentials. All four focused tests passed.
The committed-source output at
`evidence/raw/item8/inventory-seven-seas-attributes-reproduction1.json` matches
`evidence/raw/item8/inventory-seven-seas-attributes-pilot1.json` byte for byte.
Missing-template source inspection is preserved separately in
`sources/missing-template-code`. The base Minecraft lookup creates an empty
template with no attachment connectors. This is not a deliberate empty-pool
element or an observed miss probability; mod transformations and effective
placement remain to be resolved.

Source `93d526c` adds Integrated Stronghold as one family rooted at its fountain
pool. The connected room pools remain components. Its piece-bound natural
monster-spawn override names silverfish and endermen, and its packaged start
height has both absolute endpoints at Y=15. These settings do not establish
encounter counts or final surface exposure. Two missing armory templates remain
explicit, along with unresolved authored content and replacement relationships.
Five focused tests and scoped Ruff and basedpyright checks passed. Output
`evidence/raw/item8/inventory-integrated-stronghold-reproduction1.json` reproduced
`evidence/raw/item8/inventory-integrated-stronghold-pilot1.json` byte for byte.

Source `585de70` enumerates all twelve registered Integrated Villages designs
with distinct start pools. Connected buildings, paths and inhabitants remain
components, including shared components. Broader village-family relationships
remain open. Minka's declared Quark dependency, Pirate Village's target biome
and radius, height settings and missing pool/template references are preserved.
Six focused tests and scoped quality checks passed. The generated inventory
increment is isolated because the required per-family biome and template joins
produce substantial repeated source references. No unrelated source changes are
included. Committed-source output
`evidence/raw/item8/inventory-integrated-villages-reproduction1.json` matches
`evidence/raw/item8/inventory-integrated-villages-pilot1.json` byte for byte.

WDA grouping decisions are delivered in four increments: `559edc0`, `d20b0c6`,
`007d1f9` and `6540055`. All forty registered WDA roots are assigned once, with
distinct start pools and disjoint reachable template sets. Rooms, decorations
and spawners remain components. The source-bound test verifies these distinctions,
exact registry coverage, placement settings and missing references. Seven focused
tests and scoped quality checks passed. Effective placement and the remaining
gameplay attributes are not inferred from root coverage.

The resulting per-family biome and template joins are isolated in a generated
inventory increment because these required references account for its size.
No implementation changes are included with that output. Committed-source output
`evidence/raw/item8/inventory-wda-reproduction1.json` matches
`evidence/raw/item8/inventory-wda-pilot1.json` byte for byte.

Source `a590403` adds distinct packaged loot field/value references and their
source templates to the existing loot-source field. Original NBT paths remain
in `sources/pool-traces-content.json.gz`. Container and death-loot fields remain
separate, and list-valued trial-spawner references are preserved. This is source
attribution, not a generated loot count, successful table resolution or effective
loot-injection result. Existing explicit family attribute decisions remain intact.
Eight focused tests and scoped quality checks passed. The output at
`evidence/raw/item8/inventory-loot-summary-reproduction1.json` reproduced
`evidence/raw/item8/inventory-loot-summary-pilot1.json` byte for byte.
The more verbose `136ee84` pilot and reproduction were rejected for unnecessary
duplication of raw paths; they are not the current inventory. This generated
increment contains the required loot-source attribution and its documentation.

Source `729ccdd` similarly attributes authored entity base IDs to their source
templates, including passengers and non-mob entities. Unresolved entity records
remain explicit. Spawner contents, generation markers, processors, natural
spawning and actual hostility require their separate dispositions; an empty
authored-entity summary is not evidence of an empty encounter. Existing explicit
family attribute decisions remain intact. Eight focused tests and scoped quality
checks passed, including duplicate-entity, passenger and missing-ID cases.
`evidence/raw/item8/inventory-authored-entities-reproduction1.json` reproduced
`evidence/raw/item8/inventory-authored-entities-pilot1.json` byte for byte.

Sources `3b4f770` and `2f1dbda` add explicit spawner base-entity attribution.
Ordinary, trial-current, normal and ominous sources remain separate. Only
positive-weight potentials contribute entity IDs. Missing IDs/configurations,
invalid weights and custom-spawner semantics remain unresolved with source
paths. Generation-marker templates remain separate from parsed spawner sources.
This does not infer default entities, passenger populations, spawned counts or
effective processor behavior. Sixteen focused parser/assembly tests and scoped
quality checks passed. The output at
`evidence/raw/item8/inventory-spawners-reproduction1.json` reproduced
`evidence/raw/item8/inventory-spawners-pilot1.json` byte for byte.

Source `fd9705a` covers all ten registered Explorations roots. Alternate campsite,
ruin and log templates remain components or variants. Slime Cave has no declared
start pool and retains its custom-generation gap. Underground Temple retains two
missing templates. Nine focused grouping/assembly tests and scoped quality checks
passed. Committed-source output
`evidence/raw/item8/inventory-explorations-reproduction1.json` reproduced
`evidence/raw/item8/inventory-explorations-pilot1.json` byte for byte. The generated
join is isolated from implementation changes and does not close the remaining
family attributes or custom-generation questions.

The infrastructure requirements in
`INFRASTRUCTURE-INSTALLATION-AND-SERVER-TESTING.md` apply to this work. Reuse the
existing host-discovery and platform doctor, pinned acquisition/materialization,
configuration capture, and lifecycle primitives. Record each new run's source
revision. Invoke pinned Java directly, check port availability, preserve full
logs and failures, and keep operational inputs out of committed evidence.

## Required proof and boundaries

The complete inventory covers every gameplay-relevant structure family in the
retained 136-JAR stack, including every provider named in SPECS.md Item 8 and
vanilla content. Runtime structure IDs are variants, not automatically families.
Canonical grouping must cite a shared gameplay identity and preserve all member
IDs. Pools, pieces, templates, aliases, replacement structures, injected village
buildings, and feature-based structures receive explicit relationships and are
not silently omitted or counted as independent structures.

Every family must record dimension, biome constraints, approximate footprint and
vertical size, intended hostility, mob source, loot source, generated spawners,
authored versus natural enemies, visual discoverability, and surface/underground
classification. Each claim cites its source and distinguishes observed values,
packaged intent, derivation, and unresolved limitations. Registration does not
prove placement, template size does not prove assembled footprint, and a missing
observation does not prove absence.

## Smallest evidence set

1. One fresh ordinary-seed runtime under the frozen Item 6 configuration, using
   the existing retained-136 materializer and NeoForge's built-in registry dump
   command. Capture structures, structure sets, template pools, configured and
   placed features, biomes, and dimension types. Preserve command responses,
   runtime identities, configuration parity, correlated flush, and clean stop.
2. A deterministic extraction from all hash-verified retained JARs and pinned
   vanilla/NeoForge data. Preserve resource ownership, competing definitions,
   placement and pool relationships, relevant template NBT, loot references,
   spawners, and authored entities. Resolve effective availability against the
   runtime dumps and configuration, not ZIP traversal order.
3. Reuse accepted Item 7 generated-world observations under their existing r14
   identities. Bind derived family observations to those retained sources.
   Collect additional targeted evidence only for a specific unresolved required
   attribute or provider; do not rerun the Item 7 survey or claim density.
4. One canonical machine inventory, its source-bound verification, and a matching
   narrative report. Preserve exact provider and family coverage, unresolved
   cases, failures, and differences from the obsolete zero-mod report.

## Frozen dependencies

- Minecraft 1.21.1, NeoForge 21.1.249, Temurin 21.0.12.1+1-LTS.
- Retained manifest: `evidence/item-3/runtime/retained-server-candidates.txt`,
  SHA-256 `78e5bdc0697299782a535400ad5b313c088e8db10cfe075085ae4c8a531e30cb`.
- Item 6 manifest: `evidence/item-6/generated-config-manifest.json`,
  SHA-256 `2e0aaeb0f84747a3cb17146eb435d34cc7d6703b9372211e8fc8cff2df2b436f`.
- Item 6 audit: `evidence/item-6/config-audit.json`,
  SHA-256 `181e0c299f44ded319d93c84f7b983738364b4090286251b00421fa041b989dd`.
- Item 7 completion: `evidence/item-7/completion.json`,
  SHA-256 `0ef7c83438ab2a2cfe67eadc858e806ada9c9eecc213d883649ae3e8493cb1d3`.
- Item 7 raw release: `item-7-raw-evidence-2026-09-04-r14`.

Preserve Item 7 nondeterminism, Better Caves failure, IDAS missing biome tags,
unresolved YUNG Bridges/Extras identities, and unresolved diagnostics. No tuning,
candidate readmission, tier assignment, or Item 9 through 11 execution is allowed.

## Validation and delivery

Validate required fields and exact coverage against the actual source universe,
all referenced identities, canonical grouping, and deterministic output. Focused
tests must exercise omissions, double counting, conflicting sources, and the
runtime lifecycle boundaries actually used. Inspect the human-facing inventory
for meaningful source-supported descriptions. Run affected quality checks once
the increment passes. Commit and push independently verifiable increments.

Open the Item 8 PR promptly when the local specification gate passes. Request
`@codex review`, inspect the completed cycle and all findings, fix valid findings
in separate commits, and request review again after fixes. Verify a completed
clean review covering the final changes and the required thumbs-up reaction.
Merge without squashing and verify the accepted head in fetched `origin/main`.
The Item 7 user exception does not waive any Item 8 review or evidence gate.

### Nether bridge and fungus grouping increments

The bridge source increment is `70196ea`; the fungus source increment is
`a49dbc8`. Each decision preserves variant membership, definitions and template
sizes. Reproduce their focused source checks with:

```sh
uv run pytest tests/item8/test_family_decisions.py -q
```

Executed inventory commands at their corresponding source revisions:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-bridge-70196ea.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-bridge-70196ea-repro.json
cmp evidence/raw/item8/inventory-bridge-70196ea.json evidence/raw/item8/inventory-bridge-70196ea-repro.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-fungus-a49dbc8.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-fungus-a49dbc8-repro.json
cmp evidence/raw/item8/inventory-fungus-a49dbc8.json evidence/raw/item8/inventory-fungus-a49dbc8-repro.json
```

Use fresh output names when reproducing; the builder refuses overwrites.
The bridge join is `d635337`; the fungus join is `541acfa`. Neither is an
Item 8 completion claim. Effective custom placement and gameplay attributes
remain unresolved.

Nether well source increment `d320686` is checked by the same focused test
command above. Its generated join is `2cb05ba`. Reproduction at that revision:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-well-d320686.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-well-d320686-repro.json
cmp evidence/raw/item8/inventory-well-d320686.json evidence/raw/item8/inventory-well-d320686-repro.json
```

Circular ruin source increment `2ba75aa` uses the existing Nether variant test.
Generated join `d62ade9` reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-circle-2ba75aa.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-circle-2ba75aa-repro.json
cmp evidence/raw/item8/inventory-circle-2ba75aa.json evidence/raw/item8/inventory-circle-2ba75aa-repro.json
```

Medium house source `298911d` and generated join `8d778dc` used:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-medium-house-298911d.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-medium-house-298911d-repro.json
cmp evidence/raw/item8/inventory-medium-house-298911d.json evidence/raw/item8/inventory-medium-house-298911d-repro.json
```

Nether generator source `37e0c78` and evidence `d3e8c20` used:

```sh
uv run -m tools.inspect_item8_pool_elements --archive moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar --output evidence/raw/item8/moog-nether-code-pilot1
uv run -m tools.inspect_item8_pool_elements --archive moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar --output evidence/item-8/sources/moog-nether-generator-code
diff -qr evidence/raw/item8/moog-nether-code-pilot1 evidence/item-8/sources/moog-nether-generator-code
```

Use new output paths when reproducing. The generator's `postLayoutAdjustments`
selects fixed height or terrain utility results and moves the assembled pieces.
The called terrain utilities and inherited layout path remain necessary to
resolve effective placement. This is source evidence, not a completed runtime
placement claim.

Observed geometry source `62be1ff` and generated evidence `be1171c` use the
existing world-bounds artifact. Reproduction:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-geometry-62be1ff.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-geometry-62be1ff-repro.json
cmp evidence/raw/item8/inventory-geometry-62be1ff.json evidence/raw/item8/inventory-geometry-62be1ff-repro.json
uv run pytest tests/item8/test_family_decisions.py -q
```

Only observations with `chunk_full=true` contribute to the approximate geometry
fields; all original observations remain linked. Values describe saved-piece
layout envelopes including air/padding, not occupied blocks, complete component
population or family-wide size limits. Explicit family assessments override
the generic estimates. Missing suitable observations remain unknown.

Ruin-fragment reconciliation (`61d6501`, joined in `0f500c9`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-ruins-61d6501.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-ruins-61d6501-repro.json
cmp evidence/raw/item8/inventory-ruins-61d6501.json evidence/raw/item8/inventory-ruins-61d6501-repro.json
```

The remaining Nether roots (`5640516`, joined in `d278fc7`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-nether-5640516.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-nether-5640516-repro.json
cmp evidence/raw/item8/inventory-nether-5640516.json evidence/raw/item8/inventory-nether-5640516-repro.json
```

The existing family-decision tests check all 52 mns registry entries exactly once
and bind the remaining roots to their packaged settings and missing-component
lists. Family relationships and effective gameplay attributes remain provisional.

Voyager log piles and lanterns (`12d4090`, joined in `4396e1f`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-voyager-12d4090.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-voyager-12d4090-repro.json
cmp evidence/raw/item8/inventory-voyager-12d4090.json evidence/raw/item8/inventory-voyager-12d4090-repro.json
```

Voyager dead trees (`0ce48c8`, joined in `7851498`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-dead-tree-0ce48c8.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-dead-tree-0ce48c8-repro.json
cmp evidence/raw/item8/inventory-dead-tree-0ce48c8.json evidence/raw/item8/inventory-dead-tree-0ce48c8-repro.json
uv run pytest tests/item8/test_family_decisions.py -k moog_modular -q
```

The first validation attempt failed the draft assertion that all dead-tree
marker lists were empty (34 passed, 1 failed). Preserved template content shows
SAVE-mode structure blocks in acacia, acacia_trunk and birch. The corrected
rationale and test preserve those markers; both affected cases passed. No raw
template evidence was changed, and effective marker processing remains open.

Voyager stalls and End scraps (`d077750`, joined in `0f0b9e9`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-voyager-d077750.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-voyager-d077750-repro.json
cmp evidence/raw/item8/inventory-voyager-d077750.json evidence/raw/item8/inventory-voyager-d077750-repro.json
uv run pytest tests/item8/test_family_decisions.py -q
```

All 37 focused tests passed. Scoped Ruff and basedpyright checks passed.
The eight roots form two working groups; their template loot references remain
attributed to the corresponding variants. Neither has retained world
observations. Existing catalogs and checks suffice for this grouping increment;
no additional measurement system was introduced. Required effective gameplay
attributes and final inventory completeness remain unresolved.

Voyager living trees (`7389ff9`, joined in `a85bc74`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-trees-7389ff9.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-trees-7389ff9-repro.json
cmp evidence/raw/item8/inventory-trees-7389ff9.json evidence/raw/item8/inventory-trees-7389ff9-repro.json
uv run pytest tests/item8/test_family_decisions.py -q
```

All 38 focused tests and scoped Ruff/basedpyright checks passed. Nine roots
retain their full definitions and fifteen alternative template dimensions.
The direct source check binds the approximate footprint and height lists to
those dimensions and preserves big oak's exceptional loot and terrain checks.
These are packaged envelopes, including padding and air, not measurements of
occupied blocks. The two retained world observations remain linked separately.

Voyager wells (`c4646fc`, joined in `4f36c29`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-wells-c4646fc.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-wells-c4646fc-repro.json
cmp evidence/raw/item8/inventory-wells-c4646fc.json evidence/raw/item8/inventory-wells-c4646fc-repro.json
uv run pytest tests/item8/test_family_decisions.py -q
```

All 39 focused tests and scoped Ruff/basedpyright checks passed. The existing
Voyager tree test now also checks wells, preserving full definitions, template
dimensions and exact loot references. Seventeen roots form one working family;
twenty templates include components and alternatives. Twelve retained world
observations remain linked. Existing observed-envelope estimates supply the
qualified geometry fields without adding component heights or introducing a
measurement system. Effective gameplay attributes remain unresolved.

Voyager carts and igloos (`631cb1a`, joined in `925a781`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-carts-631cb1a.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-carts-631cb1a-repro.json
cmp evidence/raw/item8/inventory-carts-631cb1a.json evidence/raw/item8/inventory-carts-631cb1a-repro.json
uv run pytest tests/item8/test_family_decisions.py -q
```

All 40 focused tests and scoped Ruff/basedpyright checks passed. The direct
source check binds six complete definitions, ten unique reachable templates,
authored entity IDs, SAVE markers, loot references and the small igloo's stray
spawner. Shared villager templates remain components. Four cart observations
are linked; no retained igloo observations exist. Effective populations and
marker/loot processing remain unresolved. No new measurement system was added.

Remaining Voyager roots (`f4fdcc2`, joined in `dd2c364`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-voyager-f4fdcc2.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-voyager-f4fdcc2-repro.json
cmp evidence/raw/item8/inventory-voyager-f4fdcc2.json evidence/raw/item8/inventory-voyager-f4fdcc2-repro.json
uv run pytest tests/item8/test_family_decisions.py -q
```

All 41 focused tests and scoped Ruff/basedpyright checks passed. The existing
root/settings test now verifies all 129 Voyager registry IDs exactly once,
including prior variant groups. The 64 new working root assignments retain
complete generation settings, missing-component lists and joined content.
All prior family records remain unchanged. The large generated increment is
isolated from its source decisions and documentation; expanded biome lists
and shared component attribution account for most of its size. Canonical
relationships and effective gameplay attributes remain open. In particular,
cathedral loot references `minecraft:mvs/cathedral_common` and two empty explicit
spawner IDs in the large warped tower remain visible for disposition.

Repurposed witch huts (`c5f5dd6`, joined in `fa401f2`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-witch-c5f5dd6.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-witch-c5f5dd6-repro.json
cmp evidence/raw/item8/inventory-witch-c5f5dd6.json evidence/raw/item8/inventory-witch-c5f5dd6-repro.json
uv run pytest tests/item8/test_family_decisions.py -q
```

All 42 focused tests and scoped Ruff/basedpyright checks passed. The reused
variant test checks six matching definitions, template dimensions, authored
witch/cat entities and absent loot/spawner/marker records. Packaged dimensions
and hostile intent are recorded with limitations. There are no retained world
observations for this family; generated population and effective processing
remain unresolved. No new measurement system was introduced.

Remaining Repurposed designs (`5022316`, joined in `0555981`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-repurposed-5022316.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-repurposed-5022316-repro.json
cmp evidence/raw/item8/inventory-repurposed-5022316.json evidence/raw/item8/inventory-repurposed-5022316-repro.json
uv run pytest tests/item8/test_family_decisions.py -q
```

All 43 focused tests and scoped Ruff/basedpyright checks passed. The direct
provider check verifies 107 distinct registry entries in 17 design groups,
complete variant definitions, nonempty direct pool traces without missing
components, and twelve explicitly untraced mansion/monument paths. The latter
are not converted into empty-content claims. Sixteen added groups join the
remaining 101 roots; the earlier witch-hut group and all other prior families
remain unchanged. Effective attributes and final canonical acceptance remain
unresolved. No additional measurement system was needed.

CTOV outposts (`07bcde5`, joined in `c5c8c7a`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-outposts-07bcde5.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-outposts-07bcde5-repro.json
cmp evidence/raw/item8/inventory-outposts-07bcde5.json evidence/raw/item8/inventory-outposts-07bcde5-repro.json
uv run pytest tests/item8/test_family_decisions.py -q
```

All 44 focused tests and scoped Ruff/basedpyright checks passed. The direct
outpost check verifies the common definition and each variant's biome, size,
start pool and missing-component list, the exact badlands/mesa duplicate, and
complete distinct assignment of all 78 CTOV registry IDs. Existing village
size checks remain intact. No retained outpost observations exist. Missing
components are preserved rather than silently corrected or counted as families.

Towns & Towers (`2177cc2`, joined in `a0c9c6e`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-towns-2177cc2.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-towns-2177cc2-repro.json
cmp evidence/raw/item8/inventory-towns-2177cc2.json evidence/raw/item8/inventory-towns-2177cc2-repro.json
uv run pytest tests/item8/test_family_decisions.py -q
```

All 45 focused tests and scoped Ruff/basedpyright checks passed. The provider
check binds all 60 registry roots exactly once to eight working groups, complete
variant definitions, `kaisyn` start pools, template traces and exact missing
component lists. Nested exclusive resource paths are preserved. Prior family
records are unchanged. Ocean and desert-mimic observations are linked; outpost
fort/tower/camp and general village groups have no retained observations.
Missing resources, effective attributes and final canonical reconciliation
remain open. No additional measurement system was needed.

IDAS (`1a65a9e`, joined in `60e419b`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-idas-1a65a9e.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-idas-1a65a9e-repro.json
cmp evidence/raw/item8/inventory-idas-1a65a9e.json evidence/raw/item8/inventory-idas-1a65a9e-repro.json
uv run pytest tests/item8/test_family_decisions.py -q
```

All 46 focused tests and scoped Ruff/basedpyright checks passed. The existing
provider check now also verifies 84 distinct IDAS registry roots across 62
working groups, full variant definitions and exact missing-component lists.
Nested optional-mod identifiers remain intact. Dependencies and adaptive pool
switches are preserved without claiming that declared start-pool traces cover
the effective replacement. The first lint attempt caught pytest parameter-name
formatting; it was corrected before the successful checks. A JSON key-order
rewrite was rejected during diff inspection and removed before committing;
prior decisions and generated family records remain unchanged. The generated
join is isolated because it expands existing biome, template and observation
attribution for the whole provider. No new measurement system was introduced.

AdoraBuild (`306e678`, joined in `d0ad289`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-adora-306e678.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-adora-306e678-repro.json
cmp evidence/raw/item8/inventory-adora-306e678.json evidence/raw/item8/inventory-adora-306e678-repro.json
uv run pytest tests/item8/test_family_decisions.py -q
```

All 47 focused tests and scoped Ruff/basedpyright checks passed. The existing
provider check now binds 106 distinct AdoraBuild roots across 31 working groups,
full definitions and missing-component lists. Material and size variants remain
explicit without increasing the family count for each root. The generated join
is isolated from its source decisions. Prior family records are unchanged.
World observations exist for basalt chambers, houses, Nether fortresses and
prisons. Custom generator behavior, effective attributes and final canonical
reconciliation remain open. No new measurement system was needed.

Terralith (`7b386d2`, joined in `0c06094`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-terralith-7b386d2.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-terralith-7b386d2-repro.json
cmp evidence/raw/item8/inventory-terralith-7b386d2.json evidence/raw/item8/inventory-terralith-7b386d2-repro.json
uv run pytest tests/item8/test_family_decisions.py -q
```

All 48 focused tests and scoped Ruff/basedpyright checks passed. The reused
provider check binds 28 distinct roots in 16 working groups, full definitions,
start-pool families and exact missing-component lists. Cabin and witch-hut
shared designs retain both registry identities and their different definitions.
The underground-prefixed witch hut has an empty resolved biome set and surface
heightmap projection. No retained Terralith structure observations exist.
The generated increment is isolated, and prior family records remain unchanged.
Effective attributes and final canonical reconciliation remain open.

Illager Invasion (`63df576`, joined in `d30900f`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-illagers-63df576.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-illagers-63df576-repro.json
cmp evidence/raw/item8/inventory-illagers-63df576.json evidence/raw/item8/inventory-illagers-63df576-repro.json
uv run pytest tests/item8/test_family_decisions.py -q
```

All 50 focused family tests passed, including explicit hostile-component attribution.
Scoped Ruff/basedpyright checks passed. The output is byte-identical across two
builds and all previous family records are unchanged. This uses existing
registry, packaged, configuration and world-observation sources.

Creating Space (`b08ad94`, joined in `fe209a5`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-space-b08ad94.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-space-b08ad94-repro.json
cmp evidence/raw/item8/inventory-space-b08ad94.json evidence/raw/item8/inventory-space-b08ad94-repro.json
uv run pytest tests/item8/test_family_decisions.py -q
```

All 51 focused family tests passed, including full nested root definitions.
Scoped Ruff/basedpyright checks passed. The output is byte-identical across two
builds and all previous family records are unchanged. This uses existing
registry, packaged, configuration and world-observation sources.

Supplementaries (`1c77ad2`, joined in `9111d69`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-supplementaries-1c77ad2.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-supplementaries-1c77ad2-repro.json
cmp evidence/raw/item8/inventory-supplementaries-1c77ad2.json evidence/raw/item8/inventory-supplementaries-1c77ad2-repro.json
uv run pytest tests/item8/test_family_decisions.py -q -k provider_groups
```

All seven affected provider cases passed; 45 unaffected cases were deselected.
Scoped Ruff/basedpyright checks passed. The output is byte-identical across two
builds and all previous family records are unchanged. This uses existing
registry, packaged, configuration and world-observation sources.

Illager hostile intent is bound to packaged entity components without claiming
live selection or population. Space outposts retain reused vanilla legs as
components. Supplementaries binds frozen common/toggle configs and custom
spawn-box definitions; its markers are not ordinary block spawners. The initial
Supplementaries lint failure reported test complexity 11 above limit 10; an
unnecessary conditional on an existing shared-catalog assertion was removed
without removing that assertion. Road signs have observations 374, 407, 754
and 787. The other ten roots added in these increments have none. Custom
generation and remaining effective attributes are unresolved.

Aether and Deep Aether (`d883abe`, joined in `b006a3f`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-aether-d883abe.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-aether-d883abe-repro.json
cmp evidence/raw/item8/inventory-aether-d883abe.json evidence/raw/item8/inventory-aether-d883abe-repro.json
uv run pytest tests/item8/test_family_decisions.py -q -k authored_designs
```

All 17 affected authored-root cases passed; 37 unaffected cases were deselected.
Scoped Ruff/basedpyright checks passed. Both builds are byte-identical and all
previous family records remain unchanged. Custom paths without start pools
remain explicit in the generated content fields, not empty-content claims.

BetterEnd (`664d235`, joined in `8e21c9f`) reproduced with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-betterend-664d235.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-betterend-664d235-repro.json
cmp evidence/raw/item8/inventory-betterend-664d235.json evidence/raw/item8/inventory-betterend-664d235-repro.json
uv run pytest tests/item8/test_family_decisions.py -q -k authored_designs
```

All 18 affected authored-root cases passed; 37 unaffected cases were deselected.
Scoped Ruff/basedpyright checks passed. Both builds are byte-identical and all
previous family records remain unchanged. Custom paths without start pools
remain explicit in the generated content fields, not empty-content claims.

Aether's six unregistered ruined-portal definitions remain in the source
catalog, outside the four registered Aether roots. Deep Aether contributes
three direct-pool designs and one custom brass dungeon. BetterEnd contributes
one traced village and thirteen untraced custom roots; lake and mountain
variant relationships remain open. The village trace retains two missing
templates. Existing BetterEnd observations are linked; none exist for the eight
Aether/Deep Aether roots. Initial Aether lint reported the existing test's
statement count above its limit; identical key-set assignments were combined
without introducing another helper. No new measurement system was needed.

Vanilla and whole-registry assignment (`4ad283f`, joined in `8dd7f9c`):

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-vanilla-4ad283f.json
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-vanilla-4ad283f-repro.json
cmp evidence/raw/item8/inventory-vanilla-4ad283f.json evidence/raw/item8/inventory-vanilla-4ad283f-repro.json
uv run pytest tests/item8/test_family_decisions.py -q -k 'design_groups_cover_registry or all_runtime_structure_ids'
```

Three affected checks passed (54 deselected), together with scoped Ruff and
basedpyright. Full variant definitions bind 34 vanilla roots across 21 groups;
24 roots lack direct pools and remain explicitly untraced. The ancient-city
missing template remains visible. The whole-registry check compares the exact
887-ID set with every assignment and rejects duplicates or omissions. It proves
registry assignment only, not canonical-family or non-registry completeness.
Both builds are byte-identical and all prior family records are unchanged.

Village Taverns' five packaged Lithostitched modifiers expose the next gap:
they add limited delegate elements to vanilla village house pools, while the
current pool trace does not apply modifiers. The existing packaged catalog
retains their exact conditions, target pools and definitions. Closing this
requires modifying the existing trace, not a separate measurement system.

Lithostitched delegate prerequisite (`4fe823b`, evidence `fc6adee`, decoder `06b1ae2`):

```sh
uv run -m tools.inspect_item8_pool_elements --archive lithostitched-1.7.10+beta4-neoforge-21.1.jar --output evidence/item-8/sources/lithostitched-pool-additions-code
uv run pytest tests/item8/test_pool_links.py tests/item8/test_pool_trace.py -q
```

The output directory must be absent when reproducing. All six disassembly
hashes matched their identity records. The existing selector includes three
previously inspected condition/config classes alongside the three new classes.
Thirteen affected tests passed, including retained terminal constraints,
nested unknowns and missing delegates. Scoped Ruff/basedpyright checks passed.
The initial lint findings were explicit regex formatting and the observed-codec
branch count; the existing codec complexity exception was extended narrowly.

This delivers decoding support, not effective modifier application. The pinned
code confirms additions append weighted elements and limited elements delegate
to their wrapped template. Conditions, other applicable modifications and
runtime generation remain unresolved. The accepted pool trace and inventory
are unchanged until that application step is supported and implemented.

## Village Taverns parent-family relationships

The existing modifier and pool evidence now has explicit parent links in each
applicable family decision's village_taverns_templates field. This is component
attribution, not a new family classification or observed placement count.

The packaged catalog contains 26 applicable additions conditioned on
village_taverns: five from Village Taverns and 21 from CTOV. The preserved trace
includes all 26 modifiers. Of their 26 distinct template references, 25 are
reachable from 66 registered roots in 22 current working groups: 60 CTOV roots
in 20 groups, five vanilla village roots in one group, and the IDAS castle root.
The castle reaches the plains tavern through its pool graph, so restricting
attribution to village-named roots would omit a real relationship.

ctov:village/dark_forest/jobsite/tavern is the remaining untraced addition.
Its target ctov:village/halloween/house is registered, but no current structure
trace reaches that template. Preserve it as an included modifier with no traced
parent, not a missing mod, missing pool, generating family or observed failure.
These links do not establish successful placement, full provider completeness,
final CTOV canonical grouping or all non-registry content.

The existing builder preserves these links inside grouping_decision. The
focused family test independently derives the template set from the packaged
modifier definitions, checks selected modifier dispositions and joins the
existing structure traces to every parent assignment. Its assertions are the
tracked reproduction logic for the counts above. No new measurement system,
collector or general relationship framework is introduced.

```sh
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-tavern-relationships.json
```

Decision SHA-256:
`f74b70a63144b337d3483dba03e50a3193bcf82b06eeeb1112d3f6898e7c3236`.

All 63 affected tests passed. Scoped Ruff and Basedpyright passed; the initial
lint finding was one long test line, corrected without changing behavior.

Parent attribution and its test are delivered in `1e7dd7c`. Inventory rebuilt
at that commit with the command above, SHA-256:
`e0fddbb286ce87c8a23285d7af33eac42563db754f8ad833d1826080d4c50327`.
Only grouping-decision attribution/evidence and the decision input hash change.
Family membership, content attributes and world-observation links are preserved.

## CTOV village definition reconciliation (2026-09-05)

All 66 village roots in the existing 22 CTOV working design groups now retain
full packaged definitions and exact missing-component dispositions from the
existing pool traces. Together with the already reconciled 12 outpost roots,
the CTOV assignments cover all 78 runtime structure IDs exactly once. This does
not finalize relationships between village designs or establish provider-wide
non-registry completeness. No family count changes in this increment.

The existing CTOV size-group test independently reconstructs the groups from
packaged definitions, verifies exact runtime coverage, compares every definition
and pool start, and requires the stored missing references to equal the trace.
Missing components remain potential-path defects, not measured generation
failure rates. Tavern component relationships are preserved.

Verification:

```sh
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tools/build_item8_inventory.py tests/item8/test_family_decisions.py
uv run basedpyright tools/build_item8_inventory.py tests/item8/test_family_decisions.py
```

All 63 affected tests and both scoped checks passed. The data increment preserves
all 66 definitions directly rather than introducing another schema or generator;
the existing test verifies the full addition against the preserved catalog and
traces. Decision SHA-256:
`5f49f674fbadd6f86decc6b97623526150ba97b0d919ad8da63e751fe5f392e9`.
Inventory regeneration uses `uv run -m tools.build_item8_inventory --output
evidence/raw/item8/inventory-ctov-definitions.json` and is delivered separately.

Definitions and verification are delivered in `21fdbe0`. Inventory regenerated
at that revision, SHA-256:
`9205723b5e8748e56aeac40190d15365aa2b198a98c79e81ecb37409a0c5112e`.
Only the 22 village grouping decisions and decision input hash change; all
family memberships, other attributes and world-observation links are preserved.

## CTOV content and start-placement attributes (2026-09-05)

The existing 23 CTOV groups now distinguish packaged authored entities from
structure-controlled natural spawning. Resolved village templates contain
civilian, passive or defensive mobs and sometimes display entities, with no
hostile entity IDs. All village definitions declare empty spawn overrides.
Outpost templates include ravagers; their definitions separately override monster
spawns with pillagers, evokers, vindicators and witches. These are potential
sources, not live entity counts or proof of effective runtime replacements.

No spawner blocks or generation markers occur in the resolved reachable CTOV
templates. This does not dispose of missing templates or external generation
hooks. The inventory preserves these limitations rather than treating the
entire provider as proven spawner-free.

All CTOV starts use WORLD_SURFACE_WG projection. Village underground specifies
an absolute start offset of -14; the other designs and outposts specify zero.
Every definition uses surface_structures, demonstrating why generation step
alone does not establish underground/surface placement. These attributes record
start intent, not assembled room elevations, terrain exposure or visibility.

The added case in the existing family-decision test compares every recorded
entity ID, natural override and placement field with preserved sources and
requires empty spawner, marker and unresolved-entity lists for resolved content.
No new extraction or measurement system was needed. The initial focused run
passed all three CTOV tests; type checking then required two explicit JSON casts,
which changed no behavior. Full affected verification uses the three commands
in the preceding CTOV section. Decision SHA-256:
`b67aca5bcab0e5c621f7d5d2a12b72e02a2ab89af1e31847adc7d8d726529032`.

All 64 affected tests and scoped Ruff/Basedpyright checks passed. The inventory
is regenerated separately using:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-ctov-attributes.json
```

Attributes and verification delivered in `f937ea9`. Inventory rebuilt at that
revision, SHA-256:
`f51b1333d6e322ab60f9f7f051958ce683a482bf9c553faafa02efd24d2b7e97`.
Only the affected CTOV attributes/grouping decisions and decision input hash
change. Membership, geometry, loot and world-observation links are preserved.

## CTOV canonical village relationship (2026-09-05)

The 22 CTOV village design groups are consolidated into one `ctov:village`
family, preserving all 66 registry IDs and each named design under
`design_variants`. All exact variant definitions, missing references and tavern
links are retained. CTOV outposts remain a separate hostile family.

The family decision follows shared civilian settlement identity, not a count of
start pools. All village roots use the same Lithostitched jigsaw contract, empty
spawn overrides and civilian template content. Their definitions differ only in
biomes, start pools, expansion size and start height. Fortified, canopy and
underground designs retain their architecture/placement distinctions as variants,
consistent with the vanilla and Towns & Towers village treatment. This is an
Item 8 identity decision, not Item 9 tier assignment or a claim that the variants
have identical layouts, exposure or gameplay experience.

The existing size-relationship test still derives all 22 three-size design groups
from packaged data, now requires them to partition one family, and checks common
definition fields. The content test verifies the combined entity sources and
per-root placement offsets. Tavern coverage still binds the same 66 affected
roots across the stack; their family owners are now CTOV village, vanilla village
and IDAS castle. No templates become independent families.

The working total is now 431 groups for 887 registered roots. Other grouping and
provider questions remain open, so this is not an accepted final count.
Decision SHA-256:
`4d545b2a01ea7d142a4fbd15f7917a836559a6fd48634c04526c44aefedf6483`.

Verification and subsequent inventory regeneration:

```sh
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py tests/item8/test_integrated_suppression.py
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-ctov-family.json
```

All 67 affected tests and scoped checks passed. The smaller decision file
replaces duplicated family attributes with one family and explicit design/root
relationships. Inventory regrouping is delivered separately because it is a
large generated change produced by the existing builder.

Grouping and verification are delivered in `5bb0942`. Inventory regenerated at
that revision, SHA-256:
`21481771b21790e45a616efbef2d7b958fe719302b4bcf4e0dc8683e749760e5`.
The 22 prior CTOV village rows become one, retaining their union of templates,
biome constraints, loot references and saved-start observation indexes. All other
family rows are unchanged. Raw sources and their identities are unchanged.

## MVS rock and pond family reconciliation (2026-09-05)

`mvs:boulder` and `mvs:stone_rock` are retained as two roots of `mvs:rock`.
Their full definitions differ only in start pool. One boulder and six stone-rock
material/shape templates are alternatives of the same rock-landmark family.
Resolved content has no authored entities, loot, spawners or generation markers.

`mvs:mushroom_pond` and `mvs:small_oak_pond` are two roots of `mvs:pond`.
Their definitions likewise differ only in start pool. Each design has upper and
lower components, preserving vegetation/layout differences and distinct
`mvs:mushroom_pond` and `mvs:pond` loot sources. These four templates are components,
not four families. No authored entities, spawners or markers occur in resolved
pond templates. All four roots have no missing or unresolved trace elements.

Exact definitions and template dimensions remain in each variant. This is a
family relationship decision, not proof of occupied/assembled dimensions,
effective natural spawning or discovery. Other MVS relationship questions,
including camps and floating-island designs, are not resolved by this increment.
The working total becomes 429 groups with the same 887 registry roots.

The added two cases in the existing family-decision tests compare definitions,
common fields, pool traces, template identities/sizes, entity/spawner/marker
absence and distinct loot sources directly with preserved catalogs. Existing
MVS coverage requires all 129 roots to remain assigned exactly once. An initial
read-only inspection expected a variants field on singleton rows and stopped
with KeyError; inspecting their actual shape resolved that without changing data.

Decision SHA-256:
`4373ff8a6f7a5429f4f94907dd39a7d9d70a28d841f052c42a400e0f0790c705`.

```sh
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-mvs-formations.json
```

All 66 affected tests passed. Type checking then required an explicit string
parameter on the empty loot set; after that annotation-only fix, both formation
cases and scoped Ruff/Basedpyright checks passed. No source behavior changed.

Grouping delivered in `bdcee2c`; inventory regenerated at that revision, SHA-256:
`151e5afe848e375cfdc7ef42887ec8e43c311250a45882a52645362de1c2e9ed`.
All other family rows are unchanged. The two merged families preserve the union
of their roots, templates, biome constraints and saved-start observation indexes.

## MVS surface camp family reconciliation (2026-09-05)

Campsite, fire camp and horse campsite are three layout/reward variants of
`mvs:campsite`. Each reaches one resolved template with no authored entities,
spawners or generation markers. Horse campsite therefore does not establish an
authored horse source. Fire camp has no loot references; horse campsite uses
`mvs:abandoned`; campsite also uses general and common/uncommon house loot.
These references stay attached to the exact source templates.

The definitions share biome constraints, zero-offset surface projection, empty
spawn overrides and generation type. Full variant definitions preserve different
jigsaw sizes and terrain checks. Mine with campsite remains separate: its lower
mining component contains a spawner and its trace includes shared villager
pieces. Its relationship to the modular MVS mineshaft is still open.

The existing formation-content test now covers the three camp roots and the
mine boundary, comparing full definitions, template sizes, missing references,
authored content and loot sources. All MVS roots remain covered by the existing
129-root uniqueness check. No runtime experiment or additional measurement
system was needed. Working total becomes 427 groups for 887 registered roots.

Decision SHA-256:
`94b18c93ceb35a902f74f791dee0dad8097083bb733544516eadcd097ec3eb64`.

```sh
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-mvs-camps.json
```

All 67 affected tests and scoped Ruff/Basedpyright checks passed. Full variant
records retain the terrain-check differences; no configuration was changed.

Grouping delivered in `aa01ac1`; inventory regenerated at that revision, SHA-256:
`d38983b380fedb771dbe47aefb274e287a9dfa355e37d4b9a617babac68df33e`.
Camp root/template/biome/loot and observation coverage is preserved. The mine
row changes only its grouping rationale; other family rows are unchanged.

## MVS floating-island family reconciliation (2026-09-05)

The two floating-island roots form one `mvs:floating_islands` family. Their full
packaged definitions differ only by start pool: WORLD_SURFACE_WG projection with
an absolute offset of 60, size 1, no terrain adaptation and empty spawn overrides.
The nature layout is a 26 by 19 by 30 template with MVS common/uncommon/rare house
loot and no authored entity. The large-house layout is 26 by 28 by 23 and reaches
three shared villager components. Its loot references shipwreck treasure and
stronghold crossing/library. The villager pieces are components, not families.

All five resolved templates have no spawners or generation markers. Full variant
records retain sizes, definitions and missing-component dispositions. These are
layout and habitation/reward variants of an elevated island family; no claim of
identical encounter value, actual assembled footprint or visual discovery range
is made. The working total becomes 426 groups with 887 registered roots.

The existing related-layout test now verifies this pair's definitions, template
coverage/sizes, per-root authored entity IDs and loot sources. No additional
measurement system or runtime was needed. Mining-family reconciliation remains
open and is not changed by this increment.

Decision SHA-256:
`0139d328e23c57ecb52802819165db0befc25d2b352cf932e5e9f7b01dffcf2d`.

```sh
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-mvs-islands.json
```

All 68 affected tests and scoped Ruff/Basedpyright checks passed. This uses the
existing extraction and inventory paths; raw sources are unchanged.

Grouping delivered in `18ecfe4`; inventory regenerated at that revision, SHA-256:
`87667133ab2560dfa6120872a0023dcf761217e2f81080a631925808fa9d6a34`.
Both roots and their template, biome, loot and observation coverage are retained.
All other family rows are unchanged.

## MVS mining-family relationship and encounter sources (2026-09-05)

Mine with campsite and the modular mineshaft remain separate families. The former
uses one authored site and a lower mining component, plus shared villager
alternatives. The latter assembles entrance, corridor, intersection and stair
pieces, has jigsaw size 17 and an overflow pool allowed outside normal boundaries.
These are different assembly/layout identities, not biome or material substitutions.
Shared villager components and a mining theme do not merge them. This closes the
explicit relationship question without claiming equal or measured difficulty.

Mine with campsite has a skeleton spawner in its lower template and no authored
hostile template entity. The mineshaft has authored bogged, evokers and skeletons,
and spawner NBT selecting bogged, creepers and skeletons. Both include potential
villagers; the mineshaft also contains an armor stand, which is not counted as an
enemy. Both root definitions have empty spawn overrides. Natural spawning remains
conditional on biome/world state. Existing spawner and mob fields retain exact
source-template attribution; two required attributes now record encounter intent
and the authored-versus-natural distinction explicitly.

The existing decoder verifies spawner assignments from preserved NBT. The added
family-decision test checks distinct roots, definition settings, template coverage,
entity IDs and spawner sources; generic singleton checks bind all source fields.
This does not prove effective runtime replacements or count live mobs. Working
family count remains 426; other design/provider and attribute gaps remain open.

Decision SHA-256:
`e0ed25faf9b0f6f8af09d7656d5fafa445287661d34641af2417e89387e21d58`.

```sh
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-mvs-mining.json
```

All 69 affected tests and scoped Ruff/Basedpyright checks passed. No additional
measurement system, runtime or configuration change was required.

Decisions and attributes delivered in `7c1d6c6`; inventory rebuilt at that
revision, SHA-256:
`bf56126ef196c73126ab1da8880b4027c5f8c98b3b2e6331df5ebbc47a182e31`.
Only both mining families' grouping decisions, intended hostility and enemy
attribution change, plus the decision input hash. All other fields are preserved.

## BetterEnd lake-family reconciliation (2026-09-05)

Five registered lake roots now belong to `betterend:end_lake`, with all types,
biome constraints and procedural implementations retained as variants. Normal
and rare lake classes inherit EndLakeStructure and only forward construction and
return their own type. The base generator creates EndLakePiece. Both megalake
classes create LakePiece with different size parameters and terrain checks.
They remain different generation algorithms inside one lake-formation family,
not five independent families merely because five types are registered.

Registration constructor handles are bound through the preserved verbose
EndStructures bootstrap table. The existing family-decision test now checks
those handles, all five packaged definitions, source hashes, inheritance and
piece allocation. BetterEnd coverage also checks all 14 roots exactly once
across singleton and grouped records. No new extraction or runtime is needed.

This family relationship does not establish material composition, mob/loot
absence, effective placement, actual dimensions or frequency. Piece-content
interpretation and remaining attributes stay open. Normal/rare names are not
observed frequency measurements. The working total becomes 422 groups with
887 registered roots. Mountain relationships remain unresolved.

Decision SHA-256:
`55477e77db70a5504032cd850757f77eec038789e41df0a9d126edad54b27692`.
The initial two focused BetterEnd cases passed; lint requested assertion/quote
formatting and one line wrap, corrected without changing behavior.

```sh
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-betterend-lakes.json
```

All 70 affected tests and scoped Ruff/Basedpyright checks passed. The source
capture remains the already delivered `1f7f8fe` increment.

Grouping delivered in `f90d6da`; inventory rebuilt at that revision, SHA-256:
`620b2c61a0890bd4e2e387c4dd4f6e907682c653f752a8835a728eea6133ec2a`.
All lake roots, biome constraints, custom-generation records and saved-start
observation indexes remain represented. Other family rows are unchanged.

## BetterEnd mountain-family reconciliation (2026-09-05)

Ordinary and painted mountains are two variants of `betterend:mountain`, retaining
both registered types, biome restrictions and generator/piece identities.
Both extend FeatureBaseStructure, sample WORLD_SURFACE_WG and create procedural
mountain pieces. Ordinary uses CrystalMountainPiece; painted uses
PaintedMountainPiece and a palette of end stone, flavolite and violecite states.
Their distinct height thresholds, shape parameters and material paths remain
preserved in the source evidence rather than treated as identical generation.

This is one natural terrain-formation identity with shape/material variants.
Raw-generation step and empty spawn overrides do not prove that every piece is
free of entities, loot or spawners. Piece interpretation, actual geometry and
visual discovery remain open. The grouping test now verifies both mountain
registration bootstrap bindings, definitions, inheritance, piece allocation and
painted palette references using the already captured sources. No new extraction,
measurement system or runtime was needed. Working total becomes 421 groups with
887 registered roots; provider-wide completion remains unproven.

Decision SHA-256:
`1def4cbabbfb5bf97e5afa984144424469000aa5bfe891227610dd290b062712`.

```sh
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-betterend-mountains.json
```

All 71 affected tests passed. After wrapping one overlong test assertion, the
three affected BetterEnd cases and scoped Ruff/Basedpyright checks passed.

Grouping delivered in `8ca1e21`; inventory regenerated at that revision, SHA-256:
`d04abd3d02744ce7af0ac2ae286642ceaedca036efa603a9db08122b78280072`.
Both roots and their biome constraints, custom-generation records and saved-start
observation indexes remain represented. Other family rows are unchanged.

## BetterEnd mountain placement and visual cues

The source capture delivered in `01d4f63` supports two required attributes for
both mountain variants. Their root generators select WORLD_SURFACE_WG height,
requiring Y greater than 5 for ordinary mountains and greater than 50 for painted
mountains. Piece code establishes a surface-rooted mountain body and crystals,
or columns with noise-varied stone layers. These authored cues now replace the
undifferentiated UNKNOWN placement and visual fields. Actual visibility distance,
occlusion and discovery probability remain unmeasured.

MountainPiece stores separate radius and height parameters but uses radius for
all bounding-box axes. Existing saved-world envelopes remain unchanged and must
not be relabeled occupied mountain dimensions. Mob, loot and spawner attribution
remain open. No runtime or measurement system was added.

Decision SHA-256:
`87b4d8967824e33e6c8dbdd7dd689654b24d215390f4bbf63c26ccd74a199422`.
Reproduction and validation:

```sh
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run pytest -q tests/item8/test_family_decisions.py -k betterend
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-betterend-mountain-cues.json
```

The initial test extension exceeded the existing lint complexity/statement limits;
it was separated into a focused placement/cue test without a shared abstraction.
Four focused BetterEnd cases and scoped Ruff/Basedpyright checks pass. An initial
read-only inventory inspection assumed families was a list and raised TypeError;
it was corrected to use the existing mapping, with no artifact mutation.

The affected suite passed 71 tests before the test-only split; all four BetterEnd
cases passed afterward. Inventory regenerated at `a485c80`, SHA-256:
`175fd05691be098c8e5904482325772757cdf9185a5017b3d765429e920f67ea`.
Only the mountain grouping evidence and its placement/visual fields changed.
All other families, saved observation links and size envelopes are unchanged.

## BetterEnd mountain direct encounter and loot attribution

The preserved root generators, FeatureBaseStructure, BasePiece, MountainPiece,
CrystalMountainPiece and PaintedMountainPiece support the direct content
attribution. The procedural paths write stone, moss and crystal blocks. They
contain no direct entity creation/insertion, spawner placement, container loot
assignment, template placement or configured/placed-feature delegation. The
family now records environmental intent, no direct authored mobs/spawners or
container tables, and empty structure spawn overrides. Natural spawning,
harvested block drops and external retained-mod injections remain distinct.
This is not a live-world population or spawner count.

The focused test binds the complete seven-class selection and its disassembly
hashes, checks the direct-content references and both empty spawn overrides.
Existing material/palette and constructor-binding tests provide positive source
coverage. No extraction, runtime, measurement system or general validator was
added. The saved-world size and placement/cue attributes remain unchanged.

Decision SHA-256:
`3b9163176c218891042b6caa75b4060a4ec413fa5293079fb1c4ebd3e1c6e727`.

```sh
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-betterend-mountain-content.json
```

Source inspection also identifies an upstream placement condition for subsequent
integration: FeatureBaseStructure.findGenerationPoint rejects its independently
sampled position below Y=10 before invoking the root's generatePieces. The
currently recorded root thresholds do not replace this earlier check. Preserve
both sampling stages when completing placement eligibility; do not infer a
single effective threshold from their different sample positions.

All 73 affected tests and scoped Ruff/Basedpyright passed. Inventory regenerated
at `1ee796e`, SHA-256:
`24e6dfa796602032aedb3e97642453fa92b9ceeace619f70df51797a4b3383aa`.
Only the mountain direct-content attributes and their grouping decision changed.
All other family rows, observation links and geometry envelopes are unchanged.

## BetterEnd mountain base placement precheck

The earlier placement finding is now integrated into the existing mountain
classification field. FeatureBaseStructure.findGenerationPoint requires its
getGenerationHeight result to have Y >= 10 before creating the generation stub.
That helper uses WORLD_SURFACE_WG/getFirstOccupiedHeight. The later root
getBaseHeight samples and their Y > 5 or Y > 50 conditions remain separate.
The two sampling stages must not be collapsed into one threshold at one position.
This closes the demonstrated omission without changing generation or adding tools.

Decision SHA-256:
`2e7648906f19e6052298cc4a999aa591a6694756315cc6a63da0dc3ea9d6a10b`.
The existing placement test binds the parent class, threshold, branch ordering
and height query. All five focused BetterEnd cases and scoped checks pass.

```sh
uv run pytest -q tests/item8/test_family_decisions.py -k betterend
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-betterend-mountain-precheck.json
```

All 73 affected tests and scoped checks passed. Inventory regenerated at
`b52dfa9`, SHA-256:
`e7c1a4fefa8ba492c93cef684994c60509cf8849a44934500d6563d7413fee80`.
Only the mountain placement field and its grouping decision changed.

## BetterEnd lake placement and visual cues

All five lake roots now have source-backed surface/submerged placement and visual
cue records. They inherit the independently sampled base Y >= 10 precheck.
EndLake roots then require their center Y >= 10 and reject cardinal samples with
absolute height difference above 5. Megalakes require center Y > 5 and reject
cardinal samples below center minus 6. Ordinary lake water level uses the minimum
center/neighbor height; megalakes use center height. These conditions are not
frequency measurements, and the two sampling stages remain separate.

Both piece algorithms produce water basins with terrain-derived shore materials.
EndLakePiece has endstone-dust patches; LakePiece can place jungle grass or
umbrella moss on the rim after a survival check. Full biome top-material resolution
and observed visibility remain outside these source-derived cues. Existing size
and world-observation evidence is preserved. No new extraction or runtime needed.

Decision SHA-256:
`b7802248007f4c80faabb18c925d108231ef123c2061aadbf66dde359af4d75c`.

```sh
uv run pytest -q tests/item8/test_family_decisions.py -k betterend
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-betterend-lake-cues.json
```

Six focused BetterEnd tests and scoped Ruff/Basedpyright pass. The lake test binds
both preserved source manifests, both terrain-check algorithms and piece material
references. Existing registration tests bind the five roots and their inheritance.

All 74 affected tests and scoped checks passed. Inventory regenerated at
`8292695`, SHA-256:
`25e78dd6bbe34e3ac2c6ee60c1bda55119ae79772c2f69c6c32fc29270a48247`.
Only lake placement/cues and their grouping decision changed. Other family rows,
size envelopes and world observation links are unchanged.

## BetterEnd lake direct content attribution

The helper capture delivered in `28ed678` completes the direct source set for
this attribution: five root classes, FeatureBaseStructure, BasePiece, both lake
pieces, EndBiome and BlockFixer. No direct entity creation, explicit spawner
configuration or container-loot assignment occurs in these captured classes.
BlockFixer adjusts vegetation/crystals and fluids and schedules fluid ticks.
The five family content/intent fields now record these direct-source facts.

This does not close effective material attribution. EndBiome delegates material
selection to a SurfaceMaterialProvider, and its returned block states and later
block behavior are not fully resolved. The spawner field explicitly preserves
that limitation rather than claiming every dynamic surface state is non-spawner.
Natural spawning, harvested drops and external injections remain distinct.

The existing mountain direct-content test now also covers the eleven lake classes,
using their preserved disassembly hashes and all five empty spawn overrides.
No new validator, extraction, measurement system or runtime was added here.
Seven focused BetterEnd tests and scoped checks pass.

Decision SHA-256:
`96cf175ab478a94d86edbc4c638c96c33b84f9d24ba2aa7d6fa4d01cc0d2914e`.

```sh
uv run pytest -q tests/item8/test_family_decisions.py -k betterend
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-betterend-lake-content.json
```

All 75 affected tests and scoped checks passed. Inventory regenerated at
`a4548bf`, SHA-256:
`65d6dd6270f40edae66a5401a4e3aafe3f3aba5d4adccf9f6703b0dd00c8958f`.
Only lake direct-content fields and their grouping decision changed. Other family
rows, size envelopes, placement/cues and observation links are unchanged.

## YUNG's Bridges non-registry contribution

The existing non_registry_content field now records the verified YUNG's Bridges
feature path instead of leaving all non-registry content as one UNKNOWN string.
This minimal extension is required because the structure-only family groups
cannot represent a provider with no structure registry IDs. It reuses the existing
decision file, pinned inputs, builder and feature-reference tests; no new schema,
validator framework or measurement system is introduced.

The NeoForge bridge_addition modifier targets #yungsbridges:has_structure/bridge
and adds yungsbridges:bridge_list at surface_structures. Its placed feature uses
the configured multiple_attempt_single_random selector, which references 22
configured variants pointing to 11 distinct template IDs. The configured variants
and placed root are in the preserved runtime dumps; no yungsbridges structure ID
is in the structure dump. The Forge-directory duplicate is not another NeoForge
contribution. Stone/wood, intact/broken and axis variants are preserved as related
bridge layouts, not 22 or 11 accepted families.

Configuration, custom placement/generator behavior, template content, generated
observations and final family attributes still need reconciliation. The existing
421 structure-registry groups and 887 roots do not include an accepted bridge
family yet. This is a verified contribution path, not a completion claim.

Decision SHA-256:
`c4f5a9bbf909c60826b9331f13a6c4e92ab86de0b30e02f072325e7fd6f3ec3f`.

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py tests/item8/test_family_decisions.py tests/item8/test_dimension_capture.py
uv run ruff check tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-yungs-bridge-path.json
```

The initial focused test passed; lint then required a top-level import and typed
JSON reads. Those test-only issues were fixed without changing the contribution.
Scoped Ruff/Basedpyright now pass.

All 77 affected tests passed; the bridge test and scoped checks passed after
the test-only typing/import fixes. Inventory regenerated at `6309287`, SHA-256:
`da35ac84a7e3c198fc648088f7001b8cfad29ab311f6e3bf16d84738e0176c97`.
Only non_registry_content and the pinned decision identity changed. All 421
structure-registry family rows remain unchanged.

## YUNG bridge template membership and nominal sizes

The contribution now preserves the eleven selector-referenced template XYZ
sizes, along with three packaged templates absent from that selector:
wood/13_0, wood/13_0_broken and wood/15_0. None is silently dropped or counted as
active solely because it is packaged. All fourteen templates have empty entity
and block-entity lists. Generator transformations and marker-block interpretation
remain open; empty block-entity lists are not proof of effective loot/spawner
absence. Nominal dimensions are template envelopes, not observed occupied bounds.

A focused test binds membership, dimensions and empty lists to the existing
redacted template catalog. No extraction, runtime or measurement system added.
Seven affected feature-reference/inventory-source tests passed. Two overlong test
lines were wrapped; scoped Ruff and Basedpyright pass. Searching the frozen
configuration paths and manifest for a bridge-named file found none; this is not
proof of absent code/configuration controls, which remain to be inspected.

Decision SHA-256:
`ded939c069ee1071dc317bb1426e0def3d0d86f0266433c132ba507afb515900`.

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py tests/item8/test_inventory_sources.py
uv run ruff check tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-yungs-bridge-templates.json
```

Inventory regenerated at `01edbb8`, SHA-256:
`38eb038f5c04562162292988e8d55c407ea6f78cc489cdac8a0c5db9f69d3938`.
Only the bridge contribution and decision identity changed; all 421 registry
family rows and 887 roots remain unchanged.

## YUNG bridge generation ordering and success limitation

The bridge contribution now records the source-bound generation flow: set origin
Y to world sea level; rotate counterclockwise 90 degrees for non-Z-axis variants;
place the template; then execute the twelve recorded custom processors in order.
The selector randomly tries remaining placed-feature candidates, removes failed
candidates and stops at the first successful return or exhaustion. This is not
an observed frequency or pacing result.

AbstractTemplateFeature discards StructureTemplate.placeInWorld's boolean.
BridgeFeature returns true when template loading returned non-null. Accordingly,
feature success alone cannot prove all template blocks were placed. This source
limitation is preserved without modifying the retained mod or treating it as an
observed world failure. Processor effects, support geometry and placement
eligibility remain open. No new extraction or measurement system was added.

Eight affected feature-reference/inventory-source tests passed. After wrapping
one long test line, scoped Ruff and Basedpyright passed.
Decision SHA-256:
`59a6d7d18eb9b560825eeed494b532cfbe5a21426bbfa69817a5b096cbf89bba`.

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py tests/item8/test_inventory_sources.py
uv run ruff check tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-yungs-bridge-generation.json
```

Inventory regenerated at `955936c`, SHA-256:
`05295953bfbab2da42d0ef9f9feac58a4013ab14313718f59c9151fb192e1966`.
Only the decision identity and bridge generation/evidence fields changed.
All 421 registry family rows and 887 roots remain unchanged.

## Bridge support extent

DynamicLegProcessor delegates support markers to the captured interface's
generatePillarDown method. It replaces the marker, then descends at fixed X/Z
through air or liquid while Y > 0. It stops at Y <= 0 or non-air, non-liquid
material. The literal zero boundary is not the world's minimum build height.
Both block-write results are discarded. Nominal template height therefore
describes the body; terrain-dependent supports can extend below it. This records
source intent, not measured successful occupied height. No new source capture
or measurement system is needed.

Reproduce the focused support check and inventory with:

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py tests/item8/test_inventory_sources.py
uv run ruff check tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-yungs-bridge-supports.json
```

Nine affected tests passed. Scoped Ruff and Basedpyright pass after splitting
one compound test assertion. Decision SHA-256:
`f9a58e0977649c0f6d09ade7791561bf46a069d839eadabb0145b4b1b78146cc`.

Inventory regenerated at `733c0cf`, SHA-256:
`5410d6d5ae2e6e5ad584dece89db3396c70c561056de5d9e47545c97fcd3a9e7`.
Only the decision identity and bridge support-geometry field changed. All 421
registry family rows and 887 roots remain unchanged.

## Bridge direct encounter and loot contribution

The fourteen captured processor/module/interface classes contain no direct
entity-spawning, spawner-configuration or container-loot references. Combined
with the existing fourteen-template entity/block-entity check, this supports
the narrowly scoped direct-content fields in the bridge contribution. The
processor calls concern block replacement, support extension and state
adaptation. Environmental infrastructure is a source-based interpretation,
not a safety measurement. Natural mobs, delegated engine/API behavior and
external retained-mod effects are not excluded. No new capture or measurement
system was added.

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py tests/item8/test_inventory_sources.py
uv run ruff check tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-yungs-bridge-encounters.json
```

Ten affected tests passed; scoped Ruff and Basedpyright passed. Decision SHA-256:
`d894507f6a028766e091ede35bb58de28a9489cd5d2a1f51deafe4f7e5642fb4`.

Inventory regenerated at `544d5de`, SHA-256:
`53d49ef90e2b842f8b6321ef74b8fbc1e06537de934201b149c9e00533e0f08e`.
Only the decision identity and direct bridge encounter-content field changed.
All 421 registry family rows and 887 roots remain unchanged.

## Bridge terrain placement

The captured BridgePlacement.getPositions resolves the custom bank/span checks.
It searches candidate positions at sea level minus one and returns the first
accepted position. Both endpoint centers and enough contiguous lateral bank
cells must occlude and have WORLD_SURFACE height no higher than sea level.
The configured span rectangle must be liquid; despite the minWaterZ/maxWaterZ
names, the predicate is not water-specific. The generation step later raises
template origin to sea level. Exact loop ranges and endpoint separation are
recorded in the contribution. This supports surface-crossing placement intent,
not observed visibility or frequency. Biome and rarity filters are separate.

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py tests/item8/test_inventory_sources.py
uv run ruff check tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-yungs-bridge-placement.json
```

Eleven affected tests passed; scoped Ruff and Basedpyright passed. Decision SHA-256:
`c6e3111cd30e6aa12bbb566d0691837fc217fe01ea9979cddecb57c23e016bc6`.

Inventory regenerated at `e8503b5`, SHA-256:
`71f820a7edd7337111c7e8b8a031e0ef11a99babdea3152b440f7a3ccd459ed5`.
Only the decision identity and bridge placement-eligibility field changed.
All 421 registry family rows and 887 roots remain unchanged.

## Bridge biome and modifier constraints

Existing merged tags resolve yungsbridges:has_structure/bridge to six registered
biomes: vanilla river/frozen_river, Regions Unexplored cold_river/muddy_river/
tropical_river and Terralith warm_river. No required members are missing. Only
the captured overworld possible-biome list overlaps these members. This is not
observed placement. Each of the 22 inline variants applies terrain placement,
rarity_filter chance=3, then RNG initialization. The captured initializer reseeds
the supplied random source from two odd long values, X/Z and constants, returning
the same position. Multiple selector attempts prevent interpreting chance=3 as
an observed per-chunk bridge probability. Configuration registration and external
modifications still require reconciliation. No new measurement system was added.

Eleven affected tests and scoped Ruff/Basedpyright passed. Decision SHA-256:
`35b9fbabcdc6521dd3cdbbb11d7432204e9b88e571c4bdb1a94c58423f9b0cb2`.

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py tests/item8/test_inventory_sources.py
uv run ruff check tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-yungs-bridge-biomes.json
```

Inventory regenerated at `c19f9d5`, SHA-256:
`f2497cb9bd2118ce0e1910cd2a203d9d51ea21d83636cb7f3addf2601b3c2a97`.
Only decision identity and bridge biome/modifier constraints with evidence changed.
All 421 registry family rows and 887 roots remain unchanged.

## YUNG Extras non-registry entry points

The existing contribution map now records the retained YUNG Extras provider's
three NeoForge biome modifiers. Two add 16 desert and 46 swamp placed features;
each of these 62 distinct IDs has a same-ID configured feature in the captured
runtime. There are no yungsextras structure-registry roots. Eleven configured
feature types describe generator categories, not accepted canonical families.
The third modifier declares vanilla desert-well removal; its effective scope
still requires configuration/biome reconciliation. Forge-path duplicates are not
additional NeoForge entry points. Template and generator interpretation remain
open. This reuses existing catalogs, registry evidence and contribution fields;
no new capture, schema or measurement system was added.

Twelve affected tests and scoped Ruff/Basedpyright passed. Decision SHA-256:
`a294b2c9219e1916ef1384acd0e4d8392133499f2b56a93a2a57e53cb5ffd92b`.

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py tests/item8/test_inventory_sources.py
uv run ruff check tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-yungs-extras-entrypoints.json
```

Inventory regenerated at `fe1fb1e`, SHA-256:
`9fcd6b648bd22c311a0d9f167c0013cb500e3817ed6c06406666e0dc719cadac`.
Only the decision identity and new Extras entry-point contribution changed.
All 421 registry family rows and 887 roots remain unchanged.

## YUNG Extras biome scope

The three modifier tags resolve through existing merged tag evidence and the
verified biome registry without missing required members. Desert additions and
vanilla desert-well removal share minecraft:desert, biomesoplenty:lush_desert
and terralith:lush_desert. Swamp additions use minecraft:swamp and
minecraft:mangrove_swamp. Only the captured overworld possible-biome list
intersects these sets. This resolves packaged biome scope, not actual placement,
effective registration/configuration effects or observed removal. Optional
absent tag members are not treated as active content. No new capture or
measurement system was added.

Thirteen affected tests and scoped Ruff/Basedpyright passed. Decision SHA-256:
`b850abc5df9278da4113694f5e01254e4cf08099a927185527f4f509840336b5`.

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py tests/item8/test_inventory_sources.py
uv run ruff check tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-yungs-extras-biomes.json
```

Inventory regenerated at `397812a`, SHA-256:
`7a1110e2734dd4f04a4084ed2ffbe9aa3be0a6af9fc61ffd5518ff40c831aba0`.
Only decision identity and Extras biome/removal scope with evidence changed.
All 421 registry family rows and 887 roots remain unchanged.

## YUNG Extras explicit template membership

Fifty-nine configured features explicitly name 59 distinct packaged templates;
all resolve. Their unrotated nominal XYZ envelopes are now recorded. Three
configured features have empty configs and require generator-code attribution:
desert_chillzone, desert_giant_torch and desert_ruins_0. Three packaged templates
remain outside the explicit links, but are not declared unused based on that
fact. Template dimensions are not processed/occupied world geometry. Block-entity
contents and custom generation still require attribution. Existing catalogs and
the contribution map suffice; no new extraction or measurement system was added.

Fourteen affected tests passed. Scoped Ruff/Basedpyright passed after wrapping
one long assertion. Decision SHA-256:
`91acf25034c7c4bde3596b7ef5c81947184d736fff3e6f1cb6ea90ad0a16f629`.

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py tests/item8/test_inventory_sources.py
uv run ruff check tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-yungs-extras-templates.json
```

Inventory regenerated at `2957779`, SHA-256:
`f66b81d0def7ecf9de36eb82f036ef646ed9b343930b92f8f030a9546ab1c060`.
Only decision identity and Extras template membership with evidence changed.
All 421 registry family rows and 887 roots remain unchanged.

## YUNG Extras packaged entities and chest loot

All 62 packaged templates have empty entity lists. Four templates contain block
entities: chillzone has one chest, ruins_0 has two, giant_torch and swamp_pillar_2
have four campfires each. Both referenced chest loot tables resolve uniquely in
the existing packaged catalog. No stored spawner block entity occurs in these
templates. These facts do not exclude custom generation effects. In particular,
the chest-bearing desert templates still require code attribution to their
empty-config feature generators. No observed loot or complete generated-content
claim is made, and no new extraction or measurement system was added.

Fifteen affected tests and scoped Ruff/Basedpyright passed. Decision SHA-256:
`3ff61997f724c9f11ab624e583845082bcc27534112904187c16b0fa40e38457`.

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py tests/item8/test_inventory_sources.py
uv run ruff check tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-yungs-extras-content.json
```

Inventory regenerated at `bae0ae4`, SHA-256:
`c27dbad3867324ff9110ef5f0dfe04a5e6b3dfd4867e8af9205cb9b3c431ff3a`.
Only decision identity and Extras packaged-template content changed.
All 421 registry family rows and 887 roots remain unchanged.

## Extras desert class-to-template calls

The three captured classes pass fixed template IDs to createTemplateFromCenter:
chillzone, giant_torch and ruins_0 respectively. The first two use ground above();
ruins uses ground directly. The helper subtracts half template X/Z, preserves Y,
and places with default settings before applying its processor list. It discards
the placement boolean; the callers test non-null template loading. Full placement
success is therefore not established by the returned boolean.

This is class-to-template evidence. FeatureModule constructs these classes, but
the current non-verbose capture omits registration annotations. Exact runtime
feature-ID binding remains open. The JSON-explicit links are preserved separately.
No new capture or measurement system was added for this interpretation.

Sixteen affected tests and scoped quality checks passed. Decision SHA-256:
`251c7036fc0bae5d26b0f94b9970198857887a1dc244d1fc4a80537c458f796d`.

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py tests/item8/test_inventory_sources.py
uv run ruff check tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-extras-desert-calls.json
```

Inventory regenerated at `0f8e610`, SHA-256:
`55fd39f5efd49aee91e1a922eacc763291a09dc9892ba4175c1802bd741eeb0d`.
Only decision identity and Extras desert generator-template calls/evidence changed.
All 421 registry family rows and 887 roots remain unchanged.

## Extras code-based template links resolved

The preserved class-level and field-level AutoRegister annotations bind the
three desert feature IDs to the classes whose template calls were already
verified. All 62 packaged templates now have a traced feature link: 59 explicit
JSON locations and three code-based paths. The paths remain separate in the
inventory. The earlier open-link statements are superseded; this does not close
family grouping, terrain checks or effective generated contents.

Seventeen affected tests and scoped quality checks passed. Decision SHA-256:
`f72a460733e7d8ee465b0f7a8d0340879a5e5afb48e97d48ae2833dfd3173279`.

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py tests/item8/test_inventory_sources.py
uv run ruff check tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-extras-code-links.json
```

Inventory regenerated at `4bb656f`, SHA-256:
`6354d013331c716f3091e87ce3b49fa03a766471a7a8cd2167bfc0bf0c50e5d9`.
Only decision identity and Extras code-link attribution/evidence changed.
All 421 registry family rows and 887 roots remain unchanged.

## Extras code-linked template envelopes

The three code-linked templates now record nominal XYZ dimensions: chillzone
3x4x4, giant_torch 4x7x4 and ruins_0 4x5x4. Together with the existing 59 explicit
links, all 62 packaged template envelopes are accounted for. These are template
bounds, not observed occupied dimensions or accepted family groupings.

Seventeen affected tests and scoped checks passed. Decision SHA-256:
`0a03048d57cafe7a3fc1dd156944561c56c85e5017b7a65cd54343374ec6a437`.

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py tests/item8/test_inventory_sources.py
uv run ruff check tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_feature_modifier_references.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-extras-code-sizes.json
```

Inventory regenerated at `bb970de`, SHA-256:
`c7fa2fed220886d952ea872056cd9fcf0899719e431b70923fc21be72b4835ea`.
Only decision identity and three code-linked template sizes changed.
All 421 registry family rows and 887 roots remain unchanged.

### Extras well processor loot and placement

The preserved DesertWellFeature, DesertWellProcessor and FeatureProcessorModule
sources now establish processor-generated archaeology loot that is absent from
stored template block entities. Brown glass markers use the vanilla desert-well
archaeology constant; yellow glass markers use Extras' extra_archeology table.
The decision preserves both random selection rules, the brown-marker minimum-fill
pass, conditional brushable block-entity assignment, and placement failure limits.
It also records the ground checks and template origin six blocks below landing.
These are code-derived rules, not measured reward counts or successful placements.

Validation: 18 affected tests passed. Ruff initially reported a combined assertion;
splitting it resolved the finding, and scoped Ruff/Basedpyright passed.

```sh
uv run pytest -q tests/item8/test_feature_modifier_references.py tests/item8/test_inventory_sources.py
uv run ruff check tools/build_item8_inventory.py tests/item8/test_feature_modifier_references.py
uv run basedpyright tools/build_item8_inventory.py tests/item8/test_feature_modifier_references.py
```

Inventory regeneration at `b8c4a7e` changed only input identity and the Extras
non-registry contribution. All registry-family rows and Bridges content remain
unchanged. Reproduce with a fresh output directory:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-extras-well-generation.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-extras-well-generation.json
```

### Extras swamp placement and appearance

The six registered swamp feature types use their configured templates through
AbstractSwampFeature and its shared SwampFeatureProcessor. The inventory now
records each generator's selected non-empty terrain offsets and common landing
anchor. Ogre checks are at landing height; the other five check four blocks below.
These checks do not establish solid ground across the entire footprint.

Gray markers become masonry with downward supports through air, liquid or
replaceable blocks. There is no explicit minimum-Y guard in that processor loop,
and template height excludes these terrain-dependent supports. Other recorded
effects are masonry/stair substitution and randomized candle color, count and
lighting. These are authored appearance rules, not observed visual discoverability.
The decision retains the limits of direct source inspection and placement success.

The existing focused command above passed 19 tests, and scoped Ruff/Basedpyright
passed. No extraction, runtime, measurement system or generalized helper was added.

Inventory regeneration at `5f52351` changed only input identity and the Extras
swamp-generation contribution. All registry-family rows and other contribution
fields remain unchanged. Reproduce with a fresh output directory:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-extras-swamp-generation.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-extras-swamp-generation.json
```

### Extras remaining desert surface generators

Chillzone, giant torch, small ruins and obelisk now record their sand landing
requirement, four solid support offsets and template anchors. The first, second
and fourth place one block above landing; small ruins place at landing height.
All four inherit the empty custom processor list from AbstractNbtFeature.
This closes their direct terrain/processor attribution, not external stack effects
or observed discoverability. The preserved source captures were reused unchanged.
The existing focused command passed 19 tests; scoped Ruff/Basedpyright passed.

Inventory regenerated at `d06f076`; only input identity and the Extras desert
surface-generation field changed. All registry-family rows remain unchanged.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-extras-desert-surface.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-extras-desert-surface.json
```

### Extras and Bridges initialization attribution

Both contribution records now link the preserved entrypoint and module-loader
sources. Common initialization scans the module package and calls the module
service. The packaged NeoForge loader delegates to a default method containing
only return. This implementation performs no configuration registration. Service
selection, annotation-driven registration and external controls are explicitly
outside that conclusion. Extras' top-level scope now reflects its delivered
62 template links and direct generator rules instead of the obsolete entrypoint-only
status. Canonical family and effective attribute completion remain open.

Twenty focused tests and scoped Ruff/Basedpyright passed using the existing
commands above. No runtime, source extraction or new validation framework added.

Regeneration at `f569bde` changed only the input identity, both initialization
records and their source links, and the Extras scope correction. Registry-family
rows are unchanged. Reproduce with a fresh output directory:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-yung-initialization.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-yung-initialization.json
```

### Feature-generated family reconciliation

Extras' 62 configured variants now form ten working authored-form families:
desert chillzone, giant torch, small ruins, obelisk and well; swamp arch, church,
cubby, ogre and pillar. Single and double arches share one family: both are thin
masonry arch designs with the same processor and landing placement, while span
count changes width and support checks. Each other grouping records its rationale
using the preserved design, template envelope, contents and generator distinctions.
These are inventory grouping judgments, not Item 9 encounter classifications.

Bridges' 22 configured variants form one bridge family, preserving 11 linked
templates. Stone/wood, damage, length and orientation remain variants of the
same selector-driven river crossing. Three templates outside the traced selector
links are retained as packaged content, not counted as active families.

The existing focused command passed 21 tests, including exact-once coverage of
all traced configured variants. Basedpyright initially rejected a generic JSON
value as a set key; explicit string conversion fixed that typing issue. Scoped
Ruff/Basedpyright then passed. The 421 registry groups remain separate; these
additional eleven feature-family records do not establish a final pack-wide total.
Required attributes and full retained-provider coverage remain incomplete.

Regeneration at `0a17e78` changed only input identity and the two contributions
family membership/rationale records. Registry rows and prior attribute evidence
are unchanged. Reproduce with a fresh output directory:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-yung-feature-families.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-yung-feature-families.json
```

### Feature-family template geometry

Each of the eleven feature families now lists its exact linked templates and
distinct nominal XYZ envelopes. X/Z are approximate authored footprint and Y is
template height. The records explicitly exclude occupied-world interpretation,
terrain-dependent bridge/swamp supports, and any assumption that desert-well
height is entirely above ground. Bridge orientation can exchange X/Z.

The existing focused command passed 22 tests, including a join from every family
member through the preserved template links to its recorded envelope. Scoped
Ruff/Basedpyright passed. No new capture or measurement system was needed.

Regeneration at `62b6af5` changed only input identity and the eleven feature
families template lists, envelopes and geometry limitations. Other inventory
records remain unchanged. Reproduce in a fresh directory:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-yung-family-geometry.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-yung-family-geometry.json
```

### Feature-family biome and dimension scope

All eleven feature families now carry their addition-modifier biome tag, resolved
registered biomes and captured dimension overlap. Extras desert families share
three eligible desert biomes; swamp families share swamp and mangrove swamp.
Bridges retains six eligible river biomes. Only overworld overlaps in the captured
live dimension lists. This is eligibility, not observed family generation.

Twenty-three focused tests passed, including binding each Extras family's complete
member set to exactly one addition modifier. The existing tag-resolution tests
remain the underlying evidence. Ruff found one long test line; wrapping it resolved
the finding and scoped Ruff/Basedpyright passed. No new measurement was required.

Regeneration at `4b1e33a` changed only input identity and the eleven feature
families biome/dimension fields. Other inventory records remain unchanged.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-yung-family-biomes.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-yung-family-biomes.json
```

### Feature-family content attribution

Extras family records now join their member templates to preserved authored
entities, block entities and chest loot. Chillzone retains its one chest, small
ruins its two chests, giant torch its four campfires, and swamp pillar its
campfire-bearing variant. Empty stored spawner/entity lists remain explicitly
limited to templates. Wells separately list processor-created archaeology loot,
so their absence of template chests cannot conceal that reward source.

The bridge family now carries the existing direct encounter-content findings,
including their natural-spawning and external-modification limitations. Twenty-four
focused tests and scoped Ruff/Basedpyright passed. No new measurement or source
capture was needed. Effective whole-stack content remains an open requirement.
