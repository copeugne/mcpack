# Retained-provider scope pass

Status: every retained provider has a supported membership disposition.
Canonical family reconciliation remains incomplete.
Supported provider dispositions: 136 of 136. The exact queue below has 0 open rows.
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
| `BiomesOPlenty-neoforge-1.21.1-21.1.0.13.jar` | BOP entry, feature and delegated-material captures; test_bop_feature_candidates.py | RESOLVED: All registered features and packaged resources have contribution roles. Anomaly and monolith are two accepted landmark families; both pumpkin forms and bone-spine IDs are excluded decorations. Canonical membership decisions are integrated below. No structure roots, templates or pools. See final BOP disposition below. |
| `CreateDragonsPlus-1.11.2b.jar` | create-dragons-plus-provider, startup and conditional captures | RESOLVED: Machine/fluid/dye/recipe and existing-loot support, no independent family. Preserve loot and processing effects below. |
| `CreeperOverhaul-neoforge-1.21.1-4.0.6.jar` | `creeper-overhaul-provider` (e8d3713), `creeper-overhaul-login` (d21ca8f), test_creeper_overhaul_provider_scope.py | RESOLVED: Biome mob spawning, entity behavior/loot and cosmetic synchronization; no independent structure family. Full payload and bundled-library boundary below. |
| `DungeonsArise-1.21.1-2.1.68-release.jar` | `wda-provider-scope` | RESOLVED: see WDA structure-provider disposition below. |
| `FarmersDelight-1.21.1-1.3.2.jar` | `farmers-delight-provider` (555d912), common setup 15cb251, server packet 6678ec9; test_farmers_delight_provider_scope.py | RESOLVED: Five vanilla village components, farm-processor crop changes, vegetation and food/item interactions. No independent structure family. Full disposition below. |
| `GlitchCore-neoforge-1.21.1-2.1.0.2.jar` | Sources a447496 and a2fc4ee; test_glitchcore_provider_scope.py | RESOLVED: Consumer events, configuration synchronization and platform adapters. No independent family. See GlitchCore disposition below. |
| `IllagerInvasion-v21.1.6-1.21.1-NeoForge.jar` | `illagerinvasion-provider`, `illagerinvasion-extensible-enums` (e0f2c9a), existing pool codecs, test_illagerinvasion_provider_scope.py | RESOLVED: Five existing roots, thirteen mansion replacement components and encounter/loot modifications. Bundled enum library has no independent family; disconnected pillager pool/template preserved below. |
| `LeavesBeGone-v21.1.1-1.21.1-NeoForge.jar` | `leavesbegone-provider` (69119c6), test_small_utility_provider_scope.py | RESOLVED: Leaf ticking and chunk tick persistence; no authored structure contribution. See small utility provider dispositions below. |
| `Patchouli-1.21.1-93-NEOFORGE.jar` | `patchouli-provider`, `patchouli-books`; complete payload/source binding. | RESOLVED: documentation books, existing lectern interaction and consumer multiblock APIs. No independent family. |
| `PuzzlesLib-v21.1.52-1.21.1-NeoForge.jar` | 875c52c6 provider entries; a97ac77c startup delegates. | RESOLVED: shared consumer event, registry and behavior APIs, no independent generated family. See Puzzles Lib membership closure. |
| `Quark-4.1-480.jar` | `quark-end-generators`, `quark-end-registration`, `quark-fallen-log-decor`, `quark-landmark-encounter-generators`, `quark-monster-box-behavior`, `quark-monster-box-bindings`, `quark-nether-spikes`, `quark-spire-config-annotations`, `quark-stone-clusters`, `quark-underground-base`, `quark-underground-context`, `quark-underground-fill`, `quark-underground-styles`, `quark-vegetation`, `quark-world-category` | RESOLVED: Existing five named nonregistry site candidates, terrain/vegetation and existing-structure replacement hooks; bundled Biolith adds biome/surface support. Full disposition below; canonical count and attributes remain open. |
| `TerraBlender-neoforge-1.21.1-4.1.0.8.jar` | Sources 3230f7ff and c2de78c1; test_terrablender_provider_scope.py | RESOLVED: Consumer biome regions, noise and surface rules; no independent family. See TerraBlender disposition below. |
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
| `accessories-neoforge-1.1.0-beta.53+1.21.1.jar` | accessories-provider and accessories-startup | RESOLVED: Existing-entity accessory equipment/data APIs, no independent family. Preserve inventory/loot/NBT effects below. |
| `adorabuild-structures-2.11.0-neoforge-1.21.3.jar` | `adorabuild-provider`, existing runtime/root and pool graph evidence | RESOLVED: 106 existing roots; all 110 pools and 121 templates connected; one preserved missing pool reference. See AdoraBuild provider disposition below. |
| `aether-1.21.1-1.5.10-neoforge.jar` | Existing Aether source captures, test_aether_provider_scope.py and focused candidate/component checks | RESOLVED: Three dungeon candidates, cloud terrain, conditional holiday-tree boundary, inactive portal components, common hooks and selected-library roles accounted for below. Canonical grouping and attributes remain open. |
| `aethersdelight-0.1.4.2-1.21.1.jar` | `aethers-delight-provider` (13d2013), test_aethers_delight_provider_scope.py | RESOLVED: Ore, plant and food/item content, including both packaged compatibility data packs. No independent structure family. Full disposition below. |
| `alternate_current-mc1.21-1.9.0.jar` | `alternate-current-provider` (4b722aa), test_small_utility_provider_scope.py | RESOLVED: Existing redstone-wire updates, configuration and profiling; no independent family. See redstone, configuration and loot provider dispositions below. |
| `amendments-1.21-2.0.15-neoforge.jar` | amendments-provider, startup, block-replacement and reused shared Moonlight plugin | RESOLVED: Existing block/gameplay support and cauldron replacements in existing structures, no independent family. |
| `architectury-13.0.8-neoforge.jar` | d943fcbb entry/hooks; 8ed7b7ec event/biome delegates; 4a879ad8 spawn synchronization. | RESOLVED: consumer event, extension and biome APIs, no independent generated family. See Architectury membership closure. |
| `attributefix-neoforge-1.21.1-21.1.3.jar` | `attributefix-provider` (69119c6), test_small_utility_provider_scope.py | RESOLVED: Existing attribute range configuration; no structure contribution. See small utility provider dispositions below. |
| `azurelibarmor-neo-1.21.1-3.1.2.jar` | Sources a37e5b08 and 57ea6b5c; test_small_utility_provider_scope.py | RESOLVED: Item animation identity, synchronization and rendering support; no independent family. See AzureLib Armor disposition below. |
| `bclib-21.0.24.jar` | Reused integration dispatch, generation entry, provider entry, post-init, common hooks and nested MixinExtras captures | RESOLVED: Shared consumer generation, block/item and lifecycle APIs. No independent family. Preserve seed/write-boundary effects described below. |
| `bettercombat-neoforge-2.3.2+1.21.1.jar` | aea34a1e entries; c6a937e0 resources; 60b953d3 team compatibility; reused Tiny Config. | RESOLVED: player combat and weapon attributes, no independent generated family. See Better Combat membership closure. |
| `bettervillage-neoforge-1.21.1-3.3.1.jar` | `bettervillage-code` | RESOLVED: see Better Village provider disposition below. |
| `bookshelf-neoforge-1.21.1-21.1.81.jar` | 3a315ed2 provider entries; 17cdf0d7 common initialization. | RESOLVED: utility codecs, commands and consumer gameplay/loot APIs, no independent generated family. See Bookshelf membership closure. |
| `bundle-api-neoforge-1.1.0.jar` | `bundle-api-provider` (a14b5e0), test_small_utility_provider_scope.py | RESOLVED: Custom bundle data components, item interaction and rendering; no independent family. See bundle and shield dispositions below. |
| `c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar` | 52 C2ME source captures; test_c2me_provider_scope.py | RESOLVED: existing generation, scheduling, persistence and view-distance modifications; no independent family. See final C2ME membership closure below. |
| `cc-tweaked-1.21.1-forge-1.119.0.jar` | cc-tweaked-provider, startup, registry-lifecycle and client-entries; focused provider test | RESOLVED: player computers, existing-block lifecycle and loot modifiers, no independent family. See CC:Tweaked membership closure below. |
| `chipped-neoforge-1.21.1-4.0.2.jar` | `chipped-provider`, `chipped-crafting`; complete payload binding. | RESOLVED: building blocks, recipes, player workbench crafting and block behavior. No independent structure family. |
| `cloth-config-15.0.140-neoforge.jar` | `cloth-config-provider` (6e7567c7), complete payload/source binding. | RESOLVED: config-screen API; sole automatic initialization is client-guarded. No independent family. |
| `coffee_delight-1.4.1.jar` | `coffee-delight-provider` (49445ab), test_coffee_delight_provider_scope.py | RESOLVED: Vanilla coffee-bush patch and food/item content, with no independent structure family. Full disposition below. |
| `collective-1.21.1-8.25.jar` | `collective-provider`, `collective-services`, `collective-init`, existing `collective-mixin-plugin`; full payload/source binding. | RESOLVED: shared data, consumer entity/callback/network APIs and platform services. No independent family. |
| `comforts-neoforge-9.0.5+1.21.1.jar` | comforts-provider and comforts-spectrelib; focused provider test | RESOLVED: player sleeping equipment, sleep events and config support, no independent family. See Comforts membership closure below. |
| `create-1.21.1-6.0.10.jar` | Create captures and test_create_provider_scope.py; final disposition below. | RESOLVED: Ore generation, player construction, machine behavior, GameTest fixtures and client Ponder scenes. All three embedded libraries accounted for. No independent natural structure family. |
| `create-enchantment-industry-2.4.0.jar` | cei-entries, hooks, registrations and world-interaction; focused provider test | RESOLVED: player machines, experience processing, existing-block lightning transformation and client tutorials, no independent family. See Enchantment Industry membership closure below. |
| `createbigcannons-5.11.6+mc.1.21.1.jar` | Seven cbc source increments and test_cbc_provider_scope.py | RESOLVED: player-built cannon equipment, contraption assembly, projectile effects and tutorials, no independent family. See Big Cannons membership closure below. |
| `createdieselgenerators-1.21.1-1.3.15.jar` | diesel-provider, registrations, commands and oil-data; reused Sable Companion | RESOLVED: player machines, virtual oil resources, fuel effects and tutorials, no independent family. See Diesel Generators membership closure below. |
| `creatingspace-1.21.1-1.7.18.jar` | Existing root decisions, creating-space-provider, creating-space-arrival, creating-space-common-delegates and test_creating_space_provider_scope.py | RESOLVED: Four existing roots, five connected pools, six templates partitioned, terrain and common-hook roles accounted for. Disconnected outpost retained below. Canonical grouping and attributes remain separate. |
| `cristellib-neoforge-1.21.1-3.1.7.jar` | `cristellib-provider`, `cristellib-writers`, `cristellib-set-writers`, `cristellib-conditions`, `cristellib-builtin`; full payload/source binding. | RESOLVED: consumer pack loading and existing structure-set configuration. No independent family; Waystones replacement condition fails in the frozen runtime. |
| `cupboard-1.21-3.7.jar` | `cupboard-provider` (77dd750), test_small_utility_provider_scope.py | RESOLVED: Shared configuration, lookups, diagnostics and existing-entity handling; no independent family. Frozen error-suppression setting and limitations below. |
| `curios-neoforge-9.5.1+1.21.1.jar` | curios-provider, curios-delegates and focused source binding | RESOLVED: equipment slot data, existing-entity inventory and consumer item behavior, no independent family. See Curios membership closure below. |
| `deep_aether-1.21.1-1.1.5.1.jar` | `deep-aether-totem-scope`, `deep-aether-provider`, `deep-aether-aeroblender`, `deep-aether-biome-setup`; focused candidate and provider checks | RESOLVED: Four roots, fifteen templates, custom feature candidates, common hooks, optional packs and active AeroBlender accounted for. Preserve inactive Sacred Lands and fallen-tree grouping boundaries. See final Deep Aether disposition below. |
| `dummmmmmy-1.21-2.0.12-neoforge.jar` | Source 51ba791c; test_small_utility_provider_scope.py | RESOLVED: Item/dispenser-placed target dummy and existing-entity interaction hooks. No independent family. See target dummy disposition below. |
| `emi_loot-0.7.9+1.21+neoforge.jar` | ebf5a286 entry paths; a2f485ef parser and accessors. | RESOLVED: existing-loot inspection and client display synchronization, no independent generated family. See EMI Loot membership closure. |
| `emi_ores-1.2+1.21.1+neoforge.jar` | Source 824f34de; test_small_utility_provider_scope.py | RESOLVED: Reads and sends existing ore/geode generation information; no independent family. See EMI Ores disposition below. |
| `ends_delight-2.6+neoforge.1.21.1.jar` | `ends-delight-provider` (311c1fe), test_ends_delight_provider_scope.py | RESOLVED: Chorus succulent vegetation, food/loot and existing knife-attack behavior. No independent structure family. Full disposition below. |
| `explorations-neoforge-1.21.1-1.6.2.jar` | `explorations-provider` (0e6f5e4), prior scarecrow/slime/deepslate captures, test_explorations_provider_scope.py | RESOLVED: Ten existing roots, one scarecrow design, named decorated-mushroom candidate and four statue components in village houses pools. Missing and unused components preserved below. |
| `fastasyncworldsave-1.21-2.6.jar` | `fastasyncworldsave-provider` (7a82503), test_small_utility_provider_scope.py | RESOLVED: Saved-data and level-data write processing; no authored structure contribution. See save and structure utility dispositions below. |
| `forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar` | All 43 nested modules, preserved sources and test_fabric_provider_scope.py | RESOLVED: Consumer APIs, biome modifiers, conventional tags and test-only template; all module contribution roles resolved below. No independent family. |
| `fzzy_config-0.7.6+1.21+neoforge.jar` | `fzzy-provider`, `fzzy-delegates`, `fzzy-registrations` | RESOLVED: configuration and consumer registration API; no independent family. See Fzzy Config closure below. |
| `geckolib-neoforge-1.21.1-4.8.4.jar` | Sources 1284a76a and 58568f7f; test_small_utility_provider_scope.py | RESOLVED: Animation data, item identity, rendering and synchronization support; no independent family. See GeckoLib disposition below. |
| `idas-1.13.7+1.21.1-neoforge.jar` | `idas-provider` (afb3cee), prior suppression evidence, test_idas_provider_scope.py | RESOLVED: 84 existing roots, complete component partition, compatibility pool declarations and Labyrinth encounter hooks. See IDAS disposition below; shared Integrated API and final attributes remain open. |
| `integrated_api-1.7.3+1.21.1-neoforge.jar` | Existing pool-codecs and source 88a0f54; test_integrated_api_provider_scope.py | RESOLVED: Shared generation codecs, existing structure modifiers, tags and consumer data loaders. No independent family. See Integrated API disposition below. |
| `integrated_stronghold-1.1.4+1.21.1-neoforge.jar` | `integrated-stronghold-provider`, existing root/graph and family-decision regression | RESOLVED: one existing root, both modification mixins, all components and disconnected/missing templates accounted for. See Integrated Stronghold provider disposition below. |
| `integrated_villages-1.3.3+1.21.1-neoforge.jar` | `integrated-villages-provider` (97000f2), prior suppression evidence, test_integrated_villages_provider_scope.py | RESOLVED: Twelve existing roots, full component partition, four incompatible legacy addition declarations and existing village suppression. See Integrated Villages disposition below. Shared Integrated API remains open. |
| `kotlinforforge-5.11.0-all.jar` | `kff-language`, `kff-mod` | RESOLVED: language loading and consumer APIs; no independent family. See Kotlin for Forge closure below. |
| `letmedespawn-1.21.x-neoforge-1.5.0.jar` | `letmedespawn-provider` (69119c6), test_small_utility_provider_scope.py | RESOLVED: Existing mob persistence/discard behavior; no independent family. See small utility provider dispositions below. |
| `libraryferret-neoforge-1.21.1-4.0.0.jar` | `libraryferret-provider` (8c60e03), test_small_utility_provider_scope.py | RESOLVED: Abstract consumer-supplied jigsaw/placement support and coin content. No independent family. See additional shared provider dispositions below. |
| `lithostitched-1.7.10+beta4-neoforge-21.1.jar` | Existing pool/alias/modifier sources; provider entry 4fbbe70 and remaining hooks 37c3259; test_lithostitched_provider_scope.py | RESOLVED: Shared generation codecs, terrain/biome changes and existing vanilla template/processor/alias components. No independent family. See Lithostitched provider disposition below. |
| `lootintegrations-1.21.1-4.7.jar` | `lootintegrations-provider` (47047d6), test_small_utility_provider_scope.py | RESOLVED: Core integration loader and loot-list modifier, 43 definitions and seven chest-table targets. No independent family; remains a required loot-attribute input. See disposition below. |
| `mca-neoforge-7.7.11+1.21.1.jar` | Sources 28273db and bd25ce8; test_mca_provider_scope.py | RESOLVED: Existing-village recognition, villager replacement, entity/interaction behavior and structure location. No independent family. See MCA disposition below. |
| `moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar` | Eight capture directories bound by test_moog_library_provider_scope.py; latest registration boundaries ee8e2c0. | RESOLVED: shared generation and modification library; no independent authored family or packaged generation resources. See Moog library provider disposition below. |
| `moonlight-neoforge-1.21.1-3.0.17.jar` | Six Moonlight source increments and reused supplementaries-shared-plugin | RESOLVED: consumer APIs and existing-structure spawn-box components; no independent family. See Moonlight closure below. |
| `naturalist-1.0.2-neoforge-1.21.1.jar` | `naturalist-provider` (9682cb0), test_naturalist_provider_scope.py | RESOLVED: Mob spawning, existing entity/item/crop behavior and client spawn-egg resources. No independent structure family. Full disposition below. |
| `oceansdelight-neoforge-1.0.4-1.21.1.jar` | `oceansdelight-provider` (2b575d8), test_oceansdelight_provider_scope.py | RESOLVED: Food content and four existing aquatic-mob loot declarations; no independent family. See Ocean's Delight disposition below. |
| `owo-lib-neoforge-0.12.15.5-beta.1+1.21.jar` | owo-entries, owo-common-hooks, owo-delegates and byte-identical Fabric base classes | RESOLVED: consumer APIs and ore placement behavior; no independent family. See owo-lib closure below. |
| `player-animation-lib-forge-2.0.4+1.21.1.jar` | Source d1d22f75; test_small_utility_provider_scope.py | RESOLVED: Client-only animation entry and client mixins; no independent family. See Player Animator disposition below. |
| `polymorph-neoforge-1.1.0+1.21.1.jar` | 0b9f0152 entries; 562005f3 startup; 48f73c41 events; e4e27ae2 ticker. | RESOLVED: existing-container recipe selection and recipe data, no independent generated family. See Polymorph membership closure. |
| `prickle-neoforge-1.21.1-21.1.11.jar` | Sources eb9670dc and 4e7468fb; test_config_library_provider_scope.py | RESOLVED: Configuration adapters, platform lookup and initialization; no independent family. See configuration library disposition below. |
| `quickrightclick-1.21.1-1.9.jar` | `quick-right-click-provider`, `quick-right-click-placement`, `collective-mixin-plugin`; full payload/source binding. | RESOLVED: player-operated tables/storage and temporary beds/shulkers. No independent family. |
| `railways-0.2.1+neoforge-mc1.21.1.jar` | Provider entry eaa7a6b, player assembly 0e7edb0, common hooks d17d854; test_railways_provider_scope.py | RESOLVED: Construction, player vehicles, existing-block/entity behavior, data migration and visual/network support. No independent structure family. See final Railways disposition below. |
| `ranged_weapon_api-neoforge-2.3.3+1.21.1.jar` | `ranged-weapon-provider` (ac503af9), full payload/source binding. | RESOLVED: ranged combat attributes, effects, item use and projectile mechanics. No independent family. |
| `regions-unexplored-0.6.1-neoforge-21.1.jar` | Existing feature, component and entry captures; tree source 0f263ed, root/condition source f4ad223; focused candidate/provider tests | RESOLVED: Fallen-log candidate, Ashen trial-chamber component, terrain/vegetation, full payload and common-entry roles accounted for. Fallen-log canonical boundary remains open. See final RU disposition below. |
| `repurposed_structures-7.5.21+1.21.1-neoforge.jar` | Existing mansion/monument/pool evidence, `repurposed-provider`, `repurposed-feature-roles`, `repurposed-assembly`, `repurposed-datagen-entry`; focused provider and component checks. | RESOLVED: 107 existing roots, 23 dungeon/well configuration candidates, all feature and component roles, common hooks and data-generation entry accounted for below. Canonical grouping and effective eligibility remain separate. |
| `resourcefulconfig-neoforge-1.21-3.0.11.jar` | Sources b335f9e8; test_config_library_provider_scope.py | RESOLVED: Configuration parsing, interface initialization and server settings accessors; no independent family. See configuration library disposition below. |
| `resourcefullib-neoforge-1.21-3.0.12.jar` | resourcefullib-provider, startup and storage; focused provider test | RESOLVED: consumer fluid, registry and networking APIs plus application storage, no independent family. See Resourceful Lib membership closure below. |
| `ritchiesprojectilelib-2.1.2+mc.1.21.1-neoforge.jar` | `projectile-library-provider` (50bc747), test_small_utility_provider_scope.py | RESOLVED: Projectile entity, chunk-loading and synchronization support; no authored structure family. Packaged mixin files lack loader declarations. See disposition below. |
| `servercore-neoforge-1.5.17+1.21.1.jar` | Five ServerCore source increments | RESOLVED: existing-server ticking, spawning and lookup changes; no independent family. See ServerCore closure below. |
| `shield_api-neoforge-2.2.0.jar` | `shield-api-provider` (a14b5e0), test_small_utility_provider_scope.py | RESOLVED: Custom shield interaction, item attributes, rendering and EMI integration; no independent family. See bundle and shield dispositions below. |
| `simplyswords-neoforge-1.63.0-1.21.1.jar` | Three Simply Swords source increments | RESOLVED: weapons, item powers and loot modification; no independent family. See Simply Swords closure below. |
| `sparsestructures-neoforge-1.21.1-3.0.jar` | `sparsestructures-provider` (69119c6), test_small_utility_provider_scope.py | RESOLVED: Existing structure-set placement modification; no independent family. See small utility provider dispositions below. |
| `structure_layout_optimizer-neoforge-1.0.12.jar` | `structure-layout-optimizer-provider` (8c60e03), test_small_utility_provider_scope.py | RESOLVED: Existing jigsaw assembly and template filtering modifications. No independent family. See additional shared provider dispositions below. |
| `structure_pool_api-neoforge-1.2.1+1.21.1.jar` | `structure-pool-api-provider` (69119c6), test_small_utility_provider_scope.py | RESOLVED: Caller-supplied pool injection and piece limits; no independent family. See small utility provider dispositions below. |
| `structureessentials-1.21.1-5.0.jar` | `structureessentials-provider` (7a82503), test_small_utility_provider_scope.py | RESOLVED: Existing structure lookup, placement, biome compatibility and diagnostic modifications; no independent family. Frozen activation settings bound below. |
| `supplementaries-neoforge-1.21.1-3.6.8.jar` | Existing generation, data, common-entry and integration captures; final server hooks 46127c7 and map delegate 3660300; test_supplementaries_provider_scope.py | RESOLVED: Galleon and road-sign roots, cave-urn cache candidate, all pools/templates, component injections, full payload and executable contribution roles accounted for below. Cave-urn canonical boundary and effective family attributes remain separate. |
| `tectonic-3.0.22-neoforge-21.1.jar` | `tectonic-provider`, `tectonic-config-selection` (fba027c), test_tectonic_provider_scope.py | RESOLVED: Terrain, placement modifications and the named underground-river lantern candidate. No packaged structure roots, pools or templates. See Tectonic disposition below. |
| `ubesdelight-neoforge-1.21.1-0.4.13.jar` | `ubes-delight-provider` (b6ef5a0), MidnightLib ca67c60, config delegates e40ea32; test_ubes_delight_provider_scope.py | RESOLVED: Four crop chains, food/item interactions and bundled configuration support. No independent structure family. Full disposition below. |
| `worldweaver-21.0.24.jar` | Six wover provider captures, existing pool-codecs and biome modifier captures | RESOLVED: Shared consumer generation/registry/terrain APIs and presets, no independent family. Preserve terrain and pack-loading effects below. |
| `wunderlib-21.0.10.jar` | Source 185b55c; test_small_utility_provider_scope.py | RESOLVED: Networking entries and supplied-coordinate geometry; no independent family. See WunderLib disposition below. |
| `youre-in-grave-danger-neoforge-2.0.13.jar` | Three grave provider source increments | RESOLVED: player death, grave storage and recovery; no independent family. See grave provider closure below. |

## Final Regions Unexplored provider disposition

Regions Unexplored membership is RESOLVED. Retain the named stump-and-fallen-log
candidate and its six variants, with the documented stump-only outcome. Retain
Ashen as an encounter component of the existing vanilla trial-chamber family.
The provider adds no runtime structure root. The other inspected feature,
terrain, plant, tree, root and decoration implementations introduce no further
named authored-site candidate. Canonical treatment of the fallen-log candidate
remains an explicit grouping decision, not an invented final family count.

The common initializer registers biome/content types, the already-accounted
feature and tree components, configuration predicates, surface rules and
Lithostitched integration. The NeoForge constructor attaches common/client
setup, sign block-entity compatibility, entity spawn-placement/attribute
registration and registry aliases. After registry freeze, setup concerns block
tool interactions and flammability. The separate client entries register client
presentation and particles. These callbacks do not supply an unexplained
independent site writer.

All nine common mixins have contribution roles:

| Hook | Role |
| --- | --- |
| BiomeMixin | Configured tundra snow handling. |
| CropPlacerMixin | Crop support on the supplied soil blocks. |
| EatBlockGoalMixin | Existing mob grass-eating behavior on RU vegetation/soil. |
| NetherrackBlockMixin | Bonemeal conversion of existing Nether substrate. |
| TrunkPlacerDirtMixin | Peat, silt and alpha-grass handling below trees. |
| VillagerProfessionAccessor | Existing profession secondary-POI block set. |
| WorldCarverMixin | Grass/dirt tests include RU soil during existing carving. |
| removals/BiomeListMixin | Removes disabled biomes from the client buffet list. |
| removals/HolderLookupMixin | Filters disabled biomes from registry lookup listing. |

The NeoForge-specific mixin file is empty. Its absence of extra hooks and the
full archive/META-INF/JSON5 accounting are bound by the provider checks.

The initializer audit exposed a root-placer gap outside the earlier three tree
component directories. Source f4ad223, extractor fbe9cc4, closes it with Magnolia
root placement, both processor conditions and five type-registration classes.
Manifest SHA-256:
2ab92b26ac69369210999d31c70f384201f0a8f6cc9a384b0e15831c2df2ae06.
The independent capture matches. Magnolia writes the supplied root state around
an existing tree trunk, following eligible positions downward. The previously
captured Willow root placer is reused. Both are tree components. ConfigCondition
tests a configured key; MatchingBiomesCondition tests the generator's biome at
the processor position. Neither creates a root, template or authored layout.
The state-provider, load-predicate and surface-rule registrations point to the
already-captured ground-cover, configuration-predicate and configuration-rule
implementations. No new implementation family follows from these registrations.

The focused provider test now accounts for all 23 packaged trunk, foliage,
decorator and root classes using new and reused hash-bound source. This corrects
the narrower 21-class tree-directory boundary rather than hiding the gap.
Together with candidate tests, the full 8077-file payload, overlays, common
entries, 53 feature implementations, modifier/surface consumers, Ashen component
and fallen-log variants have supported membership dispositions.

```sh
uv run pytest -q tests/item8/test_regions_unexplored_provider_scope.py tests/item8/test_regions_unexplored_candidates.py
uv run ruff check tests/item8/test_regions_unexplored_provider_scope.py tests/item8/test_regions_unexplored_candidates.py
uv run basedpyright tests/item8/test_regions_unexplored_provider_scope.py tests/item8/test_regions_unexplored_candidates.py
```

Five cases pass (1.07s), with scoped Ruff and Basedpyright passing. No runtime
experiment or new measurement system was added. Census: 89 resolved providers,
47 open. Item 8 canonical grouping, attributes and final review/delivery remain
open. Do not restart the older RU checkpoints below.

## Final Railways provider disposition

Railways membership is RESOLVED with no independent structure family. The
packaged vehicle, optional recipe pack and three visual resource packs are
accounted for in the checkpoint below. Source d17d854 completes the remaining
105 common hooks; together with StructureMixin, all 106 declared common entries
are bound to the actual JAR and retained disassembly. The 68 separately declared
client entries are distinguished from that set. Both mixin plugin bodies are
retained in eaa7a6b. Source and exact reproduction commands are under sources/.

The inspected targets, injected methods and bodies establish these roles:

- Accessors expose existing contraption, carriage, block-entity, inventory,
  navigation, track, train, camera and rendering state. Static accessor stubs
  do not create sites. Fields added to edge data, bogeys and flywheels likewise
  extend existing object state.
- Train, carriage, navigation, schedule, signal, station, track-edge, observer
  and travelling-point hooks change existing vehicle routing, coupling, fuel,
  controls, serialization and display. Station assembly and relocation act on
  existing train graphs. Minecart hooks construct the custom minecart type;
  they do not place authored world locations.
- Track placement and block-use hooks alter player construction, crossing
  selection, casing, collision shapes, bogey styles and item drops. Roller
  paving is invoked from an operating contraption's movement context. Wrench
  hooks disassemble an existing train/station and drop its schedule. Deployer
  activation permits handcar item use. These are construction interactions,
  not independent world-generation entry points.
- Door, sliding-door and pathfinder hooks alter existing door interaction;
  explosion/fireball hooks alter damage to tracks. Containers, toolboxes,
  mounted storage, fluid networks, seats and conductor interaction hooks
  alter existing inventories, blocks and entities.
- ChunkSerializer, IOWorker, player-save and StructureTemplate-save hooks add
  data-version metadata. DataFixTypes, NbtUtils, schematic, track-material and
  saved-railway hooks migrate or clean existing data. None introduces a new
  authored layout or structure root.
- Conductor possession changes camera, movement, player tracking and packet
  broadcast behavior. Voice-chat compatibility changes the speaking/listening
  position and identity. Key registration, configuration UI, nixie displays,
  boiler client initialization and renderer access are support roles. The
  custom-payload hook dispatches the existing Railways packet set.

The loader and ModSetup dispatch register construction content and supporting
capabilities, with the actual common event wrappers retained and inspected.
The two mixin plugins select declared compatibility hooks; their ASM operations
extend rolling modes and container access. No additional mixin list or packaged
code-loading mechanism supplies an unexplained structure route. Full archive
accounting includes META-INF, the access widener and optional packs. Further
train gameplay or security acceptance belongs to its applicable later gate;
it is unnecessary to determine whether these contributions create a family.

The existing three focused cases now also require every declared common hook
and both plugin classes to be covered by hash-bound source. They pass (0.29s),
with scoped Ruff and Basedpyright passing. No new runtime experiment, schema or
measurement system was added. Census: 88 resolved providers, 48 open. Canonical
family grouping and Item 8's eleven attributes remain unfinished.

## Railways membership checkpoint

Resource-pack follow-up: the three optional packs are legacy_palettes (493
files), green_signals (six) and legacy_semaphore (three). The complete partition
is 495 textures, one model, three pack icons and three metadata files. META-INF
contains only the manifest and NeoForge mod metadata; architectury.common.json
names the packaged access widener. The focused resource-pack case passes; all
three current Railways cases pass (1.50s), with scoped Ruff/Basedpyright passing.
The common-hook reconciliation remains open. Census unchanged: 87 resolved,
49 open. This uses the existing test path and adds no measurement system.

Railways remains OPEN. Archive railways-0.2.1+neoforge-mc1.21.1.jar has SHA-256
b7636c8b1b0352ed1a130dfe67f8bb574e2fc08803ed1cda4d3ea00505193914.
Source eaa7a6b (extractor 60016db) retains thirteen classes: all eight annotated
entries, the common initializer/event delegate, both mixin plugins and the
StructureTemplate save hook. Source 0e7edb0 (extractor cf398e3) adds ModSetup
and HandcarItem. Both captures reproduced exactly, with commands alongside them.

The focused check accounts for all 14066 payload files, including 2735 root data
files. The data partition is recipes (1071), advancements (660), loot tables
(615), tags (387), one liquid-fuel definition and one legacy structures template.
The optional phantom-track data pack contains exactly three sequenced-assembly
recipes plus metadata. This packaged content does not add a generated site.

The sole root template is data/railways/structures/handcar/assembly.nbt. It is a
3 by 3 by 3 handcar assembly, with air, seat and handcar palette entries, no
entities, and a single bogey block-entity payload. Preserve its legacy plural
structures path and DataVersion 3120. It is not an adventure family. Do not
claim that HandcarItem consumes this resource: the inspected makeTrain method
assembles the vehicle directly through temporary block placement/restoration
and CarriageContraption assembly, called through player item interaction.
StructureMixin adds Railways data-version metadata to an existing template save;
it does not generate an independent root.

The common event delegate handles redstone-link instruction ticks, joining-player
version notification and tag-cycle updates. Its NeoForge wrapper also registers
fluid/item capabilities, stops conductor viewing on game-mode change and installs
the liquid-fuel reload listener. ModSetup dispatches construction, train, item,
entity, sound, recipe, portal-track and compatibility registrations. The common
mixin plugin supplies no extra mixin list and delegates conditional selection.
The NeoForge plugin additionally patches rolling-mode enums and container-level
access. These observations narrow the scope; final entry/delegate and mixin role
reconciliation remains necessary before provider closure.

The two declared mixin files contain 106 common entries (97 plus nine), with
68 separately declared client entries. StructureMixin is inspected; the other
105 common entries still need supported role dispositions, reusing any available
consumer evidence. Inspect actual targets and callbacks. Follow a helper only
for a concrete unresolved independent-site boundary, not general train gameplay.
Also finish the resource-pack/META-INF role check and bind the resulting provider
disposition. Do not recapture the fifteen classes already retained.

```sh
uv run pytest -q tests/item8/test_railways_provider_scope.py
uv run ruff check tests/item8/test_railways_provider_scope.py
uv run basedpyright tests/item8/test_railways_provider_scope.py
```

Two focused tests pass (0.22s). Scoped Ruff and Basedpyright pass after an explicit
string type annotation for palette names. These checks establish the packaged
vehicle boundary and bind existing source, not complete provider coverage.
Census remains 87 resolved providers, 49 open.

## Lithostitched provider disposition

lithostitched-1.7.10+beta4-neoforge-21.1.jar is RESOLVED as shared generation
support and modification of existing components, with no independent family.
Archive SHA-256: d367ea1885486755dd8a162b8bb28404a35155e9fd34eba03108991363b6c70a.
The complete 445-file payload contains 339 classes, 77 data JSON files, twenty
conditional shipwreck NBT overlays, three META-INF files and six root files.
There are no nested archives. The root idea.json describes a density-function
wrapper outside the data resource tree; it supplies no independent site.

Source 4fbbe70 covers the sole annotated NeoForge entry, utility class and
registry dispatch. Source 37c3259 adds the remaining 51 common/server mixins
and the direct configuration and built-in registry delegates. Four earlier
mixin captures complete all 55 declared common/server hooks. The focused test
binds thirteen existing source manifests, archive class bytes and disassemblies;
it reuses the prior pool, alias, biome, modifier, processor and lifecycle work.
The built-in registrations expose consumer-supplied codecs and dynamic
registries. Registering a dungeon, well or jigsaw type does not instantiate an
independent family. Existing consumer-provider dispositions account for those
supplied definitions; unused generic codec implementations are not extra sites.

Inspected hooks expose registry/biome fields, apply supplied biome/terrain/noise
modifiers, filter resource loading predicates, assemble an existing jigsaw root,
and select supplied processors or templates for existing vanilla pieces. Mansion
floor selectors and the registry-aware mansion piece placer operate inside the
existing mansion root. Villager tags select villager appearance. Configuration
loading and platform lifecycle hooks register or load this behavior, without an
independent root writer. Client integrated-server lifecycle remains distinct
from the dedicated-server hook set.

All 26 template lists resolve to 97 distinct templates in the exact pinned
Minecraft inner server archive: fourteen nether fossils, thirteen ruined-portal
pieces, twenty shipwreck pieces and fifty mansion rooms. These are components
of four existing vanilla designs, not 97 families. The twenty overlay paths
match the complete shipwreck selection exactly. NeoForge overlay selection is
conditional on lithostitched:breaks_seed_parity; component membership does not
assert that the overlay is enabled or that its bytes match vanilla templates.

The two packaged modifiers compile raw templates and replace aliases for
minecraft:trial_chambers. All four referenced trial-spawner tags resolve to
existing vanilla pools. The sole packaged pool replaces the existing trial
chamber entrance cap, retaining its vanilla template and copper-bulb processor.
The 23 processor lists contain fourteen empty extension points, eight shipwreck
block-palette substitutions and one per-piece random palette-list selection.
These alter existing pieces. The remaining data consists of five density
functions, three noise configurations, three biome regions, one noise definition
and thirteen tags (seven villager types, one biome-source exclusion, one palette
list and four trial-spawner pool lists). These define terrain, eligibility or
component selection, without an independent authored site.

```sh
uv run pytest -q tests/item8/test_lithostitched_provider_scope.py
uv run ruff check tests/item8/test_lithostitched_provider_scope.py
uv run basedpyright tests/item8/test_lithostitched_provider_scope.py
```

Three focused cases pass (0.31s), with scoped Ruff and Basedpyright passing.
The initial test used the wrong template-list namespace and included a processor
tag as a processor list; exact packaged paths corrected both selectors. A
subsequent test-edit syntax error was corrected before acceptance. No raw source
or packaged evidence was changed. Census: 87 resolved providers, 49 open. Final
canonical grouping and the eleven family attributes remain unfinished.

## Naturalist provider disposition

naturalist-1.0.2-neoforge-1.21.1.jar is RESOLVED as a mob-spawn and existing
entity/item behavior provider, with no independent structure family. SHA-256:
04616a9f136c7a8fd6f9f75e83be80af33bc54924b3ca16b0f33d19273c25e95.
Its full 1347-file payload has 211 classes, 779 assets, 265 data files, 79
client resource-pack files, eight packaged generator-cache files, two metadata
files and three other root files. There are no templates, nested archives,
services, scripts or configured/placed feature definitions. The sole resource
pack contains 31 spawn-egg model JSON files, 47 textures and pack metadata.
Its registration explicitly selects client resources. The optional
LambDynamicLights initializer is declared as a client dependency/integration.

NaturalistBiomeModifiers registers add_animals with AddAnimalsBiomeModifier.
The implementation filters biome membership and appends MobSpawnSettings
SpawnerData through addSpawn. It does not place blocks or structures. The
complete biome-modifier data contains that one custom modifier and three
vanilla remove_spawns declarations: farm animals in savanna/swamp biomes and
pigs in forest biomes. The other neoforge-path document maps compostable items.
All other root data consists of tags, recipes, loot tables and advancements.
These can affect encounters/loot in existing families, but do not add a family.

The sole annotated entry is Naturalist. Its preserved constructor and callbacks
register content, configuration, entity attributes and spawn predicates,
brewing recipes, dispenser behavior, client renderers/resource packs and
development data generation. FinalizeSpawnEvent initializes dragonfly variants;
MobEffectEvent.Applicable modifies effect applicability. These operate on
existing entities/items. Seven declared common mixins are fully retained:

| Mixin | Membership role |
| --- | --- |
| BottleItemMixin | Player bottling of an existing dragonfly-owned effect cloud. |
| CreeperMixin | Existing creeper avoidance goals for lions and catfish. |
| CropBlockMixin | Existing crop ticking affected by nearby snails. |
| MapItemMixin | Existing map use while riding a giraffe. |
| MobMixin | Existing mob effects and configured Naturalist entity enablement. |
| MonsterMixin | Existing player-held teddy-bear check. |
| ZombieMixin | Existing zombie goals targeting animal eggs. |

The two other declared mixins are client-only. No mixin plugin is declared.
No authored-site route is introduced by these hooks. This disposition does
not audit every animal AI helper or claim gameplay compatibility, spawn
abundance, final encounter composition or effective configuration values.

Source 9682cb0 retains the ten inspected classes, with exact archive/class
identities and reproduction in sources/naturalist-provider/README.md. Existing
accepted packaged JSON supplies the data. No runtime measurement was added.

```sh
uv run pytest -q tests/item8/test_naturalist_provider_scope.py
uv run ruff check tests/item8/test_naturalist_provider_scope.py
uv run basedpyright tests/item8/test_naturalist_provider_scope.py
```

Two focused cases pass (0.13s). Scoped Ruff/Basedpyright pass after two line-length
corrections. Census: 86 resolved, 50 open. Five packaged-generation providers,
24 code-only and 21 unmatched rows remain. No canonical family is added.

## Ubes Delight provider disposition

ubesdelight-neoforge-1.21.1-0.4.13.jar is RESOLVED as a crop, food/item and
configuration provider, with no independent structure family. Archive SHA-256:
abbdf3927b17aef8a44a418c6f292e584a61d1fab4115d33a71c3d0a35b1e2b4.
The full 1336-file payload comprises 140 classes, 729 assets, 448 data files,
seven packaged generator-cache files, four META-INF files, three resource-pack
files and five other root files. Full payload accounting excludes templates,
extra nested libraries, scripts and services. Both packaged Ube mixin lists are
empty and declare no plugin. The only resource pack contains Presence Footsteps
block-sound mapping, metadata and an icon, with no server generation data.

The four configured crop patches (garlic, ginger, lemongrass and ube) all use
WildTertiaryCropFeature. The writer delegates floor/primary/secondary/tertiary
placements in randomized patches. The complete supplied state sets contain only
the corresponding wild crop, tall grass and respectively pink tulip, lily of
the valley, azure bluet or cornflower. Every inline writer is vanilla simple_block.
All four placed resources reference the corresponding configured ID; all four
biome modifiers reference those placed IDs at vegetal_decoration. The modifiers
allow jungle biomes and deny underground biomes. BiomeIsOverworldPlacementModifier
checks the biome tag, and AddFeaturesByFilterModifier appends supplied features
during the ADD phase. Neither generates a separate layout. There are no pools,
structure roots or disconnected templates to reconcile in this provider.

Source b6ef5a0 and configuration delegates e40ea32 establish these entry roles:

| Entry group | Membership role |
| --- | --- |
| UbesDelightImpl, UbesDelight, CommonSetupImpl, CommonSetup | Register content, configuration, common setup, dispenser interactions, composting and villager food/item sets. Client setup and built-in client pack registration are behind the client-side branch. |
| ClientSetupEventsImpl | Client block-entity renderers. |
| BakingMatBlockEntityImpl capability subscriber | Exposes the existing baking-mat inventory capability. |
| VillagerEventsImpl | Existing farmer and wandering-trader item trades. |
| Configuration, ConfigurationImpl | Forward/read annotated settings and initialize MidnightConfig. No generation callback. |
| EMIPluginImpl, ServerREIPluginImpl, UbesDelightWailaPlugin | Recipe/workstation display, recipe-display serialization and tooltip configuration/components. No independent site. |

All four annotated parent entry candidates are included in the captured set.
Other item/block recipes, loot changes and food mechanics remain relevant to
existing-family attributes where applicable. This membership disposition does
not expand into a full audit of those gameplay implementations.

The sole bundled archive is midnightlib-1.9.2+1.21.1-neoforge.jar, SHA-256
5dc6cc72e507c3fb5b5bac59e79da2aee74a9d1345dbc48e0ccecd608ac9286a.
Its complete 45-file payload has 24 classes, sixteen assets, three metadata
files, one client-only mixin configuration and an icon. There is no generation
data or further nested archive. All three annotated entries are retained in
ca67c60. They initialize configuration/client presentation and register config
screens and commands. Direct delegates in e40ea32 show that AutoCommand builds
commands to read/set configuration fields and write configuration; MidnightLibConfig
declares library UI options. Its sole declared mixin targets the client options
screen. These routes supply configuration support, not another family.

The accepted JSON catalog retains the data. Every captured class, including the
bundled classes, is hash-bound to its exact archive and preserved disassembly.
Each source directory records its extractor and exact reproduction command.
Two javap record-class outputs contain an emitted blank line at EOF. The raw
bytes were preserved and independently reproduced, rather than normalized to
satisfy git's blank-at-EOF warning. No runtime measurement was added.

```sh
uv run pytest -q tests/item8/test_ubes_delight_provider_scope.py
uv run ruff check tests/item8/test_ubes_delight_provider_scope.py
uv run basedpyright tests/item8/test_ubes_delight_provider_scope.py
```

Three focused cases pass (0.13s); scoped Ruff/Basedpyright pass after two
line-length corrections. Census: 85 resolved, 51 open. Six packaged-generation
providers, 24 code-only and 21 unmatched rows remain. No canonical family is
added by this disposition.

## Aethers Delight provider disposition

aethersdelight-0.1.4.2-1.21.1.jar is RESOLVED as an ore, vegetation and food/item
provider, with no independent structure family. Archive SHA-256:
11b07fce5c69682290106fc1c79fc447606791239a18965f71114f360e8a947e.
The complete 748-file payload comprises 58 classes, 294 assets, 362 root data
files, 23 compatibility-pack files, seven packaged generator-cache files and
four metadata/logo files. There are no templates, nested archives, services,
scripts or mixin declarations. Source 13d2013 retains all six annotated entries.
The focused source check binds the complete annotated set to that capture and
the exact archive. Only the main class references the NeoForge global bus.

The main entry registers content and configuration, adds its common setup
callback and registers itself on the global bus. Its common setup and
ServerStartingEvent methods log configuration/items and a startup message.
Config.onLoad reads the values used by that logging. The two client-only
subscribers log client setup and register a stove renderer. ADCreativeTabs
inserts existing item stacks into creative tabs. DataGenerators handles
GatherDataEvent for development data generation. None of these callbacks adds
an independent generation route.

The full root generation payload consists of five configured/placed/modifier
chains. Arkenium uses minecraft:ore, targets holystone and places arkenium ore.
Peppermint uses minecraft:random_patch. Wild ginger, leek and parsnip each use
minecraft:no_bonemeal_flower. All four plant configurations contain vanilla
simple_block with only the corresponding plant state. The placed resources
reference these exact configured IDs. The five neoforge:add_features modifiers
reference the placed IDs, using underground_ores for ore and vegetal_decoration
for plants. Plant placement uses Aether's improved_layer_placement along with
rarity and biome filtering; it supplies positions to the plant features, not
another authored layout. No unresolved template or root remains in this data.

Both packaged compatibility data packs are accounted for without assuming they
are enabled or compatible with the retained runtime:

| Pack | Complete payload | Membership disposition |
| --- | --- | --- |
| aether_redux_compat | Three recipes, four loot-modifier documents and pack metadata | Food/loot compatibility, no independent family. |
| ancient_aether_compat | Six recipes, three loot-modifier documents, one tag, three worldgen documents, one Forge biome modifier and pack metadata | Ore placement and food/item compatibility, no independent family. |

The Ancient Aether pack's wynd_arkenium_ore configured feature is a vanilla ore
definition. Both its placed definitions reference the base arkenium_ore
configured feature, not that wynd configuration. Preserve that disconnected
configured resource rather than inventing a consumer. The Forge-named biome
modifier references wynd_arkenium_ore_placed in wyndcap_peaks. These legacy paths
and references are recorded as packaged facts, not successful activation.
Whether selected or unselected, the supplied generation payload remains ore
content and introduces no site-family ambiguity.

Root non-generation data contains recipes, advancements, tags, loot tables and
modifiers, and one data map. These remain inputs to existing-family attribute
work where applicable. Membership acceptance does not claim measured ore/crop
density or a full audit of individual food/block mechanics. Packaged JSON is
retained in the existing accepted catalog; no runtime measurement was added.

```sh
uv run pytest -q tests/item8/test_aethers_delight_provider_scope.py
uv run ruff check tests/item8/test_aethers_delight_provider_scope.py
uv run basedpyright tests/item8/test_aethers_delight_provider_scope.py
```

Three focused cases pass (0.12s). Scoped Ruff/Basedpyright pass after three
line-length and two JSON typing corrections. Census: 84 resolved, 52 open. Seven packaged-generation
providers, 24 code-only rows and 21 unmatched rows remain. No canonical family
is added by this disposition.

## Ends Delight provider disposition

ends_delight-2.6+neoforge.1.21.1.jar is RESOLVED as a vegetation, food/loot
and existing-item behavior provider, with no independent structure family.
SHA-256: 65277056eb9ee9e1025633b83cb1b2568ec846dacd16507a35698244f4196881.
The full 373-file payload comprises 44 classes, 201 assets, 124 JSON data
files and four metadata/logo files. Full accounting excludes templates, nested
archives, services, scripts and mixins. The loader metadata has no additional
entry mechanisms. All three annotated entries and the complete worldgen class
set are covered by the preserved source and focused checks.

The main constructor registers blocks/items, block entities, a creative tab,
loot modifiers, common configuration and ModBiomeFeatures. The latter registers
exactly one feature, chorus_succulent, backed by ChorusSucculentFeature and
CountConfiguration. Its writer samples horizontal offsets around the supplied
origin, finds WORLD_SURFACE height and writes a chorus succulent plant state
where that state can survive. Plant cluster state varies from one to three.
This is vegetation, not an authored site or template assembly.

The complete generation data has one configured feature (count 20), one placed
feature referencing it and one neoforge:add_features modifier referencing that
placed feature. Placement uses rarity, square spread, WORLD_SURFACE and biome
filtering. The biome modifier selects minecraft:end_highlands at
vegetal_decoration. These are configuration values, not observed density or a
claim that all twenty placement attempts succeed.

The client-only subscriber registers an End stove renderer. The other automatic
subscriber handles LivingDamageEvent.Pre and changes damage when an existing
attacker holds the dragon-tooth knife against configured mob types. It does not
generate content. No class references the NeoForge global event bus. Remaining
data comprises recipes, loot tables/modifiers, tags, advancements and a damage
type. These can affect existing-family attributes; membership closure does not
claim a complete gameplay audit of food, teleportation or loot behavior.

Source 311c1fe retains the five inspected classes and its README records the
exact reproducible command. The accepted packaged JSON catalog retains the
data. No additional runtime measurement was required.

```sh
uv run pytest -q tests/item8/test_ends_delight_provider_scope.py
uv run ruff check tests/item8/test_ends_delight_provider_scope.py
uv run basedpyright tests/item8/test_ends_delight_provider_scope.py
```

Two focused cases pass (0.13s); scoped Ruff and Basedpyright pass. Census:
83 resolved, 53 open. Eight packaged-generation providers, 24 code-only rows
and 21 unmatched rows remain. No canonical family is added by this disposition.

## Coffee Delight provider disposition

coffee_delight-1.4.1.jar is RESOLVED as a vegetation and food/item provider,
with no independent structure family. SHA-256:
86ff8637d157a723f4d790e2478fa50f87a2e7b7c4b4ed6a64fb3d69a0219082.
The full 295-file payload comprises 30 classes, 167 assets, 90 data files,
three metadata/logo files and five packaged data-generator cache files.
There are no templates, nested JARs, service declarations, scripts, mixin
declarations or extra loader mechanisms. The only Mod entry registers blocks,
items, an item tab and block entities. The only automatic subscriber is
ModDataGenerator.gatherData, a development data-generation event. No class
references the NeoForge global event bus. The preserved entry and all three
worldgen bootstrap classes are bound to the exact archive in the focused check.

The complete generation payload is one configured coffee_bush feature, one
placed coffee_bush feature and one add_coffee_bush biome modifier. The configured
feature is vanilla random_patch containing simple_block with the mature
coffee_delight:coffee_bush state, requiring air above sand. The placed feature
references that exact configured ID and applies rarity, square spread and a
heightmap. The neoforge:add_features modifier references that placed ID at
vegetal_decoration. Its minecraft:has_structure/desert_pyramid biome tag selects
biomes; it neither generates a pyramid nor modifies pyramid assembly.
The source bootstraps construct these same vanilla plant-placement mechanisms.

Remaining data is 23 recipes, 20 advancements and 44 loot tables. Membership
closure does not assert observed crop abundance, loot activation or final
family attributes. The accepted packaged JSON catalog retains this payload;
source 49445ab retains the five relevant classes, with exact reproduction in
sources/coffee-delight-provider/README.md. No runtime measurement is needed.

```sh
uv run pytest -q tests/item8/test_coffee_delight_provider_scope.py
uv run ruff check tests/item8/test_coffee_delight_provider_scope.py
uv run basedpyright tests/item8/test_coffee_delight_provider_scope.py
```

Two focused cases pass (0.10s). Scoped Ruff and Basedpyright pass after removing
an unused type-only import and correcting a long line. Census: 82 resolved,
54 open. Nine packaged-generation providers, 24 code-only rows and 21 unmatched
rows remain. No canonical family is added by this disposition.

## Farmers Delight provider disposition

FarmersDelight-1.21.1-1.3.2.jar is RESOLVED as an existing-village component,
vegetation and food/item provider. It adds no independent structure family.
Archive SHA-256:
8ff438d62e1fce61542945faae45975d823e04bd6e73a07a121ea05ce2f03de7.

The complete payload has 2220 files: 292 classes, 995 assets, 927 data files
and six metadata/logo files. There are no nested archives, service declarations
or additional scripts outside the three packaged CraftTweaker examples. The
full payload test binds the exact partition and all non-JSON data paths to the
frozen archive. Accepted packaged JSON and template catalogs above retain the
data; source 555d912, common setup 15cb251 and server packet 6678ec9 retain the
inspected executable contribution routes. All 19 annotated entry candidates,
all twelve common mixins and all seven common/world classes are captured and
bound by the focused check.

### Generation membership

VillageStructures registers a ServerAboutToStartEvent hook. Under
GENERATE_VILLAGE_COMPOST_HEAPS it appends a SinglePoolElement with rigid
projection and the empty processor list to each existing village house pool:

| Existing pool | Packaged component | Weight |
| --- | --- | ---: |
| minecraft:village/desert/houses | farmersdelight:village/houses/desert_compost_pile | 3 |
| minecraft:village/plains/houses | farmersdelight:village/houses/plains_compost_pile | 5 |
| minecraft:village/savanna/houses | farmersdelight:village/houses/savanna_compost_pile | 4 |
| minecraft:village/snowy/houses | farmersdelight:village/houses/snowy_compost_pile | 3 |
| minecraft:village/taiga/houses | farmersdelight:village/houses/taiga_compost_pile | 4 |

This accounts for every packaged template. Missing target pools are skipped by
the implementation. These are components of existing villages, not five new
families. Separately, GENERATE_VILLAGE_FARM_FD_CROPS appends crop replacement
rules to the five existing minecraft:farm_<biome> processor lists. Both branches
modify existing generation. This membership disposition does not assert frozen
activation, effective processor precedence or observed placement. The separate
Repurposed Structures compatibility add-on's thirteen templates and CTOV's
compatibility components keep their existing consumer links and are not recounted.

Ten configured features comprise eight wild_crop definitions, one wild_rice
definition and one vanilla random_patch for sandy shrubs. WildCropFeature places
the supplied floor, primary and secondary plant features in random patches.
The complete supplied block-state set contains only wild crops, mushroom
colonies, mushrooms, sandy shrubs, flowers/grasses and coarse dirt. WildRiceFeature
places a double rice plant in eligible water. Neither writes an authored site.
The nine placed resources each reference the corresponding configured feature;
all nine are consumed by the nine add_features_by_filter biome modifiers at
vegetal_decoration. BiomeTagFilter and the modifier apply biome/temperature
eligibility, not another layout. The standalone sandy-shrub configured resource
has no corresponding placed resource in this provider; sandy shrub also appears
inline in crop patches. It is vegetation in either representation.

### Other executable and data roles

| Entry group | Inspected contribution |
| --- | --- |
| FarmersDelight, CommonSetup, RegistryAliases | Registry/configuration setup, rotten-tomato dispenser behavior, villager food/item sets and basket-to-bamboo_basket block/item aliases. The village callback above is the structural contribution. |
| Three client event subscribers and two client mixins | Client setup, key handling, tooltips, sign editing and block-break display. Client-only registration is explicit. |
| Four block-entity capability subscribers | Inventory capability registration for basket, cabinet, cooking pot and cutting board. |
| CommonEvents, CommonModBusEvents, VillagerEvents | Soup consumption effects, stack/food component changes and villager/wandering-trader trades. |
| ToolCarvingEvent, DogFoodEvent, HorseFeedEvent, KnifeEvents, SkilletEvents, BackstabbingEvent | Existing block/item/entity interactions, animal feeding, cake slicing, attack sound and damage/knockback changes. No independent generation route. |
| ModNetworking and server payload delegate | Client particle payload and server-held skillet flip timestamp. The inspected server handler only updates an item component. |
| Three datafix mixins | Existing item/block-entity inventory and component migration. |
| Three rich-soil mixins and VillagersTargetRichSoilMixin | Preserve rich soil under tree growth/trampling and recognize farmland for existing villager behavior. |
| CampfireBaleMixin, CuttingBoardDispenserMixin, NourishmentAlwaysEatMixin, PlacePumpkinPieMixin, RopeFenceConnectionMixin | Smoke-source checks, adjacent cutting-board dispensing, eating permission, player pie placement and fence connectivity. |
| EnumParameters and enum extensions | Cooking recipe-book categories and skillet render pose. |
| DataGenerators | GatherDataEvent registrations for generated recipes, tags, models, loot, registry data and structure updating. This is a development data-generation entry, not another dedicated-server generation route. |

The three .zs examples add/remove cooking or cutting recipes and replace recipe
components. The seven Create projectile definitions describe food projectile
items and their projectile properties. Remaining data categories are recipes,
advancements, tags, loot tables/modifiers, item data maps, a damage type, an
enchantment and weapon attributes. These can affect existing-family attributes,
but do not introduce an independent family. Membership closure is not a full
gameplay audit of these item mechanics or a claim that optional CraftTweaker
scripts execute in the retained runtime.

```sh
uv run pytest -q tests/item8/test_farmers_delight_provider_scope.py
uv run ruff check tests/item8/test_farmers_delight_provider_scope.py
uv run basedpyright tests/item8/test_farmers_delight_provider_scope.py
```

Three cases pass (0.15s); scoped Ruff and Basedpyright pass. The initial test
incorrectly expected unqualified farm processor strings; preserved source uses
minecraft:farm_<biome>, and the assertion was corrected. Initial line-length and
set-typing findings were corrected. No raw source was changed and no additional
runtime measurement was run. Census: 81 resolved, 55 open. Ten packaged-generation
providers remain, followed by the existing 24 code-only and 21 unmatched rows.

## Creeper Overhaul provider disposition

CreeperOverhaul-neoforge-1.21.1-4.0.6.jar is RESOLVED as a mob, loot and
cosmetic provider, with no independent authored structure family. Archive
SHA-256: ed83bea2826667fca80a6a8067f89fe7b97eb8b3213bbcb7f0f4e6a6898c0bc9.
The complete 317-file payload comprises 83 classes, 185 client assets,
42 data files and seven metadata/refmap/access-widener/nested-library files.
There are no packaged structures, pools, templates, features or optional packs.
The existing JSON catalog retains the data; no new runtime measurement is needed.

All seventeen biome modifiers change mob spawn lists: sixteen neoforge:add_spawns
entries for the mod's creeper types and one neoforge:remove_spawns entry for
minecraft:creeper. Their entity IDs exactly match the sixteen entity loot tables.
The remaining data comprises two cactus block loot tables and seven biome/entity
tags. These are natural encounter and loot inputs for subsequent family
attributes, not sixteen new sites or proof that each spawn succeeds.

Source e8d3713 (extractor aa2c76b) captures thirteen actual entry/delegate classes,
manifest f44ec77d75bb58eed2f2475aa44575ca4f894ee557f6ee83549a6efee6844b7c.
Source d21ca8f (extractor 382fc1c) captures the player-login delegate, manifest
abb86e8bdaf55aa9fd570fe47f21f2e30f19c50780019b3a7d4f63ee521096ec.
Both independently reproduce exactly. Supported roles:

| Entry path | Contribution |
| --- | --- |
| CreepersForge and Creepers | The sole annotated loader initializes config, blocks, entities, items, creative tabs, sounds and networking. Its listeners register entity attributes/spawn predicates, flower-pot support and supplied inter-mod plugins. Shader/client-setup listeners have client event types; the additional client initializer is guarded by Dist.isClient. |
| ModEntities, ModSpawns and CreepersForge$1 | Sixteen entity types and entity spawn predicates. Predicates consult terrain, light, water, difficulty and the creeper's enablement supplier. They do not assemble a site. |
| ModBlocks | Tiny cactus and potted tiny cactus block registration. No natural feature registration is introduced by registering these blocks. |
| CreeperPlugin and PluginRegistry | Caller-supplied attack/avoidance predicates with duplicate-ID rejection. No generation callback or authored layout is supplied by this API. Other providers retain responsibility for their own implementations. |
| IronGolemMixin | Changes target acceptance for existing creeper entities. |
| PlayerListMixin and ServerCosmetics | Player-login cosmetic-visibility synchronization. The delegate stores flags and sends them to players; no world layout is written. |
| Events, PlatformUtilsImpl and generated PlatformMethods | Calendar-event selection, explosion interaction policy, item/tool checks, attribute lookup and the fixed NeoForge platform selector. No additional structure candidate. |

The only nested JAR is resourceful-cosmetics-4j-1.0.3.jar, SHA-256
ed67d9ccb8be7deb4771e08dd95be234bf63363b320531c4ed4d7531f8429b9e.
Its twelve files are ten cosmetics-library classes plus a plain manifest and
Architectury nesting identity. There is no service, mod entry, mixin declaration,
asset or data payload. All classes belong to its cosmetics API package and
contain no Minecraft, NeoForge or Fabric class references. The complete parent
reference check finds only client/cosmetics/service/CosmeticsApi as a consumer.
This supports a client cosmetics-library disposition without recursively
auditing HTTP internals. The actual server login callback was inspected above.

Three focused cases pass (0.11s), as do scoped Ruff and Basedpyright. Initial
lint findings were a redundant compound assertion and one overlong line; both
were corrected. The checks bind full payload accounting, all spawn-only data,
loader/common-mixin entries, all fourteen captured class identities and the
nested-library boundary. No runtime launch or frozen configuration change.
Census: 80 providers resolved, 56 open. Canonical-family counting and the eleven
attributes remain downstream of whole-stack membership.

```sh
uv run pytest -q tests/item8/test_creeper_overhaul_provider_scope.py
uv run ruff check tests/item8/test_creeper_overhaul_provider_scope.py
uv run basedpyright tests/item8/test_creeper_overhaul_provider_scope.py
```

## Supplementaries packaged component checkpoint

### Final provider membership disposition

Supplementaries provider coverage is RESOLVED. Reuse the two existing root
candidates, supplementaries:galleon and supplementaries:road_sign, and retain
the freestanding cave-urn cache as a named canonical-boundary candidate.
The road-sign configured feature is part of the root's generation chain, not
another family. Galleon urns are components of the ship; the same urn patch's
freestanding cave placement requires the separate cache-versus-decoration
decision. All twelve pools and eighteen templates already have these links.
Mineshaft elevator/rope and stronghold sconces modify existing families.
Barnacles, basalt ash and wild flax retain their natural-generation roles.

Source 46127c7 (extractor 2e97fb8) closes the remaining declared hook boundary:
69 server/common mixins plus the inherited Moonlight SimpleMixinPlugin. The
four previously captured mineshaft/stronghold hooks are reused. The existing
provider check now requires exact equality between all 73 declared common
mixins and the captured classes, rather than checking four names as a subset.
The retained disassemblies supply method bodies, injection targets and optional
annotations. Manifest hashes:

- supplementaries-server-hooks: eff83e4817ac4c20f7cf47c3b8beb8647257a27a28db5492825037df90a503d0.
- supplementaries-shared-plugin: 05fbc861b5d5a7e0290ac0bdcd10d29ae1afd2410c7833b97f5fd560a9640e75.
- supplementaries-map-lookup (3660300, extractor c989eb6): 3e28fdfcaf21c79d87ef0ad595aa145dea869903dd1692776fc9643bebdac3f2.

The remaining hooks have these contribution roles. Names below are relative
to the declared mixin package; the second configuration uses neoforge/.

| Hooks | Membership disposition from entry behavior |
| --- | --- |
| AbstractArrowMixin, AbstractSkeletonMixin, BowMixin, PlayerMixin, PlayerProjectileMixin, ProjectileWeaponItemMixin, ServerPlayerMixin, SkeletonMixin, StrayMixin | Quiver storage, ammunition selection/consumption, equipment at entity spawn, drops and synchronization. These affect existing entities and items, not site layouts. |
| AbstractHorseMixin, SkellyHorseMixin, ZombieHorseMixin | Feeding, taming, conversion and persistence of existing horses. Conversion preserves entity equipment/ownership; it is not structure generation. |
| CatSitOnBlockGoalMixin, GoalUtilsMixin, WanderingTraderMixin | Cat destination selection, boat path evaluation and trader door-opening goals. |
| RedMerchantSpawnerMixin | On a failed wandering-trader spawn, conditionally spawns a RedMerchantEntity near a player or existing meeting POI, with a despawn delay and wander restriction. It does not create that POI or a merchant site. Difficulty/season inputs are not measured occurrence rates. |
| CreeperMixin, compat/CompatCreeperArclightMixin, CelebrateVillagersSurvivedRaidMixin | Festive entity state, explosion wrapping, particles and raid-celebration events. Both optional Creeper alternatives have the same non-site role. |
| EvokerMixin, SlimeMixin, LivingEntityMixin, neoforge/LivingEntityMixin | Existing-entity state, slime effects, rope movement, lunch-basket consumption and fluid travel. |
| EntityAccessor, LivingEntityAccessor, PlayerAccessor, IDispenserAccessor, IHangingEntityAccessor, neoforge/FireBlockAccessor, neoforge/ItemStackAccessor | Access to passenger, item, loot, shoulder, dispenser, facing and fire operations. These accessor declarations add no generation route. |
| BlockSourceMixin, EntityMixin, FallingBlockEntityMixin | Dispenser source positioning, step sounds and falling-block fluid sampling. |
| ExplorationMapFunctionMixin, neoforge/TreasureMapForEmeraldsMixin | Consume structure destinations for loot/trade map items or Quark quills. The captured AdventurerMapsHandler uses existing holders or ADVENTURE_MAP_DESTINATIONS, requests a location, and creates/decorates an item. No independent layout is defined. The previously recorded null-returning Quark implementation prevents a claim of successful quill creation. |
| MapItemMixin, CartographyTableMixin, CartographyTableInputSlotMixin, InkSackMixin | Existing map height, color, lighting and antique-ink data; cartography inventory handling and sign interaction. |
| BannerPatternItemMixin, BrushItemMixin, ItemsMixin, LoomInputSlotMixin, LoomMenuMixin | Tooltip creation, player brushing, shulker-shell item substitution and flag crafting. |
| GrindstoneInputSlotMixin, GrindstoneMenuMixin, GrindstoneTestSlotMixin, ShulkerBoxBlockEntityMixin, ShulkerSlotMixin | Crafting result/experience and container insertion behavior. |
| CampfireBlockMixin, ComparatorBlockMixin, FireBlockMixin, IronBarsBlockMixin, LanternBlockPlacementMixin, ObserverBlockMixin | Existing block smoke, redstone updates, fluid ignition, connection states, rope support and moving-block observer behavior. Ignition and neighbor changes are not authored sites. |
| ExplosionMixin, ServerLevelMixin, neoforge/ChunkHolderMixin | Explosion visual callback, dispenser event redirection, lightning targeting and antique-ink capability synchronization. The deferred chunk callback sends existing block-entity state to players. |
| ServerGamePacketListenerMixin | Constructor-only class; no injected method body. |
| neoforge/self/SelfFlammableFluidBlockMixin, SelfLumiseneFluidMixin, SelfGunpowderMixin | Client block extensions, fluid-type access and ignition of existing gunpowder blocks. |
| neoforge/self/SelfFrameMixin, SelfPlanterMixin, SelfNetheriteDoorMixin, SelfSafeMixin | Held-block enchanting power, plant support and player destruction permission checks. |
| neoforge/self/SelfSlingshotMixin, SelfSoapItemMixin, SelfWrenchMixin | Item enchantment/action support and player-driven hanging-entity rotation. |

SimpleMixinPlugin reads OptionalMixin annotations and tests named class
availability. It returns no additional mixin list and performs no pre/post
application work. The captured optional conditions concern Arclight Creeper
compatibility and Domestication Innovation horse compatibility. Both the
included and excluded hook roles above add no independent family, so no new
class-presence experiment is needed to establish membership. This resolves the
plugin used by Supplementaries, not the separate full Moonlight provider row.

Previously captured common entries complete the non-mixin boundary: loader
initialization reaches the accounted worldgen registry, dynamic server data and
setup delegates. Other registries and reload inputs provide items, entities,
recipes, trades, maps, fluids, songs, hourglass data, captured mobs and player
interactions. Server events perform interactions, goals, item pickup, entity
damage, player ticks and note-block behavior. Lifecycle entries initialize
faucet/fake-level support, register placeable books, synchronize data and clear
caches. These do not add an unexplained authored-site candidate. Client-only
entry annotations, integrations, both bundled libraries and the complete
parent payload retain their earlier verified dispositions below.

This closes provider membership only. Canonical grouping, effective biome and
dimension eligibility, actual placement, map success and the eleven family
attributes must retain their existing uncertainty. No runtime or baseline
change was made. Census: 79 resolved providers, 57 open. Earlier open statements
below are superseded by this final disposition.

Validation: nine focused cases pass (2.97s); scoped Ruff and Basedpyright pass.
The initial statement-count lint finding was fixed by separating the existing
frozen-input assertions into their own test, without changing their coverage.

```sh
uv run pytest -q tests/item8/test_supplementaries_provider_scope.py 'tests/item8/test_family_decisions.py::test_provider_groups_bind_full_definitions_pools_and_registry[supplementaries-2]'
uv run ruff check tests/item8/test_supplementaries_provider_scope.py
uv run basedpyright tests/item8/test_supplementaries_provider_scope.py
```

Client entry disposition: source aff2fde, extracted by 5e58a1a, binds both
SupplementariesForgeClient and PicklePlayer to class-level EventBusSubscriber
annotations with value Dist.CLIENT. Their automatic registration is excluded
from the dedicated server. The existing provider source check binds both
classes and their disassemblies to the frozen archive. This resolves the
client-entry question below, without inspecting unrelated rendering behavior.
Remaining membership work is the server common/mixin entry roles, including
the inherited Moonlight mixin-plugin behavior. Packaged data, nested libraries,
integrations and the previously resolved generation paths must not be repeated.
Validation: all six Supplementaries provider cases pass (2.16s), with scoped
Ruff and Basedpyright clean. This source binding closes no additional provider;
the membership census remains 78 resolved and 58 open.

The complete parent payload is now partitioned by the existing provider test:
6,364 non-directory files comprise 1,179 classes, 3,577 assets, 1,589 data files
and nineteen other files. The latter are the exact metadata/license/icon files,
two already inspected embedded libraries and nine darker-rope texture-pack
files. No optional data pack is hidden in that resource-pack directory.
The test records every data category and fails on an unexplained category or
changed count, under the frozen whole-archive hash. The twenty-nine worldgen
files and eighteen templates reuse the already reconciled roots, sets, pools,
processor, configured features and placed features. Five biome modifiers were
already bound separately. This does not create another family denominator.

The less conventional data folders also have explicit roles: six placeable-book
definitions describe item placement; Trinkets entities/slots describe player
equipment slots; Moonlight files describe 109 soft fluids, 34 map markers and
21 trade-folder files. The parsed catalog contains twenty trade JSON files;
the remaining file is cartographer/example.json.disabled. Two other nonstandard
data files are flute_songs/midi_converter.py (interactive note conversion) and
flute_songs/revenge.json1 (song notes). The test binds the exact three-file
exception set. The converter was inspected, not executed or installed as a
server workflow. A strict-JSON exploratory read rejected a commented trade;
the already accepted commented-JSON catalog was reused, without changing parsers.

This closes packaged file accounting, not all executable roles. The annotation
candidate set is bound to SupplementariesForge, SupplementariesForgeClient and
PicklePlayer; the latter two still need their explicit client-side disposition.
Remaining common/mixin hooks must also be reconciled. Six focused cases passed
(2.20s); after adding the nonstandard-file assertion, its affected case passed
(0.25s). Scoped Ruff and Basedpyright pass. Census remains 78 resolved, 58 open.

MixinSquared's bundled-library role is resolved. Source 88d7f4f (extractor
27c648b) retains four wrapper and four core entry classes, independently
reproduced. Wrapper manifest SHA-256:
6a7cbdcfb28d23625a5a4468a982f9d5011767bc226793639d02532001fc47c2.
Core manifest SHA-256:
a46ec939d8f5fba8cbb02ca91e76e87d25d830ebc7be3711056659e04a14d673.
The existing extractor now traverses the observed two-level nested path while
preserving pinned parent/leaf identities and output format. Its smoke output
remains in evidence/raw/item8/mixinsquared-nested-smoke.

The wrapper's configuration declares a plugin but no mixin/client/server lists.
Its plugin initializes MixinSquared, loads service-provided cancellers and
annotation adjusters, and reorders transformation extensions. Core bootstrap
registers the dynamic target selector and cancellation/annotation-adjustment
extensions. The captured registrars operate on mixin methods, annotations and
extension registries. This is transformation support for consumers' mixins,
not an independent authored-site generator. The wrapper has eleven files and
the core has sixty-three; neither contains assets or data. Their original class,
archive and disassembly identities are bound by the existing provider test.

Five focused cases pass (2.13s). A line-length issue was corrected before the
scoped quality checks. Do not recapture either bundled library or reopen the
Trinkets fallback. Remaining Supplementaries scope is other common/mixin hooks
and full parent payload accounting. Census remains 78 resolved and 58 open.

The Trinkets fallback is now resolved. The existing provider test checks the
exact dev/emi/trinkets/api/TrinketsApi.class path, including prefixed copies,
in every hash-verified retained and platform archive and recursively embedded
JAR. None supplies that class. Together with the already bound runtime absence
of the trinkets mod ID and the captured dispatcher condition, this excludes the
Trinkets initialization branch for the frozen inputs. No extra source capture
or general scanning framework was needed. Four focused cases pass (2.10s);
scoped Ruff and Basedpyright pass. This supersedes the open Trinkets instructions
below. MixinSquared, remaining common/mixin roles and parent payload accounting
remain open; census stays 78 resolved and 58 open.

Retained integration entries are captured in 11b6396 (extractor 5355d74),
manifest 1ec5f3694856a3a56bf280d1ceb4bf980a741f63fe7ad1fddba78ea6c7d2b1d3.
All eight class/disassembly identities and the existing runtime log are bound by
the focused provider test; independent r1 matches every generated file.

| Entry | Membership role |
| --- | --- |
| CreateCompat and CreateCompatImpl | init is empty; setup registers bamboo-spike and hourglass movement behaviors for existing contraptions. No independent structure registration. Preserve the dispatcher's platform condition rather than inferring activation from the mod name. |
| CCCompat and CCCompatImpl | Registers speaker/cannon capabilities and a capability event callback for their existing block entities. No independent authored-site generator. |
| CuriosCompat | Registers the Curio slot-reference codec; other helpers inspect equipped keys and quivers. Inventory compatibility. |
| FarmersDelightCompat | init is empty. Its other helpers handle existing crop/block and food interactions. No initialization-time family contribution. |
| QuarkCompat and QuarkCompatImpl | Registers Tater-in-a-Jar block/item/block-entity compatibility and subscribes to the Quark load bus. Other helpers address existing pistons, blocks, inventories and items. The tag-based quill method reads the structure tag then calls a holder-set overload that returns null; do not claim a generated quill or discoverability behavior from its name. |

The preserved runtime log lists create, computercraft, farmersdelight, quark and
curios. It does not list soul_fire_d, shulkerboxtooltip, decorative_blocks,
endergetic, caverns_and_chasms, infernalexp, architects_palette or trinkets.
Soul-fired dispatch is also hard-coded false in the captured CompatHandler
initializer. Trinkets is not yet excluded by its missing mod ID: its dispatcher
also tests dev.emi.trinkets.api.TrinketsApi class presence. Resolve that concrete
fallback or the delegate's membership role before closing compatibility coverage.

Three focused cases pass (0.89s); scoped Ruff and Basedpyright pass. Remaining
provider work is the Trinkets boundary, MixinSquared, remaining common/mixin
roles and complete parent payload accounting. Do not repeat these integration
captures or infer Item 8 attribute completion. Census remains 78 resolved, 58 open.

Common setup dispatch is now retained in 6bfcf37 (extractor 9e9c74b), manifest
cbab9d898accfb9bedc9ab98c56e9b85f08747a062353dd8350d5699dbfad049.
Its bootstrap targets bind the registered setup, asyncSetup and tag-dependent
callbacks. The latter two reach the already inspected disabled-block processor
and road-sign destination cache. Reuse those component roles. Setup registers
flammability, frame filling, item behavior and compatibility callbacks; it is
not itself an independent site generator.

Source dbcbefc (extractor 77b2261), manifest
3a14ffe0a11a67a2cb31b7825dce2fe1bdef83b644754f89816a63558144b58a,
retains RegUtils and CompatHandler. RegUtils.registerAdditionalPlacements passes
pancakes, sticks, blaze rods, gunpowder and lunch baskets to item-placement APIs.
This resolves that named route as item-to-block placement, not world generation.
CompatHandler.setup has four conditional calls: CreateCompat, CCCompat,
SoulFiredCompat and ShulkerBoxTooltipCompat. Its optional registry initialization
also dispatches named integrations. Their retained/absent status and contribution
roles still need reconciliation; the dispatcher capture alone does not close
them. Keep this specific remaining boundary instead of reopening all setup code.

Both captures reproduce independently and their class/disassembly identities
are bound in the existing provider test. Three focused cases pass (0.90s), with
scoped Ruff and Basedpyright passing. MixinSquared, remaining common and mixin
roles, and complete parent payload accounting remain open. Census stays 78
resolved and 58 open. No final canonical-family denominator is claimed.

Bundled Sable Companion service role is resolved in source 53c2374 (extractor
bbae69f). Its four-class manifest is
0e58be3a4ae7cc39891a83c05fd25707e7dafc44831648596ee5ea64dafef660,
independently reproduced and bound by the existing provider test. The nested
archive has fourteen classes and five metadata/service/image/license files, with
no packaged generation data. Its service declaration names DefaultSableCompanion.
That implementation returns empty or null sublevel lookups, zero sublevel
velocities, coordinate projections and supplied-callback results. It has no
independent authored-site generator. The interface selects the highest-priority
ServiceLoader provider and supplies coordinate overloads; the direct helpers
provide vector/quaternion codecs and client-level access. This does not prove
which service implementation wins across all retained archives or validate the
mathematical correctness of every distance overload. It does not re-enable Sable.
Three focused cases pass (0.83s); scoped Ruff and Basedpyright pass. Remaining
Supplementaries membership work includes MixinSquared, common delegates and
remaining hooks/payload accounting. Census remains 78 resolved and 58 open.

