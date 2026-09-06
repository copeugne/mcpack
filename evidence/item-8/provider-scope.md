# Retained-provider scope pass

Status: search index delivered; candidate completeness is NOT VERIFIED.
Supported provider dispositions: 43 of 136. The exact queue below has 93 open rows.
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

## Exact provider queue, initialized at 05ce184

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
| `BetterEnd-21.0.31.jar` | `betterend-feature-scope`, `betterend-formation-pieces`, `betterend-formations-code`, `betterend-lake-helpers` | Bind six building lists and crashed-ship eligibility; separate building designs from vegetation; reconcile existing roots. |
| `BiomesOPlenty-neoforge-1.21.1-21.1.0.13.jar` | `bop-feature-scope` | Bind anomaly, monolith and bone-spine placement; settle landmark versus terrain disposition; reconcile remaining features. |
| `CreateDragonsPlus-1.11.2b.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `CreeperOverhaul-neoforge-1.21.1-4.0.6.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `DungeonsArise-1.21.1-2.1.68-release.jar` | `wda-provider-scope` | RESOLVED: see WDA structure-provider disposition below. |
| `FarmersDelight-1.21.1-1.3.2.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `GlitchCore-neoforge-1.21.1-2.1.0.2.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `IllagerInvasion-v21.1.6-1.21.1-NeoForge.jar` | `pool-codecs` | Reconcile existing roots, all components and additional feature/entry routes. |
| `LeavesBeGone-v21.1.1-1.21.1-NeoForge.jar` | `leavesbegone-provider` (69119c6), test_small_utility_provider_scope.py | RESOLVED: Leaf ticking and chunk tick persistence; no authored structure contribution. See small utility provider dispositions below. |
| `Patchouli-1.21.1-93-NEOFORGE.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `PuzzlesLib-v21.1.52-1.21.1-NeoForge.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `Quark-4.1-480.jar` | `quark-end-generators`, `quark-end-registration`, `quark-fallen-log-decor`, `quark-landmark-encounter-generators`, `quark-monster-box-behavior`, `quark-monster-box-bindings`, `quark-nether-spikes`, `quark-spire-config-annotations`, `quark-stone-clusters`, `quark-underground-base`, `quark-underground-context`, `quark-underground-fill`, `quark-underground-styles`, `quark-vegetation`, `quark-world-category` | Reuse recorded nonregistry contributions and module activation; reconcile remaining generation entries and packaged resources. |
| `TerraBlender-neoforge-1.21.1-4.1.0.8.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `Terralith_1.21.1_v2.6.2_Neoforge.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect config-conditioned overlays, function entry tags and feature definitions; reconcile 28 packaged roots and unused templates. |
| `YungsApi-1.21.1-NeoForge-5.1.6.jar` | `pool-codecs` | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `YungsBetterCaves-1.21.1-NeoForge-3.1.4.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `YungsBetterDesertTemples-1.21.1-NeoForge-4.1.5.jar` | `desert-temple-suppression` | Reconcile existing roots, all components and additional feature/entry routes. |
| `YungsBetterDungeons-1.21.1-NeoForge-5.1.4.jar` | `betterdungeons-code` | Reconcile existing roots, all components and additional feature/entry routes. |
| `YungsBetterEndIsland-1.21.1-NeoForge-3.1.2.jar` | `better-end-island-activation`, `better-end-island-configuration`, `better-end-island-exit-portal`, `better-end-island-generator-dependencies`, `better-end-island-platform-gateway`, `better-end-island-processors`, `better-end-island-spike-podium` | Reuse platform/gateway, activation and generator captures; account for remaining entries and resources. |
| `YungsBetterJungleTemples-1.21.1-NeoForge-3.1.2.jar` | `jungle-temple-suppression` | Reconcile existing roots, all components and additional feature/entry routes. |
| `YungsBetterMineshafts-1.21.1-NeoForge-5.1.1.jar` | `mineshafts-code` | Reconcile existing roots, all components and additional feature/entry routes. |
| `YungsBetterNetherFortresses-1.21.1-NeoForge-3.1.5.jar` | `fortress-suppression` | Reconcile existing roots, all components and additional feature/entry routes. |
| `YungsBetterOceanMonuments-1.21.1-NeoForge-4.1.2.jar` | `monument-suppression` | Reconcile existing roots, all components and additional feature/entry routes. |
| `YungsBetterStrongholds-1.21.1-NeoForge-5.1.3.jar` | `stronghold-suppression` | Reconcile existing roots, all components and additional feature/entry routes. |
| `YungsBetterWitchHuts-1.21.1-NeoForge-4.1.1.jar` | `witch-hut-suppression` | Reconcile existing roots, all components and additional feature/entry routes. |
| `YungsBridges-1.21.1-NeoForge-5.1.1.jar` | `yungs-bridge-generation`, `yungs-bridge-processors`, `yungs-bridges-module-default`, `yungs-bridges-module-loader` | RESOLVED: see YUNG Bridges provider disposition below. |
| `YungsCaveBiomes-1.21.1-NeoForge-3.1.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `YungsExtras-1.21.1-NeoForge-5.1.1.jar` | `yungs-extras-desert-code`, `yungs-extras-generators`, `yungs-extras-initialization`, `yungs-extras-module-default`, `yungs-extras-processor-bindings`, `yungs-extras-registration` | RESOLVED: see YUNG Extras provider disposition below. |
| `Zeta-1.1-40.jar` | `quark-enablement-callers`, `zeta-biome-modifier`, `zeta-component-biomes`, `zeta-compound-biome`, `zeta-config-binding`, `zeta-config-event-fields`, `zeta-deferred-feature`, `zeta-enablement-inputs`, `zeta-generation-applicability`, `zeta-generation-spawn`, `zeta-generator-dispatch`, `zeta-horizontal-directions`, `zeta-module-assignment`, `zeta-module-name`, `zeta-module-section`, `zeta-stone-ore` | Reuse Quark module/feature dispatch captures; reconcile remaining public generation and nested entry consumers. |
| `[Neoforge]ctov-3.6.3.jar` | `ctov-provider` (82ac234), test_ctov_provider_scope.py, selection/bundle checks, existing CTOV regressions/graphs | RESOLVED: 78 existing roots, village/outpost components, compatibility injections and processors. Disconnected and missing components accounted for below. |
| `accessories-neoforge-1.1.0-beta.53+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `adorabuild-structures-2.11.0-neoforge-1.21.3.jar` | `adorabuild-provider`, existing runtime/root and pool graph evidence | RESOLVED: 106 existing roots; all 110 pools and 121 templates connected; one preserved missing pool reference. See AdoraBuild provider disposition below. |
| `aether-1.21.1-1.5.10-neoforge.jar` | `aether-bronze`, `aether-custom-entry`, `aether-piece-binding`, `aether-placement`, `aether-trap-bindings`, `aether-trapped-block` | Reconcile Bronze, Silver, Gold and terrain generation entry coverage; do not reopen Bronze helper internals. |
| `aethersdelight-0.1.4.2-1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `alternate_current-mc1.21-1.9.0.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `amendments-1.21-2.0.15-neoforge.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `architectury-13.0.8-neoforge.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `attributefix-neoforge-1.21.1-21.1.3.jar` | `attributefix-provider` (69119c6), test_small_utility_provider_scope.py | RESOLVED: Existing attribute range configuration; no structure contribution. See small utility provider dispositions below. |
| `azurelibarmor-neo-1.21.1-3.1.2.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `bclib-21.0.24.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `bettercombat-neoforge-2.3.2+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `bettervillage-neoforge-1.21.1-3.3.1.jar` | `bettervillage-code` | RESOLVED: see Better Village provider disposition below. |
| `bookshelf-neoforge-1.21.1-21.1.81.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `bundle-api-neoforge-1.1.0.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
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
| `creatingspace-1.21.1-1.7.18.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Reconcile existing roots, all components and additional feature/entry routes. |
| `cristellib-neoforge-1.21.1-3.1.7.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve conditional pack loader and structure-config consumers, including Towns and Towers Waystones declaration. |
| `cupboard-1.21-3.7.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `curios-neoforge-9.5.1+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `deep_aether-1.21.1-1.1.5.1.jar` | `deep-aether-totem-scope` | Reuse inactive totem disposition; reconcile Brass and remaining structure/feature entries. |
| `dummmmmmy-1.21-2.0.12-neoforge.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `emi_loot-0.7.9+1.21+neoforge.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `emi_ores-1.2+1.21.1+neoforge.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `ends_delight-2.6+neoforge.1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `explorations-neoforge-1.21.1-1.6.2.jar` | `explorations-deepslate`, `explorations-scarecrow-scope`, `explorations-slime-cave` | Bind scarecrow selector and nine variants as one design; reconcile roots, slime cave and remaining resources. |
| `fastasyncworldsave-1.21-2.6.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `fzzy_config-0.7.6+1.21+neoforge.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `geckolib-neoforge-1.21.1-4.8.4.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `idas-1.13.7+1.21.1-neoforge.jar` | `idas-suppression` | Reconcile existing roots, all components and additional feature/entry routes. |
| `integrated_api-1.7.3+1.21.1-neoforge.jar` | `pool-codecs` | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `integrated_stronghold-1.1.4+1.21.1-neoforge.jar` | `integrated-stronghold-provider`, existing root/graph and family-decision regression | RESOLVED: one existing root, both modification mixins, all components and disconnected/missing templates accounted for. See Integrated Stronghold provider disposition below. |
| `integrated_villages-1.3.3+1.21.1-neoforge.jar` | `integrated-village-suppression` | Reconcile existing roots, all components and additional feature/entry routes. |
| `kotlinforforge-5.11.0-all.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `letmedespawn-1.21.x-neoforge-1.5.0.jar` | `letmedespawn-provider` (69119c6), test_small_utility_provider_scope.py | RESOLVED: Existing mob persistence/discard behavior; no independent family. See small utility provider dispositions below. |
| `libraryferret-neoforge-1.21.1-4.0.0.jar` | `libraryferret-provider` (8c60e03), test_small_utility_provider_scope.py | RESOLVED: Abstract consumer-supplied jigsaw/placement support and coin content. No independent family. See additional shared provider dispositions below. |
| `lithostitched-1.7.10+beta4-neoforge-21.1.jar` | `lithostitched-alias-code`, `lithostitched-biome-injector-code`, `lithostitched-feature-modifier-code`, `lithostitched-platform-modifier-code`, `lithostitched-pool-additions-code`, `lithostitched-pool-compilation-code`, `lithostitched-processor-registration-code`, `lithostitched-random-block-code`, `lithostitched-street-processor-code`, `lithostitched-surface-lifecycle-code`, `pool-codecs` | Reuse modifier, pool, alias and processor captures; reconcile remaining entry/codec consumers and packaged modifiers. |
| `lootintegrations-1.21.1-4.7.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect core loot callbacks and consumers; addon data closures do not close this implementation. |
| `mca-neoforge-7.7.11+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar` | Eight capture directories bound by test_moog_library_provider_scope.py; latest registration boundaries ee8e2c0. | RESOLVED: shared generation and modification library; no independent authored family or packaged generation resources. See Moog library provider disposition below. |
| `moonlight-neoforge-1.21.1-3.0.17.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `naturalist-1.0.2-neoforge-1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `oceansdelight-neoforge-1.0.4-1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `owo-lib-neoforge-0.12.15.5-beta.1+1.21.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `player-animation-lib-forge-2.0.4+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `polymorph-neoforge-1.1.0+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `prickle-neoforge-1.21.1-21.1.11.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `quickrightclick-1.21.1-1.9.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `railways-0.2.1+neoforge-mc1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `ranged_weapon_api-neoforge-2.3.3+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `regions-unexplored-0.6.1-neoforge-21.1.jar` | `regions-unexplored-feature-code`, `regions-unexplored-feature-config-code` | Reuse feature/config captures; bind modifiers and template-pool component consumers; exclude terrain with rationale. |
| `repurposed_structures-7.5.21+1.21.1-neoforge.jar` | `pool-codecs`, `repurposed-mansion`, `repurposed-mansion-bindings`, `repurposed-mansion-layout`, `repurposed-mansion-processors`, `repurposed-monument`, `repurposed-monument-processors`, `repurposed-monument-rooms` | Reuse mansion/monument and codec captures; reconcile all feature/injection entries and unmatched components. |
| `resourcefulconfig-neoforge-1.21-3.0.11.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `resourcefullib-neoforge-1.21-3.0.12.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `ritchiesprojectilelib-2.1.2+mc.1.21.1-neoforge.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `servercore-neoforge-1.5.17+1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `shield_api-neoforge-2.2.0.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `simplyswords-neoforge-1.63.0-1.21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `sparsestructures-neoforge-1.21.1-3.0.jar` | `sparsestructures-provider` (69119c6), test_small_utility_provider_scope.py | RESOLVED: Existing structure-set placement modification; no independent family. See small utility provider dispositions below. |
| `structure_layout_optimizer-neoforge-1.0.12.jar` | `structure-layout-optimizer-provider` (8c60e03), test_small_utility_provider_scope.py | RESOLVED: Existing jigsaw assembly and template filtering modifications. No independent family. See additional shared provider dispositions below. |
| `structure_pool_api-neoforge-1.2.1+1.21.1.jar` | `structure-pool-api-provider` (69119c6), test_small_utility_provider_scope.py | RESOLVED: Caller-supplied pool injection and piece limits; no independent family. See small utility provider dispositions below. |
| `structureessentials-1.21.1-5.0.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `supplementaries-neoforge-1.21.1-3.6.8.jar` | `supplementaries-tags-code` | Resolve feature/structure aliases and injected components against existing roots. |
| `tectonic-3.0.22-neoforge-21.1.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `ubesdelight-neoforge-1.21.1-0.4.13.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Resolve feature/modifier/template consumers and any independent generation routes. |
| `worldweaver-21.0.24.jar` | `pool-codecs` | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `wunderlib-21.0.10.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |
| `youre-in-grave-danger-neoforge-2.0.13.jar` | Packaged/search catalogs; no Item 8 disassembly directory indexed here. | Inspect loader, event, mixin and nested entries; account for full payload and supported role. |

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
