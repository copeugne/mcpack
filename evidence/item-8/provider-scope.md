# Retained-provider scope pass

Status: search index delivered; candidate completeness is NOT VERIFIED.
Supported provider dispositions: 77 of 136. The exact queue below has 59 open rows.
The index and its keyword-based partition do not prove a complete candidate universe.
Every retained candidate has a row in provider-scope.json.gz, with exact archive
identity and the relevant packaged paths and code-reference candidates. Minecraft
and NeoForge have separate platform rows. Do not count paths or classes as families.

Extractor revision: 21eaef5. Output SHA-256:
b40f85af83a32b53eb20fbced80b914a415e61daf07772a0cf64edb1f68d3fb5.

```sh
uv run -m tools.extract_item8_sources --kind scope --output evidence/raw/item8/provider-scope-21eaef5.json.gz
cmp evidence/item-8/provider-scope.json.gz evidence/raw/item8/provider-scope-21eaef5.json.gz
```

The output reproduces exactly. The three catalogs have pinned hashes and their
archive lists must exactly match retained_sources. The join uses resource_identity
to avoid confusing structure tags with structure definitions. Scoped Ruff and
Basedpyright pass. Initial static findings concerned exception formatting and
string formatting; these were corrected. The pre-correction pilot is preserved
at evidence/raw/item8/provider-scope-pilot.json.gz and is not the accepted output.

The mutually exclusive review lanes partition the 136 retained candidates:

| Review lane | Retained JARs | Required disposition |
| --- | ---: | --- |
| Packaged structure definitions | 30 | Reconcile definitions with runtime roots and working families; also inspect additional feature paths. |
| Other generation data or templates | 25 | Assign family, injected component, terrain/vegetation, spawn-only or inactive content. |
| Code references only | 32 | Distinguish generation/injection from library, optimization, commands, client inspection and player construction. |
| No candidates in these searches | 49 | No matched generation data/code. This is a scoped search result, not a semantic absence proof or exemption from loot/mob attribution. |
| Total | 136 | Every retained archive has one row. |

These are provider review counts, not the number of unfinished families or new
implementation tasks. Existing source attribution must be reused. The full exact
names and candidate paths are in the machine-readable file, including nested
archive provenance. A mod can affect family attributes without creating a family.
In particular Loot Integrations appearing in the last lane does not exempt its
loot modifications from Item 8.

Examples requiring semantic reconciliation are listed below. This list is not
a proven exhaustive candidate queue:

1. Feature-based authored-content candidates: BetterEnd building lists and
   crashed ships, Biomes O' Plenty anomaly/monolith/bone spine, Deep Aether totem,
   Explorations scarecrow, and Supplementaries feature/structure aliases.
2. Existing nonregistry families: Quark, YUNG's Bridges, YUNG's Extras and the
   Better End Island platform/gateway contributions. Reuse their decisions;
   close coverage without repeating their detailed source interpretation.
3. Component providers: Farmer's Delight, Chef's Delight, Better Village,
   Village Taverns, Regions Unexplored and RS Farmer's Delight compatibility.
   Bind consuming families; do not add a house or pool as a standalone family.
4. Terrain, vegetation, construction and utility candidates in the remaining
   rows. Use actual resource content and code roles to dispose of them. A
   speculative possibility is not authorization for exhaustive helper tracing.
5. Reconcile family boundaries within the existing 421 provisional groups,
   especially Moog and village designs. Report accepted families and named
   unresolved alternatives separately; do not hide the latter in a vague count.

Do not resume detailed per-family attribute work until this scope queue has an
explicit disposition. The resulting finite family list, not these provider
counts, is the requested answer to how many families remain.

## Reconciliation checkpoint at ac990fd

| Candidate | Delivered result | Remaining scope decision |
| --- | --- | --- |
| BetterEnd building lists | Six live configured/placed IDs, 63 exact template choices, 21 vegetation exclusions and 42 architectural candidates. See BetterEnd feature candidate reconciliation below. | Group architectural choices by design; neither six lists nor 42 templates is the family count. |
| BetterEnd crashed ship | Inline configured placement, live placed ID, 27 packaged biome consumers, including 21 exposed by the captured End biome source. See reconciliation below. | Include the named crashed-ship candidate; reconcile shared biome modifiers and full provider coverage. Placement success remains separate. |
| BOP anomaly, monolith, bone spine | Direct writers in 846bc09; both bone-spine definitions reuse one type. | Resolve landmark/terrain boundaries and bind active placement. |
| Deep Aether totem | One stacked design with block/height/facing variations in b0194ce. | Bind registration and placement; preserve one design rather than counting blocks as families. |
| Explorations scarecrow | One figure design, nine material configurations and a selector in ac990fd. | Bind registration and selector/placement relationships; do not count ten configured entries as ten families. |

These captures are delivered and must not be repeated. They narrow the candidate
scope; they are not final per-family attribute acceptance. Supplementaries aliases,
component consumers, remaining utility/terrain dispositions and canonical grouping
within the existing provisional inventory still require reconciliation. Continue
the whole retained-provider reconciliation before returning to attribute implementation.

## Candidate-completeness gate and supported provider dispositions

Priority correction relayed from the user's side conversation: establish
candidate completeness before detailed family attributes or canonical variant
counting. Every retained mod must have supported roles: creates families, injects
components, modifies existing generation, or contributes no structures. Multiple
roles are allowed. Inspect relevant registration/event/mixin entry points and
data. Reconcile registries, features, pool injections, replacements and direct
code generation. Every potentially structural unmatched template, pool and hook
needs a candidate/component link or justified unused/disabled exclusion.

The immediate gate passes only when all 136 retained mods have supported
dispositions and no potentially structural entry points or resources remain
unexplained. Publish all candidates and named ambiguities, keeping generation
eligibility separate from canonical grouping. Zero search hits do not satisfy
this gate. Reuse existing evidence and tools; no new measurement or review system.

The following seven dispositions are supported by complete archive inspection,
not by zero keyword matches. tests/item8/test_loot_addon_provider_scope.py verifies
each frozen archive hash, accounts for every non-directory file, confirms
lowcodefml metadata, and requires all payload files to be loot-integration JSON
with the observed loot-rule fields. There are no classes, nested archives,
services, mixins, scripts, templates or generation resource files in these JARs.

| Retained mod | Supported role | Family-candidate disposition |
| --- | --- | --- |
| lootintegration_townsandtowers-1.3.jar | Loot-rule data for existing containers | No new structure families or generation hooks. |
| lootintegration_wda-1.8.jar | Loot-rule data for existing containers | No new structure families or generation hooks. |
| lootintegrations_ctov-1.4.jar | Loot-rule data for existing containers | No new structure families or generation hooks. |
| lootintegrations_integrated-1.5.jar | Loot-rule data for existing containers | No new structure families or generation hooks. |
| lootintegrations_moog-2.0.jar | Loot-rule data for existing containers | No new structure families or generation hooks. |
| lootintegrations_vanilla-1.6.jar | Loot-rule data for existing containers | No new structure families or generation hooks. |
| lootintegrations_yungs-1.5.jar | Loot-rule data for existing containers | No new structure families or generation hooks. |

Their loot effects remain relevant to existing-family loot-source attribution.
This does not classify the separate lootintegrations-1.21.1-4.7.jar implementation.

```sh
uv run pytest -q tests/item8/test_loot_addon_provider_scope.py
```

Seven focused cases pass. Ruff passes. Basedpyright initially reported untyped
JSON values; a type annotation fixed that finding and the scoped check passes.
Existing captures and decisions for other providers remain evidence to reconcile,
not automatically completed rows. Continue the whole-stack role/resource pass;
do not replace the unresolved remainder with a claim of exhaustive coverage.

## Construction-content provider dispositions

The nine Macaw entry constructors are captured in 007ff06, with exact identities
and reproduction commands in sources/macaw-provider-entries.md. The focused
full-payload check accounts for all files, permits only the observed construction
and painting data categories, checks loader metadata for extra entry mechanisms,
and binds the single annotated Mod entry to its captured class. No additional
auto-subscribers or NeoForge global-bus references appear in these class payloads.
This combines inspected constructor behavior with full archive accounting;
it is not an exclusion based only on generation-keyword absence.

| Retained mod | Supported role | Family-candidate disposition |
| --- | --- | --- |
| mcw-doors-1.1.5-mc1.21.1neoforge.jar | Construction blocks/items, sounds and creative tab | No independent structure family or generation entry point. |
| mcw-lights-1.1.5-mc1.21.1neoforge.jar | Construction blocks/items, sounds and creative tab | No independent structure family or generation entry point. |
| mcw-mcwfences-1.2.1-mc1.21.1neoforge.jar | Construction blocks/items and creative tab | No independent structure family or generation entry point. |
| mcw-mcwpaths-1.1.1-mc1.21.1neoforge.jar | Construction blocks/items and creative tab | No independent structure family or generation entry point. |
| mcw-mcwstairs-1.0.2-mc1.21.1neoforge.jar | Construction blocks/items and creative tab | No independent structure family or generation entry point. |
| mcw-mcwwindows-2.4.2-mc1.21.1neoforge.jar | Construction blocks/items, sounds and creative tab | No independent structure family or generation entry point. |
| mcw-paintings-1.1.0-mc1.21.1neoforge.jar | Painting variants and placeable-painting tag; empty entry constructor | No independent structure family or generation entry point. |
| mcw-roofs-2.3.2-mc1.21.1neoforge.jar | Construction blocks/items and creative tab | No independent structure family or generation entry point. |
| mcw-trapdoors-1.1.5-mc1.21.1neoforge.jar | Construction blocks/items and creative tab | No independent structure family or generation entry point. |

Other providers can use these blocks in their own templates. Such consumption
belongs to those component relationships and is not an independent family added
by the construction mod. This disposition does not claim no effect on block
interaction, salvage or existing loot/recipe data.

```sh
uv run pytest -q tests/item8/test_macaw_provider_scope.py
```

Nine cases pass. Scoped Ruff and Basedpyright pass after correcting an overlong
assertion and splitting a compound assertion. No additional runtime measurement.
Continue supported roles and unexplained-resource reconciliation for the other
retained providers; the whole-stack gate remains open.

## Repurposed Structures Farmer's Delight component provider

`repurposed_structures_farmers_delight_compat_v7.jar` contributes component
injection declarations, piece-count limits and block-rule processor data for
existing Repurposed Structures villages. It contributes no independent root.
The complete archive contains only three metadata files, 13 templates, 12 pool
addition documents, 12 piece-count documents and 11 processor lists. The loader
is lowcodefml; complete file accounting excludes executable code or additional
generation resource mechanisms in this add-on.

The twelve target variants are badlands, bamboo, birch, cherry, dark_forest,
giant_taiga, jungle, mountains, mushroom, oak, ocean and swamp. For each variant
`V`, the component link is:

- Root candidate: `repurposed_structures:village_V`, present in the captured
  live structure registry.
- Pool addition target: `repurposed_structures:villages/V/houses`.
- Component: `farmersdelight:villages/V/houses/compost_pile_1`.

The mushroom target also references `farmersdelight:villages/mushroom/houses/mushroom_farm`.
The sets referenced by pool additions and piece-count declarations each equal
the entire packaged template set. No template is left without a component link.
Ten crop_randomizer processor lists cover the variants other than mushroom and
ocean; the eleventh is mushroom/mushroom_randomizer. All use minecraft:rule.
These are existing-generation modifications, not additional family candidates.

This establishes the add-on's candidate boundary. Actual injection execution,
effective processor precedence and resulting family attributes still belong to
the consuming Repurposed Structures implementation and existing inventory work.
In particular, this does not resolve the already recorded bamboo processor
collision or claim that every component was observed in generated worlds.

The full JSON and template payloads are already preserved in the pinned packaged
catalogs listed above. No new raw capture is required. Reproduce the complete
archive accounting and runtime-root links with:

```sh
uv run pytest -q tests/item8/test_rs_delight_provider_scope.py
```

One case passes. Ruff and Basedpyright pass after explicit string concatenation
and JSON type corrections. This brings the explicit provider dispositions in
this document to 17 of 136. The other 119 require reconciliation into this gate,
including reuse of previously captured and interpreted evidence. This is a
provider-accounting remainder, not an unfinished-family count.

## Moog End and Soaring data providers

| Retained mod | Supported role | Root candidates | Pools | Templates |
| --- | --- | ---: | ---: | ---: |
| MoogsEndStructures-1.21-2.0.3.jar | Packaged structure families and their components, using registered pool codecs | 25 | 57 | 67 |
| MoogsSoaringStructures-1.21-2.1.2.jar | Packaged structure families and their components, using registered pool codecs | 35 | 91 | 99 |

These are root and resource counts, not canonical-family counts. The complete
candidate lists are the `mes:` and `mss:` structure roots in the existing
inventory and pool-traces-content.json.gz. All packaged roots occur in those
preserved traces. Every packaged pool links to at least one such root, with no
unresolved pool element codec in this provider pass. All templates either occur
in a root's potential graph or are explicitly unselected alternatives in the
versioned pool elements. This is candidate reachability, not observed placement.

The End provider has one such unselected alternative:
`mes:mega_ship/v1_21_9/mega_ship_deepslate_2_middle`. The Soaring provider has eight,
all under `mss:1_21_9/`: arena/arena_2, arena/arena_3, arena/arena_4, castle_tower,
desert_pyramid, large_tower, large_tower_top and taiga. Their exclusion is checked
against the actual versioned element selections for frozen Minecraft 1.21.1,
not inferred from their filenames. They are component alternatives, not extra
families. Existing pool-codec evidence and selection logic are reused.

Full archive accounting permits only metadata, icon/language assets, templates,
biome tags, loot tables, structure definitions, structure sets and template
pools. Neither archive contains executable code or a separate feature, event,
mixin, injection or direct-generation implementation. The shared Moog codec
implementation remains a separate retained-provider responsibility.

```sh
uv run pytest -q tests/item8/test_moog_data_provider_scope.py
```

Two cases pass, as do scoped Ruff and Basedpyright. The test binds original
archive identities and the preserved pool trace hash; no new capture or graph
implementation was added. Explicit provider dispositions now cover 19 of 136;
117 remain to reconcile, including already delivered evidence. Explorify, Moog
Nether and Moog Voyager are not included in this closure: their unmatched
resources still require named dispositions. Canonical design grouping remains
separate from this provider candidate-boundary result.

## Moog Voyager data provider

`MoogsVoyagerStructures-1.21-5.0.11.jar` supplies 129 root candidates, 149 pools,
327 templates and six block-rule processor lists. Its full archive has the same
data-only boundary as the End/Soaring providers, additionally permitting those
processor lists. There are no separate feature definitions or executable entry
points in this archive. All roots and pools are accounted for in the preserved
generation graph, without missing graph resources or unresolved pool elements.

Of the 92 templates outside that graph, 51 are explicitly unselected alternatives
of versioned pool elements. The other 41 have no template reference from any
packaged Voyager pool, including unselected alternatives. Their disposition is
disconnected components, unused by this provider's packaged root/pool graph:

- `mvs:animals/`: cat_black, cat_british_shorthair, cat_calico, cat_jellie,
  cat_persian, cat_ragdoll, cat_red, cat_siamese, cat_tabby, cat_tuxedo, cat_white,
  cows_1, horses_1, horses_2, horses_3, horses_4, horses_5, mule, pigs_1, sheep_1,
  sheep_2.
- `mvs:armor_stand/`: armor_stand_1, armor_stand_2, armor_stand_3, armor_stand_4.
- `mvs:cathedral/`: cathedral_start, corridors/corridor_8.
- `mvs:houses/`: medium_igloo_2, medium_igloo_2_lower.
- `mvs:mineshaft/`: barrels_1, barrels_2, barrels_3, barrels_4, cart_1, cart_2,
  cart_3, dead_end_1, logs_1, logs_2, round_staircase_3, stable.

The exact sets are checked in test_moog_data_provider_scope.py, using the original
archive and existing version-selection and graph evidence. The candidate list
remains the existing `mvs:` roots; these disconnected components do not add
independent roots. This does not assert that manual placement is impossible or
that another provider cannot inject resources. Shared Moog implementation scope
and other providers' injections remain separate responsibilities in this gate.

The existing three-case command for End, Soaring and Voyager passes. Scoped Ruff
and Basedpyright pass; the statement-count lint exception keeps the direct
archive-accounting check together instead of introducing an unnecessary helper.
Explicit provider dispositions now cover 20 of 136, with 116 still to reconcile.
Canonical grouping and effective family attributes remain deferred.

## Moog Nether data provider

`MoogsNetherStructures-1.21-3.0.0-alpha.2.jar` supplies 52 existing root candidates,
168 pools and 459 templates. Complete archive accounting also identifies eight
processor lists, four trial-spawner configurations, biome tags, loot tables and
two shared-namespace structure tags: moogs_structures:no_basalt and no_delta.
These are generation/component and encounter modifications for existing roots.
The archive contains no executable entry points or separate feature definitions.
Processor types are pillar, spawner randomization, trial-spawner randomization,
vault randomization and armor-stand equipment; exact implementation attribution
remains with the shared Moog provider and subsequent family attributes.

All 52 roots have preserved traces without missing resources or unresolved pool
elements. Twelve pools lie outside their root graphs. Their exact IDs, prefixed
with `mns:`, are:

- dragon_arena/lower_14.
- mega_arenas/mobs/arena_bowman, mega_arenas/mobs/ember_sentinel,
  mega_arenas/mobs/pit_vanguard.
- mega_fortress/crossings/small/small_crossing_2_east,
  mega_fortress/crossings/small/small_crossing_2_north,
  mega_fortress/crossings/small/small_crossing_2_south,
  mega_fortress/crossings/small/small_crossing_2_west.
- mega_fortress/mobs/blaze_sentinel, mega_fortress/mobs/fortress_guard,
  mega_fortress/start/start_crossing_north.
- very_small_nether_brick_start_pool.

Of 171 templates outside those graphs, 162 are unselected version alternatives.
The remaining nine disconnected template IDs, also prefixed with `mns:`, are
dragon_arena/lower_14; large_arena/v1_21_4/l2 and r2;
large_arena/v1_21_5/l2 and r2; large_arena/v1_21_9/l2 and r2;
mega_fortress/corridors/roofed_long_straight_2; ruins/very_small_nether_brick_1.
These resources are unused by this provider's packaged root graph. Their explicit
disposition does not assert global impossibility of placement or preempt the
separate shared-code and injection-provider checks. They add no independent
packaged root candidate. Root identity remains separate from canonical grouping.

The reused test_moog_data_provider_scope.py now checks all four Moog data
providers, including exact disconnected sets. Four cases pass, with scoped Ruff
and Basedpyright passing. Local complexity lint exceptions retain explicit
archive cases without adding a new abstraction or framework. Explicit provider
dispositions now cover 21 of 136; 115 remain to reconcile. Explorify is the
remaining data-only structure-provider batch member.

## Explorify data provider

`Explorify v1.6.5.mod.jar` has 23 existing root candidates, 57 pools and 165
distinct current-path templates. All 165 legacy `structures/` files are
byte-identical copies of corresponding `structure/` files. Do not count them
again. Full accounting covers all 477 files, including metadata, biome tags,
loot tables, processor lists, structure sets and two Cristel Lib configuration
declarations. The f15 overlay contains processor lists; f41 contains legacy-path
loot tables. Neither adds a root, pool or template candidate. There is no
executable code or separate feature-generation mechanism in this archive.

All roots use minecraft:jigsaw and have existing traces without missing graph
resources or unresolved pool elements. The disconnected pool set is
`explorify:bastion_spiral/bridge_end`, plus base_plate, feature_plate, features
and tower beneath each of `explorify:watchtower/plains/`, savanna/ and taiga/.

The 30 disconnected templates are:

- Beneath each watchtower variant above: base_plate/whole, feature_plate/whole,
  tower/whole, features/campfire, features/coal_pile, features/hay_pile,
  features/logs and features/resource_pile.
- `explorify:bastion_spiral/bridge/long`, bridge/whole and bridge_end/whole.
- `explorify:campsite/tent/09`, tent/10 and `explorify:tavern/back/06`.

These are unused by the packaged root graphs, not additional independent root
candidates. Manual placement and other providers' injections are outside that
exclusion. Cristel Lib's two declarations target the same fourteen Explorify
structure sets for placement settings and enable/disable settings. They configure
existing candidates; effective configuration attribution remains part of the
shared-library check and family attributes.

```sh
uv run pytest -q tests/item8/test_explorify_provider_scope.py
```

One case passes. Scoped Ruff and Basedpyright pass after formatting overlong
lines. Original archive identity and the existing trace hash are bound by the
check. Explicit provider dispositions now cover 22 of 136, with 114 remaining to
reconcile. The data-only structure-provider batch is accounted for; continue
remaining code providers and injection relationships before detailed attributes.

## Chef's Delight component provider

`chefsdelight-1.0.5-neoforge-1.21.1.jar` injects the ten already recorded chef/cook
house components into the five vanilla village house pools. It adds professions,
points of interest, trade offers and a component loot table. It adds no separate
structure family. The candidate link remains chefsdelight:village_components in
family-decisions.json, with frozen weights and existing content evidence reused.

All six archive classes now have preserved source: chefsdelight-villages contains
the entry and injection implementation; chefsdelight-provider-entries contains
the other four classes, delivered in 23ee872. Those handle configuration loading,
profession/POI registration, trade offers and an empty client setup callback.
The access transformer only exposes StructureTemplatePool.templates, matching
the inspected injection path. Full file accounting binds all six classes to
their disassemblies and permits only the ten known templates, component loot,
job-site tag, metadata and visual assets. No additional code, nested archive,
service, mixin, feature definition or structure root is left unaccounted for.

```sh
uv run pytest -q tests/item8/test_chefsdelight_components.py
```

Both full-provider and existing component-content cases pass. Scoped Ruff and
Basedpyright pass after splitting an assertion and using a named class string.
The existing house-content test was retained without formatting changes. No
trade-balance work or new runtime sample was added. Explicit provider dispositions
now cover 23 of 136, with 113 remaining to reconcile. Consumer family attributes
and shared-stack effects remain downstream of candidate completeness.

## Village Taverns component provider

`village_taverns-neoforge-1.1.5+1.21.1.jar` contributes the five already recorded
tavern village components, their block/item, bartender profession, trades,
schedule modification and loot data. It adds no separate structure family.
The existing village_taverns:village_components relationship is reused.

All fifteen top-level classes are captured in tavern-provider-entries,
tavern-registration-scope and tavern-remaining-entries. The only bundled JAR is
the hash-verified Tiny Config library. Its single annotated mod entry calls an
empty initializer; it declares no mixins or auto-subscriber, and packages no
generation data. Its configuration manager and the inspected Tavern caller
account for the library's role without inferring that arbitrary caller callbacks
are inert. Full file accounting permits only these classes, known component
templates and modifiers, block/chest loot, recipe/job-site data and visual assets.

The five packaged additions each target minecraft:village/V/houses and reference
village_taverns:village/V/tavern, for desert, plains, savanna, snowy and taiga.
Each has weight 5 and a Lithostitched limited delegate with limit 1. The fallback
StructurePoolAPI path is conditional on Lithostitched absence and names the same
five component identities; it is not an additional family route. The actual
loader branch and effective weights remain attributable in family attributes,
without changing this candidate boundary. No template is unexplained.

```sh
uv run pytest -q tests/item8/test_tavern_provider_scope.py
```

The focused case passes. An initial full-file assertion exposed a packaged
jeweler.png.mcmeta asset; inspection showed villager hat metadata, and the visual
asset accounting was corrected. Scoped Ruff and Basedpyright pass after line
formatting. Source captures reproduced and are durably delivered. Explicit
provider dispositions now cover 24 of 136, with 112 remaining to reconcile.
Do not repeat Tavern block, trade or configuration-source investigation absent
a concrete new contradictory finding.

## Seven Seas structure provider

`DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar` contributes five existing
structure roots, ten pools and 36 templates. Its only class has an empty
constructor and logger initialization, captured in seven-seas-entry. Complete
archive accounting identifies only that class, metadata, templates, root/set/pool
definitions, loot tables and biome tags. It has no separate feature or injected
code-generation route. All packaged pools and templates are linked to the five
existing dungeons_arise_seven_seas root candidates in the preserved inventory.

One known graph failure remains explicitly preserved:
small_yacht/small_yacht_spawners references
`dungeons_arise_seven_seas:small_yacht/small_yacht_spawner_3`, which is missing.
The packaged element has weight 1, uses minecraft:single_pool_element and empty
processors. The existing small_yacht trace records the same missing template.
Disposition: missing referenced component, not another family or permission to
invent a replacement. Keep the effect on assembled content unresolved until the
applicable family evidence establishes it. Do not change the frozen mod stack.
No packaged template or pool is left without a candidate link.

```sh
uv run pytest -q tests/item8/test_seven_seas_provider_scope.py
```

One case passes, as do scoped Ruff and Basedpyright. The first check exposed an
incorrect use of the JSON extension default for NBT identities; the test now
passes the existing helper's NBT extension explicitly. An indentation mistake
during that correction was fixed before the passing run. No production decoder
or graph behavior changed. Explicit dispositions now cover 25 of 136 providers;
111 remain to reconcile. Towns and Towers' entry source is delivered in 1608481,
but its optional pack and disconnected resources still need dispositions.

## Towns and Towers structure provider

`t_and_t-neoforge-fabric-1.13.9+1.21.1.jar` supplies 60 existing root candidates,
187 pools and 837 base templates. Its three captured classes only initialize
logging or return the platform name. Full archive accounting identifies data,
metadata and those classes, without another executable generation route. The
existing towns_and_towers roots remain the candidate list; structure tags are
not roots. Cristel Lib declarations configure existing sets and an optional pack.

The optional t_and_t_waystones_patch pack contains three template replacements:
kaisyn:village/modded/waystones/waystone_default, waystone_desert and waystone_mossy.
Its declared condition requires modid waystones; the hash-bound captured runtime
mod list lacks that ID. Disposition: conditional components, ineligible under
the declared condition in this retained stack. They are not independent roots.
Shared Cristel Lib loading behavior remains attributable to that provider.

Three base pools are disconnected from the preserved root graphs:
kaisyn:village/grove_villager_outpost/decor and the desert/mossy Waystones pools.
Twenty-three base templates are also disconnected. Their exact IDs are preserved
in the pinned catalogs and enumerated by test_towns_towers_provider_scope.py:
the savanna-plateau tower piece; badlands medium house 2_r; lighthouse master;
Iberian terminators 04/05/06; Mediterranean corner garden/stall and bishop;
Nilotic large house, leatherworker/shepherd and mason; piglin skul_tent_1;
rustic empty piece; grove table; desert/mossy Waystones; Polynesian village chief;
swamp corssroad_03/04/05 and straight_03; wooded-badlands green large hut.
Disposition: disconnected components, unused by these packaged root graphs.
Preserve exact misspellings and identities. Do not silently connect similarly
named resources or turn pieces into families.

Existing missing graph references affect eight roots: village_meadow,
village_swamp, exclusives/village_nilotic, village_sparse_jungle,
pillager_outpost_savanna_plateau, exclusives/pillager_outpost_nilotic,
exclusives/village_mediterranean and village_beach. Their exact missing IDs remain
in pool-traces-content.json.gz. Disposition: missing referenced components;
retain uncertainty about assembled content for family attributes and do not
repair the frozen baseline. All packaged resources now have candidate/component
links or explicit disconnected/conditional dispositions for this provider.

```sh
uv run pytest -q tests/item8/test_towns_towers_provider_scope.py
```

One case and scoped Ruff/Basedpyright pass. The test binds original archive,
entry disassemblies, preserved graph and runtime log identities. No new runtime
sample or graph implementation. Explicit provider dispositions now cover 26 of
136; 110 remain to reconcile. Canonical-family grouping remains separate.

## Exact provider queue, initialized at 05ce184

### Scope reassessment on 2026-09-06

The user correctly challenged the repeated statement that provider coverage is
open without a usable account of what remains. At e06c9e1, 59 rows below remain
open, including 44 with the generic instruction to inspect entry mechanisms.
Those generic instructions are insufficient as a progress explanation.

Joining the open archive names below to the existing provider-scope.json.gz
review_lane fields gives this planning partition. It is not provider acceptance
or a family count, and no new source scan or measurement system was introduced.

| Existing indexed lane | Open providers | Immediate question |
| --- | ---: | --- |
| Packaged structure definitions | 2 | Do all roots, additional routes and components have candidate links? |
| Other packaged generation candidates | 12 | Which inputs are sites, components, natural generation or inactive resources? |
| Code references only | 24 | Which actual entry routes generate or inject content, versus consuming existing content? |
| No generation candidates in indexed searches | 21 | Do the complete payload and actual entry mechanisms support a non-provider disposition? |
| Total | 59 | Close membership checks before detailed family attributes. |

The two structure-definition providers are Creating Space and Supplementaries.
Creating Space has mars/underground_outpost_1, moon/abandoned_outpost,
moon/crashed_rocket and moon/crashed_ship. Supplementaries has galleon and
road_sign. These are packaged definition names, not six newly discovered or
accepted families. In particular, Supplementaries also has a configured feature
named road_sign: reconcile the two representations before counting designs.