Stronghold component roles are resolved by source 1d28c70 (extractor b0508d1).
The seven-class common-entry manifest is
7d0fe813b6039a677168e347e9c9d73c4af2aae8d9b2728cab6e9b9783ac2e74;
independent r1 matches, and the existing focused test binds original classes
and disassemblies. StrongholdCrossingSconceMixin injects at postProcess TAIL
on vanilla StrongholdPieces.FiveCrossing, placing one wall sconce inside that
piece. StrongholdRoomSconceMixin targets RoomCrossing and places four sconces
when its room type is zero. Both check SCONCE_ENABLED. The frozen building.sconce
enabled flag is true and bound by the test. These are components of existing
vanilla stronghold pieces, not independent families. Their presence does not
prove those vanilla pieces generate under the retained stronghold replacements.

Placement/processor source a74ae7b (extractor e1e2005) resolves those roles:
the galleon placement queries exclusion zones against existing structure sets;
the processor substitutes disabled blocks inside supplied template block info.
Neither introduces another family. Its three-class manifest
aaae4d5157a42bdff7bc12d048945a324e3c0c45d8e0bf06edf46a06a7264195 is
independently reproduced and bound by the same focused test.

The common-entry capture also retains SupplementariesForge, Supplementaries,
ServerEventsForge, ServerEvents and MixinPlugin. The loader calls commonInit and
server-event registration; commonInit reaches the already inspected ModWorldgen
and ModServerDynamicResources. MixinPlugin adds no methods beyond construction
and inherits Moonlight SimpleMixinPlugin. Preserve that shared dependency for
the remaining entry coverage rather than treating the plugin name as proof.
ModSetup and other common delegates, remaining declared mixins, bundled code and
full payload reconciliation still prevent whole-provider closure. Do not repeat
the resolved generation implementations or stronghold/mineshaft component roles.
Both focused cases pass (0.79s); scoped Ruff and Basedpyright pass. Census remains
78 resolved, 58 open. This checkpoint supersedes the older open processor and
placement instructions below, not the remaining provider gate.

Custom-generation role follow-up: BarnaclesMultifaceGrowthFeature uses the
configured multiface block's placement and spread operations; BasaltAshFeature
scans a matching surface and writes the configured top and optional lower block.
These are natural growth and terrain decoration. SpawnEntityWithPassengersFeature
creates the configured entities/passengers, handles boat variants/container loot
and supplies the existing galleon component pools. It is not another site family.
RoadSignStructure and GalleonStructure select suitable positions and call vanilla
JigsawPlacement.addPieces with their start pools. Their configuration-dependent
eligibility and assembled attributes remain separate from membership.

RoadSignFeature includes deferred construction. It places a generator block and
stores its configuration. Source ccbfda7 (extractor dabd675) captures that block
entity callback; manifest a6a99e646dd7b65793defda3168306b20e1a70a901b7d37e024d4aea3f6f5194
is independently reproduced and bound by the focused test. The first tick starts
an asynchronous ROAD_SIGN_DESTINATIONS lookup; completion invokes the already
captured applyPostProcess to finish sign blocks, text, lighting and optional
notice-board content. Failure paths log and/or remove the generator. A feature
placement returning true is therefore not proof that a finished sign was observed.
This remains the same root/component design chain, not another family.

Preserve one named nonregistry grouping question: the freestanding cave-urn
cache candidate. The cave_urns biome modifier selects the cave_urns placed feature,
which selects urns_patch: a vanilla random patch of simple urn blocks marked
treasure=true. The galleon urn pool also consumes urns_patch as a component.
Do not count that component again as a galleon family, and do not silently exclude
the freestanding treasure-bearing patch as vegetation. Its cache-versus-decoration
family boundary is for explicit canonical reconciliation; no new family total is
claimed here. The other four biome modifiers select basalt ash, ocean/shore
barnacles and wild flax. All five modifier references are bound by the existing
focused component test, as is the urn patch's treasure-bearing block definition.

Two focused cases pass in 0.79s; scoped Ruff and Basedpyright pass. No new runtime
measurement or graph was added. Remaining provider work: shared processor and
placement roles, loader/event/mixin entry coverage and full payload reconciliation.
Reuse these resolved generation paths. Census remains 78 resolved, 58 open.

Generation source d6221a7, extractor 24f0a75, captures eleven identified classes
with manifest 0eb64c666c0db4bd45091038bb2b3d622a1e57f896d31fe0df1279f2ff357e5d.
Independent r1 matches, and the focused test binds every source to the archive.
ModWorldgen registers two structure types, four feature types, the elevator
piece, a placement type and a block-removal processor. The two roots and four
feature implementations are captured; remaining processor/placement semantics
must reuse existing evidence where available before adding source captures.

The elevator membership boundary is resolved: MineshaftPiecesMixin injects at
the head of vanilla MineshaftPieces.createRandomShaftPiece and substitutes the
result of MineshaftElevatorPiece.getElevator when non-null. This is a component
of existing mineshafts, not a separate structure-family root. The corridor mixin
can replace chain supports with the selected rope under its cutout condition.
Both mixins occur in supplementaries-common.mixins.json.

The elevator method rejects Y greater than 48 and checks a random draw against
MINESHAFT_ELEVATOR, plus PULLEY_ENABLED, ROPE_ENABLED and TURN_TABLE_ENABLED.
The frozen common config records pulley/rope/turntable enabled and an elevator
setting of 0.035. This is a configured input, not an observed occurrence rate;
the actual selected mineshaft implementation and placement constraints still
matter. Do not infer that elevators were observed in the clean worlds.

Two focused cases pass in 0.80s, with scoped Ruff and Basedpyright passing.
Continue the captured custom-generation implementation roles, then remaining
loader/event/mixin and payload coverage. The complete provider remains open;
the census is still 78 resolved and 58 open. Do not recapture these eleven
classes or count elevator pieces as new families.

The exact retained archive SHA-256 is
0dd0445af35aa15ad012833c4b8024d2ed70320d1ace0316d2f5b684b06a997d.
Existing family-decision checks account for galleon and road_sign roots. The new
focused component check reconciles all twelve packaged pools and eighteen
templates with the accepted pool graph. All are connected to these roots;
neither graph records missing references or unresolved pool elements.

The road-sign graph connects start_pool, the road_sign template and feature_pool.
The feature pool invokes the placed road_sign feature, which selects the
configured road_sign feature of custom type supplementaries:road_sign. These
are linked representations within the existing root candidate, not three extra
families. This proves the packaged relationship, not its actual placement success
or completeness of the custom feature implementation. Preserve the same design
boundary when reconciling any other consumers.

The galleon graph includes hull, room, sail, urn and entity-feature components.
Do not promote its boats or inhabitants to independent structure families.
Common-worldgen code also contains MineshaftElevatorPiece; its registration and
injection consumer require inspection. That is a concrete additional component
question, not an accepted family. Custom structure/feature implementations,
other generation hooks and full provider payload still require disposition.
Provider census remains 78 resolved and 58 open.

```sh
uv run pytest -q tests/item8/test_supplementaries_provider_scope.py
uv run ruff check tests/item8/test_supplementaries_provider_scope.py
uv run basedpyright tests/item8/test_supplementaries_provider_scope.py
```

One focused case passed in 0.73s, with both scoped quality checks passing. The
existing packaged catalog handles the commented road-sign pool JSON. No new
parser, graph, runtime measurement or canonical-inventory rewrite was needed.

## Creating Space packaged component checkpoint

### Final provider disposition

Creating Space provider coverage is RESOLVED. It contributes the four existing
packaged jigsaw roots already bound to the runtime registry and family decisions.
No additional independent authored family is identified by its complete packaged
payload, captured entry mechanisms, crater writer, contraption handling or common
hooks. Shared Create remains a separate open provider; this disposition does not
close Create's generation or attribute contributions.

All 1645 non-directory files are partitioned: 342 classes, 676 assets, 612 data
resources, ten packaged build-cache files and five metadata/image files. There
are no extra nested archives, service declarations, scripts or undeclared payload
categories outside that partition. The five NBT assets under ponder are client
instruction scenes. The six NBT world-generation templates are separate: five
are connected to existing roots; moon/abandoned_outpost is disconnected from
those generation graphs. It has no literal reference in the archive's classes
and no loader in the reviewed generation entry paths. Disposition: unused
packaged component in this provider's generation graph, not another family.
This combines resource and executable-role evidence rather than treating a
negative string search alone as proof.

Common-hook delegate source 3133afb, extractor 30d6302, has manifest
452f56f08a577286fe894d2e692aa26b73e67dda6027274c318fcb30c7c7145e;
independent r1 is exact and all four sources are bound by the existing test.
The common roles are:

| Captured route | Supported disposition |
| --- | --- |
| Entity ticks, equipment and breathing | Existing-entity oxygen, temperature, equipment and travel handling; the resolved arrival delegate places no site. |
| Neighbor notifications and RoomAtmosphere | Recompute the oxygen room's shape, sealers and leaf filters from existing blocks; update atmosphere entity data, not room construction. |
| IgniteOnPlace | Conditional Venus placement reactions: fire and soil replacement, not an authored-site generator. |
| DataEventHandler and UnlockedDesignManager | Load and synchronize engine exhaust/power-pack unlock lists; initial entries include bell_nozzle and open_cycle. |
| CSDimensionUtil | Travel-map, cost, gravity, arrival-height and atmosphere lookups. removeUnreachableDimensions filters a travel list, not world generation registries. |
| Declared entity, gravity and contraption mixins | Existing-entity properties/movement and collection of existing rocket multiblock parts. |
| Fluid mixin and FluidInit | Fluid-contact block conversions, including dimension-dependent stone and source-lava obsidian; no assembled site. |
| Recipe mixins | Ingredient matching, retained item data and recipe serialization. |
| Remaining annotated entries and mixins | Configuration registration/reload, capabilities, client controls/rendering/tooltips and oxygen overlay/backtank behavior. No separate authored-content route. |

Custom datapack data describes propulsion components, reachable dimensions and
block mass. Remaining JSON covers recipes, loot, advancements, tags, damage and
the already-accounted dimension/terrain/generation definitions. These can remain
inputs to family attributes without becoming extra families. Preserve the
existing Mars bastion-leg fallback and the unused Moon cave configuration;
neither is silently repaired or promoted to an independent family.

The existing root decision case plus the three focused provider cases passed:

```sh
uv run pytest -q tests/item8/test_creating_space_provider_scope.py 'tests/item8/test_family_decisions.py::test_provider_groups_bind_full_definitions_pools_and_registry[creatingspace-4]'
```

Four cases passed in 0.98s. Scoped Ruff and Basedpyright pass. No new runtime
experiment was needed. Census: 78 resolved, 58 open. This is provider coverage,
not completion of Item 8 or final acceptance of canonical groups and attributes.

### Earlier incremental checkpoints

Arrival follow-up is RESOLVED in source 526983c, extractor 215a6a4. Manifest
04e25ddcbb7b1105bcf0d27eb83c605dda16a97ec4d683d829f94d74e97da0e1
is bound by the existing source-coverage test. CustomTeleporter chooses arrival
height and the rocket's stored destination X/Z (or an ordinary entity's X/Z),
then constructs DimensionTransition with DO_NOTHING for the post-transition
action. No platform placement or named template load in this delegate. Do not
reopen this boundary merely because travel uses dimension and position helpers.
Continue remaining common-entry/mixin roles, full payload and the disconnected
outpost's other consumers. This follow-up does not close the entire provider.

The captured crater writer has a terrain role: it writes AIR, updates the
carving mask and applies CarvingContext.topMaterial through its local callback.
Its height calculation consumes density values. Its structure references read
existing starts and perform bounding-box calculations; they do not construct
new structure starts. Do not infer successful structure relocation from the
adjustBoundingBox call: its returned value is discarded. This inspection is
for content membership, not a crater-shape or relocation correctness experiment.

The focused packaged check binds all three carver configurations and all seven
biomes' carver declarations. Mars cave/plains select the vanilla cave configuration;
Moon cave/plains select the custom crater configuration. The separately packaged
moon_cave carver is not referenced by those seven biome declarations. Venus uses
the vanilla canyon and space has no carvers. No additional authored family is
introduced by these carver paths.

RocketContraption.assemble searches an existing moved structure and starts it
moving. addBlock extends the captured contraption's block information and engine
properties. RocketContraptionEntity.disassemble updates flight-recorder NBT in
that block map before calling Create's contraption disassembly. Their indexed
StructureTemplate references are StructureBlockInfo records for those blocks,
not named world-generation template loads. Travel delegates to
CustomTeleporter.getTransition; inspect that actual arrival boundary before
closing the travel path. This is the next concrete source dependency, not a
reason to audit the flight scheduler or propulsion equations.

Both focused cases and scoped quality checks pass after adding the carver
consumer assertions. Other common-entry/mixin roles, complete payload roles and
the disconnected outpost's possible other consumers still require disposition.

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

### Hanging-fixture boundary resolved on 2026-09-06

The decisions and working inventory now explicitly exclude
`tectonic:underground_river/lanterns` and the hanging-light branch of
`terralith:cave/frostfire/frostfire_ceiling` from additional structure families.
Each repeats an individual chain-and-light fixture on existing cave terrain.
Neither contribution assembles a separate site beyond that fixture. Their
authored materials justify preserving them as named environmental contributions,
but do not make every repeated ceiling decoration a family. This decision is
based on the complete configured geometry, not the provider name, vanilla codec,
lack of loot, or a numerical size cutoff. It does not exclude distinct buildings
or landmarks containing the same blocks.

The existing provider tests now bind both exclusion records and their evidence
identities while retaining the geometry, placement-route and frozen-configuration
checks. All four cases and scoped Ruff/Basedpyright pass. The existing builder
reproduces the inventory exactly:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-hanging-fixture-dispositions.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-hanging-fixture-dispositions.json
uv run pytest -q tests/item8/test_tectonic_provider_scope.py tests/item8/test_terralith_provider_scope.py
uv run ruff check tests/item8/test_tectonic_provider_scope.py tests/item8/test_terralith_provider_scope.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_tectonic_provider_scope.py tests/item8/test_terralith_provider_scope.py tools/build_item8_inventory.py
```

Use an absent output path. This closes two named family-boundary questions,
adding no families and changing no baseline content. It does not assert inactive
placement or observed frequency. The decorated-mushroom and other named boundary
questions remain open. The 421 provisional registry groups and provider census
(90 resolved, 46 open) are unchanged.

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

### Decorated-mushroom boundary resolved on 2026-09-06

`explorations:large_mushroom` is now an explicit decorated-vegetation exclusion
in the decisions and rebuilt inventory. The configuration creates a mushroom
stem and brown-mushroom canopy using giant trunk and jungle foliage placers.
Its sole decorator hangs chains and lanterns from foliage; it adds no separately
constructed site layout. This follows the actual geometry and decorator role,
not the vanilla codec, lack of loot or a numerical size threshold. Constructed
tree houses and other sites using vegetation as support are not excluded by
this decision. Keep the named generation contribution and the existing
Collections.shuffle limitation; no baseline content was changed.

The existing provider test binds the decision and evidence hashes, stem/canopy
providers, placers and complete decorator list alongside its placement/modifier
checks. Both cases and scoped Ruff/Basedpyright pass. Inventory reproduction:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-decorated-mushroom-disposition.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-decorated-mushroom-disposition.json
uv run pytest -q tests/item8/test_explorations_provider_scope.py
uv run ruff check tests/item8/test_explorations_provider_scope.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_explorations_provider_scope.py tools/build_item8_inventory.py
```

Use an absent output path. This closes the previously named mushroom boundary
without adding a family. Other named groupings and 46 provider rows remain open;
the 421 provisional registry groups are unchanged. Required attributes and final
review/delivery gates remain incomplete.

### Scarecrow family decision recorded on 2026-09-06

The decisions and rebuilt working inventory now record `explorations:scarecrow`
as one nonregistry family. Its nine configured/placed material variants are
acacia, bamboo, birch, cherry, dark oak, jungle, mangrove, oak and spruce. The
unsuffixed selector references those same variants. Facing, material choices
and the figure's five component positions do not add families.

The existing source and complete provider inspection below support this decision.
The existing feature test now binds the decision's evidence hashes, exact variant
lists and runtime configured/placed membership, alongside the selector and nine
biome-modifier routes. Both provider cases and scoped Ruff/Basedpyright pass.
The inventory rebuild reproduces exactly with the existing tool:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-scarecrow-membership.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-scarecrow-membership.json
uv run pytest -q tests/item8/test_explorations_provider_scope.py
uv run ruff check tests/item8/test_explorations_provider_scope.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_explorations_provider_scope.py tools/build_item8_inventory.py
```

Use an absent output path. No source recapture or world experiment was required.
Effective biome eligibility, actual placement and required attributes remain
separate from this membership decision. The decorated mushroom's boundary is
still unresolved. The 421 provisional registry groups and whole-provider census
(90 resolved, 46 open) are unchanged; this is one explicit nonregistry grouping
closure, not the final family count.

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

### Crashed-ship membership decision recorded on 2026-09-06

The machine-readable decisions and rebuilt inventory now include
`betterend:crashed_ship` as one independent nonregistry family. Its dedicated
placement and erosion produce a standalone wreck. Reusing
`minecraft:end_city/ship` does not turn that wreck into a city component; the
ship attached to an End city remains a component of the existing city family.
Rotation, erosion and biome occurrences remain variants of this wreck family.
The source and direct biome routes below already establish this boundary, so
no additional capture, experiment or generic helper inspection is required.

The existing crashed-ship test now binds the decision's source hashes and
template/placed-feature identity. All thirteen BetterEnd cases pass, as do
scoped Ruff and Basedpyright. Rebuild the inventory with:

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-crashed-ship-membership.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-crashed-ship-membership.json
uv run pytest -q tests/item8/test_betterend_feature_candidates.py
uv run ruff check tools/build_item8_inventory.py tests/item8/test_betterend_feature_candidates.py
uv run basedpyright tools/build_item8_inventory.py tests/item8/test_betterend_feature_candidates.py
```

The output path must not already exist. This closes one family-membership
decision, not the Item 8 exit gate. The 421 registry-root groups are unchanged;
nonregistry families are additional contributions. Observed occurrence and
required family attributes remain separate work. Current provider coverage is
90 resolved and 46 open; this decision does not change that census.

The broader `uv run pytest -q tests/item8/test_family_decisions.py` run returned
70 passed and three failures. The failed cases are
`test_authored_designs_bind_roots_settings_and_missing_components` for
`explorations:` and `aether:`, and
`test_design_groups_cover_registry_and_bind_variant_definitions` for
`repurposed_structures`. Each still expects the old generic custom-generation
UNKNOWN string where earlier decisions now contain a resolved empty list or a
more specific limitation. All 421 registry groups and these test bodies are
unchanged by this increment. These existing assertion inconsistencies must be
reconciled against their focused source tests before the full Item 8 gate.
The three failures reproduced with `uv run pytest -q
tests/item8/test_family_decisions.py --lf --tb=short`; raw output is retained at
`evidence/raw/item8/crashed-ship-family-regressions.log`. This is not a claim
that the full family-decision gate passes.

The follow-up correction removes only the two blanket assertions that an
untraced custom generator must retain the original generic UNKNOWN prose.
Pool tracing cannot establish that claim. The registry membership, definition,
pool-backed missing-component comparisons and evidence-hash assertions remain.
No family decision, missing-resource finding or uncertainty was changed. Existing
Explorations, Bronze dungeon, cloud, mansion and monument source/component tests
cover the independent evidence; they are included in the affected validation:

```sh
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_explorations_provider_scope.py tests/item8/test_aether_bronze_components.py tests/item8/test_aether_cloud_source.py tests/item8/test_mansion_components.py tests/item8/test_monument_components.py --tb=short
uv run ruff check tests/item8/test_family_decisions.py
uv run basedpyright tests/item8/test_family_decisions.py
```

All 87 affected cases pass, with zero scoped Ruff or Basedpyright findings.
The preceding three failures are preserved as the rejected pre-fix result.
This resolves the assertion defect only; provider coverage and Item 8 completion
remain open.

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

### Regions Unexplored remaining captured feature roles

The 35 implementations in source 04c515f now have contribution dispositions.
Their actual block writers, supplied configured-feature materials and internal
branch/cap/root geometry establish the following roles. Reuse this inspection;
source coverage alone was insufficient in the preceding checkpoint.

| Implementations | Contribution role |
| --- | --- |
| GlisteringIvyFeature, HangingEarlightFeature | Hanging plant columns and roof substrate patches using ivy/wart or earlight and Nether terrain states. |
| HangingPrismariteFeature | Hanging prismarite blobs and pillars. Mineral decoration, not a building or authored monument. |
| HyacinthPlantsFeature, HyacinthStockFeature | Aquatic plants, blooms, seagrass and supplied tall-hyacinth states. |
| GiantBlueBioshroomFeature, GiantGreenBioshroomFeature, GiantPinkBioshroomFeature, GiantYellowBioshroomFeature | Mushroom stems and caps using configured bioshroom stem/block/glowing-block states. Large plant geometry does not establish an adventure family. |
| AshenTreeFeature, AspenTreeFeature, BlackwoodTreeFeature, CypressTreeFeature, DeadTreeFeature, EucalyptusTreeFeature, GiantCypressTreeFeature | Trunks, foliage, roots and branches with supplied wood/leaf states; cypress adds moss and hanging vegetation. |
| KapokTreeFeature, LarchTreeFeature, LargeSocotraTreeFeature, LushPineTreeFeature, MegaBaobabTreeFeature, SakuraTreeFeature | Tree canopies and branches; kapok and pine include vines, and Sakura includes a bee-nest placement. A bee nest on a tree is an ecological component, not a separate authored encounter site. |
| SmallEucalyptusTreeFeature, SmallJoshuaTreeFeature, SmallOakTreeFeature, StrippedPineTreeFeature, TreeShrubFeature, UltraBaobabTreeFeature | Supplied tree/shrub logs, leaves and branches, with ground/root handling. Size or material variants are not independent families. |
| CobaltShrubFeature, LargeJoshuaTreeFeature, MediumJoshuaTreeFeature, SmallSocotraTreeFeature, YellowBioshroomShrubFeature, BrimWillowFeature, TallBrimWillowFeature | Direct natural-set wood/leaves, mushroom or Nether plant states, producing shrubs, branches and tree forms. |

The 26 tree/shrub implementations, four giant bioshrooms and five plant/mineral
implementations account for all 35 captured classes. They introduce no additional
named authored-site candidate. The existing stump-and-fallen-log candidate remains
separate, with its six configuration variants and possible stump-only outcome.
The earlier thirteen terrain feature and Ashen trial-chamber component decisions
also remain unchanged.

PlaceOnGroundDecorator source e06c9e1 is now bound in the existing candidate test.
Its exact manifest is
2b459bc6975a0ddffe6826ea332312ef7f78e0d31354d165d455f3d127f03544.
The writer chooses the configured state above eligible dirt using supplied
height and target checks. It decorates an existing tree's ground neighborhood;
it does not supply another architectural layout. Branch-mode configuration in
several tree writers controls whether natural branches are placed. Do not expand
that material-selection boundary into a gameplay or tree-shape audit.

The two focused candidate/source cases pass (0.96s), with scoped Ruff and
Basedpyright passing, using the commands in the preceding checkpoint. No source
was recaptured and no new measurement system was introduced. Regions Unexplored
remains OPEN for its remaining common-entry, tree-placer/decorator and complete
payload/overlay/JSON5 roles. Current census is still 88 resolved, 48 open.

### Regions Unexplored full payload and overlay boundary

The focused provider test now accounts for all 8077 non-directory files in the
frozen archive and each root data category. This closes the file-accounting gap,
while semantic entry/configuration and custom tree-component checks remain open.
The only embedded archive is META-INF/jars/json5-java-3.0.0.jar, SHA-256
2e0f73784e6bc4c755e52d485f628d110d397f079d58b118658b903be9aa0533.
Its complete payload is 28 JSON5 classes plus a manifest, with no loader metadata,
services, scripts, Minecraft references or NeoForge entry annotations. Parent
class references are limited to RUConfigHandler and the four Json5Ops classes.
It supplies configuration parsing/serialization; no independent mod entry or
packaged world-generation data exists in the nested archive. Do not audit its
parser internals as a structure-family requirement. The parent's configuration
behavior remains part of the pending common-entry interpretation.

All thirty overlay files have explicit roles:

| Overlay | Files | Contribution |
| --- | ---: | --- |
| painted_planks | 16 | Shaped crafting recipes. |
| birch_aspen_trees | 6 | Vanilla tree definitions using birch/aspen components. |
| oak_taller_trees | 4 | Vanilla oak tree configurations. |
| taiga_pine_trees | 2 | Vanilla pine/mega-pine tree configurations. |
| common_grass_sprouts | 1 | A random plant patch. |
| forest_fancy_oaks | 1 | A selector among existing birch, oak and fancy-oak vegetation. |

NeoForge's pack metadata declares all six directories with regions_unexplored:config
conditions. Painted planks uses key painted_planks; the other five use their
vanilla_changes/<overlay> keys. Preserve conditional activation separately from
membership. These declarations do not create another structure root or authored
site. The tree-component implementations still require their pending dispositions.

```sh
uv run pytest -q tests/item8/test_regions_unexplored_provider_scope.py
uv run ruff check tests/item8/test_regions_unexplored_provider_scope.py
uv run basedpyright tests/item8/test_regions_unexplored_provider_scope.py
```

Both focused cases pass (0.16s); scoped Ruff and Basedpyright pass. This uses the
existing pinned archives and test infrastructure. No new runtime experiment or
measurement system was added. RU remains OPEN for common/configuration entry
roles and the remaining registered tree placers/decorators. Census: 88 resolved,
48 open. Earlier full-payload/overlay/JSON5 inventory gaps are now resolved and
must not restart.

### Regions Unexplored custom tree-component closure

Source 0f263ed, extractor 16127c9, retains the remaining 24 tree/configuration
classes. Manifest SHA-256:
c0e8750b46dd656807e33cc3906aa98fd736da650cc01cdd0754cc94ec63f243.
The independent capture matches every file. The existing two decorator captures
complete all 21 classes in the packaged trunkplacer, foliageplacer and
treedecorator directories. Their roles are now resolved:

- Nine foliage placers produce canopy or mushroom-cap layers. Their shared
  context and utility write supplied foliage states through FoliageSetter,
  checking valid tree positions, persistent leaves and waterlogging.
- Aspen, Magnolia and Redwood trunk placers write configured logs, branch
  geometry and foliage attachment positions. RUTrunkPlacer supplies height,
  dirt-below and axis handling. These four classes are tree components.
- GroupBranchDecorator and RandomBranchDecorator place supplied branches and
  leaves around an existing log set. HangingVinesDecorator places supplied
  vine states. WillowTrunkDecorator adds configured wood roots. AttachedToLogs
  and PlaceOnGround retain their previously accepted decoration roles.
- The three type registries register nine foliage types, three trunk types and
  six decorators. Registration and component types are not independent families.
  TrunkPlacerDirtUtil distinguishes peat, silt and alpha-grass substrates.

These implementations use the already-inspected supplied tree materials and
add no independent authored-site candidate. No recursive parser, branch-mode,
shuffle or general tree-gameplay audit is needed for this disposition.
RUConfigHandler reads/writes client/common JSON5 configuration via their codecs;
it creates missing defaults and attempts cleanup of named legacy configuration
files. It is configuration I/O, not an independent generation callback. The
common-condition caller still selects effective settings separately from family
membership. The NeoForge-specific mixin file is explicitly empty on all three
sides and has no plugin.

Three focused provider cases pass (0.19s), with scoped Ruff and Basedpyright
passing, using the commands above. The test binds the new and reused source
hashes and compares every packaged tree-component class against the captured
set. Final RU common-entry interpretation and provider closure remain open;
archive, overlay, feature and tree-component coverage need no repetition.
Census remains 88 resolved providers, 48 open.

### Create packaged generation boundary

Source 1fa2306, extractor cb34d9e, preserves AllFeatures, LayeredOreFeature,
ConfigPlacementFilter and CreateGameTests. Independent capture reproduces
byte-for-byte; identities SHA-256 is
7fb69a735eb1ffd0ada39ca9d1950120cf5fa87b142dc3e9814fab7ab9b5a5fe.

The hash-bound packaged data contains exactly three configured/placed/modifier
chains: zinc_ore, striated_ores_overworld and striated_ores_nether. Zinc uses
vanilla ore; the other two use the registered layered_ore feature. The captured
writer selects supplied layer states and replaces matching terrain, respecting
write eligibility and air exposure. It does not create another site candidate.
ConfigPlacementFilter reads the common world-generation disable flag. Effective
activation is separate from this contribution-role disposition.

All 245 top-level NBT resources partition into 67 data/create/structure/gametest
paths and 178 assets/create/ponder paths. CreateGameTests registers the six test
classes with RegisterGameTestsEvent and delegates test construction to
CreateTestFunction. Exact template-consumer reconciliation remains required;
this resource-path partition alone does not prove reachability or exclusion.
No packaged structure definitions or template pools occur in the full data
category partition. Embedded archive contents remain outside this partial check.

```sh
uv run pytest -q tests/item8/test_create_provider_scope.py
uv run ruff check tests/item8/test_create_provider_scope.py
uv run basedpyright tests/item8/test_create_provider_scope.py
```

One focused case passes (0.13s); scoped checks pass. Initial formatting and
untyped JSON findings were corrected. Create remains OPEN for common entry,
embedded-library roles and remaining template consumers. Census remains
89 resolved and 47 open. Reuse these ore-source and packaged-data checks.

### Create main entry and test-template consumer

Source 9dcbd3c (extractor cd1fefb) retains four additional entry/consumer classes;
independent capture matches. Identities SHA-256:
151d5db9de69c37bd56cb596da59fe227f4f750b77a873cae8c0459b7d4738d5.
The existing Create provider test binds every captured byte to its frozen JAR.

CreateTestFunction.of accepts GameTest-annotated methods, requires a nonempty
template and a GameTestGroup, constructs %s:gametest/%s/%s from namespace, group
path and template, and builds a Minecraft TestFunction. Together with the prior
CreateGameTests registration this resolves the test-loader role. It does not
claim that every packaged fixture is currently referenced by a test annotation.
Unused fixtures would still require an explicit disconnected disposition.

Create.onCtor registers the already resolved ore feature and placement types,
content/recipe/entity systems and one structure processor registration.
AllStructureProcessorTypes registers only create:schematic, using
SchematicProcessor.CODEC. Its consuming construction path remains to be bound.
The common setup initializes fluid, NBT and construction interaction handlers.
The declared CreateMixinPlugin supplies no additional mixin list and only filters
Xaero compatibility classes according to mod availability. Other common mixin
and event bodies remain outstanding; the constructor alone is not their proof.

Two focused cases pass (0.16s), with scoped Ruff and Basedpyright passing using
the commands in the preceding checkpoint. Create remains OPEN. Continue its
common-event/mixin membership roles, schematic/Ponder consumers and embedded
library entries. Do not repeat the ore or GameTest loader interpretation.
Census remains 89 resolved, 47 open. No runtime or capture process is live.

### Create common dispatch and schematic construction

Source 65cb9b2 (extractor 76ac38c) preserves CommonEvents, ModBusEvents and
three schematic consumers; source b546705 (extractor 6c26595) preserves the
observed RuntimeDataGenerator. Both independent captures reproduce exactly.
Their identities hashes are bound in test_create_provider_scope.py.

CommonEvents dispatches existing contraption, minecart, train, logistics,
redstone and toolbox state updates, player synchronization, command registration,
recipe/belt reload listeners and lifecycle cleanup. These dispatch roles do not
add another authored-site candidate. Do not expand into ordinary machine or
vehicle simulation internals without a concrete membership question.

ServerSchematicLoader accepts a ServerPlayer upload into the uploaded-schematic
area and associates it with a schematic table. SchematicPrinter requires a
deployed schematic ItemStack and anchor; it loads the supplied template into a
SchematicLevel, prepares transformed block/entity targets and material requirements.
SchematicProcessor handles supplied template NBT and entity filtering. This is
player construction, not an additional natural-generation family. This scope
finding is not a security or correctness audit of schematic upload/printing.

ModBusEvents also adds create:dynamic_data through RuntimeDataGenerator. That
concrete call requires inspection beyond the packaged JSON catalog, using the
existing extractor rather than a new measurement system. The captured writer
iterates registered items, constructs cutting/washing recipes and item tags,
then inserts them into the dynamic pack. Recipe serialization is delegated to
RuntimeDataGenerator$StandardBuilder and remains the exact uninspected output
boundary. Preserve that outstanding check; do not claim whole dynamic-pack closure.

Three focused cases pass (0.22s), with scoped Ruff/Basedpyright passing using
the existing commands above. Create remains OPEN for the dynamic recipe output
boundary, other annotated/common mixin entry roles, Ponder and embedded-library
roles. Reuse completed common dispatch and schematic interpretation. Census is
89 resolved and 47 open. No runtime or source capture process is live.

### Create dynamic-data output resolved

Source 23fbee3, extractor 346e42e, preserves StandardBuilder. Its independent
capture matches; identities SHA-256 is
3bfb8d0f3a362eec0930be85992d6ee2470bf3aa40b1621748ec7c78061b7292.
The builder encodes a processing recipe with Recipe.CONDITIONAL_CODEC and inserts
successful JSON results into JSON_FILES with the recipe/ prefix. Together with
RuntimeDataGenerator's item-tag writer, this closes the observed dynamic-pack
membership question: recipe and item-tag content, no additional family candidate.
No recursive inspection of generic recipe codecs is required for membership.

The same focused test file now inventories the declared top-level entry surface:
58 classes contain Mod/EventBusSubscriber annotation descriptors, and 43 distinct
classes are declared in the common mixin list. These sets are disjoint. At this
checkpoint four annotated entries are already captured (Create, CommonEvents,
ModBusEvents and CreateGameTests), leaving 54 annotated classes and 43 common
mixins to disposition. Client-only annotations can justify exclusion once
inspected; these are entry checks, not 97 new families or a requirement to audit
all gameplay helpers. The three embedded libraries remain Flywheel, Ponder and
Registrate. Ponder template-consumer roles remain outstanding.

Four focused cases pass (0.47s); scoped Ruff/Basedpyright pass. Provider census
remains 89 resolved and 47 open. Continue the finite entry and embedded-library
checks without reopening the resolved dynamic pack, ore or schematic roles.

### Create declared common-mixin roles

Source 9ad30e0 (extractor 969a3d9) retains all 43 declared common mixins with
annotations. Independent capture matches; identities SHA-256:
e7941906291f7bfe6f15b3989e4db734cb57c0aec9e2ac55f370bd4cd2be7193.
The focused test requires exact equality between captured classes and the
common declaration list, in addition to every source and disassembly hash.

| Declared hooks | Membership role |
| --- | --- |
| ArmorTrimMixin, CustomItemUseEffectsMixin, SmithingMenuMixin | Cardboard trim textures, custom use effects, trim advancement and backtank enchantment handling. |
| BeehiveBlockMixin, BlockItemMixin, BlockMixin | Deployer hive interaction, placement and captured block drops. Existing machine interactions. |
| EnchantedCountIncreaseFunctionMixin | Loot count adjustment for crush damage. Existing entity loot behavior, not a generation route. |
| EntityMixin, LavaSwimmingMixin, MobMixin, PlayerMixin, ProjectileUtilMixin | Fire-immunity metadata, seats, diving boots, contraption collision/attack/pickup and rider interaction. |
| MapItemSavedDataMixin | Existing station marker persistence, placement on a map and removal/update when stations change. |
| WaterWheelFluidSpreadMixin | Fluid passage around an existing waterwheel and its structural blocks. |
| ItemStackMixin and the three datafixer mixins | Clipboard component migration, stored block-position renames, item-component migration and schema registration for existing data. |
| BuiltInRegistriesMixin | Initializes CreateBuiltInRegistries and skips the validation callback for Create-owned registries. The initialization delegate remains part of the pending registry-entry check; do not infer registry content from skipped validation. |
| Twenty-four accessor mixins | Expose existing block shape/state, loot predicate, concrete conversion, crop age, dispenser, falling block, fluid, test, item-frame/model/inventory, entity particle, registry, minecart fuel, effect, NBT accounting, potion, projectile, entity-tick, recipe, system-report and hit-result data or methods. These accessors do not initiate generation. |

This closes interpretation of the declared common-hook bodies. No named family
candidate was added. Do not recursively audit ordinary machine, movement, loot
or migration helpers on the strength of these hooks alone. The precise
CreateBuiltInRegistries initialization boundary remains to reconcile with the
54 outstanding annotated entries. Ponder consumers and the three embedded
libraries also remain. The common-hook batch must not be recaptured.

Four focused cases pass (0.47s); scoped Ruff/Basedpyright pass. Census remains
89 resolved providers and 47 open. No runtime or capture process is live.

### Create remaining entry capture, client exclusions and registry roles

Source 05d472d (extractor 6fdfb9e) retains the remaining 54 annotated entries
and CreateBuiltInRegistries. Independent capture reproduces exactly; identities
SHA-256 is 3428176fa46ad9d0a07e89f9f7c1748b8bea6154e793ad07bc7e251dbf8fbafb.
The test binds all bytes and requires exact equality with the annotated class
set minus the four previously captured entries, plus the registry initializer.
Do not recapture this batch. Full methods and annotations are already delivered.

Seventeen subscribers explicitly declare Dist.CLIENT, and CreateClient declares
a client-only Mod entry. These eighteen entries are excluded from dedicated
server generation on their loader metadata. They are rendering/input/UI helpers;
client class names alone were not used as exclusion evidence. Ponder's supplied
assets and embedded library still need their separate content-role disposition.

Four additional annotated entries have resolved non-family roles:

- CreateRegistriesImpl registers the potato projectile datapack registry.
- CreateDataMapsImpl registers regular and superheated blaze-burner fuel maps.
- RemapHelper aliases legacy block, item, fluid and block-entity identifiers.
- AllConfigs registers client/common/server configuration, stress-value providers
  and load/reload dispatch.

CreateBuiltInRegistries defines twelve typed registries for mechanical arms,
fan processing, item attributes, displays, mounted storage, contraptions,
package-port targets and potato-projectile render/hit actions. This resolves
the specific registry-initialization question left by BuiltInRegistriesMixin.
It introduces no independent structure-family registry.

Thirty-two of the captured annotated entries still need their final contribution
role recorded. Their captures must be reused; ordinary gameplay helper tracing
is not required absent a specific unresolved site boundary. The three embedded
libraries and Ponder consumers also remain. No new family candidate was added.
Four focused cases pass (0.51s); scoped checks pass after fixing Ruff's regex
flag spelling. Census remains 89 resolved, 47 open. No capture or runtime is live.

### Create remaining 32 annotated entry roles resolved

Reuse full source 05d472d and its exact source binding in the four passing
Create focused cases recorded above. This increment interprets existing evidence;
no new capture, runtime, measurement system or test framework was needed.
The following groups account for all 32 entries left after the eighteen client
exclusions and four registry/configuration dispositions.

