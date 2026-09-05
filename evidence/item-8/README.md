# Item 8 evidence plan

Status: IN PROGRESS. No family count or completion claim is accepted yet.

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