The twelve other packaged-generation rows are Creeper Overhaul, Farmer's Delight,
Aether's Delight, Coffee Delight, Create, End's Delight, Forgified Fabric API,
Lithostitched, Naturalist, Railways, Regions Unexplored and Ube's Delight.
The exact archive identities and resource paths are already in the indexed
artifact and the queue below. A template may be a component or player schematic;
a biome modifier may only change mob spawning. Their presence does not establish
an independent family. Conversely, a code-only or unmatched search row cannot
be excluded from membership using its search lane alone.

Continuation priority: reconcile the two structure-definition providers and
the remaining packaged-content candidates, closing shared loader dependencies
when they control those candidates. Then close the code-only and unmatched
entry checks. Reuse delivered provider dispositions and captures throughout.
Keep the current RU source checkpoint; do not restart its 53 implementation
captures. Follow further helpers only for a specific unresolved site or component
boundary, as required by the existing stopping rule below.

The deliverable for this stage is a named candidate list with every retained
provider accounted for and every remaining merge/split alternative explicitly
listed. The final family count follows resolution of those alternatives. The
887 runtime roots and 421 provisional groups do not supply that answer by
themselves. Progress updates must distinguish provider closures, candidate
additions and grouping decisions instead of reporting source captures as if
they reduced the family backlog.

This is the working queue, not an acceptance result. Initially, the 26 dispositions
above and 110 queued archive names partitioned the 136-line retained manifest.
WDA, Better Village, YUNG Bridges and YUNG Extras are resolved below:
30 dispositions and 106 open providers. Their rows remain as closure links. Minecraft and NeoForge are
shared consumers, not
extra retained mods. Existing capture directories below are relative to
`sources/`; their presence means evidence to reuse, not provider closure. An
empty directory index does not mean no evidence exists in other items.

Each row has the same bounded stopping rule: account for the complete packaged
payload and executable generation entry mechanisms, then link structural
resources to existing candidates/components or give a supported inactive,
disconnected or non-structural disposition. Follow a helper only when the entry
behavior leaves a concrete candidate unresolved. Do not audit unrelated gameplay
internals. Update a row when closed, with the existing disposition reference.

After every row is resolved, reconcile the already enumerated 887 roots and
nonregistry contributions into canonical designs, publishing any named grouping
alternatives. Only then report the final family denominator and finish the eleven
attributes. This separates unknown membership from incomplete attributes.

| Retained archive | Existing Item 8 captures to reuse | Next scope check or closure |
| --- | --- | --- |
| `AI-Improvements-1.21-0.5.3.jar` | `ai-improvements-provider` (69119c6), test_small_utility_provider_scope.py | RESOLVED: Existing-entity AI goals and look control; no structure contribution. See small utility provider dispositions below. |
| `Almanac-1.21.1-2-neoforge-1.5.2.jar` | `almanac-provider` (8c60e03), test_small_utility_provider_scope.py | RESOLVED: Configuration/command support and existing item/entity behavior. No independent family. See additional shared provider dispositions below. |
| `BetterEnd-21.0.31.jar` | BetterEnd source captures and shared BCLib/Wover consumers; test_betterend_feature_candidates.py | RESOLVED: Fourteen existing roots, the complete 128-template partition, feature candidates, common hooks and modifier consumers accounted for below. Named architectural and landmark grouping decisions remain open for canonical reconciliation. |
| `BiomesOPlenty-neoforge-1.21.1-21.1.0.13.jar` | BOP entry, feature and delegated-material captures; test_bop_feature_candidates.py | RESOLVED: All registered features and packaged resources have contribution roles. Anomaly and monolith are landmark candidates; giant pumpkin and carved-pumpkin patches retain named decoration boundaries for canonical grouping. No structure roots, templates or pools. See final BOP disposition below. |
| `CreateDragonsPlus-1.11.2b.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `CreeperOverhaul-neoforge-1.21.1-4.0.6.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `DungeonsArise-1.21.1-2.1.68-release.jar` | `wda-provider-scope` | RESOLVED: see WDA structure-provider disposition below. |
| `FarmersDelight-1.21.1-1.3.2.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `GlitchCore-neoforge-1.21.1-2.1.0.2.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `IllagerInvasion-v21.1.6-1.21.1-NeoForge.jar` | `illagerinvasion-provider`, `illagerinvasion-extensible-enums` (e0f2c9a), existing pool codecs, test_illagerinvasion_provider_scope.py | RESOLVED: Five existing roots, thirteen mansion replacement components and encounter/loot modifications. Bundled enum library has no independent family; disconnected pillager pool/template preserved below. |
| `LeavesBeGone-v21.1.1-1.21.1-NeoForge.jar` | `leavesbegone-provider` (69119c6), test_small_utility_provider_scope.py | RESOLVED: Leaf ticking and chunk tick persistence; no authored structure contribution. See small utility provider dispositions below. |
| `Patchouli-1.21.1-93-NEOFORGE.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `PuzzlesLib-v21.1.52-1.21.1-NeoForge.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `Quark-4.1-480.jar` | `quark-end-generators`, `quark-end-registration`, `quark-fallen-log-decor`, `quark-landmark-encounter-generators`, `quark-monster-box-behavior`, `quark-monster-box-bindings`, `quark-nether-spikes`, `quark-spire-config-annotations`, `quark-stone-clusters`, `quark-underground-base`, `quark-underground-context`, `quark-underground-fill`, `quark-underground-styles`, `quark-vegetation`, `quark-world-category` | RESOLVED: Existing five named nonregistry site candidates, terrain/vegetation and existing-structure replacement hooks; bundled Biolith adds biome/surface support. Full disposition below; canonical count and attributes remain open. |
| `TerraBlender-neoforge-1.21.1-4.1.0.8.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `Terralith_1.21.1_v2.6.2_Neoforge.jar` | `terralith-provider` (b87f3bb), test_terralith_provider_scope.py | RESOLVED: 28 existing roots, terrain/vegetation and one named Frostfire ornament candidate. Overlay, disconnected and missing component dispositions below; canonical ornament grouping remains open. |
| `YungsApi-1.21.1-NeoForge-5.1.6.jar` | Existing `pool-codecs`; `yungs-api-provider` (a796af9); test_yungs_api_provider_scope.py | RESOLVED: Shared registration, placement/pool codecs and existing-structure terrain/feature hooks. No independent family. See disposition below. |
| `YungsBetterCaves-1.21.1-NeoForge-3.1.4.jar` | `better-caves-provider` (d9e30ff); test_better_caves_provider_scope.py | RESOLVED: Cave/cavern carving and liquid-region/aquifer terrain support. No independent structure family. See disposition below. |
| `YungsBetterDesertTemples-1.21.1-NeoForge-4.1.5.jar` | Existing suppression source; `desert-temple-provider` (02ae27e); test_desert_temple_provider_scope.py | RESOLVED: One existing root, 28 connected pools, 198 templates and one disconnected crushing corridor. Placement, Pharaoh/state hooks and component registrations accounted for below. |
| `YungsBetterDungeons-1.21.1-NeoForge-5.1.4.jar` | Existing `betterdungeons-code`; `dungeons-provider` (f9696df); test_dungeons_provider_scope.py | RESOLVED: Five existing roots, 33 pools, 227 templates, one disconnected bridge and one missing zombie stair. Remaining registration/context/modifier paths are accounted for below. |
| `YungsBetterEndIsland-1.21.1-NeoForge-3.1.2.jar` | Existing platform/gateway, configuration and generator captures; `end-island-provider` (6e1f551); test_end_island_provider_scope.py | RESOLVED: All 41 templates belong to the existing arrival platform, gateway and dragon arena groups. Remaining entry hooks modify these contributions; see disposition below. |
| `YungsBetterJungleTemples-1.21.1-NeoForge-3.1.2.jar` | `jungle-temple-provider` (e4bb5e3), prior suppression source, test_jungle_temple_provider_scope.py | RESOLVED: One existing root, 17 connected pools and 127 templates including two disconnected table props. Custom placement and eight component processors accounted for below. |
| `YungsBetterMineshafts-1.21.1-NeoForge-5.1.1.jar` | Existing `mineshafts-code`; `mineshafts-provider` (26d2a97); test_mineshaft_provider_scope.py | RESOLVED: Thirteen roots in the existing mineshaft group, one structure set and eleven registered piece types. Remaining entries and the diagnostic suppression limitation are accounted for below. |
| `YungsBetterNetherFortresses-1.21.1-NeoForge-3.1.5.jar` | `fortress-provider` (5933abb), prior suppression source, test_fortress_provider_scope.py | RESOLVED: One existing root, 15 connected pools, 169 templates with 20 disconnected components and one missing template. Component processors and existing-fortress spawning hook accounted for below. |
| `YungsBetterOceanMonuments-1.21.1-NeoForge-4.1.2.jar` | `ocean-monument-provider` (a2f2832), prior suppression source, test_ocean_monument_provider_scope.py | RESOLVED: One existing root, 13 connected pools, 59 templates including two disconnected seagrass components. Ten block processors and marked-trident hook accounted for below. |
| `YungsBetterStrongholds-1.21.1-NeoForge-5.1.3.jar` | `stronghold-provider` (41964b5), prior suppression source, test_stronghold_provider_scope.py | RESOLVED: One existing root, 12 pools and 97 templates with thirteen disconnected components and one missing pool. Custom placement and component consumers accounted for below. |
| `YungsBetterWitchHuts-1.21.1-NeoForge-4.1.1.jar` | `witch-hut-provider` (04b6ab5), prior suppression capture, test_witch_hut_provider_scope.py | RESOLVED: Two existing roots, three pools, six connected templates and five component processors. Packaged services and entry roles are accounted for below. |
| `YungsBridges-1.21.1-NeoForge-5.1.1.jar` | `yungs-bridge-generation`, `yungs-bridge-processors`, `yungs-bridges-module-default`, `yungs-bridges-module-loader` | RESOLVED: see YUNG Bridges provider disposition below. |
| `YungsCaveBiomes-1.21.1-NeoForge-3.1.1.jar` | `cave-biomes-provider` (7f76013); test_cave_biomes_provider_scope.py | RESOLVED: Cave terrain, vegetation, existing-family biome eligibility and ambient encounters. All 38 worldgen resources and common hooks accounted for below; no independent family. |
| `YungsExtras-1.21.1-NeoForge-5.1.1.jar` | `yungs-extras-desert-code`, `yungs-extras-generators`, `yungs-extras-initialization`, `yungs-extras-module-default`, `yungs-extras-processor-bindings`, `yungs-extras-registration` | RESOLVED: see YUNG Extras provider disposition below. |
| `Zeta-1.1-40.jar` | `quark-enablement-callers`, `zeta-biome-modifier`, `zeta-component-biomes`, `zeta-compound-biome`, `zeta-config-binding`, `zeta-config-event-fields`, `zeta-deferred-feature`, `zeta-enablement-inputs`, `zeta-generation-applicability`, `zeta-generation-spawn`, `zeta-generator-dispatch`, `zeta-horizontal-directions`, `zeta-module-assignment`, `zeta-module-name`, `zeta-module-section`, `zeta-stone-ore` | RESOLVED: Consumer module/configuration, registry, biome/generator and structure-replacement dispatch. No independent family. See Zeta disposition below. |
| `[Neoforge]ctov-3.6.3.jar` | `ctov-provider` (82ac234), test_ctov_provider_scope.py, selection/bundle checks, existing CTOV regressions/graphs | RESOLVED: 78 existing roots, village/outpost components, compatibility injections and processors. Disconnected and missing components accounted for below. |
| `accessories-neoforge-1.1.0-beta.53+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `adorabuild-structures-2.11.0-neoforge-1.21.3.jar` | `adorabuild-provider`, existing runtime/root and pool graph evidence | RESOLVED: 106 existing roots; all 110 pools and 121 templates connected; one preserved missing pool reference. See AdoraBuild provider disposition below. |
| `aether-1.21.1-1.5.10-neoforge.jar` | Existing Aether source captures, test_aether_provider_scope.py and focused candidate/component checks | RESOLVED: Three dungeon candidates, cloud terrain, conditional holiday-tree boundary, inactive portal components, common hooks and selected-library roles accounted for below. Canonical grouping and attributes remain open. |
| `aethersdelight-0.1.4.2-1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `alternate_current-mc1.21-1.9.0.jar` | `alternate-current-provider` (4b722aa), test_small_utility_provider_scope.py | RESOLVED: Existing redstone-wire updates, configuration and profiling; no independent family. See redstone, configuration and loot provider dispositions below. |
| `amendments-1.21-2.0.15-neoforge.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `architectury-13.0.8-neoforge.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `attributefix-neoforge-1.21.1-21.1.3.jar` | `attributefix-provider` (69119c6), test_small_utility_provider_scope.py | RESOLVED: Existing attribute range configuration; no structure contribution. See small utility provider dispositions below. |
| `azurelibarmor-neo-1.21.1-3.1.2.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `bclib-21.0.24.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `bettercombat-neoforge-2.3.2+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `bettervillage-neoforge-1.21.1-3.3.1.jar` | `bettervillage-code` | RESOLVED: see Better Village provider disposition below. |
| `bookshelf-neoforge-1.21.1-21.1.81.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `bundle-api-neoforge-1.1.0.jar` | `bundle-api-provider` (a14b5e0), test_small_utility_provider_scope.py | RESOLVED: Custom bundle data components, item interaction and rendering; no independent family. See bundle and shield dispositions below. |
| `c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Include nested C2ME module entry/mixin paths; distinguish generation scheduling changes from content providers. |
| `cc-tweaked-1.21.1-forge-1.119.0.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `chipped-neoforge-1.21.1-4.0.2.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `cloth-config-15.0.140-neoforge.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `coffee_delight-1.4.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `collective-1.21.1-8.25.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `comforts-neoforge-9.0.5+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `create-1.21.1-6.0.10.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `create-enchantment-industry-2.4.0.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `createbigcannons-5.11.6+mc.1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `createdieselgenerators-1.21.1-1.3.15.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `creatingspace-1.21.1-1.7.18.jar` | Existing root decisions and test_creating_space_provider_scope.py; packaged component partition below. | All five pools linked. One of six templates is disconnected from root graphs; resolve other consumers and executable entry routes before provider closure. |
| `cristellib-neoforge-1.21.1-3.1.7.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve conditional pack loader and structure-config consumers, including Towns and Towers Waystones declaration. |
| `cupboard-1.21-3.7.jar` | `cupboard-provider` (77dd750), test_small_utility_provider_scope.py | RESOLVED: Shared configuration, lookups, diagnostics and existing-entity handling; no independent family. Frozen error-suppression setting and limitations below. |
| `curios-neoforge-9.5.1+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `deep_aether-1.21.1-1.1.5.1.jar` | `deep-aether-totem-scope`, `deep-aether-provider`, `deep-aether-aeroblender`, `deep-aether-biome-setup`; focused candidate and provider checks | RESOLVED: Four roots, fifteen templates, custom feature candidates, common hooks, optional packs and active AeroBlender accounted for. Preserve inactive Sacred Lands and fallen-tree grouping boundaries. See final Deep Aether disposition below. |
| `dummmmmmy-1.21-2.0.12-neoforge.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `emi_loot-0.7.9+1.21+neoforge.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `emi_ores-1.2+1.21.1+neoforge.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `ends_delight-2.6+neoforge.1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `explorations-neoforge-1.21.1-1.6.2.jar` | `explorations-provider` (0e6f5e4), prior scarecrow/slime/deepslate captures, test_explorations_provider_scope.py | RESOLVED: Ten existing roots, one scarecrow design, named decorated-mushroom candidate and four statue components in village houses pools. Missing and unused components preserved below. |
| `fastasyncworldsave-1.21-2.6.jar` | `fastasyncworldsave-provider` (7a82503), test_small_utility_provider_scope.py | RESOLVED: Saved-data and level-data write processing; no authored structure contribution. See save and structure utility dispositions below. |
| `forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `fzzy_config-0.7.6+1.21+neoforge.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `geckolib-neoforge-1.21.1-4.8.4.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `idas-1.13.7+1.21.1-neoforge.jar` | `idas-provider` (afb3cee), prior suppression evidence, test_idas_provider_scope.py | RESOLVED: 84 existing roots, complete component partition, compatibility pool declarations and Labyrinth encounter hooks. See IDAS disposition below; shared Integrated API and final attributes remain open. |
| `integrated_api-1.7.3+1.21.1-neoforge.jar` | `pool-codecs` | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `integrated_stronghold-1.1.4+1.21.1-neoforge.jar` | `integrated-stronghold-provider`, existing root/graph and family-decision regression | RESOLVED: one existing root, both modification mixins, all components and disconnected/missing templates accounted for. See Integrated Stronghold provider disposition below. |
| `integrated_villages-1.3.3+1.21.1-neoforge.jar` | `integrated-villages-provider` (97000f2), prior suppression evidence, test_integrated_villages_provider_scope.py | RESOLVED: Twelve existing roots, full component partition, four incompatible legacy addition declarations and existing village suppression. See Integrated Villages disposition below. Shared Integrated API remains open. |
| `kotlinforforge-5.11.0-all.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `letmedespawn-1.21.x-neoforge-1.5.0.jar` | `letmedespawn-provider` (69119c6), test_small_utility_provider_scope.py | RESOLVED: Existing mob persistence/discard behavior; no independent family. See small utility provider dispositions below. |
| `libraryferret-neoforge-1.21.1-4.0.0.jar` | `libraryferret-provider` (8c60e03), test_small_utility_provider_scope.py | RESOLVED: Abstract consumer-supplied jigsaw/placement support and coin content. No independent family. See additional shared provider dispositions below. |
| `lithostitched-1.7.10+beta4-neoforge-21.1.jar` | `lithostitched-alias-code`, `lithostitched-biome-injector-code`, `lithostitched-feature-modifier-code`, `lithostitched-platform-modifier-code`, `lithostitched-pool-additions-code`, `lithostitched-pool-compilation-code`, `lithostitched-processor-registration-code`, `lithostitched-random-block-code`, `lithostitched-street-processor-code`, `lithostitched-surface-lifecycle-code`, `pool-codecs` | Reuse modifier, pool, alias and processor captures; reconcile remaining entry/codec consumers and packaged modifiers. |
| `lootintegrations-1.21.1-4.7.jar` | `lootintegrations-provider` (47047d6), test_small_utility_provider_scope.py | RESOLVED: Core integration loader and loot-list modifier, 43 definitions and seven chest-table targets. No independent family; remains a required loot-attribute input. See disposition below. |
| `mca-neoforge-7.7.11+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar` | Eight capture directories bound by test_moog_library_provider_scope.py; latest registration boundaries ee8e2c0. | RESOLVED: shared generation and modification library; no independent authored family or packaged generation resources. See Moog library provider disposition below. |
| `moonlight-neoforge-1.21.1-3.0.17.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `naturalist-1.0.2-neoforge-1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `oceansdelight-neoforge-1.0.4-1.21.1.jar` | `oceansdelight-provider` (2b575d8), test_oceansdelight_provider_scope.py | RESOLVED: Food content and four existing aquatic-mob loot declarations; no independent family. See Ocean's Delight disposition below. |
| `owo-lib-neoforge-0.12.15.5-beta.1+1.21.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `player-animation-lib-forge-2.0.4+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `polymorph-neoforge-1.1.0+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `prickle-neoforge-1.21.1-21.1.11.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `quickrightclick-1.21.1-1.9.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `railways-0.2.1+neoforge-mc1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `ranged_weapon_api-neoforge-2.3.3+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `regions-unexplored-0.6.1-neoforge-21.1.jar` | `regions-unexplored-feature-code`, `regions-unexplored-feature-config-code` | Reuse feature/config captures; bind modifiers and template-pool component consumers; exclude terrain with rationale. |
| `repurposed_structures-7.5.21+1.21.1-neoforge.jar` | Existing mansion/monument/pool evidence, `repurposed-provider`, `repurposed-feature-roles`, `repurposed-assembly`, `repurposed-datagen-entry`; focused provider and component checks. | RESOLVED: 107 existing roots, 23 dungeon/well configuration candidates, all feature and component roles, common hooks and data-generation entry accounted for below. Canonical grouping and effective eligibility remain separate. |
| `resourcefulconfig-neoforge-1.21-3.0.11.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `resourcefullib-neoforge-1.21-3.0.12.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `ritchiesprojectilelib-2.1.2+mc.1.21.1-neoforge.jar` | `projectile-library-provider` (50bc747), test_small_utility_provider_scope.py | RESOLVED: Projectile entity, chunk-loading and synchronization support; no authored structure family. Packaged mixin files lack loader declarations. See disposition below. |
| `servercore-neoforge-1.5.17+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `shield_api-neoforge-2.2.0.jar` | `shield-api-provider` (a14b5e0), test_small_utility_provider_scope.py | RESOLVED: Custom shield interaction, item attributes, rendering and EMI integration; no independent family. See bundle and shield dispositions below. |
| `simplyswords-neoforge-1.63.0-1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `sparsestructures-neoforge-1.21.1-3.0.jar` | `sparsestructures-provider` (69119c6), test_small_utility_provider_scope.py | RESOLVED: Existing structure-set placement modification; no independent family. See small utility provider dispositions below. |
| `structure_layout_optimizer-neoforge-1.0.12.jar` | `structure-layout-optimizer-provider` (8c60e03), test_small_utility_provider_scope.py | RESOLVED: Existing jigsaw assembly and template filtering modifications. No independent family. See additional shared provider dispositions below. |
| `structure_pool_api-neoforge-1.2.1+1.21.1.jar` | `structure-pool-api-provider` (69119c6), test_small_utility_provider_scope.py | RESOLVED: Caller-supplied pool injection and piece limits; no independent family. See small utility provider dispositions below. |
| `structureessentials-1.21.1-5.0.jar` | `structureessentials-provider` (7a82503), test_small_utility_provider_scope.py | RESOLVED: Existing structure lookup, placement, biome compatibility and diagnostic modifications; no independent family. Frozen activation settings bound below. |
| `supplementaries-neoforge-1.21.1-3.6.8.jar` | `supplementaries-tags-code` | Resolve feature/structure aliases and injected components against existing roots. |
| `tectonic-3.0.22-neoforge-21.1.jar` | `tectonic-provider`, `tectonic-config-selection` (fba027c), test_tectonic_provider_scope.py | RESOLVED: Terrain, placement modifications and the named underground-river lantern candidate. No packaged structure roots, pools or templates. See Tectonic disposition below. |
| `ubesdelight-neoforge-1.21.1-0.4.13.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `worldweaver-21.0.24.jar` | `pool-codecs` | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `wunderlib-21.0.10.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `youre-in-grave-danger-neoforge-2.0.13.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |

## Creating Space packaged component checkpoint

Source continuation: c212c8a selects the bounded entry set and 4d43faf retains
all 39 disassemblies. Manifest SHA-256:
eba1da2e07326fc6b3f57060d05bc7130695911a5fc118be589e2e09a1a515c4.
The exact extraction command and independent r1 comparison are recorded in
sources/creating-space-provider/README.md. The source-coverage case binds all
thirteen annotated entries, nineteen declared mixins and their plugin, and the
six indexed generation-reference classes. Two focused cases pass in 0.25s,
with scoped Ruff and Basedpyright passing. This proves capture coverage of those
mechanisms, not complete semantic coverage of every reachable operation.

CSMixinPlugin.getMixins returns null, shouldApplyMixin returns true, and its
other lifecycle methods do not inject code. No additional mixin list is supplied
by this plugin. CreatingSpace registers the captured CarverInit, common setup,
custom datapack registries and a block-mass reload listener. Continue with the
captured event/mixin and crater/rocket roles and any concrete delegated content
consumer; no need to recapture these 39 sources. The disconnected outpost's
other-consumer disposition and whole-provider closure remain open.

The exact archive is a02eb4c17201f2add8343ebe7b4476890ae9b59a7f5af7e0309f6e00b9c65866,
with 1645 non-directory files. Existing family-decision checks already bind the
four root definitions. The focused component check now accounts for all five
packaged pools and all six world-generation templates against the accepted
pool-traces-content.json.gz input. All five pools are reached. Five templates
are reached; creatingspace:moon/abandoned_outpost is disconnected from those
graphs. The connected outpost uses separate top and basement templates.
Do not count the disconnected template as another family or assert it is unused
by executable code until its other consumers are resolved.

The Mars outpost pool has minecraft:bastion/bridge/legs as its fallback. The
existing graph consequently includes vanilla leg_0 and leg_1 components. This
is a preserved packaged relationship, not evidence that those legs appeared in
a generated Mars site or that the provider adds a bastion family. These four
graphs have no recorded missing references or unresolved pool elements.

The five configured-feature definitions use four minecraft:ore entries and one
minecraft:geode entry, named for nickel, aluminum, cobalt and nickel sulfate.
No custom feature type occurs in these definitions. Executable entry and mixin
roles, custom data consumers and any additional generation routes remain open.
The archive declares a mixin plugin; complete that boundary before provider
closure. Census remains 77 resolved and 59 open.

```sh
uv run pytest -q tests/item8/test_creating_space_provider_scope.py
uv run ruff check tests/item8/test_creating_space_provider_scope.py
uv run basedpyright tests/item8/test_creating_space_provider_scope.py
```

One focused case passed in 0.23s, and both scoped quality checks passed. Reuse
the existing root-decision checks and component graph; no new graph or runtime
measurement was added.

## WDA structure-provider disposition

DungeonsArise-1.21.1-2.1.68-release.jar contributes 40 existing packaged roots,
166 pools and 877 templates. Every packaged root uses minecraft:jigsaw. The
captured six-class executable path registers dungeons_arise:generic_structures,
but none of this archive's 40 root definitions uses that type. It is not another
family. Source capture 1b230be records the mod entry, registration, pool-driven
assembly and caller-supplied placement overload. No independent feature entry or
additional root is supplied by these classes.

The full-payload check accounts for all files, including the six functions.
Their commands create particles/sounds, modify projectile NoGravity and summon
combat evoker fangs; they do not place another structure. Seven processor lists
use minecraft:rule for component block/loot changes. Other data is tags,
advancements, enchantments, loot and predicates; visual assets are translations.
There are no nested archives, service files or mixin entry files in this payload.

Twelve pools and 54 templates are disconnected from the preserved root graphs.
The exact sets are enumerated in test_wda_provider_scope.py and bound to the
preserved archive and graph identities. They include illager castle/hall and old
mushroom-village components, the jungle-tree-house start pool, no-effects wishing
well components, and individual unused pieces from otherwise existing designs.
Disposition: disconnected components, not independently registered families.
This is packaged-graph coverage, not proof that every connected piece generates.

Preserve missing references on four existing roots:

- foundry: missing pool underworld/foundry/foundry_corridor_gears.
- thornborn_towers: missing template thornborn_towers_hanging_bridge_2_medium_terminator.
- bandit_village: missing template bandit_village_deco_3.
- mechanical_nest: missing pool mechanical_nest_decoration and templates
  mechanical_nest_bridge_terminator_6_ and mechanical_nest_spawner_6.

Exact namespaced paths remain in pool-traces-content.json.gz. These are component
failures with assembly uncertainty for later attributes. Do not repair the frozen
baseline or count similarly named unused components as replacements.

```sh
uv run pytest -q tests/item8/test_wda_provider_scope.py
```

One case passes. Scoped Basedpyright passes; Ruff passes after removing an unused
noqa code found in the first static run. Source reproduction is documented in
sources/wda-provider-scope/README.md. No new graph, runtime or measurement system.
Provider dispositions: 27 of 136; 109 remain open in the explicit queue.

## Better Village provider disposition

Better Village replaces components of the existing five vanilla village variants
and modifies their placement through its captured StructureSetMixin. It adds no
independent family. Reuse the complete seven-class source capture in 45ab692 and
the contribution regression from 9595c52, delivered with inventory attribution in
18c7466. No source recapture or new family decision is required.

The full archive consists of those seven classes, nine metadata/documentation
files, 246 vanilla village template replacements and four compatibility JSON
files. Its declared mixins are exactly StructureSetMixin and
AbstractDecorationEntityMixin; the access transformer exposes only the two
StructureTemplatePool template fields. There are no additional resource classes,
functions, nested archives, services or feature definitions in the payload.

The existing contribution regression verifies 244 selected reachable replacements
across desert, plains, savanna, snowy and taiga villages. The two disconnected
components are minecraft:village/snowy/streets/crossroad_01 and straight_05. All
four compatibility targets are absent and their metadata is disabled. Frozen
placement configuration and the captured activation log remain bound by that
regression. Keep the decoration mixin's suppression of error-level logging in
mind when interpreting logs, as already documented in the source README.

```sh
uv run pytest -q tests/item8/test_bettervillage_provider_scope.py tests/item8/test_family_decisions.py -k 'bettervillage or better_village'
```

Two cases pass, 72 unrelated cases deselected. Scoped Ruff and Basedpyright pass
after shortening two overlong access-transformer assertions. No additional runtime
or measurement framework. Provider dispositions: 28 of 136; 108 remain open.

## YUNG Bridges provider disposition

The provider contributes the already recorded nonregistry bridge path. It has
23 configured features: one selector and 22 configurations referencing eleven
templates. These are configuration/layout alternatives, not 23 or eleven accepted
canonical families. Existing grouping remains provisional until the whole-stack
candidate boundary is closed. The registered structure list has no yungsbridges
roots. Existing tests bind actual configured/placed registries, biome modifier,
selector, dimension overlap, template links, generation and processors.