| Entries | Contribution role |
| --- | --- |
| SuperGlueHandler, SuperGlueItem | Player block placement and glue-item interaction, creating glue attachments/effects around placed blocks. |
| CouplingHandler, MinecartCouplingItem, MinecartContraptionItem | Existing minecart occupancy/coupling and wrench-driven pickup of a supplied contraption into an item. |
| CardboardArmorHandler, DivingBootsItem, DivingHelmetItem, NetheriteDivingHandler, ExtendoGripItem, CardboardSwordItem | Equipped-item effects on hitbox, targeting, breathing, movement, fire protection, reach, durability, sound, knockback and attack handling. |
| HauntedBellPulser | A player holding the bell triggers a client pulse packet. No site writer. |
| ClipboardValueSettingsHandler, ZapperInteractionHandler, WrenchEventHandler | Player-triggered settings copy/paste, block selection and wrench callbacks on existing blocks. |
| SymmetryHandler | Player place/break events with the symmetry wand invoke matching construction/removal; other hooks render its mirror and particles. Player construction is not a naturally generated family. |
| FluidBottleItemHook, FluidReactions | Bottle interaction and block-state outcomes of colliding pipe fluids/spills. Existing pipe operation, not independent site generation. |
| ValveHandleBlock, CrushingWheelBlockEntity, DeployerFakePlayer, ManualApplicationRecipe | Player valve interaction, crushed-mob drop motion, deployer drop/XP/retaliation rules, and right-click application recipes replacing the clicked block. |
| FunnelItem, ItemHatchHandler, StockTickerInteractionHandler, BlazeBurnerHandler, ClickToLinkBlockItem, LinkHandler, ScheduleItemEntityInteraction | Player item/block/entity interactions, logistics manager UI, burner egg/splash impact, link frequencies and train conductor schedules. |
| ItemUseOverrides, ValueSettingsInputHandler, EdgeInteractionHandler | Player-triggered block use, settings and connection callbacks on existing block entities. |

These entry triggers and bodies are bounded to existing entities/items/blocks or
explicit player construction. No independent authored-site candidate emerged.
Do not expand this membership check into generic machine simulation, permission,
recipe, combat or network correctness audits. The exact source remains available
for later required family attributes where applicable.

All top-level annotated-entry and declared common-mixin roles are now accounted
for. Create remains OPEN for embedded Flywheel/Ponder/Registrate roles, Ponder
content consumers and final complete payload reconciliation. The 32-entry batch
must not be restarted. Census remains 89 resolved and 47 open.

### Create embedded Flywheel and Registrate resolved

Flywheel source 4a7f244 (extractor f61db3a) independently reproduces exactly.
The focused test binds its nested archive and disassembly identity. Its only
annotated entry, FlywheelNeoForge, explicitly declares Mod dist=CLIENT. All
three declared mixin configurations contain client lists only, with no common,
server or plugin entries. Its 636 files partition into 555 classes, 71 assets,
three metadata files and seven root mixin/refmap/image/pack files. No data,
service loader or deeper nested archive is present. This rendering library
contributes no dedicated-server structure family. No render-backend audit is
required to reach that membership disposition.

Registrate's immutable nested archive contains 88 com/tterrag/registrate classes
and a manifest declaring FMLModType: GAMELIBRARY. There are no annotated Mod or
EventBusSubscriber entries, services, mixins, packaged data or deeper archives.
Its consumer-driven registration role is already shown by Create.onCtor calling
CreateRegistrate.registerEventListeners. It has no independent family payload or
automatic generation entry. Do not inspect all generic builder internals absent
a concrete unresolved consumer contribution.

Both full nested-file partitions and exact hashes are checked by
 test_create_flywheel_and_registrate_membership in the existing provider test.
Five focused cases pass (0.61s); scoped Ruff and Basedpyright pass using the
existing commands above. The Flywheel source has no UUID-literal matches.

Two of Create's three embedded libraries are now resolved. Remaining Create
membership work is Ponder's entries/services, common accessors and content
consumers, followed by final complete parent payload reconciliation. Reuse all
closed top-level and nested roles. Census remains 89 resolved, 47 open.

### Create final membership disposition

Ponder source 0177383 (extractor 28badcf) retains all six annotated entries,
five service implementations, three common accessors and the Ponder, PonderClient
and PonderSceneRegistry consumers. Independent capture reproduced exactly.
Common startup registers configuration, packets and commands. Client entries
manage guide rendering, resources, input and configuration UI. Services wrap
platform metadata, packet transport, rendering, fluid properties and player
block placement. Common accessors expose biome seed, entity level and server
storage; they do not create authored sites.

PonderSceneRegistry compiles storyboards by loading a template through Minecraft's
client resource manager and placing it in a PonderLevel based on the current
client level. This accounts for the parent's 178 assets/create/ponder templates
as client guide scenes. The 67 data/create/structure/gametest templates are test
fixtures under the already resolved GameTest consumer. Neither set adds natural
structure families. Ponder's complete 531-file partition contains 470 classes,
47 assets, nine metadata files and five root files. Its five services and three
common accessors are bound to the captured source. No server mixin, mixin plugin,
data directory or deeper nested archive is present.

The final parent accounting covers all 11753 files: 2692 classes, 5076 assets,
3974 data files, seven metadata files and four root files. The metadata contains
only the manifest, loader declaration, access transformer, three already
resolved nested libraries and their jarjar metadata. The 25 custom Create data
files are potato-projectile definitions for the previously inspected registry.
The existing exact worldgen partition is three ore chains; all template paths,
58 annotated entries and 43 common mixins have retained contribution roles.
Reuse their earlier source interpretation, including dynamic recipe/tag output,
rather than reopening generic machine or library behavior.

Create membership is RESOLVED with no independent natural structure family.
This does not claim its machines, projectiles or loot have no relevance to later
family attributes. No candidate was added or removed by this final closure.
Six focused cases pass, with scoped Ruff and Basedpyright passing:

```sh
uv run ruff check tests/item8/test_create_provider_scope.py
uv run basedpyright tests/item8/test_create_provider_scope.py
uv run pytest -q tests/item8/test_create_provider_scope.py
```

Current census: 90 resolved, 46 open providers. Forgified Fabric API is the last
open packaged-generation lane provider; 24 code-only and 21 unmatched rows also
remain. Resolve those membership rows, then named canonical merge/split decisions
before resuming the eleven attributes. These provider counts are not family counts.

### Forgified Fabric API packaged-data boundary

Source 6eb28e4, produced by extractor bbdf6f3 and independently reproduced,
resolves the sole packaged biome modifier. FabricBiomeApiV1 registers a unit
codec whose modifier receives BiomeModificationImpl's sorted list. That list
starts empty and addModifier receives predicates and consumer callbacks from
callers. FabricBiomeModifier selects the phase and biome, then applies those
records. BiomeModifications exposes caller-supplied feature, carver and spawn
registration. This is shared dispatch, not an independent authored site.

The parent contains 43 nested archives and five other metadata/icon files.
All nested archives have been checked for data and further archives. No deeper
JAR or binary NBT template exists. Packaged data is exactly 491 conventional
tags, the biome modifier JSON and one empty GameTest SNBT fixture. The focused
check binds that partition and all five captured class/disassembly identities.

```sh
uv run ruff check tests/item8/test_fabric_provider_scope.py
uv run basedpyright tests/item8/test_fabric_provider_scope.py
uv run pytest -q tests/item8/test_fabric_provider_scope.py
```

One case and scoped checks pass. This closes the packaged-data question, not
whole provider membership. Remaining: bundled entry/mixin contribution roles,
including biome selection and resource/test consumers. Do not repeat the
modifier capture or expand generic callback internals without an unresolved
site contribution. No new family candidate; census stays 90 resolved, 46 open.

### Fabric biome selection hooks

Source d052da5 (extractor 2426342) independently reproduces all six declared
biome mixins and the NetherBiomeData/TheEndBiomeData consumers. The existing
provider test binds the complete declared mixin set and exact source identities.

| Hook | Membership role |
| --- | --- |
| BiomeSourceMixin | Passes possible biome sets through the extension hook. |
| ChunkNoiseSamplerMixin, NoiseConfigMixin | Propagate the world seed to climate samplers. |
| MultiNoiseUtilMultiNoiseSamplerMixin | Retains that seed and constructs the End biome noise sampler. |
| NetherBiomePresetMixin | Appends caller-registered biome/noise-point pairs to the Nether preset. NetherBiomeData's map starts empty. |
| TheEndBiomeSourceMixin | Retains the biome registry lookup, selects a returned biome through overrides and includes registered custom biomes in the possible set. |

TheEndBiomeData's built-in choices reference vanilla End, highlands, small
islands, midlands and barrens biomes. Its public methods accept replacement
biome keys and weights from consumers. These are biome-selection contributions,
not additional authored sites. Do not recursively audit the weighted-selection
algorithm or generic codec behavior for family membership.

Two focused Fabric cases and scoped Ruff/Basedpyright pass using the commands
above. No new family candidate. Whole provider membership remains open for the
other bundled entry/mixin roles, particularly resource loading and GameTest
consumers. Census remains 90 resolved, 46 open; these completed biome roles must
not be recaptured or reinterpreted on continuation.

### Fabric GameTest consumer roles

Source 6bffda6 (extractor ad51ae4) independently reproduces all five GameTest
mixins plus generated entry, initializer and namespace consumer. The generated
entry invokes FabricGameTestModInitializer, which registers classes from the
fabric-gametest entrypoint with Minecraft's GameTestRegistry. Namespace and test
registry hooks supply test names and invoke FabricGameTest implementations.
StructureTemplateManagerMixin adds an SNBT resource source to the template
manager; this is a loading path, not a natural structure placement request.
TestCommandMixin reads the test-output directory property. TestServerMixin
changes the test server's dedicated-server flag.

These roles account for the packaged empty test fixture without creating an
independent family. They do not imply that all template-manager calls are
restricted to tests. No custom authored site is supplied by this module's
packaged data. The existing focused source check now covers both biome and
GameTest declared mixins without duplicating the binding implementation.
Three focused Fabric cases and scoped Ruff/Basedpyright pass with the commands
above. Remaining whole-provider work is the other bundled entry/mixin roles,
particularly resource loading. Reuse all closed biome and GameTest roles.
Census remains 90 resolved, 46 open; no family candidate was added.

### Fabric resource-loading checkpoint

Source cce2d3d (extractor 8cf0d23) independently reproduces the thirteen declared
common resource-loading mixins, generated entry and ResourceManagerHelperImpl.
The existing focused check binds their complete declared set and source hashes.
Four Fabric cases and scoped Ruff/Basedpyright pass with the commands above.

The hooks cover pack visibility/activation, resource type and source tracking,
reload-listener ordering, default/test pack selection and known-pack registry
synchronization. No independent site candidate has emerged. ResourceManagerHelperImpl
registers caller-provided mod pack paths and reload listeners. Two concrete
consumers were retained separately in 6326f21 (extractor 149e849), with independent
byte-for-byte reproduction: ModResourcePackUtil and ModNioResourcePack.

ModNioResourcePack opens mod paths and overlays. ModResourcePackUtil's fallback
resources are pack.mcmeta and pack.png. The default/test selection methods call
ModResourcePackCreator.loadPacks. That specific pack-discovery delegate remains
to inspect before closing this module; do not restart its thirteen hooks or
expand registry packet behavior into a networking audit. The two-consumer source
still needs its focused identity binding alongside the final discovery result.
Census remains 90 resolved, 46 open providers. Other Fabric module entry/mixin
roles remain after this resource-loading question.

### Fabric resource-loading membership resolved

Source 8cfe15c retains ModResourcePackCreator (extractor 6cf2878) and the
PlaceholderResourcePack/Factory supplier (extractor e29938a). Both captures
independently reproduce. The focused check also binds the previously delivered
ModResourcePackUtil and ModNioResourcePack source in 6326f21.

ModResourcePackCreator.loadPacks constructs the fixed fabric pack, adds
programmer-art and high-contrast paths only for CLIENT_RESOURCES, and returns
to ResourceManagerHelperImpl's caller-registered built-in pack list. The fixed
pack has no namespaces, returns no ordinary resource and enumerates no resources;
its factory wraps that same pack. It supplies pack metadata rather than structure
content. Together with mod-path/overlay loading and the complete packaged-data
partition, this resolves resource loading as infrastructure for consumer content,
with no independent family. No further generic supplier or packet audit is needed.

Five focused Fabric cases and scoped Ruff/Basedpyright pass using the existing
commands. Reuse the resolved biome, GameTest and resource-loading roles. Other
bundled module entry/mixin roles remain before whole-provider closure. Census
remains 90 resolved, 46 open providers; no family candidate was added.

### Exact Fabric module queue

The frozen parent contains 43 modules. Twenty-one membership roles are resolved below;
22 remain open. These are internal modules of one retained provider, not added
providers or families. All packaged data is already partitioned by the existing
Fabric check. Open rows require contribution-role inspection, not an audit of
every implementation method. Reuse existing captures and stop at the content
boundary. This queue replaces the unspecified phrase "other Fabric modules".

| Fabric module | Membership disposition |
| --- | --- |
| `fabric-api-base-0.4.42+d1308ded19.jar` | RESOLVED: empty loader entry and consumer-driven event/utility library; see below. |
| `fabric-api-lookup-api-v1-1.6.71+c290471319.jar` | RESOLVED: consumer API caches and startup type validation; no independent family. See below. |
| `fabric-biome-api-v1-13.0.31+1e62d33c19.jar` | RESOLVED: biome selection and consumer callbacks; see above. |
| `fabric-block-api-v1-1.1.0+b0c22bb819.jar` | RESOLVED: block interface, read/accessor or climbing roles; no independent family. See below. |
| `fabric-block-view-api-v2-1.0.11+e9036fd419.jar` | RESOLVED: block interface, read/accessor or climbing roles; no independent family. See below. |
| `fabric-blockrenderlayer-v1-1.1.52+c290471319.jar` | RESOLVED: client utility, no independent server family; see below. |
| `fabric-client-tags-api-v1-1.1.15+e053909619.jar` | RESOLVED: empty or client-guarded entry and client API roles; no independent server family. See below. |
| `fabric-command-api-v2-2.2.28+36d727be19.jar` | RESOLVED: Entry and selector hook 0224278, initializer 703f0ac. Caller-supplied command/argument registration and selector flags; no independent family. |
| `fabric-content-registries-v0-8.0.19+5e0d320019.jar` | RESOLVED: Caller content properties, tools, brewing, fuel, composting and gift data. Sources 2cbd452 and e5c769a; no independent family. |
| `fabric-convention-tags-v1-2.1.5+7f945d5b19.jar` | RESOLVED: tag keys and legacy-tag warning callback; no independent family. |
| `fabric-convention-tags-v2-2.11.1+87e5848019.jar` | RESOLVED: conventional tags, tag interface and translation warnings; no independent family. |
| `fabric-data-attachment-api-v1-1.4.5+26d408aa19.jar` | RESOLVED: Caller attachment-type registration and transfer of existing data. Sources a17da36, db84f92 and e6aa022; no independent family. |
| `fabric-data-generation-api-v1-20.2.34+a4c3605619.jar` | RESOLVED: Empty initializer and data-output hooks for consumer pack generation. Source 36951e9; no independent family. |
| `fabric-entity-events-v1-1.8.0+5ede667619.jar` | RESOLVED: Existing-entity event and elytra/sleep callbacks; no independent family. See entity-event disposition below. |
| `fabric-events-interaction-v0-0.7.13+86e0887119.jar` | RESOLVED: Existing interaction callbacks and cancelled-break state synchronization; sources e030cd8 and 5147b43. No independent family. |
| `fabric-game-rule-api-v1-1.0.53+36d727be19.jar` | RESOLVED: Game-rule maps, command categories and client rule editing; no independent family. See final loot/recipe/rule disposition below. |
| `fabric-gametest-api-v1-2.0.5+29f188ce19.jar` | RESOLVED: test registration and SNBT loading; see above. |
| `fabric-item-api-v1-11.2.0+0c57911319.jar` | RESOLVED: Existing item/component and enchantment modification support; sources 4ddacfa and 41d9c83. No independent family. |
| `fabric-item-group-api-v1-4.1.7+e324903319.jar` | RESOLVED: Empty initializer, creative-menu modification callbacks and client UI resources. Source 07cd09b; no independent family. |
| `fabric-key-binding-api-v1-1.0.47+62cc7ce119.jar` | RESOLVED: client utility, no independent server family; see below. |
| `fabric-lifecycle-events-v1-2.6.0+e40d8add19.jar` | RESOLVED: Entry and seven common/server hooks 4de41d1, initializer 353d68f. Existing lifecycle callbacks and loaded-chunk bookkeeping; no independent family. |
| `fabric-loot-api-v2-3.0.15+a3ee712d19.jar` | RESOLVED: Legacy loot interfaces and v3-to-v2 consumer callback forwarding; no independent family. See final loot/recipe/rule disposition below. |
| `fabric-loot-api-v3-1.0.3+333dfad919.jar` | RESOLVED: Loot provenance, consumer reload callbacks and builder/accessor support; no independent family. See final loot/recipe/rule disposition below. |
| `fabric-message-api-v1-6.0.14+6a754fce19.jar` | RESOLVED: Empty initializer and chat callbacks; source 1e30004. No independent family. |
| `fabric-model-loading-api-v1-2.1.0+6e8f52c719.jar` | RESOLVED: client rendering/input roles, including declared entry hooks; no independent family. See below. |
| `fabric-networking-api-v1-4.3.0+30a980d919.jar` | RESOLVED: Packet transport, negotiation and existing connection/entity callbacks; source ad9fbe2. No independent family. |
| `fabric-object-builder-api-v1-15.2.1+cc242efd19.jar` | RESOLVED: Empty initializer and supplied object/type support. Source 0fa369a; no independent family. |
| `fabric-particles-v1-4.0.2+824f924c19.jar` | RESOLVED: client rendering/input roles, including declared entry hooks; no independent family. See below. |
| `fabric-recipe-api-v1-5.0.15+59440bcc19.jar` | RESOLVED: Ingredient serializer registration and NeoForge ingredient-wrapper codecs; no independent family. See final loot/recipe/rule disposition below. |
| `fabric-registry-sync-v0-5.3.1+f9aace1619.jar` | RESOLVED: Caller registry registration and existing-registry callbacks; sources 4bc3d16, e5a03ee and 7b86b55. No independent family. |
| `fabric-renderer-api-v1-3.4.1+9125b6dc19.jar` | RESOLVED: empty or client-guarded entry and client API roles; no independent server family. See below. |
| `fabric-renderer-indigo-1.7.1+9125b6dc19.jar` | RESOLVED: client rendering/input roles, including declared entry hooks; no independent family. See below. |
| `fabric-rendering-data-attachment-v1-0.3.49+73761d2e19.jar` | RESOLVED: block interface, read/accessor or climbing roles; no independent family. See below. |
| `fabric-rendering-fluids-v1-3.1.6+a51883b219.jar` | RESOLVED: empty or client-guarded entry and client API roles; no independent server family. See below. |
| `fabric-rendering-v1-5.1.0+1a09bd5a19.jar` | RESOLVED: Client-guarded initialization and fifteen client-only hooks; source 2e5d280. No independent family. |
| `fabric-resource-conditions-api-v1-4.3.0+5bdd099819.jar` | RESOLVED: Consumer resource filtering and declared overlay selection. Sources 969f1bb and abcf742; no independent family. |
| `fabric-resource-loader-v0-1.3.1+4ea8954419.jar` | RESOLVED: consumer pack loading; see above. |
| `fabric-screen-api-v1-2.0.25+0ae1214819.jar` | RESOLVED: client rendering/input roles, including declared entry hooks; no independent family. See below. |
| `fabric-screen-handler-api-v1-1.3.90+8dbc56dd19.jar` | RESOLVED: Empty initializer and menu-opening support; source c5ebd6e. No independent family. |
| `fabric-sound-api-v1-1.0.23+10b84f8419.jar` | RESOLVED: client utility, no independent server family; see below. |
| `fabric-transfer-api-v1-5.4.3+a25cb45619.jar` | RESOLVED: Existing inventory/fluid capability adapters and transactional container hooks. Source 94eaafd; no independent family. |
| `fabric-transitive-access-wideners-v1-6.2.0+6c854b6f19.jar` | RESOLVED: access declarations only; no code or data payload. |
| `forgified-fabric-loader-2.5.68+0.18.4+1.21.1-full.jar` | RESOLVED: Loader service and existing FML metadata adaptation; sources 1cb6fe0, 4beaa6b and 6a6fcc4. No independent family. |

The transitive-access-wideners module has exactly five files: manifest, lowcodefml
metadata, access transformer, icon and nesting metadata. There are no class,
service, mixin or data files. It changes member accessibility and supplies no
independent site. The focused packaged-data test binds this complete partition.

### Fabric API Base membership resolved

Source da5dce0 (extractor 77dc50e) independently reproduces its only annotated
entry. The constructor calls Object's constructor and returns, with no registration
or static initializer. The complete module contains 17 classes and four metadata/
icon files. No mixin, service, packaged data or nested archive is present. Other
classes implement consumer-driven events, ordering and utility types; no automatic
content contribution remains to follow. No independent family is added.

The existing provider test binds the full partition, sole annotated entry and
source identities. Six focused Fabric cases and scoped Ruff/Basedpyright pass
using the commands above. Fabric module queue: five resolved, 38 open. Whole
provider count stays 90 resolved, 46 open. Next: remaining named module entries,
starting with conventional tag registration; do not repeat API Base internals.

### Fabric v1 conventional tags resolved

Source 73efd5b (extractor ff7e104) independently reproduces the entry,
TagRegistration and ConventionLogWarnings. The entry installs a server-start
warning callback, which reads registry tags and logs migration warnings.
TagRegistration creates tag keys rather than registered structures or resources.
The module contains twelve classes and four metadata/icon files, with no mixins,
services or data. The focused check binds this full partition, sole annotated
entry and all three source identities. No independent family is added.

Seven focused Fabric cases and scoped checks pass using the existing commands.
Module queue: six resolved, 37 open. Whole-provider census: 90 resolved, 46 open.
Next: v2 conventional tags, then the remaining named module roles.

### Fabric v2 conventional tags resolved

Source e1c7c24 (extractor 27f6181) independently reproduces the entry,
TagRegistration, TranslationConventionLogWarnings and the sole TagKeyMixin.
Registration creates tag keys, including keys for existing structures, rather
than structure definitions. The entry installs translation-warning checks that
read item tags and language entries. The mixin declares the FabricTagKey
interface on TagKey; it contains no methods or fields. These roles add no
independent family. The module's complete partition is 16 classes, 491 tag JSON
files, fourteen language files and five metadata/icon/mixin-declaration files.

The focused test binds that partition and all four source identities. Eight
Fabric cases and scoped Ruff/Basedpyright pass. The initial type check rejected
an untyped JSON variable; its explicit type annotation fixed that check before
acceptance. Fabric module queue: seven resolved, 36 open. Whole provider census
stays 90 resolved, 46 open. Next: remaining named module entries and hooks.

### Fabric block-render-layer, key-binding and sound modules resolved

Source 1c35ebe (extractor 5624e8a) independently reproduces the sole annotated
entry in each module. Block-render-layer and key-binding initialization is
explicitly guarded by FMLEnvironment.dist.isClient(). The sound entry invokes
only Object's constructor and returns. Every declared mixin is client-only,
with no common/server list or plugin. Their complete payloads are nine, seven
and four classes respectively, with metadata, icon and mixin declarations;
sound additionally contains assets/fabric-sound-api-v1/sounds/empty.ogg.
No data, service loader or nested archive is present. These modules supply
client rendering/input/sound support, not an independent server family.

The existing test binds all complete partitions, annotated-entry sets, mixin
sides and source identities. Eleven focused Fabric cases and scoped checks pass.
A missing type annotation on an empty set and its resulting line length were
corrected before acceptance. Module queue: ten resolved, 33 open. Whole-provider
census remains 90 resolved, 46 open; no family candidate was added.

### Three Fabric client API membership roles resolved

Source 339a264 (extractor 6ff2013) independently reproduces client-tags,
renderer-api and rendering-fluids entries. Client tags and renderer API have
constructors that only call Object and return. Fluid rendering guards its
initializer with FMLEnvironment.dist.isClient. These entry paths add no
server content. Full module partitions contain respectively 7, 35 and 20 classes;
all remaining files are exact metadata/icon sets plus the declared client mixin
configs. No data, service or nested archive payload remains unexplained.

Client tags has no mixin config. Renderer API has four main client mixins and
one client debug-HUD mixin. Fluid rendering has three client mixins. None of
these configurations declares common/server hooks or a plugin. Each module
has only its generated annotated mod entry, with no annotated event subscriber.
The existing client-utility test now handles the actual zero/two/one config
partitions and binds every source/class/archive identity. No rendering helper
inspection is needed for family membership. No family is added.

```sh
uv run pytest -q tests/item8/test_fabric_provider_scope.py
uv run ruff check tests/item8/test_fabric_provider_scope.py
uv run basedpyright tests/item8/test_fabric_provider_scope.py
```

All fourteen focused Fabric cases and scoped checks pass. Fabric queue: thirteen
resolved, thirty open modules. Whole-provider census stays 90 resolved and 46
open because Fabric is still one unfinished provider. Source reproduction
commands and exact hashes are in the three source READMEs.

### Four Fabric client rendering and input modules resolved

Source b3a9dd3 (extractor e2ae798) retains seven entry/hook classes, reproduced
independently. Model loading, particles and screen API have empty generated
loader constructors. Indigo initialization is guarded by isClient. The particle
subscriber handles RegisterParticleProvidersEvent and initializes the client
particle factory with the Minecraft particle engine. Screen subscribers forward
client screen render, keyboard and mouse events to Fabric callbacks, including
input cancellation. These client event routes add no independent world site.

Indigo declares a mixin plugin, so it was inspected explicitly. It reads mod
properties for renderer presence and compatibility, returns the Indigo
applicability choice and supplies no additional mixin list. Its load, target,
pre-apply and post-apply callbacks add no content. No renderer helper audit is
needed beyond these roles.

Complete module partitions contain 39 model-loading, 20 particle, 58 Indigo and
36 screen classes. Nonclass files are metadata/icons, the exact client mixin
configs and particle/Indigo access transformers. No data, service or nested
archive payload is present. Client mixin counts are respectively 5, 3, 5 and 3;
none declares common or server mixins. The existing test binds every captured
entry/subscriber/plugin and the complete annotated-entry set.

```sh
uv run pytest -q tests/item8/test_fabric_provider_scope.py
uv run ruff check tests/item8/test_fabric_provider_scope.py
uv run basedpyright tests/item8/test_fabric_provider_scope.py
```

All eighteen focused cases and scoped checks pass. Fabric now has seventeen
resolved and twenty-six open modules. No family was added. Whole-provider
coverage remains 90 resolved, 46 open, including the unfinished Fabric parent.

### Three Fabric block utility modules resolved; lookup callback remains open

Source 771947f (extractor 231284d) reproduces four generated entries and all
nine declared common mixins across lookup, block API, block-view API and
rendering-data attachment. The latter three entries are empty. Block API adds
interfaces and tag-driven trapdoor-climbing behavior, retaining ladder-facing
checks. Block-view supplies block/render-data interfaces and delegates existing
biome reads. Rendering-data attachment defaults its attachment to null and
forwards its render-data accessor. These are consumer utilities, not independent
generation paths. No content helper tracing is required for those three roles.

The existing test binds all common hooks and the full payload partitions:
29 lookup, 8 block API, 12 block-view and 8 rendering-data classes. Nonclass
files are exact metadata/icons/mixin configs, plus the block-view access
transformer. Client-only additional mixins number two for block-view and one
for rendering-data; neither client config has a common/server hook or plugin.
Every module has only its generated annotated entry, no annotated subscriber,
and no data/service/nested archive payload.

Lookup is deliberately still open. Its common hook maintains weak lookup
cache references and invalidates caller caches. Source 3a9ed5d (extractor
2043743) reproduces ApiLookupImpl: its only initialization action registers
EntityApiLookupImpl.checkSelfImplementingTypes on SERVER_STARTED. Inspect that
concrete callback next; the callback name is not absence proof. Do not repeat
the delivered cache/initializer captures or inspect unrelated lookup methods.

```sh
uv run pytest -q tests/item8/test_fabric_provider_scope.py
uv run ruff check tests/item8/test_fabric_provider_scope.py
uv run basedpyright tests/item8/test_fabric_provider_scope.py
```

All twenty-two focused cases and scoped checks pass. Three membership roles
close, giving twenty resolved and twenty-three open Fabric modules. No family
is added. Whole-provider census stays 90 resolved and 46 open. Exact source
reproduction commands and hashes are in the five source READMEs.

### Fabric lookup membership resolved

Source 6a7858d (extractor 65b700e) independently reproduces the identified
EntityApiLookupImpl callback. Its REGISTERED_SELVES map starts empty and is
populated by registerSelf with caller-supplied entity types. At server start,
the one-time callback constructs an instance with EntityType.create and checks
Class.isInstance. It throws explicitly for a null instance or incompatible
API class. It does not add the instance to the world or register a generation
route. Construction alone is not an authored spawn. Consumer entity definitions
remain attributable to their own providers, without a general constructor audit.

This closes the remaining lookup contribution boundary using the existing
entry/cache capture and complete 29-class payload partition. The existing test
now also binds the initializer and callback manifests, class hashes and exact
disassembly hashes. No family is added.

```sh
uv run pytest -q tests/item8/test_fabric_provider_scope.py
uv run ruff check tests/item8/test_fabric_provider_scope.py
uv run basedpyright tests/item8/test_fabric_provider_scope.py
```

All twenty-two cases and scoped checks pass. The focused binding function now
has 52 explicit statements; a local PLR0915 exception retains the direct checks
without adding a helper or framework merely to satisfy the statement limit.
The initial lint finding was corrected before acceptance. Fabric queue:
twenty-one resolved, twenty-two open modules. Whole-provider census remains
90 resolved, 46 open. Reuse all lookup sources; no remaining lookup membership
question requires further helper tracing.

### BOP landmark family integration

The existing named decisions are now integrated in family-decisions.json and
the reproduced inventory: biomesoplenty:anomaly and biomesoplenty:monolith each
contribute one independent landmark family. State and size variation do not
create additional families. Both bone-spine configured IDs share one natural
column writer and contribute no family. Existing source, registration, packaged
placement and captured dimension-biome evidence are reused and hash-bound.
The two pumpkin boundaries remain the next BOP canonical decisions.

Five focused cases and scoped quality checks pass. No source capture, world run
or measurement framework was added. The 421 registry groups are unchanged; the
two landmarks are outside that registry, and the global family total remains
unaccepted pending the remaining provider and grouping decisions.

```sh
uv run pytest -q tests/item8/test_bop_feature_candidates.py
uv run ruff check tests/item8/test_bop_feature_candidates.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_bop_feature_candidates.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-bop-landmarks-r1.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-bop-landmarks-r1.json
```

### BOP pumpkin boundaries closed

Both big_pumpkin and pumpkin_patch are now explicit decorated-vegetation
exclusions in family-decisions.json and the reproduced inventory. The former
writes a giant plant with a stem and leaves; its carved/light block references
are replacement predicates. The latter scatters plants and individual light
fixtures without assembling an independent site. Neither contributes a family.
The preserved writers and already-bound registered/packaged biome routes
suffice; no recapture or helper expansion was needed.

BOP canonical membership is now settled: two independent landmark families,
anomaly and monolith. Bone-spine and both pumpkin boundaries are closed. Other
provider roles retain the prior complete partition. Required attributes and
generated-world reconciliation remain Item 8 work. Five focused cases and
scoped quality checks pass. The registry groups remain unchanged.

```sh
uv run pytest -q tests/item8/test_bop_feature_candidates.py
uv run ruff check tests/item8/test_bop_feature_candidates.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_bop_feature_candidates.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-bop-pumpkins-r1.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-bop-pumpkins-r1.json
```

### BetterEnd ruined-pillar canonical grouping

The two named feature candidates now form one explicit nonregistry family,
betterend:ruined_obsidian_pillar. FallenPillarFeature and
ObsidianPillarBasementFeature use the same column motif with different remnant
shapes, transforms and weathering. These are two variants, not two independently
composed site designs. Their independent Dragon Graveyards placement keeps the
family separate from central End spike components. Neither material nor a
shared generic shape helper is by itself the grouping rationale.

The existing eight-class source capture, both inline configured/placed routes
and captured End biome membership are bound to the decision. Thirteen focused
cases, scoped checks and inventory reproduction pass. No new source or geometry
measurement was added. Exact placement orientation and the eleven attributes
remain separate from this membership decision.

Next reconcile BetterEnd architectural choices and its disconnected house.
The existing registry groups also include terrain/vegetation entries (including
BetterEnd mountains and lakes); their canonical dispositions must be resolved
before treating the working group count as a family total.

```sh
uv run pytest -q tests/item8/test_betterend_feature_candidates.py
uv run ruff check tests/item8/test_betterend_feature_candidates.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_betterend_feature_candidates.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-betterend-pillars-r1.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-betterend-pillars-r1.json
```

### BetterEnd fixture and disconnected-house dispositions

lantern_woods/light_1 is now an explicit ambient-fixture exclusion. Its narrow
pedestal/wall/fence, chain and filalux content forms a light, not an independent
site. It remains a selected and attributable generation contribution.
blossoming_spires/house is preserved as a disconnected architectural candidate,
not an additional active family: the current configured lists omit it and the
direct consumer does not scan adjacent files. A demonstrated additional consumer
would reopen that eligibility decision. Existing legacy-list evidence is reused.

This settles two named template questions. Of the original 42 selected
architectural candidates, 41 remain for design grouping after the fixture
exclusion. Those are template candidates, not 41 accepted families. Existing
21 vegetation exclusions and the six extra old-Bulbis vegetation templates
remain unchanged. No renderer, measurement or new source capture was added.

Thirteen focused cases, scoped quality checks and inventory reproduction pass.
The test binds the exact fixture palette/size/selection and both decisions to
the existing source and template catalogs.

```sh
uv run pytest -q tests/item8/test_betterend_feature_candidates.py
uv run ruff check tests/item8/test_betterend_feature_candidates.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_betterend_feature_candidates.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-betterend-template-exclusions-r1.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-betterend-template-exclusions-r1.json
```

### BetterEnd furnished-building family decisions

Six complete building designs are integrated under betterend:biome_buildings:
mushroom library, mushroom tree house, Lantern Woods cabin, Shadow Forest
mansion, Umbrella Jungle workshop house and Umbrella Jungle raised house.
The decision records each exact template, packaged box and design rationale.
The two Umbrella Jungle houses are not merged by name: broad workstation
construction differs from the narrow tall ladder/chest design. The mushroom
library and dwelling likewise differ in built form and furnished function.

These independently selected biome templates are outside the existing village
component graph. Rotation, terrain merging, offsets and recurring biome
placements do not add families. Packaged boxes are not accepted assembled-world
footprint measurements. Existing source, catalogs and active-list checks are
reused; no renderer or measurement system was added.

Fourteen focused cases and scoped checks pass. The new direct binding checks
join all six named templates, their used furnishing blocks and packaged sizes
to their active configured lists. The remaining BetterEnd selected architectural
queue is 35 ruin templates; grouping them remains open.

```sh
uv run pytest -q tests/item8/test_betterend_feature_candidates.py
uv run ruff check tests/item8/test_betterend_feature_candidates.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_betterend_feature_candidates.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-betterend-buildings-r1.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-betterend-buildings-r1.json
```

### BetterEnd ruin layout inspection

Source tool 3b14c8d renders the existing 35 ruin templates in six fixed sheets,
retained under sources/betterend-ruin-views. All six were manually inspected,
and every SVG reproduces byte for byte. The README records hashes, commands,
the rejected small-scale pilot and diagram limitations. No new dependency or
runtime measurement was introduced. Palette summaries did not preserve the
ordinary block arrangements needed for these remaining canonical comparisons.

The views distinguish low floor remnants, light fixtures, column/pedestal
forms, gateways and roofed construction within the ruin-named files. Family
assignments still require the material/content join and cross-biome comparison;
this capture alone closes no family decision. Do not repeat the rendering or
expand its fidelity without a concrete unresolved layout boundary.

### BetterEnd selected ruin grouping closed

All 35 ruin-named templates now have an explicit disposition in
family-decisions.json: thirty templates in ten design families, plus five
ambient light-fixture exclusions. The families are timber building remnants,
stone column remnants, masonry foundations, pedestal courts, central pedestal
altars, gateway remnants, a tiered purpur ruin, a crystal spire, an overgrown
fountain and an enclosed masonry ruin. Every group's exact template paths and
architectural rationale are recorded.

The grouping compares preserved layouts across biomes, with the exact palette
and stored-content evidence. Material, orientation, differing survival and
furnishings may vary within a design. This does not assert transformed-copy
equivalence or reconstruct an unknown original intact building. Individual
light supports remain fixtures despite their ruin filenames.

Together with the six furnished building families and the earlier light_1
exclusion, the 42 selected architectural candidates now comprise sixteen
design families represented by 36 templates and six excluded fixtures. All
21 selected vegetation templates remain excluded. The disconnected house is
still a separately preserved inactive candidate. No selected BetterEnd biome
template remains without a membership disposition. This is not a total for
BetterEnd's registry roots, independent pillar/ship routes or the whole pack.

Fifteen focused cases, scoped checks and inventory reproduction pass. The new
check reconciles all 35 exact archive paths to a disjoint exhaustive assignment
and active configured-list selection, with source/view hashes bound. Next
resolve terrain/vegetation entries in the provisional registry groups and
continue the other named providers' canonical boundaries.

```sh
uv run pytest -q tests/item8/test_betterend_feature_candidates.py
uv run ruff check tests/item8/test_betterend_feature_candidates.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_betterend_feature_candidates.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-betterend-ruins-r1.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-betterend-ruins-r1.json
```

### BetterEnd registry roles and reconciled membership subtotal

All fourteen BetterEnd structure-registry IDs remain accounted for exactly once
in nine groups. Three are authored structures: bridge, village and eternal
portal. Six are explicitly natural formations: lakes, mountains, giant ice star,
giant mossy glowshroom, small island and sulphuric cave. The captured writers
establish these roles. Natural formations remain inventoried rather than being
silently dropped from the registered structure universe or presented as buildings.

The independent feature/template routes add eighteen distinct families: sixteen
biome architecture families, one crashed ship and one ruined obsidian pillar.
The ship's already accepted singleton membership is now explicit as a families
list. The test verifies disjoint membership and a subtotal of 27 BetterEnd groups:
21 authored structure families and six natural-formation groups. Fixture,
vegetation and disconnected-template exclusions remain explicit. This is a
provider membership subtotal, not the final pack count or completed attributes.

The broad family-decision and BetterEnd checks passed 89 cases. A subsequent
explicit subtotal binding passed all sixteen BetterEnd cases. Initial typing
and formatting findings were corrected; scoped checks and reproduction pass.
No new source, world experiment or measurement was needed. Continue remaining
provider/family boundaries; do not re-inventory these BetterEnd inputs.

```sh
uv run pytest -q tests/item8/test_betterend_feature_candidates.py tests/item8/test_family_decisions.py
uv run pytest -q tests/item8/test_betterend_feature_candidates.py
uv run ruff check tests/item8/test_betterend_feature_candidates.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_betterend_feature_candidates.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-betterend-registry-roles-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-betterend-registry-roles-r2.json
```


## Tree membership decisions, 2026-09-06

The three previously named tree boundaries are now resolved in
family-decisions.json and reproduced in inventory.json. Aether holiday_tree is
vegetation with scattered snow/presents. Deep Aether fallen_tree has two
log/mushroom configurations. Regions Unexplored fallen_tree has six configured
variants and eight placed variants. Each contribution has an empty additional
family list with its rationale and preserved source identities. These are
membership decisions based on complete supplied forms, not exclusions based
only on feature type or file names.

