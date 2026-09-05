# Item 8 evidence plan

Status: IN PROGRESS. No family count or completion claim is accepted yet.

Current working inventory regenerated at `bdcee2c`, SHA-256
`151e5afe848e375cfdc7ef42887ec8e43c311250a45882a52645362de1c2e9ed`.
All 887 registered roots are assigned once in 429 working groups. This is not
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