All 31 classes are accounted for by the five source directories named in
test_yungs_bridges_provider_scope.py. The seven remaining registration, service,
configuration and mixin classes were delivered in a20bccf, reproduced using
dfca574. They introduce no further candidate content. YUNG API module annotation
scanning remains part of that shared provider's scope.

The full payload contains fourteen templates, 23 configured features, one placed
feature, five tags, the Forge/NeoForge biome-modifier declarations, known metadata
and the two service registrations. No unexplained additional payload remains.
The existing nonregistry regression binds the NeoForge declaration to the active
selector. Three templates remain explicitly unreferenced: yungsbridges:bridge/wood/
13_0, 13_0_broken and 15_0. They are disconnected layouts, not extra active families.

SuppressLogMixin optionally cancels Util.logAndPauseIfInIde for messages beginning
"Detected setBlock in a far chunk" and containing "yungsbridges:bridge_list". It
adds no generation route. Preserve this logging limitation: absence of that
warning cannot establish absence of far-chunk placement. No baseline change.

```sh
uv run pytest -q tests/item8/test_yungs_bridges_provider_scope.py tests/item8/test_feature_modifier_references.py -k 'yungs_bridge'
```

Seven cases pass, 22 unrelated cases deselected. Scoped Ruff/Basedpyright pass.
No new runtime, graph or measurement framework. Provider dispositions: 29 of 136;
107 remain open. Family grouping and the full Item 8 gate are still incomplete.

## YUNG Extras provider disposition

The provider contributes the existing nonregistry feature entrypoints. Complete
archive accounting covers 29 classes, 62 templates, 62 configured features,
62 placed features, three tags, three loot tables and three biome-modifier
declarations for each of the Forge and NeoForge resource paths. The remaining
payload is known metadata and two service descriptors. No nested archive, mixin,
function or additional unexplained resource remains.

All templates are assigned: 59 through configuration location fields and three
through already recorded desert-generator constants and registration annotations.
The existing contribution tests bind all 62 template identities and their links,
actual configured/placed registries, NeoForge biome additions and vanilla well
removal, code placement, processor content and loot. The three templates outside
explicit JSON location links are not unused; their code links resolve them.
Do not count 62 configured entries as 62 canonical families.

Existing source captures are reused. Seven remaining service, configuration and
RNG-placement classes were delivered in 4d7edec using extractor 04db73f. Their
behavior adds no further authored content. All 29 classes are bound by the focused
full-payload check. The shared YUNG API annotation scanner remains attributable
to its own provider. No baseline configuration or world was changed.

```sh
uv run pytest -q tests/item8/test_yungs_extras_provider_scope.py tests/item8/test_feature_modifier_references.py -k extras
```

Nine cases pass, 20 unrelated cases deselected. Scoped Ruff and Basedpyright pass.
Provider dispositions: 30 of 136; 106 remain open. This resolves provider coverage,
not canonical grouping or the final Item 8 gate.

## Moog library provider disposition

The shared library supplies the existing generic jigsaw and Nether jigsaw
implementations, pool elements/pieces, placement modifiers, processors and terrain
adaptation. Its role is implementing and modifying consumer-provided generation.
It contributes no independent authored family. The four Moog data providers have
separate, already closed coverage dispositions; their grouping remains provisional.

The full nonclass payload is exhausted by metadata, two declared mixin configs,
one registry service, access declarations, pack metadata, icon and license.
There are no packaged roots, features, pools, templates, functions, nested JARs
or other data resources. The two loader/subscriber entry classes are the already
captured NeoForge entry and the build-time NBT datagen subscriber. All sixteen
declared mixins and the sole service implementation have preserved captures.
The source roles, not a zero-hit keyword result, establish this disposition.

Common/NeoForge entry captures bind the registration and lifecycle callbacks.
Registration wrappers forward supplied names and suppliers to DeferredRegister;
they do not introduce an extra design. Lifecycle callbacks start/stop locating
infrastructure, register the trial-spawner JSON reload listener, and expose debug
commands. The direct locate handlers search supplied registered structures.
The datagen callback writes through DataGenerator, not a live world event.

Mixin and direct-helper captures resolve tagged basalt/delta suppression, locate
radius changes, codec weight limits, optional jigsaw-block retention and terrain
adaptation around existing starts. Accessors expose existing pieces/pools and
resources. Reuse the previously captured pool/version/generator paths to interpret
consumer resources. Do not count registered implementation types or terrain
adaptation as families. No need to trace unrelated geometry or registry containers.

Keep runtime activation and effective attributes separate: optional mixins are
not proved active by class presence; debug flags initially default false but can
change; invalid trial-spawner JSON is logged and skipped. Effective processors,
loot and spawner attributes still need consumer attribution during the later
attribute pass. This closure does not certify those attributes or gameplay.

```sh
uv run pytest -q tests/item8/test_moog_library_provider_scope.py tests/item8/test_moog_data_provider_scope.py
uv run ruff check tests/item8/test_moog_library_provider_scope.py
uv run basedpyright tests/item8/test_moog_library_provider_scope.py
```

Five focused cases pass. Scoped checks pass after type annotations and long
string formatting corrections; no behavioral failure was hidden. Eight existing
capture directories are hash-bound to the frozen archive. Latest five-class
capture ee8e2c0 reproduced using f28c96b. No new runtime or measurement framework.
Provider dispositions: 31 of 136; 105 remain open.

## Integrated Stronghold provider disposition

The provider contributes the existing integrated_stronghold:stronghold root,
using integrated_api:generic_structure and integrated_api:stronghold placement.
All 44 packaged pools are connected to that root. The trace also reaches the
vanilla minecraft:empty pool. Of 61 packaged templates, three are disconnected:

- integrated_stronghold:portal_room/portal_room_endrem.
- integrated_stronghold:small_room/armory_left.
- integrated_stronghold:small_room/armory_right.

The root references missing small_room/small_armory_left and small_armory_right
templates in the same namespace. These are preserved component failures.
Do not substitute the similarly named packaged armories or count the alternate
portal room as a separate active family. The existing root/family regression
already binds its runtime registry identity, start pool and spawn override.

All nine classes are captured in 0bca5a4 using f70a1a0 and reproduced independently.
The NeoForge entry registers sounds, disc items and a creative tab. Common entry
and the generated platform bridge introduce no additional generation. Both
declared mixins modify vanilla stronghold generation/locating, as described in
the source README. The artificial far-away locate result is not a structure
observation. The packaged eye_of_ender_located tag replaces its values with the
Integrated Stronghold root; effective stack tag selection remains separate.

The complete archive payload contains only these classes, metadata/refmap,
visual/audio assets, the known root/set/pools/templates/processors, loot,
spawner configuration, tags, music, recipe and advancement resources. No extra
feature, function, service or nested archive remains unexplained. Shared
Integrated API processors and placement are attributed to that provider; this
closure does not certify effective loot/spawner behavior or every attribute.

```sh
uv run pytest -q tests/item8/test_integrated_stronghold_provider_scope.py tests/item8/test_family_decisions.py -k integrated_stronghold
```

Two cases pass, 72 unrelated cases deselected; scoped Ruff/Basedpyright pass.
The first new scope assertion omitted the trace's external minecraft:empty pool;
it was corrected to preserve that reference explicitly. Type/line formatting was
also corrected. No evidence, baseline or family decision was changed to pass.
Provider dispositions: 32 of 136; 104 remain open.

## AdoraBuild provider disposition

All 106 packaged roots are already present in the preserved inventory and runtime
coverage regression. They use vanilla jigsaw (69), End jigsaw (16), Nether jigsaw
(14) and Overworld jigsaw (7). The latter three are implementation types registered
by this provider, not three additional families. Existing grouping remains
provisional until whole-stack candidate coverage and canonical reconciliation.

All 110 packaged pools and 121 templates occur in the preserved root graphs.
No disconnected packaged pool or template remains. The basalt_chambers_large_1
root retains its missing minecraft:basalt_chambers/chambers pool reference.
This is a component failure with assembly uncertainty, not another family or
permission to substitute an alternate namespaced resource. Connected templates
are potential components, not proof of observed placement.

Source capture 6aac21f accounts for all seven classes and reproduces with
6fcc20c. The entry registers three custom structure codecs. Registry wrappers
forward supplied entries; custom generators select heights and invoke vanilla
JigsawPlacement with configured pools/aliases. No additional independent feature,
placement event or hardcoded authored design appears in these complete paths.

The full payload is exhausted by these classes, metadata, logos/translations,
roots/sets/pools/templates, vanilla rule processor lists, tags, loot and
advancements. There are no mixin descriptors, functions, nested JARs, services
or separate feature resources. Frozen Cristel Lib configuration/selection and
effective family attributes remain separately attributable to their consumers.

```sh
uv run pytest -q tests/item8/test_adorabuild_provider_scope.py tests/item8/test_family_decisions.py -k adorabuild
```

Two cases pass, 72 unrelated cases deselected; scoped Ruff/Basedpyright pass.
Initial scope-test corrections accounted for two packaged image assets and
stopped strict JSON parsing of the commented end structure-set resource. The
existing preserved graph/catalog remains the resource-processing authority;
no alternate parser or rewritten resource was introduced. Static flow/complexity
findings were resolved within the direct test. No new runtime or measurement.
Provider dispositions: 33 of 136; 103 remain open.

## CTOV selection checkpoint (provider still open)

The captured callback and frozen ctov-common.toml select 63 village roots
(21 configured variants at three enabled sizes) and eleven outpost roots, with
weights 10/4/1 for villages and 1 for outposts. All 74 are in the captured registry.
Four of the 78 registered CTOV roots are outside this callback's selected list:
pillager_outpost_mesa and small/medium/large village_underground. This is the
scope of CTOV's callback, not proof that no other provider could modify eligibility.
Do not remove registered candidates or confuse eligibility with family grouping.

All 1,019 CTOV modifier JSON records in the preserved catalog are template-pool
element additions. Exactly 63 pass the captured NeoForge mod-presence conditions:
21 each for chefsdelight, farmersdelight and village_taverns. The other 956 fail
those conditions. This establishes component-addition selection, not successful
placement or completed accounting of every template. Both source catalog and
actual mod-list log identities are bound by the focused test.

```sh
uv run pytest -q tests/item8/test_ctov_provider_selection.py
```

Two cases pass; scoped Ruff and Basedpyright pass. The test binds the preserved
source capture and frozen config, reuses the existing condition evaluator, and
adds no parser or measurement system. Remaining: compatibility directories/ZIP,
full payload, disconnected/missing components and their modifier relationships.
Provider count remains 33 resolved, 103 open.

### CTOV bundled-resource disposition

The extended-mushrooms ZIP contains five processor JSON files and pack metadata,
all byte-identical to the loose bundled copies. The loose metadata is located at
ctov-extended-mushrooms/data/pack.mcmeta. One processor list uses apply_random;
the other four use block_swap for mushroom component materials. These are
component transformations, not family definitions. No executable nested archive
or independent root occurs in that ZIP.

The savage-and-ravage add-on contains eleven base_plate.nbt outpost components
and pack metadata. They are under the bundled prefix and legacy structures path,
not additional root definitions. Captured CTOV entry code provides no loader
for either bundled pack. Preserve the files without enabling or migrating them.

The two .jso files contain add_structure_set_entries documents referencing
eleven existing outposts and 63 existing village roots. They are outside the
JSON modifier catalog, not extra families. Their entries all have weight 1;
do not substitute those weights for the active callback's frozen 10/4/1 village
weights. The callback is the separately verified selection path.

```sh
uv run pytest -q tests/item8/test_ctov_bundled_resources.py
```

One focused case and scoped Ruff/Basedpyright pass. The initial expected
processor-type set was corrected after inspecting the four block_swap documents;
no source resource was changed. Remaining CTOV coverage is ordinary full-payload
accounting and disconnected/missing component relationships. Counts remain
33 resolved, 103 open.


## CTOV provider candidate coverage

The complete frozen archive is accounted for by test_ctov_provider_scope.py,
using the already delivered twelve-class source, callback selection and bundle
checks. CTOV contributes 78 existing root candidates and modifies their component
pools and processors. Its only placed feature references vanilla forest flowers,
not another authored structure. The underground structure-set declaration has a
.txt extension; preserve its references to the three existing underground roots
without treating it as an active JSON set. Legacy Monobank templates and Monobank
and Wares loot are compatibility components, not independent roots.

Of 181 packaged current-path pools, 19 are outside CTOV root graphs: eleven
common village pools (bees, flowers, pet, pet_aquatic, five villager and two
waystone variants), mesa_fortified/tree, and seven Monobank village pools.
The focused check preserves their exact IDs. Of 2,093 current-path templates,
960 occur in the captured CTOV root graphs and 1,133 do not. Of the latter,
1,005 have references in compatibility modifiers whose mod conditions fail in
the frozen runtime. None is referenced by a condition-passing CTOV modifier.
The remaining 128 are disconnected components: 44 animal templates, 56 jobsites,
three decorations, eight allay cages, five trees, one target, seven road pieces,
three houses and one bee component. These are unused by the inspected provider
routes, not a claim that other providers or manual commands cannot place them.
No disconnected component adds an independent root or family merely by existing.

Twenty-seven CTOV root traces retain missing-resource records; none has an
unresolved pool-element codec. Existing CTOV family regressions retain the
missing-component and mesa/badlands alias findings. Do not repair the baseline
or infer actual placement from these potential graphs. Whole-stack overrides
and final village/outpost family grouping remain separate inventory work.

```sh
uv run pytest -q tests/item8/test_ctov_provider_scope.py tests/item8/test_ctov_provider_selection.py tests/item8/test_ctov_bundled_resources.py tests/item8/test_family_decisions.py -k ctov
uv run ruff check tests/item8/test_ctov_provider_scope.py
uv run basedpyright tests/item8/test_ctov_provider_scope.py
```

Seven focused cases pass. Basedpyright passes; three initial line-length findings
were formatted and Ruff then passed. An exploratory count that unwrapped only
limited elements was incomplete: accounting for guaranteed delegates changes
inactive references from 985 to 1,005 and residual components from 148 to 128.
Only the complete tracked check supports the accepted partition above. No new
runtime experiment, parser, production graph behavior or family decision changed.
Provider dispositions now cover 34 of 136; 102 remain in the exact queue.

## Small utility provider dispositions

Six complete archives are now accounted for by the parameterized
`test_small_utility_provider_scope.py`. Source capture 69119c6 preserves all 69
classes, including entry annotations, subscribers, callbacks, mixins and the
Sparse Structures service implementation. Exact identities and reproduction
commands are in `sources/small-utility-providers.md`. The test binds every class
to that source and accounts explicitly for every remaining file. No archive has
unexplained data, nested executable content or additional entry declarations.

| Provider | Supported role | Family-candidate disposition |
| --- | --- | --- |
| AI Improvements | Goal removal and look-control changes on existing entities | No authored structures or generation entry. |
| AttributeFix | Configured bounds on existing ranged attributes | No authored structures or generation entry. |
| Leaves Be Gone | Leaf-distance and random-tick scheduling, with chunk tick serialization | Existing vegetation behavior; no authored structure candidate. |
| Let Me Despawn | Equipment-related mob persistence and discard behavior | No structure candidate; retain relevance to existing authored enemies. |
| Sparse Structures | Modifies existing structure-set placement, codec bounds and locate arithmetic | No new root, pool, template or authored family. |
| Structure Pool API | Adds consumer-supplied templates to existing pools and tracks piece limits | Shared component mechanism; no packaged component or independent family. |

The last two libraries are not excluded as irrelevant: their modifying roles
are explicitly recorded. Existing Item 8 placement inputs and Village Taverns'
conditional fallback relationship are reused. Other consumers are reconciled in
their own provider rows. Configured combat, despawn and placement effects remain
part of applicable downstream attributes, not a reason to trace unrelated helper
internals during candidate enumeration. No baseline setting changed.

```sh
uv run pytest -q tests/item8/test_small_utility_provider_scope.py
uv run ruff check tests/item8/test_small_utility_provider_scope.py
uv run basedpyright tests/item8/test_small_utility_provider_scope.py
```

Six cases pass. Initial checks found one overlong line and an untyped empty set;
formatting and a set[str] annotation resolve them. Scoped Ruff and Basedpyright
pass. Provider dispositions: 40 of 136, with 96 remaining in the exact queue.
Canonical grouping and family attributes have not been advanced by this closure.

## Additional shared provider dispositions

Almanac, Library Ferret and Structure Layout Optimizer have complete supported
provider roles. All 38 classes are preserved in 8c60e03 using selector 4f65e40;
independent captures reproduced exactly. Identities, commands and inspected
entry/helper boundaries are in `sources/small-utility-providers.md`. The existing
small-utility test now includes these three archive cases and explicitly accounts
for their full payload, including all declared mixins and service implementations.

- Almanac: configuration/reload commands, command callback dispatch, equipment-drop
  support and item custom-data cleanup. It adds no structure-generation route.
  Its existing Let Me Despawn relationship remains relevant to mob attributes.
- Library Ferret: coin items and visual/recipe content; abstract jigsaw generation,
  placement and configuration bases for consumer-supplied structures. No concrete
  authored generator, root, pool or template is packaged. Its ten legacy-path
  recipes use smelting/blasting. Do not reinterpret helpers as families or migrate
  those recipes as part of this inventory.
- Structure Layout Optimizer: collision, connector, candidate-order and template
  filtering modifications on existing structures. Its service supplies a method
  name for processor inspection. No independent authored content is contributed.
  Provider closure does not claim unchanged layout outcomes or measured performance.

```sh
uv run pytest -q tests/item8/test_small_utility_provider_scope.py
uv run ruff check tests/item8/test_small_utility_provider_scope.py
uv run basedpyright tests/item8/test_small_utility_provider_scope.py
```

All nine cases pass, including the previous six. Ruff and Basedpyright pass.
No new measurement, framework, baseline configuration or family grouping change.
Provider dispositions now cover 43 of 136; 93 remain in the exact queue. Continue
whole-provider candidate reconciliation before detailed family attributes.

## Ocean's Delight provider disposition

All 15 classes are captured in 2b575d8 using selector 75232ba and independently
reproduced. The mod entry registers food blocks, items and a creative tab, plus
client setup. The only auto-subscriber installs build-time recipe/model/tag/language
providers. It does not introduce an authored generation path. Full archive
accounting covers 67 visual assets, 31 recipes, 27 recipe-unlock advancements,
five tags, four loot modifiers, their global list, five packaged build caches,
two metadata files and the logo. No root, pool, template, nested archive, service
or mixin is unexplained.

The four packaged farmersdelight:add_item declarations target elder guardian,
guardian, squid and glow squid. Their added items are respectively
`oceansdelight:elder_guardian_slab`, `oceansdelight:guardian` and
`oceansdelight:tentacles` for both squid types. The elder-guardian and squid cut
modifiers require an attacker holding a Farmer's Delight knife; guardian_drop
has only the guardian entity condition. The global list has replace=false and
names these four declarations. This is loot provenance for existing mobs,
including those in existing structures, not four new families. Effective combined
loot still depends on resource selection and the Farmer's Delight implementation.

```sh
uv run pytest -q tests/item8/test_oceansdelight_provider_scope.py
uv run ruff check tests/item8/test_oceansdelight_provider_scope.py
uv run basedpyright tests/item8/test_oceansdelight_provider_scope.py
```

One focused case passes. Initial lint/type findings were three long lines and
two untyped JSON values; formatting and JsonValue casts resolve them. Ruff and
Basedpyright pass. No new measurement, production behavior, baseline configuration
or family grouping changed. Provider dispositions: 44 of 136, with 92 open.

## Bundle and shield provider dispositions

Bundle API and Shield API contribute no independent structure family. Source
capture a14b5e0, using 49dd5dd, preserves all 30 classes and reproduces exactly.
Their full payloads contain only these classes, loader metadata, refmaps, mixin
declarations and icons. No generation resource, template, script, nested archive
or unexplained entry point remains. The existing parameterized provider test
binds the complete archives and preserves all declared mixin targets.

Bundle API supplies stored item components, a content predicate, container-content
manipulation, bundle item interaction and client rendering. Shield API supplies
custom shield repair/attributes/equip sounds, player shield damage/cooldown and axe
interaction hooks, client model predicates and EMI repair-recipe display. These
are player item/combat mechanisms, not authored world layouts. The Shield API
MinecraftClientMixin is listed in its common mixin declaration; preserve this
fact without inventing a newly observed runtime failure or changing the baseline.

```sh
uv run pytest -q tests/item8/test_small_utility_provider_scope.py
uv run ruff check tests/item8/test_small_utility_provider_scope.py
uv run basedpyright tests/item8/test_small_utility_provider_scope.py
```

Eleven cases pass. The first two added cases incorrectly included each client
subscriber in the @Mod entry set. The test and source explanation now distinguish
the one @Mod class from the client EventBusSubscriber in each archive. A local
complexity exception keeps these explicit cases in the existing test without
adding an abstraction. Scoped Ruff and Basedpyright pass. Provider dispositions:
46 of 136 resolved, 90 open. No family grouping or detailed attribute work resumed.

## Projectile library provider disposition

Ritchie's Projectile Library contributes projectile/chunk-loading/network support,
not an independent authored structure family. All 34 classes are preserved in
50bc747 using 0cbba5c and reproduced independently. Its @Mod entry and two
subscribers configure network, player-login, level-tick and client effects. The
saved chunk manager services supplied chunk coordinates; ProjectileBurst supplies
abstract projectile behavior and collision callbacks. These may affect gameplay
and loaded chunks, but introduce no authored root, layout, pool or template.

Full archive accounting covers every class and seven other files: manifest,
NeoForge metadata, icon, pack metadata, access widener and two mixin JSON files.
The first check correctly failed because neither mixin file is declared in the
loader TOML, and the manifest contains only its version header. The check now
preserves that exact state and separately binds the packaged mixin classes.
The common file references ServerEntityMixin, implementing precise motion sync;
the Forge file's list is empty. Do not present this code as empirically activated,
repair the baseline or infer a new compatibility failure from its packaging alone.

```sh
uv run pytest -q tests/item8/test_small_utility_provider_scope.py
uv run ruff check tests/item8/test_small_utility_provider_scope.py
uv run basedpyright tests/item8/test_small_utility_provider_scope.py
```

Twelve cases pass. The explicit archive case required a local branch-count lint
exception, retaining the existing direct test instead of a new metadata framework.
Ruff and Basedpyright pass. No additional measurement or family grouping change.
Provider dispositions: 47 of 136 resolved, 89 open. Continue candidate completeness
before detailed attributes.

## Terralith provider candidate disposition

Source b87f3bb preserves all eleven classes and reproduces exactly. The entry
loads configuration and registers its resource-condition codec; client classes
provide configuration UI. The declared mixin list and access transformer are
empty. No separate code-authored generator, nested executable or service is
present. The focused check accounts for every one of the archive's 2,075 files.
Visual assets, biome/structure icon metadata, recipes, advancement/loot data,
tags, biome definitions and terrain resources are not additional structure roots.

All 28 packaged roots use minecraft:jigsaw and have existing captured root
graphs. Of 49 pools, nothing, spire and village/baby_villager are outside those
graphs. Of 173 templates, 126 are connected and 47 are disconnected. Their exact
IDs are preserved in the focused check. The disconnected content includes old
ruins, decorative components, village houses and a dungeon template. No inspected
provider route places these as independent families; this does not assert that
other providers or manual commands cannot reference them. The fortified desert
village retains missing templates village/desert/houses/farmer and toolsmith1.
Do not substitute the packaged farm1 template. No root has an unresolved pool
element codec. These are potential component graphs, not observed placement.

All six NeoForge overlay conditions evaluate false under the frozen Terralith
configuration. In particular custom_structures=true prevents the disabling
overlay from replacing the seven ordinary structure sets. The remaining disabled
overlays concern intro text, skylands, terrain slabs, recipes and stone generation.
The parallel Fabric declarations are not six more contributions in this NeoForge
stack. Ordinary functions initialize scoreboards, schedule welcome text, mark
bundle recipe detection and provide a manual spreadplayers testing command.
None places authored layouts. The testing command was inspected, not executed.

The 492 packaged configured-feature documents, including overlay copies, use
vanilla feature codecs for trees, vegetation, terrain, ores and compositions.
Their nested types also use vanilla codecs. That fact alone is not an exclusion
of authored designs. Inspection retains the following explicit dispositions:

| Candidate or contribution | Disposition |
| --- | --- |
| Existing 28 Terralith structure roots | Retain existing root candidates; canonical design/variant reconciliation is still separate. |
| terralith:cave/frostfire/frostfire_ceiling hanging ornament | Named nonregistry candidate. The ceiling vegetation selector has a 0.07 branch constructing a downward chain column with a hanging soul lantern. Its placed feature is referenced by frostfire_caves. Whether this recurring ornament warrants an independent family or an ambient-decoration exclusion remains a named canonical grouping decision, not unknown candidate membership. |
| terralith:yellowstone/vents | Terrain effect. A simple-block feature places campfires below magma and water, with a downward environment scan. Caldera and Yellowstone reference the placed feature. This is not an authored campsite layout. |
| Remaining tree, plant, ore, cave and surface features | Terrain/vegetation contributions, including feature compositions. No independent authored template placement or custom generator is hidden behind their vanilla feature types. |
| Disconnected pools/templates | Inactive through the inspected provider routes; retained as components with exact IDs, not promoted to families by file count. |

The new named ornament question does not resume detailed attributes or settle
the final family denominator. Whole-stack resource selection and canonical
grouping remain required. No baseline configuration or production code changed.

```sh
uv run pytest -q tests/item8/test_terralith_provider_scope.py
uv run ruff check tests/item8/test_terralith_provider_scope.py
uv run basedpyright tests/item8/test_terralith_provider_scope.py
```

Two focused cases pass; scoped Ruff and Basedpyright pass. Initial type findings
were resolved with explicit JSON type casts. A local statement-count exception
keeps the complete payload check together without introducing a helper framework.
Provider dispositions: 48 of 136 resolved, 88 open. Candidate completeness remains
the immediate task, followed by named canonical grouping decisions, all eleven
attributes, the applicable final gate and the required PR review/merge workflow.

## Tectonic provider candidate disposition

Source fba027c preserves 31 directly relevant classes across the entry capture
and ConfigState selection capture. Both reproduced exactly. The focused check
accounts for all 310 files, including 57 classes, and binds both annotated mod
entries and all thirteen declared mixins. The remaining uncaptured classes are
configuration records and client UI consumed by those entries. No unaccounted
loader/subscriber, service or nested executable entry remains. WorldCarverMixin
is packaged but not declared; do not infer its activation.

The built-in server datapack has 245 files. It contains density functions,
noise, noise settings, carvers, placed/configured features, tags, six modifiers
and pack metadata. There are no packaged structure roots, pools or templates.
All files, including inactive overlay data, have explicit resource categories in
the focused check. The generator code supplies scalar terrain functions, feature
placement positions and dimension/noise height changes. Commands locate terrain
using density predicates; the compatibility exporter writes configuration JSON.
These mechanisms add no independent authored layout.

| Contribution | Candidate disposition |
| --- | --- |
| tectonic:underground_river/lanterns | Named nonregistry ornament candidate. A downward column has two to eight chain blocks and one hanging lantern. A conditional add_features modifier targets Overworld biomes. Frozen mod_enabled and river_lanterns are true. Placement also depends on underground-river density, ceiling and air predicates. Retain the family-versus-ambient-decoration decision alongside Terralith's Frostfire ornament; neither is silently omitted or automatically counted as a family. |
| Underground-river ice | Simple ice-block terrain feature. Its modifier is disabled by frozen river_ice=false. |
| Underground-river lichen | Adds the existing vanilla glow_lichen feature with river-density placement restrictions; vegetation, not a new authored layout. |
| Ocean-monument offset | StructurePieceMixin moves existing OCEAN_MONUMENT_BUILDING bounding boxes while enabled. Frozen monument_offset is -30. Preserve this placement modifier for existing monument attributes, not a second monument family. |
| Remaining terrain modifiers and resources | Dimension/noise height limits, frozen-ocean climate, island density, carvers, noise and ore placement. No independent structural candidate. |

The normal overlay.mod applies at the frozen data format. Both format-82
overlays are inapplicable to Minecraft 1.21.1; the extra configured lantern
document there uses iron_chain instead of chain and is not an additional active
design. ConfigState maps no_carvers to the negation of carvers_enabled. With the
frozen values, no_carvers, ore_fix and ultrasmooth conditions are false. The
Terralith compatibility overlay concerns terrain integration and adds no authored
layout. Selection and potential placement are not generated-world observations.

```sh
uv run pytest -q tests/item8/test_tectonic_provider_scope.py
uv run ruff check tests/item8/test_tectonic_provider_scope.py
uv run basedpyright tests/item8/test_tectonic_provider_scope.py
```

Two focused cases pass. Initial lint findings were two long lines and one short
ambiguous loop variable; formatting and naming fixes resolve them. Scoped Ruff
and Basedpyright pass. No runtime measurement, new framework or baseline change.
Provider dispositions: 49 of 136 resolved, 87 open. Continue the remaining
provider census before canonical grouping and detailed family attributes.

## Explorations provider candidate disposition