Aether seasonal eligibility and present reward relevance remain explicit.
Regions Unexplored can produce a stump without the full fallen log. Neither
exclusion claims disabled generation or successful observed placement. No
registry root was removed. The Ashen template remains a trial-chamber component.
These decisions supersede the open tree membership boundaries in earlier dated
entries. Provider coverage stays 90 resolved and 46 open.

Validation uses the existing three candidate test files and source bindings:

```sh
uv run pytest -q tests/item8/test_aether_cloud_source.py tests/item8/test_deep_aether_candidates.py tests/item8/test_regions_unexplored_candidates.py
uv run ruff check tests/item8/test_aether_cloud_source.py tests/item8/test_deep_aether_candidates.py tests/item8/test_regions_unexplored_candidates.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_aether_cloud_source.py tests/item8/test_deep_aether_candidates.py tests/item8/test_regions_unexplored_candidates.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-tree-boundaries-r1.json
cmp evidence/raw/item8/inventory-tree-boundaries-r1.json evidence/item-8/inventory.json
```

Eleven focused cases and scoped quality checks pass. The initial test assertions
had redundant sorting and incomplete typing; these were corrected without
changing the membership decisions or source captures. Inventory status remains
INCOMPLETE. No additional evidence class or measurement system was introduced.


## Quark canonical membership, 2026-09-06

Quark contributes four canonical families: spiral_spire, fairy_ring,
monster_box and nether_obsidian_spike. The spire is one recognizable landmark;
the ring and associated buried ore are one marker/reward design; the monster box
is one authored proximity encounter; ordinary and large Nether spikes are one
shape family with the large spawner/chest encounter variant preserved explicitly.
No Quark runtime structure root duplicates these nonregistry contributions.

The prior fallen_log family inclusion is corrected to decorated vegetation,
consistent with the other fallen-tree decisions. Its generated form is a short
trunk with optional moss, vines and ferns. Hollow block substitution does not
compose a separate site. The previous geometry, conditions and uncertainty are
preserved under excluded_design. This corrects membership without erasing the
original source-derived details. Terrain styles, stone generation and other
vegetation remain excluded contributions. Their source evidence is reused.

This resolves the five previously named Quark candidate boundaries as four
families and one excluded vegetation candidate. Provider coverage stays 90 of
136. Detailed effective attributes and observations remain open. The earlier
provider-wide open scope strings do not override this membership decision.
No source capture, runtime experiment or measurement system was added.

```sh
uv run pytest -q tests/item8/test_quark_provider_scope.py
uv run ruff check tests/item8/test_quark_provider_scope.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_quark_provider_scope.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-quark-membership-r1.json
cmp evidence/raw/item8/inventory-quark-membership-r1.json evidence/item-8/inventory.json
```

Two focused cases, scoped quality checks and inventory reproduction pass.


## Supplementaries cave-cache membership, 2026-09-06

The freestanding cave urn patch is one canonical family,
supplementaries:cave_urn_cache. Its form is a group of authored treasure vessels,
generated independently of a building or vegetation feature. Random positions,
partial placement and repeated urn blocks are variants of the same cache design.
The existing galleon urn pool consumes that same urns_patch as a ship component;
it does not add another family. Road-sign feature/root reconciliation remains
unchanged. This settles the named cache-versus-decoration membership question.

The existing packaged-data test now binds the galleon reuse and both membership
dispositions as well as the freestanding modifier/placed/configured chain.
Configured tries and repetitions are not observed urn counts. The treasure=true
state is not proof of actual rewards or placement success. Effective eligibility,
reward behavior and other required attributes remain open. Provider coverage
stays 90 resolved, 46 open. No source recapture or runtime measurement was added.

```sh
uv run pytest -q tests/item8/test_supplementaries_provider_scope.py
uv run ruff check tests/item8/test_supplementaries_provider_scope.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_supplementaries_provider_scope.py tools/build_item8_inventory.py
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-cave-urn-membership-r1.json
cmp evidence/raw/item8/inventory-cave-urn-membership-r1.json evidence/item-8/inventory.json
```

Eight focused cases and scoped checks pass. The initial lint pass flagged the
expanded single component-chain test's statement count. A local PLR0915 waiver
keeps the related artifact join together without introducing a test helper.


## Fabric loot, recipe and game-rule membership resolved, 2026-09-06

Four existing module rows are closed using entry captures from 568d72c and
initializer source 0f9b272 (extractor fa3226d). No additional source capture or
runtime experiment was needed. The two parked initializer manifests and outputs
match their existing independent r1 reproductions exactly.

Game-rule API has an empty generated entry, five common rule-map/category/
command mixins and three client rule-editing hooks. Loot v2 has two legacy
builder-interface hooks; its initializer forwards v3 replace/modify/all-loaded
events to v2 consumers. Loot v3 has an empty entry and six provenance, reload,
builder and accessor hooks operating on consumer-supplied loot. Recipe API has
two ingredient mixins and two initializers registering five ingredient
serializers and the NeoForge ingredient wrapper. These are support roles with
no independent structure contribution. Consumer-specific loot effects remain
required family-attribute inputs, not new families of this library.

The existing test binds every declared common hook and sole annotated loader,
all three initializer classes, exact archive/class/disassembly identities and
complete payload partitions. Class counts are 27, 14, 17 and 27 respectively.
Nonclass payloads are the exact metadata, icons, mixin files and applicable
access transformers. Recipe's declared relative mixin names contain dots; the
existing package/name join now resolves these to class paths. No new validator
or generalized helper was added.

Fabric now has 25 resolved and 18 open modules out of 43. Whole-provider coverage
remains 90 resolved, 46 open; no family was added or removed in this increment.
The queue above is updated in place. Twenty-six focused cases and scoped Ruff
and Basedpyright pass:

```sh
uv run pytest -q tests/item8/test_fabric_provider_scope.py
uv run ruff check tests/item8/test_fabric_provider_scope.py
uv run basedpyright tests/item8/test_fabric_provider_scope.py
```


## Fabric entity-event membership resolved, 2026-09-06

Source 9402ecf (extractor a2c1e65) binds the empty generated loader, annotated
EntityEventHooks and all nine declared common mixins. They forward existing
entity damage/death/combat/conversion, player respawn/join/leave, dimension
changes, sleeping and elytra decisions to consumer events. Their bed position/
state and flight changes concern existing entities. No independent structure
contribution is introduced. Consumer behavior remains attributable separately.

The module's complete payload is 47 classes and five metadata/icon/mixin files,
with no client/server-only mixin file, plugin, data resource or nested archive.
The existing test binds both annotated classes, all nine common hooks and every
archive/class/disassembly hash. Independent r1 reproduction matches exactly.
Twenty-seven Fabric cases and scoped Ruff/Basedpyright pass using the existing
commands above. Fabric now has 26 resolved and 17 open modules; overall providers
remain 90 resolved and 46 open. No family count changes in this increment.

Command source 0224278 and lifecycle source 4de41d1 are also delivered and
independently reproduced, but their modules remain open. The exact next calls
are org/sinytra/fabric/command_api/FabricCommandApiV2.onInitialize and
net/fabricmc/fabric/impl/event/lifecycle/LifecycleEventsImpl.onInitialize.
Reuse their existing selector, seven lifecycle hooks and guarded client-entry
findings. Do not repeat collection of the 21 captured classes.

Initial extraction stopped at argument parsing because the nested archive
allowlist was incomplete; a2c1e65 fixes the exact three archive selections and
hash bindings. No failed capture was represented as accepted source evidence.
No runtime experiment or measurement system was added.

### Fabric command and lifecycle membership resolved

Sources 703f0ac and 353d68f complete the two named initializer boundaries.
Command registration consumes caller-supplied argument maps, initially empty,
and forwards command registration callbacks. The existing selector hook manages
caller-defined flags. Lifecycle initialization forwards events for existing
servers, worlds, chunks, entities and tags. CHUNK_GENERATE reports a new chunk;
it does not create it. Unload processing enumerates existing loaded objects.
WorldMixin maintains the loaded-chunk set. Neither module adds a family.

The existing test binds both source manifests to exact nested archive/class
bytes, accounts for all 16 command and 73 lifecycle classes and all metadata,
and includes the lifecycle server-only WorldChunkMixin. Separate client hook
counts are one and five; client initialization is guarded. Independent source
reproduction is recorded in each source README. Validation:

```sh
uv run pytest -q tests/item8/test_fabric_provider_scope.py
uv run ruff check tests/item8/test_fabric_provider_scope.py
uv run basedpyright tests/item8/test_fabric_provider_scope.py
```

All 29 cases and scoped checks pass. Fabric: 28 resolved modules, 15 open.
Whole providers: 90 resolved, 46 open. No family-list change. Continue the
remaining named module and provider roles, then outstanding canonical grouping;
do not repeat these completed initializer paths or resume detailed attributes.

### Fabric item-group membership resolved

Source 07cd09b binds the empty generated initializer and ItemGroupMixin.
The latter forwards consumer callbacks for creative-tab display and search
collections. The complete payload comprises fifteen classes, ordinary loader
metadata, an access transformer, common and client mixin declarations, an icon,
29 translations and the creative-menu button texture. The sole automatic entry
is captured; the sole common hook and sole client hook are accounted for.
These contributions introduce no generated family.

All 30 cases in tests/item8/test_fabric_provider_scope.py pass. Scoped Ruff and
Basedpyright pass after correcting an initial literal-list lint finding. Reuse
the validation commands above. Fabric now has 29 resolved modules and 14 open;
whole providers remain 90 resolved and 46 open. No family-list change.

Sources 2cbd452 (content registries, sixteen classes), a17da36 (data attachment,
six classes) and 36951e9 (data generation, eleven classes) are also delivered.
Their manifests and every disassembly reproduce byte for byte with commands in
the respective READMEs. Their membership rows stay open pending contribution
roles and payload bindings. Data attachment specifically calls the uncaptured
AttachmentEntrypoint.onInitialize. Do not repeat these delivered entry captures.

### Fabric content registries and data generation membership resolved

Content registry source 2cbd452 has an empty generated initializer, automatic
fuel and hoe-tool subscribers and thirteen common hooks. These expose or adjust
existing tool transformations, villager food/gift collections, brewing recipes,
fire properties, waxing/oxidation maps and pathfinding types. Fuel and tilling
operate on caller registrations and existing item/block interactions. The generic
BaseRegistryMixin delegate is bounded by source e5c769a: only compostability and
raid-hero gift lookups are modified. Neither branch generates a site.

Data-generation source 36951e9 has an empty initializer and ten common hooks.
They adapt data output paths, JSON key order, consumer model generation and
namespace filtering, loot-provider access and recipe output identifiers. These
are pack-authoring services with no independent world-generation entry. The
remaining implementation types are the associated output/provider APIs.

The existing source-binding test accounts for all 39 content-registry classes
and 53 data-generation classes, exact automatic entries, declared hooks and
complete metadata/resource sets. Both archives have an access transformer and
no client-only hook file or generation data payload. All 32 focused Fabric cases,
scoped Ruff and Basedpyright pass using the commands above. Fabric now has 31
resolved modules and 12 open. Whole providers remain 90 resolved and 46 open.
No family-list change and no new measurement system.

Attachment initializer source db84f92 reproduces exactly and copies existing
attachment values on respawn, dimension change and conversion. Its registration
callback in AttachmentModImpl remains unresolved; the module stays open. Reuse
the existing entry and initializer captures when resolving that callback.

### Fabric data attachment membership resolved

Source e6aa022 resolves AttachmentModImpl's invokedynamic callback to
AttachmentRegistryImpl.registerNeoTypes. It registers entries from an initially
empty map. Public registration takes caller-supplied IDs and attachment types,
either deferred or directly in NeoForge ATTACHMENT_TYPES. Type translation,
serialization access and transfer operate on existing attachment holders.
Source db84f92 binds transfer on respawn, dimension changes and mob conversion.
No default site or independent world-generation route is introduced.

The older nonverbose source remains preserved. The new verbose source is needed
to expose the previously unresolved callback target, not a new evidence system.
Both manifests reproduce independently with commands in their READMEs. The
existing test binds all three captures, all twenty classes, both automatic
entries, four common access hooks, one client hook and the complete resource
set including one translation. The client initializer is guarded.

All 33 focused Fabric cases, scoped Ruff and Basedpyright pass. An initial test
complexity failure was corrected by using the existing source table for multiple
captures and the existing resource set for the translation. No helper or new
validator was introduced. Fabric: 32 resolved modules, 11 open. Whole providers:
90 resolved, 46 open. No family-list change. Continue remaining named modules
and provider membership; do not reopen attachment internals without a concrete
contradiction or resume detailed family attributes before membership is frozen.

### Fabric message, screen handler and rendering membership resolved

Sources 1e30004 and c5ebd6e preserve empty message/screen-handler initializers
and both common hooks per module. Message hooks decorate chat and forward
allow/notification callbacks for chat, game and command messages. Screen hooks
expose menu-close policy and encode supplied extended menu-opening data. Neither
provides a generated site. Source 2e5d280 shows rendering initialization guarded
by Dist.isClient; all fifteen declared rendering hooks are client-only.

The existing tests bind the exact archives, class/disassembly identities, full
payloads and automatic entries: message has 32 classes and two client hooks;
screen handler has nine classes and an access transformer; rendering has 73
classes and fifteen client hooks. Other resources are exact loader metadata,
icons and hook declarations. There is no generation-data payload. All 36 focused
Fabric cases, scoped Ruff and Basedpyright pass using the commands above.
Fabric: 35 resolved modules, eight open. Whole providers: 90 resolved, 46 open.
No family-list change.

Resource-condition source 969f1bb is delivered with independent byte-identical
reproduction. Its initializer and ten data-loading hooks still require semantic
reconciliation. Keep that module open; the other three dispositions do not prove
resource-condition behavior. Reuse the delivered capture instead of recapturing.

### Fabric resource-condition membership resolved

Source 969f1bb binds the generated initializer and ten loading hooks. Source
abcf742 resolves the initializer/evaluation and overlay delegates. Initialization
registers nine predicate types. The loader hooks filter supplied JSON resources,
retain registry/tag/feature context, and append consumer-declared overlays whose
conditions pass. They do not contribute an authored layout or independent site.
The module's remaining types are condition API/codecs, predicate implementations
and overlay records. The full payload has 31 classes, an access transformer,
loader metadata, one icon and the common mixin declaration, with no generation
resources or additional executable entry. The existing test binds this payload,
all automatic/common entries and both source manifests to the frozen archive.

All 37 focused Fabric cases, scoped Ruff and Basedpyright pass using the commands
above. Both delegate disassemblies independently reproduce byte for byte. No new
measurement system was added. Effective consumer conditions remain part of each
family's eligibility evidence; this membership disposition does not assert they
pass. Fabric now has 36 resolved modules and seven open. Whole providers remain
90 resolved and 46 open. No family-list change. Continue the remaining named
module/provider checks and canonical grouping before detailed attributes.

### Fabric object-builder membership resolved

Source 0fa369a preserves the empty initializer and eleven common hooks. They
expose block properties, extend supplied entity/block-entity builders and type
collections, copy existing attribute maps, forward comparator calculations for
existing minecarts, handle nullable saved-data fix types and suppress empty
trade results. These hooks and the caller-facing builder APIs do not introduce
an independent authored layout. The module contains no packaged generation data.

The existing test binds all 44 classes, the sole automatic entry, eleven hooks,
access transformer and exact metadata/icon payload. Its declared mixin filename
is fabric-object-builder-v1.mixins.json, without the archive name's api segment;
that exact difference is now accounted for in the existing path. All 38 focused
Fabric cases and scoped Ruff/Basedpyright pass using the commands above.
Fabric: 37 resolved modules, six open. Whole providers: 90 resolved, 46 open.
No family-list change.

Interaction source e030cd8 and item source 4ddacfa are delivered and independently
reproduce byte for byte. They remain open at InteractionEventsRouter.onInitialize
and the item RegistryLoaderMixin's EnchantmentUtil delegate respectively. Reuse
their other entry/hook captures. These are named remaining calls, not completed
provider dispositions or permission to audit unrelated gameplay internals.

### Fabric interaction and item membership resolved

Interaction source 5147b43 resolves the router called by e030cd8. Initialization
registers block-attack and cancelled-break handlers. They forward existing block
interactions and resend existing block states to the player. The other captured
hooks forward player/entity/block use and attack, break and advancement events.
The guarded client initializer and three client hooks do not add server content.

Item source 41d9c83 resolves the loading delegate in 4ddacfa. It copies a supplied
enchantment, invokes its modification callback and rebuilds the same entry, with
source classification for vanilla, mod and data-pack inputs. Other captured
hooks support components, equipment slots, durability, recipe remainders,
enchantment acceptance and tooltips. The generated initializer is empty. These
modules supply no independent authored site or packaged generation resources.

The existing test binds complete payloads of 36 interaction and 43 item classes,
all automatic entries, two and thirteen common hooks respectively, and three and
one client hooks. Both exact resource sets contain loader metadata, icons and
mixin declarations. The delegate sources independently reproduce byte for byte.
All 40 focused Fabric cases, scoped Ruff and Basedpyright pass using the commands
above. Fabric now has 39 resolved modules and four open: networking, registry
sync, transfer and loader. Whole providers remain 90 resolved and 46 open.
No family-list change. Continue those four checks, then the other provider and
canonical grouping decisions; do not repeat the resolved interaction/item paths.

### Fabric transfer membership resolved

Source 94eaafd preserves the empty generated initializer, automatic capability
adapter and ten common hooks. The adapter registers item/fluid handlers against
existing block and block-entity types and installs caller storage lookup
fallbacks. Its recursion guard and wrapper constructors operate on supplied
capabilities. Hooks adapt existing container mutation, furnace cooking state,
jukebox items, cached item/fluid variants and fluid sounds. No independent
world-generation or authored-site route is introduced. The remaining APIs and
implementation classes provide storage views, transactions, variants and wrappers.

The existing test binds all 120 classes, both automatic entries, all ten hooks
and the complete metadata/icon/mixin payload. No generation data, client mixin
file or access transformer exists in this module. All 41 focused Fabric cases
and scoped Ruff/Basedpyright pass using the commands above. The source capture
independently reproduces byte for byte. Fabric: 40 resolved, three open. Whole
providers: 90 resolved, 46 open. No family-list change.

The last three entry captures are also delivered and reproduced: networking
ad9fbe2 (seventeen classes), registry sync 4bc3d16 (six classes), loader 1cb6fe0
(one language-loader service). Networking requires interpretation of its existing
hooks; registry sync calls FabricRegistryInit.onInitialize; the loader service
installs FabricLoaderBootstrap. Those named boundaries remain open. Reuse the
captures, then close the Fabric provider only after all three are resolved.

### Fabric networking membership resolved

Existing source ad9fbe2 preserves the empty generated initializer, automatic
networking events and all fifteen common hooks. These implement packet codecs,
channel negotiation, login/configuration task handling, connection lifecycle
callbacks and existing-entity tracking callbacks. Event hooks forward player
readiness and configuration events and conditionally expose the development
debug command. They do not supply an authored site, placement rule or world
generation registration. No further packet-helper tracing is needed for this
family-membership boundary.

The existing focused test binds all 129 classes, both automatic entries, all
fifteen common hooks, eight client hooks and the complete metadata/icon/access
transformer payload. The whole Fabric data check already accounts for every
nested module's generation resources. The source was independently reproduced
in ad9fbe2; no new capture or runtime measurement was needed.

All 42 Fabric cases and scoped Ruff/Basedpyright pass. Fabric: 41 resolved, two
open (registry sync and loader). Whole providers: 90 resolved, 46 open. This
closes a module disposition, adds no family and does not establish the final
family count.

### Fabric registry membership resolved

The six entry/hook classes in 4bc3d16 expose registry accessors and forward
existing registry setup callbacks. Initializer e5a03ee registers the datapack
registry callback. Delegate 7b86b55 stores caller-supplied keys/codecs in an
initially empty list and submits precisely those registrations to NeoForge.
Its duplicate-key set starts with vanilla registry keys; it creates no authored
site or independent feature. Registry entry callbacks likewise forward supplied
entries. This resolves the concrete startup question without further tracing.

The existing test binds the three captures, all 26 module classes, the one
automatic entry, five common hooks, 22 translation resources and complete
metadata/icon/access-transformer payload. There is no client mixin file or
generation data. All 43 focused Fabric cases and scoped Ruff/Basedpyright pass.
Fabric: 42 resolved, one open (loader). Whole providers: 90 resolved, 46 open.
No canonical family is added.

### Fabric loader and whole-provider membership resolved

The declared loader service (1cb6fe0) installs the launch bootstrap (4beaa6b).
The bootstrap handles no class transformation phases and forwards the existing
FML mod list. The delegate (6a6fcc4) wraps those existing metadata records,
indexes their IDs and provided aliases, rejects duplicate IDs and sets the
loaded flag. It supplies no generation resource, structure design or placement
registration. Remaining loader APIs concern mod metadata, entrypoint consumers,
mappings and language/loader utilities; no independent content is introduced.

The focused test binds all three sources, all 785 classes, the sole service,
LIBRARY manifest and all sixteen non-class resources. There are no automatic
Mod/EventBusSubscriber annotations, mixin declarations, nested JARs, templates
or data resources in this module. All 44 Fabric cases and scoped Ruff and
Basedpyright pass. All 43 nested modules now have supported dispositions; the
parent payload and nested generation-data accounting are already verified by
the existing test. Fabric contributes consumer APIs and modifiers, conventional
tags and the explicitly test-only empty template, with no independent family.

Whole providers: 91 resolved, 45 open. The remaining provider rows are the
existing 24 code-reference and 21 unmatched-search rows. These lanes are planning
inputs, not absence proofs. Canonical Moog grouping remains open independently.
No family count changes in this increment. Do not reopen Fabric internals
without a concrete contradictory generation or component finding.

### WunderLib membership resolved

Source 185b55c preserves both automatic entry classes and the single indexed
structure-reference class. The common entry installs networking payload handlers,
the client entry installs network adapters, and Bounds converts supplied numeric
extrema into a BoundingBox. Other Bounds methods perform geometry, interpolation
and serialization. This is a shared math/UI/network library without an independent
authored design or generation registration. The bounding-box reference is fully
explained; no generic geometry or network helper audit is needed.

The small-utility test binds the pinned archive, all 142 classes, both automatic
entries and the complete four-file non-class payload. Only the plain manifest,
NeoForge mod metadata, icon and license accompany the classes. There are no
mixins, service declarations, nested modules, templates or generation data.
Nineteen small-utility cases and scoped Basedpyright pass; the sole initial Ruff
finding was a long assertion, corrected before the passing scoped Ruff run.
The source independently reproduces byte for byte.

Whole providers: 92 resolved, 44 open (23 code-reference and 21 unmatched-search
rows). No family added or grouping changed. Continue remaining contribution
boundaries and Moog grouping before attributes.

### MCA membership resolved

Source 28273db retains the two automatic NeoForge entries, all 21 common
mixins and all six indexed structure-reference classes (MixinProtoChunk is
both a common hook and an indexed reference). Registration targets items,
blocks, sounds, particles, entities, AI types, professions, components,
advancement triggers, block entities and the creative tab. Reload listeners
consume dialogue, names, gifts, appearance, tasks and building-type rules.
No independent structure or feature registration occurs in these entry paths.

WorldUtils looks up supplied IDs/tags in the existing structure registry and
calls findNearestMapStructure. DestinyMessage locates such an existing site,
loads its destination chunk and changes player/spawn position. BlockBoxExtended
is geometry. Village and VillageManager maintain saved village membership,
bounds, population, building records and reputation. Their world tick processes
reported buildings and entity encounters, including bounty hunters and Reaper
state. These records are not new world-generation roots.

Source bd25ce8 resolves the concrete building question. All 26 building_types
JSON documents are recognition rules: block/tag counts, priority, map display,
boundary margin and grouping properties. BuildingTypes loads those rules;
Building validates existing block states and records coordinates. Its addBlock
method updates the recorded map, not the world. No template, authored layout or
placement is encoded by those documents. Thus inn, graveyard, library and the
other recognition labels must not be counted as independently generated families.

The remaining common hooks adapt existing villager/zombie types and professions,
entity insertion, chat, riding, milk effects, baby-item handling, furnace
advancements, translation and particle/AI constructors. Flint-and-steel/Reaper
and goat-triggered entity behavior remain encounter inputs, not independent
generated structures. Villager replacements, bounty hunters, loot and other
MCA effects still require attribution in relevant family attributes; this
membership disposition does not claim those effects are absent or fully audited.

The focused test binds the archive and both source manifests, accounts for all
543 classes, 2,034 assets, 770 data resources and seven remaining metadata/icon/
license files, and checks every recognition definition against its observed
fields and positive block counts. It binds both automatic entries, all 21 common
hooks and eight declared client hooks. There are no nested JARs or NBT templates;
the complete data categories contain no generation definitions. Both source
captures independently reproduce byte for byte.

```sh
uv run pytest -q tests/item8/test_mca_provider_scope.py
uv run ruff check tests/item8/test_mca_provider_scope.py
uv run basedpyright tests/item8/test_mca_provider_scope.py
```

One focused case and both scoped quality checks pass. Whole providers: 93
resolved, 43 open (22 code-reference and 21 unmatched-search rows). No family
added. Continue the remaining providers and canonical Moog grouping.

### Integrated API membership resolved

Source 88a0f54 retains initialization, the datagen entry and all 27 common
hooks. The common initializer registers rule-test, position-test, structure-type,
placement-modifier, processor, piece, pool-element, structure-placement and
condition registries. These are consumer codecs/types, not independent authored
structure definitions. Existing pool-codecs evidence for IAStructurePieces and
IASinglePoolElement is reused. The setup callback is empty. Server lifecycle
callbacks set the server reference and manage existing-structure lookup services.

The actual common hooks have bounded roles: structure-block and jigsaw size
limits, pool weight-codec range, terrain blending for supplied structure starts,
tag-based suppression, feature suppression inside existing starts, lookup radius
and disabled-tag handling, accessors and logging for block-attached entities.
StructurePoolMixin raises the permitted weight range; it is not a pool-content
injection. The datagen entry writes converted consumer NBT during data generation.
Neither is an independent family. Other shared placement, processor and jigsaw
implementations serve consuming registered definitions and their components.

Reload listeners consume spawner definitions, map trades, piece-count limits and
workstation rules. Those inputs remain part of family mob, loot, placement and
component attribution. The membership disposition does not close effective
consumer configuration, missing components or runtime attribute uncertainties.

The complete packaged data is 48 biome collection tags and three empty control
tags (skippable_features, disabled_structures and unskippable_structures). Other
packs may extend those tags, so their packaged emptiness is not an effective
runtime suppression claim. No structure definitions, templates, configured
features or independent layouts are packaged. The complete payload comprises
206 classes, 51 tag files, one icon and seven metadata/configuration files.
There are no nested archives or services. The focused check binds the original
archive, all 30 captured classes, both automatic entries, both mixin declarations,
all 27 common hooks and two declared client hooks. Source reproduction is exact.

```sh
uv run pytest -q tests/item8/test_integrated_api_provider_scope.py
uv run ruff check tests/item8/test_integrated_api_provider_scope.py
uv run basedpyright tests/item8/test_integrated_api_provider_scope.py
```

One focused case and both scoped quality checks pass. Whole providers: 94
resolved, 42 open (21 code-reference and 21 unmatched-search rows). No canonical
family added or grouping changed. Continue those providers and Moog grouping;
do not audit clean generic codec helpers without a concrete family boundary.

### GlitchCore membership resolved

Source a447496 preserves twelve automatic entries and all eight common hooks.
The entries forward consumer events for registration, commands, trades, ticks,
tags, item/block interaction, tools, colors, particles, rendering and tooltips.
The mixins adapt existing item use, player joins, configuration tasks, platform
queries, networking and rendering. They provide no authored site or independent
placement route. Source a2fc4ee resolves the remaining common startup callback:
GlitchCore.init registers only its sync_config packet. Static initialization
creates the logger, channel and packet handler. No further networking helper
inspection is required for family membership.

The focused test binds both source manifests, all 80 classes, twelve automatic
entries, eight common hooks, four client hooks and the complete nine-file
non-class payload. Only metadata, access declarations, mixin configurations,
icons and pack metadata accompany code. There are no generation data files,
templates, nested archives or services. Both source captures independently
reproduce byte for byte. Consumer event effects remain attributable to their
providers; this shared library introduces no independent family.

```sh
uv run pytest -q tests/item8/test_glitchcore_provider_scope.py
uv run ruff check tests/item8/test_glitchcore_provider_scope.py
uv run basedpyright tests/item8/test_glitchcore_provider_scope.py
```

One focused case and scoped Ruff pass. An initial Basedpyright finding for
untyped TOML declarations was fixed with the existing explicit type pattern;
Basedpyright then passes. Whole providers: 95 resolved, 41 open (21 code-reference
and 20 unmatched-search rows). No family count change. Continue remaining
provider contribution boundaries and canonical Moog grouping.

### TerraBlender membership resolved

Sources 3230f7ff and c2de78c1 preserve common/NeoForge entry, the startup
handler, all ten common hooks and the server-start biome initializer. The
initializer enumerates existing dimension stems, reads their generators and
world seed, appends consumer biome entries, initializes region parameter maps
and chooses surface-rule categories. It does not define or place authored sites.

Hooks modify multi-noise and End biome selection, deferred biome lists, noise
settings and namespaced surface-rule composition. Registry bootstrap adds the
merged material-rule codec. The remaining classes supply biome-region APIs,
surface-rule wrappers, weighted noise and configuration support. These are
terrain and consumer eligibility roles, not independent structure families.

Preserve two implementation limitations: MixinChunkGenerator cancels the
vanilla validate hook, and MixinPrimaryLevelData returns a stable lifecycle.
Those changes cannot serve as compatibility acceptance evidence. They do not
add an authored family or justify reopening accepted empirical world evidence
without a concrete contradiction. Effective biome and surface effects remain
relevant to consuming family attributes.

The complete packaged data contains two dimension-type tags selecting vanilla
Overworld/Nether types and one deferred_placeholder biome with empty features,
carvers and all mob-spawn lists. No template, structure definition, configured
feature or independent content route is present. The focused check binds all
63 classes, the sole automatic entry, ten common and one client hook, both
mixin declarations and all twenty non-class files (data, translations, metadata,
access declarations and images). No nested archives or services occur. Both
source captures independently reproduce byte for byte.

```sh
uv run pytest -q tests/item8/test_terrablender_provider_scope.py
uv run ruff check tests/item8/test_terrablender_provider_scope.py
uv run basedpyright tests/item8/test_terrablender_provider_scope.py
```

One focused case and Basedpyright pass. An overlong assertion was corrected
before the passing Ruff run. Whole providers: 96 resolved, 40 open (20
code-reference and 20 unmatched-search rows). No family added. Continue
remaining provider boundaries and canonical Moog grouping before attributes.

### Prickle and Resourceful Config membership resolved

Prickle sources eb9670dc and 4e7468fb cover the loader, both declared services
and common initializer. Initialization verifies platform availability and rejects
repeat initialization. Services provide configuration property adapters and the
platform configuration path. Both mixin lists are empty. Complete payload
accounting binds 47 classes and nine non-class files; no generation data,
templates or nested archives occur. No independent family is contributed.

Resourceful Config source b335f9e8 covers the loader, declared parser service
and all three common mixin accessors. The parser reads caller-supplied annotated
configuration classes. The accessors expose server settings and the player
limit. Startup initializes configuration compatibility and a web configuration
interface, and stores the started server reference. This is an operational role;
network exposure was not tested by this membership inspection. The complete
payload has 186 classes, 35 interface/language assets and five other files.
No generation data, templates or nested archives occur. No independent family
is contributed. Configuration effects on consumers remain separate attributes.

The existing captures reproduce independently as recorded in their source
README files. The focused test binds archive hashes, complete payloads, automatic
entries, common hooks, declared services and all captured disassembly identities.
No further generic configuration helper tracing is needed for membership.

```sh
uv run pytest -q tests/item8/test_config_library_provider_scope.py
uv run ruff check tests/item8/test_config_library_provider_scope.py
uv run basedpyright tests/item8/test_config_library_provider_scope.py
```

Two cases and scoped quality checks pass. The initial seven-argument test
signature exceeded the existing Ruff limit; grouping the archive identity into
one tuple fixes that finding. Whole providers: 98 resolved, 38 open. This closes
two unmatched-search rows, leaving 20 code-reference and 18 unmatched-search
rows. Canonical Moog grouping remains open; no family count changed here.

### Target dummy membership resolved

Source 51ba791c binds the NeoForge entry, common initialization, all six common
mixins, event callbacks and item/dispenser placement. Initialization registers
one target-dummy entity/item, particles, entity attributes, configuration,
client messages and dispenser behavior. Item use checks the placement space,
removes replaceable blocks and creates the dummy at the selected location.
Dispensing creates the same entity adjacent to the dispenser. Neither path
defines a generated site or a structure family.

The common hooks implement armor-stand head rotation, dummy-specific enchantment
applicability, damage/healing reporting and tool/sword wear behavior. Registered
events handle critical hits, natural-spawn cancellation near eligible scarecrows
and scarecrow/decoy goals on existing mobs. Preserve these mob effects for
encounter attribution; no claim of absent gameplay impact or measured activation
is made. The source supports no independent authored world-generation family.

The complete archive contains 45 classes, 28 visual/language assets, fifteen
crafting/damage-type/tag data files and eight metadata/mixin/access files.
There are no structures, templates, generation data, services or nested archives.
The sole automatic entry and both declared mixin configurations are bound by
the existing utility-provider test. All eleven disassemblies reproduce exactly.
No further dummy combat or generic library implementation audit is required.

```sh
uv run pytest -q tests/item8/test_small_utility_provider_scope.py
uv run ruff check tests/item8/test_small_utility_provider_scope.py
uv run basedpyright tests/item8/test_small_utility_provider_scope.py
```

Twenty focused cases and scoped quality checks pass. Whole providers: 99
resolved, 37 open (20 code-reference, 17 unmatched-search). No family added.
Continue the remaining provider contribution checks and Moog grouping before
attributes. These are membership checks, not a new gameplay measurement system.

### EMI Ores membership resolved

Source 824f34de covers both entries, common initialization, platform helper,
datapack synchronization and all thirteen common mixins. The common initializer
is empty. NeoForge registers two client-bound payloads and a datapack-sync
listener. The listener enumerates existing placed features and biome generation
settings, selects ore/geode configurations and sends their information to clients.
Its new PlacedFeature objects contain filtered placement modifiers for the
outgoing information map. They are not registered or placed into a world.

All common mixins are abstract accessor methods exposing existing generation
parameters: block/state tests, probabilities, counts, height providers, rarity,
state lists and tags. There are no injected generation methods. The platform
helper only returns the configuration path. The client entry initializes its
information display and clears received feature data on logout. There is no
independent structure-family contribution. This display's filtered information
is not a substitute for effective-generation or pacing evidence.

The complete payload binds 33 classes, 72 language/interface/texture assets
and five metadata/mixin files. No data pack, template, service or nested archive
occurs. Two automatic entries and the single mixin declaration are accounted
for. The eighteen captured sources reproduce byte for byte. The existing utility
test binds the complete payload, entries, accessors and disassembly identities.
No further client rendering or serialization audit is needed for membership.

```sh
uv run pytest -q tests/item8/test_small_utility_provider_scope.py
uv run ruff check tests/item8/test_small_utility_provider_scope.py
uv run basedpyright tests/item8/test_small_utility_provider_scope.py
```

Twenty-one cases and scoped quality checks pass. Whole providers: 100 resolved,
36 open (19 code-reference, 17 unmatched-search). No family added. Continue the
remaining provider checks and canonical Moog grouping before detailed attributes.

### Player Animator membership resolved

Source d1d22f75 retains the sole automatic mod entry and declared mixin plugin.
The entry is explicitly annotated Dist.CLIENT. It registers client animation
resource reload and rendering compatibility setup. The plugin has empty load,
pre/post-apply and target callbacks, returns no additional mixins, and filters
bend-only client hooks using the existing animation capability check.

The complete archive has 127 classes and five metadata/access/mixin files.
There are no data, assets, templates, services or nested archives. The single
mixin declaration contains seventeen client hooks and no common/server hooks.
The focused utility case binds the archive, complete payload, automatic-entry
set, side annotation, mixin declaration and both source identities. Independent
source reproduction matches byte for byte. No independent family is contributed.
Client rendering implementation need not be traced for this dedicated-server
family membership decision.

```sh
uv run pytest -q tests/item8/test_small_utility_provider_scope.py
uv run ruff check tests/item8/test_small_utility_provider_scope.py
uv run basedpyright tests/item8/test_small_utility_provider_scope.py
```

Twenty-two cases and scoped quality checks pass. Whole providers: 101 resolved,
35 open. No family added; remaining provider checks and canonical Moog grouping
precede detailed family attributes.

### AzureLib Armor membership resolved

Sources a37e5b08 and 57ea6b5c bind the loader, common initialization, three
services, two common hooks and direct entry delegates. The loader registers
an item identity data component and an animation-command packet. Services
supply platform lookups, packet delivery and client-conditional animation
resource reload. The unconditional Shoulder Surfing compatibility initializer
only checks mod presence and sets a flag. The packet retrieves an existing
item animator by identity and dispatches supplied animation actions to it.
Consumer actions are not independent families of this shared animation library.

The common hooks assign item identity components and handle comparison/copying
for container synchronization. Five other declared hooks are client rendering
and cache hooks. This establishes the contribution role without claiming network
safety, rendering correctness or compatibility acceptance. No independent
world-generation family is contributed.

The complete archive has 343 classes and thirteen metadata, access, service,
mixin, icon and license files. It has no data pack, assets directory, templates
or nested archives. The sole automatic entry, three declared services and all
common hooks are bound to the ten captured classes. Both captures reproduce
independently byte for byte. The focused case extends the existing utility
checks; no new measurement system or generalized validator was introduced.

```sh
uv run pytest -q tests/item8/test_small_utility_provider_scope.py
uv run ruff check tests/item8/test_small_utility_provider_scope.py
uv run basedpyright tests/item8/test_small_utility_provider_scope.py
```

Twenty-three cases and scoped quality checks pass. Whole providers: 102 resolved,
34 open. No family added. Continue the remaining provider queue and Moog
canonical grouping before attributes; no more animation-helper tracing is needed.

### GeckoLib membership resolved

Sources 1284a76a and 58568f7f cover the loader, four services, three common
hooks, constants initialization and concrete packet registration. Startup
registers the persistent/synchronized item animation ID data component and
fifteen client-bound animation data, trigger, stop and stateless-animation
packets. The constants init method itself is empty. Client initialization is
side-conditional. No structure, feature, authored site or independent family
is registered by these entry paths.

The common hooks handle item ID removal on copies/splits and comparison during
container/equipment synchronization. Services expose consumer rendering events,
item/armor models, platform paths and packet delivery. Those are shared animation
roles. Consumer-authored world content remains attributable to the consumer.
This membership result does not assert that animation or networking correctness
has been tested, and does not require a broader serialization/rendering audit.

The complete archive has 256 classes and ten metadata, service, mixin, icon,
access and license files. No data, assets, templates or nested archives occur.
The sole automatic entry, four declared services, three common and four client
hooks are accounted for. All ten captured classes are bound to the archive and
source manifests; both captures reproduce independently byte for byte.

```sh
uv run pytest -q tests/item8/test_small_utility_provider_scope.py
uv run ruff check tests/item8/test_small_utility_provider_scope.py
uv run basedpyright tests/item8/test_small_utility_provider_scope.py
```

