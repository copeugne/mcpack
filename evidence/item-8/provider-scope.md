# Retained-provider scope pass

Status: candidate enumeration delivered; semantic reconciliation in progress.
This replaces the unbounded instruction to investigate unspecified providers.
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

The immediate semantic reconciliation queue is:

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
this finite provider queue before returning to attribute implementation.