Source 0e6f5e4 binds all 33 classes and reproduced independently. The earlier
scarecrow, Slime Cave and deepslate interpretations are reused. The mod entry
registers the scarecrow, two existing custom structure types, their piece and
processor support, and tree decorators. ServerAboutToStartEvent loads the frozen
statue configuration and mutates target village pools. Two service implementations
provide platform access and registry forwarding; two accessor mixins support
pool mutation and tree-decorator registration. No unexplained executable entry
or resource category remains in the 201-file archive.

All ten packaged structure roots match the captured runtime registry. Nine have
pool graphs; the tenth is the already inspected single-template Slime Cave.
All fifteen packaged pools are connected. Of 55 templates, 49 occur in the nine
root graphs. The remaining six have explicit dispositions: slime_cave belongs to
its custom generator, statue_1 through statue_4 are injected village components,
and underground_temple/intersections/corner is disconnected. The temple graph
instead references missing underground_temple/intrusions/corner and
underground_temple/rooms/small_hall_down. Do not silently replace either reference
or enable the unused component. No graph has an unresolved pool-element codec.

| Contribution | Candidate disposition |
| --- | --- |
| Ten existing registry roots | Retain existing candidates, including the custom Slime Cave and underground temple. Custom generator classes are not additional families. |
| Scarecrow | One five-position figure with nine material variants. Each variant has a configured feature, placed feature and biome modifier using its matching biome tag. The unsuffixed selector references the same nine configured variants, so it is not a tenth design. |
| explorations:large_mushroom | Named decorated-mushroom candidate. A vanilla tree codec builds mushroom-stem and brown-mushroom geometry with the custom lantern decorator. The placed feature and biome modifier are present. Resolve authored-landmark versus decorated-vegetation grouping explicitly; do not exclude it just because its outer codec is vanilla. |
| Four statue templates | Components injected into minecraft:village/{plains,savanna,snowy,taiga}/houses. Each template has weight 2 in plains/savanna, 3 in snowy and 4 in taiga under the frozen config. These are not independent roots or sixteen families. |
| Cave-vine decorator and block processors | Shared vegetation and existing-piece transformations. No packaged configured feature uses the cave-vine decorator. External consumers remain part of whole-stack reconciliation. |
| One disconnected temple-corner template | Unused by the inspected provider routes; retained without correcting the different missing corner reference. |

The lantern decorator uses Collections.shuffle without the generation random
source when selecting leaves. Preserve this limitation; candidate coverage is
not a claim of deterministic ornament positions. Existing Slime Cave marker
write/insertion limitations also remain. No baseline content was repaired and
no new runtime measurement was run.

```sh
uv run pytest -q tests/item8/test_explorations_provider_scope.py
uv run ruff check tests/item8/test_explorations_provider_scope.py
uv run basedpyright tests/item8/test_explorations_provider_scope.py
```

Two focused cases pass. The first check disproved an assumed decor pool suffix:
VillageType's actual concatenation recipe is village/{type}/houses. The source
explanation and test now bind houses explicitly. One long line was formatted;
Ruff and Basedpyright pass. Provider dispositions: 50 of 136 resolved, 86 open.
Continue the provider census; canonical grouping, complete attributes and final
delivery gates remain incomplete.

## Illager Invasion nested dependency checkpoint

The complete archive inspection found a declared nested executable,
META-INF/jars/extensibleenums-neoforge-21.1.1.jar, SHA-256
35720e0569288b37fe59dfd3781691019d24ce1fab48623980b9d7a9b5af2e1c.
Its candidate role must be supported before closing the parent provider.
The existing source-capture tool supports only bundled Tiny Config and rejects
this parent/path. The smallest necessary extension is a second exact pinned
parent/path/hash case in that existing path. This resolves a concrete uncovered
entry boundary, not a new measurement framework or audit of enum internals.
Provider count remains 50 resolved, 86 open until the parent disposition passes.

## Illager Invasion provider candidate disposition

Source e0f2c9a preserves the directly relevant parent entry, registry, callback,
configuration, mixin and generator classes, plus all sixteen nested Extensible
Enums classes. Both captures reproduce exactly. The focused check binds both
annotated entries in each archive, every declared mixin, all source identities,
and the exact nested archive identity. It accounts for every parent file and
every nested file; no unexplained data category, service or nested executable
remains. The parent has 499 files, including 137 classes and 203 visual assets.

Five packaged roots match the captured runtime registry: firecaller_hut,
illager_fort, illusioner_tower, labyrinth and sorcerer_hut. Four use vanilla
jigsaw; Labyrinth delegates to vanilla jigsaw assembly and requires the resulting
stub Y to be at most 47. This is an existing root's placement condition, not a
new family. The no-liquid pool element implementations are reused from the
existing pool-codec evidence.

Of 25 packaged pools, 24 occur in these root graphs. The disconnected pool is
illagerinvasion:mobs/pillager. Of 63 packaged templates, 49 occur in the graphs;
the remainder is the corresponding pillager template and thirteen vanilla-
namespace woodland-mansion replacements. The exact replacement IDs are preserved
in the focused check. All five graphs have no missing resources or unresolved
pool-element codecs. These facts describe potential component relationships,
not successful world generation.

| Contribution | Candidate disposition |
| --- | --- |
| Five existing roots | Existing authored candidate families; retain their component graphs and placement conditions. |
| Thirteen woodland-mansion templates | Replacement components of the existing mansion family. Do not count them as thirteen independent structures. Effective whole-stack resource selection remains an attribute/input reconciliation task. |
| WoodlandMansionPieceMixin | Handles custom mob markers within existing mansion pieces. Entity creation, persistence and insertion requests are authored encounter provenance; no new layout. |
| Disconnected pillager pool/template | Component unused by the inspected provider routes. Preserve it without promoting an entity template to a family or asserting that external consumers cannot use it. |
| Mob, raid, patrol, villager-goal and loot callbacks | Modifications and encounter/loot sources for existing content. No separate authored layout or feature-based structure route. |
| Bundled Extensible Enums | Caller-supplied enum extension, used here for raid member registration. No generation resources, templates or independent family; both declared mixin lists are empty. |

Other packaged data is loot, recipes/unlock advancements, tags and trim material.
No configured feature, placed feature, script, additional root mechanism or
unassigned structure component is present. Remaining gameplay classes implement
entities, AI, items, block/menu behavior, rendering and data generation consumed
by the inspected entries. This candidate pass does not audit unrelated combat or
enum mutation internals or certify shared-library correctness.

```sh
uv run pytest -q tests/item8/test_illagerinvasion_provider_scope.py
uv run ruff check tests/item8/test_illagerinvasion_provider_scope.py
uv run basedpyright tests/item8/test_illagerinvasion_provider_scope.py
```

Two focused cases pass; Ruff and Basedpyright pass. No runtime measurement or
baseline change. Provider dispositions: 51 of 136 resolved, 85 open. Continue
candidate completeness before canonical grouping and detailed attributes.

## Save and structure utility dispositions

Fast Async World Save and Structure Essentials have complete supported provider
roles. Source 7a82503 preserves all 32 classes; independent captures reproduce
exactly. Commands, identities and entry interpretation are in
sources/small-utility-providers.md. The existing parameterized test accounts for
every file in both archives, binds the single mod entry in each, and checks every
declared mixin and the Structure Essentials plugin. No nested executable,
service, authored generation resource, root, pool or template is unaccounted for.

Fast Async World Save changes saved-data and level-data write execution and
saved-data filename handling. It provides no independent family. This is a
provider-role disposition, not a new claim of persistence correctness or speed.

Structure Essentials modifies existing generation and lookup behavior, with
inspection/timing commands and error handling. Its plugin permits the declared
mixins under the frozen disableLegacyRandomCrashes=true setting. The frozen
configuration disables automatic biome expansion and minimum-distance exclusion
and sets spacingSeparationModifier=1.0. The complete configuration hash is bound
by the focused test. Search limits and placement exception handling must remain
part of interpreting existing observations; provider closure does not claim that
every feature placement succeeds or that all lookup failures mean absence.

```sh
uv run pytest -q tests/item8/test_small_utility_provider_scope.py
uv run ruff check tests/item8/test_small_utility_provider_scope.py
uv run basedpyright tests/item8/test_small_utility_provider_scope.py
```

Fourteen cases pass, including the twelve previously accepted providers. A local
statement-count lint exception keeps the explicit archive/config cases in the
existing test instead of introducing a validation framework. Ruff and Basedpyright
pass. No runtime measurement, baseline change or detailed family grouping work.
Provider dispositions: 53 of 136 resolved, 83 open. Continue the remaining census.

## BetterEnd feature candidate reconciliation

The earlier crashed-ship uncertainty is narrowed by existing packaged evidence,
without another source capture or world run. Its configured feature is embedded
inside `data/betterend/worldgen/placed_feature/crashed_ship.json`; absence of a
separate configured-feature registry ID does not make it inactive. The placed ID
`betterend:crashed_ship` exists in the captured runtime registry. Its declaration
uses rarity 500, in-square placement and biome filtering. These inputs are not an
observed occurrence rate.

The packaged route has 27 explicit biome consumers, all named in
`tests/item8/test_betterend_feature_candidates.py`. Twenty-one occur in the
captured End biome source. Six cave-biome references do not: empty_aurora_cave,
empty_end_cave, empty_smaragdant_cave, jade_cave, lush_aurora_cave and
lush_smaragdant_cave. Do not infer that those six are globally unreachable from
this biome-source result. The additional
`data/betterend/wover/worldgen/biome_modifications/defaults.json` declaration
requests the ship for non-BetterEnd biomes with Wover End barrens, midland or
highland tags. Its shared modifier semantics remain in WorldWeaver's census row;
this does not erase the 21 directly linked biome-source candidates.

The preserved CrashedShipFeature selects `minecraft:end_city/ship`, with erosion
and placement distinct from a ship attached to an End city. Retain one named
crashed-ship candidate. Its source precheck uses X for both squared chunk
coordinates, requires the resulting sum to reach 3600, Y greater than 5, and an
End-stone-tag block below. Do not repair that behavior or claim generated-world
occurrence from packaged eligibility. Reuse the existing source manifest
7a3fe03fddacad093573ad808d94b41463643acf11df321dc2b7a6fdeb5dd30d.

All six building-list configured IDs and corresponding placed IDs exist in the
runtime registries. Each is directly referenced by its corresponding packaged
biome, and all six biomes occur in the captured End biome source. Their placed
features declare rarity 10, in-square placement and biome filtering. Existing
BuildingListFeature source also imposes an even chunk-coordinate sum, Y greater
than 58, air at the placement point and terrain-tag support below. It selects one
configured template, with rotation/mirror variations. A list is not an assembled
village or a family count.

The following partition accounts for every choice. Paths share
`/data/betterend/structure/biome/<biome>/` and end in `.nbt`. Number intervals are
inclusive. The focused test asserts the exact sets, verifies every template
exists and decodes it using the existing template decoder.

| Biome/list prefix | Architectural candidate choices | Vegetation choices excluded from authored-family candidates |
| --- | --- | --- |
| blossoming_spires | ruins_1 through ruins_8 (8) | None |
| chorus_forest | ruins_1 through ruins_8 (8) | fallen_tree_1 through fallen_tree_4; stump_1 through stump_3 (7) |
| foggy_mushroomland | library, tree_house, ruins_1 through ruins_3 (5) | fallen_tree_1, fallen_tree_2, stump_1, stump_2 (4) |
| lantern_woods | cabin, light_1, ruins_1, ruins_2 (4) | log_1, log_2, stump_1 through stump_3 (5) |
| shadow_forest | small_mansion, ruins_1 through ruins_8 (9) | stump_1, stump_2, fallen_log_1, fallen_log_2 (4) |
| umbrella_jungle | house_1, house_2, ruins_1 through ruins_6 (8) | jellyshroom_cluster (1) |
| Total template choices | 42 | 21 |

The vegetation disposition uses decoded content, not the names alone: the 21
choices contain only the explicitly checked natural wood, fungal, foliage,
plant and End-stone blocks, with no stored entities or block-entity data. The
remaining 42 contain constructed materials, architecture or furnishings,
including lamps, masonry, bookshelves, doors and containers. Preserve them as
named architectural candidates. The umbrella cluster's stripped fungal bark is
part of the inspected natural cluster, not sufficient by itself to invent a
building. Conversely, lantern_woods/light_1 combines pedestal, wall, fence and
chain with a light-bearing plant and stays in the architectural candidate set.

Canonical grouping remains a specific task: compare the six ruin sets and the
two umbrella houses for shared designs, and relate standalone light/ruin designs
to the other named ornament candidates. Do not collapse choices by numbered
filename or promote every template to a family. Full BetterEnd provider coverage
also still requires its other entry points, resources and existing roots. The
provider total therefore remains 53 resolved and 83 open.

```sh
uv run pytest -q tests/item8/test_betterend_feature_candidates.py
uv run ruff check tests/item8/test_betterend_feature_candidates.py
uv run basedpyright tests/item8/test_betterend_feature_candidates.py
```

Two focused cases pass. Initial lint/type findings were confined to test
formatting, explicit types and split assertions; they are corrected. Ruff and
Basedpyright pass. The tests reuse frozen archive dd883e2f91fa7ee8a0594dc3844de38bf3e550d91ff1247b2801808904fd013a,
the existing source capture and dimension-biome evidence. No new measurement,
source-disassembly batch, schema or baseline change.

### BetterEnd extra biome templates and consumer boundary

Source 9ee6454, selected by dd6ed45, establishes that the building-list codec
accepts an explicit nonempty list of path/offset/merger entries. getRandom selects
one list member, and StructureInfo passes its stored path directly to the
BetterEnd class-resource loader. There is no adjacent-file or directory scan.
The existing six lists therefore do not acquire the extra templates implicitly.
Commands and the exact six-class identity manifest are in
sources/betterend-entry-template-consumers/README.md.

The new third case in test_betterend_feature_candidates.py binds that source and
accounts for every biome-directory template outside the 63 configured choices:

- `blossoming_spires/house.nbt`: a furnished 21 by 32 by 21 template. It is an
  architectural candidate disconnected from the six configured lists. Keep it
  named while reconciling other consumers; do not count it as active solely
  because it is packaged.
- `old_bulbis_gardens/fallen_tree_1.nbt` through `fallen_tree_3.nbt` and
  `old_bulbis_gardens/tree_stump_1.nbt` through `tree_stump_3.nbt`: six vegetation
  templates. Decoded palettes contain only BYG stem/wood, BetterEnd moss/vine/
  polypore and air, with no stored entities or block-entity data. They add no
  authored architectural candidate regardless of the separate compatibility
  activation question.

The seven adjacent structures.json lists use `nbt`, `offsetY` and `terrainMerge`,
which are not the current BuildingListFeatureConfig/StructureInfo codec fields.
Their existence does not extend the accepted configured choices. Preserve these
resources and the distinction; do not rewrite them into current configuration.
The common entry also exposes the BetterEndPlugin service loader and conditional
BYG callback registration, which must be reconciled with the remaining provider
entries. Full provider coverage remains open, with 53 resolved and 83 open rows.

The same three validation commands in the preceding section now pass three
focused cases, Ruff and Basedpyright. No new measurement or evidence format.

### BetterEnd pillar features and vanilla End components

Source ced7655, selected by d6f6c51, preserves the two pillar-feature bodies and
six declared End-content mixins. The capture reproduces exactly. Commands and
interpretation are in sources/betterend-pillar-end-hooks/README.md. The fourth
case in test_betterend_feature_candidates.py binds all eight classes, their
mixin declarations, packaged feature routes and the component template sets.

`betterend:fallen_pillar` and `betterend:obsidian_pillar_basement` are named
nonregistry candidates. Both have live placed-feature IDs, inline configured
features and direct references from the packaged dragon_graveyards biome.
Their rarity filters declare 20 and 8 respectively, followed by in-square and
biome filters. They generate weathered obsidian forms in code through BCLib SDF
operations. They do not consume the central-pillar templates. Keep their
landmark-versus-terrain decision explicit; a terrain package name is not an
exclusion rationale. No footprint experiment is needed to establish these paths.

SpikeFeatureMixin selects every packaged pillar component: pillar_base_1 through
4, pillar_top_1 through 4, and the four corresponding _cage tops. The index is
radius minus one for radius 2 through 5. These twelve files are variants and
components of the existing central End pillars, not additional independent
families. EndSpikeMixin reads their persisted height state. EndPodiumFeatureMixin
selects end_portal_active or end_portal_inactive according to portal state;
those two templates are alternatives for the existing exit portal. Both template
sets exist and decode successfully. This resolves fourteen component references.

The related EndDragonFight hook changes existing portal/crystal respawn handling.
EndCityFeatureMixin modifies the existing city's generation eligibility rather
than introducing another city layout. EndPlatformFeatureMixin delegates platform
creation to TerrainGenerator, which remains to be reconciled. Configuration
binding and interaction with YUNG's End Island remain explicit downstream
interpretation work within this census. Do not assume that a captured declared
mixin wins over another provider or that a template request proves placement.

Four focused cases, Ruff and Basedpyright pass using the commands above. The
provider remains open: these are candidate and component resolutions, not whole
BetterEnd closure. Overall provider coverage remains 53 resolved and 83 open.

### BetterEnd complete packaged-template partition

Source b5655b9, selected by d14f2ea, resolves the platform helper and Eternal
Portal template consumer. GeneratorOptions copies typed GeneratorConfig values;
the remaining key-to-field binding is explicitly GeneratorConfig, not an
unbounded helper audit. TerrainGenerator.makeObsidianPlatform either suppresses
vanilla creation, leaves it alone or relocates its obsidian platform according
to those option values. It supplies no additional independent template design.
BiomeIslandFeature fills terrain materials through SDF operations and supplies
no authored building template or encounter. Preserve its actual placement
consumers separately rather than interpreting its registry name as a dimension.

EternalPortalStructure loads portal/eternal_portal for the existing live
betterend:eternal_portal root. Together with the two exit-portal alternatives
already resolved, this accounts for all three packaged portal templates.

The fifth case in test_betterend_feature_candidates.py accounts for all 128 NBT
templates in the frozen BetterEnd archive, with no unmatched path category:

| Template group | Count | Disposition |
| --- | ---: | --- |
| Six configured building lists | 63 | 42 architectural candidate choices and 21 vegetation choices, as enumerated above. |
| Other biome templates | 7 | Six vegetation templates and the explicitly disconnected blossoming_spires/house candidate. |
| Village | 43 | 41 connected components and two disconnected components of the existing End village design. |
| Central pillars | 12 | Base/top/cage components of existing central End pillars. |
| Portals | 3 | Eternal Portal component and active/inactive exit-portal alternatives. |
| Total | 128 | Template accounting, not family count or proof of successful generation. |

The existing village graph retains two missing references:
`betterend:village/street_decoration/work_01` and
`betterend:village/terminators/stree_terminator_01`. The two packaged disconnected
templates are instead `betterend:village/decoration/work_01` and
`betterend:village/terminators/street_terminator_01`. These are different IDs;
do not substitute them, rewrite evidence or repair the frozen baseline.
The graph has no unresolved pool-element codecs. Five native pools connect to
the root; the sixth native pool, village/decorations, is empty with fallback to
village/terminators and is not reached by this root graph.

Five focused cases, Ruff and Basedpyright pass with the existing commands. The
source capture independently reproduced byte for byte. No new measurement or
schema. BetterEnd still requires remaining code-generation entries, configuration
binding and shared modifier/consumer reconciliation; complete template accounting
alone does not close that provider. Overall coverage remains 53 resolved and
83 open providers. Keep the 128-template boundary closed while doing that work.

### BetterEnd frozen generator branch selection

Source 9d70795, selected by 13f1e49, resolves the GeneratorConfig key-to-field
binding left open above. The source independently reproduced byte for byte.
Its table, command and frozen configuration identity are in
sources/betterend-generator-config/README.md. The sixth focused case binds the
constructor capture, exact frozen file hash and relevant values.

Under the frozen values, generate_obsidian_platform=true and
entity.spawn.has_spawn=false make BetterEnd's platform helper return without
cancelling or relocating vanilla platform creation. Both has_portal/replace_portal
and has_pillars/replace_pillars are true, enabling this provider's replacement
conditions. has_dragon_fights is true. use_new_generator=true and
end_city_fail_chance=1 make the city hook's nextInt(1) test return zero, so this
hook does not reject the existing city stub. This is a code derivation under the
frozen settings, not an observed world result or a claim about the final outcome
of competing mixins. Preserve those interactions in the remaining provider scope.

Six focused cases, Ruff and Basedpyright pass. GeneratorConfig is no longer an
open binding question for these branches. The 128-template accounting remains
closed. Continue remaining generation entries, shared modifiers and consumers;
do not reopen this configuration trace or add a new runtime measurement.
Whole-provider counts remain 53 resolved and 83 open.

### BetterEnd remaining custom roots and cave consumers

Source 5428e8f preserves eighteen remaining root, cave-consumer and integration
classes, reproduced exactly with selector 95997cf. Manifest SHA-256:
eb0d8ea37b2766dc0081c0e84035d9c37168758023bb33400d3028ef73363dbd.
The README in sources/betterend-remaining-root-consumers records the exact command
and interpretation boundaries. Common entry capture 4307aa7 separately preserves
biome, portal, command, integration-interface and loot entry bodies.

The complete packaged BetterEnd root list now matches the live registry exactly:
end_bridge, end_lake, end_lake_normal, end_lake_rare, end_village, eternal_portal,
giant_ice_star, giant_mossy_glowshroom, megalake, megalake_small, mountain,
painted_mountain, small_island and sulphuric_cave. This is fourteen roots, not
fourteen accepted families. Existing lake/mountain, village and portal evidence
is reused, with the remaining five custom roots bound to the new capture.

| Root | Candidate disposition |
| --- | --- |
| end_bridge | EndBridgeStructure selects anchors and creates EndBridgePiece, which writes an end-stone-brick deck and walls. One bridge-design candidate; anchors, materials and span variations are not separate families. |
| sulphuric_cave | Cave terrain with water, sulphuric rock, vents, brimstone, crystals and tube worms. Reconcile with the existing formation inventory; do not count pieces as families. |
| giant_ice_star | Snow/emerald-ice SDF formation; retain its named terrain candidate disposition. |
| giant_mossy_glowshroom | Fungal SDF formation; retain its named vegetation candidate disposition. |
| small_island | Terrain with flower/vine or waterfall/stalactite treatment. Named terrain candidate, with variation within the generator. |

VillagePools creates the already accounted pool keys. Its village_chorus key
resolves to a placed vanilla chorus_plant feature, not a second village route.
EndCaveFeatures consumes the separate cave-biome picker, updates cave biome
information and dispatches floor/ceiling features; CaveChunkPopulatorFeature
also dispatches cave floor/ceiling features. This closes the missing consumer
link without claiming every surface-biome feature executes inside caves.

BYGIntegration explicitly delegates to BYG block, feature and biome registries.
Flamboyant's init is empty and its explicit registration concerns colored blocks;
DyeDepot supplies colored crafting recipes. BCLib conditional dispatch and
retained BetterEndPlugin services remain shared activation inputs. Do not
expand into unrelated recipe auditing or inactive compatibility geometry.

Validation: seven cases pass in test_betterend_feature_candidates.py, including
the exact fourteen-root package/runtime set and eighteen source identities.
Scoped Ruff and Basedpyright pass. The initial added case included the ZIP
directory entry as a file and failed; corrected to exclude actual directories.
Initial missing JSON type casts were corrected before acceptance.

Remaining provider coverage: other feature registration consumers, remaining
declared common generation mixins, shared integration and Wover modifier
activation. Keep packaged template and root enumeration closed unless new
evidence contradicts them. Provider counts remain 53 resolved and 83 open;
family grouping and detailed attributes are not complete.

### BetterEnd retained compatibility and plugin boundary

The frozen runtime mod list contains betterend and bclib, but not byg,
flamboyant or dye_depot. BCLib source aa14b93 establishes that registerAll calls
an integration's normal init only when modIsInstalled succeeds; that check
delegates to the integration's ModCore.isLoaded. BetterEnd's previously captured
entry initializes the corresponding ModCore objects with these exact mod IDs.
Therefore the three compatibility initializers do not add a generation route
through this normal dispatch in the retained runtime. Preserve the separate
datagen branch without claiming that datagen ran. No absent compatibility tree
needs a geometry audit for this census.

All 136 hash-verified retained archives and their recursively nested JARs were
checked for the exact BetterEndPlugin service declaration. None provides it.
Their module-info.class entries also contain no reference to that service
interface. This is an explicit ServiceLoader declaration boundary, not keyword
absence used to infer that a whole mod has no structures. It closes this named
plugin entry question for the retained candidate inputs; it does not waive
remaining generation/modifier consumers or cover unretained external plugins.

The logic is preserved in test_betterend_retained_plugin_and_compatibility_inputs.
It binds the debug log SHA-256
e5b47378d791027242ba28dd36c999c07ae4e01a1b90e1534e66bcd42c1e694b
and the BCLib source manifest SHA-256
d085183016dd793119d9f8bbab449fbbc791851dce4ea8244e18da2e9aa4af2c.
All eight BetterEnd cases and scoped Ruff/Basedpyright pass:

```sh
uv run pytest -q tests/item8/test_betterend_feature_candidates.py
uv run ruff check tests/item8/test_betterend_feature_candidates.py
uv run basedpyright tests/item8/test_betterend_feature_candidates.py
```

An exploratory follow-up tried an incorrect BCLib filename after its service
scan and failed with FileNotFoundError. The retained manifest supplied the
correct bclib-21.0.24.jar identity; accepted source and tests use that identity.
Remaining BetterEnd census work is its other feature registration consumers,
declared common generation mixins and shared Wover modifiers. The compatibility
initializers and retained service declarations are now resolved. Provider counts
remain 53 resolved and 83 open. BCLib's whole-provider row remains open.

### BetterEnd declared common mixin coverage

Source 5726bc8 preserves the remaining 26 common mixins, using selector e1bffd9.
The capture reproduces exactly. Manifest SHA-256:
5dd3d155fcd660a11f2950742cffce16b67fba212735daa59ef83c8948d7d9a1.
Together with the six previously preserved End hooks, it covers all 32 names in
betterend.mixins.common.json exactly once. Source roles and the exact reproduction
command are in sources/betterend-common-mixins/README.md.

The remaining hooks modify existing terrain generation, chorus vegetation,
entity/player behavior, recipe support, advancement callbacks and initialization.
No separate authored family is supplied by these hook bodies. Terrain hooks use
the previously captured TerrainGenerator; their accessors and target flags are
not new generation candidates. The empty portal.EntityMixin body adds nothing.

Preserve two explicit placement effects. StructureMixin resolves the existing
structure registry key through the configured toggle and returns INVALID_START
when disabled. WorldGenRegionMixin replaces ensureCanWrite with a check requiring
each chunk-axis distance from the center to be less than two. That changes the
write boundary of existing generation, not the candidate list. No baseline fix,
new geometry experiment or performance audit follows from these observations.
Declared-hook coverage is not a claim that every injection ran or that competing
providers cannot affect final behavior.

Nine focused BetterEnd cases pass, including exact declared/captured mixin
equality and archive/class/disassembly identity binding. Scoped Ruff and
Basedpyright pass; one overlong assertion line was corrected during validation.
Use the commands recorded in the preceding section. BetterEnd's remaining census
areas are other feature consumers and shared Wover modifiers. Root, template,
compatibility and declared common-mixin checks stay closed. Overall provider
counts remain 53 resolved and 83 open; Item 8 is not complete.

### BetterEnd Wover biome modifier consumers

Source f9c8400 preserves the Wover modifier codec, application workers and the
six predicate implementations used by BetterEnd. Both capture directories
reproduce exactly; their READMEs record the commands. Manifest SHA-256 values:
a369761c4511706e0486eae7465fb74d379e4dc97f91dd74113c206b71d55868
(wover-biome-modifier-consumers) and
dfea087f9938a66807e94d9d2f9a46d110e82dae07092fde2777780979299cbf
(wover-biome-modifier-codec).

BetterEnd packages exactly two biome_modifications resources. defaults.json
adds the existing crashed_ship placed feature at decoration index 4 and the
flavolite_layer, thallasium_ore and ender_ore features at index 6. Its predicate
excludes the betterend namespace and requires one of the Wover End barrens,
midland or highland biome tags. This extends existing candidates, not the
authored-family list.

eternal_portals.json adds betterend:has_structure/eternal_portal to biomes whose
namespace is neither minecraft nor betterend and whose path contains neither
mountain nor lake. The predicate has no dimension or End-biome requirement.
Preserve that distinction for the existing portal family's biome/dimension
attributes; do not silently describe this eligibility extension as End-only.
It does not prove that portals actually generate in every matching dimension.

The codec maps predicate, features, biome_tags and spawns into BiomeModification.
Its registry worker subscribes at server readiness, tests each modifier against
biome contexts, adds matching tags and applies feature/mob changes. FeatureMap
resolves placed-feature holders; GenerationSettingsWorker appends features at
their decoration index. The tag worker updates existing tag contents and logs
a warning if its required accessor is unavailable. These consumers do not create
an unlisted structure design.

The retained debug log at line 19125 records the Wover aggregate application
message. It proves the application phase ran, not the exact per-modifier or
per-biome outcome. Use the preserved live tags and generated-world observations
for downstream effective constraints; no new runtime experiment is warranted
to close this candidate-contribution question alone.