Twenty-four utility cases and Basedpyright pass. Ruff found one overlong line;
wrapping that assertion fixes it and Ruff passes. Whole providers: 103 resolved,
33 open. No family added. Remaining provider contributions and canonical Moog
grouping still precede detailed attributes. Do not repeat GeckoLib helper tracing.


### Chipped membership resolved

Sources 869bee77 and 9fd54ae5 bind the two automatic entries, initialization,
two common hooks and registered crafting packet handler. Startup registers
blocks/items, creative tabs, menus and recipes, plus barrel block-entity
compatibility. The client entry registers screens. Common hooks choose Chipped
block drops and nether-wart support blocks. The packet dispatches crafting in
an existing player WorkbenchMenu. No independent structure family.

The frozen archive contains 62 classes. All other files are the five declared
metadata/icon/refmap/mixin files, building-block assets and JSON tags,
advancements, recipes and loot tables. The focused case accounts for every
payload category and automatic entry, checks mixin declarations, and binds all
eight source captures to the archive. There are no nested archives or services.
Independent capture reproductions match byte for byte. This resolves membership;
block loot and crafting behavior are not a claim of absent gameplay effects.

```sh
uv run pytest -q tests/item8/test_small_utility_provider_scope.py
uv run ruff check tests/item8/test_small_utility_provider_scope.py tools/inspect_item8_pool_elements.py
uv run basedpyright tests/item8/test_small_utility_provider_scope.py tools/inspect_item8_pool_elements.py
```

25 utility cases pass. Scoped Ruff and Basedpyright pass after wrapping one
initial overlong test line. Whole providers: 104 resolved, 32 open. No family
added. Continue the remaining provider queue and canonical grouping, without
further Chipped crafting or networking inspection.


### Patchouli membership resolved

Sources c73260ac and 212a5402 cover the two automatic entries, two services,
two common recipe accessors, book initialization, lectern interaction,
network registration and multiblock roles. Startup registers book items,
sounds, data components and advancement triggers. BookRegistry loads consumer
book JSON into its book map. Server startup sends book reload information;
both registered packets are client-bound. Lectern events operate on an existing
lectern. Client entry and service support book models, displays and overlays.

MultiblockRegistry starts empty and accepts consumer definitions. The abstract
multiblock supports validation and rendering, and has an explicit caller-driven
place method that writes replaceable blocks. This is a library capability, not
an automatic world-generation registration or an independent authored family.
Do not misstate this as an inability to write blocks. No further generic book
or client helper tracing is needed for membership.

The frozen archive has 198 classes, 42 client assets, two item tags (both add
patchouli:guide_book to vanilla book tags), and seven metadata/service files.
Full payload accounting excludes unreported templates, generation data and
nested archives. The focused test binds all twelve captures and declared entry
points to the frozen archive. Independent captures reproduce byte for byte.

```sh
uv run pytest -q tests/item8/test_small_utility_provider_scope.py
uv run ruff check tests/item8/test_small_utility_provider_scope.py tools/inspect_item8_pool_elements.py
uv run basedpyright tests/item8/test_small_utility_provider_scope.py tools/inspect_item8_pool_elements.py
```

26 utility cases and scoped quality checks pass. Whole providers: 105 resolved,
31 open. No family added. Finish remaining provider contributions and canonical
Moog grouping before detailed attributes.


### Cloth Config membership resolved

Source 6e7567c7 binds the sole automatic entry. Its constructor calls the demo
mods-page registration only under Dist.isClient; the dedicated-server path
returns without registration. There are no mixin declarations, services or
nested archives. Access transformation exposes three client GUI members.
No independent generated family. Consumer config APIs do not define sites.

The focused case accounts for 633 classes, exactly 23 language files, three
GUI textures and ten metadata/license/icon/access-transformer files, including
shaded TOML/YAML library metadata. There are no data resources or structure
templates. It checks every automatic entry and binds the preserved disassembly
to the frozen archive. Independent r1 reproduction matches byte for byte.

```sh
uv run pytest -q tests/item8/test_small_utility_provider_scope.py
uv run ruff check tests/item8/test_small_utility_provider_scope.py tools/inspect_item8_pool_elements.py
uv run basedpyright tests/item8/test_small_utility_provider_scope.py tools/inspect_item8_pool_elements.py
```

27 utility cases and scoped quality checks pass. Whole providers: 106 resolved,
30 open. No family added. Do not trace further config-screen helpers; continue
remaining provider dispositions and canonical Moog grouping before attributes.


### CristelLib membership resolved

Sources 301e7486, 8cf26f9e, 70b3b9ce, 0e6adb61 and 781e1a8d bind twenty
classes covering entries, annotated plugin discovery, the built-in consumer,
resource loading/storage, set writers and the relevant conditional pack path.
The built-in API configures existing vanilla structure sets and registers the
shared CONFIG_PACK. Other consumers supply their declarations and resources.
Automatic configuration wraps existing sets. The toggle writer removes disabled
members; the placement writer changes salt, spacing, separation and frequency.
Neither adds an independent authored design. Preserve these generation effects
for effective per-family attributes; membership closure is not a no-effect claim.

Pack injection requires its supplied condition and absence from disabledPacks.
The mod_loaded codec tests the actual loaded/loading NeoForge mod list when
no version is supplied. Existing Towns and Towers evidence binds the optional
Waystones pack declaration to that condition and proves Waystones absent in the
frozen runtime. Its three replacements are therefore ineligible, not new families.
Existing Explorify and Towns and Towers resource dispositions remain their
consumer attribution; do not duplicate families under the library provider.

The full archive has 95 classes, three translations and nine other files,
including one nested Jankson archive. Jankson has 42 parser classes and two
metadata files, no loader entries, services, generation data or Minecraft code
references. The common declared mixin set has only a client pack-selection hook.
The additional packaged descriptor names a pack-root accessor; it is captured
conservatively even though it is not declared by the NeoForge metadata.
No independent family is contributed by this library or its bundled parser.

```sh
uv run pytest -q tests/item8/test_cristellib_provider_scope.py tests/item8/test_towns_towers_provider_scope.py
uv run ruff check tests/item8/test_cristellib_provider_scope.py tools/inspect_item8_pool_elements.py
uv run basedpyright tests/item8/test_cristellib_provider_scope.py tools/inspect_item8_pool_elements.py
```

Two focused cases and scoped quality checks pass. Initial Basedpyright findings
for untyped JSON variables were fixed with explicit types. Captures reproduce
byte for byte. Raw ConditionNode has a trailing blank line: the default staged whitespace
check failed, and the raw file was preserved with only blank-at-eof excluded
from that generated-evidence check. Built-in pre-selector captures are retained
as pilots; accepted source and r2 were produced after selector delivery, as
recorded in their README. No raw evidence was rewritten to pass.
Whole providers: 107 resolved, 29 open. No family added. Do not continue generic
CristelLib parser, configuration or version-comparator tracing. Finish remaining
provider roles and canonical Moog grouping before detailed attributes.


### Ranged Weapon API membership resolved

Source ac503af9 binds both entries, common initialization and all ten common
hooks. Initialization attaches ranged damage/haste effect modifiers; hooks
register attributes/effects, adjust draw timing and item attributes, and alter
arrow damage/velocity. NeoForge item-use ticking applies ranged haste. Client
entry and six client hooks support rendering and item presentation. These are
combat/item capabilities, with no generated-site registration or authored
structure design. Preserve combat effects for later encounter attribution.

The archive contains 54 classes, seven translations, three icons/textures and
four metadata/refmap/mixin files. It has no data resources, templates, services
or nested archives. The focused case accounts for every nonclass file, checks
the automatic entries/mixin declarations and binds all thirteen captures to
the frozen archive. Independent r1 reproduction matches byte for byte.

```sh
uv run pytest -q tests/item8/test_small_utility_provider_scope.py
uv run ruff check tests/item8/test_small_utility_provider_scope.py tools/inspect_item8_pool_elements.py
uv run basedpyright tests/item8/test_small_utility_provider_scope.py tools/inspect_item8_pool_elements.py
```

28 utility cases and scoped quality checks pass. The first payload assertion
omitted the ten client assets; the failing test exposed that omission, and
explicit accounting was corrected. No archive or raw source was changed.
Whole providers: 108 resolved, 28 open. No family added. Do not continue generic
weapon mechanics or damage-balance inspection; continue remaining providers
and canonical Moog grouping before detailed attributes.


### Quick Right Click membership resolved

Sources 458fa978 and 74487ac1 bind the active NeoForge entry/event path, three
common hooks and temporary placement. Item right-click dispatches held beds,
tables and storage. Temporary bed/shulker placement serves immediate player
interaction; hooks handle wake, respawn and closing storage. These operations
can write world blocks, but are not independent generated structure families.
This is membership evidence, not a proof of duplication safety or permissions.

Source 55d1c0ea binds the external Collective mixin plugin. It filters declared
hooks by loader/bundle eligibility, returns no additional mixins and has empty
load/target/pre/post callbacks. Collective's full provider remains open; reuse
this source when closing that provider. Do not duplicate shared helper tracing.

All 79 Quick Right Click classes and ten other files are accounted for. The
NeoForge metadata selects its three common hooks. Forge/Fabric descriptors and
counterpart code are packaged alternatives, not the selected NeoForge entry.
No data, assets, templates, services or nested archives are present. The focused
case binds ten Quick Right Click classes and the Collective plugin to their
frozen archives. Independent r1 captures reproduce byte for byte.

```sh
uv run pytest -q tests/item8/test_quick_right_click_provider_scope.py
uv run ruff check tests/item8/test_quick_right_click_provider_scope.py tools/inspect_item8_pool_elements.py
uv run basedpyright tests/item8/test_quick_right_click_provider_scope.py tools/inspect_item8_pool_elements.py
```

The focused case and scoped quality checks pass. Whole providers: 109 resolved,
27 open. No family added. Continue remaining provider roles and canonical Moog
grouping before detailed attributes; no further generic quick-access menu audit.


### Collective membership resolved

Sources 71c6534b, f59d9219, 9f1bd61d and reused plugin 55d1c0ea bind twenty-five
classes: active entries/events, four common hooks, nine active services and
initialization delegates. Collective initializes shared data/name lists and
configuration JSON, item/enchantment constants and consumer networking. Its
entity-replacement lists start empty; event handling applies supplied replacement
rules and queued entity/runnable actions. Services register supplied blocks/items,
forward portal events, query loader/tool/tag properties and teleport existing
entities. None defines an independent authored structure family.

Preserve effects on existing spawners, entity replacement, player-head caching,
block-entity and bonemeal callbacks for later attribution. Experimental-world
warning handling is conditional on development mode or hideexperimentalwarning;
it is not compatibility proof. RegisterMod includes update checking. Membership
closure does not claim networking, permissions or consumer-handler safety.

The complete payload is 567 classes, 27 service descriptors (nine per packaged
loader), three JSON name/message lists, one translation and thirteen other
metadata/icon/access/mixin files. The NeoForge metadata selects four common and
five client hooks. The reused plugin adds no additional mixins. Forge/Fabric
code and service descriptors are packaged alternatives. There are no nested
archives, templates or generation data. The focused case validates all payload
files, data shapes, selected hooks, services and preserved source identities.

```sh
uv run pytest -q tests/item8/test_collective_provider_scope.py tests/item8/test_quick_right_click_provider_scope.py
uv run ruff check tests/item8/test_collective_provider_scope.py tools/inspect_item8_pool_elements.py
uv run basedpyright tests/item8/test_collective_provider_scope.py tools/inspect_item8_pool_elements.py
```

Two focused cases and scoped quality checks pass. One overlong test line was
wrapped after the initial Ruff finding. All captures reproduce byte for byte.
Whole providers: 110 resolved, 26 open. No family added. Do not continue generic
Collective service, event or networking internals; continue remaining provider
roles and canonical Moog grouping before detailed attributes.


## EMI Loot membership closure

Exact archive emi_loot-0.7.9+1.21+neoforge.jar, SHA-256
a89805cdcb2e11734624d7239112643ee6b8f95e6b71b3a720530df6a5c18980.
The complete payload has 209 classes, 90 client assets, 15 direct-drop entity
descriptions, one display-exclusion list and seven metadata/configuration files.
There are no nested archives, services or packaged generation definitions.

Sources ebf5a286 and a2f485ef retain four automatic entries, all 40 common
hooks and the relevant parser/resource delegates. Entry registration supplies
three loot-condition codecs, two loot-function codecs and six client-bound
payloads. The two injection hooks initiate parsing/postprocessing after resource
reload. The other 38 hooks expose existing fields or component apply methods.
They do not inject generation. The static registry accessor throws before Mixin
transformation; it is not a runtime generator.

ServerResourceData reads direct-drop descriptions into a private map. Its
NeoForge delegate posts the table-load event, so consumers may transform these
parsed tables. LootTableParser reads existing registries, builds five sender
maps and synchronizes display data to compatible players. Client entries clear
and reload display state. The provider contributes no independent generated
family. Do not count its chest/drop descriptions as structures or continue
generic loot-parser/network internals for membership. This disposition does not
claim a complete loot-behavior or information-disclosure audit.

Reproduction commands and manifest identities are in the two source READMEs.
`uv run pytest -q tests/item8/test_emi_loot_provider_scope.py` passes, binding the
full archive payload, entry/hook coverage and all 49 captured class identities.
Scoped Ruff and Basedpyright pass after a precedence-parenthesization lint fix.
Whole-provider queue: 111 resolved, 25 open. Working family groups remain 410;
canonical Moog decisions remain provisional. Item 8 is not complete.


## Puzzles Lib membership closure

Exact archive PuzzlesLib-v21.1.52-1.21.1-NeoForge.jar, SHA-256
00069866c4c6bb67ee5192d1b425d46e6a1601dc598e61bd10b67ba5fa8b029c.
The complete payload contains 951 classes and 14 other files, including three
service declarations. No packaged data, assets, templates or nested archives.

Sources 875c52c6 and a97ac77c bind both automatic entries, all three services,
two mixin plugins, all 15 declared common/server hooks and startup delegates.
PuzzlesLibMod initializes shared proxy events and one optional client-bound
entity-capability message. The proxy load-complete callback initializes consumer
contexts and event invokers. NeoForge registration maps native events to
consumer callbacks. Both registration methods invoke only the event registry's
register overloads, rather than an independent generation registration.

Hooks cover consumer minecart construction, enchanted loot bonuses, menu data,
data-generation tag helpers and biome/spawn/registry accessors. Preserve the
loot-bonus and consumer-supplied behavior effects for attribute attribution.
Development hooks modify commands, server settings, EULA handling and pack/data
generation support. Both plugins gate their named development hooks using the
loader environment; NeoForgeEnvironment reads FMLEnvironment.production. Neither
plugin supplies additional mixins. Do not infer operational acceptance or EULA
authorization from these hooks. The runtime identity remains frozen.

No independent generated family. No further generic consumer event, networking,
configuration or development-tool tracing is needed for membership. Full archive,
entry/hook/service and 27 source identities are bound by:
`uv run pytest -q tests/item8/test_puzzles_lib_provider_scope.py`. The test and
scoped Ruff/Basedpyright pass after adding an explicit type to parsed metadata.
Both captures reproduce exactly using the commands in their source READMEs.
Whole providers: 112 resolved, 24 open. Working groups remain 410. This is a
membership disposition, not the complete Item 8 attribute or exit gate.


## Architectury membership closure

Exact archive architectury-13.0.8-neoforge.jar, SHA-256
5ec578f814e8cca87aeffa6e424032e78d9ea5ea6b603dd834c2dc13c31141ee.
Complete payload: 382 classes and eight metadata/configuration/icon files.
No packaged data, assets, templates, services or nested archives.

Sources d943fcbb, 8ed7b7ec and 4a879ad8 retain the sole automatic entry,
all 17 common hooks, the plugin and startup delegates. The plugin returns
the already declared NeoForge chunk-serializer hook, not an additional family.
Hooks attach consumer extension APIs to items, entities and fluids, forward
lightning/falling-block/bucket events, support armor/creative tabs and attach
level context to chunk events. Preserve consumer behavior effects for attribution.

Common startup registers native event forwarding and consumer setup callbacks.
Server event registration returns without additional handlers. Biome startup
registers the none_biome_mod_codec serializer. Its modifier applies predicate
and consumer pairs from additions, removals, replacements and postprocessing
lists; all four lists start empty. This supports consumer-supplied biome changes
and does not supply an independent generated family. Entity-spawn initialization
registers a client-bound payload type; packet creation takes an existing entity
and server tracker. It synchronizes that entity rather than adding a generator.

No independent generated family. Do not continue generic event, biome wrapper,
packet codec or networking internals for membership. Full payload, entry/hook
coverage and all 28 source identities are bound by:
`uv run pytest -q tests/item8/test_architectury_provider_scope.py`. The focused
test, scoped Ruff and Basedpyright pass. All three captures reproduce exactly
using commands recorded in their source READMEs. Whole providers: 113 resolved,
23 open. Working family groups remain 410; Item 8 is not complete.


## Bookshelf membership closure

Exact archive bookshelf-neoforge-1.21.1-21.1.81.jar, SHA-256
19e88d40da2b6a114c2b808f7fb469d96e66a5379df0a8a43fcb7834498b3e76.
Complete payload: 173 classes, five language assets, fake-player damage type
and tag, eleven empty creative-tab item tags, five services and metadata.
No structure definitions, templates or nested archives.

Sources 3a315ed2 and 17cdf0d7 bind the sole automatic entry, all five service
implementations, all 27 common hooks, common initialization and content-provider
defaults. Common initialization runs startup checks. The retained content service
defines ingredient/load-condition/item-predicate/criterion/loot codecs, loot
descriptions and commands. ContentProvider defaults add no generation. Gameplay
and render helpers act on supplied objects; network handlers register supplied
packets; the platform helper exposes loader context.

Hooks expose existing fields and consumer callbacks, apply load conditions and
loot modifications, manage recipe/reload state, support creative-tab and potion
contributions, and handle fake-player damage/kill semantics. Preserve these loot
and encounter effects for attribute attribution. Their existence is not a proof
of unrestricted or harmless automation. No independent generated family. Do not
trace generic loot, condition, registry or network internals for membership.

`uv run pytest -q tests/item8/test_bookshelf_provider_scope.py` binds the full
archive payload, empty tags, entry/hook/service coverage and 35 captured class
identities. This focused test, scoped Ruff and Basedpyright pass. Both source
captures reproduce exactly with the commands in their READMEs. Whole providers:
114 resolved, 22 open. Working groups remain 410 and canonical Moog decisions
remain provisional. Item 8 is not complete.


## Better Combat membership closure

Exact archive bettercombat-neoforge-2.3.2+1.21.1.jar, SHA-256
afb1f28271ee3b622947f533aa754bb22ed67edd4940a3e9fdf2cca1edb7b8a9.
Full outer payload: 158 classes, 161 client assets, 41 weapon-attribute JSON
definitions and seven other files including nested Tiny Config. No packaged
structure definitions or templates.

Sources aea34a1e, c6a937e0 and 60b953d3 capture five automatic entries, all
ten common hooks, the mixin plugin and common/resource/compatibility delegates.
Entries initialize configuration, sounds/particles, attack handling and
synchronization. WeaponRegistry reads weapon_attributes into attribute maps and
encodes them for synchronization. Hooks affect existing player attacks, reach,
knockback, dual wielding, hand selection, item data and ranged-weapon handling.
Preserve these combat effects for later hostility/mob attribution.

The plugin checks for Player Animator's IAnimation class and adds no additional
hooks. Compatibility initialization conditionally registers an FTB team-relation
matcher. These paths supply no independent generated family. Do not continue
generic combat balance, team, attribute parser or network auditing for membership.

Nested Tiny Config SHA-256:
eef9a1d8b3fa561b08cb7b765ba15f2055277d44399cb1261cec0296550c6e3c.
Every contained file name and byte matches the Village Taverns nested copy
whose archive hash is 1587ed9848881e7b677da5b8c85e0f35719315eb5f6571592d31840cf1421f63.
Reuse tiny-config-entry and the existing Tavern payload check. Its automatic
entry calls an empty initializer; ConfigManager reads/writes consumer JSON.
Do not confuse archive-container byte differences with different class behavior.

`uv run pytest -q tests/item8/test_better_combat_provider_scope.py tests/item8/test_tavern_provider_scope.py`
passes three cases, binding full payload, entry/hook/source identity and complete
nested-member equivalence. Scoped Ruff/Basedpyright pass after separating the
nested equivalence assertion into its own focused case. All 20 new captured
classes reproduce exactly using the three source README commands. Whole providers:
115 resolved, 21 open. Working groups remain 410 and 100 explicitly provisional
Moog records still require canonical decisions. Item 8 is not complete.


## Polymorph membership closure

Exact archive polymorph-neoforge-1.1.0+1.21.1.jar, SHA-256
bec8118978adeb052de9c4eaf9a595830621d82515a764f32f9c8a4dd52ab94b.
Full payload: 98 classes, 16 translations, six GUI sprites, three services and
12 other metadata/documentation files. No data, templates or nested archives.

Sources 0b9f0152, 562005f3, 48f73c41 and e4e27ae2 bind the sole automatic
entry, all three services, 15 core common hooks, five declared integration
hooks, their plugin and startup/runtime delegates. Initialization registers
recipe-data attachments, five client-bound and three server-bound packet
handlers, furnace/crafter recipe-data factories and existing-menu associations.
Chunk and server-level hooks supply recipe context around existing block ticks.
Other hooks support recipe caches, crafting/smithing selection and recipe-viewer
transfers. These are not structure-generation paths.

Common events handle container/disconnect state and periodic watched-block
updates. BlockEntityTicker starts with an empty map, removes invalid entries
and ticks recipe data for registered existing block entities. FastBench support
updates the selected crafting result and synchronizes it. The NeoForge integration
service offers FastBench conditionally on mod presence. Integration hooks are
conditional; their plugin may log and disable failed modules with warnings.
Preserve that limitation instead of treating readiness as compatibility proof.

No independent generated family. Do not expand membership into generic recipe
implementation, inventory/network safety or widget internals.
`uv run pytest -q tests/item8/test_polymorph_provider_scope.py` passes, binding
the full payload, entry/hook/service coverage and all 33 source identities.
Scoped Ruff/Basedpyright pass after wrapping one long assertion. Four captures
reproduce exactly using their README commands. Whole providers: 116 resolved,
20 open. Working groups remain 410; 100 explicitly provisional Moog records
still require canonical decisions. Item 8 is not complete.

## BCLib whole-provider membership closure

The frozen bclib-21.0.24.jar SHA-256 is
`a7efd02dd3409dbac9c8455c5ed4fa4ca340e2af1c39f211038198dfa1c92093`.
It contains 627 classes, 103 client assets, five data files and eleven other
metadata/license/nested files. The data consists of disabled recipe configuration
and four bonemeal block tags. Assets contain rendering patterns, models,
textures, blockstates, languages, material definitions and icons. There are no
packaged structure roots, pools or templates contributed by this archive.

Reuse bclib-integration-dispatch for the main entry and conditional integration
API. Captures 7dae8acd, ccfcb07c and bfdb98bf retain the direct generation entry,
all nine automatic entries, all 35 common hooks and PostInitAPI. The thirteen
client-only hooks and empty UI client list declare no plugin or common hooks.
The 50 retained outer classes bind the entry/hook boundary and the selected
shared API delegates. The main entry registers consumer block/item, recipe,
configuration, lifecycle and piece support; datagen registration is separate
from the frozen runtime content evidence.

TemplatePiece accepts a caller-supplied template or persisted piece NBT, places
that template and optionally erodes/covers its bounds. It is a piece, not an
additional family. BetterEnd's already inventoried content remains attributed
to its actual roots/templates and consumer configuration. PostInitAPI operates
on existing registered blocks and items and consumer callbacks. Other hooks
extend existing anvil, recipe, loot-list, lighting, piston, portal, boat,
elytra, shears and sign behavior, diagnostics and accessors. Do not expand the
family inventory into audits of those generic gameplay implementations.

Generation effects are retained explicitly: ChunkGeneratorMixin rotates the
feature seed and resets its counter at biome decoration entry.
WorldGenRegionMixin replaces ensureCanWrite with an absolute chunk-distance
check of less than two on both horizontal axes. Neither introduces a family;
neither is evidence of unchanged generation or general compatibility.
Lifecycle callbacks handle configuration/data exchange and migration.
SpawnRuleBuilder registers consumer-supplied entity spawn placements.

Nested MixinExtras is bound by 2f92d5b1. Its archive SHA-256 is
`9c617719248f8b89847348fc7ea5e705739c147ae5e172551264d225bc9f2507`.
The GAMELIBRARY contains 503 classes and four manifest/configuration/license/
annotation-processor files, no packaged content or Minecraft class references.
Its initialization config declares only a plugin. The plugin initializes
MixinExtrasBootstrap and returns no additional mixins. This is shared injection
infrastructure. The failed request for nonexistent nested mod metadata is
preserved in its capture README; the actual manifest is authoritative.

Reproduce the captures with their README commands. Focused verification:
`uv run pytest -q tests/item8/test_bclib_provider_scope.py` (two cases).
The tests bind archive identity, complete payload categories, automatic entries,
all common hooks and their preserved source bytes, client declarations and the
nested payload/plugin. Scoped Ruff and Basedpyright pass after correcting test
assertion style and explicit JSON typing. Independent capture reproductions
match bytes. No additional measurement system was introduced.

Disposition: no independent generated family. Whole providers: 117 resolved,
19 open. The 410 working groups and 100 explicitly provisional Moog decisions
are unchanged. Canonical grouping, required attributes and final Item 8
review/delivery remain open.

## WorldWeaver whole-provider membership closure

Frozen worldweaver-21.0.24.jar SHA-256:
`cd1a1c247a4870479a64a5ad837a0f42ebfadfcd1507131284eec05a4a6af51e`.
The complete archive contains 794 classes, 21 client assets, 25 mixin
configurations, one service file, five other metadata/license files and one
data file. No nested archives or packaged structure/pool/template definitions
are present. The data file is
`data/wover/worldgen/noise_settings/amplified_nether.json`, a terrain setting.
Assets are languages, one model and icons. Ten client-only hooks are declared;
no mixin configuration declares a plugin or separate server hook list.

The provider evidence comprises 372669cb (seven automatic entries and six
registry services), 46c52394 (seventeen direct module initializers), 3b2c7fd9
(listener targets), f632c8bd (ten registration targets), 55320bc3 (all 45 common
hooks) and 1717ee10 (six direct bootstrap boundaries). These contain 91 distinct
classes. Earlier nonverbose captures remain partial evidence; 3b2c7fd9 fills
the demonstrated listener-target omission. Reproduce each with the extractor
commit and exact command in its README, not with a later changed extractor.

Generation registrations supply reusable feature types (block placement,
postprocessing, sequence, condition, pillar and template), placement codecs,
structure/piece types, material rules, biome sources and chunk generators.
Legacy aliases are not new families. Reuse StructurePoolElementTypeManagerImpl
and SingleEndPoolElement in pool-codecs and the existing biome-modifier
captures accepted with BetterEnd. Consumers remain attributed to their actual
frozen registry entries, packaged/configured content and observed worlds.
Do not count shared codecs, pieces or registration events as extra families.

Configured/placed feature, pool, set and surface bootstraps dispatch consumer
events. ModCore's supplied datapack list starts empty and its listener loads
registered pack roots from their owning mod. It warns and skips missing or
invalid pack metadata. WorldWeaver's archive supplies no such independent
architectural content. Preset options are normal, large, amplified, superflat
and legacy_17; available options do not prove the frozen world's selected
preset. Existing runtime and frozen configuration identities remain authority.

Preserve actual effects: biome feature-step rebuilding, consumer Nether/End
biome selection, surface-rule injection, registry/lifecycle events and preset
selection support. NoiseGeneratorSettingsMixin warns when overwriting an
already overwritten surface-rule set; its getter named getOriginalSurfaceRules
returns the current field. Recipe/advancement/item-stack/potion/POI/tag hooks
are consumer gameplay APIs. This membership disposition is not an unchanged
behavior or general compatibility claim, and does not justify expanding Item 8
into generic event, recipe, networking or terrain-tuning audits.

Focused verification is
`uv run pytest -q tests/item8/test_wover_provider_scope.py`.
It binds archive identity, full payload categories, automatic/service entries,
all common hooks, client-only declarations and preserved source bytes.
Scoped Ruff and Basedpyright pass. Capture r1 reproductions match bytes.
The combined provider and BetterEnd feature-candidate check passed 17 cases:
`uv run pytest -q tests/item8/test_wover_provider_scope.py tests/item8/test_betterend_feature_candidates.py`.
No new measurement system or evidence framework was added.

Disposition: shared consumer generation/terrain APIs, no independent family.
Whole providers: 118 resolved, 18 open. Working groups remain 410; the 100
explicitly provisional Moog grouping decisions remain open. Detailed family
attributes and final Item 8 review/main delivery have not passed.

## Create Dragons Plus whole-provider membership closure

Frozen CreateDragonsPlus-1.11.2b.jar SHA-256:
`9b15e464465a639de9ef5a935ae9fd94ea545904517d1428bc784a4012e0a1e2`.
Full payload inspection binds 352 classes; data consists of recipes, loot tables,
advancements, tags, data maps and physics/floating-material definitions. Assets
contain models, blockstates, languages, textures, an atlas and nine Ponder
resources. There are no packaged server structure roots, pools or templates.
Client tutorial assets are not independent generated-world families.

332870dc retains fourteen automatic entries, all 34 common hooks and their
shared plugin. fb5716dd adds three direct startup delegates and three nested
library classes. The 52 outer classes cover those entry/hook/delegate boundaries.
All five mixin configurations share CDPMixinConfigPlugin; the only client hook
is airflow-particle behavior. Optional integration code was inspected without
activating absent mods or changing the frozen retained stack.

The common entry registers block/item/fluid/recipe, fan-processing and data-map
support. Its SERVER_DATA pack installs CDPRuntimeRecipeProvider. Fluid reaction
and open-pipe hooks operate on existing machinery/fluids. Existing loot tables
receive blaze-upgrade smithing-template rewards. Dye/fan contribution callbacks,
block-freezing providers and conditional fluid-hatch compatibility are consumer
processing support, not independent generated families. Preserve those loot
and block/entity effects for later attributes; this is not a no-gameplay-impact
or general compatibility claim.

The nested conditional-mixin-neoforge-0.6.4.jar SHA-256 is
`0ae7b346d87879e81f276e6a590a6af1e723193e6eb3e94c1f71f7ab5b54d59f`.
Its 19 classes and five metadata/license/icon files provide conditional mixin
selection and annotation cleanup. Its NeoForge and common entry initialization
is empty. It has no packaged generation content. No broader restriction-checker
or integration-implementation audit is required for family membership.

Reproduce the three captures with their README commands. dfb52035 corrected
shell quoting for dollar signs in nested class names; the original captures
and r1 reproduction used argument lists and were unaffected. Raw source and
identity manifests reproduce byte for byte. Verification:
`uv run pytest -q tests/item8/test_create_dragons_plus_provider_scope.py`
passes two cases binding the parent/nested payloads, entries, hooks, plugin and
preserved source bytes. Scoped Ruff and Basedpyright pass after wrapping two
long test lines. No new measurement system was added.

Disposition: no independent generated family. Whole providers: 119 resolved,
17 open. Working groups remain 410 and 100 explicitly provisional Moog decisions
remain. Canonical grouping, attributes and final Item 8 review/main delivery
are still incomplete. Stop tracing generic CDP recipe/network/processing code.

## Accessories whole-provider membership closure

Frozen accessories-neoforge-1.1.0-beta.53+1.21.1.jar SHA-256:
`10017a3da78ea63e9ece27a1ca32f8cf490362f348778cf8cb759e7282f3beb0`.
The complete archive has 416 classes, 27 data files, 133 client assets and twelve
other metadata/schema files. Data defines accessory entity/group/slot resources
and enchantment/entity/item tags. Assets are languages, UI textures, shaders
and atlases. No nested archive, service descriptor or packaged structure,
pool/template generation content is present.

7aab0d60 retains the two automatic entries, all 32 common hooks and both mixin
plugins. c1e2927f retains Accessories.init and AccessoriesEventHandler, giving
38 distinct captured classes. The 36 client-only hooks are separately declared.
Both plugins return empty extra-mixin lists. The common plugin can disable its
temporary NBT fixes using a configuration marker and logs an old-world-data
warning. The NeoForge plugin selects the Curios hook only with curios present
and cclayer absent. No frozen configuration was changed.

Entries and delegates implement accessory capabilities, armor-slot support,
equipping/use/drop handling, commands, render data and synchronization.
onWorldTick reaches player revalidation after reload; entityLoad synchronizes
existing player containers. Common hooks extend equipment/inventory,
enchantment/loot and existing entity behavior, NBT and accessors. These affect
real gameplay and saved data but do not introduce an independent generated
family. Preserve their effects for attribution; this is not a compatibility,
privacy or no-gameplay-impact claim. Do not expand membership into general
packet, renderer, equipment or NBT implementation audits.

The focused command
`uv run pytest -q tests/item8/test_accessories_provider_scope.py`
passes one case binding the complete archive categories, entry/hook/plugin
coverage and source bytes. Scoped Ruff and Basedpyright pass. Both independent
r1 source reproductions match disassembly and identity manifest bytes. Exact
commands and extractor commits are in the capture READMEs. No new measurement
system or generalized verification framework was added.

Disposition: no independent generated family. Whole providers: 120 resolved,
16 open. The 410 working groups and 100 explicitly provisional Moog grouping
decisions remain unchanged. Item 8 canonical grouping, attributes and final
review/main delivery are incomplete.

## Amendments whole-provider membership closure

Frozen amendments-1.21-2.0.15-neoforge.jar SHA-256:
`e44e67d5c2eb5a73ee8ca3d1e9099ed20ccbf8167022bc407df8434b1bf362b5`.
Full payload binding covers 252 classes, 52 data files, 397 client assets and
eight metadata/configuration files. No nested archive or independent packaged
structure, pool or template is present. Data includes recipes, loot, tags,
damage/enchanting/soft-fluid definitions and three Blueprint repaletters.

4ece1d82 retains the automatic entry, all 39 common hooks and the shared plugin;
e248456f retains startup/events/Blueprint registration; 97966218 retains the
registry, structure cauldron block, replacement codec and Supplementaries
compatibility. The combined boundary contains 48 distinct classes. Eleven
client-only hooks are separately declared. Reuse the accepted
supplementaries-shared-plugin capture for Moonlight SimpleMixinPlugin; its
identity manifest SHA-256 is
`05fbc861b5d5a7e0290ac0bdcd10d29ae1afd2410c7833b97f5fd560a9640e75`.
Moonlight's separate whole-provider row remains open.

The Blueprint files replace cauldrons or water cauldrons in existing structure
tags, including villages, with configured amendment cauldron states.
BlockStateRepaletter checks the supplied original block and configured random
chance and returns a replacement state on a match. StructureCauldronHack is
its registered block/block-entity support. These are structure-content
modifiers, not independent families. Presence of conditional integration data
does not prove its activation or actual fluid contents in observed worlds;
retain those distinctions for the later attributes.

Other registration/setup paths add block/item/entity support, extra placement
variants, dispenser/POI/recipe conditions and faucet integration. Hooks and
ModEvents extend existing block and player interactions, cauldrons, signs,
skulls, brewing, bells, projectiles and explosions. Preserve those gameplay
and content effects. No general networking, block-entity, rendering or
compatibility audit is required for membership, and no runtime setting changed.

`uv run pytest -q tests/item8/test_amendments_provider_scope.py` passes one case
binding archive categories, entries/hooks/plugins, packaged replacement targets
and preserved source bytes. Scoped Ruff and Basedpyright pass; all three source
r1 reproductions match bytes. The raw javap record-class output ends with an
extra blank line, which git diff --check flags. It is preserved byte for byte
as raw evidence rather than cosmetically rewritten; documentation and test
diffs pass whitespace checks. No new measurement system was added.

Disposition: no independent generated family. Whole providers: 121 resolved,
15 open. Working groups remain 410 and 100 explicitly provisional Moog grouping
decisions remain. Final canonical grouping, attributes and Item 8 review/main
delivery remain incomplete.

## C2ME partial provider disposition

Provider membership remains OPEN. The outer entry and base module dispatch are
retained in 957658fa. Worldgen-threading hooks are retained in ff824a0b and
their direct transformation/state delegates in cb33666e. These 49 captured
classes account for startup diagnostics, module selection and the complete
worldgen-threading module hook set. They establish no independent family.

The latter module modifies existing structure state: atomic chest/trap flags
and references, thread-local piece counts/selection, synchronized collections,
volatile field annotations, locked mansion grids and guarded region tick writes.
Its extension exports debug mappings and its transformer changes field access
flags. Preserve random ownership failures and optional fallback behavior as
limitations; this inspection does not prove unchanged generation or concurrency
correctness. No benchmark, fresh server experiment or new measurement system
was required. Do not trace generic debug formatters or config/executor internals.

```sh
uv run pytest -q tests/item8/test_c2me_threading_scope.py
uv run ruff check tests/item8/test_c2me_threading_scope.py
uv run basedpyright tests/item8/test_c2me_threading_scope.py
```

The focused test passes and binds the complete module payload, 36 common hooks,
plugin, entrypoint and five direct delegates to their archive and source hashes.
Scoped quality checks pass after replacing an initially rejected split string
with the exact single-line member name. Every capture reproduces byte-for-byte
with its recorded extractor. Source README files retain the commands and hashes.
Whole providers remain 121 resolved and 15 open; no canonical grouping changed.

C2ME continuation: 5a44fce9 retains the remaining 18 module initialization
boundaries (26 classes). Entries initialize settings, view-distance networking
and serialization of supplied chunks. Config and listener delegates remain
bounded startup inputs to reconcile. Do not expand this into a packet or NBT
correctness audit. 7658d2f6 retains ten pool/generation hooks: existing random
source replacement, aquifer computation, structure terrain blending, End biome
and block-shape caching, and biome/noise executor redirection. cb594f9b retains
the pool codec wrapper, which locks and delegates the existing codec. This
closes the pool-wrapper question without adding a family. All these captures
reproduce byte-for-byte using their committed extractor and README command.
Extractor Ruff and Basedpyright checks pass. No new measurement was run.

The remaining index points to accessors, existing-structure state,
chunk lifecycle/serialization, ore and surface computation, density-function
compilation, noise math and random implementations. Reconcile them against the
already inspected callers; a class-name reference is neither an additional
family nor automatic justification to inspect every implementation helper.
Whole-provider closure still requires accounting for the remaining hooks,
startup delegates and bundled-library entry roles. Preserve the existing
threading disposition and stop tracing already resolved paths. Counts remain
121 providers resolved, 15 open, with 100 provisional Moog grouping decisions.

C2ME continuation in 914afefd resolves the eight remaining configuration and
view-distance startup delegates. They read settings, send render-distance
values and set a render-distance override. They add no independent family.
9afeb260 retains every common hook declared by the allocation, density-function
compilation, math and native-math modules (27 classes). These hooks reuse
existing ore/surface/noise inputs and modify allocation, evaluation, caching
or sampling. Preserve optional activation and numerical-equivalence limits;
this is not a performance or compiler correctness audit. All captures reproduce
exactly with their committed extractor. Extractor quality checks pass.

Next C2ME boundaries are base accessors/lifecycle hooks, client view distance,
general-threading and chunk-status fixes, no-tick view distance, chunk-I/O and
scheduling, chunk serialization/system/I-O rewrites, server commands and
lighting. Reuse all resolved generation and startup roles. In particular, do
not inspect density AST internals, random algorithms, numeric equivalence or
configuration parsers merely because the provider index references them.
The scheduling mixin declaration contains a null entry; retain it as packaged,
with no invented class target. It is not a family candidate. Bundled-library
entry roles remain to reconcile. Whole providers remain 121 resolved, 15 open.

