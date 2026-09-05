# Retained-provider scope pass

Status: search index delivered; candidate completeness is NOT VERIFIED.
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
| BetterEnd building lists | Six live configured-feature IDs and their mixed building/vegetation lists; selector source in 9695ae5. | Assign actual designs and variants; do not call all six lists one family or count every template separately. |
| BetterEnd crashed ship | Registered feature implementation and vanilla ship template reuse in 9695ae5. | Establish active configured/placed use before adding a family. |
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