Ten focused BetterEnd cases, Ruff and Basedpyright pass using the commands above.
The new case binds the complete two-file set, exact payload hashes, named
feature/tag contributions and Wover archive/class/disassembly identities.
BetterEnd's remaining census area is other feature consumers. Root, template,
common-mixin, compatibility and these modifier contribution checks stay closed.
Overall provider counts remain 53 resolved and 83 open. Whole Wover provider
coverage and Item 8 completion are not claimed by this consumer-specific result.

### BetterEnd remaining feature-type reconciliation

Source 936f990 captures the remaining 84 feature-package classes; together with
the existing captures, all 94 classes in world/features are preserved exactly
once. Source 7431ddd binds the seven delegated plant growth implementations,
their base and EndBlocks registration. Both new captures reproduce exactly.
Their manifests are respectively
8ff7d86a2ca142e9a4fc4eac7bfee020c9e5301be3cb894ad7b42015578d0254 and
2252cf72f8e265ab1b314a98677c758eb0735264a09707e1d5595a8b1e908d16.
These are source-class counts, not family counts.

All 63 custom types referenced by the packaged configured features and inline
placed-feature definitions have one explicit role in
test_betterend_remaining_feature_types_have_explicit_roles. Every type is also
present in the preserved EndFeatures registration body. The exhaustive partition
is four previously recorded authored/landmark candidate routes, 22 terrain or
cave consumers, and 37 vegetation/ecological-nest routes. Four additional vanilla
types are ore, random_patch, vegetation_patch and multiface_growth.

| Feature group | Disposition |
| --- | --- |
| building_list_feature, crashed_ship | Existing architectural choices and crashed-ship candidate. Reuse the earlier template and placement accounting. |
| fallen_pillar, obsidian_pillar_basement | Existing named landmark-versus-terrain candidates. Final canonical grouping remains open. |
| Arches, spires, crystals, obsidian boulder, ore layers, ponds/lakes, sulphur formations and vents | Terrain/mineral placement. Configurations and placement implementations supply the materials and shape, not another authored building/encounter family. |
| Round/tunnel caves, cave populator and stalactite features | Cave terrain and the previously bound cave-biome decoration consumers. |
| Trees, fungi, shrubs, vines, aquatic and scatter plants | Vegetation placement and growth. Configuration/base/inner classes are component consumers, not families. |
| glow_pillar_feature | Registered GlowingPillarSeedBlock grows roots, leaves and luminophor. Vegetation, distinct from the obsidian-pillar candidates. |
| menger_sponge_feature | Places wet sponge blocks in its underwater placement path. Ecological resource, not a constructed sponge-shaped dungeon. |
| silk_moth_nest | Places the nest block beneath appropriate foliage. Ecological nest, not an authored encounter structure. |
| dragon_bone_ore | Inline vanilla ore placement replacing end stone with dragon-bone blocks. A mineral deposit, not a separately assembled skeleton structure. |

The new delegated-plant source binds BlueVine, EndLily, EndLotus, GlowingPillar,
Hydralux, Lanceleaf and NeonCactus fields to their concrete growth consumers.
No assumption about vegetation rests solely on a seed/sapling filename.
NBTFeature configuration and BuildingListFeature/CrashedShip inner classes remain
components of their already enumerated routes; they do not add template choices.

Twelve focused BetterEnd cases pass, including complete feature-package identity
coverage, the exhaustive configured-type partition and registration bindings.
Ruff and Basedpyright pass after correcting a path-expression formatting conflict.
The source reproduction commands are in the two new source READMEs; use the
existing focused test commands above.

The final packaged-resource join remains before whole-provider closure. The five
files under data/betterend/datapacks contain only the Nourish food-tag extension
and its pack metadata, not additional generation data. Preserve this inspection
with the final payload accounting. Do not recapture or reclassify the 94 feature
classes. Overall provider counts remain 53 resolved and 83 open until that final
join is accepted; canonical family grouping and attributes remain separate.

### BetterEnd provider census closure

The final payload join now passes. The frozen archive's 9,639 non-directory
entries are accounted for by exact data categories, client assets, 668 classes,
ten packaged datagen-cache files and nine metadata/license files. The complete
253-entry worldgen partition includes the two configured carvers, independently
captured in 50dd10e. They carve terrain and coat cave surfaces with cave-biome
materials; neither introduces an authored family. The only embedded datapack
contains four Nourish food tags and pack metadata. The sole NeoForge Mod
annotation belongs to the already inspected BetterEnd common entry class.

Together with the preceding dispositions, this closes provider candidate
coverage: fourteen runtime roots, all 128 templates, 94 feature-package classes,
all 63 configured custom feature types, all 32 declared common mixins, the two
Wover modifiers, cave dispatch, retained plugin and conditional compatibility
inputs have supported roles. This does not assert that every declared hook ran
or that every eligible placement succeeded. Missing/disconnected templates,
the loot callback identity mismatch and the portal modifier's lack of an End
dimension predicate retain their recorded dispositions. No frozen data was fixed.

Canonical decisions still include grouping the architectural template choices,
the disconnected blossoming-spires house, and the fallen-pillar and obsidian
basement landmark boundaries. Existing village, bridge, portal and crashed-ship
routes must be reconciled with the provisional inventory, not counted again.
These are named grouping questions, not unidentified provider contributions.

Validation: thirteen focused cases, scoped Ruff and Basedpyright pass using the
commands above. The final payload/carver case binds the exact archive contents
and preserved source identities. Its initial overlong line was corrected before
acceptance. Current census: 54 supported provider dispositions and 82 open rows.
Item 8, final canonical grouping and eleven-attribute completion remain open.

### Biomes O' Plenty named feature decisions

The existing source capture 846bc09 is reused without recapture. The two focused
tests bind its three exact class/disassembly identities to the frozen archive,
packaged configured and placed features, biome consumers, live registries and
the preserved dimension-biome-source membership capture.

| Candidate | Scope decision and evidence |
| --- | --- |
| monolith | Retain one distinct landmark candidate. The direct writer builds a rectilinear obsidian form with variation in its dimensions; dimensional variation is not another design. Packaged placement uses rarity chance 4, in-square, MOTION_BLOCKING heightmap and biome filtering. Its sole packaged biome consumer is end_corruption, present in the captured End biome source. |
| anomaly | Retain one distinct landmark candidate. In addition to modifying underlying terrain, the direct writer builds a cube of ANOMALY blocks with stable interior and randomized surface states. This is a discrete authored form, not merely a terrain-material replacement. Packaged placement uses rarity chance 2 with the same remaining modifiers as monolith; end_corruption is its sole packaged biome consumer and is in the captured End source. Block-state variation does not create separate families. |
| bone_spine / nether_bone_spine | Natural decoration, excluded as an independent structure family. Both empty configurations use the same direct writer, which places a vertical bone-block column. The nether variant has a placed route consumed by visceral_heap, present in the captured Nether biome source. The plain configured ID has no reference anywhere in this archive's packaged JSON except the two type declarations. This is a bounded packaged-route result, not proof that another provider could never reference it. |

All four configured IDs and the three connected placed IDs exist in the captured
live registries. All 321 packaged placed features use string feature references,
so there is no additional inline configured implementation hidden in those
entries. Runtime registration and biome-source membership do not prove a
successful placement or measured encounter frequency. Canonical inventory
integration follows the census; these two landmarks are not added to the 887
structure-registry roots, and unrelated Moog monoliths must not be merged by name.

The initial exploratory path filter also matched biome tags and then an archive
directory entry. Those two failed reads informed no accepted count. The tracked
checks use the exact worldgen-biome prefix and only JSON files. The initial
combined test exceeded the complexity limit; splitting the independent selector
reference check resolved it. Two tests, Ruff and Basedpyright pass:

```sh
uv run pytest -q tests/item8/test_bop_feature_candidates.py
uv run ruff check tests/item8/test_bop_feature_candidates.py
uv run basedpyright tests/item8/test_bop_feature_candidates.py
```

BOP whole-provider coverage remains open for its remaining feature types and
generation entry hooks. Current provider totals remain 54 resolved and 82 open.

Entry reconciliation in d802cf9 now preserves and reproduces the normal loader,
feature/carver registrars, biome setup, datagen subscriber and both declared
fluid mixins. See sources/bop-generation-entries/README.md. Cave carving and
fluid-type mixins add no authored family. The entry registration binds all 78
custom types referenced by the packaged configured features. Its three extra
types are dead_coral_tree, dead_coral_mushroom and dead_coral_claw, which have no
standalone packaged configured entry. They remain in consumer reconciliation,
not presumed inactive from that absence. The other thirteen configured types
are vanilla types. These are feature-type counts, not family counts.

The remaining BOP feature scope is therefore 75 custom configured types after
the three named decisions above, plus the three registered coral consumers.
Use their existing configurations and concrete placement roles; follow only
unresolved candidate behavior, not unrelated plant/block gameplay. Whole payload
accounting still needs its final join. Do not repeat the entry capture or the
three named decisions. Three focused BOP cases pass; scoped Ruff and Basedpyright
pass after fixing one long line and typing the regular-expression result.

### Biomes O' Plenty provider census closure

The remaining 78 registered feature writers are preserved in edc36d3, with
shared tree and quartz material writers in 4314947. Both captures reproduce
exactly using their source README commands. The complete 81-type registration
now has an explicit, nonoverlapping role partition in the focused BOP test.

| Contribution | Final provider disposition |
| --- | --- |
| anomaly and monolith | Two existing named landmark candidates, with their packaged placement and captured End biome-source membership bound above. |
| big_pumpkin and pumpkin_patch | Two named decoration-boundary questions for canonical grouping. The first writes a giant pumpkin form, oak-log stem and persistent leaves. Its carved-pumpkin/jack-o-lantern references belong to the replaceable-space predicate, not writes to the giant form. The second scatters ordinary/carved pumpkins, jack-o-lanterns and persistent leaves. Both have packaged placement with rarity chance 1 and the pumpkin_patch biome consumer, present in the captured Overworld biome source. Do not silently equate either resource name with an accepted family. |
| Terrain/mineral writers | Ground-material patches, cliffs, lakes/tidepools, rocks, quartz, vents and fumaroles. Direct materials and the quartz inner writer establish these roles. Bone spine remains natural decoration. |
| Vegetation and ecological decoration | Trees, fungi, ground and hanging plants, vines, leaf piles, fallen logs/stumps, coral, barnacles, webs and a packed-mud termite mound. These writers supply natural materials/ecological forms rather than buildings or authored encounter layouts. Shared tree block-state providers are bound by the delegated-material capture. |
| Three coral types without standalone configured files | All three are inline configured features inside the packaged dead_coral simple_random_selector. This resolves the earlier open consumer question; standalone-file absence did not imply inactivity. |
| Cave and fluid hooks | The previously bound origin cave carver and two fluid-type mixins add no authored family. |
| Remaining resources | Biomes and tags supply terrain, eligibility and ecological constraints; wolf variants, loot, recipes, advancements, damage types, trim materials, jukebox and data-map resources are content or attribute inputs. Assets, metadata and datagen caches are accounted for separately. They are not independent structure families. |

The full frozen archive accounting covers all 4,542 non-directory files,
including 317 classes and the complete worldgen partition: 279 configured
features, 321 placed features, 69 biomes and one configured carver. The only
loader/subscriber annotation classes are the already preserved NeoForge entry
and datagen handler. There are no nested archives, service-provider files,
structure definitions, template pools or NBT templates in the accounted payload,
and no BOP root in the captured structure registry.

Five focused cases, scoped Ruff and Basedpyright pass using the BOP commands
above. The tests bind all 81 registered feature writers, exact source identities,
the inline coral selector, named placement consumers and exhaustive payload
categories. Two formatting findings (the regex flag alias and a long line) were
corrected before acceptance. No new measurement, runtime world, baseline change
or interpretation of rarity as observed encounter pacing was introduced.

Provider census is now 55 resolved and 81 open. BOP contribution membership is
accounted for; canonical pumpkin boundaries and final family integration remain
separate from provider closure. Item 8 and its eleven-attribute gate remain open.

### Redstone, configuration and loot provider dispositions

The three source captures below reproduce exactly with the commands in their
source READMEs. The existing small-utility test binds each complete class and
non-class payload, loader/subscriber entries, declared mixins and exact source
identities. There are no unaccounted nested archives, generation data, templates,
service providers or extra entry mechanisms in these payloads.

| Provider | Contribution disposition |
| --- | --- |
| Alternate Current (30 classes, 4b722aa) | Server-level wire-handler creation, redstone placement/removal/neighbor hooks, configuration save and operator commands. Wire nodes, queues, connections and update order process existing redstone signals; LevelHelper writes the supplied wire state and updates neighbors. No independent authored family. This is not redstone-equivalence, trap-behavior or performance evidence. |
| Cupboard (18 classes, 77dd750) | Configuration loading/reloading, client configuration UI, registry/block lookup, math/vector support and five diagnostic/entity-handling mixins. Off-thread entity additions are queued and drained by a later server-thread addEntity call. Conditional entity-load recovery and rotation repair affect existing entities, not authored spawn layouts. No independent family. Optional mixin declarations and thread-name testing remain limitations; this scope result does not prove every injection ran. |
| Loot Integrations (9 classes, 47047d6) | Reload listener reads integration definitions; the loot-table mixin invokes the manager, which guards recursive application and calls the stack modifier. Weighting, item-count limits, duplicate policy and the additional-map suppression context affect existing loot attribution. No independent authored family. Previously enumerated addons remain consumers of this core loader, not separate evidence of its implementation. |

Frozen Cupboard configuration is bound by SHA-256
937698438af081495eebab187013f66570218e1443f35db8a2ca0b4cb6d9638b:
skipErrorOnEntityLoad, debugChunkloadAttempts and forceHeapDumpOnOOM are false;
logOffthreadEntityAdd is true. Source recovery branches must not be described
as enabled merely because their implementation exists.

Frozen Loot Integrations configuration is bound by SHA-256
898873bac11398a75f7faddeb31410246d43be578868ba58d390b58667b44d31:
skipMapItems is true, skipExistingItems is false, moddedItemWeight is 3, and
container-table/debug output are false. Map suppression applies to the additional
integration context, not all original chest maps. The full packaged data is
43 integration definitions, seven chest tables and the barrier ignored-item tag.
All definitions use loot_table, integrated_loot_tables and max_result_itemcount.
The table named empty contains a bone entry. The six other tables contain
minecraft:empty entries with their actual individual weights preserved by the
test. The initial test incorrectly expected identical empty entries in all seven
tables; it failed and was corrected against archive inspection. No raw data was
changed, and no effective reward frequency is inferred from these declarations.

Validation: 18 focused utility cases, Ruff and Basedpyright pass. A long test line
was also corrected. Reproduction and verification:

```sh
uv run pytest -q tests/item8/test_small_utility_provider_scope.py
uv run ruff check tests/item8/test_small_utility_provider_scope.py
uv run basedpyright tests/item8/test_small_utility_provider_scope.py
```

Current census: 58 resolved providers and 78 open. These closures add no family
candidate and do not complete the affected families' eleven required attributes.

## Integrated Villages provider disposition

Source 97000f2 plus the prior suppression capture covers all fourteen classes in
integrated_villages-1.3.3+1.21.1-neoforge.jar. The focused payload check binds all
1475 files to the frozen archive identity and the exact source manifests. No
additional nested archive, service, script or feature/carver registration is
present in this payload. Entry, configuration, loot diagnostic and pool consumer
roles are documented with the source; the two declared mixins modify generation
and direct locate behavior for existing vanilla/Terralith villages.

All twelve packaged roots are already in the inventory and preserved graph.
Ten use Integrated API generic_structure, pirate uses biome_facing_structure,
and quark/minka uses optional_dependency_structure. Reuse runtime registration,
frozen suppression and prior design enumeration. These twelve roots are not a
new canonical family count. Shared Integrated API implementation remains an open
provider dependency.

The existing graph accounts for all 421 pools and 754 templates. Exactly 51 pools
and 74 templates are disconnected from those twelve root graphs. Their exact
IDs are retained in test_integrated_villages_provider_scope.py. They are village
house, job, path, decoration, mob and compatibility components, not independent
registered families. Several have names resembling missing references; do not
silently substitute them. Missing pool/template references remain on cabin,
kutcha, marketstead, oasis, pirate, quark/minka and sunken roots. The test binds
the complete missing-reference lists to the preserved graph; all twelve traces
have no unresolved pool elements. Graph reachability does not prove successful
world placement of every connected piece.

Four additional component declarations target Mediterranean bakery, pirate
market, tavern market and tavern well. Each targets one of the disconnected
packaged templates. All use name and required_mod, while the captured consumer
reads target_pool and optional condition. Preserve this incompatible declaration
shape. The missing target_pool is read before the codec exception handler. Entry
code does not register the reload listener, and this source capture establishes
neither successful injection nor an observed runtime parsing failure. Mod absence
alone is not their effective disposition. Their candidate role is nevertheless
bounded: components of existing villages, not additional structure families.

Twelve Integrated API workstation definitions select block components. One
integrated_structure_spawners definition declares zombie weight 15 and skeleton
weight 10. These are component/encounter inputs for shared consumers, not new
structure roots or proof of realized spawners. Other packaged data consists of
loot, tags, advancements, processors and structure sets. Preserve these inputs
for the later eleven-attribute pass.

```sh
uv run pytest -q tests/item8/test_integrated_villages_provider_scope.py tests/item8/test_integrated_suppression.py
uv run ruff check tests/item8/test_integrated_villages_provider_scope.py
uv run basedpyright tests/item8/test_integrated_villages_provider_scope.py
```

Five cases pass; scoped Ruff and Basedpyright pass. The initial new test looked
for the condition codec in ExpandedPoolEntry, but javap places that codec in the
enclosing AdditionalStructureTemplatePool. Correcting the asserted source file
resolved the test failure without changing raw evidence. Initial formatting
findings were corrected. Provider dispositions now cover 59 of 136, leaving
77 open. Canonical family grouping and the final Item 8 gate remain open.

## IDAS provider disposition

Source afb3cee and the prior idas-suppression capture cover all 21 packaged
classes in idas-1.13.7+1.21.1-neoforge.jar. The focused test binds their manifests,
class bytes and disassemblies to the frozen archive, accounts for all 967 files,
and matches all 84 packaged roots to the captured runtime registry. Other than
roots, pools, processors and structure sets, this payload contains loot, tags,
advancements, encounter-spawner definitions, music, a recipe and visual/audio
assets. There are no nested archives, service entry files, functions or additional
feature/carver definitions. The NeoForge entry registers ordinary disc/fragment
items, sound events and a creative tab, configures IDAS, and initializes the
mining-fatigue structure tag. Its common server-start callback is empty.

All 214 pools and 259 templates have a component disposition against the existing
root graphs. The exact 21 disconnected pools and 23 disconnected templates are
listed in test_idas_provider_scope.py. They include alternate compatibility
rooms and entrances, old house pools, desert camp/pyramid pieces, a bear den,
a Labyrinth test template and a pillager-camp variant. They do not have independent
root registrations. Do not count them as standalone families.

The disconnected-default-graph label is not an assertion of unconditional
inactivity: enchantingtower, haunted_manor and labyrinth explicitly declare
alternate start pools for Ars Nouveau or Ice and Fire through
integrated_api:mod_adaptive_structure. Preserve those alternate component links.
Three other roots declare optional dependencies: archmages_tower requires
Ars Nouveau; dread_citadel and sirens_cove require Ice and Fire. Shared Integrated
API selection behavior is still an open provider dependency. Root registration,
compatibility declarations and successful placement are different claims.

Preserve all missing pool references: ancient_mines/ancient_mines_entrance2,
desert_pyramid/desert_pyramid_villager, dread_citadel/dread_citadel12 and
dread_citadel/dread_citadel5. Their root membership and exact IDs are bound to the
preserved graph. All 84 traces have no unresolved pool elements. A similarly named
template does not replace a missing pool. The existing unresolved biome-constraint
and dimension-attribute questions are not resolved by this provider disposition.

Five packaged mixins modify existing structures and encounter behavior.
DisableStructuresMixin and LocateStructuresCommandMixin address existing
vanilla/Ice and Fire generation and direct locate requests. Reuse the prior
suppression check. ServerLevelMixin attaches dimension-local Labyrinth cleared
state. ServerPlayerTickMixin checks survival players every 100 ticks, requiring
a loaded valid piece in the applies_mining_fatigue tag, the enabled setting and
an uncleared structure. It applies or refreshes mining fatigue subject to the
existing effect's amplifier/duration. The frozen Apply Mining Fatigue setting is
true; the packaged tag names idas:labyrinth. This is an existing-encounter input,
not an independent generation route or a runtime gameplay acceptance claim.

LabyrinthBossKilledMixin identifies a qualifying boss, finds a tagged structure
piece and records cleared state using the structure start chunk's world position.
Its recognition includes the named Pharaoh Husk, its packaged head-texture
alternative and the Gorgon identifier. The stateCache/stateRegion classes store
and retrieve cleared flags. These hooks do not create independent structures.
Preserve their exact behavior for later encounter attribution; do not infer that
all boss, effect-removal or persistence behavior has been tested in game. Eighteen
integrated_structure_spawners resources declare weighted mob lists for shared
consumers, likewise component inputs rather than additional families.

```sh
uv run pytest -q tests/item8/test_idas_provider_scope.py tests/item8/test_integrated_suppression.py
uv run ruff check tests/item8/test_idas_provider_scope.py
uv run basedpyright tests/item8/test_idas_provider_scope.py
```

Five cases pass; scoped Ruff and Basedpyright pass. The payload test keeps one
explicit archive/graph assertion with a local complexity exemption, avoiding a
new helper solely to divide that assertion. An initial exploratory path substring
also matched a structure tag and raised KeyError; the tracked check uses the
existing resource_identity function and cannot mistake tags for roots. No raw
input was changed. Current provider census: 60 resolved and 76 open. Family
canonicalization, eleven attributes and the final Item 8 delivery gate remain open.

## Better Witch Huts provider disposition

Source 04b6ab5 and the prior witch-hut-suppression capture cover all twenty
packaged classes. The focused test binds source and archive hashes and accounts
for all 54 files in YungsBetterWitchHuts-1.21.1-NeoForge-4.1.1.jar. The two
packaged service declarations select the captured NeoForge modules/platform
implementations. Common initialization scans the module package for YUNG API
registration annotations; its modules service delegates to an empty default.
There is no additional independent generator in these entry paths. Configuration
and direct vanilla locate/suppression behavior reuse existing evidence.

The two roots, betterwitchhuts:witch_hut and betterwitchhuts:witch_circle, exactly
match the runtime registry. All three pools and six templates are connected in
the preserved graphs. The hut has small, large and double template alternatives;
the circle has its own template; witch and cat are shared mob components. There
are no disconnected components, missing references or unresolved pool elements.
Do not count the mob templates or layout alternatives as additional families.

The sole main processor list binds all five captured custom processors. Log and
fence supports extend down from template markers; circle masonry is varied and
supported; brewing-stand item NBT and potted plants are populated/varied. These
are existing-component modifications. Source README preserves the relevant roles,
including support extension outside original template bounds and the distinction
between written item NBT and runtime acceptance. Detailed vertical size, effective
content and final family attributes remain open. Shared YUNG API registration
and randomizer semantics are still attributed under its separate provider row.

Other payload resources are structure sets, tags, loot, translations, logos and
metadata. No additional nested archive, script, feature/carver data or unexplained
resource class is present. This disposition accounts for provider candidates;
it does not assert gameplay completion or change the frozen baseline.

```sh
uv run pytest -q tests/item8/test_witch_hut_provider_scope.py tests/item8/test_yung_suppression.py
uv run ruff check tests/item8/test_witch_hut_provider_scope.py
uv run basedpyright tests/item8/test_witch_hut_provider_scope.py
```

The new payload case and six existing suppression cases pass. Scoped Ruff and
Basedpyright pass. Initial line-length and statement-count findings were resolved
with a wrapped assertion and a local exemption keeping the single archive/graph
assertion together. The source capture independently reproduces exactly. Current
census: 61 resolved providers, 75 open. Canonical family grouping and Item 8's
remaining attribute and final delivery gates are unchanged.

## Better Nether Fortresses provider disposition

Source 5933abb and fortress-suppression preserve all 26 packaged classes in
YungsBetterNetherFortresses-1.21.1-NeoForge-3.1.5.jar. The focused check binds
archive/class/source identities, accounts for all 244 files, and matches the
single betterfortresses:fortress root against the runtime registry. Three
packaged service declarations select the captured NeoForge modules, platform
and item-frame processor providers. Common registration scans the module package;
the modules service delegates to an empty default. Reuse the prior configuration,
vanilla suppression and direct locate evidence.

All 15 pools are connected in the preserved root graph. Of 169 templates,
20 are disconnected; their exact IDs are listed in test_fortress_provider_scope.py.
These are bridge, stair, pillar, hall and tower alternatives or props. None has
an independent root. The missing reference betterfortresses:halls/hall_4 is
preserved; the packaged halls/hall_4_ has a distinct ID and is not substituted.
The root graph has no unresolved pool elements. Do not count disconnected pieces
or alternate layouts as new families, or equate graph reachability with observed
successful placement.

The main processor list uses seven captured custom processor types plus vanilla
rule processing. They construct component supports/arches, replace liquid and
stair markers, vary wart placement and populate existing item-frame entity NBT.
Pillar states and item choices use shared YUNG API randomizers. The existing
spawning mixin recognizes monster-category positions over nether bricks inside
a valid Better Fortress start. These are component and existing-encounter effects,
not independent families. Preserve direct support writes outside template bounds
and exact item NBT for later size/content attribution. Shared YUNG API semantics
remain an open provider dependency; this closure is not a gameplay or final
attribute acceptance claim.

Other data is loot, tags, an advancement, translations and metadata/assets.
There are no nested archives, functions, feature/carver definitions or unexplained
payload categories. The source capture reproduces exactly.

```sh
uv run pytest -q tests/item8/test_fortress_provider_scope.py tests/item8/test_yung_suppression.py
uv run ruff check tests/item8/test_fortress_provider_scope.py
uv run basedpyright tests/item8/test_fortress_provider_scope.py
```

Seven cases pass. Scoped Ruff and Basedpyright pass after correcting an overlong
assertion and explicitly typing the JSON processor IDs as strings. No raw input
or frozen configuration changed. Current census: 62 resolved providers and 74
open. Canonical grouping, eleven attributes and the final Item 8 gate remain open.

## Better Ocean Monuments provider disposition

Source a2f2832 plus the prior monument-suppression capture accounts for all 28
classes in YungsBetterOceanMonuments-1.21.1-NeoForge-4.1.2.jar. The focused test
binds archive/class/source hashes and accounts for all 122 files. The NeoForge
entry and common/module paths register the component processors through YUNG API
and load configuration. Two packaged service declarations select the captured
NeoForge module/platform providers; the modules default is empty. Reuse prior
vanilla monument suppression and direct locate evidence.

The sole packaged root, betteroceanmonuments:ocean_monument, matches the runtime
registry. All 13 pools are connected in its preserved graph. Of 59 templates,
only kelp/seagrass and kelp/seagrass_tall are disconnected. These are vegetation
components, not independent families. The root trace has no missing references
or unresolved pool elements. Connected components are accounted for without
claiming every piece was observed generating.

The sole processor list names all ten captured block processors. Their source
roles are sea-level air/water treatment, waterlogging/postprocessing, support
legs, slab ornaments, copper oxidation, sponge, gravel and seagrass variation,
and preserving existing blocks at void markers. These effects operate on the
existing monument. In particular the support writer can extend below template
bounds, an input to later vertical-size attribution rather than another family.
Shared YUNG API registration remains an open provider dependency.

PersistentTridentMixin cancels despawning only for a server-side thrown trident
with the packaged owner marker and a valid piece in the monument tag. The tag
contains this existing root; ProjectileAccessor supplies its owner-field access.
Preserve the exact source predicate, not a claim that all tridents persist.
The marker originates in packaged code and is not captured player data. This
hook changes an existing component's behavior and adds no generation route.

Other payload is loot, tags, translations, logos and loader metadata. There are
no nested archives, functions, feature/carver definitions or unexplained resource
categories. Full attributes and runtime behavior remain separate acceptance work.

```sh
uv run pytest -q tests/item8/test_ocean_monument_provider_scope.py tests/item8/test_yung_suppression.py
uv run ruff check tests/item8/test_ocean_monument_provider_scope.py
uv run basedpyright tests/item8/test_ocean_monument_provider_scope.py
```

Seven affected cases and scoped quality checks pass. Source extraction reproduces
exactly. Census: 63 resolved providers, 73 open. No canonical family count or final
Item 8 completion claim follows from this provider closure.

## Better Strongholds provider disposition

Source 41964b5 plus stronghold-suppression preserves all 32 packaged classes in
YungsBetterStrongholds-1.21.1-NeoForge-5.1.3.jar. The focused check binds exact
archive/class/source identities and accounts for all 181 files. Three packaged
service declarations select the captured NeoForge module, platform and processor
providers. The module loader delegates to an empty default; the processor service
exposes armor-stand and item-frame codecs. Common initialization uses YUNG API
module registration, and the configuration loader reads the four existing
ore/rare-block/armor-stand/item-frame selection tables. These are component inputs,
not additional independent generators. Reuse the prior suppression evidence.

