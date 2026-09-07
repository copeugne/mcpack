# IDAS snifferhenge assessment

Nine remaining entries for two connected components. Existing catalogs and
processor inspection suffice; no new runtime or measurement system.

## mob_source

Neither connected template declares authored entities, unresolved entity compounds, physical spawners or generation markers. Both select ticking-only waterlogging_fix_processor, with no mob injection. The monument name and archaeology source do not establish a live sniffer encounter. Environmental spawning remains possible.

## loot_table_source

Both templates reference the defined idas:archeology/suspicious_gravel_snifferhenge table. Its archaeology pool includes pottery sherds, tools, materials and named journal items; these are source possibilities, not measured rewards or proof of journal narrative content. Selected ticking-only processor assigns no loot NBT. No live mob follows from the archaeology table.

## generated_spawners

No ordinary or trial spawner blocks or generation markers in either connected template. Selected ticking-only processor does not introduce spawners. No generated spawner source is identified.

## authored_or_natural_enemies

No authored entity or spawner-based enemy source. Empty root spawn_overrides declares no family-specific natural override; ordinary environmental spawning remains separate. Absence of authored enemies does not guarantee every generated site is safe.

## intended_hostility

Archaeological monument with shared suspicious-gravel loot and no authored hostile entities or spawners. Evidence supports discovery and excavation interest without a hostile encounter claim, Item9 tier or assumed live sniffer population.

## visual_discoverability

Surface-associated monument supplies a visible architectural cue, while its attached lower archaeological section can remain hidden. Nominal24 by27 footprint and21 height include lower geometry and padding, not measured sightlines or exposed silhouette. Terrain and vegetation can obscure the site.

## underground_surface_classification

Surface-associated monument with lower connected component. Root generic_structure projects WORLD_SURFACE_WG offset0,size1,beard_thin adaptation,terrain range10/radius1,ignore_waterlogging. Both pools rigid. Nominal lower origin is seven blocks below the main origin; actual burial relative to terrain and complete generated placement are not measured.

## Geometry and evidence

Family evidence binds templates-redacted, pool-traces-content and packaged JSON.
Under data/idas/structure/snifferhenge/, snifferhenge1.nbt has size24,14,27 and
down_west aligned connector at0,0,0; snifferhenge2.nbt has size24,7,27 and up_west
aligned connector at0,6,0. Both name/target idas:snifferhenge. Adjacent connection
gives bottom origin0,-7,0 relative to main0,0,0. Inclusive union x0..23,z0..26,
y-7..13 gives24 by27 horizontal and21 vertical. This describes the nominal
complete assembly, not measured terrain burial or guaranteed bottom placement.
Corresponding worldgen/template_pool/snifferhenge resources each contain one
rigid element and empty fallback. Trace has no missing components or unresolved
elements. Reuse the exact ticking-only processor inspection in
idas-desert-market-assessment/README.md; it adds no entity or loot NBT.

Both components retain the literal archaeology source defined at
data/idas/loot_table/archeology/suspicious_gravel_snifferhenge.json. The table
is an item reward source, not a live sniffer entity declaration. Preserved
journal item definitions do not prove substantive written narrative. No
reward-yield, sightline or realized encounter measurement is required here.

## Reproduction

```sh
uv run -m tools.build_item8_inventory --output evidence/raw/item8/idas-snifferhenge-assessment-r1.json
uv run pytest -q tests/item8/test_family_decisions.py tests/item8/test_inventory_sources.py tests/item8/test_world_bounds.py
```

Use a fresh output path. Only snifferhenge and input identity may change.
Final integration, acceptance and PR/review/main remain open.