## Final C2ME membership closure

C2ME membership is RESOLVED, with no independent generated family. The exact
parent is c2me-neoforge-mc1.21.1-0.3.0+alpha.0.93.jar, SHA-256
2735b16e136e51c03c9a8211fbecaf9d571a28475981223c60662465664f5322.
The parent contains 20 C2ME modules and six bundled libraries. MixinSquared
contains one additional nested archive. All are covered by the fixed-parent
payload and source-identity test. They contain no data resources or NBT
templates. The lighting module's Fabric metadata declares no entrypoint and
references its already covered mixin configuration.

All declared common/server hooks, NeoForge automatic entries, module startup
paths and mixin plugins have source dispositions. Existing generation state,
random and terrain computation, chunk lifecycle/I-O, serialization, lighting,
view distance and diagnostics are their roles. The command reports pending
no-tick chunk loads; it does not generate structures. Fifty-two existing
capture directories retain 259 disassemblies with exact parent/nested/class
identities and independent byte-identical reproduction commands. The final
remaining-hook increments are 7afc4e46 through 241de3bd; 56cbfb4f closes the
command and bundled plugin boundaries. Earlier C2ME captures remain required.

Asyncutil, exp4j, JCTools, Reactive Streams and RxJava have no Minecraft class
references, data/templates or runtime entry declarations. They are used as
asynchronous, expression and collection utilities by the inspected consumers.
MixinSquared's plugin initializes target-selector and mixin extension support
and loads annotation-adjuster/canceller services. Its nested annotation
processor is a compilation service, not a runtime generation entry. No further
generic helper, scheduler, compiler or network audit is needed for membership.

Preserve the recorded generation and lifecycle modifications as attribute and
identity context. This closure does not assert every optional hook activates,
numerical equivalence, concurrency correctness or persistence safety. Preserve
the null scheduling declaration without an invented target. The source capture
is not an operational test. No fresh server experiment or measurement system
was required.

```sh
uv run pytest -q tests/item8/test_c2me_provider_scope.py tests/item8/test_c2me_threading_scope.py
uv run ruff check tests/item8/test_c2me_provider_scope.py
uv run basedpyright tests/item8/test_c2me_provider_scope.py
```

Both focused cases pass. The provider test binds the complete nested archive
topology, missing data/templates, declared entry/hook coverage and every
retained source manifest/hash, and rejects unexplained capture files. Scoped
quality checks pass. An initial long nested-archive dictionary key was wrapped
without changing its value. The direct topology test has narrowly documented
complexity suppressions to avoid adding a helper framework.

Whole providers: 122 resolved, 14 open. Working groups remain 410 and 100
explicitly provisional Moog grouping decisions remain. Item 8's canonical
family list, attributes, final gate and review/main delivery remain incomplete.

## CC:Tweaked membership closure

CC:Tweaked membership is RESOLVED, with no independent generated family.
Archive cc-tweaked-1.21.1-forge-1.119.0.jar has SHA-256
169e2fe0445e320562c0568baa4c796a69a3464a0a5e902c484be1be3e326a0b.
Its 1,190 classes, computer Lua programs, recipes, advancements, tags, upgrade
and loot data are bound by the focused provider test. No structure definitions
or NBT templates are packaged. Nested Cobalt and JZlib provide Lua/runtime
and compression support, with no Minecraft references or service entries.

Source increments 602c594a, 67708b9f, 8d0af4df and a66abd1c retain 31 classes
and reproduce byte-for-byte with their committed extractor commands. They
cover automatic entries, all four common mixins, three common service
providers, direct registration/integration delegates and computer lifecycle.
Both automatic client subscribers explicitly declare Dist.CLIENT. The client
service and mixin roles are rendering, UI and client-network support.

Mod registries add computer blocks/items, block entities, data components,
upgrades, menus, commands, recipes, loot conditions and creative tabs. Server
lifecycle operates registered computers and existing block-entity ticks.
Common mixins migrate computer/turtle data. Create integration supplies block
movement checks; More Red integration supplies bundled-redstone capability.
These are construction and existing-content behavior, not a generated family.
Stop tracing generic Lua, filesystem, networking, renderer or turtle APIs.

Retain the computercraft:treasure_disk injection into ten existing vanilla
loot tables: SIMPLE_DUNGEON, ABANDONED_MINESHAFT, STRONGHOLD_CORRIDOR,
STRONGHOLD_CROSSING, STRONGHOLD_LIBRARY, DESERT_PYRAMID, JUNGLE_TEMPLE,
IGLOO_CHEST, WOODLAND_MANSION and VILLAGE_CARTOGRAPHER. CommonHooks supplies
the extra loot pool and ForgeCommonHooks adds it on loot-table loading. This
is a family loot-attribute input, not another family or proof of an observed
disk in a specific chest. Player-programmed construction remains distinct
from automatically generated authored content. No tuning or new measurement
was needed for this provider decision.

```sh
uv run pytest -q tests/item8/test_cc_tweaked_provider_scope.py
uv run ruff check tests/item8/test_cc_tweaked_provider_scope.py
uv run basedpyright tests/item8/test_cc_tweaked_provider_scope.py
```

The focused case and scoped quality checks pass. The test binds the frozen
payload, data categories, nested libraries, common entry/hook/service set,
client side declarations and all captured archive/class/source hashes. It
rejects escaped capture paths and unexplained files. One initial assertion
line exceeded the style limit by one character; it was wrapped without a
semantic change. No runtime activation or gameplay equivalence is inferred
from this source-membership check.

Whole providers: 123 resolved, 13 open. Working groups remain 410; 100
explicitly provisional Moog grouping decisions remain. Final canonical
membership, family attributes, final gate and review/main delivery remain open.

## Comforts membership closure

Comforts membership is RESOLVED with no independent generated family.
Archive comforts-neoforge-9.0.5+1.21.1.jar has SHA-256
6b0fd35a1349107e08a45539adbde9683bb203febc43a3305f6fc4ac73e59615.
The payload has 64 classes, 66 recipes, 66 advancements, 33 block loot tables
and five tags. It contains no structure definitions or NBT templates.
Nested SpectreLib has 53 classes, no generation data or templates, one mod
entry and one configuration service. Its exact bytes are pinned by the parent
and the nested SHA-256 in the source manifest and focused test.

Source increments 431d2335 and 55948d4a retain 14 classes. They cover both
automatic entries, all four Comforts services, the SpectreLib config service,
all three common mixins, registration and the direct sleep-event handlers.
Both captures reproduce byte-for-byte using their committed README commands.
Comforts registers blocks, items, block entities, sleep-data attachments and
recipe conditions. Client initialization is guarded by Dist.CLIENT. Common
events operate player sleep, spawn-setting, wake time, effects and existing
sleeping equipment. The mixins change sleep status and expose player sleep
state. SpectreLib supplies config lifecycle, paths and client synchronization.
These are player construction and utility roles, not authored world generation.
Stop at these established roles; no generic config, networking or sleep-system
correctness audit is needed for family membership. No runtime experiment or
new measurement system was added.

```sh
uv run pytest -q tests/item8/test_comforts_provider_scope.py
uv run ruff check tests/item8/test_comforts_provider_scope.py
uv run basedpyright tests/item8/test_comforts_provider_scope.py
```

The focused case and quality checks pass. The test binds archive identities,
payload categories, automatic entries, services, mixins and captured class and
source hashes, rejecting escaped paths and unexplained capture files. The
fixed two-archive test exceeded the statement style limit by two statements;
a narrow suppression avoids introducing a helper solely for that style limit.
Source membership does not prove gameplay compatibility or observed generation.

Whole providers: 124 resolved, 12 open. Working groups remain 410 and explicit
provisional Moog decisions remain 100. Canonical reconciliation, all required
attributes, the final gate, review and main delivery remain incomplete.

## Resourceful Lib membership closure

Resourceful Lib membership is RESOLVED with no independent generated family.
Archive resourcefullib-neoforge-1.21-3.0.12.jar has SHA-256
5e36f2c69de008dc5795f730c84ab767688f15c810944b585485349a0c911261.
Its 222 classes contain one automatic mod entry and one common fluid mixin.
It packages no data resources, NBT templates or services. Nested Bytecodecs
(54 classes) and YABN (26 classes) contain only classes and manifests, with no
Minecraft references. Parent archive identity pins their exact bytes.

Source increments 418a89d6, 47a79be9 and 687f2e87 retain six classes and
independently reproduce exactly. The entry calls common initialization,
selects a server API proxy or client-guarded client initialization, and
registers a network-setup listener. The server proxy reads existing registry
access. Networking dispatches consumer-supplied handlers from an initially
empty listener list. Common initialization creates application cache/data
storage and a readme file. The sole mixin obtains the fluid type from existing
ResourcefulFlowingFluid data, caches it, and explicitly rejects missing data.
These utility and consumer API roles do not define or generate a family.
Stop general networking, storage and fluid behavior tracing at these roles.
No new runtime measurement or evidence framework was required.

```sh
uv run pytest -q tests/item8/test_resourcefullib_provider_scope.py
uv run ruff check tests/item8/test_resourcefullib_provider_scope.py
uv run basedpyright tests/item8/test_resourcefullib_provider_scope.py
```

The focused case and quality checks pass. The test binds frozen archive and
nested payloads, the automatic entry and complete common mixin set, and exact
captured source/class hashes. Escaped paths and unexplained capture files fail.
One assertion was wrapped to meet the line-length style limit, without changing
its behavior. Membership inspection is not networking, storage or gameplay
correctness evidence.

Whole providers: 125 resolved, 11 open. Working groups remain 410, with 100
explicit provisional Moog grouping decisions. The complete canonical list,
required attributes, final acceptance, review and main delivery remain open.

## Enchantment Industry membership closure

Create Enchantment Industry membership is RESOLVED with no independent
structure family. Archive create-enchantment-industry-2.4.0.jar has SHA-256
3830e27941fe08334217ded82713907a176bd2feb209292da25154e4c082585e.
Its 338 classes, complete data categories, 23 client Ponder templates and 15
block loot tables are bound by test_cei_provider_scope.py. No packaged
structure definitions occur. Recipes and data maps configure experience,
enchanting, forging and printing. Sable physics data remains packaged optional
content, not permission to enable Sable.

Sources 7f3f848b, 75fd1607, c4e39444 and f02b44f4 retain 47 classes and
independently reproduce exactly. They cover all 11 automatic entries, all 20
common/conditional mixins, direct common registration targets, lightning block
transformation and the client Ponder registration boundary. CEIClient and
CEIAClient declare client-only mod entry sides; three item-renderer subscribers
also declare Dist.CLIENT. The data-generator entry guards its registration
with DatagenModLoader.isRunningDataGen. Optional common integration entry
constructors guard their delegates with ModList.isLoaded. Apotheosis,
Apothic Enchanting and Sable are absent from the retained candidate metadata;
no optional activation is claimed.

Common registration adds machines, fluids, items, block entities, creative tabs,
recipes, enchantment tags, data maps, advancement triggers, stats, mounted
storage, arm interactions and item attributes. Hooks operate existing Create
machines, deployer attacks and experience drops, item repair, clipboard data
and fluid handling. Lightning finds existing experience blocks and converts
them to super-experience blocks. It does not place an independent authored
structure. Ponder assets are reached from a client-registered Ponder plugin.
Player industrial processing and tutorial scenes are not separate families.

Reuse Create Dragons Plus membership evidence for CDPMixinConfigPlugin and
its nested Conditional Mixin library. Enchantment Industry's nested library
is byte-identical, SHA-256
0ae7b346d87879e81f276e6a590a6af1e723193e6eb3e94c1f71f7ab5b54d59f.
Do not recapture that library or expand into machine, recipe, experience,
networking or optional-mod compatibility audits for this membership decision.

```sh
uv run pytest -q tests/item8/test_cei_provider_scope.py tests/item8/test_create_dragons_plus_provider_scope.py
uv run ruff check tests/item8/test_cei_provider_scope.py
uv run basedpyright tests/item8/test_cei_provider_scope.py
```

All three focused cases pass, including the reused plugin/library evidence
binding. Scoped quality checks pass after wrapping three long test lines.
The provider test binds payload categories, the automatic entry and mixin set,
nested identity and every captured class/source hash. It rejects escaped paths
and unexplained capture files. Source membership is not evidence of runtime
activation, observed generation or gameplay equivalence. No runtime measurement
or new evidence framework was needed.

Whole providers: 126 resolved, 10 open. Working groups remain 410 and explicit
provisional Moog grouping decisions remain 100. Canonical membership, required
attributes, final acceptance, clean review and main delivery remain incomplete.

## Big Cannons membership closure

Create Big Cannons membership is RESOLVED with no independent generated
structure family. Archive createbigcannons-5.11.6+mc.1.21.1.jar has SHA-256
9345e8773aa8be0f33bbf633796124e70d84c0c299aac94d8d252086f8712ffe.
Its 855 classes, complete data-category partition and 29 Ponder NBT assets are
bound by test_cbc_provider_scope.py. There are no nested JARs or service entries.
Packaged data describes cannon recipes, equipment, projectiles, block armor,
impact transformations, fluid properties, tags and related parameters. It has
no structure definitions or generated-world templates. Tutorial assets belong
to the client Ponder namespace, not independent world generation.

Reuse seven source increments: 5c75167e (entry/plugin declarations), 6444274f
(common and conditional hooks), ce85231e (common initialization), 09ecf172
(shared events), d0844cc0 (damage lifecycle), 38af6929 (registrations), and
b67e8d0b (construction integrations). All 62 captured classes independently
reproduce exactly. The entry and hook set includes all four automatic entries,
the mixin plugin, and all 32 common/conditional hooks. CBCClientNeoForge
explicitly declares Dist.CLIENT; 15 additional mixins are declared client-only.
Optional plugin checks and integration selection are preserved without claiming
that excluded Sable or other optional providers are active.

Registrations add cannon blocks and items, block entities, projectile and
contraption entities, fluids, recipes, menus, particles, sounds, data components,
display sources and mechanical-arm interactions. Construction integrations
register movement checks, cannon-loader/fragile contraption types, copycat armor
serialization and Curios gas-mask equipment predicates. These consume existing
or player-built blocks and equipment. Contraption uses of StructureBlockInfo
and searchMovedStructure are assembly of existing blocks, not generated families.

Shared events handle player construction/breakage, data reload and synchronization,
munition recipes and existing-world damage state. The world tick delegate updates
partial damage records and block-damage visuals. Its load path restores existing
damage data. Projectile/explosion effects and block-impact transformations alter
existing content; they are not independently generated authored structures.
Stop generic cannon, physics, networking, recipe, serializer and damage-system
tracing here. Membership inspection does not prove compatibility, persistence
correctness, cannon balance or acceptable shared-server damage.

```sh
uv run pytest -q tests/item8/test_cbc_provider_scope.py
uv run ruff check tests/item8/test_cbc_provider_scope.py
uv run basedpyright tests/item8/test_cbc_provider_scope.py
```

The focused source/payload case and scoped quality checks pass. The test binds
archive identity, complete packaged data categories, tutorial-only NBT paths,
automatic entries, common mixin targets and all captured source/class hashes.
It rejects escaped capture paths and unexplained source files. A single test
assertion was wrapped to meet the line-length style limit. No new runtime
measurement or evidence framework was needed for the membership decision.

Whole providers: 127 resolved, 9 open. Working groups remain 410 and explicit
provisional Moog decisions remain 100. Canonical reconciliation, attributes,
final acceptance, clean review and main delivery remain incomplete.

## Diesel Generators membership closure

Create Diesel Generators membership is RESOLVED with no independent generated
structure family. Archive createdieselgenerators-1.21.1-1.3.15.jar has SHA-256
56ef1d574278fc311f1ffa223dbd613077b899354a18d01ae8dca2578a4e2990.
Its 239 classes, complete packaged data categories and ten Ponder NBT assets
are bound by test_diesel_provider_scope.py. Data contains recipes, loot, tags,
an advancement and five fuel definitions, with no worldgen structure definitions.
The templates are client tutorial assets. No independent authored family is
provided by this payload or the inspected initialization and common hooks.

Reuse source increments 9dd6ae20, 44ae9c8a, c8adfcaa and 07de7794. Their 32
classes reproduce exactly and cover all three automatic entries, twelve common
mixins, direct registration targets, commands and oil data. Registrations supply
machine blocks, items, fluids, block entities, entity types, recipes, menus,
sounds, storage, data components and display sources. ModEvents registers Ponder
on client setup and machine capabilities/common processing handlers. Common
hooks operate existing machines, contraption coordinates, turret entity data,
player tools and fuel explosions. Three additional mixins are client-only.

GameEvents.loadLootTable reads entity loot into ReverseLootTable.ALL for item
to entity lookup. It does not insert loot or create another family. Oil commands
read or modify chunk resource amounts. OilChunksSavedData stores integer values
and derives defaults from seed, biome and configuration through noise sampling;
it does not place a structure or template. This is a virtual extraction resource,
not another canonical authored family. No resource balance or persistence claim
is made by this membership inspection.

The nested Sable Companion is byte-identical to the already resolved
Supplementaries library, SHA-256
873633e35046e3761b277ff8a1ecad0d55d9a3014fa81a0b084c9aecba1f3bed.
Reuse source 53c2374 and its four-class service binding; do not recapture it.
Neither this library nor the packaged Sable hook re-enables excluded Sable.
The unnecessary duplicate selector e2b1e848 was removed completely by revert
89b07d38 after Ruff found the duplicate key. The failure and correction remain
in history; the corrected extractor passes scoped checks. No new measurement
system or evidence framework was needed. Stop generic machine, network, recipe,
compatibility-library and resource-economy tracing for this membership decision.

```sh
uv run pytest -q tests/item8/test_diesel_provider_scope.py
uv run pytest -q tests/item8/test_supplementaries_provider_scope.py::test_supplementaries_bundled_companion_service
uv run ruff check tests/item8/test_diesel_provider_scope.py
uv run basedpyright tests/item8/test_diesel_provider_scope.py
```

Both focused cases and scoped quality checks pass. The new test binds the
archive, complete data categories, tutorial NBT partition, nested identity,
automatic entry/common mixin set and every captured class/source hash. Escaped
paths and unexplained capture files fail. One test line was wrapped for style.

Whole providers: 128 resolved, 8 open. Working groups remain 410 and explicit
provisional Moog decisions remain 100. Final canonical membership, attributes,
acceptance, clean review and main delivery remain incomplete.

## Curios membership closure

Curios membership is RESOLVED with no independent generated family. Archive
curios-neoforge-9.5.1+1.21.1.jar has SHA-256
a45df2125c26219974aba7507ffc9afe7b83acc941a386af3faacb1cc0056fde.
Its 152 classes and ten equipment-slot definitions are bound by the focused
test. It packages no structure definitions, NBT templates or nested JARs.
Its single platform service implements equipment-related queries.

Source increments 68eeeb92 and 38e02fc7 retain 24 classes and reproduce exactly.
They cover both automatic entries, the platform service, all thirteen common
mixins, registration, data reloaders, shared events, commands and direct API
implementation. The reloaders build slot definitions and entity-to-slot maps.
They do not spawn entities or authored structures. Shared events operate on
existing entities' equipment, inventory contents, modifiers, synchronization,
drops, and consumer item callbacks. Commands edit player equipment slots.
The item-entity constructor supplies dropped equipment, not an encounter family.

Mixins integrate equipment with advancement predicates, data migration,
inventory checks, looting/fortune, piglin neutrality and snow protection. These
are equipment-dependent modifications to existing gameplay, not new structures.
Consumer-supplied item callbacks remain attributable to their owning providers.
Stop general inventory, networking, rendering, commands and equipment API
tracing at these established roles. No new runtime measurement was needed.

```sh
uv run pytest -q tests/item8/test_curios_provider_scope.py
uv run ruff check tests/item8/test_curios_provider_scope.py
uv run basedpyright tests/item8/test_curios_provider_scope.py
```

The focused case and scoped quality checks pass. The test binds the archive,
complete data payload, service, automatic-entry and common-mixin sets, and
captured class/source hashes. It rejects escaped paths and unexplained files.
One assertion was wrapped for style without a semantic change. This membership
decision does not establish equipment balance, compatibility or persistence.

Whole providers: 129 resolved, 7 open. Working groups remain 410 and explicit
provisional Moog decisions remain 100. Final canonical membership, attributes,
acceptance, clean review and main delivery remain incomplete.

## Fzzy Config provider closure

The exact retained archive has SHA-256
4e5cc1438087b0bc0276969e88b9ad0bdf2bcc60d6caf5fe79e18947d7a29050.
Its 755 classes include two automatic loader entries. There are no packaged
`data/` resources, NBT templates, service declarations or common mixin configs.
The two nested parser libraries are pinned by the parent and the focused test:
Jankson 1.2.3 has 42 classes; Tomlkt 0.3.7 has 139. Neither has Minecraft class
references or service declarations. Their remaining files are metadata.

Source increments 574fadb2, 0f4f3dc3 and dafcbafd preserve eight classes.
The entry registers configuration synchronization and lifecycle callbacks,
configuration payloads, commands and a registry callback. NetworkEvents forwards
configuration updates and join/reload synchronization, starts synchronized config
handling and stops its threading utility. PlatformUtils commands list, inspect,
accept or reject quarantined configuration updates. They do not place sites.

RegistryBuilderImpl starts with an empty registry list and adds registries built
from caller-supplied keys. Its companion registers that list. RegistrarImpl wraps
caller-supplied registries and item suppliers in DeferredRegister; its initially
empty unbound set is attached to an event bus by the companion. These are consumer
registration APIs, not independent structure registrations. The client entry
registers client networking. No independent family is added. Stop generic
configuration, parser, permission and networking tracing here; this decision does
not claim those subsystems are otherwise tested.

Each capture reproduced byte for byte into its independent r1 directory using
the command in its README. Reproduce the source and archive binding check with:

```sh
uv run pytest -q tests/item8/test_fzzy_provider_scope.py
uv run ruff check tests/item8/test_fzzy_provider_scope.py tools/inspect_item8_pool_elements.py
uv run basedpyright tests/item8/test_fzzy_provider_scope.py tools/inspect_item8_pool_elements.py
```

The focused test passes (one case), as do scoped Ruff and Basedpyright.
Whole-provider dispositions are now 130 resolved and 6 open. The 410 working
groups and 100 explicit provisional Moog decisions are unchanged. These are not
a final family count. Final canonical reconciliation and attributes remain open.

## Kotlin for Forge provider closure

The retained outer archive SHA-256 is
ac827b62ce8fe71760208671b4a694e3ccd35049075f9406a751cffb5a5c9779.
It contains no classes, only metadata and 11 nested archives. The focused test
checks the exact member list and all nested archives for generation payloads.
None contains data resources, NBT templates, deeper archives or mixin configs.
Eight Kotlin runtime libraries have no Minecraft class references. Kotlin Reflect
has three Kotlin reflection service declarations; the other seven have none.
These do not provide structure content.

The three remaining modules are kfflang (19 classes), kfflib (46), and kffmod (2).
The helper library has no NeoForge automatic entries or services; its non-class
files are metadata. Its Minecraft references concern capability, profiler, deferred
holder and vector utility APIs. It does not independently install content.

Source increments 5dc5e092 and a93663c8 preserve six classes, including both
language services and both mod entry classes. The NeoForge language loader reads
consumer mod annotations, applies distribution selection and creates their mod
containers. The container instantiates consumer entry classes and injects their
event subscribers. AutoKotlinEventBusSubscriber registers consumer annotated
classes and methods. The Forge language provider separately reads Forge mod
annotations and assigns language targets; this does not activate Forge on the
frozen NeoForge platform. Both packaged mod entries only initialize a logger and
log that Kotlin for Forge is enabled. No independent family is added.

Stop generic language runtime, reflection, coroutine and utility implementation
tracing. This disposition is about provider membership, not general loader
compatibility. Source captures reproduce exactly into independent r1 directories;
their READMEs preserve commands and manifest identities. Validation:

```sh
uv run pytest -q tests/item8/test_kff_provider_scope.py
uv run ruff check tests/item8/test_kff_provider_scope.py tools/inspect_item8_pool_elements.py
uv run basedpyright tests/item8/test_kff_provider_scope.py tools/inspect_item8_pool_elements.py
```

Both focused cases pass. Ruff first flagged one long assertion; it was wrapped,
and scoped Ruff and Basedpyright pass. Whole providers: 131 resolved, 5 open.
Working groups remain 410 and explicit provisional Moog decisions remain 100.
Final canonical reconciliation, attributes and Item 8 acceptance remain open.

## Moonlight provider closure

The retained archive SHA-256 is
41bbe274c689ef4229892b6e46da57d27dce34a40fe7e2de0c230cd0e2bc0e98.
Its 684 classes include two automatic entries. Both mixin configurations are
accounted for: 43 common/platform hooks, 18 client hooks, and one plugin inheriting
already-preserved SimpleMixinPlugin. No nested archives, NBT templates or services
are packaged. Data contains 17 soft-fluid descriptions, one empty generic map
marker definition, one reload token, five color sets and five tag files. None is
an independent structure definition or template.

Sources 10f33521, 7ef8cd70, 582434ee, 96d6605e, 944483ae and 06fe6e74 preserve
55 classes. Reuse supplementaries-shared-plugin for the inherited plugin instead
of recapturing it. The focused binding covers all 56 captured classes together.

MoonlightRegistry registers consumer placement filters, loot entry/condition
types, trades and saved-data registries, items, data components and a schedule.
Its spawn-box block, block entity, pool element and piece are one component path.
JigsawPlacementMixin obtains those pieces from marker blocks in an existing
single template (or the first single element of a list) and appends their bounds.
SpawnBoxStructurePiece.place immediately returns without placing blocks.
JigsawCodecWithExtra adds spawn-box settings to an existing jigsaw definition;
ChunkGeneratorMixin asks an existing ISpecialSpawnsStructure for its spawn list.
Template and jigsaw replacement hooks replace authored marker blocks with their
final states. These pieces and settings must not be counted as extra families.
Their effects belong to consuming families' mob/spawn attributes.

The dynamic resource wrapper posts an early reload event. DynamicResourcesInternals
starts with empty provider/generator collections and runs consumer registrations;
RegHelperImpl likewise drains a caller-populated initialization queue. Moonlight's
common initialization installs config, trade, color, fluid, map, network and
consumer event facilities. Its global datapack folder is an external pack source,
not bundled authored content or evidence that an extra pack was selected.
ModLootModifiers registers add/replace-item codec types, not a populated loot
modifier payload. External consumers remain attributed through their own providers.

The other hooks handle existing blocks and entities: optional block entities,
item placement, grindstone triggers, inventory death events, lightning/fire,
piston movement, bee pollination, shearing, extinguishing, fake-level support,
villager AI callbacks, teleport history, configuration/resource conditions and
map/debug data. The place-structure command hook only sends debug information
about the structure already placed. Map data and packet hooks manage markers and
synchronization, not site generation. Client hooks and the client fluid helper
support rendering and resource handling. No independent Moonlight family is added.
Stop generic map, network, recipe, trade and helper tracing here. This does not
claim general compatibility, correctness of every utility, or gameplay acceptance.

All six new captures reproduce exactly in their independent r1 directories.
Their READMEs retain extraction commands and identity hashes. Focused validation:

```sh
uv run pytest -q tests/item8/test_moonlight_provider_scope.py
uv run ruff check tests/item8/test_moonlight_provider_scope.py tools/inspect_item8_pool_elements.py
uv run basedpyright tests/item8/test_moonlight_provider_scope.py tools/inspect_item8_pool_elements.py
```

One focused case and scoped Ruff/Basedpyright pass. Whole providers: 132 resolved,
4 open. Working groups remain 410 and explicit provisional Moog decisions remain
100. Canonical reconciliation, required attributes and final Item 8 acceptance
remain incomplete.

## owo-lib provider closure

The retained archive SHA-256 is
de6ed336bd80154b7241a7b3276694befc1c94550add8bcdfe7f82e5172fd13d.
It has 492 classes, no packaged data or NBT templates, two automatic mod entries
and one annotation-processor service. The mixin config declares 40 common hooks,
one server hook and 45 client entries, with no plugin. The networking mixin also
appears in the client list; this is not a separate content provider.

Source increments 37dfc1f7, bcfb3b59 and c34ff986 preserve 50 classes. The main
entry installs LootOps callbacks and networking; the client entry installs screen,
config, item-group, UI and shader support. ConfigAP processes Java configuration
annotations to generate wrapper source at compile time, not world generation.
LootOps.ADDITIONS and TagInjector.ADDITIONS start empty and are populated through
caller-supplied item/table/tag inputs. Registry mutation methods similarly act on
supplied entries. These are shared APIs, not independent structure registrations.

Copenhagen hooks existing ore placement. It records selected ore positions and
reapplies their block states after the ore pass. Maldenhagen's selected-block set
starts empty and is filled by callers. This is an ore behavior, not an authored
site family. Do not mistake world-level block writes alone for site generation.
Other common hooks cover serialization and codec errors, item components, creative
groups, inventory/screen synchronization, recipe remainders, player-data and
advancement save callbacks, text codecs, usage statistics and slot access.
The level-info tweak guards development game-rule changes; the EULA hook handles
console agreement. Neither establishes world-generation content or substitutes
for the frozen runtime lifecycle evidence. Debug commands and wisdom logging do
not register generated families. Stop generic network, debug and utility tracing.

Six nested libraries have no data, templates or deeper archives. Five are Endec,
Gson/Jankson adapters, Jankson and Netty serialization support, with no Minecraft
class references or automatic entries. The sixth is Fabric API base. Its archive
hash differs from the prior retained Fabric bundle, but all 17 class paths and
bytes match that already-audited module exactly, including its generated entry.
Reuse fabric-base-entry and the Fabric provider disposition. Do not recapture or
infer which archive wins resolution from byte equivalence. The focused test binds
this comparison to both retained parent identities. No independent family is added.

All three captures reproduce exactly in independent r1 directories. Their README
commands retain the extractor and manifest identities. Reproducible checks:

```sh
uv run pytest -q tests/item8/test_owo_provider_scope.py
uv run ruff check tests/item8/test_owo_provider_scope.py tools/inspect_item8_pool_elements.py
uv run basedpyright tests/item8/test_owo_provider_scope.py tools/inspect_item8_pool_elements.py
```

Two focused cases pass. Ruff requested iterable unpacking in one test expression;
that style correction was applied and scoped Ruff/Basedpyright pass. Provider
membership is resolved, not general library or gameplay correctness. Whole
providers: 133 resolved, 3 open. Working groups remain 410 and explicit provisional
Moog decisions remain 100. Final canonical membership and attributes remain open.

## ServerCore provider closure

The retained archive SHA-256 is
5d3b3ac3fc61ef304af929cec2637481eed211fc694d6074258e02abbcfe3467.
It contains 692 classes, no data resources or NBT templates, one automatic mod
entry, four services and 60 declared common mixins. The plugin selects optimization
and compatibility hooks from configuration and loaded-mod checks. No client or
server-only mixin lists are declared. This records packaged possibilities, not a
claim that every conditional hook is active.

Sources 5fbd3211, 57d2f8b8, a181a2df, 6ea01b7a and b1076151 preserve 70 classes.
All entry/service/plugin boundaries and 60 hooks are bound by the focused test.
The two platform services supply environment/version/config, permissions, chunk
tick forcing and text parsing. The other two services implement shaded Adventure
text serialization. Three nested configuration libraries (Dazzleconf core, its
SnakeYAML adapter, and SnakeYAML) contain 119, 16 and 237 classes respectively.
They contain no Minecraft class references, data/templates, services or deeper
archives. They are not authored-content providers.

Startup initializes platform access and configuration. Server events reload
configuration, initialize dynamic settings, update them on ticks and reset them
on shutdown. DynamicManager adjusts existing view/simulation distances and mob
capacities. The registered command groups concern ServerCore, statistics and mob
caps. None of these paths declares independent structure content.

Feature hooks change existing entity activation/inactive ticking, breeding caps,
item/experience merging, autosave timing, movement into unloaded chunks and
villager ticking. Spawning hooks gate existing monster spawners, natural spawn
intervals, infested effects, portal random ticks and zombie reinforcements. These
are relevant mob-attribute context; no new structure family follows from them.
Do not claim unchanged encounter behavior or runtime activation solely from this
membership decision. Reuse the frozen configuration for later attribution.

Optimization hooks change existing biome and structure checks, chunk tickets,
command parsing, map/player handling, pathfinding, chunk loading, broadcasts,
cached ticking sets and random lightning/fluid/ice/snow work. StructureCheckMixin
uses an approximate position and biome eligibility to avoid some synchronous
loads; it does not construct a structure. ChunkGeneratorMixin reads existing
structure references through an available chunk or the existing manager. This
is not a new template/root registration or proof of optimization correctness.
No independent ServerCore family is added. Stop general tick/performance/helper
tracing here; performance and broad compatibility remain outside this scope.

All five source captures reproduce exactly into independent r1 directories.
Their READMEs retain reproduction commands and manifest identities. Validation:

```sh
uv run pytest -q tests/item8/test_servercore_provider_scope.py
uv run ruff check tests/item8/test_servercore_provider_scope.py tools/inspect_item8_pool_elements.py
uv run basedpyright tests/item8/test_servercore_provider_scope.py tools/inspect_item8_pool_elements.py
```

One focused case passes. One long test line was wrapped after Ruff reported it;
scoped Ruff/Basedpyright pass. Whole providers: 134 resolved, 2 open. Working
groups remain 410 and explicit provisional Moog decisions remain 100. Canonical
reconciliation, required attributes and final Item 8 acceptance remain incomplete.

## Simply Swords provider closure

Archive SHA-256: 4619dcf1501fc82c1a52acd4c88a466436f5c1d7d2bccc0932912a12b0bc5198.
The 286 classes have two automatic entries, four common mixins, two client mixins,
no mixin plugin, nested archive, service entry or NBT template. The packaged
categories are bound in test_simplyswords_provider_scope.py: item attributes,
recipes, tags, advancements, book data and one legacy plural loot_tables resource.
The legacy plural directory is not assumed to be an active 1.21.1 loot table.

Sources 295a0c93 (simplyswords-entries), 94876e7d (simplyswords-startup) and
26569325 (simplyswords-content-delegates) retain eleven classes. Each README
records the exact reproduction command and identity manifest. Independent r1
captures match. Forge initialization delegates to SimplySwords.init, which
registers items, sounds, effects, recipe types, entities, components and particles.
GemPowerRegistry defines item powers. TransformationRegistry maps blocks to item
transformations. ContainedRemnantItem.useOn consumes the held item and drops the
transformed item; checkNearbyBlocks reads nearby blocks and emits feedback.
Neither is a generated building or landmark. Common hooks act on existing
entities and players, effects, item abilities and cooldowns. Client initialization
and rendering do not supply dedicated-server structure families.

ModLootTableModifiers registers configuration-dependent chest loot callbacks.
They inspect chest paths, village eligibility, Spectrum exclusions, standard,
rare, runic and unique weights, and disabled unique weapon loot. This is an
attribute input for consuming families, not a new family. Winning frozen options
and observed loot remain separate attribution work; no universal injection or
observed reward claim is made here.

No independent Simply Swords family is added. Stop general combat, weapon and
helper tracing. Membership is resolved; family loot attribution remains required.

```sh
uv run pytest tests/item8/test_simplyswords_provider_scope.py -q
uv run ruff check tests/item8/test_simplyswords_provider_scope.py
uv run basedpyright tests/item8/test_simplyswords_provider_scope.py
```

## Grave provider closure

You're in Grave Danger archive SHA-256:
dd2142a3c6a9d5b990ab36220be482f7aa9f528755f93b8fef8996f509ddcda2.
Its 142 classes contain two automatic entries, four common and one server mixin,
two client mixins, and no mixin plugin, nested archive, service entry or NBT.
Packaged data categories and exact source bindings are reproduced by
test_yigd_provider_scope.py. Data consists of tags, two enchantments, a legacy
recipe directory, a grave block loot table and three custom grave resources.

Thirteen classes in yigd-entries (2c0a3dac), yigd-delegates (dcd64d22) and
yigd-resources retain startup, common/server hooks, registered event handlers and
custom resource consumers. Each capture README records the extractor revision,
command and manifest hash; independent r1 captures match exactly.

Startup registers grave blocks/items, block entities, attachments, components,
networking, commands and event handlers. ServerEventHandler handles player death,
inventory drops, respawn, player positions and saved death data. YigdServerEventHandler
handles grave creation eligibility, placement positions, recovery and drop rules.
These are player-death recovery mechanics, not independently generated authored sites.
EndPlatformFeatureMixin changes the existing End platform block predicate to include
graves. LevelChunkMixin notifies a removed grave block entity. Compass and spawn
protection hooks concern grave recovery. RegistryDataLoaderMixin conditionally
cancels the provider's enchantment loads, not structure registry entries.

The custom loaders read grave_shape.json into the grave block shape, graveyard.json
into grave coordinates, and grave_areas.json into drop-rule overrides. Packaged
graveyard coordinates and override areas are empty. The grave shape is block-model
geometry, not a building template. The grave block loot table returns the grave
item and conditionally copies components for Silk Touch. It is not chest loot.
No independent family is added. Stop general recovery, networking and command
tracing. These dispositions close the final retained-provider membership row.

```sh
uv run pytest tests/item8/test_yigd_provider_scope.py -q
uv run ruff check tests/item8/test_yigd_provider_scope.py
uv run basedpyright tests/item8/test_yigd_provider_scope.py
```

All 136 retained providers now have supported dispositions. The remaining membership
work is canonical reconciliation: 100 explicit provisional Moog grouping decisions,
plus reconciliation of the recorded nonregistry contributions with the existing
working groups. Neither 887 roots nor 410 working groups is a final family count.
The required attributes and final Item 8 acceptance also remain incomplete.

The focused grave provider test passes. Ruff reported one long assertion, which
was wrapped; scoped Ruff and Basedpyright pass after that formatting correction.

## Finite canonical reconciliation queue after provider closure

Checkpoint: provider closure 7a7e1b5f. The exact source is family-decisions.json,
SHA-256 f27120a993441bfcd3ab8716022f8dc8a0cf547e161dd766471edf1498156ccb.
The following 100 group records explicitly say either "provisional" or
"not a final canonical-family decision" in their rationale. This is a grouping
review queue, not 100 missing families. It does not automatically certify the
other 310 groups: final reconciliation must account for every one of the 887
runtime roots exactly once, distinguish variants and components, and incorporate
the recorded nonregistry family decisions without duplicate membership.

### Moog's Soaring Structures: 25 decisions

- `mss:arena`
- `mss:calcite_house`
- `mss:castle_ruin`
- `mss:castle_tower`
- `mss:desert_pyramid`
- `mss:desert_well`
- `mss:diorite_house`
- `mss:frozen_pond`
- `mss:jungle`
- `mss:large_tower`
- `mss:leaf_hollow`
- `mss:mangrove`
- `mss:muddy_water_hole`
- `mss:mushroom`
- `mss:nether_portal`
- `mss:palm_island`
- `mss:red_sand`
- `mss:small_deepslate_house`
- `mss:small_oak_house`
- `mss:small_pond`
- `mss:small_tower`
- `mss:spruce_huts`
- `mss:taiga`
- `mss:volcano`
- `mss:white_house`

### Moog's Nether Structures: 22 decisions