The sole betterstrongholds:stronghold root matches the runtime registry. All
12 pools are connected in the preserved graph. Thirteen of 97 templates are
disconnected: a soul-torch doorway, a hallway trap, a new hallway terminator and
ten statue terminator alternatives. Their exact IDs are bound in
test_stronghold_provider_scope.py. They are components, not independent families.
The graph preserves one missing pool, betterstrongholds:spiral_stairs, and no
unresolved pool elements. Do not silently manufacture that pool or treat missing
references as successfully traversed content.

BetterStrongholdsPlacement selects chunks for the existing root. Its packaged
structure set binds spacing/separation, salt and radial parameters to that root;
its implementation extends random-spread candidate selection with a radial
section filter. This is not another family or an observed pacing measurement.
Nine processor lists use the nine captured component processor types plus vanilla
rule processing. Their roles cover ruin/block variation, banners, end-portal
frames, supports, ore/rare-block markers, redstone and existing armor-stand and
item-frame NBT. Preserve direct support extension and written item data for later
size/content attribution. Shared YUNG API randomizers, banner creation and
registration remain an open provider dependency.

Other packaged payload is loot, tags, an advancement, translations and metadata
or visual assets. There are no nested archives, functions, feature/carver data
or unexplained resource categories. Provider coverage does not establish all
attributes or successful runtime gameplay behavior.

```sh
uv run pytest -q tests/item8/test_stronghold_provider_scope.py tests/item8/test_yung_suppression.py
uv run ruff check tests/item8/test_stronghold_provider_scope.py
uv run basedpyright tests/item8/test_stronghold_provider_scope.py
```

Seven affected cases and scoped quality checks pass. The initial graph assertion
incorrectly expected the missing spiral_stairs ID in the traversed pool set;
the preserved graph records it separately in missing. The assertion was corrected
without changing raw evidence. A local complexity exemption keeps the single
archive/graph assertion together. Source capture reproduces exactly. Census:
64 resolved providers, 72 open. Canonical grouping and Item 8's remaining
attribute and delivery gates are open.

## Better Jungle Temples provider disposition

Source e4bb5e3 and jungle-temple-suppression preserve all 32 packaged classes.
The focused check binds archive, class and source identities and accounts for
all 203 files. Three services select the captured NeoForge module, platform and
processor providers. Common registration delegates to YUNG API; the module-loader
default and compatibility initializer are empty. Prior suppression evidence
continues to bind the frozen configuration. Shared YUNG API remains open.

The sole betterjungletemples:jungle_temple root matches the runtime registry.
All 17 pools are connected. Of 127 templates, only props/prop_table_0 and
props/prop_table_1 are disconnected from the preserved graph. They are table
components, not independent families. No missing references or unresolved pool
elements occur in this graph. This establishes component accounting, not observed
placement success for every template.

Custom placement selects the same root using random-spread placement, horizontal
biome search and an enhanced exclusion check. The two processor lists use eight
custom types in total: block replacement, pillar supports, vine decoration, torch
variation, blast-furnace marker variation, arrow dispensers, fireball dispensers
and item-frame position correction. These modify this temple's components.
ArrowData supplies trap item information. Pillar extension and serialized trap
contents remain inputs for later size and content attribution; this closure does
not assert effective runtime NBT acceptance. Item-frame processing adjusts existing
frame coordinates and does not randomize loot.

Other payload is loot, tags, translations, visual assets and loader metadata.
No nested archives, functions, feature/carver definitions or unexplained payload
categories remain. No additional family candidate was found in these entry paths.

```sh
uv run pytest -q tests/item8/test_jungle_temple_provider_scope.py tests/item8/test_yung_suppression.py
uv run ruff check tests/item8/test_jungle_temple_provider_scope.py
uv run basedpyright tests/item8/test_jungle_temple_provider_scope.py
```

Seven affected cases pass. The first scoped Ruff run reported function complexity;
a local exemption preserves the existing single-archive assertion pattern.
Scoped Ruff and Basedpyright then pass. The source's independent reproduction
is recorded in its README. Census: 65 resolved providers, 71 open. Canonical
grouping, required attributes and final Item 8 delivery remain open.

## Better End Island provider disposition

The complete frozen archive has 101 files and 45 classes. Existing source captures
cover generation, activation, configuration and component processors; source
6e1f551 adds only the nine remaining command, registration and mixin entries.
The focused payload check binds those source identities, both packaged services,
every declared mixin and the exact ten remaining internal helper/interface types.
Those internal types have no loader, event-subscriber, mixin or YUNG module entry
annotation. They support the captured fight lifecycle. This is a bounded entry
reconciliation, not a claim that every packaged class needs separate disassembly.

Reuse the existing exhaustive template assignment and its focused test: all 41
packaged templates are assigned once to arrival_platform (one), gateway (one)
and dragon_arena (39). Spike indices, initial/broken/guarded states and tower
sections are arena components. No packaged or live betterendisland structure
registry root exists; these are nonregistry generation contributions. The known
platform/gateway replacements and spike/podium generation retain their prior
configuration, source and failure limitations. No new independent candidate was
found in the remaining entry hooks.

The permission-level-two end_island reset command delegates to the same dragon
fight. The two world-data mixins attach and serialize its state; the server tick
hook triggers its initial summon. The Endergetic compatibility hook conditionally
replaces the fight object. The accessor exposes existing fight fields and dragon
creation. Gateway block-entity hooks select landing positions using block queries
and the packaged cannot-place-player-on tag. These are existing encounter and
transport behavior, not additional authored designs. Processor registration
exposes the three already captured block, obsidian and dragon-egg processors.
The module-loader default is empty. Shared YUNG API remains separately open.

All other payload is translations, two tags, visual assets and loader metadata.
There are no nested archives, functions or additional generation resource types.
Do not infer runtime placement success, gameplay validation or complete attributes
from this provider disposition.

```sh
uv run pytest -q tests/item8/test_end_island_provider_scope.py tests/item8/test_feature_modifier_references.py -k end_island
uv run ruff check tests/item8/test_end_island_provider_scope.py
uv run basedpyright tests/item8/test_end_island_provider_scope.py
```

Seven focused cases pass. Ruff initially found three long lines and an unused
complexity exemption; these were corrected. Scoped Ruff and Basedpyright pass.
The nine-class source capture reproduces exactly. Census: 66 resolved providers,
70 open. The whole-stack canonical denominator and Item 8 closure remain open.

## Better Mineshafts provider disposition

Reuse mineshafts-code for the specialized generator, component construction,
frozen configuration, vanilla suppression and locate behavior. Source 26d2a97
adds only remaining initialization, service, piece registration and mixin classes.
Together the sources cover all 51 packaged classes with exact archive/class/text
identities. The focused check accounts for all 95 files and both service bindings.

All thirteen packaged roots equal the captured runtime roots for this provider.
They use the existing specialized mineshaft generator and differ by biome/config
inputs, as bound by the existing family-decision check. The sole structure set
contains all thirteen with weight one each. There are no packaged templates,
pools, features, functions, nested archives or additional generation data types.
The eleven piece registrations refer to entrance, tunnel, room, ore-deposit and
intersection components of this generator. They are not independent families.

Common initialization scans the module package through YUNG API; NeoForge
initialization loads the existing configuration. The module service delegates to
an empty default. Platform/service helpers resolve the packaged implementation
and mod/development queries. Shared YUNG API remains a separate open dependency.
Other data is biome/block/structure tags and translations, plus visual assets and
loader metadata. Accessor mixins expose block-survival and bounding-box operations.

SuppressLogMixin cancels logAndPauseIfInIde only when the message starts with
Detected setBlock in a far chunk and contains bettermineshafts:mineshaft. It does
not prevent the block write. This is a diagnostic limitation: absence of that
warning cannot prove absence of far-chunk writes. Preserve existing generator
and generated-world limitations; no runtime experiment or tuning follows from
this source finding. Existing evidence continues to bind vanilla mineshaft and
mesa-mineshaft suppression to the frozen enabled configuration.

```sh
uv run pytest -q tests/item8/test_mineshaft_provider_scope.py tests/item8/test_family_decisions.py -k 'mineshaft_provider or mineshaft_group or vanilla_mineshaft_suppression'
uv run ruff check tests/item8/test_mineshaft_provider_scope.py
uv run basedpyright tests/item8/test_mineshaft_provider_scope.py
```

Three affected cases pass. One overlong line was corrected after the first Ruff
run; scoped Ruff and Basedpyright pass. The source capture reproduces exactly.
Census: 67 resolved providers, 69 open. No additional candidate family was found;
whole-stack grouping, remaining attributes and the final delivery gate stay open.

## Better Dungeons provider disposition

The frozen archive contains 389 files and 64 classes. Source f9696df adds sixteen
entry, module, service and context classes to the seven specialized generator
classes already in betterdungeons-code. The remaining classes are configuration
holders/definitions and component processors with two switch helpers. The focused
check binds the archive and source identities, excludes additional loader,
subscriber, mixin or YUNG-module annotations on those remaining classes, and
links all 29 processor classes to their captured module's codec references.
Detailed processor effects remain attribute work, not additional family entries.

Five packaged roots equal the runtime roots: small, small Nether, skeleton,
zombie and spider dungeon. The spider dungeon uses its already captured code
assembly. The other four have preserved pool traces. All 33 packaged pools are
connected to these roots. Of 227 templates, only skeleton_dungeon/bridges/
bridge_stone_1 is disconnected. The zombie graph preserves the missing template
zombie_dungeon/big_stairs_crumbled_0. No unresolved pool elements occur. These are
component dispositions, not successful placement claims or additional families.

Twelve processor lists reference all 29 local codec IDs plus minecraft:rule.
The codec references cover component block/decoration, chest, spawner, banner,
stair and support consumers. Four piece registrations are spider components;
the two custom structure registrations select the existing spider and small-Nether
roots. DungeonType's six mob-theme labels are not independent structure families.
DungeonContextMixin initializes thread-local banner/chest counters for template
placement. The locate hook rejects an exact small-Nether query when its enabled
field is false, and the accessor exposes bounding-box coordinates.

Common initialization scans the module package through YUNG API. The module
service delegates to an empty default; the NeoForge entry loads configuration.
The configuration event/world-load handlers assign the eleven existing settings.
They add no independent generator. Shared YUNG API remains separately open.

Both packaged Forge and NeoForge biome-modifier declarations remove the vanilla
monster_room and monster_room_deep features for the small-dungeon biome tag.
Keep their loader-specific identities distinct. They replace generation rather
than introduce another design. The YUNG API tags target existing small-Nether
content for basalt-column/delta interaction. Remaining data is loot, tags,
advancements, translations and loader/visual metadata. Full file accounting finds
no nested archives, functions or additional generation resource categories.

```sh
uv run pytest -q tests/item8/test_dungeons_provider_scope.py tests/item8/test_family_decisions.py -k 'dungeons_provider or spider_dungeon'
uv run ruff check tests/item8/test_dungeons_provider_scope.py
uv run basedpyright tests/item8/test_dungeons_provider_scope.py
```

Two focused cases pass. Initial scoped checks found line lengths, the existing
single-archive function's branch count, two untyped values and implicit string
concatenation. Narrow annotations/style corrections resolve them; Ruff and
Basedpyright pass. Source capture reproduces exactly. Census: 68 resolved
providers, 68 open. Whole-stack canonical grouping, effective attributes and
Item 8's final review/delivery gate remain open.

## Better Desert Temples provider disposition

The frozen archive contains 323 files and 62 classes. Source 02ae27e adds 27
entry, mixin, module, service, placement and state classes to the three already
captured suppression/configuration classes. Remaining classes are configuration,
Pharaoh-data interface, two chance-data holders and 26 component processors.
The focused check binds archive/class/source identities, all declared mixins,
three service selections and the absence of additional loader/subscriber/mixin
or YUNG-module annotations on those remaining types. Module and processor-service
codec references account for all 26 processor classes.

The only packaged root equals the runtime betterdeserttemples:desert_temple.
All 28 pools are connected. Of 198 templates, hall_room/crushing_corridor is the
only disconnected component. The preserved graph has no missing references or
unresolved elements. The sole processor list uses the 26 local codecs plus
minecraft:rule. Armor stands, item frames, Pharaoh content, block/ornament changes
and support construction are component consumers, not independent families.
Their full effective attribute behavior is not claimed by this census closure.

Common initialization scans the module package through YUNG API, and the NeoForge
entry loads the existing configuration. The module service delegates to an empty
default. Custom placement selects this temple through random-spread and biome
search logic. Accessors expose biome source, box coordinates and processor
operations. Existing vanilla suppression remains bound to the frozen settings.
Shared YUNG API is separately open.

The mining-fatigue and temple tags both name this existing root. Server-level
initialization attaches a dimension-local temple-state cache. Player ticking
checks survival, configuration, a loaded valid tagged temple and its uncleared
state before applying mining fatigue. The Pharaoh utility recognizes a Husk by
the packaged head-texture marker. Death/discard hooks attempt to mark the existing
temple cleared using its original position, with current-position lookup if that
position is absent. Other Pharaoh hooks store/restore that position; cache/region
code persists cleared-state flags. Sound/effect handling affects the existing
encounter. These paths do not add another structure design. Keep the exact
source predicates and runtime-behavior limitations rather than inferring that
every generated temple contains or successfully processes the Pharaoh.

All other payload is loot, tags, advancements, translations, visual assets and
loader metadata. There are no nested archives, functions or additional generation
resource categories. This closes provider candidate scope, not Item 8 attributes.

```sh
uv run pytest -q tests/item8/test_desert_temple_provider_scope.py tests/item8/test_yung_suppression.py
uv run ruff check tests/item8/test_desert_temple_provider_scope.py
uv run basedpyright tests/item8/test_desert_temple_provider_scope.py
```

Seven affected cases pass. The first test-generation attempt had a quoting error
and produced no test file; the corrected attempt passed the cases. One overlong
line was then corrected, and scoped Ruff/Basedpyright pass. Source reproduction
matches exactly. Census: 69 resolved providers, 67 open. Whole-stack family
count, canonical decisions, attributes and final review/main merge remain open.

## Better Caves provider disposition

Source d9e30ff preserves 23 entry, carver, layer, context and mixin classes. The
focused check binds exact archive/class/source hashes and accounts for all 64
files and 49 classes. Remaining types are configuration, data/interface, noise,
carver-builder and liquid-region support; none declares another loader,
subscriber, mixin or YUNG-module entry annotation. All seven declared mixins
and the single platform service are bound to their captured implementations.

The provider contributes terrain carving, not an independent structure family.
Its complete data payload consists of two configured carvers and two NeoForge
biome modifiers. better_cave uses the single registered custom WorldCarver;
surface_cave uses minecraft:cave. The add modifier selects both for Overworld
biomes at the air carving step, while the remove modifier targets vanilla cave
and cave_extra_underground. There are no structure roots, templates, pools,
functions, nested archives or other generation resource types in this archive.
The captured live structure registry contains no bettercaves root.

The custom carver resolves server context and invokes MasterController, which
selects cave/cavern layers. Layers sample noise and invoke column carvers;
AbstractCarver writes carving block states and schedules fluid postprocessing.
Debug materials visualize carving. The packaged better_cave configuration has
debug_settings.enabled false, so its listed plank/brick/metal debug materials
are not authored building candidates. This is source/data interpretation, not
an observation that every carve attempt succeeds.

Mixins attach server/carving contexts and substitute configured liquid-region
results during aquifer processing. The configuration loader reads liquidregions
settings and preserves its logged error/default paths. The exact frozen JSON
has one dimension entry, minecraft:overworld, with region size 0.001, water
chance 40.0 and liquid altitude -55. These are terrain inputs, not family counts
or measured density. Configuration bakeConfig is empty. Shared YUNG API noise
and registration support remains separately open.

Remaining payload is loader metadata, one translation file and visual assets.
This bounded census conclusion does not reopen or replace Item 7's accepted
world evidence, prove runtime equivalence, or establish all family attributes.

```sh
uv run pytest -q tests/item8/test_better_caves_provider_scope.py
uv run ruff check tests/item8/test_better_caves_provider_scope.py
uv run basedpyright tests/item8/test_better_caves_provider_scope.py
```

One focused case passes. An unused lint exemption and one long line were removed;
JSON types were made explicit. Scoped Ruff and Basedpyright pass. The source
capture reproduces exactly. Census: 70 resolved providers, 66 open. Continue
Cave Biomes and shared API scope before whole-stack canonical reconciliation.

## Cave Biomes provider disposition

The frozen YungsCaveBiomes-1.21.1-NeoForge-3.1.1.jar has 581 files and 187
classes. Source 7f76013 preserves 55 entry, feature, module, service and common
mixin classes; its independent reproduction matches exactly. The focused check
binds archive and disassembly hashes, full payload categories, entry annotations,
service selection, all declared common mixins and every worldgen resource.

Role: cave terrain and vegetation, biome eligibility for existing structures,
and biome encounters. No independent authored structure family is added.
There are no packaged structure definitions, structure sets, pools, templates,
functions, nested archives or separate biome-modifier resources. The runtime
structure registry has no yungscavebiomes root. This negative registry result
is only one input; the feature and hook dispositions below address other paths.

| Path | Supported disposition |
| --- | --- |
| Two biomes, sixteen configured features and twenty placed features | Every configured feature has a placed consumer; every placed feature is referenced by Frosted Caves or Lost Caves. The extra dead-bush placement uses vanilla patch_dead_bush. Repeated placements do not create families. |
| Twelve custom Feature implementations | Cactus patches, prickly-peach cactus patches, ice sheets, icicle clusters and large icicles, water-surface ice fragments, noisy sphere/floor/ceiling/surface replacement and sandstone pillars. These write vegetation or geological materials using positions, noise and cave surfaces. They do not assemble independent buildings or encounter layouts. The three generic sphere/floor replacement types without packaged configured instances remain code capabilities, not extra candidates. |
| PillarRockFeature and large-icicle variants | Noisy sandstone columns and cave-constrained ice/dripstone formations. Pillar uses the supplied simple block provider, whose packaged value is layered_ancient_sandstone. Large, tilted and small icicles use the same feature with different parameters and rare-ice probabilities. These are terrain/resource formations, not additional landmark designs. |
| Existing-family consumers | Both biomes include vanilla monster_room and monster_room_deep features. Minecraft mineshaft and stronghold biome tags add the cave_biomes tag. These extend existing contributions and must be reconciled with already recorded vanilla/YUNG suppression; they are not unconditional runtime placement claims. |
| Biome registration and noise hooks | TerraBlender region registration and the cave region select cave biomes and modify vanilla climate parameters. Common noise mixins attach biome registry/source/sampler/seed context. Frosted aquifer hook changes fluid handling. The two marble mixin classes contain no injected methods. |
| Remaining common mixins | Accessors expose existing state; debug hooks send goal/path packets. Frosted hooks handle icicle projectiles, potion ice, cauldron drips, ice friction/rendering, frost-effect state and skeleton conversion. Lost Caves hooks handle brushing, cactus/dead-bush eligibility, sandstorm effects and server sandstorm state/ticks. These modify terrain, blocks or existing entities, not independent authored generation. |
| Commands and services | Sandstorm control and player-join synchronization. Both armor-trim debug registration callbacks require a development environment; the custom command produces armor-stand displays. These are command behavior, not naturally generated families. The sole platform service selects NeoForgePlatformHelper. |
| Remaining classes and resources | Block/item/entity behavior, mob goals, criteria/effects, configuration, networking, sandstorm state, client rendering/particles/sounds/JEI, registration modules, feature configuration/math/noise helpers. Modules register blocks, items, entities, loot keys, effects, potions, sounds, particles, criteria, decorative patterns and networking. Nine declared client mixins concern rendering, textures and client sandstorm state. No separate event-subscriber entry is present; the only mod entries are the captured common NeoForge entry and client entry. |

Biome mob lists include ice_cube and sand_snapper along with vanilla mobs. These
are natural spawning inputs, not authored room spawners. Loot tables, rare ice,
brushable sand and mob loot remain attribution inputs if relevant to the later
family attributes. This scope closure does not accept their gameplay behavior,
prove every hook executed or repeat Item 7 observations.

Frozen configuration is evidence/item-6/frozen/config/yungscavebiomes-neoforge-1_21_1.toml,
SHA-256 3be6874eada8f1920b8dc30f9345c07afc7d5a7d4621f642f78c57cbe1756b27.
It preserves cave climate parameters, vanilla Dripstone Caves climate changes
and enabled sandstorms. Shared YUNG API and TerraBlender remain separate open
provider rows; this closure does not assert their full-stack compatibility.

```sh
uv run pytest -q tests/item8/test_cave_biomes_provider_scope.py
uv run ruff check tests/item8/test_cave_biomes_provider_scope.py
uv run basedpyright tests/item8/test_cave_biomes_provider_scope.py
```

One focused case and scoped quality checks pass. Early read-only probes first
used raw JSON parsing on commented biome data, then confused biome tags with
biome definitions by matching a path substring. Neither result was accepted.
The tracked check reuses the existing comment-aware decoder and restricts the
resource root to data/yungscavebiomes/worldgen/. Initial lint/type findings were
corrected before acceptance. Census: 71 resolved providers and 65 open.

## YUNG API provider disposition

The frozen YungsApi-1.21.1-NeoForge-5.1.6.jar has 197 files and 179 classes.
Source a796af9 preserves 43 entry, registration, service, plugin and mixin
classes. Existing pool-codecs preserves the pool element module and Yung single
pool element; do not recapture it. The focused check binds both manifests and
all 45 disassemblies to the frozen archive, whose SHA-256 is
08e1d21690d3213a4c62de6b6cf79f3527afb2e72e0cad0e1848d46eb8f682ca.

Role: shared registration and structure-generation infrastructure, with
modifications to existing structures. No independent authored family. Its sole
packaged data consists of four initially empty structure tags. There are no
structure definitions, sets, templates, pools, features, biome modifiers,
functions, nested archives or separate event-subscriber entries. Its runtime
structure namespace is empty; codec types are not structure roots.

| Mechanism | Supported scope disposition |
| --- | --- |
| Common/NeoForge entry, annotation scanner and field router | Initializes the API module package and dispatches supplied fields by type into registration queues. NeoForge registry events consume the queued objects with their supplied resource names. Consumer mods retain ownership of content. |
| Generation modules | Register the generic Yung jigsaw structure type, enhanced random-spread placement type and pool-element codecs, plus queued consumer feature, placement-modifier, piece and processor types. These are reusable implementations, not new configured family instances. |
| Post-load dispatch and four services | Enqueues supplied static methods for common setup and registers supplied compostable blocks. NeoForge services implement annotation scanning, block-entity/particle construction and platform lookup. Remaining registration wrappers/modules concern supplied blocks, items, entities, creative tabs, commands, criteria, effects, potions, particles and sounds. |
| Four feature-suppression mixins and MixinUtils | Basalt columns, deltas, magma and vines consult their corresponding structure tags. The helper uses generated structure references, valid starts and bounding-box containment. These restrict features inside existing tagged structures; the API's own empty tag files do not imply the effective tags are empty. Consuming YUNG provider tag declarations are retained in their earlier dispositions. |
| Beardifier and NoiseChunk hooks | Apply enhanced terrain-density and aquifer overrides around existing structures. Remaining adaptation, mask, noise and geometry classes support this path; no standalone authored layout is registered by these hooks. |
| Eight accessors, jukebox hook and weight hook | Expose existing pool/terrain/potion state, cancel jukebox record handling when its level is null, and wrap the structure weight codec with an upper bound of 5000. The weight injection has require=0, so its declaration is not proof it executed. |
| Mixin plugin | getMixins returns null and pre/post hooks do nothing. shouldApplyMixin permits declared common mixins. Its sole special development-environment condition names MinecraftServerMixin, which is absent from both the archive and declarations. There is no additional plugin-supplied generation entry. |
| Remaining implementation classes | Consumer-driven jigsaw assembly, conditions, actions, modifiers, selectors, exclusions, randomizers, banner/spawner data, codecs, JSON, geometry and noise helpers. They implement the already registered types and consumer APIs. Their capability names and piece classes are not additional family candidates. |

The fifteen common mixins and one NeoForge mixin are all captured. All payload
files are accounted for as classes, the four tags, four service declarations,
loader/pack/mixin metadata, license and four icon/catalogue assets. No new
configuration or runtime experiment is introduced. This does not prove gameplay
compatibility, every optional injection, placement success or final family
attributes. It closes the shared provider's candidate contribution scope.

```sh
uv run pytest -q tests/item8/test_yungs_api_provider_scope.py
uv run ruff check tests/item8/test_yungs_api_provider_scope.py
uv run basedpyright tests/item8/test_yungs_api_provider_scope.py
```

One focused case and scoped quality checks pass. An initial long test line was
wrapped before acceptance. The source r1 reproduction matches every generated
file. Census: 72 resolved providers and 64 open. Continue with Quark's existing
generator/module evidence and remaining provider resources; do not restart the
completed YUNG provider work or detailed family attributes.

## Quark provider disposition

The frozen Quark-4.1-480.jar has SHA-256
989c465df2e4cb9f602840c2eec143358bf11462cc19dc0b0c7c9f17449e75a5.
The focused check accounts for all 9367 files, including 967 outer classes,
optional packs and the exact bundled Biolith archive. Eighteen existing source
manifests are hash-bound; all packaged world generators, top-level world modules
and Feature implementations are represented by retained disassemblies. New
source increments 174dba6, b9670f9 and 4e4a158 complement earlier captures without
repeating generator or configuration interpretation.

The existing candidate list remains quark:spiral_spire, quark:fairy_ring,
quark:fallen_log, quark:monster_box and quark:nether_obsidian_spike. Preserve these
five named site candidates for canonical reconciliation; this is not the final
whole-stack family count. The existing underground_styles, vegetation and
stone_generation entries are contribution dispositions, not extra families.
No new independent candidate is identified in the remaining paths below.

| Contribution path | Supported disposition |
| --- | --- |
| Existing generators | Reuse the existing spire, ring, log, monster-box and Nether-spike captures and decisions. Do not count repeated blocks, ring mushrooms, material variants or individual spikes as new families. Existing central-island reach and observed-world limitations remain separate from provider membership. |
| Underground and stone generation | Existing captured underground style/base/context/fill paths replace and decorate cave surfaces with Permafrost and Corundum materials. Stone clusters and stone-type generators are terrain/resource contributions. Their materials and configuration variants are not authored site families. |
| Six configured features, eight placed features and one biome | All configured features are Minecraft trees: five blossom colors and ancient_tree. Placed features select blossom trees, inline glow-shroom/glow-extra implementations or vanilla ore_lapis. Glimmering Weald supplies biome generation and spawn lists. These are vegetation, ore and biome inputs, not standalone structures or pools. Ancient/azalea wood and tree decorators remain vegetation. |
| Other existing vegetation | Reuse captured chorus vegetation, water petals, fallen-log decoration and blossom-tree consumers. The log itself remains the named candidate; attached vegetation does not multiply it. |
| Gold bars and variant chests | Register block-replacement callbacks against existing structure context. Chest material selection and fortress fence adjustments modify consuming structures, not independent layouts. Existing loot sources and container behavior remain attribute inputs. |
| Generation hooks | ChunkGenerator supplies structure/pool context, climate hooks handle disabled biome parameters, mushroom hooks adjust replacement behavior, SpringFeature consults NoMoreLavaPockets, and WorldGenRegion repairs chunk-access behavior. These modify existing generation. Spawner replacement is disabled in the frozen configuration and its callback checks that state before touching the existing spawner. |
| Other entry roles | The main Quark entry starts the existing CommonProxy/Zeta module path, registers pack finders and capabilities. Its event subscriber handles brewing. Other automatic entries are datagen or client animation/rendering. Remaining common/client mixins concern entity, block, inventory, redstone, trading, rendering and interaction behavior. ServerLevel's captured hook stores the magnet tracker. Lootr integration services and optional mixin adapt existing containers; they do not supply generation layouts. Lootr is not in the retained manifest. Shared Zeta interface-delegate dispatch remains its own provider responsibility. |
| Bundled Biolith | Exact nested SHA-256 7f5c86757c61f56c7dccf602b44a2c17ba08d32d7e88cb531cbcd0c7b4789eab. Its 106 files include 95 classes, metadata, a platform service and assets; no data definitions or authored templates. The captured entry, APIs, loaders, fifteen declared mixins and plugin connect supplied biome/surface rules, world lifecycle and feature indexing. Glimmering Weald calls addOverworld. Biolith's optional biome-source integrations are compatibility paths, not independent content. |
| Optional packs | Programmer art contains only assets and pack metadata. Optional datapacks contain pack metadata, component tags and three vanilla stone-ore configured-feature overrides. They introduce no structure definitions, pools or templates. Frozen Vanilla Stone Clusters is false; regardless of activation these three ore overrides are terrain, not family candidates. |

Full payload roles: outer code comprises Quark content/integration/datagen and
its bundled tween engine; assets are models/textures/sounds and UI resources.
Root data comprises recipes, advancements, loot tables/modifiers, tags, damage
and jukebox definitions plus the fifteen worldgen resources above. There are no
NBT templates or mcfunctions anywhere in the outer archive. Biolith's loaders
accept biome_placement.json and surface_generation.json under biolith; Quark
packages neither input and uses the inspected API call instead. These statements
are grounded in full payload accounting and the captured generation entry roles,
not just keyword absence.

