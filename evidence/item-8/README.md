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