- `mns:copper_tower`
- `mns:crimson_forge`
- `mns:dragon_arena`
- `mns:giant_skull`
- `mns:grave_yard`
- `mns:large_arena`
- `mns:large_house_1`
- `mns:lava_pool`
- `mns:mega_fortress`
- `mns:nether_tower`
- `mns:nether_wart_farm`
- `mns:ruined_portal`
- `mns:sandy_skull`
- `mns:shrine`
- `mns:small_arena`
- `mns:smoking_shrine`
- `mns:soul_fire`
- `mns:sword`
- `mns:train`
- `mns:warped_dome`
- `mns:warped_house`
- `mns:warped_pool`

### Moog's Voyager Structures: 53 decisions

- `mvs:azelea_house`
- `mvs:barn`
- `mvs:beach_bar`
- `mvs:bee_dome`
- `mvs:bench`
- `mvs:cartographer_tower`
- `mvs:castle_ruins`
- `mvs:cathedral`
- `mvs:crimson_enchanting_table`
- `mvs:crystal`
- `mvs:deepslate_house`
- `mvs:desert_house`
- `mvs:desert_pump`
- `mvs:duck`
- `mvs:flower_hole`
- `mvs:fox_hut`
- `mvs:gallows`
- `mvs:haystack`
- `mvs:horse_pen`
- `mvs:house`
- `mvs:jungle_tower`
- `mvs:lamp_chest`
- `mvs:large_mushroom`
- `mvs:large_warped_tower`
- `mvs:lecturn_garden`
- `mvs:log_ruin`
- `mvs:mushroom_statue`
- `mvs:nether_devil`
- `mvs:ocean_tower`
- `mvs:out_house`
- `mvs:paths`
- `mvs:pile`
- `mvs:railway`
- `mvs:red_tower`
- `mvs:ruined_beacon`
- `mvs:shed`
- `mvs:small_pillager_tower`
- `mvs:small_ruin`
- `mvs:small_ship`
- `mvs:small_swamp_house`
- `mvs:snowy_dog_hut`
- `mvs:snowy_fossil`
- `mvs:statue_ruins`
- `mvs:stone_fountain`
- `mvs:stone_pillars`
- `mvs:sunzi_gate`
- `mvs:tall_house`
- `mvs:tree_monument`
- `mvs:villager_statue`
- `mvs:warped_house`
- `mvs:wheat_grain_bin`
- `mvs:windmill`
- `mvs:wooden_wheat_farm`

### Nonregistry reconciliation input

There are 33 existing contribution records in non_registry_content.contributions.
These include accepted families, components and explicit exclusions. They are not
33 open providers or 33 additional families. Reuse their recorded dispositions;
resolve their representation in the canonical list and any membership conflicts.
The exact contribution keys are:

- `yungsbridges:bridges`
- `yungsextras:feature_entrypoints`
- `betterendisland:platform_gateway`
- `quark:spiral_spire`
- `quark:fairy_ring`
- `quark:fallen_log`
- `quark:monster_box`
- `quark:nether_obsidian_spike`
- `quark:underground_styles`
- `quark:vegetation`
- `quark:stone_generation`
- `village_taverns:village_components`
- `chefsdelight:village_components`
- `deep_aether:totem`
- `betterend:crashed_ship`
- `explorations:scarecrow`
- `tectonic:underground_river/lanterns`
- `terralith:cave/frostfire/frostfire_ceiling`
- `explorations:large_mushroom`
- `biomesoplenty:anomaly`
- `biomesoplenty:monolith`
- `biomesoplenty:bone_spine`
- `biomesoplenty:big_pumpkin`
- `biomesoplenty:pumpkin_patch`
- `betterend:ruined_obsidian_pillar`
- `betterend:lantern_woods/light_1`
- `betterend:blossoming_spires/house`
- `betterend:biome_buildings`
- `betterend:biome_ruins`
- `aether:holiday_tree`
- `deep_aether:fallen_tree`
- `regions_unexplored:fallen_tree`
- `supplementaries:cave_urn_cache`

This reconciliation is done when the named canonical list accounts for all runtime
roots and these contributions, with no unresolved membership decision or duplicate
family. Attribute completion is a separate remaining Item 8 requirement. Do not
resume generic provider audits or add another measurement system for this queue.

## Soaring house and tower membership decisions

Ten decisions in family-decisions.json now have explicit built-form rationales.
The six houses are calcite_house, diorite_house, small_deepslate_house,
small_oak_house, spruce_huts and white_house. The four tower/ruin designs are
castle_ruin, castle_tower, large_tower and small_tower. None is merged solely by
shared material, theme or generic jigsaw codec. Paired huts and modular lower,
side and top pieces remain components of their parent design.

The manually inspected houses and towers sheets under sources/soaring-design-views-r3
are hash-bound in each decision. Existing packaged summaries preserve furnishings
and authored entities. Existing complete pool traces identify attached pieces;
the views show selected main templates rather than pretending to render complete
assemblies. No generated-world size, successful placement or gameplay claim is
introduced. See the decision rationales for the specific built-form distinctions.

The historical 100-name checkpoint above remains dated context. Current explicitly
provisional remainder: 90 (Soaring 15, Nether 22, Voyager 53). The working family
count remains 410 until all canonical and nonregistry reconciliation is complete.

```sh
uv run pytest tests/item8/test_family_decisions.py -q
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

All 73 existing family-decision tests pass, with scoped Ruff and Basedpyright
passing. Diagram evidence d07a3b79 was delivered after an HTTP 408 on the first
push; retrying the same commit with an 8 MiB HTTP post buffer succeeded and the
delivered ref was verified before committing these dependent decisions.

Working inventory regenerated from 42246219. Independent r1/r2 outputs match
byte for byte. Inventory SHA-256: a05f8a0d5645a7a36b074b8ba29474d4a2dffe87efcd8cef0ff21e488c56e7a9.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-soaring-houses-towers-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-soaring-houses-towers-r2.json
```

## Soaring pond variants

The frozen_pond and small_pond roots now form mss:pond. The manually inspected
landscape sheet shows the same focal pond-island motif with different climate,
scale, edging and decoration. Both packaged templates have empty entity and block
entity lists. The cultivated patch in small_pond and fence/rock decoration in
frozen_pond remain variants. The chambered muddy_water_hole encounter is separate.
The exact definitions remain in the variant map: snowy versus general Overworld
biome tags, different height intervals, assembly sizes 2 and 1, and separate pools.
These are preserved differences, not normalized away or treated as identical inputs.

The focused merge regression verifies both definitions against packaged data,
unique root membership, empty authored entity/block-entity lists and evidence
hashes. Nineteen affected family tests pass, with scoped Ruff and Basedpyright
passing. Explicit provisional remainder is 88. The source decision list now has
409 working groups; the derived inventory awaits the next regeneration.

```sh
uv run pytest tests/item8/test_family_decisions.py -q -k 'soaring_pond or authored_designs or soaring_rivers'
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
```

## Remaining Soaring design decisions

The remaining thirteen Soaring rationales now bind the selected pool graph,
packaged contents and inspected views where applicable. The pyramid, well and
portal retain distinct built forms. Jungle, leaf hollow, mangrove, muddy water
hole, mushroom, palm island, red sand, taiga and volcano retain their documented
site arrangements; furnishings and encounter contents prevent treating their
landscape names as vegetation exclusions. The individual rationales state the
specific comparisons, components and limitations. This is an interpretive site
design grouping, not a claim that a different biome or template guarantees a family.

Arena is one connected 21-template encounter assembly. Its ordinary/trial spawners,
vaults and authored bogged are components of that site. The versioned pool elements
for pieces 2, 3 and 4 select the original paths on 1.21.1. The 1_21_9 alternatives
in the same resources do not change membership or add live templates on this stack.
No new arena view or measurement was required to establish its assembly boundary.

Soaring now has 26 working canonical groups covering all 35 runtime roots, including
the existing tree and river variant groups and the new pond group. No Soaring
rationale remains explicitly provisional. The remaining explicit queue is 75:
Nether 22 and Voyager 53. Overall source groups remain 409. Nonregistry reconciliation,
all required attributes and final Item 8 acceptance remain incomplete.

All 74 existing and directly affected family-decision cases pass. Scoped Ruff
and Basedpyright pass for the inventory builder.

```sh
uv run pytest tests/item8/test_family_decisions.py -q
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Inventory refreshed from cc8343cb after all Soaring membership decisions. Both
independent outputs match byte for byte. SHA-256: c6342abc3852f2562aa83ddacd828a274ee4e9ef5cabbe5231f904ec82f4d54d.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-soaring-settled-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-soaring-settled-r2.json
```

## Nether paired family decisions

Eight Nether decisions now have explicit layout/content rationales: giant_skull,
sandy_skull, shrine, smoking_shrine, copper_tower, nether_tower, lava_pool and
warped_pool. The two inspected sheets in sources/nether-pair-views are bound in
their evidence alongside the full template catalog and existing pool traces.
The skull forms, shrine plans, tower arrangements and pool upper/lower compositions
are distinct. Neither material, size, shared naming nor generic generation code
alone establishes these boundaries. Lower pool templates remain components.

These decisions add no runtime measurements or attribute-completion claims.
The remaining explicit queue is 67 (Nether 14, Voyager 53). Overall working
groups remain 409. The derived inventory will be refreshed from these decisions.

The affected Nether source-binding case passes, as do scoped Ruff and Basedpyright.

```sh
uv run pytest 'tests/item8/test_family_decisions.py::test_authored_designs_bind_roots_settings_and_missing_components[mns:]' -q
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Inventory regenerated from 282e291c. Both independent runs match byte for byte.
SHA-256: dbd33667b810b11f4d1b83d60f958ade966fa2bea31c5ce8720663761379971a.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-nether-pairs-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-nether-pairs-r2.json
```

## Nether house and forge boundaries

The forge, large house and warped-house decisions are settled, along with the
medium-house record's explicit relationship to the latter two. The forge is an
open workshop, the medium variants share a compact gabled form, the large house
is a hall-and-tower composition, and the warped variants share an upright framed
form. The six warped templates are equal-weight alternatives of one family.
No new family is counted for their different furnishings or slight size variation.

The inspected source sheets in sources/nether-house-views and the full packaged
catalog are hash-bound to these four records. The existing graph binds the selected
1.21.1 large-house version. This settles three explicitly provisional decisions;
the medium family was already grouped but its relationship note required closure.
Remaining explicit queue: 64 (Nether 11, Voyager 53). Working groups remain 409.
Attribute and generated-world claims remain separate, and the inventory refresh
follows this decision increment.

Eight affected cases pass; scoped Ruff and Basedpyright pass.

```sh
uv run pytest tests/item8/test_family_decisions.py -q -k 'mns or moog_modular_variants'
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Inventory refreshed from e11fe710 and independently reproduced byte for byte.
SHA-256: 2c45fab771257defa1c76dfcf8c52b0193ba8d72a73b22cacf241d254c82698a.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-nether-houses-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-nether-houses-r2.json
```

## Nether arena and fortress boundaries

Small and large arenas now form mns:arena with two explicit architectural layouts.
The inspected pieces share a walled fighting-court motif with galleries and entrance
structures. The larger multilevel layout, trial/vault fixtures and different mobs
are variant attributes. Shared mob templates alone were not the grouping basis.
The exact small/large definitions and selected template sets remain in the variant
map, including lowest-land versus fixed-height placement, liquid eligibility and
carving differences. The direct regression checks these inputs against preserved
sources, unique root ownership and the shared mob-only template intersection.

The dragon arena remains separate: its head/body/limb construction above a broad
platform is a sculptural encounter design rather than another walled court layout.
Its seven upper, thirteen lower and four mob templates are components. The fortress
remains one branching furnished complex with 196 reachable alternatives, including
rooms, passages, crossings, stairs and encounter modules. Neither reachable count
is a per-instance observation. Boundary exemptions, terrain adaptation, spawn
overrides and version selection remain preserved in the source records.

Nine affected cases pass, with scoped Ruff and Basedpyright passing. Explicit
provisional remainder: 60 (Nether 7, Voyager 53). Source working groups: 408.
The derived inventory refresh follows this increment. Item 8 attributes, nonregistry
reconciliation, final family count and final review/merge remain incomplete.

```sh
uv run pytest tests/item8/test_family_decisions.py -q -k 'mns or moog_modular_variants or nether_arena'
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
```

Inventory regenerated from 5e5cb5e2 and independently reproduced exactly.
SHA-256: 3d9a33d0bf30fa6699bcdbfc85a5408dd2f6e5d1a5e4a2cad7a38347a69ee629.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-nether-arenas-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-nether-arenas-r2.json
```

### Nether landmark relationships, 2026-09-06

The seven remaining Nether designs retain separate families based on inspected
layouts and template contents: grave yard, wart farm, ruined portal, soul fire,
sword, train and warped dome. Existing wells retain their three root variants
and lower components. Circular encounter ruins retain their two variants and
remain distinct from generic fragments, the portal frame and the grave plot.
Source views delivered at 8d99f50c reproduce exactly. No new measurement system
was introduced. Root assignments and generation settings are unchanged.

Nine affected cases pass; scoped Ruff and Basedpyright pass. Working groups
remain 408. The explicit provisional remainder is 53, all Voyager. Provider
coverage remains 136/136. Attribute completion, nonregistry reconciliation and
final review/merge remain outstanding. Derived inventory refresh follows.

```sh
uv run pytest tests/item8/test_family_decisions.py -q -k 'mns or moog_modular_variants or nether_arena'
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Inventory regenerated from a9637207 and independently reproduced exactly.
SHA-256: f119b21e5b24961e14a1614af19f27c9c7dd8f4d1b352dcf5a496c10be15fbc3.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-nether-landmarks-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-nether-landmarks-r2.json
```

### Voyager benches, paths and harvest heaps, 2026-09-07

Views delivered at 77146722 and preserved template contents resolve four
provisional decisions. Benches retain five seating/accessory alternatives; paths
retain two landscaped route alternatives. Haystack and pile become one harvest
heap family with five material/layout alternatives across both retained roots.
The shared heap motif, rather than a common root or loot table alone, supports
the merge. Full definitions and template ownership remain in the variants map.
No functional seating, transport, observed generation or reward equality is
inferred from these source interpretations. Diagram limitations remain explicit.

Thirteen affected cases pass, including direct root/definition preservation for
the merge. Scoped Ruff/Basedpyright pass. Working groups: 407. Explicit provisional
remainder: 49, all Voyager. Nonregistry reconciliation, eleven required attributes
and final review/merge remain incomplete. Inventory refresh follows.

```sh
uv run pytest tests/item8/test_family_decisions.py -q -k 'mvs or voyager_harvest'
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
```

Inventory regenerated from 784d6923 and independently reproduced exactly.
SHA-256: ba90f9bc4a827236676bd6fd061574d149b9a3d72a74aa93dc6cc23f6b3351b2.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-voyager-small-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-voyager-small-r2.json
```

### Voyager tower and outbuilding relationships, 2026-09-07

Views delivered at b580a10f resolve six tower roots and three outbuilding roots.
Red and jungle towers share a broad tiered, buttressed and tapering composition;
they merge into one family with material, vegetation, layout and encounter
variants. Both full root definitions and all five component identities remain.
Jungle/taiga biome constraints, different size limits and terrain checks are
preserved. The comparison filename nether_towers does not establish a dimension.

Cartographer, large warped, ocean and small pillager towers retain distinct
shaft/crown, side-turret, cylindrical and open stacked-platform compositions.
Barn, shed and out-house remain distinct hall, shallow enclosure and narrow
shelter designs. Tops, lower pieces and shared villager templates are components.
Empty spawner entity objects remain unresolved. These decisions establish source
design relationships, not observed gameplay or natural spawning.

Sixteen affected cases pass, including direct merged-root definition and component
preservation. Scoped Ruff/Basedpyright pass. Working groups: 406. Explicit
provisional remainder: 40, including eight houses whose views are already inspected.
Attribute completion, nonregistry reconciliation and final review remain open.
Inventory refresh follows.

```sh
uv run pytest tests/item8/test_family_decisions.py -q -k 'mvs or voyager'
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
```

Inventory regenerated from 0eea8158 and independently reproduced exactly.
SHA-256: 22b251c84c08e77652ab4066842cbf1102e57c936a060712b299805126be52d2.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-voyager-towers-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-voyager-towers-r2.json
```

### Voyager house relationships, 2026-09-07

Eight house designs retain separate families after comparison of the existing
house/outbuilding sheets and preserved template contents. The decisions describe
roof, enclosure, frontage and support arrangements rather than relying on material
or size names. Shared villager templates remain component options. No architecture
template in this comparison has packaged spawners; the standard house's authored
item entities are not hostile inhabitants. Warped-house Overworld constraints and
the swamp-house omission of cannot_spawn_in_liquid remain preserved.

Sixteen affected cases and scoped Ruff/Basedpyright pass. No new source capture or
test machinery was needed. Working groups remain 406. Explicit provisional queue:
32, all Voyager, with its exact names in the active handoff. Nonregistry reconciliation,
required attributes and final review remain incomplete. Inventory refresh follows.

```sh
uv run pytest tests/item8/test_family_decisions.py -q -k 'mvs or voyager'
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Inventory regenerated from cf877811 and independently reproduced exactly.
SHA-256: 4ed633922ed26ff99ff681f08730e98098c1f84e0b89e0f6195f7d121d2b06c7.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-voyager-houses-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-voyager-houses-r2.json
```

### Voyager cathedral and facility decisions, 2026-09-07

The connected cathedral graph establishes one modular family; 29 reachable
templates are alternatives/components, not 29 structures per instance. Packaged
cathedral_start and ordinary corridor_8 are not selected by that graph. The
minecraft:mvs/cathedral_common references remain preserved and require effective
loot disposition during attribute completion. No namespace correction is inferred.

Eight facility layouts remain distinct after inspection of views delivered at
6178f004 and their contents: beach bar, enchanting installation, pump depiction,
horse pen, lamp cache, lectern garden, raised grain bin and wheat plot. Their
functional blocks and loot references remain attributed to their templates; no
observed animal presence, machinery throughput or production loop is inferred.

Sixteen affected cases and scoped Ruff/Basedpyright pass. Working groups remain
406; the explicit provisional remainder is 23 and all remaining views are already
inspected. Nonregistry reconciliation, required attributes and final review remain
open. Inventory refresh follows.

```sh
uv run pytest tests/item8/test_family_decisions.py -q -k 'mvs or voyager'
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Inventory regenerated from f7a27e9a and independently reproduced exactly.
SHA-256: 8119e9753a9fcbf79e581851738d0c7a8e3e797f0c6bfd325cb1d8868007dda9.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-voyager-facilities-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-voyager-facilities-r2.json
```

### Voyager shelter and sculpture decisions, 2026-09-07

Fox and snowy dog huts share one small shelter motif with biome, roof, ground and
accessory variants. Both complete definitions and root-specific templates remain
in animal_hut. The existing small-variant preservation test now also covers this
merge. Neither template authors an animal. Bee dome remains a distinct glazed
apiary enclosure, with hive block entities rather than an inferred bee count.

Large mushroom remains an authored constructed landmark based on its crafted
materials and broad cap/stalk layout. It is distinct from the narrow pedestal
mushroom figure. Duck, horned devil, villager and skeletal-arch fossil designs
retain their different sculptural compositions. No authored mob is inferred from
any sculpture name. The existing source views and template contents suffice.

Seventeen affected cases and scoped Ruff/Basedpyright pass. Working groups: 405.
Explicit provisional remainder: 14. Attribute completion, nonregistry reconciliation
and final review remain open. Inventory refresh follows.

```sh
uv run pytest tests/item8/test_family_decisions.py -q -k 'mvs or voyager'
uv run ruff check tests/item8/test_family_decisions.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_family_decisions.py tools/build_item8_inventory.py
```

Inventory regenerated from dee267e2 and independently reproduced exactly.
SHA-256: be6481c55cce473a269696c513fa580e699ff9b93530ff9231bcb8f06a31307d.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-voyager-sculptures-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-voyager-sculptures-r2.json
```

### Final Voyager provisional decisions and broader backlog correction, 2026-09-07

Fourteen remaining Voyager ruins and landmarks retain distinct inspected design
compositions. Root assignments are unchanged. Crystal lower and shared ship
villager templates remain components. Ruined beacon has no packaged beacon block;
railway contains actual rail blocks; neither a working network nor moving ship or
windmill is inferred. Seventeen affected cases and scoped quality checks pass.
Working groups remain 405. Explicit Voyager provisionals: zero.

This does not close canonical reconciliation. Manual inspection of rationale
sentences mentioning canonical, related-design or replacement relationships that
remain open or require reconciliation identifies 128 existing records below.
The earlier explicit-provisional queue was incomplete as an overall progress
measure. These are records to reconcile, not 128 newly discovered families. Some
contain dependency, replacement or exclusion questions rather than layout questions.
Use the existing evidence and resolve each actual note; do not mechanically erase
boilerplate or assume registry membership proves generation. Nonregistry records
and required attributes also remain open.

- adorabuild_structures (31): acacia_well, ancient_palace, bamboo_campfire, basalt_chambers, birch_beehive, blackstone_bastion, blackstone_temple, buried_sand_castle, dark_oak_mansion, end_bubble, end_gateway, end_ship, end_temple, frozen_shelter, house, library, mountain_mine, mushroom, nether_fortress, nether_fossil, nether_portal, nether_temple, ocean_bubble, ocean_temple, prison, red_sand_temple, sand_castle, sand_pyramid, tree, tree_house, watercraft
- aether (4): bronze_dungeon, gold_dungeon, large_aercloud, silver_dungeon
- creatingspace (4): mars/underground_outpost_1, moon/abandoned_outpost, moon/crashed_rocket, moon/crashed_ship
- deep_aether (4): altar_camp, brass_dungeon, campfire, combiner_corridor
- idas (62): abandoned_lighthouse, abandoned_vineyard, abandonedhouse, ancient_mines, ancient_portal, ancient_statue, animal_den, apothecary_abode, ars_nouveau/archmages_tower, bazaar, bearclaw_inn, beekeepers_house, botanist, brickhouse, castle, collectors_museum, cottage, desert_camp, desert_market, desert_pyramid, desert_ruins, dig_site, enchantingtower, farmhouse, fishermans_lodge, frozen_crypt, haunted_manor, hermits_hollow, hunters_cabin, iceandfire/dread_citadel, iceandfire/sirens_cove, labyrinth, lumber_camp, mason_house, necromancers_spire, nether_pump_camp, nexus, pillager_camp, pillager_fortress, pumpkin_cafe, redhorn_guild, ruined_church, ruined_fort, ruined_well, ruins_of_the_deep, snifferhenge, sunken_ship, sunken_ship/sunken_ship_ruins, the_log, tinkers_citadel, tinkers_workshop, train_ruins, tree_of_wisdom, treetop_tavern, tudor_pub, underground_camp, wacky_wares, washing_camp, windswept_shrine, winter_wagon, witches_treestump, wizard_tower
- illagerinvasion (5): firecaller_hut, illager_fort, illusioner_tower, labyrinth, sorcerer_hut
- integrated_stronghold (1): stronghold
- terralith (16): desert_outpost, fortified_village, glacial_hut, igloo, mage_complex, mage_tower, rubble, spire, underground/frosted_dungeon, underground/giant_bee_hive, underground/mining_outpost, underground/old_refinery, underground/sunken_tower, underground_cabin, valley_lodge, witch_hut
- towns_and_towers (1): village

```sh
uv run pytest tests/item8/test_family_decisions.py -q -k 'mvs or voyager'
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Inventory regenerated from cb74b266 and independently reproduced exactly.
SHA-256: 047dc079c1a85e503cf313d9accc1cf3cd7b18e44c0a345e6557615fe3af33db.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-voyager-final-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-voyager-final-r2.json
```

### Canonical exclusion and eligibility reconciliation, 2026-09-07

Four family records now agree with the existing source and eligibility evidence.
Aether large_aercloud is a provider-selected cold-aercloud block formation and is
excluded from authored families. Its reuse as Silver Dungeon cloud bedding does
not make another dungeon family. The record and source attributes remain retained.

Deep Aether altar_camp, campfire and combiner_corridor each select one same-named
Sacred Lands template, but their required biome is absent from every captured
dimension. The captured jigsaw consumer follows the supplied pool. They remain
registered inactive candidates, excluded from active families in this frozen
baseline. Changed packs/dimensions or a demonstrated independent route reopen this
disposition. No root was deleted and no broad generation claim was inferred.

Ten existing source/eligibility cases and scoped quality checks pass. No new
capture, renderer or measurement was added. The named canonical backlog decreases
from 128 to 124. Working coverage groups remain 405; this is not the final authored
family count. Nonregistry reconciliation and required attributes remain open.

```sh
uv run pytest tests/item8/test_aether_cloud_source.py tests/item8/test_totem_scope.py tests/item8/test_deep_aether_candidates.py -q
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Inventory regenerated from b325116a and independently reproduced exactly.
SHA-256: 0f3970e1c9d3310e3c4b0de48c3a6c5b5032bc8dadfae2a32b03aab0fd44a7e7.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-cloud-sacred-lands-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-cloud-sacred-lands-r2.json
```

### IDAS optional dependencies and adaptive pools, 2026-09-07

Captures b9d76078 and 82b5f4ec bind OptionalDependencyStructure's rejection branch,
its inherited JigsawStructure caller and the PlatformHooks to NeoForge ModList
lookup. The existing parser and hash-verified registry-run debug log show neither
ars_nouveau nor iceandfire loaded. Archmages tower, dread citadel and sirens cove
remain registered inactive candidates, excluded from active canonical families.
Their roots and missing-component evidence remain preserved.

ModAdaptiveStructure changes pools only when every named change mod is loaded.
The three IDAS adaptive roots therefore retain default pools; their alternate
compatibility pieces are not new families. Their broader design reconciliation
remains open, so this does not reduce that portion of the backlog.

Four affected cases and scoped Ruff/Basedpyright pass. The source captures reproduce
exactly. Canonical-note backlog: 121, down from 124. Coverage groups remain 405.
No world experiment or new measurement system was added. Inventory refresh follows.

```sh
uv run pytest tests/item8/test_idas_provider_scope.py tests/item8/test_family_decisions.py -q -k 'idas or optional_dependencies'
uv run ruff check tests/item8/test_idas_provider_scope.py tools/build_item8_inventory.py
uv run basedpyright tests/item8/test_idas_provider_scope.py tools/build_item8_inventory.py
```

Inventory regenerated from b296565c and independently reproduced exactly.
SHA-256: 9c4475699659ebec70769cb33202dea7679a4657f09cfc56c3808e60743396fe.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-idas-dependencies-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-idas-dependencies-r2.json
```

### Stronghold replacement and fortified-village reconciliation, 2026-09-07

Integrated Stronghold and Better Strongholds each reject vanilla STRONGHOLD normal
generation. Their own roots use integrated_api:generic_structure and
yungsapi:yung_jigsaw respectively, so neither matches these vanilla-type filters.
The two custom assemblies remain separate families; vanilla remains a suppressed
candidate. The artificial locate position and effective Eye of Ender tag selection
are not structure observations or proofs of generation. Missing components remain.

Both Terralith fortified-village roots are suppressed by the already bound frozen
Integrated Villages setting and exact-key hook. Their family record now records
that inactive disposition while preserving both variants and missing pieces.
Command placement and pre-existing structures remain outside the normal-generation
claim. No new source capture or experiment was required.

Thirteen affected cases and scoped quality checks pass. Named canonical backlog:
119, down from 121. Coverage groups remain 405, including inactive candidates.
Nonregistry reconciliation and required attributes remain open.

```sh
uv run pytest tests/item8/test_integrated_suppression.py tests/item8/test_yung_suppression.py tests/item8/test_integrated_stronghold_provider_scope.py tests/item8/test_family_decisions.py -q -k 'suppression or stronghold'
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Inventory regenerated from 2eb64661 and independently reproduced exactly.
SHA-256: 400b5d2608332439e6dcf1e738d335f7f23f72cae9364cda5d33573657549e42.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-replacement-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-replacement-r2.json
```

### Creating Space design reconciliation, 2026-09-07

Existing template contents and root graphs distinguish the Mars drill-and-pulley
installation, Moon upper-building/fluid-machinery basement installation, compact
engine-and-flight-recorder rocket wreck, and broad sliding-door ship wreck.
Bastion legs are reused components; the Moon installation top and basement are
connected pieces. These four records retain separate design identities. Source
machinery does not prove operation, occupants or effective placement. No new
capture, rendering pass or measurement was needed.

The existing affected case and scoped checks pass. Canonical-note backlog: 115,
down from 119. Coverage groups remain 405. Remaining named records by provider:
IDAS 59, AdoraBuild 31, Terralith 15, Illager Invasion 5, Aether 3, Deep Aether 1,
and Towns and Towers 1. Nonregistry reconciliation and required attributes remain.

```sh
uv run pytest tests/item8/test_family_decisions.py -q -k creatingspace
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Inventory regenerated from 9f172cf6 and independently reproduced exactly.
Only the four Creating Space grouping decisions and the decision input identity
changed. SHA-256: 37a685b6856bbb9fd5161b5db855639eec30d01493222d3de968d6b45fd6361c.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-creatingspace-designs-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-creatingspace-designs-r2.json
```

### Illager Invasion design reconciliation, 2026-09-07

Five design records retain their distinct boundaries. Firecaller is a base-plate
farm compound; sorcerer is a standalone hut. The fort has one architectural root;
illusioner has three equal-weight tower alternatives with common dimensions,
principal construction materials and stacked encounter elevations. Labyrinth
connects its tower to halls and room alternatives. Shared mob templates remain
components. Existing graphs and template contents suffice; no new source capture,
rendering or measurement was added. Provider replacement-component dispositions
remain unchanged. Effective gameplay and placement attributes remain open.

Three affected cases and scoped checks pass. Canonical-note backlog: 110, down
from 115. Coverage groups remain 405. The remaining named records are IDAS 59,
AdoraBuild 31, Terralith 15, Aether 3, Deep Aether 1 and Towns and Towers 1.

```sh
uv run pytest tests/item8/test_illagerinvasion_provider_scope.py tests/item8/test_family_decisions.py -q -k illagerinvasion
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Inventory regenerated from edd0bf75 and independently reproduced exactly.
Only the five Illager Invasion grouping decisions and the decision input identity
changed. SHA-256: 8a68f25b473a8e8e2b6cee131886202efdb2e1035b56bb64cd09a46c215c7257.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-illager-designs-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-illager-designs-r2.json
```

### Aether dungeon design reconciliation, 2026-09-07

Existing custom-entry, builder/piece and template evidence supports four separate
assemblies: Bronze connected rooms/tunnels, Silver multi-floor building, Gold
island/chamber, and Deep Aether Brass rotated rooms with upper parts and a door.
Shared cloud bedding is supporting terrain. The Brass processor's bronze naming
does not alias its own assembly to Bronze. Silver test_door remains unselected
in the inspected paths. Selected room alternatives and boss forms remain components.
These decisions bind already delivered sources, not new captures or measurements.
Successful assembly, placement and effective gameplay attributes remain unproven.

Six affected cases and scoped quality checks pass. Canonical-note backlog: 106,
down from 110. Remaining named records: IDAS 59, AdoraBuild 31, Terralith 15, Towns
and Towers 1. Coverage groups remain 405, not a final active authored-family count.
Nonregistry contribution reconciliation and required attributes remain open.

```sh
uv run pytest tests/item8/test_aether_bronze_components.py tests/item8/test_aether_cloud_source.py tests/item8/test_deep_aether_candidates.py -q -k 'bronze or silver_gold or brass or packaged_candidate_partition'
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Inventory regenerated from f9705ace and independently reproduced exactly.
Only the four dungeon grouping decisions and the decision input identity changed.
SHA-256: 36a7af5025bf1800f3cd7b32f6c6965949ae48bc736229ad751aa26ab768140a.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-aether-designs-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-aether-designs-r2.json
```

### Towns and Towers settlement reconciliation, 2026-09-07

The village group retains all 26 full root variants under the same settlement
convention used for CTOV and Integrated Villages. Existing template content binds
the unusual members: trader meeting point with tents, llama pens and authored
traders; grove building with beds, workstations and village inhabitants; snowy inn
with beds, inhabitants and decor. These are settlement architecture variants,
not an assertion of identical layouts or peaceful population. Piglin/brute spawn
overrides remain explicit. The ocean ship remains a separate design. Vanilla-ID
replacements remain components of their consuming vanilla family, not aliases
of these independent roots. Missing components and effective attributes remain.

Three affected cases and scoped checks pass. Canonical-note backlog: 105, down
from 106. Remaining named records: IDAS 59, AdoraBuild 31 and Terralith 15. Coverage
groups remain 405. No new capture, rendering or measurement was needed.

```sh
uv run pytest tests/item8/test_towns_towers_provider_scope.py tests/item8/test_family_decisions.py -q -k 'towns or towers'
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Inventory regenerated from 420fe50f and independently reproduced exactly.
Only the village grouping decision and the decision input identity changed.
SHA-256: 79129d05f74bb755e2ce3b847df40b51c03aac486ebd2429383e5359362410dc.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-towns-designs-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-towns-designs-r2.json
```

### Terralith encounter/cache design reconciliation, 2026-09-07

Four records now bind existing template contents and component graphs. Spire is
one connected assembly with loot and spawners in its base halves, not terrain
alone. Frosted dungeon is a distinct deepslate chamber with a stray spawner.
The underground hive templates are alternatives with dedicated loot barrels;
the decorative hive lacks those cache contents and is not selected by this root.
Both witch-hut roots share one template while preserving eligibility and spawn
input differences. Neither names nor generation-step labels prove exposure.

The affected existing case and scoped quality checks pass. Canonical-note backlog:
101, down from 105 (IDAS 59, AdoraBuild 31, Terralith 11). Coverage groups remain
405. No new capture or measurement was added. Remaining building and rubble
comparisons, required attributes and nonregistry reconciliation remain open.

```sh
uv run pytest tests/item8/test_family_decisions.py -q -k terralith
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Inventory regenerated from d2213481 and independently reproduced exactly.
Only the four Terralith grouping decisions and the decision input identity changed.
SHA-256: 555f07790ee25963ece0b361fe1ca49cf29fec08b1d2bb99284d4597c8b5f4da.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-terralith-encounters-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-terralith-encounters-r2.json
```

### Terralith rubble design reconciliation, 2026-09-07

All six biome sets retain corresponding small, medium and large authored ruin
alternatives. Existing templates bind brushable blocks to common trail-ruins loot;
large alternatives also bind decorated pots to rare trail-ruins loot. Medium pots
lack that rare-loot binding. Matching size envelopes and corresponding masonry,
timber, sign and vegetation substitutions support one family with material and
size variants. These are authored archaeological caches, not terrain-only rubble.
Effective exposure and reward behavior remain unproven. No new capture or
measurement was needed.

The affected case and scoped checks pass. Canonical-note backlog: 100, down from
101 (IDAS 59, AdoraBuild 31, Terralith 10). Coverage groups remain 405. Required
attributes and nonregistry contribution reconciliation remain open.

```sh
uv run pytest tests/item8/test_family_decisions.py -q -k terralith
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Inventory regenerated from 79ed59c4 and independently reproduced exactly.
Only the rubble grouping decision and the decision input identity changed.
SHA-256: d86bac33950fd68da7afc7939df4543ecb868fa22b50273228408d4279a96cf5.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-terralith-rubble-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-terralith-rubble-r2.json
```

### Terralith building design reconciliation, 2026-09-07

The ten remaining records bind the delivered comparison sheets at 7adf45b5 and
existing templates/graphs. Surface buildings preserve the open desert compound,
extended valley lodge, compact igloo and glacial residence alternatives.
Underground designs distinguish broken-roof cabins, framed mining shelters,
elongated refinery and narrow sunken tower. Shared cabin roots and size alternatives
remain within their respective families. The five mage tower variants share their
tower form; the complex adds connected roads, barracks and houses and remains a
separate assembly. Shared mob pieces are components. Full root settings remain.

The existing affected definition/registry/evidence case and scoped checks pass.
Canonical-note backlog: 90, down from 100, comprising IDAS 59 and AdoraBuild 31.
Coverage groups remain 405. View limitations remain recorded in the source README;
these decisions do not prove generated geometry, exposure or effective gameplay.
Required attributes and reconciliation of 33 nonregistry contributions remain open.

```sh
uv run pytest tests/item8/test_family_decisions.py -q -k terralith
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Inventory regenerated from 9d75c96b and independently reproduced exactly.
Only the ten Terralith grouping decisions and the decision input identity changed.
SHA-256: 04bc241dbb692e7473df65b408f83da459dff061bf895493134e78ef14d73613.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-terralith-buildings-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-terralith-buildings-r2.json
```

### AdoraBuild small installations and furnished vegetation correction, 2026-09-07

Existing template contents distinguish the acacia well, bamboo sleeping/cooking
camp and birch apiary. The well preserves dispenser/tripwire/redstone inputs;
operation is unproven. The apiary preserves dedicated loot, hive blocks and authored
bee entities rather than being dismissed as a natural nest. These three canonical
design relationships are resolved without new capture or measurement.

The prior tree description was inaccurate: all three tree templates contain
ladders, campfires and loot chests; birch also contains masonry, bookshelves,
crafting and enchanting equipment. Cherry and oak preserve their own nest/crafting
contents. The mushroom is furnished accommodation. Both records now describe
these authored contents, but their relationships to other residence/tree-house
designs remain open. Neither is excluded as vegetation based on its filename.

The affected definition/registry/evidence case and scoped checks pass. Canonical
backlog: 87, down from 90 (IDAS 59, AdoraBuild 28). Coverage groups remain 405.
Required attributes and reconciliation of 33 nonregistry contributions remain open.

```sh
uv run pytest tests/item8/test_family_decisions.py -q -k adorabuild
uv run ruff check tools/build_item8_inventory.py
uv run basedpyright tools/build_item8_inventory.py
```

Inventory regenerated from 1ccfea35 and independently reproduced exactly.
Only the five AdoraBuild grouping decisions and the decision input identity changed.
Three records are resolved; tree and mushroom remain open.
SHA-256: 98a4a76bcae6e401ae55bb8b11e1a6883359b3a476a5e8ced8df82c39ca86c80.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-adora-installations-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-adora-installations-r2.json
```

### AdoraBuild furnished tree family boundaries, 2026-09-07

Views a052167e and preserved template contents show a substantial masonry workshop
beneath birch, distinct from cherry/oak tree-and-camp caches. The birch root moves
to birch_tree_workshop with its full definition retained. Negative offset and bury
adaptation are source inputs, not observed exposure. Cherry/oak remain variants
with their nest, loot and crafting differences. The tree-house alternatives retain
their constructed room volumes and different chest/pot elevations. The furnished
mushroom stem-and-cap residence remains a separate design.

The existing definition/registry/evidence check now expects the split and continues
to bind every root exactly once to full packaged definitions and component traces.
That case and scoped quality checks pass. Canonical-note backlog: 84, down from 87
(IDAS 59, AdoraBuild 25). Coverage groups: 406, up from 405 because of the justified
birch split. No new root or provider was introduced. Required attributes and
33 nonregistry contribution records remain open.

```sh
uv run pytest tests/item8/test_family_decisions.py -q -k adorabuild
uv run ruff check tools/build_item8_inventory.py tests/item8/test_family_decisions.py
uv run basedpyright tools/build_item8_inventory.py tests/item8/test_family_decisions.py
```

Inventory regenerated from 54e4d725 and independently reproduced exactly.
Only the three original design records, the new birch workshop record and the
decision input identity changed. Root-specific fields separate with the birch
root; all 887 roots remain covered exactly once and full variants are preserved.
SHA-256: ed705d7d330b1bae950b92245a3f8500ff4bba7415ba3e73dd1d3ca55728edd7.

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/inventory-adora-trees-r2.json
cmp evidence/item-8/inventory.json evidence/raw/item8/inventory-adora-trees-r2.json
```