Frozen quark-common.toml SHA-256 is
94bfff490eea33f9bb105fae298606c4708ddb8af2f3df8630cc0f0ac7e85327.
Reuse the earlier Zeta category/module binding and initial-refresh evidence.
Do not reinterpret a declared hook or optional pack as observed execution.
Biome mobs, Wraith rules, chest replacement, loot modifiers and Monster Box
behavior remain inputs to detailed family attributes. Provider coverage does
not prove spawning success, generated-world occurrence, frequency or final
canonical boundaries. Earlier working-decision scope strings are historical
checkpoints; canonical inventory regeneration remains deferred until the full
provider queue is resolved.

```sh
uv run pytest -q tests/item8/test_quark_provider_scope.py
uv run ruff check tests/item8/test_quark_provider_scope.py
uv run basedpyright tests/item8/test_quark_provider_scope.py
```

The focused case and scoped quality checks pass. Initial test formatting/type
findings were corrected before acceptance. No new runtime measurement, helper
framework or generator capture was added for this closure. Census: 73 resolved
providers and 63 open. Next reconcile shared Zeta using its existing captures.

## Zeta provider disposition

The frozen Zeta-1.1-40.jar has SHA-256
4f17d1a2b9fd6d18ddb7697aa451db7fb154053b8648f79de279ae0d7e68a2fa.
All 627 files are accounted for: 609 org/violetmoon classes, seven bundled
math/fast classes, four assets, loader/access-transformer/pack/mixin metadata,
and one biome-modifier definition. No nested archives, services, templates,
structure roots/sets, pools, functions or separate authored generation data
are packaged. The preserved runtime structure registry has no zeta root.

Role: shared module, configuration, registry and generation infrastructure.
No independent authored family. Nineteen existing source manifests bind 49
distinct captured classes to the archive. The recent c79f551 and a6d0b5b sources
complement earlier configuration/generator captures; they do not replace them.

| Mechanism | Supported contribution disposition |
| --- | --- |
| ZetaModForge, ZetaMod, ForgeZeta and common proxy | Creates the shared instance, starts registration/event infrastructure and loads general configuration with null categories and module finder for Zeta itself. The proxy bridges loader and play events. Consumer module definitions retain content ownership. |
| Existing module/configuration path | Reuse category/module assignment, name/section binding, initial configuration refresh and enabled-state propagation captured for Quark. These choose consumer behavior; they are not new families or evidence of actual placement. |
| Single packaged biome modifier | data/zeta/neoforge/biome_modifier/biome_modifier.json declares zeta:biome_modifier. Its registered implementation dispatches existing consumer biome/features/spawn modifications. Earlier component/compound-biome, deferred-feature and generator captures remain the implementation evidence. |
| RegistryDataLoader hook and dynamic registration | RegisterDynamicUtil notifies signed-up Zeta instances. ZetaRegistry selects the queued entries for the supplied registry key, returns if absent/empty, evaluates consumer-supplied creators and registers their supplied IDs. Static/dynamic registry wrappers provide reusable registration, not authored default structures. |
| StructureStart, StructurePiece and StructureTemplate hooks | Set/clear current structure context and apply registered block-state replacement functions to existing content. The replacement handler stores supplied functions; Quark's gold-bar/chest consumers are already accounted for. This does not create another structure layout. |
| InterfaceDelegateMixinPlugin | Handles declared annotated interface-method and return-value transformations. It is shared by Zeta and Quark. This is bytecode dispatch for their declared hooks, not an additional packaged generation definition. Preserve its actual transformation/error behavior; this scope closure does not accept every transformed method's gameplay correctness. |
| Other common and client hooks | Accessors expose block, item, loot, predicate, potion and spawn-placement state. Creative-tab filtering checks enablement, piston hooks select the shared resolver, and Forge block/item/weathering interfaces adapt existing behavior. Three client declarations concern block/item colors and rendering. None supplies an independent authored site. |
| Remaining implementation roles | Event wrappers/buses, registries, module/configuration metadata, client UI/rendering, block/item/entity interfaces, networking, recipes, advancement/loot conditions, piston handling, utility/math and supplied biome/generator support. The sole mod annotation is ZetaModForge; no separate event-subscriber entry or nested executable payload exists. Do not turn every interface/helper into a new provider or family. |

Fourteen common mixins and four Forge-side common mixins are all captured;
the plugin and client declarations are included in the focused metadata check.
The complete packaged-data and loader inventory complements source semantics;
zero registry roots alone is not the basis for exclusion. Shared behavior can
still affect biome constraints, loot, spawning and structure blocks, so its
consumer links remain inputs to the eleven attributes. This disposition does
not prove every hook executed, world occurrences, pacing, compatibility or final
canonical boundaries. Those separate requirements remain open as recorded.

```sh
uv run pytest -q tests/item8/test_zeta_provider_scope.py
uv run ruff check tests/item8/test_zeta_provider_scope.py
uv run basedpyright tests/item8/test_zeta_provider_scope.py
```

One focused case and scoped quality checks pass. An initial test incorrectly
assumed a bundled-library package prefix; actual full archive inspection showed
seven math/fast classes and the assertion was corrected to the measured exact
partition. Formatting findings were also corrected. No raw source was changed.
Census: 74 resolved providers and 62 open. Next reconcile Repurposed Structures,
reusing its existing mansion, monument, processor and pool-codec evidence.

## Repurposed Structures nonregistry candidate increment

Provider scope remains OPEN. Source 452e33e preserves the relevant registration,
NBT feature, modifier and common hook implementations with exact reproduction.
The frozen archive SHA-256 is
aeb473f0a0a0632cea089377cdd9f66c42cf6f97557fd32c368ac40635285dd2.

The configured NBT feature set includes sixteen dungeon configurations and
seven well configurations outside the current non_registry_content contribution
list. These must be reconciled before canonical counting. All twenty-three have
matching named placed-feature and biome-modifier references, and every selected
NBT template exists in the frozen archive. This is packaged reachability, not
observed placement, effective eligibility or twenty-three canonical families.

| Candidate path under repurposed_structures | Configurations requiring reconciliation |
| --- | --- |
| dungeons/ | badlands, dark_forest, deep, desert, end, icy, jungle, mushroom, nether, ocean_cold, ocean_frozen, ocean_lukewarm, ocean_neutral, ocean_warm, snow, swamp |
| wells/ | badlands, cherry, forest, mossy_stone, mushroom, nether, snow |

The dungeon entries use nbt_dungeon; wells use nbt_feature. Ocean-temperature
configurations share template choices, so configuration count must not become a
family count. Preserve template/design, material and placement variants during
canonical reconciliation. Keep these candidates in the finite provider work list;
do not defer them behind detailed attributes or exclude them for lacking a
structure-registry root. The existing mansion/monument evidence is separate and
must be reused rather than recaptured.

```sh
uv run pytest -q tests/item8/test_repurposed_feature_candidates.py
uv run ruff check tests/item8/test_repurposed_feature_candidates.py
uv run basedpyright tests/item8/test_repurposed_feature_candidates.py
```

One focused case and scoped quality checks pass. Remaining Repurposed scope is
full feature roles, pool/template component reconciliation, entry/hook roles and
supported exclusions. Census is unchanged: 74 resolved providers, 62 open.

### Repurposed existing-graph partition

The existing pool-traces-content catalog covers 95 of the 107 packaged roots.
The twelve other roots are mansion_birch/desert/jungle/mangrove/oak/savanna/
snowy/taiga and monument_desert/icy/jungle/nether. Their custom assembly source
already exists; absence from the generic pool graph is not an exclusion.

| Resource partition | Pools outside generic root traces | Templates outside generic root traces |
| --- | ---: | ---: |
| Mansion paths | 416 | 597 |
| Monument paths | 80 | 92 |
| Dungeon NBT feature paths | 0 | 36 |
| Well NBT feature paths | 0 | 7 |
| Other paths requiring individual disposition | 7 | 53 |
| Total outside generic root traces | 503 | 785 |

The full packaged denominators are 1099 pools and 3162 templates. The 95 traces
have no missing or unresolved-element entries. This statement covers those
traces only, not custom assemblies, all feature consumers or the whole provider.
The table groups exact resource namespaces; it does not prove every grouped
resource is selected by its custom generator. Reconcile the retained mansion
and monument selectors before accepting that stronger claim.

The seven other pools are cities/nether/no_stair_room,
cities/overworld/no_stair_room, villages/cherry/trees, villages/giant_taiga/trees,
villages/giant_taiga/zombie/terminators, villages/mountains/trees and
villages/swamp/trees, all under repurposed_structures. The other 53 templates
partition into ancient_cities (3), bastions (5), mineshafts (16), strongholds (2)
and villages (27). Exact paths remain in the preserved template catalog and
are reproducibly selected by the new graph-partition test. These are component
questions, not 60 new families and not yet supported unused exclusions.

The two cases in test_repurposed_feature_candidates.py and scoped quality
checks pass. Early read-only probes used the wrong catalog path, then compared
resource_identity tuples against string IDs and omitted the NBT extension.
Those outputs were rejected. The tracked check uses the actual sources path,
identity[0] and explicit extensions. No accepted source data was changed.

### Repurposed custom component partition

The existing mansion selector and child-pool check now accounts for all 597
packaged mansion templates: 592 parent choices and five shared mob templates.
Of 416 pools, 376 are selector candidates and 24 are child mob pools. The other
16 are the front/side stair pools for the eight variants. Their single-template
entries reference templates already in the parent set, with empty fallbacks.
They introduce no additional authored site candidate.

The monument selectors account for 76 pools and 88 templates. The remaining four
pools and four templates are openings/wall_2, one per variant. Each template is
a 4 by 3 by 1 air-only volume without entities or block entities. These are
opening components, not independent sites. This closes the custom resource
partition for candidate membership; it does not prove runtime selection or
successful placement of every component.

```sh
uv run pytest -q tests/item8/test_mansion_components.py tests/item8/test_monument_components.py
uv run ruff check tests/item8/test_mansion_components.py tests/item8/test_monument_components.py
uv run basedpyright tests/item8/test_mansion_components.py tests/item8/test_monument_components.py
```

Remaining Repurposed scope: the seven other pools and 53 other templates listed
above, remaining feature roles and entry/hook dispositions. Provider scope is
still OPEN. These checks reuse the existing evidence and tests.
Four focused cases, scoped Ruff and Basedpyright pass. An initial lint failure
placed the existing complexity suppression on the wrong line of the multiline
function declaration; moving it to the declaration line resolved that failure.

### Repurposed residual resource roles

The third case in test_repurposed_feature_candidates.py binds the seven residual
pools to their actual contents. The two city no_stair_room pools contain existing
large, medium and tiny rooms plus bridge ends. Four village trees pools select
cherry, mega pine, pine and swamp tree features. The giant-taiga zombie terminator
pool selects four normal road-end templates. These are component alternatives,
not independent authored family candidates. Their absence from generic traces
remains recorded; this check does not establish actual selection.

| Residual templates | Count | Supported resource disposition |
| --- | ---: | --- |
| Mineshaft minecarts | 16 | Each matching mineshaft_minecarts configuration selects a 1 by 1 by 1 template with one chest minecart. These are encounter/loot components of mineshafts. |
| Ancient-city bottom_right_corner | 3 | No single-pool location selects the exact name. Pools select the corresponding _1 and _2 corner variants instead. Preserve these extra wall components. The initial substring search incorrectly appeared to find exact references and was rejected. |
| Stronghold crossing | 2 | No single-pool location selects the exact template. Piece-count data imposes a maximum of seven, without a required minimum. A same-named pool reference in start stairs targets a pool, not this NBT file. Preserve the extra crossing components without claiming activation. |
| Underground bastion mob templates | 5 | Air/jigsaw-only templates with one skeleton or skeleton horse each. No single-pool location selects these exact NBT files. The horse name also appears as a pool reference, which is a different resource kind. |
| Village components | 27 | Houses, streets, villagers and mobs under variants with existing village root definitions. None is selected by a single-pool location in this archive. Preserve the disconnected component alternatives; do not turn these paths into independent village families. |
| Total | 53 | All residual template resource roles accounted for; this is not runtime reachability proof. |

This closes the residual resource-role partition. Source entry/feature/hook
reconciliation must still determine whether additional code consumers affect
these dispositions before the provider row closes. Census remains 74 resolved
and 62 open. No new measurement or evidence format was added.

```sh
uv run pytest -q tests/item8/test_repurposed_feature_candidates.py
uv run ruff check tests/item8/test_repurposed_feature_candidates.py
uv run basedpyright tests/item8/test_repurposed_feature_candidates.py
```

Three focused cases pass. Initial formatting, unused suppression and JSON typing
findings were corrected in the focused check. Raw catalogs remain unchanged.

### Repurposed complete feature partition

Source 762b6f9 preserves the remaining 31 feature classes with exact independent
reproduction. Manifest SHA-256:
4e90a8ed5ea83a2db56830de2cd50d5dc2c5ed1149eb0d0ad06477eed7409230.
Together with the two existing NBT feature captures, this accounts for every
implementation class in the archive's world/features package outside configs.
The fourth focused case binds that exact class set, source hashes and the full
136 configured-feature partition across 37 types. The types and per-type counts
are explicit in the test, so additions or omissions fail the check.

| Feature implementation group | Contribution role |
| --- | --- |
| NbtDungeon and NbtFeature | Previously recorded sixteen dungeon and seven well configurations. Reuse their candidate/template links; do not count configurations as canonical families. |
| MinecartFeature | Reads the configured nbtPath, checks supporting block and fluid conditions, obtains that template and places it with entities enabled. The sixteen configured templates were checked above. A missing template logs a warning and returns false. No independent building design. |
| DrownedWithArmor, ShulkerMob, Skeletons, SkeletonHorseman, WitherSkeletonWithBow | Entity construction, equipment, persistence and placement at the supplied feature origin. These are authored encounter components. Equipment/enchantment helpers do not define another structure candidate. |
| MineshaftSupport | Reads surrounding arch/fence material and supplied configuration, extends supports, handles water-based openings and updates connected blocks. These are mineshaft component writes, not separate authored sites. |
| ConfigurableCoral and its claw, mushroom and tree implementations | Coral block placement and geometry using supplied coral materials. Vegetation components. |
| OceanTemperatureRandomSelector | Chooses a supplied placed feature using biome names and temperature. Its sole packaged configuration chooses three living or three dead coral forms for an ocean village. It introduces no separate authored site. |
| SimpleBlockWithFluidTick and UnderwaterBlockPileFeature | Supplied block-state placement, plant/fluid handling and underwater piles. Packaged piles use cobblestone, kelp, hay, melon or pumpkin material. These are block/vegetation decorations. |
| StructureChorus, StructureCrimsonPlants, StructureWarpedPlants, StructureFlowers, StructureGrass, StructureNetherwart, StructureSeagrass, StructureVine, StructureVineAndLeaves | Plant placement or overgrowth around the supplied origin and target blocks. No independent authored site. |
| StructureBreakage and StructureVineBreakage | Carving/replacement of existing blocks, with air, water and vines as applicable. These alter component condition rather than define a new structure family. |
| StructureChains, StructureEndRodChains, StructureFire and its map initializer, StructurePowderSnow, StructurePostProcessConnectiveBlocks | Chain/rod/fire/snow placement and connection-state updates on existing components. The noise helper supplies snow variation, not an additional content provider. |
| Packaged vanilla feature types | Trees, coral, flowers, patches and block piles. Their full type counts are included in the 136-row partition. |

The inspected feature methods write these blocks/entities, place the already
enumerated NBT choices, or delegate to the configured coral selector choices.
No additional independent family candidate was found in this feature pass.
This does not accept every invocation's success, exact gameplay effects or
effective placement eligibility. The shared entry, non-feature generation and
injection review still precedes whole-provider closure.

```sh
uv run pytest -q tests/item8/test_repurposed_feature_candidates.py
uv run ruff check tests/item8/test_repurposed_feature_candidates.py
uv run basedpyright tests/item8/test_repurposed_feature_candidates.py
```

Four focused cases pass. A read-only configuration probe initially included a
ZIP directory entry; filtering for JSON files corrected the probe. One overlong
test line was corrected. No raw evidence changed. Census remains 74 resolved
providers and 62 open; canonical counting remains downstream of provider closure.

## Repurposed Structures provider disposition

The complete frozen archive and its contribution boundaries are accounted for.
The provider contributes the 107 packaged roots that exactly match its captured
runtime structure registry, plus the already recorded sixteen dungeon and seven
well feature configurations. Canonical designs and variants must still be
reconciled; neither 107 nor 23 is a canonical-family count. Reuse all component
and feature dispositions above when doing that reconciliation.

Source 015f351 captures the seven remaining structure generators, common jigsaw
manager/assembler and piece-count manager. Its manifest SHA-256 is
10a3a2a15d647c5c52c171034c84be9c2fc68e1fe42dd571e8a6c725a6de6746.
Source 6fed290 captures the additional annotated data-generation entry, manifest
0d2237b825ac55da59a8908beb120e562b67a58ccc3a5de1c151e1bbd980d9bf.
Both independently reproduce exactly. The focused provider check binds all twelve
existing source manifests to the exact archive and disassembly hashes.

| Boundary | Supported contribution disposition |
| --- | --- |
| GenericJigsawStructure and subclasses | Consume configured start pools, size, height, biome/terrain checks, liquid settings and placement bounds. City, Nether, mineshaft, shipwreck and End stronghold implementations specialize placement of their supplied root candidates. They do not declare an additional independent root outside the packaged/runtime set. |
| MineshaftEndStructure | Uses the supplied start pool and common piece-limited assembly with its End placement/bounds handling. Keep it within the existing End mineshaft candidate. |
| PieceLimitedJigsawManager and Assembler | Start from the supplied pool, use its raw weighted elements, follow the jigsaw NBT pool field through the pool registry, and consider fallback pools. Required-piece selection, maximum counts, bounds, collision and attachment checks constrain these candidates. They do not treat a pool identifier as a same-named template identifier. Empty/missing pools and exhausted required-piece attempts have explicit log paths; this scope disposition does not claim every attempt succeeds. |
| StructurePieceCountsManager | Loads conditions, required counts and maxima for a target structure. A null alwaysSpawnThisMany produces no required-piece entry. The crossing maximum-only records therefore do not independently add those extra templates to the candidate set. |
| PoolAdditionMergerManager | Loads supplied rs_pool_additions data, parses the target pool and entries, then adds entries to existing pool lists. Reuse the already reconciled Farmer's Delight add-on component targets; the loader is not another family. Parsing failures remain explicit. |
| Common and NeoForge entries | Initialize registries and forward setup, start/stop, reload and trade events. Reload inputs are mob-spawner rules, structure-map trades, piece counts and pool additions. Loot-import and map-trade consumers affect existing families' attributes or discovery rather than define sites. |
| Declared feature mixins | Adjust existing bamboo, jungle bush, basalt/delta, falls, geodes, lakes, vines and snow placement using tagged structure context. These are generation modifications, not new authored designs. |
| Other declared common mixins | Access existing entity, map, loot, structure, pool and world state; adjust block-attached-entity logging, locate behavior and pool weight codec limits. No independent authored site. Their presence does not prove every injection executed. |
| Data-generation entry | StructureNbtUpdaterDatagen handles GatherDataEvent and registers a data provider when includeServer is true. This is build-time data generation, not a runtime family entry. The sole client-only mixin concerns the structure-block screen. |
| Remaining packaged implementation | Configuration, registry/event adapters, predicates, block processors, map/loot/spawner consumers, placement support, codecs, geometry/noise and data holders support the above entries. No extra service, nested archive, script or function payload exists. Do not expand this boundary review into unrelated helper correctness. |

Complete archive accounting covers 5842 files and 248 classes. Data categories
include all 3162 templates, 1099 pools, 327 processor lists, 136 configured
features, 157 placed features, 107 roots and 37 structure sets. The non-worldgen
data consists of the preserved tags, loot, spawner rules, piece counts, biome
modifiers, advancement and map-trade inputs. There is no unexplained additional
packaged content category. Both annotated entries and all 30 declared common
mixins are bound to captured source. This complements the semantic review;
absence of a keyword alone is not the exclusion criterion.

The resource-role and assembly checks support retaining the residual templates
as components of their existing candidate groups, with their disconnected or
non-selected status as qualified above. No additional standalone family follows
from them. Preserve effective eligibility, custom-layout reachability, generated
occurrences, downstream attributes and named variant/grouping decisions as
separate unfinished Item 8 work. In particular this closure neither proves all
107 roots generate nor counts biome variants as separate families.

```sh
uv run pytest -q tests/item8/test_repurposed_provider_scope.py tests/item8/test_repurposed_feature_candidates.py tests/item8/test_mansion_components.py tests/item8/test_monument_components.py
uv run ruff check tests/item8/test_repurposed_provider_scope.py tests/item8/test_repurposed_feature_candidates.py tests/item8/test_mansion_components.py tests/item8/test_monument_components.py
uv run basedpyright tests/item8/test_repurposed_provider_scope.py tests/item8/test_repurposed_feature_candidates.py tests/item8/test_mansion_components.py tests/item8/test_monument_components.py
```

Census: 75 resolved providers and 61 open. Next reconcile Aether, reusing its
existing Bronze, piece, placement and trap evidence. Do not repeat Repurposed's
source capture, component partition or feature inventory during that work.

## Aether candidate partition in progress

Provider scope remains OPEN. The frozen archive is
`aether-1.21.1-1.5.10-neoforge.jar`, SHA-256
a999a9265eb550a46a0f8eedfee7c3c75371d7f6cf34b7c09ff800e48633e9f8.
The existing cloud-provider test now binds the full packaged candidate partition:

| Resource group | Count | Current disposition |
| --- | ---: | --- |
| Base structure roots | 4 | Bronze, Silver, Gold and large aercloud exactly match the captured Aether runtime registry. Reuse the existing cloud terrain disposition. |
| Optional ruined-portal roots | 6 | Packaged under packs/ruined_portal, absent from the captured runtime registry. Preserve optional provenance; do not count them as active families. |
| Bronze templates | 6 | Previously captured and linked to Bronze assembly. Do not reopen Bronze helper internals for provider coverage. |
| Silver templates | 11 | Reconcile existing Silver entry with its builder and components, including test_door. |
| Gold templates | 4 | Reconcile existing Gold entry with island, boss room, tunnel and stub components. |
| Ruined-portal templates | 13 | Preserve their optional-pack relationship and check loader/entry consumers before final inactive disposition. |
| Configured features | 25 | Eleven types. Four custom implementations are aercloud, lake, crystal island and shelf; the others are vanilla ore/tree/plant/spring/selector types with supplied configurations. Custom behavior and special tree decorations still need roles. |
| Bundled JARs | 3 | Cumulus Menus 2.0.7, Accessories beta.48 and Nitrogen Internals 1.1.25, exact hashes bound by the test. Reconcile effective loader selection and shared roles; embedded filenames alone do not prove which version runs. |

All 34 NBT templates are under these four component namespaces. This is a
resource partition, not a canonical-family count or completed provider review.
Reuse the existing Aether source directories and tested cloud/Bronze bindings.
Remaining work is the named component consumers, custom feature/tree roles,
loader/event/mixin entry coverage and bundled-library disposition.

```sh
uv run pytest -q tests/item8/test_aether_cloud_source.py
uv run ruff check tests/item8/test_aether_cloud_source.py
uv run basedpyright tests/item8/test_aether_cloud_source.py
```

Two focused cases and scoped quality checks pass. No new measurement or capture
was needed for this resource partition. Census remains 75 resolved and 61 open.

### Aether Silver and Gold component candidates

The captured Silver entry selects rear, boss_room and skeleton. Its builder
selects floor, door, wall, tall_staircase, boss_door, staircase and chest_room.
SilverDungeonPiece qualifies supplied names under aether:silver_dungeon/.
Together these account for ten of the eleven packaged Silver templates.
The extra test_door template is not selected by these captured call-site names,
and no class in the archive contains its literal name. Preserve it as an
unselected component in these paths, not a separate family or a universal claim
about dynamically supplied names.

The captured Gold entry selects island, boss_room, stub and tunnel, accounting
for all four packaged Gold templates. GoldDungeonPiece qualifies supplied names
under aether:gold_dungeon/. Stub caves and the assembly pieces belong to this
existing dungeon candidate. Do not count those pieces as independent families.

The third case in test_aether_cloud_source.py binds the two exact source
manifests, every class/disassembly hash in them, the literal namespace recipes
in the frozen piece classes and these complete template-name partitions.
It does not simulate layout reachability or prove placement success, assembled
dimensions, boss behavior or visual discovery. These remain later attributes.

```sh
uv run pytest -q tests/item8/test_aether_cloud_source.py
uv run ruff check tests/item8/test_aether_cloud_source.py
uv run basedpyright tests/item8/test_aether_cloud_source.py
```

Three focused cases pass. One overlong manifest-reference line was corrected.
Remaining Aether scope: custom feature/holiday-decoration roles, main-entry
delegates/common hooks, optional portal consumer disposition and bundled-library
selection/roles. Reuse this component partition; census stays 75 resolved and
61 open until that provider scope is closed.

### Aether holiday-tree candidate boundary

Retain aether:holiday_tree as a named decoration/family-boundary candidate for
canonical reconciliation. It is not an accepted additional canonical family.
The configured tree's custom decorator places snow or provider-selected blocks
around suitable base-log positions. The supplied weighted provider contains snow
and aether:present. Do not dismiss that authored decoration solely because its
configured feature type is minecraft:tree, or count each decorated block as a
separate design.

The fourth case in test_aether_cloud_source.py binds the exact configured and
placed feature, the aether:holiday_filter placement entry and all four packaged
Skyroot biome consumers (forest, woodland, meadow and grove). Frozen
config/aether-server.toml has Generate Holiday Trees always=false and Generate
Holiday Trees seasonally=true, SHA-256
578abca7702fcecdb39845a7043f6ec1c504f153f6d3b4af45daedb29df931de.
These are input bindings, not proof the seasonal filter passed in any recorded
world. HolidayFilter is now captured in sources/aether-holiday-filter at 934edeb:
it uses the JVM calendar month, permitting December and January with these
frozen settings, subject to the other placement conditions. This resolves the
filter-source question without claiming an observed tree. Present
block reward behavior belongs to the later attribute pass, not provider scope.

```sh
uv run pytest -q tests/item8/test_aether_cloud_source.py
uv run ruff check tests/item8/test_aether_cloud_source.py
uv run basedpyright tests/item8/test_aether_cloud_source.py
```

Four focused cases and scoped quality checks pass. Keep this named ambiguity
with the finite candidate list. Remaining provider roles and canonical grouping
are still open; no new measurement system is required.

### Aether custom feature roles

The four custom feature implementations captured in sources/aether-provider
have these roles in the packaged configurations:

| Implementation | Contribution and census disposition |
| --- | --- |
| AercloudFeature | Writes the configured cloud block into empty positions along randomized clusters. Cloud terrain, not another authored structure family. |
| AetherLakeFeature | Carves air and supplied fluid, replaces suitable surface material and freezes water where the biome permits. Lake terrain, not another authored structure family. |
| ShelfFeature | Selects suitable ground/air boundaries and delegates supplied-block disk placement. The quicksoil configuration forms ground shelves. |
| CrystalIslandFeature | Attempts the configured crystal tree, then forms its supporting grass/holystone ground with surface-material handling. Tree and terrain formation; no separate architectural component is selected by this implementation. |

These roles use the existing captured implementations and packaged candidate
partition, not a new world measurement. The holiday-tree decoration remains the
separate named boundary above. Do not reopen these feature implementations to
measure geometry or rewards during the census.

Aether's remaining provider checks are main-entry/common-hook contributions,
optional ruined-portal activation and component consumers, and effective
selection/contribution roles for its three nested libraries. Provider census
remains 75 resolved and 61 open; these are providers, not remaining families.

### Aether nested-library runtime selection

The preserved registry-r1 debug log explicitly records JarSelector using the
top-level Accessories beta.53 archive instead of the embedded beta.48 candidate.
Its final mod list contains Accessories 1.1.0-beta.53+1.21.1. Attribute active
Accessories code to that retained provider's queue row; do not separately audit
the unselected beta.48 implementation as another running contribution.

Cumulus 2.0.7 and Nitrogen 1.1.25 appear in the final mod list, with discovery
records identifying Aether as their parent. Their contribution roles remain to
be resolved. The existing packaged partition binds all three embedded hashes;
test_aether_nested_runtime_selection binds the log hash and exact selection,
parent and final-list records. This closes selection, not library behavior.

```sh
uv run pytest -q tests/item8/test_aether_cloud_source.py
uv run ruff check tests/item8/test_aether_cloud_source.py
uv run basedpyright tests/item8/test_aether_cloud_source.py
```

Five focused cases and scoped quality checks pass. No new runtime run or
measurement system. Continue main/common hooks, portal consumers, and the two
selected embedded library roles before closing Aether's provider row.

### Aether optional ruined-portal disposition

The captured main entry registers builtin/aether_ruined_portal as a server-data
pack. Its PackSource receives add_ruined_portal_automatically; Aether$2 returns
that supplied boolean from shouldAddAutomatically. Frozen aether-common.toml
sets Add Ruined Portals automatically=false. The pack is not required by its
PackSelectionConfig. All six optional root definitions use aether:ruined_portal
and are absent from the captured runtime registry. Disposition: optional,
inactive structure candidates in this frozen registry, not active families.

GlowstoneRuinedPortalStructure selects under the aether namespace from ten
ruined_portal/portal_1 through portal_10 names and three giant_portal_1 through
giant_portal_3 names. Its generation stub passes the selected resource to
GlowstoneRuinedPortalPiece. These account for all thirteen packaged portal
templates as components of the optional roots. Do not count the pieces as
thirteen additional families or claim that another configuration cannot enable
the optional pack.

test_aether_cloud_source.py now binds the common-hook source manifest, exact
portal template partition, all optional root types and frozen common-config
hash. The initial read-only ZIP probe mistakenly included a directory entry
and failed JSON decoding; rerunning with the .json filter resolved that probe
error. No source evidence or frozen configuration was changed.

```sh
uv run pytest -q tests/item8/test_aether_cloud_source.py
uv run ruff check tests/item8/test_aether_cloud_source.py
uv run basedpyright tests/item8/test_aether_cloud_source.py
```

Six focused cases and scoped checks pass. This resolves the optional portal
resource/activation boundary. Aether common-hook roles and selected bundled
library roles remain open; census remains 75 resolved and 61 open.

### Aether selected-library entry boundaries

Source aether-cumulus-entry (62defac) records the Cumulus mod entry's CLIENT
restriction, its client subscribers and its globally declared storage mixin.
The mixin wraps the directory-lock check while loading level summaries: it
returns false when world preview is active and MixinHooks.canUnlockLevel permits
it, otherwise calling the original check. It does not place a structure in this
captured method. The exact platform service is IPlatformHelper implemented by
NeoForgePlatformHelper. Its behavior remains to be inspected before closure.

Source aether-nitrogen-entry (9c29cff) records Nitrogen's entry and tooltip
subscriber. In addition to user information and packet handling, the constructor
registers loot types, biome-modifier serializers, foliage placers and trunk
placers. Do not exclude its world-generation support based on its user hooks.
Reconcile these serializers and their actual packaged consumers.

The existing packaged partition test now checks both embedded payloads for data,
packs and further embedded archives, enumerates their common mixins and binds
the Cumulus platform-service declaration. Neither contains packaged data, packs
or further JARs. Nitrogen has no common mixins or services; Cumulus has the one
storage mixin and one platform service above. The first test attempt incorrectly
asserted no services and failed on Cumulus. The corrected expectation preserves
that discovered entry; it does not silently ignore it. Scoped type errors in
the new mixin-list accumulation were also corrected. Six focused cases and
scoped checks pass using the commands immediately above. Contribution roles
remain open, not inferred from this payload partition alone.

### Aether reload and selected-library role resolution

Source aether-reload-consumers (7340422) closes the two reload handlers:
RecipeReloadListener clears the freezing block's cached recipe tables and
results; BannerReloadListener clears the cached Swet banner item. Neither
selects or places another site.

Source aether-cumulus-platform (300dd88) closes the platform service's role:
it discovers CumulusEntrypoint-annotated MenuInitializer implementations for
the client menu path and forwards supplied packets through PacketDistributor.
Together with the captured client entry and storage-summary lock predicate,
this accounts for Cumulus as menu/preview/platform support, not an independent
structure provider. No runtime structure-placement success is implied.

Source aether-nitrogen-world (c5d2128) resolves the registered world support:
nitrogen_internals:add_mob_charge modifies the supplied biome's mob-spawn charge
and energy budget for a supplied entity type. It does not select structure
resources. hooked_trunk_placer builds trunks and branches from a supplied tree
configuration and returns foliage attachments. aether_pine_foliage_placer and
hooked_foliage_placer place leaf rows around supplied foliage attachments.
These are mob-spawn settings and tree geometry, not independent architectural
families. Nitrogen supplies no packaged data to invoke them independently;
other mods' supplied configurations remain attributable to their own provider
rows. Loot support remains relevant to the later attribute pass.

All three source captures have exact reproducible commands and independently
matching r1 output in their READMEs. This closes the reload-handler and selected
library role questions using the existing source path, without a new validator
or runtime sample. Aether's remaining common-hook reconciliation and final
whole-provider check are still required. Census remains 75 resolved and 61 open.


### Aether provider scope resolved

The frozen archive's entry, declared common mixins and complete packaged payload
are reconciled with the existing candidate/component evidence. Provider coverage
is RESOLVED. This is not Item 8 completion or a final canonical-family count.

The common hooks modify existing entities, equipment, combat, riding, time,
dimension travel and player attachments. AbstractArrow handles arrow effects and
synchronization; ArmorStand and Mob handle equipment; DimensionType handles time;
Entity and LivingEntity handle travel/damage; Player handles riding/equipment and
appearance; ServerPlayer removes its attached Aerbunny on disconnect. EventHooks
modifies accessories on an existing mob's spawn. ModelBuilder handles model
textures, and accessor mixins expose existing fields/methods. These are not
independent structure starts. DimensionHooks initializes level data and manages
time or portal interaction/travel; its callbacks do not select another authored
world-generation design. The two reload cache handlers and library roles have
separate resolved dispositions immediately above. Do not audit unrelated combat
or attachment internals to repeat this provider census.

The complete data partition adds no unassigned structure resources beyond the
previously recorded roots, templates and feature boundary. Remaining data is
recipes, advancements, tags, loot, damage types, songs, item fuel/composting maps,
Moa types, trims and the Aether dimension/terrain definitions. The three developer
functions only teleport, set spectator/night vision or replace dirt/stone with
air. Their exact contents are bound by the provider test; they do not place sites.

Optional classic, tips, CTM, colorblind and tooltip packs provide presentation
resources; Accessories packs provide equipment slots/tags and temporary freezing
provides recipes. The ruined-portal pack is accounted for above. The six
Immersive Portals definitions convert conventional portals or respond to water
bucket use between the Overworld and Aether. setupImmersivePortalsPack requires
immersive_portals_core, absent from the hash-bound runtime mod list. These are
inactive compatibility definitions, not additional active authored families.

The inventory therefore retains Bronze, Silver and Gold dungeon candidates,
large-aercloud terrain, and the explicitly named conditional holiday-tree
boundary. Portal templates remain components of inactive optional roots. Preserve
all earlier component/eligibility limitations; provider closure does not prove
observed placement, dimensions, rewards or visual discoverability.

The focused provider check reuses the established provider-test pattern. It
binds the original archive, all fifteen existing source manifests and their
class/disassembly identities, the complete payload partition, annotated entry,
common mixins and exact function contents. Together with the candidate, nested
selection and Bronze checks it is the bounded proof for this provider. Initial
string-format lint findings were corrected without changing expected commands.

```sh
uv run pytest -q tests/item8/test_aether_bronze_components.py tests/item8/test_aether_provider_scope.py tests/item8/test_aether_cloud_source.py
uv run ruff check tests/item8/test_aether_provider_scope.py tests/item8/test_aether_cloud_source.py
uv run basedpyright tests/item8/test_aether_provider_scope.py tests/item8/test_aether_cloud_source.py
```

Scoped checks pass. Census is 76 resolved providers and 60 open. Continue the
remaining provider queue before canonical reconciliation and the eleven family
attributes. No final Item 8 gate, review or merge is claimed.

### Deep Aether candidate partition

test_deep_aether_candidates.py binds the frozen archive and existing parsed
catalog. Four packaged roots exactly match the captured runtime registry:
altar_camp, brass_dungeon, campfire and combiner_corridor. The three non-Brass
roots use deep_aether_jigsaw and target sacred_lands. Reuse test_totem_scope.py's
existing dimension-membership result; registry presence is not active biome
eligibility. The totem's earlier inactive disposition remains in force.

All fifteen templates partition into twelve Brass components (five numbered
rooms, five boss counterparts, door and room_part_up) and three Sacred Lands
components named after the three jigsaw roots. Their actual executable consumers
still need reconciliation; template count is not family count.

The sixty configured features contain seven Deep Aether implementation types:
aercloud_cloud, rain_aercloud_cloud, aercloud_roots, fallen_tree,
improved_mushroom_feature, poison_lake and totem. Reuse the totem capture and
accepted Aether cloud/lake/shelf roles, then inspect the remaining custom
implementations and registration for contributions outside packaged definitions.
DAFeatures and the Brass/jigsaw entry consumers are the next source boundaries.
The original strict-JSON probe failed on packaged comments; the existing parsed,
hash-bound catalog supplies these definitions without changing the archive.

Two bundled archives are hash-bound: Aeroblender 1.0.0 and TerraBlender 4.1.0.3.
Resolve effective selection against the retained top-level TerraBlender 4.1.0.8,
and account for Aeroblender's entry role. Do not audit both TerraBlender versions
as running merely because both are packaged.

```sh
uv run pytest -q tests/item8/test_deep_aether_candidates.py tests/item8/test_totem_scope.py
uv run ruff check tests/item8/test_deep_aether_candidates.py
uv run basedpyright tests/item8/test_deep_aether_candidates.py
```

Two focused cases and scoped checks pass. Deep Aether remains OPEN. Remaining
work is the named structure/feature consumers, annotated/common mixin entries,
optional-pack roles and nested-library selection/contribution roles. Census
remains 76 resolved and 60 open; no new measurement system is required.

### Deep Aether library selection and entry source

The preserved registry-r1 log explicitly selects retained TerraBlender 4.1.0.8
over embedded 4.1.0.3. Its final mod list confirms that version and AeroBlender
1.0.0; the discovery record identifies Deep Aether as AeroBlender's parent.
test_deep_aether_nested_runtime_selection binds these records and the exact log
hash. Attribute active TerraBlender behavior to its retained provider row and
do not audit the unselected embedded implementation as another running provider.
AeroBlender's contribution role remains open.

The existing extractor now captures Deep Aether's fourteen annotated entries,
eleven common mixins, feature registration/nine remaining implementations and
eight Brass/jigsaw consumers in sources/deep-aether-provider. Manifest SHA-256:
71c441da5bd3213d84b0ce9f1f38f098979d158b3f16146397428b99e958d5c4.
Independent r1 matches every generated file. Verbose source preserves side
annotations and callback bindings. Interpret these captured boundaries before
following any helper; do not repeat the totem or candidate partition.

Three focused candidate/selection/totem cases and scoped checks pass using the
commands above. Provider coverage remains OPEN. Source capture is not acceptance
of the contribution roles; no final family count or Item 8 completion is claimed.

### Deep Aether Brass component reconciliation

The captured BrassDungeonStructure selects brass_dungeon_room_0 through _4.
createBossRoom appends _boss for the boss-room branch, uses the ordinary room
otherwise, and adds room_part_up. generatePieces also selects door.
BrassDungeonPiece qualifies the supplied names under brass_dungeon/. Together
these select all twelve packaged Brass templates as dungeon components, not
twelve independent families. This is a call-site/name reconciliation, not a
simulation of successful assembly or a proof of dimensions or encounter quality.

test_deep_aether_brass_source_binding binds the exact source manifest and every
captured class/disassembly hash, plus the actual constant-pool concatenation
recipes and room-name choices. The existing packaged partition supplies the
exact twelve-template set. Four focused candidate/selection/source/totem cases
pass; a combined-assertion lint finding was split and its affected case rerun.
Scoped Ruff and Basedpyright pass. No new capture or measurement was needed.

Remaining Deep Aether work: jigsaw consumer/eligibility reconciliation, custom
feature and common-entry roles, optional packs and AeroBlender's contribution.
Do not reopen the Brass room-name or inactive-totem checks during that census.

### Deep Aether jigsaw component and eligibility reconciliation

DAJigsawStructure applies HeightSpawningChecks and then calls vanilla
JigsawPlacement.addPieces with the supplied start pool, height, size, alias and
placement settings. The height check compares the chunk-origin surface height
strictly between the supplied minimum and maximum. It does not select an
independent template outside the supplied pool route.

Each of altar_camp, campfire and combiner_corridor uses its same-named pool.
Each pool contains exactly one rigid minecraft:single_pool_element referring
to deep_aether:sacred_lands/<name>, with empty processors and empty fallback.
These account for the three packaged Sacred Lands templates as components of
the existing roots. The focused candidate test now binds these exact pool
documents; the source-binding case already covers both captured consumers.

All three roots require deep_aether:sacred_lands. The previously accepted
dimension-membership evidence in test_totem_scope.py excludes that biome from
every captured dimension. Disposition: registered but ineligible through these
packaged root/biome routes in the captured baseline, not three active families.
Preserve the candidates and reopen only if another active route is demonstrated.
This does not prove universal unreachability under changed packs or dimensions.

Four focused cases and scoped Ruff/Basedpyright pass using the commands above.
Brass and jigsaw component reconciliation are now resolved. Remaining provider
work is custom feature/common-entry roles, optional packs and AeroBlender,
followed by the whole-provider check. Census remains 76 resolved and 60 open.

### Deep Aether fallen-tree candidate boundary

Retain the fallen Aerglow tree as a named candidate for canonical reconciliation,
with ordinary and rotten-log configuration variants. FallenTreeFeature writes
supplied log states along a horizontal direction and can add supplied decoration
blocks around the logs where placement tests permit. Its supplied configurations
are fallen_aerglow_tree (roseroot_log) and empty_fallen_aerglow_tree
(rotten_roseroot_log); both use lightcap_mushrooms decoration. Do not count each
log, mushroom, orientation or length as an independent family.

The existing candidate test binds both configurations, their placed features
fallen_aerglow_forest and empty_fallen_aerglow_forest, and the packaged biome
references in aerglow_forest, blue_aerglow_forest and mystic_aerglow_forest.
Configured bounds are inputs, not a guarantee of generated dimensions.
This preserves a membership/grouping boundary, not a claim of observed placement,
an accepted final family count or a later gameplay classification.

Four focused cases and scoped checks pass with the commands above. The first
read-only method lookup assumed addDecorators was private; the captured method
is public, and its body was inspected under that actual signature. No capture
was changed or regenerated. Remaining provider work is the other custom-feature
roles, common entries/mixins, optional packs and AeroBlender's contribution.

### Deep Aether remaining feature roles

The captured DAFeatures registration and implementation bodies resolve the
remaining custom feature roles without another runtime sample:

| Implementation | Contribution role |
| --- | --- |
| AercloudCloudFeature | Noise-shaped supplied cloud blocks, with optional aercloud grass. Terrain formation. |
| RainAercloudCloudFeature | Cloud formation with fluid placement and post-processing. Terrain formation. |
| RootFeature | Places aercloud-root blocks at suitable empty positions. Vegetation decoration. |
| PoisonLakeFeature | Carves a supplied-fluid lake, forms its barrier/surface and handles freezing/post-processing. Terrain formation. |
| DAHugeMushroomFeature | Supplied mushroom cap/stem blocks, roots and ground alteration. Large vegetation, not a separate architectural template route. |
| CloriteColumnsFeature | Finds suitable air/ground boundaries and places columns. Stone terrain formation. |
| ConfiguredBoulder | Places supplied blocks in a boulder formation at suitable ground. Stone terrain formation. |
| RockSpikeFeature | Forms a stone spike; not selected by the captured DAFeatures registration. Preserve the implementation's existence without counting it as a separate active site. |

The configured-feature partition already binds all packaged custom types.
Clorite columns and configured boulders are registered but have no configured
feature among that partition. The totem and fallen-tree candidate dispositions
remain separate and unchanged. No dimensions, placement success or gameplay
attributes are inferred from these implementation roles.

### AeroBlender integration source

The selected library's entry, region/surface types and declared mixins are
captured in sources/deep-aether-aeroblender. Manifest SHA-256:
414711e4c35a498420ead8f3a7de80e7e7b8feb15909a19fb2dcebdba6ef5dc7.
Independent r1 matches every generated file. The entry and mixins adapt region
selection, biome-source applicability, noise-layer uniqueness and namespaced
surface rules for Aether. They do not select architectural templates. The
default region supplies Aether biome mappings and surface-rule support.
Bind the library's complete payload in the final provider check; do not inspect
its configuration-value builders unless an actual eligibility input needs them.

Remaining Deep Aether scope is common entry/mixin roles, optional packs and
the complete provider check including this nested payload. Census remains 76
resolved and 60 open. All source is delivered; no process remains running.

### Final Deep Aether provider disposition

Deep Aether provider coverage is RESOLVED. Reuse the candidate, Brass, jigsaw,
totem, fallen-tree and feature dispositions above. The four registered roots,
fifteen templates and sixty configured features are fully partitioned. Preserve
the inactive Sacred Lands routes and the named fallen-tree grouping boundary.
Neither templates nor configuration variants become additional families.

The final common-setup delegates are retained in sources/deep-aether-biome-setup
at 193bbe3, manifest SHA-256:
d0c5ae38827b28d5db0048c2f5da5603e116a8c070991d1ab198b610af2a126f.
DARegion and DARareRegion add climate-to-biome mappings. DASurfaceData selects
surface block states using biome, noise and depth conditions. These resolve the
actual common-setup calls without introducing additional authored-site routes.

The captured main entry registers data generation, common setup, capabilities,
network packets, recipe categories and optional packs. GatherDataEvent is an
offline data-generation path. Common registration and the fourteen annotated
entry classes cover entity registration, equipment and combat effects, block
interactions, client presentation and the generation routes already reconciled.
Dungeon player/death hooks affect encounters and rewards in existing dungeons.
They remain attribute inputs, not independent families.

The eleven common mixins handle brewing fuel/menu acceptance, glove attributes,
trivia text, cloud collision, block sound, fluid replacement, dripstone and snow
interactions, item conversion and Aerwhale riding/container/entity state. These
are existing-block/entity behavior. No unresolved authored-site entry remains
in those captured boundaries. The separately declared client mixins concern
rendering and presentation.

The whole archive has 4,136 files and 375 classes. Its data contains 132 worldgen
resources, fifteen structure templates, tags, recipes, advancements, loot and
item/entity-related definitions. The 265 optional-pack files contain 86 recipe,
49 advancement and two legacy recipes entries, plus assets and pack metadata.
There are no additional structure definitions in those packs. Packaged datagen
cache files are part of the pinned archive identity, not new runtime inputs.
No outer service declarations or executable function/script files are present.

The selected AeroBlender payload is exactly sixteen classes and nine other files.
Fourteen classes already captured cover its entry, region/surface support and
mixins; the two remaining classes define configuration values. Its four data
files supply density, noise, Aether noise settings and a dimension-type tag.
The other files are loader/access metadata, mixin configuration and pack metadata.
There is no additional template or structure payload. The embedded TerraBlender
4.1.0.3 is not selected; retained 4.1.0.8 remains its own open provider row.

```sh
uv run pytest -q tests/item8/test_deep_aether_provider_scope.py tests/item8/test_deep_aether_candidates.py tests/item8/test_totem_scope.py
uv run ruff check tests/item8/test_deep_aether_provider_scope.py
uv run basedpyright tests/item8/test_deep_aether_provider_scope.py
```

Five cases pass (1.86 seconds); scoped Ruff and Basedpyright pass. The final case
binds four preserved source manifests to original class and disassembly bytes,
the whole payload partition, annotated entries, common mixins, optional-pack
categories and the complete selected nested payload. It extends the existing
provider-check pattern to close this specific coverage gap. No new measurement,
framework or runtime sample was added. Provider closure does not establish
observed placement, the final canonical count or the eleven family attributes.
Supported dispositions now cover 77 of 136 providers; 59 remain open.

### Regions Unexplored packaged component boundary

Provider coverage remains OPEN. Existing feature and surface contribution
checks are reused. Source increment f479e0a retains fifteen loader/common-entry
and mixin classes in sources/regions-unexplored-provider, extracted with a5efbc8.
Manifest SHA-256:
cb7185024530c1b77bbf71dbf9ccefb2ba1acf505688896a1803f0a4240a4894.
Independent r1 matches every generated file. The new focused check binds these
classes, including all three annotated entry classes and nine common mixins,
to the retained archive and captured disassembly bytes.

The pinned archive has 8,077 files and exactly one NBT template:
regions_unexplored:trial_chambers/ashen. Its sole actual template-pool definition
selects that template and the melee trial-spawner pool tag includes that pool.
The existing pool-link check already proves the selected graph reaches this
component from minecraft:trial_chambers; normal and ominous spawn potentials
name regions_unexplored:ashen. Preserve this as an existing-family encounter
component, not an independent family. No packaged structure or structure-set
definition and no regions_unexplored runtime structure root are present.

The provider's own worldgen directory contains 386 configured features,
287 placed features, 78 biomes, ten processor lists, five noise definitions,
one density function and one template pool. Tags and overlays are separate
resource roles and must not be added to these definition counts.

```sh
uv run pytest -q tests/item8/test_regions_unexplored_candidates.py tests/item8/test_pool_links.py tests/item8/test_feature_modifier_references.py tests/item8/test_surface_rule_contribution.py
uv run ruff check tests/item8/test_regions_unexplored_candidates.py
uv run basedpyright tests/item8/test_regions_unexplored_candidates.py
```

41 cases pass (12.40 seconds). Scoped Ruff and Basedpyright pass after splitting
one overlong line. No new measurement or repeated runtime capture. Remaining
provider work: interpret the captured entry/mixin roles, account for custom
features beyond the existing modifier subset, and reconcile the remaining
payload including overlays and the embedded JSON5 library. The provider stays
in the existing queue: 77 resolved and 59 open. Do not repeat the Ashen component
or the previously accepted 34 feature-modifier and surface-rule analyses.

### Regions Unexplored fallen-tree candidate

Source 23f8c7b adds the fallen-tree implementation and the two direct biome/
surface delegates under sources/regions-unexplored-generation-delegates.
Manifest SHA-256:
b779daaf84f5a04384246079c6ada082941188e6319cb4c8835bfe6dad089770.
The existing extractor 389b2ed produced an exact independent r1 repeat.

Retain one named stump-and-fallen-log candidate with six configuration variants:
larch, maple, oak, pine, silver_birch and snow_pine. Their supplied log states,
length bounds and decorators vary; these are not six independently established
families. RUFallenTreeFeature places the stump first, chooses a horizontal
direction, tests the log run and places/decorates that run only if it fits.
Its place method returns true regardless of the log-fit result. Preserve the
possible stump-only outcome; do not claim observed placement or whole-form
success from the return value or supplied length bounds.

The focused candidate test binds the exact six configurations, their supplied
logs and bounds, empty stump decorators, attached-to-log decorator type, and
the new source manifest/class/disassembly identities. Decorator implementation
and placement-consumer reconciliation remain open. This is a named canonical
boundary, not a completed family count or a new runtime measurement.

```sh
uv run pytest -q tests/item8/test_regions_unexplored_candidates.py
uv run ruff check tests/item8/test_regions_unexplored_candidates.py
uv run basedpyright tests/item8/test_regions_unexplored_candidates.py
```

Both cases and scoped quality checks pass. Provider coverage remains OPEN:
77 resolved, 59 open. Continue the other feature/entry and payload roles rather
than repeating this candidate's implementation capture.

### Regions Unexplored region and terrain integration

The captured RULithostitched entry registers three integration callbacks:
worldgen modifiers, regions and biome injectors. Its modifier callback adds
Nether surface rules, removes water springs in Inferno, and wraps Overworld
fluid-level floodedness using inferno_weight. These alter terrain generation;
they do not create a structure start, pool or template.

RUSurfaceRuleBuilder.nether composes vanilla surface conditions and supplied
block states, including nylium, netherrack, gravel, lava and bedrock. Its remaining
helpers return block/air rules or noise conditions. BiomeTarget supplies biome
replacement parameters and target holders. Its special injector branches add
climate points for Prismachasm and Redstone Caves, force Inferno using depth and
density conditions, and force Chalk Cliffs using climate conditions. Other
special cases return null. No architectural content is selected by these
methods. These direct delegates are now reconciled; do not expand their census
into a terrain-quality experiment or general climate-mapping audit.

The source identities are bound by the passing candidate checks above. This
resolves contribution roles only. Frozen effective settings and observed
placement remain distinct evidence. The provider is still OPEN pending the
remaining feature, entry and payload dispositions.

### Regions Unexplored fallen-tree placement and decoration links

The eight packaged placed-feature definitions map to the six configurations:
larch, maple and silver_birch map directly; oak_dense and oak_sparse share oak;
pine and pine_on_dirt share pine; pine_on_snow uses snow_pine. Nineteen packaged
biomes reference these placements. The exact mapping is now bound by the existing
candidate test. This proves packaged consumer links, not observed placements or
effective biome frequency in every captured dimension.

AttachedToLogsDecorator is retained in source 1c53b0f, extracted with 947a0fa.
Its manifest SHA-256 is
7656c29c7f0b77b5827cbb01b082d2509f800a7cac87e342ec47bc6785bdc77d.
Independent r1 matches. The decorator shuffles the supplied log positions,
checks all configured directions or a random one, applies its probability test,
and places the supplied block state only in air with non-air below. The six
configurations supply moss carpet, mushrooms or snow. These decorate the
existing candidate rather than introducing another structural layout.
The previously inspected Lithostitched random-block provider supplies the
configured mushroom states and does not require another capture.

Both candidate cases and scoped Ruff/Basedpyright pass using the commands above.
The test also binds the decorator's original class and preserved disassembly.
Fallen-tree implementation, variants, packaged placement links and decorator
roles are resolved for this scope pass. Preserve the stump-only limitation.
Remaining provider work is other features, common entry roles and remaining
payload/overlay/JSON5 coverage. Census remains 77 resolved and 59 open.

### Regions Unexplored rock, spire, ground and pool feature roles

The thirteen implementations in sources/regions-unexplored-terrain-features
(source 4d65d81) and the shared PointedRedstoneUtils writer in
sources/regions-unexplored-redstone-writer (source 690e757) resolve this batch:

| Implementation | Contribution role |
| --- | --- |
| BasaltBlobFeature | Basalt column/blob terrain. Chest and masonry references occur in CANNOT_PLACE_ON exclusions, not in a generated chest/building palette. |
| FloorIcicleFeature | Upward icicle block columns with base, middle, frustum and tip states. Mineral/ice decoration. |
| MarshFeature | Ground and water reshaping with grass, lilies and other surface vegetation. Marsh terrain. |
| NetherRockFeature | Irregular bone/overgrown-bone formations with ground/netherrack handling. Natural geological decoration, not an articulated authored skeleton. |
| ObsidianSpireFeature | Obsidian/cobalt-obsidian blobs and a spire formed by direct block placement. Geological formation, not a rectilinear monument design. |
| PointedRedstoneFeature and PointedRedstoneClusterFeature | Cave mineral columns and clusters. Shared writer creates raw-redstone bases and pointed-redstone columns with direction/thickness states; cluster also handles water. |
| RockPillarFeature | Stone pillars/blobs with surface grass and underwater coral choices. Geological/reef formation. |
| SeaRockFeature | Configured rock geometry, water/air clearing and ice/snow handling. The packaged hyacinth rock supplies stone and mossy stone. |
| WaterEdgeFeature | Ground-edge reshaping and duckweed vegetation at water boundaries. |
| IceSpireFeature | Configured spire geometry through trunk/foliage providers. The packaged ice_spire supplies packed ice and ice, not a wooden structure. |
| RURockFeature | Offset blobs of supplied stone/cobblestone/mossy variants. |
| CarvedLimitedPoolFeature | Water-pool carving with supplied slope and slope-top states and wall/pool predicates. The packaged definition supplies dirt and grass over mud. |

These paths contribute terrain, minerals and vegetation rather than another
canonical authored-site family. This uses their actual writers and supplied
materials, not the provider name or a keyword absence rule. Randomized natural
formations follow the existing BetterEnd/BOP terrain distinction. Do not count
each blob, column, material variant or feature configuration as a family.

The two new manifest hashes are:
408438fe5484a1798d6487f12725cd3becac5c315a0d99dc585163177a2d474c
(terrain implementations) and
31143f1076e6d08d7280dd918331ce67087d07626cfe25778608398c26827bdd
(shared redstone writer). The existing candidate/source test binds all class
and disassembly bytes to the retained archive. Both cases and scoped Ruff and
Basedpyright pass with the commands above. No runtime experiment or new
validation framework was added. Do not infer placement frequency, footprint or
reproducibility of random geometry from these contribution-role decisions.

This batch is resolved. Other vegetation implementations, remaining common
entry roles and full payload/overlay/JSON5 reconciliation still prevent provider
closure. Census remains 77 resolved and 59 open.

### Regions Unexplored registered implementation source coverage

Source 04c515f captures the remaining 35 feature implementations selected by
RUFeatureTypes, using extractor b5e5564. The full generation command is in
sources/regions-unexplored-vegetation-features/README.md. Manifest SHA-256:
6e77e0aab7c6f999e08de37eca0fdf8417b07377823cd848bae016e50cdc1bb6.
Independent r1 matches every generated file. The isolated large source increment
preserves complete implementations rather than selected favorable excerpts.

The existing test now binds this manifest and the original feature-registration
manifest, then reconciles all 53 directly constructed custom-feature classes
against preserved class/disassembly identities. This is source coverage only:
18 implementation captures preceded this increment; the remaining 35 still need
semantic contribution dispositions. It does not close the whole provider,
resolve custom tree placers/decorators, or establish a canonical-family count.

Both focused candidate/source cases pass (0.93 seconds); scoped Ruff and
Basedpyright pass. An overlong line and implicit string concatenation were
corrected before final validation. Continue the captured vegetation roles and
remaining common-entry/payload boundaries. Do not repeat accepted terrain,
fallen-tree, trial-chamber, modifier or surface checks. Census remains 77
resolved and 59 open.
