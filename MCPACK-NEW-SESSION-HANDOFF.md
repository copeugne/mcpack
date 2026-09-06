# Adventure & Engineering Minecraft Pack — New-Session Handoff

> Historical checkpoint: this file records the repository state on 2026-09-01 and is not the current continuation authority. Use `SPECS.md`, the master execution status in `Adventure-Engineering-Pack-Execution-Ledger.md`, and current Git/GitHub state for present status. The dated instructions below are preserved as recovery history.

## Current continuation checkpoint - 2026-09-04

### Continuation update - 2026-09-06

BetterEnd crashed-ship family membership is now recorded in family-decisions.json
and the rebuilt working inventory. Its independent placement and erosion make it
one standalone wreck family despite reuse of the vanilla End-city ship template.
Existing runtime, biome and source evidence is reused. Thirteen focused BetterEnd
cases and scoped Ruff/Basedpyright pass. Reproduction and limits are recorded in
evidence/item-8/provider-scope.md. This resolves one named family decision, not
the final total. The 421 registry-root groups are unchanged. Provider coverage
still has 46 open rows, including Fabric with 33 open modules. Prioritize the
complete named membership list and explicit merge/split decisions; do not resume
detailed attributes or expand generic library tracing. No runtime process is live.
The broader family-decision run has 70 passes and three existing stale
custom-generation UNKNOWN assertions (Explorations, Aether, Repurposed Structures).
Their registry groups are unchanged by the ship increment. Reconcile those
assertions narrowly against existing focused source tests before final validation;
see the failure details and rerun command in provider-scope.md.

Three Fabric client utility modules resolved: block render layers, key bindings,
and sound. Source 1c35ebe (extractor 5624e8a) independently reproduces the entries;
client initialization guards/client-only mixins and full partitions are bound.
Eleven focused Fabric cases and scoped checks pass. Module queue: ten resolved,
33 open. Continue named open modules, reusing all closed roles. Whole census:
90 resolved, 46 open. No new family candidate or live process.

Fabric v2 conventional tags resolved: source e1c7c24, extractor 27f6181,
independently reproduced. Conventional tag keys, tag interface and translation
warnings add no family. Full partition and source binding pass in eight focused
Fabric cases; scoped checks pass. Module queue: seven resolved, 36 open. Next:
remaining named module entries/hooks. Whole census stays 90 resolved, 46 open.
No live runtime or capture process.

Fabric v1 conventional tags resolved: source 73efd5b, extractor ff7e104,
independently reproduced. Tag keys and server-start migration warnings only;
no data/mixin/service payload. Seven focused Fabric cases and scoped checks pass.
Module queue: six resolved, 37 open. Next: v2 conventional tag roles. Whole
provider census stays 90 resolved, 46 open. No new family candidate or live process.

Fabric API Base is resolved: source da5dce0 (extractor 77dc50e), independently
reproduced, has an empty sole loader entry and no data/mixin/service payload.
Six focused Fabric cases and scoped checks pass. Module queue: five resolved,
38 open. Next: conventional tag registration and remaining named modules.
Whole-provider census remains 90 resolved, 46 open. No family candidate added.
No live runtime or capture process.

Fabric now has an exact 43-module queue in provider-scope.md: four resolved,
39 open. The fourth resolved module is transitive access wideners: five files,
lowcodefml metadata/access declarations and no executable or data payload.
The existing Fabric test binds the complete file partition and queue coverage.
Five focused cases and scoped checks pass. Next: inspect the named open module
entry/hook roles. Whole-provider census remains 90 resolved, 46 open; module
counts are not family counts. No live runtime or capture process.

Fabric resource-loading membership is resolved. Discovery/fixed-pack source
8cfe15c (extractors 6cf2878, e29938a) independently reproduces. Fixed pack has
metadata only, no namespaces or ordinary resource content; other packs are
consumer-supplied. Five focused Fabric cases bind all three consumer batches,
and scoped checks pass. Next: other bundled Fabric module entry/mixin roles.
Do not restart biome, GameTest, resource or pack-supplier checks. No new family
candidate. Census remains 90 resolved, 46 open. No live runtime/capture process.

Fabric resource sources are delivered: cce2d3d (extractor 8cf0d23), thirteen
common hooks, entry and ResourceManagerHelperImpl; 6326f21 (extractor 149e849),
ModResourcePackUtil and ModNioResourcePack. Both independently reproduce.
Four focused Fabric cases and scoped checks pass, binding the first batch.
Next: inspect ModResourcePackCreator.loadPacks, the concrete default/test pack
discovery delegate, then bind the two-consumer source and record final module
roles. Other Fabric modules still remain. No new family candidate; census is
90 resolved, 46 open. No live runtime or capture process.

Fabric GameTest roles are resolved from source 6bffda6 (extractor ad51ae4):
five mixins and three entry/namespace consumers, independently reproduced.
The module registers tests and loads SNBT resources; no natural placement
request or new family candidate. Three focused Fabric cases and scoped checks
pass. Remaining Fabric: other bundled entry/mixin roles, particularly resource
loading. Reuse closed packaged-data, modifier, biome and GameTest work. Census:
90 resolved, 46 open. No live runtime or capture process.

Fabric biome selection roles are resolved from source d052da5 (extractor
2426342): six declared mixins and Nether/End registration data, independently
reproduced. Seed propagation and consumer-supplied biome selection add no site
candidate. Two focused Fabric cases and scoped checks pass. Remaining Fabric:
other bundled entry/mixin roles, particularly resource loading and GameTest
consumers. Do not repeat packaged-data, modifier or biome-selection checks.
Census remains 90 resolved, 46 open. No live runtime or capture process.

Forgified Fabric API packaged-data boundary is resolved by source 6eb28e4
(extractor bbdf6f3), independently reproduced. Its biome modifier dispatches
consumer callbacks from an initially empty list. All 43 nested archives contain
only 491 tags, one modifier JSON and one empty GameTest SNBT as packaged data;
no deeper JAR or binary NBT. One focused case and scoped checks pass. Remaining
Fabric work: bundled entry/mixin contribution roles, including biome selection
and resource/test consumers. Reuse the five captured classes. Census remains
90 resolved, 46 open. No live runtime or capture process.

Create membership is RESOLVED. Ponder source 0177383 (extractor 28badcf)
and the final complete parent partition close the last gaps. Ponder templates
are client guide scenes, GameTest templates are fixtures, and generation is
three ore chains. No independent family added. Six focused cases, Ruff and
Basedpyright pass. Census: 90 resolved, 46 open providers. Next: Forgified Fabric
API, then 24 code-only and 21 unmatched rows, followed by canonical grouping.
The 887 runtime entries and 421 provisional groups are not final family counts.
Reuse all closed Create roles. No runtime or capture process is live.

Create embedded Flywheel and Registrate membership is resolved. Flywheel
source 4a7f244 (extractor f61db3a) is independently reproduced and client-only;
Registrate is a consumer-driven library with no automatic entry or data payload.
Five focused cases and scoped checks pass. Remaining Create work: Ponder
entries/services/common accessors and template consumers, then final complete
parent payload reconciliation. Reuse all closed roles. Census remains
89 resolved, 47 open. No runtime or capture process is live.

Create remaining 32 annotated-entry roles are now resolved from source 05d472d.
No new capture or family candidate. All top-level annotated and declared common
mixin roles are accounted for; do not restart them. Remaining Create work:
embedded Flywheel/Ponder/Registrate roles, Ponder content consumers and final
complete payload reconciliation. Existing four passing focused cases bind the
source. Census: 89 resolved, 47 open. No runtime or source capture is live.

Create remaining annotated entry source 05d472d (extractor 6fdfb9e) is
delivered and independently reproduced. Eighteen client-only entries and four
registry/configuration/alias entries are dispositioned; CreateBuiltInRegistries
also resolves the common-mixin initialization question. Thirty-two captured
annotated entries remain to interpret, followed by Ponder and the three embedded
libraries. Do not recapture the 55-class batch. Four focused cases and scoped
checks pass. Census: 89 resolved, 47 open. No runtime or capture process is live.

Create common-mixin batch is delivered: all 43 classes in source 9ad30e0
(extractor 969a3d9), independent repeat exact, roles in provider-scope.md.
Four focused checks and scoped quality checks pass. Do not recapture these
hooks. Remaining: 54 annotated entry classes, including registry reconciliation
and the concrete CreateBuiltInRegistries.init delegate, plus Ponder consumers
and embedded Flywheel/Ponder/Registrate roles. No new family candidate added.
Census remains 89 resolved, 47 open. No runtime or capture process is live.

Create dynamic-pack membership is resolved: StandardBuilder source 23fbee3
(extractor 346e42e) writes recipe JSON; parent writes item tags. No family added.
Four focused checks and scoped quality checks pass. Remaining top-level entry
surface is explicit: 54 uncaptured annotated classes and 43 common mixins;
client-only exclusions require annotation inspection, not gameplay audits.
Ponder template consumers and the three embedded libraries (Flywheel, Ponder,
Registrate) also remain. Reuse all resolved Create roles. Census: 89 resolved,
47 open. No runtime or capture process is live.

Create common dispatch and schematic construction roles are now recorded.
Sources 65cb9b2 and b546705 independently reproduce; three focused cases and
scoped quality checks pass. A concrete dynamic datapack call was found in
ModBusEvents: RuntimeDataGenerator emits recipe/tag inputs, with serialization
in RuntimeDataGenerator$StandardBuilder still to inspect. Other Create work:
remaining annotated/common mixin roles, Ponder and embedded-library roles.
Do not repeat common dispatch, schematic or ore interpretation. Census remains
89 resolved, 47 open. No runtime or capture process is live.

Create main entry, GameTest template construction, schematic processor
registration and mixin plugin are captured in 9dcbd3c (extractor cd1fefb),
independently reproduced and bound by two passing focused cases. GameTest loader
role is resolved; per-fixture references are not claimed. Remaining Create work:
common-event/mixin roles, schematic/Ponder consumers and embedded libraries.
Reuse the delivered ore and GameTest loader checks. Census: 89 resolved, 47 open.
No runtime or source capture is live.

Create ore-source and packaged-data checks are delivered. Source 1fa2306
(extractor cb34d9e) reproduces independently. Three ore chains introduce no
additional site candidate; 67 GameTest and 178 Ponder NBT paths are partitioned.
One focused test and scoped quality checks pass. Remaining Create membership
work: common entry hooks, embedded-library roles and exact template consumers.
Do not repeat the ore-writer or data-category pass. Census remains 89 resolved,
47 open. No runtime or capture process is live.

Regions Unexplored membership is RESOLVED. Final common-entry interpretation
and root/processor source f4ad223 close the outstanding gap. All 23 packaged tree
component classes (including roots) are bound, correcting the earlier 21-class
boundary. Five focused candidate/provider cases pass (1.07s); scoped quality
checks pass. Retain the fallen-log canonical grouping question and Ashen as a
trial-chamber component. No additional named authored-site candidate was added.
Census: 89 resolved, 47 open. Remaining packaged-generation providers: Create
and Forgified Fabric API; 24 code-only and 21 unmatched rows also remain. Next:
finish those provider membership checks, then canonical grouping before detailed
attributes. No runtime or capture process is live. Older RU checkpoints are
historical and must not restart their completed work.

RU tree-component roles are now resolved. Source 0f263ed (extractor 16127c9)
retains 24 missing tree/configuration classes; independent capture matches.
The provider test binds these and the two reused decorators, covering all 21
packaged tree-component classes. Three cases pass (0.19s), with scoped quality
checks passing. The configuration loader is JSON5 I/O; NeoForge's own mixin file
is empty. Next: finish interpretation of the already-captured common entry and
nine common mixins, then assemble RU's final provider disposition. Do not repeat
feature, tree-component, full-payload or overlay inspections. Census stays
88 resolved, 48 open. No runtime or capture process is live.

RU full payload, six overlay directories and embedded JSON5 archive boundaries
are now checked in test_regions_unexplored_provider_scope.py. Both cases pass
(0.16s), with scoped Ruff/Basedpyright passing. The thirty overlay files are
sixteen recipes and fourteen vegetation definitions. JSON5 has no independent
Minecraft entry and only configuration consumers in the parent. Remaining RU
work is common/configuration entry interpretation and registered tree placers/
decorators. Do not repeat feature or archive inventories. Census: 88 resolved,
48 open. No runtime or capture process is live.

Regions Unexplored is current. The remaining 35 captured feature implementations
now have explicit plant/mineral/tree contribution dispositions in provider-scope.md;
none adds another named authored-site candidate. The ground-decorator source
e06c9e1 is bound by the existing candidate test. Both cases pass (0.96s), with
scoped Ruff/Basedpyright passing. Do not repeat these 35 implementations, the
thirteen terrain implementations, the fallen-log candidate or Ashen component.
Remaining RU work: common-entry roles, other registered tree placers/decorators,
and full payload/overlay/embedded JSON5 boundary. Census remains 88 resolved,
48 open. No runtime or capture process is live.

Railways membership is RESOLVED. Source d17d854 completes all 106 declared
common hooks together with the prior StructureMixin capture. Their roles and
all packaged resources are accounted for in the final provider disposition.
Three focused cases pass (0.29s); scoped Ruff/Basedpyright pass. No independent
family added. Census: 88 resolved, 48 open. Remaining packaged-generation
providers: Create, Forgified Fabric API and Regions Unexplored. Reuse RU's
existing checkpoint. The 24 code-only and 21 unmatched rows remain. Next:
finish the remaining membership checks, then canonical grouping before detailed
attributes. No runtime or capture process is live. Older Railways checkpoints
below preserve the now-resolved steps and must not restart them.

Railways is current and remains OPEN. Delivered source eaa7a6b and 0e7edb0
covers fifteen classes, including all eight annotated entries, both mixin plugins,
common setup/events, StructureMixin and player handcar assembly. The focused
provider checkpoint accounts for the full payload, three optional crafting
recipes and the sole legacy handcar template. Two tests pass (0.22s); scoped
Ruff/Basedpyright pass. No independent family arises from the handcar component.
Next: reconcile the other 105 declared common mixin roles, finish actual
entry/delegate and resource-pack/META-INF boundaries, then close the provider.
Do not audit general train gameplay or repeat the fifteen captures. Census stays
87 resolved, 49 open. No runtime or capture process is live.

Lithostitched membership is RESOLVED. The full archive, all declared common/server
hooks, 26 template lists, twenty overlays and remaining resource roles are bound
by test_lithostitched_provider_scope.py. Three cases pass (0.31s); scoped Ruff and
Basedpyright pass. No independent family added. Census: 87 resolved, 49 open.
Next: close the remaining membership queue, prioritizing the four remaining
packaged-generation providers (Create, Forgified Fabric API, Railways and Regions
Unexplored) and shared consumers. Reuse the RU checkpoint and all existing source.
The 24 code-only and 21 unmatched rows remain. Do not resume detailed family
attributes before the finite candidate list and canonical grouping decisions.
No runtime is live. The previous Lithostitched checkpoint below is historical.

Lithostitched membership is in progress. Reuse the 38 previously captured
classes; do not repeat their pool, alias, modifier or processor analysis.
New entry source 4fbbe70 (extractor 9dbb13d) retains the sole annotated entry,
central utilities and platform registry dispatch. The remaining hook capture
is under evidence/item-8/sources/lithostitched-provider-hooks, extractor
0c1ecb552cb270d7419df2306d10468c30c907fa, manifest
7b4524568318a99cc4fc77d5ac4d8c23c125cc492d5c3045ae6347f3d170a8c2.
All 53 new classes reproduce exactly: 51 remaining declared common/server
mixins and two direct configuration/registry delegates. Together with the four
older mixin captures, all 55 declared common/server hooks now have source.
No runtime is live. Census remains 86 resolved, 50 open; source coverage is
not a provider closure.

Next: bind the inspected hook roles and full 445-file payload, then reconcile
26 packaged template lists and the twenty shipwreck overlay templates with
existing vanilla consumers. The two packaged worldgen modifiers compile raw
templates and replace trial-chamber aliases; the sole packaged pool is the
existing trial-chamber entrance cap. Other packaged data is processor lists,
terrain/noise/region definitions and tags. Preserve overlay enablement separately
from membership. Hooks select supplied templates/processors or alter existing
biome/terrain/jigsaw behavior. Follow a further delegate only for a concrete
unresolved independent-site boundary; do not audit every unused library codec.
Finish the existing focused provider check and supported disposition before
decrementing the queue. No new measurement or framework is required.

Naturalist membership is RESOLVED. Source 9682cb0 captures its entry, seven
common mixins and mob-spawn modifier. Two focused cases pass (0.13s); scoped
Ruff/Basedpyright pass. No independent family added. Census: 86 resolved,
50 open. Remaining packaged-generation providers are Create, Forgified Fabric
API, Lithostitched, Railways and Regions Unexplored. The 24 code-only and
21 unmatched rows also remain. Next: Lithostitched's supplied generation
modifications, reusing existing pool-codec captures and consumer dispositions.
Do not resume family attributes before membership and named grouping decisions.

Ube's Delight membership is RESOLVED. Source b6ef5a0, bundled entry ca67c60 and
configuration delegates e40ea32 cover crop generation, common entries and the
MidnightLib boundary. Three focused cases pass (0.13s); scoped Ruff/Basedpyright
pass. Census: 85 resolved, 51 open. No independent family added. Remaining
packaged-generation providers: Create, Forgified Fabric API, Lithostitched,
Naturalist, Railways and Regions Unexplored; 24 code-only and 21 unmatched rows
also remain. Next: Naturalist's spawn/content boundary, then the remaining
generation providers and their shared dependencies. Reuse all five closed
Delight-provider dispositions and the RU checkpoint; do not restart them.

Aether's Delight membership is RESOLVED. Source 13d2013 covers all six annotated
entries; three focused cases (0.12s) cover the full payload, five ore/plant chains
and both packaged compatibility data packs. Scoped Ruff/Basedpyright pass.
Census: 84 resolved, 52 open. No independent family added. Preserve the Ancient
Aether pack's disconnected wynd ore configuration and legacy Forge paths as
documented; do not infer activation or rerun runtime for this membership role.
Next: Ube's Delight, including its MidnightLib bundle and declared common hooks.
Seven packaged-generation providers, 24 code-only and 21 unmatched rows remain.

End's Delight membership is RESOLVED. Source 311c1fe binds its sole custom
generator to chorus succulent plants and covers all three annotated entries.
Two focused cases pass (0.13s); scoped Ruff/Basedpyright pass. Census: 83 resolved,
53 open. Next: Aether's Delight's five ore/plant generation chains, its two
packaged compatibility data packs and loader/event entries, then Ube's Delight.
Do not redo the closed Farmer's, Coffee or End's Delight providers. Eight
packaged-generation providers, 24 code-only and 21 unmatched rows remain.

Coffee Delight membership is RESOLVED. Source 49445ab and two focused checks
(0.10s) establish a vanilla coffee-bush patch and food/item content, with no
independent family. Scoped Ruff/Basedpyright pass. Census: 82 resolved, 54 open.
Remaining packaged-generation providers: Aether's Delight, End's Delight,
Ube's Delight, Create, Forgified Fabric API, Lithostitched, Naturalist, Railways
and Regions Unexplored. The existing 24 code-only and 21 unmatched rows also
remain. Next: End's Delight's custom crop writer and common entries, followed
by the other food add-ons. Do not redo Farmer's Delight or Coffee Delight.

Farmer's Delight membership is RESOLVED in the provider-scope disposition.
Source 555d912, common setup 15cb251 and server packet 6678ec9 account for
five existing-village components, crop processor changes, vegetation and
non-generation entries. Three focused cases pass (0.15s); scoped Ruff and
Basedpyright pass. Census: 81 resolved, 55 open. Reuse this closure rather than
reopening food/item mechanics. Continue the dependent food add-ons and remaining
packaged providers: ten packaged-generation rows, 24 code-only and 21 unmatched
rows remain. Canonical membership/grouping still precedes detailed attributes.

Creeper Overhaul provider membership is RESOLVED. Source e8d3713 and login
delegate d21ca8f establish mob-spawn/loot/cosmetic roles without an independent
family. All 317 parent files, seventeen spawn modifiers and the nested
cosmetics-library boundary are accounted for by three focused cases (0.11s);
scoped Ruff/Basedpyright pass. Census: 80 resolved, 56 open. Next packaged
provider is Farmer's Delight, before its dependent food add-ons. Eleven
packaged-generation providers remain, plus the existing code-only and
unmatched-entry queues. Do not restart Supplementaries or Creeper Overhaul.

Supplementaries provider membership is now RESOLVED. The final disposition in
evidence/item-8/provider-scope.md supersedes all older open Supplementaries
checkpoints. Reuse server-hook/shared-plugin source 46127c7 and map delegate
3660300. All 73 declared common mixins are accounted for, including the four
previously captured structure hooks. The remaining entries add no independent
site. Galleon, road sign and the named cave-urn cache boundary remain the inputs
to later canonical reconciliation; no final family count is asserted.
Nine focused checks and scoped Ruff/Basedpyright pass. Census: 79 resolved,
57 open. Next: the twelve remaining packaged-generation providers, beginning
with Creeper Overhaul. Keep the completed RU feature checkpoints. Do not redo
Supplementaries, inspect unrelated gameplay helpers, or resume attributes
before whole-stack membership and named canonical decisions are resolved.

MixinSquared inspection identified a concrete extractor limitation: its Forge
wrapper contains META-INF/jars/MixinSquared-0.3.3.jar, one level deeper than the
existing nested-archive reader supports. Close this actual executable-library
boundary by extending the existing pinned reader to traverse the exact nested
member chain. Keep parent and leaf SHA-256 checks and existing output format;
do not add a new extraction system. The wrapper SHA-256 is
e5f1afc19c38005b03615d7c3af65df6b9150cb25150ac5267b587a116f425e3;
the inner SHA-256 is
0eaa67fa937cc65ab78a981cd9e4e741d03eaf7236983d7e30818ac99da0632f.
Trinkets fallback is resolved in 4d50c66. Reuse the latest Supplementaries
checkpoint in evidence/item-8/provider-scope.md; census remains 78/136 resolved.

Supplementaries placement/processor membership paths are resolved in source
a74ae7b, extracted by e1e2005. Reuse sources/supplementaries-placement-processor
under evidence/item-8. Three class identities are bound by the existing provider
test: both cases pass; scoped Ruff and Basedpyright pass after a line-length fix.
The exclusion placement only queries other structure sets; the processor
transforms blocks within existing template block information. Neither adds a
family. Cave-urn cache remains a named canonical-boundary candidate.

Provider census remains 78 resolved, 58 open. Next concrete Supplementaries
membership checks are its SupplementariesForge loader and common delegates,
MixinPlugin and declared common hooks (including the two Stronghold sconce
mixins), plus full payload and the two nested archives. Exploratory metadata
inspection found mixinsquared-forge-0.3.3.jar and
sable-companion-common-1.21.1-1.6.0.jar. This is not a nested-provider disposition
or authorization to re-enable Sable. Bind the actual loader reachability and
contribution roles using existing tooling before closing Supplementaries.
Do not repeat resolved roots, pools, templates, features, elevator or processor
analysis. Source captures alone do not reduce the provider/family backlog.

Creating Space provider coverage is now RESOLVED. See its final disposition in
evidence/item-8/provider-scope.md and test_creating_space_provider_scope.py.
Four existing roots, five connected pools and six templates are accounted for;
the disconnected moon/abandoned_outpost template is preserved as an unused
component in this provider's packaged generation graph. Crater, rocket, arrival,
common hooks and full payload roles are resolved. Source 3133afb (extractor
30d6302) closes four common delegates; source 526983c closes arrival. Reuse all
accepted captures and checks rather than restarting them.

Census is 78 resolved and 58 open. Next provider: Supplementaries, reconciling
its two root definitions, configured road-sign representation, other feature
content and component injections. Canonical grouping and eleven attributes
remain downstream of membership closure. Four applicable Creating Space cases
passed in 0.98s; scoped quality checks pass. No runtime process is live.

Priority correction following the user's challenge about unknown remaining
families: use the scope reassessment under the exact provider queue in
evidence/item-8/provider-scope.md. The 59 open rows partition into 2 with indexed
structure definitions, 12 with other packaged generation candidates, 24 with
code-reference matches only and 21 with no indexed matches. This is planning
information, not semantic acceptance. Resolve membership across this queue
before further detailed natural-feature analysis or family attributes.
Start with Creating Space and Supplementaries, following their actual shared
loader dependencies. Publish named grouping alternatives after membership
closure; do not substitute 887 roots or 421 provisional groups for families.

RU ground-decorator source is delivered in e06c9e1, extractor 62c2e12,
manifest 2b459bc6975a0ddffe6826ea332312ef7f78e0d31354d165d455f3d127f03544.
Its direct writer selects the configured block state above eligible dirt, with
target and height checks. No additional helper capture is needed for that
writer. The existing candidate test still needs this manifest binding and the
vegetation-role disposition remains unfinished. Preserve that checkpoint while
prioritizing whole-queue membership. No provider closure is claimed by this
reassessment: 77 resolved and 59 open. No new runtime measurement was run.

Latest RU checkpoint: terrain-feature roles are RESOLVED in 5d187f9. Shared
redstone writer source 690e757 (extractor 3460144) closes that direct helper.
Do not repeat the thirteen terrain features or their writer. Source 04c515f
(extractor b5e5564) now captures the remaining 35 vegetation implementations;
manifest 6e77e0aab7c6f999e08de37eca0fdf8417b07377823cd848bae016e50cdc1bb6,
independent r1 exact. Test increment 0fd9f1a reconciles all 53 directly constructed
RUFeatureTypes implementation classes with captured source. Both cases and
scoped checks pass. All commits pushed and remote-verified.

Current work: semantic roles for the 35 captured vegetation implementations,
then remaining common entries, custom tree placers/decorators, full payload and
overlays. JSON5 exploratory inspection found 29 files (28 classes and one
manifest), no loader annotations, and parent references only from RUConfigHandler
and Json5Ops classes. Nested SHA-256:
2e0f73784e6bc4c755e52d485f628d110d397f079d58b118658b903be9aa0533.
This exploratory inspection is not yet bound by the final provider check.
No runtime is live. Census remains 77 resolved and 59 open; source coverage is
not provider closure or the final family denominator.


Latest RU checkpoint: be03a80 resolves fallen-tree placement and decoration
links. Eight placed definitions map to six configurations with nineteen packaged
biome consumers. AttachedToLogsDecorator is captured in 1c53b0f (extractor
947a0fa), manifest 7656c29c7f0b77b5827cbb01b082d2509f800a7cac87e342ec47bc6785bdc77d.
Both candidate tests and scoped checks pass. Do not repeat this boundary.

Current work is the remaining terrain feature roles. Source 4d65d81 captures
thirteen rock/spire/ground/pool implementations using extractor 7fc2e24, under
sources/regions-unexplored-terrain-features. Manifest SHA-256:
408438fe5484a1798d6487f12725cd3becac5c315a0d99dc585163177a2d474c.
Independent r1 matches. These sources are delivered, but their complete role
interpretation and provider-test binding remain open. Initial inspection shows
BasaltBlob's chest and masonry references belong to CANNOT_PLACE_ON, not a
chest-generation claim. PointedRedstoneFeature and its cluster delegate to
PointedRedstoneUtils, whose body is not yet captured. Keep any follow-up tied to
that concrete writer boundary. Other vegetation, common entries and remaining
payload/overlay/JSON5 roles still follow. Census remains 77 resolved, 59 open.
All increments are pushed and remote-verified. No runtime process is running.


Latest RU increment: c373525 binds one stump-and-fallen-log candidate with six
configuration variants and preserves the possible stump-only outcome. Both
focused candidate cases and scoped Ruff/Basedpyright pass. Source 23f8c7b,
extractor 389b2ed, adds RUFallenTreeFeature, RUSurfaceRuleBuilder and BiomeTarget;
manifest b779daaf84f5a04384246079c6ada082941188e6319cb4c8835bfe6dad089770.
Independent r1 matches. All source and tests are pushed and verified.

Region/surface delegate roles are now reconciled in provider-scope.md:
Nether surface composition, Inferno spring/aquifer modification, and biome
replacement/climate-point/forced-placement support. No extra site route in
these delegates. Do not recapture or re-audit them. Fallen-tree decorator and
placement-consumer links remain open, along with other custom features,
remaining common entry roles and payload/overlay/JSON5 reconciliation.
Provider census remains 77 resolved and 59 open. No runtime process is live.


Current provider: Regions Unexplored, still OPEN. Delivered a5efbc8 adds fifteen
entry/common-mixin selectors; f479e0a retains the source with an exact independent
repeat; ac87000 binds the archive component boundary and existing graph checks.
All are pushed and remote-verified. Source manifest SHA-256:
cb7185024530c1b77bbf71dbf9ccefb2ba1acf505688896a1803f0a4240a4894.
41 focused candidate/pool-link/feature-modifier/surface cases passed in 12.40s;
scoped Ruff and Basedpyright pass after one line wrap. No runtime is running.

The sole NBT template and actual pool are trial_chambers/ashen, already reached
by the accepted minecraft:trial_chambers graph. No own structure-registry roots
or packaged structure definitions. Do not repeat that component reconciliation.
Remaining RU work: common-entry/mixin role disposition, custom features beyond
the already accepted modifier subset, remaining payload/overlays and JSON5.
The captured RULithostitched registers surface modifiers, regions and biome
injectors; its nether rule delegates to RUSurfaceRuleBuilder.nether and biome
injection uses BiomeTarget. These concrete generation delegates are not yet
resolved by this provider census. Common setup calls afterRegistriesFreeze
(block-tool/fire compatibility and RUBlocks/RUEntityTypes post-registration).
Avoid interpreting names or method signatures alone as provider closure.

Census remains 77 resolved and 59 open. Deep Aether is closed, as recorded below.
Canonical-family count, attributes and final delivery gates remain incomplete.


Latest checkpoint: Deep Aether provider coverage is RESOLVED in 6da0c86,
pushed and remote-verified. The three final biome/surface delegates were
preserved in 193bbe3. Five focused candidate/provider/totem cases pass;
scoped Ruff and Basedpyright pass. Do not reopen the completed Deep Aether
source, component, optional-pack or nested-library checks. Its inactive
Sacred Lands routes and fallen-tree candidate remain canonical-grouping inputs.

Current census: 77 supported provider dispositions, 59 open providers. The
exact queue is evidence/item-8/provider-scope.md, starting at its Exact provider
queue section. That historical table started with 110 rows after 26 closures;
51 of its rows are now RESOLVED and 59 remain open. Do not interpret the table
as only 110 retained candidates or the provider count as a family count.

The user's unresolved request is a finite canonical-family inventory and exact
remaining family count. Finish this existing provider queue before returning
to the eleven attributes. Use the existing packaged/runtime catalogs and
captured sources. Inspect actual generation boundaries; do not audit unrelated
gameplay helpers or add measurement systems for hypothetical gaps. Then resolve
canonical designs and publish each named grouping ambiguity. The 887 roots and
421 provisional groups remain inputs, not an accepted final denominator.
No runtime process is live and no external blocker prevents continuation.
Final Item 8 evidence, Codex review loop and verified main merge remain open.

Earlier checkpoints below are preserved as history and superseded where they
conflict with this latest checkpoint.

Deep Aether is current, still OPEN. Candidate partition 63d6dfd and runtime
library selection fa379f0 are delivered: four roots, fifteen templates, sixty
configured features; active TerraBlender is retained 4.1.0.8, not embedded .3.
AeroBlender 1.0.0 loads from Deep Aether. Source 53427f4, extractor 9b16faf,
captures 43 annotated/common-mixin/feature/Brass-jigsaw boundary classes in
sources/deep-aether-provider. Manifest SHA-256:
71c441da5bd3213d84b0ce9f1f38f098979d158b3f16146397428b99e958d5c4.
Independent r1 matches all generated files. Do not repeat this capture.

Brass room-name reconciliation is delivered: five ordinary rooms and five boss
counterparts plus door and room_part_up account for all twelve Brass templates.
The focused source check binds the manifest/class hashes and real concatenation
recipes. Four candidate/selection/source/totem cases and scoped checks pass.
Reuse the inactive totem disposition. Remaining work is jigsaw/eligibility,
feature and common-entry roles, optional packs and AeroBlender's role, then the
whole-provider check. Census remains 76 resolved and 60 open. No blocker or
live runtime process. Canonical grouping and attributes still follow the census.

Aether provider coverage is now RESOLVED in the final provider-scope.md section.
The census has advanced to 76 resolved and 60 open. Nine focused Aether cases
pass, along with scoped Ruff/Basedpyright. The provider check binds fifteen
existing source manifests, full archive partition, entry/common mixins and the
three exact developer functions. No further Aether census helper audit is needed.
Preserve the holiday-tree canonical boundary and inactive optional portals;
family grouping and attributes remain separate. Continue the remaining provider
queue, starting with Deep Aether and reusing its existing captures. Final Item 8
gate, Codex review loop and verified main merge remain mandatory.

Latest aac294c and dc5cda4 are pushed and verified. Six focused Aether cases
and scoped checks pass. Optional portal activation/components are resolved:
frozen common config disables automatic activation, six roots are absent from
the runtime registry, and the captured generator selects exactly the thirteen
packaged portal templates. Do not repeat that boundary.

Extractor eb16438 and source increments 8c792b0 (aether-entry-delegates),
62defac (aether-cumulus-entry), 9c29cff (aether-nitrogen-entry) are delivered.
Each exact command and manifest hash is in its README; independent r1 matches.
Cumulus's mod entry is CLIENT restricted, but its common storage mixin and
IPlatformHelper service must be accounted for. The storage wrapper only changes
the lock predicate while loading summaries; inspect NeoForgePlatformHelper's
role before final closure. The first no-services test failed correctly and now
binds that exact service. Nitrogen's constructor registers biome modifiers and
tree placers as well as loot support, beyond its user-info hooks. Resolve those
serializers and consumers; do not infer no contribution from no packaged data.

DimensionHooks is captured; world-load initializes Aether level data, time hooks
manage time, and portal interaction paths delegate portal-frame activation.
Finish bounded role interpretation. ReloadListeners registers RecipeReloadListener
and BannerReloadListener; those inner handlers are not yet captured. Keep any
necessary follow-up tied to those concrete entry boundaries. A read-only catalog
search found a Deep Aether loot modifier mentioning nitrogen; it is exploratory,
not a complete consumer proof. Census stays 75 resolved and 61 open. No blocker.

Latest delivered increments: 75ad62e records the four custom feature roles and
resolves HolidayFilter; 5bf0795 binds actual nested-library selection to the
preserved runtime log. Five focused Aether cases and scoped checks pass.
Accessories beta.53 is selected from the retained top-level archive; do not
audit embedded beta.48 as running code. Cumulus 2.0.7 and Nitrogen 1.1.25 load
from Aether and still need contribution roles. Census remains 75 resolved and
61 open. The user's immediate priority is closing this finite provider queue
and canonical family denominator before returning to detailed attributes.

Source 4487f8f, extractor 54c0801, captures 49 common-entry/listener/mixin and
portal classes in sources/aether-common-hooks. Manifest SHA-256:
9c3b21c8bf2eab73550acc646a9c74081c15daac08c941367f298adf0bb8c50f.
Independent r1 matches all generated files. Both refs are pushed and verified.
The earlier Aether main capture was non-verbose and lacked callback bootstrap
bindings. The new capture fixes this concrete evidence gap using the existing
extractor, with the old source preserved. Do not recapture these classes.

Next interpret those roles and resolve the two selected nested libraries.
DimensionListener delegates world-load/time/portal behavior to DimensionHooks;
inspect that concrete boundary, not every gameplay helper. Main callbacks also
identify AetherCommands and ReloadListeners; dataSetup is a GatherDataEvent
callback. Portal pack source reads add_ruined_portal_automatically, whose frozen
common config is false; six optional roots remain absent from the runtime
registry. Its captured pack-source and portal-template consumers still need
final reconciliation. Source capture alone does not close these roles or Aether.
No runtime process is live and no external blocker exists.

Latest Aether increments 93dbd29 and f3a2b1b are pushed and remote-ref verified.
Silver's ten selected component names and Gold's four account for their template
sets except Silver test_door, which has no literal reference in archive classes.
Do not repeat this component reconciliation. Four focused Aether cloud/candidate
cases and scoped quality checks pass.

Retain aether:holiday_tree as a named decoration/family-boundary candidate, not
an accepted additional canonical family. Its decorator selects snow/present
blocks; all four packaged Skyroot biomes reference its placed feature. Frozen
config has always=false and seasonally=true, hash
578abca7702fcecdb39845a7043f6ec1c504f153f6d3b4af45daedb29df931de.
HolidayFilter still needs inspection before effective eligibility is accepted.
Present reward mechanics remain later attributes. The new candidate is recorded
at the end of provider-scope.md and must survive canonical reconciliation.

Next resolve the four captured custom feature roles, main-entry/common hooks,
optional portal consumers and the three nested-library selection/roles. Initial
CrystalIslandFeature reading shows a crystal-tree placement followed by ground
formation, and ShelfFeature delegates supplied-block disk placement. Do not turn
those initial reads into accepted provider exclusions without finishing the
bounded role reconciliation. Census remains 75 resolved and 61 open. No blocker.

Latest Aether source cb00a94 is pushed and remote-ref verified. Extractor 8976b7a
captures 23 entry/plugin, custom feature, holiday-decoration and Silver/Gold
assembly classes in sources/aether-provider. Manifest SHA-256:
917c3ffbb199539bfbe375f4a7381d4498f327a2ce9d5cdc28ad01d978f604ee.
Independent r1 matches every generated file. Do not repeat these captures.

Candidate partition 4bc4292 is also delivered: four base/runtime roots, six
optional ruined-portal roots absent from the captured registry, 34 templates
(six Bronze, eleven Silver, four Gold, thirteen portal), 25 configured features
across eleven types, and three exact nested JAR identities. Two focused cloud/
partition cases and scoped quality checks pass. See provider-scope.md's final
Aether section for the finite resource queue and nested identities.

Next interpret the captured Silver/Gold consumers and four custom features plus
holiday decoration, then reconcile main-entry delegates, common mixins and the
three bundled libraries. Source capture alone is not provider closure. Initial
source reading has not produced accepted additional dispositions yet. Preserve
the existing Bronze/cloud results and do not resume detailed attributes before
the provider census and canonical grouping close. Census remains 75 resolved,
61 open. No blocker exists; this turn delivered concrete evidence increments.

Latest closure 716fadb is pushed and remote-ref verified. Repurposed Structures
provider coverage is RESOLVED. Census is now 75 resolved providers and 61 open.
Nine focused cases and scoped Ruff/Basedpyright pass. The full disposition is
at the end of provider-scope.md; its exact queue row and current count are updated.

Delivered source increments: 015f351 covers the ten assembly boundaries with
manifest 10a3a2a15d647c5c52c171034c84be9c2fc68e1fe42dd571e8a6c725a6de6746;
6fed290 covers the data-generation entry with manifest
0d2237b825ac55da59a8908beb120e562b67a58ccc3a5de1c151e1bbd980d9bf.
Both independently reproduced exactly. The provider check binds twelve existing
source manifests, 5842 files, 248 classes, both annotated entries, thirty common
mixins and the exact equality of 107 packaged/runtime roots. Its family boundary
also includes the existing dungeon/well configuration candidates. Canonical
grouping, effective eligibility and attributes remain separate unfinished work.

Next is Aether. Reuse aether-custom-entry, aether-bronze, aether-piece-binding,
aether-placement, aether-trap-bindings and aether-trapped-block. The cloud entry
README already contains a later tested terrain/provider disposition; do not
restart its superseded initial follow-up. Reconcile remaining provider entries,
Silver/Gold consumers and full resource roles without reopening Bronze helper
internals. No blocker exists. Final Item 8 review/main merge remains mandatory.

Latest feature-role increment fbc383b is pushed and remote-ref verified.
Source 762b6f9 captures the remaining 31 feature implementations with exact r1
reproduction; the two earlier NBT features are reused. All 136 configured
features across 37 types now have recorded roles at the end of provider-scope.md.
Four focused cases and scoped quality checks pass. No additional independent
candidate was found beyond the already recorded dungeon/well candidates.
Census remains 74 resolved and 62 open. Do not repeat the feature pass.

Next close Repurposed's non-feature generation/injection and lifecycle roles.
Existing common/NeoForge entries register codecs, lifecycle/reload dispatch,
map trades and pool additions. The seven uncaptured top-level generation
implementations are CityNetherStructure, GenericJigsawStructure,
GenericNetherJigsawStructure, MineshaftEndStructure, MineshaftStructure,
ShipwreckNetherStructure and StrongholdEndStructure. Their concrete common
assembly consumer is PieceLimitedJigsawManager (including Assembler); the
piece-count reload path is StructurePieceCountsManager. Inspect those boundaries
only where they can change the already enumerated candidate/component links.
Do not treat every uncaptured utility, config, processor or data-holder class as
a new mandatory work item. Reuse mansion/monument and residual resource roles.
No blocker exists; final canonical count, attributes and review/main merge remain.

Latest resource-role increment 9a1a30d is pushed and remote-ref verified.
The preceding b1e0fa7 closes the custom mansion/monument resource partition.
Repurposed's seven residual pools and 53 templates now have component roles
recorded at the end of provider-scope.md. Three Repurposed focused cases and
scoped quality checks pass; the mansion/monument increment passed four cases.
Census remains 74 resolved providers and 62 open. This is concrete progress,
not whole-provider closure or a final family count.

Next finish Repurposed feature and entry/hook reconciliation, using existing
452e33e captures. Common/NeoForge entry review has begun: registry initialization,
reload listeners, pool additions, lifecycle dispatch and map trades. Do not
repeat resource partition work or disassembly captures already delivered.
The 16 minecart templates are configuration-selected components; two crossing
templates have count limits but no direct pool location. Same-named jigsaw pool
references are not NBT template references. Three ancient-city corner templates
are distinct from selected _1/_2 variants. Five bastion mob templates and 27
village components have no direct pool locations in this archive. Code consumer
review still precedes any whole-provider inactive/reachability claim.
After provider closure continue the exact existing queue, then canonical
grouping and eleven attributes. Final review and main merge remain mandatory.

Latest Repurposed graph-partition increment 683a9ef is pushed and remote-ref
verified. Census remains 74 resolved providers, 62 open. Two focused cases
and scoped quality checks pass. Repurposed provider scope remains OPEN.

The preserved generic graph covers 95 of 107 roots, with no missing or unresolved
element entries in those 95 traces. The other roots are eight mansion and four
monument variants with custom assembly source already captured. Outside the
generic graph: 503 pools (416 mansion, 80 monument, seven other) and 785 templates
(597 mansion, 92 monument, 36 dungeon, seven well, 53 other). Full denominators:
1099 pools and 3162 templates. These namespace partitions are not proof that
every custom resource is selected. No family count follows from them.

Next bind retained mansion/monument selector code to these custom pools and
resolve the seven other pools plus 53 other templates. Exact residual pool
names and template category counts are at the end of provider-scope.md;
test_repurposed_feature_candidates.py reproduces the partitions. Do not repeat
captures or mislabel untraced resources as unused. Keep the 23 dungeon/well
configured candidates from 5d51d25 in the finite candidate reconciliation.
Remaining feature roles and entry/hook dispositions still precede provider
closure. Final canonical count, attributes and review/main merge remain open.
This turn delivered a verified evidence partition; no blocker exists.

Latest Repurposed candidate increment 5d51d25 is pushed and remote-ref
verified. Census remains 74 resolved providers, 62 open. Repurposed Structures
is OPEN. Source 452e33e preserves 45 entry, NBT feature/configuration, modifier,
pool-addition and common mixin classes with exact r1 reproduction. Earlier
34 mansion/monument/processor/pool classes remain reusable evidence.

Important candidate omission found and recorded at the end of provider-scope.md:
sixteen dungeon NBT feature configurations and seven well configurations were
absent from the current nonregistry contribution list. The focused test binds
all 23 to matching placed features, biome modifiers and existing templates.
One case and scoped quality checks pass. These are configurations/candidates,
not 23 canonical families; ocean temperature variants share template choices.
Do not lose this candidate list or postpone it behind attributes.

Next reconcile remaining Repurposed feature roles and the complete pool/template
partition, plus entry/hook roles and supported exclusions. Initial archive
counts: 5842 files, 248 classes, 107 structure definitions, 37 structure sets,
1099 pools, 327 processor lists, 136 configured features, 157 placed features
and 3162 templates. These are resource counts, not family counts or scope closure.
Do not recapture delivered NBT, mansion or monument sources. Final canonical
count, eleven attributes and review/main merge remain open. This turn delivered
source and a verified candidate increment; no blocker is present.

Latest closure at 6e9da02 is pushed and remote-ref verified. Census:
74 resolved providers, 62 open. Zeta provider scope is closed. Its one packaged
biome modifier, registration/module/configuration/generator dispatch and
existing-structure replacement hooks add no independent family.

One focused case in tests/item8/test_zeta_provider_scope.py passes, with scoped
Ruff and Basedpyright clean. It binds nineteen source manifests, 49 distinct
captured classes, complete 627-file payload, declared mixins and sole mod entry.
The initial assumed library prefix in the test failed; actual full inspection
identified seven math/fast classes, recorded in the passing exact partition.
Do not recapture completed Zeta/Quark sources or expand generic helpers.

Next reconcile Repurposed Structures using its existing mansion/monument,
processor, layout, room and pool-codec captures listed in the provider queue.
Complete remaining generation/injection entry roles and packaged resource
reconciliation, preserving missing/disconnected components and canonical
variant boundaries. Full provider census precedes canonical grouping and the
eleven detailed attributes. Final Item 8 review and main merge remain open.
This turn delivered a provider closure; no blocker is present.

Latest Zeta source increments c79f551 and the subsequently delivered dynamic
registration source commit are pushed and remote-ref verified. Census remains
73 resolved providers and 63 open. Zeta is not closed yet. zeta-provider captures
25 new entry/proxy/plugin/replacement/common-mixin classes; dynamic-registration
and dynamic-registry capture RegisterDynamicUtil and ZetaRegistry respectively.
All three outputs reproduce exactly and scoped extractor checks pass.

The dynamic-registration question is resolved: registry-load notifications
reach signed-up Zeta instances; each registry selects queued entries by supplied
registry key, returns for absent/empty queues, evaluates consumer-supplied
creators and registers their supplied IDs. No new authored content was identified.
StructureStart sets/clears structure context, while piece/template hooks apply
consumer block-state replacements. ZetaMod itself starts with null module finder
and categories plus general configuration. Reuse these captures and the existing
22 configuration/generation classes. Do not recapture or trace generic holders.

Next write the focused Zeta payload/source check and provider disposition.
Initial archive accounting: 627 files, 616 classes, no nested JAR or templates,
one data/zeta/neoforge/biome_modifier/biome_modifier.json declaring
{"type":"zeta:biome_modifier"}, four assets, loader/pack/mixin metadata.
Fourteen common mixins plus four Forge-side common mixins are captured; three
client mixins concern colors/rendering. The sole mod entry is ZetaModForge.
The interface-delegate plugin handles annotated interface transformations and
must be included in the role disposition. Shared registry/module/biome/generator
consumers are already captured, not new independent candidate families.
Final canonical count, detailed attributes and review/main merge remain open.
This turn delivered evidence resolving a concrete callback; no blocker exists.

Latest closure at 6e765f5 is pushed and remote-ref verified. Census:
73 resolved providers, 63 open. Quark provider scope is closed. The existing
five named site candidates remain spire, fairy ring, fallen log, Monster Box
and Nether obsidian spike; terrain/vegetation contributions are not extra
families. Canonical whole-stack grouping remains separate and incomplete.

One focused case in tests/item8/test_quark_provider_scope.py passes, with scoped
Ruff and Basedpyright clean. It binds eighteen source manifests, exact outer and
nested payloads, all world generators/top-level world modules/feature classes,
packaged worldgen categories and frozen configuration. The detailed disposition
is at the end of provider-scope.md. Do not recapture or repeat completed Quark
and Biolith sources or reinterpret provider closure as observed placement.

Next close shared Zeta using the existing captures listed in its queue row.
Inspect remaining entry/plugin roles and complete packaged payload accounting;
reuse module/config/biome/generator dispatch evidence. Do not expand generic
math or unrelated gameplay internals. All remaining providers precede final
canonical grouping and detailed family attributes. Item 8, clean review and
main merge remain open. This turn delivered a provider closure; no blocker.

Latest source checkpoints b9670f9 and 4e4a158 are pushed and remote-ref
verified. Census remains 72 resolved providers and 64 open. Quark remains open.
The specific spawner callback is resolved: configChanged copies isEnabled to
staticEnabled; spawnerUpdate immediately returns when false or client-side.
Frozen experimental."Spawner Replacer" is false. Enabled behavior only changes
an existing spawner's entity type. Reuse quark-spawner-replacement (one class)
and prior Zeta binding evidence; do not recapture or run a new experiment.

quark-biolith-provider captures 26 bundled Biolith entry/API/service/loader/
plugin/mixin classes through existing nested extraction support added at
1ee9b51. Both captures reproduce exactly; scoped extractor checks passed.
The Biolith loaders read biolith/biome_placement.json and
biolith/surface_generation.json resources. Quark supplies neither resource;
Glimmering Weald uses the captured direct BiomePlacement API. Biolith initializes
configuration, compat, commands and criteria, and its hooks connect supplied
biome/surface rules to generation. Complete its bounded role reconciliation
with final Quark payload/entry accounting; do not expand unrelated math helpers.

Remaining Quark closure work is the focused full-payload/source check and
supported narrative disposition, including optional datapacks, declared hooks,
existing generator candidates, bundled Biolith roles and frozen configuration.
The full outer payload partition observed is 903 org classes, 64 tween-engine
classes, 4479 assets, 3580 data files, 285 resource-pack files, 44 datapack files,
seven META-INF files and five root metadata/icon files. This sums to 9367 and
is an inspection lead to bind in the focused check, not a provider closure.
No generation-class name outside the known world/mixin paths was found except
datagen QuarkTags$Structures; name search alone is not absence evidence.
Preserve existing candidate and variant distinctions. Final canonical family
count, attributes and review/main merge remain open. This turn delivered source
evidence and resolved a concrete callback; no blocker is present.

Latest source checkpoint at 174dba6 is pushed and remote-ref verified.
Census remains 72 resolved providers and 64 open; Quark is not closed.
quark-provider-entries preserves 26 previously uncaptured entry/module/feature/
mixin classes, with exact r1 reproduction and passing scoped extractor checks.
Reuse the earlier 34 Quark classes and recorded nonregistry generators.

Remaining Quark scope checks: bundled Biolith, SpawnerReplacerModule's direct
callback, and final full packaged-resource/entry-role reconciliation. The captured
SpawnerBlockEntityMixin calls that experimental module. Frozen quark-common.toml
has experimental."Spawner Replacer" = false (line 1648); bind its implementation
to this setting rather than inferring activation from the hook declaration.
Glimmering Weald, Gold Bars and Variant Chests are true in the frozen file.
No new independent family has been accepted in this source increment.

Quark archive SHA-256 is
989c465df2e4cb9f602840c2eec143358bf11462cc19dc0b0c7c9f17449e75a5.
Initial full listing has 9367 files and 967 classes, fifteen root worldgen JSONs,
optional datapacks (including three vanilla ore configured-feature overrides)
and a programmer-art resource pack. The nested archive path is
META-INF/jarjar/biolith-neoforge-3.0.10.jar, SHA-256
7f5c86757c61f56c7dccf602b44a2c17ba08d32d7e88cb531cbcd0c7b4789eab.
It has 106 files and 95 classes, twelve common and three NeoForge mixin entries,
a NeoForge mixin plugin, one platform service and no packaged data definitions.
These observations are leads for a bounded shared-biome-provider reconciliation,
not a closure. GlimmeringWealdModule calls Biolith BiomePlacement.addOverworld.
Zeta and its interface-delegate mixin plugin remain a separate provider row.
Do not recapture existing Quark generators or audit unrelated gameplay internals.
Final canonical count, attributes and review/main merge remain open. This turn
made progress through delivered source evidence; no blocker is present.

Latest checkpoint at 82238e0: shared YUNG API provider scope is closed,
pushed and remote-ref verified. Census: 72 resolved providers, 64 open. One
focused case and scoped quality checks pass. Source a796af9 preserves 43
registration/service/plugin/hook entries with exact r1 reproduction; existing
pool-codecs contributes two reused classes. No independent family. The four
empty packaged tags are extended by consuming providers; do not call their
effective values empty. Optional weight injection (upper bound 5000, require=0)
is a declaration, not confirmed execution. Full disposition is in provider-scope.md.

Next reconcile Quark using its existing source directories listed in
the provider queue, its recorded nonregistry families and frozen module state.
Do not recapture known generators or reopen completed YUNG provider work.
Finish its remaining packaged-resource and generation-entry coverage, then the
remaining named providers before canonical family grouping and attributes.
Shared Zeta remains a separate provider responsibility. Final family count,
eleven attributes and clean review/main merge remain open. This goal turn
made progress through a delivered provider closure; there is no blocker.

Latest checkpoint at 967baca: Cave Biomes provider scope is closed, pushed
and remote-ref verified. Census: 71 resolved providers, 65 open. One focused
case and scoped quality checks pass. Source 7f76013 reproduces exactly.
All 38 worldgen resources are accounted for as cave terrain/vegetation and
existing vanilla feature consumers. No independent family. Biome eligibility,
natural mob inputs, common hooks and frozen configuration are recorded in
provider-scope.md. Do not repeat this closure or detailed attribute work yet.

Next: shared YUNG API. Initial archive inspection confirms 197 files, 179
classes, four structure tags and four platform services. Common mixin metadata
selects YungsApiMixinPlugin and fifteen mixins; the NeoForge metadata adds
IncreaseStructureWeightLimitMixinNeoForge. Its sole mod entry is
YungsApiNeoForge. Reuse pool-codecs and existing consuming YUNG source captures;
inspect registration dispatch, plugin and modifier roles before closing this
provider. These initial observations are leads, not acceptance. The first
metadata probe accidentally included class paths containing /services/ and
failed UTF-8 decoding; the corrected probe restricted META-INF/services/.
Canonical grouping, final family count, eleven attributes and review/main merge
remain open. Previous goal turn delivered source evidence; this turn delivered
provider closure. No blocker and no new measurement system.

Latest checkpoint at b270bb3: Better Caves provider scope is closed,
pushed and remote-ref verified. Census: 70 resolved providers, 66 open. One
focused case and scoped quality checks pass. Source d9e30ff reproduces exactly.
Its two configured carvers, two biome modifiers, seven mixins and generation
path contribute terrain/liquid-region support, with no independent family.
Frozen liquid-region input and packaged disabled debug mode are bound by the
focused check. Next inspect Cave Biomes (581 files, 187 classes, 38 worldgen
resources observed in initial archive listing), then shared YUNG API. These
initial counts are leads, not closed scope. Do not repeat Better Caves or other
delivered providers. Canonical count, attributes and review/main merge stay open.

Latest checkpoint at f5b7069: Better Desert Temples provider scope is closed,
pushed and remote-ref verified. Census: 69 resolved providers, 67 open. Seven
focused cases and scoped quality checks pass. Source 02ae27e reproduces exactly.
One existing root, all 28 pools and 198 templates are accounted for; preserve the
disconnected crushing corridor. All 26 processors are component registrations.
Pharaoh, mining-fatigue and saved-state hooks affect the existing temple.
Next reconcile YUNG's Better Caves, Cave Biomes and shared API provider roles,
then the remaining named queue. Keep detailed attributes deferred and do not
repeat completed YUNG structure-provider closures. Whole-stack canonical family
count, remaining boundaries, attributes and review/main merge remain open.

Latest checkpoint at 4d72e0f: Better Dungeons provider scope is closed,
pushed and remote-ref verified. Census: 68 resolved providers, 68 open. Two
focused cases and scoped quality checks pass. Source f9696df reproduces exactly.
Five roots, all 33 pools and 227 templates are accounted for. Preserve the one
disconnected skeleton bridge and missing zombie stair. Six mob-theme labels and
29 processor codecs are component inputs, not additional families. Detailed
processor attributes remain deferred. Next reconcile Better Desert Temples using
the existing desert-temple-suppression source, then remaining YUNG/shared and
other provider rows. Do not repeat Dungeons or earlier closures. Final family
count, canonical boundaries, attributes and review/main merge remain open.

Latest checkpoint at 32b2d46: Better Mineshafts provider scope is closed,
pushed and remote-ref verified. Census: 67 resolved providers, 69 open. Three
focused cases and scoped quality checks pass. New source 26d2a97 reproduces
exactly and complements the existing forty-class generator capture. All thirteen
roots and the sole set remain the existing mineshaft group. Preserve the narrow
far-chunk diagnostic suppression limitation recorded in provider-scope.md.

Next reconcile Better Dungeons using betterdungeons-code, which already captures
seven specialized generator classes. Initial archive inspection found five roots,
227 templates, three declared mixins and both Forge/NeoForge vanilla-dungeon
removal declarations. These are leads, not a closed disposition. Inspect remaining
entry/module/service paths and link all components before updating its row.
Do not repeat delivered Mineshafts work. Final census, canonical family count,
remaining attributes and review/main merge are still open.

Latest checkpoint at 9680555: Better End Island provider scope is closed,
pushed and remote-ref verified. Census: 66 resolved providers, 70 open. Seven
focused cases and scoped Ruff/Basedpyright pass. Nine remaining entry hooks in
6e1f551 reproduce exactly; prior generator and template evidence is reused.
All 41 templates stay assigned to arrival platform, gateway and dragon arena.
Remaining hooks affect their lifecycle, fight state and landing-position search.
Continue the named provider queue, prioritizing reused generation-entry evidence.
Do not repeat this closure or deepen unrelated helpers. The final family count,
remaining canonical decisions, eleven attributes and review/main merge are open.

Latest checkpoint at 97b5249: Better Jungle Temples provider scope is closed,
pushed and remote-ref verified. Census: 65 resolved providers, 71 open. Seven
focused cases, Ruff and Basedpyright pass. Source e4bb5e3 is reused; one existing
root, 17 connected pools and 127 templates are accounted for, including two
disconnected table props. No additional independent candidate was found.

The user's latest correction is that explaining the unknown count is insufficient:
finish finding it. The missing count is unfinished audit work, not a request for
user input. The next deliverable remains the complete named canonical family list
and its denominator, followed by exact outstanding attribute gaps. Provider closure
counts cannot substitute for that deliverable. Continue the 71 named open rows in
evidence/item-8/provider-scope.md using existing evidence first. Limit new source
inspection to generation entry paths and concrete unresolved contributions; do not
capture every class merely to close a provider. Resolve remaining named family
boundaries before resuming detailed attributes. No new measurement system, broader
review framework or downstream work is authorized by this clarification.

Latest checkpoint at 920c24e: Better Strongholds provider scope is closed,
pushed and remote-ref verified. Census: 64 resolved providers, 72 open. Seven
affected cases and scoped quality checks pass. Source 41964b5 reproduces exactly.
One existing root, 12 connected pools and 97 templates are accounted for, with
thirteen disconnected components and one missing spiral_stairs pool. Custom
placement selects this root; entity/block processors modify its components.
Next inspect YUNG's Better Jungle Temples using jungle-temple-suppression.
Do not repeat delivered provider work. Shared YUNG API, canonical grouping,
full attributes and the final Item 8 gate remain open.

Latest checkpoint at 8e2b6df: Better Ocean Monuments provider scope is closed,
pushed and remote-ref verified. Census: 63 resolved providers, 73 open. Seven
affected cases and scoped quality checks pass. Source a2f2832 reproduces exactly.
One existing root, 13 connected pools and 59 templates are accounted for; two
seagrass templates are disconnected, with no missing graph references. Ten block
processors and the specifically marked trident hook modify existing components.
Next inspect YUNG's Better Strongholds using the existing stronghold-suppression
capture. Keep shared YUNG API and canonical grouping work open. Do not repeat
delivered providers or resume detailed attributes before the census closes.

Latest checkpoint at e474790: Better Nether Fortresses provider scope is closed,
pushed and remote-ref verified. Census: 62 resolved providers, 74 open. Seven
affected cases and scoped Ruff/Basedpyright pass. Source 5933abb reproduces
exactly. Its single root, 15 pools, 169 templates and seven custom processor
types have component dispositions. Preserve twenty disconnected templates and
the missing halls/hall_4 reference; halls/hall_4_ is a different packaged ID.
Existing-fortress spawning and item-frame modifications remain attribute inputs.
Next inspect YUNG's Better Ocean Monuments using the prior monument-suppression
capture. Do not repeat delivered provider closures or start detailed attributes
before the provider census and canonical family boundaries are resolved.

Latest checkpoints: IDAS provider scope closed at 26cfbef; Better Witch Huts
closed at 4e96ee2. Both are pushed and remote-ref verified. Current census is
61 resolved providers and 75 open. IDAS's 84 roots, 214 pools and 259 templates
are accounted for, including named compatibility branches, 21 disconnected
pools, 23 disconnected templates and missing pools on three roots. Its Labyrinth
hooks modify an existing encounter. Better Witch Huts has two existing roots,
three pools and six templates, all connected without missing references; its
five processors are component modifiers. Exact source captures, disposition
checks, limitations and passing commands are in evidence/item-8/provider-scope.md.
Do not repeat these closures. Next inspect YUNG's Better Nether Fortresses using
the existing fortress-suppression evidence. Keep shared API dependencies and
canonical family grouping open; do not resume detailed attributes yet.

Latest checkpoint at 086bbc8: Integrated Villages provider scope is resolved,
pushed and remote-ref verified. Five focused cases, Ruff and Basedpyright pass.
Current queue: 59 resolved providers, 77 open. All twelve existing roots, 421
pools and 754 templates have bounded component dispositions. Preserve 51
unconnected pools, 74 unconnected templates, seven roots with missing references,
and four incompatible legacy injection declarations. Shared Integrated API is
still open. Next finish IDAS provider scope using its existing suppression
capture and eighteen remaining classes delivered at afb3cee. The r2 capture
reproduces exactly. Finish component and hook dispositions next. Do not repeat
Integrated Villages or return to detailed attributes before the census closes.

Latest checkpoint at e8875ca: Alternate Current, Cupboard and Loot Integrations
provider scope is resolved, pushed and remote-ref verified. Eighteen focused
utility cases, Ruff and Basedpyright pass. Current queue: 58 resolved providers,
78 open. These three add no independent family. Keep Cupboard's frozen disabled
entity-load suppression and Loot Integrations' actual seven chest-table contents
as recorded; the table named empty contains bone. The core loot modifier remains
an attribute input. All source captures reproduce exactly. Continue the remaining
provider queue using evidence/item-8/provider-scope.md; do not redo these closures.

Latest checkpoint at fd93f7f: BOP provider census is resolved, pushed and remote
ref verified. Five focused cases, Ruff and Basedpyright pass. Queue: 55 resolved
providers, 81 open. All 81 BOP registered feature types have supported roles;
the three coral types are embedded in dead_coral's selector. Preserve anomaly
and monolith candidates plus the named giant-pumpkin/carved-patch boundaries
for canonical reconciliation. Source and final dispositions are under
evidence/item-8/provider-scope.md. Do not repeat BetterEnd or BOP coverage.
Continue the remaining provider rows before attributes or final family counting.

Current checkpoint at 711a696: BetterEnd provider candidate coverage is resolved.
The commit is pushed and its remote ref verified. Thirteen focused cases, Ruff
and Basedpyright pass. Current queue: 54 resolved providers and 82 open, recorded
in evidence/item-8/provider-scope.md. Earlier BetterEnd continuation questions
below are superseded by the delivered root, entry, mixin, modifier, feature and
configured-carver dispositions. Do not repeat those investigations.

The user again identified the missing final family count as the problem to fix.
Serial deep provider inspection has delayed that outcome. Continue the census
across the remaining named rows using existing evidence first. Follow additional
code only for a concrete possible unlisted contribution or family-boundary gap,
not because a class has not been captured. Stop each provider check when its
candidate contribution has a supported disposition. Add no measurement system.
Canonical reconciliation must explicitly resolve named design alternatives and
deduplicate roots, variants, components and nonregistry routes before reporting
a final denominator. Then finish the eleven attributes and final review/merge.
The 887 registry roots and 421 provisional groups are still not final families.

Latest continuation correction at 4307aa7: the paragraphs below are earlier
checkpoints. BetterEnd's complete 128-template partition is now bound by
69fb95a, including the seven extra biome templates, legacy lists, village,
pillars and portals. Frozen generator branch selection is bound by ad9dd54.
Do not repeat those checks. The eight common entry captures in 4307aa7 are
pushed and remote-ref verified; their nine generated files reproduce exactly.
See evidence/item-8/sources/betterend-common-entries/README.md for the bounded
interpretations and preserved limitations.

The user's immediate requested outcome is an exhaustive named candidate list
and a defensible family remainder. Provider counts alone do not satisfy it.
Coverage remains 53 resolved and 83 open. Do not resume detailed attributes
or turn every uncaptured class into another mandatory investigation. Resolve
actual generation and component consumers using the existing evidence first.
For BetterEnd, remaining named entry questions include cave feature dispatch,
the concrete BYG/Flamboyant/DyeDepot integration routes, BetterEndPlugin service
providers, remaining declared common mixin generation hooks, and shared Wover
modifiers. These must be reconciled with the existing roots and feature
registrations. An uncaptured class is not itself a missing family. No additional
measurement framework, world run, or baseline repair is authorized by these
questions. Finish the provider census and explicit grouping decisions before
claiming a final family denominator.

Current continuation: provider census first, with 53 of 136 supported provider
dispositions and 83 open rows in evidence/item-8/provider-scope.md. The later
commits below supersede the older 47-provider checkpoint. Save/structure utility
closure d01ceec is pushed and verified; fourteen focused cases passed. No new
authored family from Fast Async World Save or Structure Essentials.

BetterEnd candidate reconciliation f77f3f2 is pushed and verified. Reused source
and packaged/runtime evidence establish an inline configured crashed-ship route,
27 packaged biome consumers and 21 consumers exposed by the captured End biome
source. Six cave-biome references are recorded separately. The six building
lists have exactly 63 template choices: 21 inspected vegetation exclusions and
42 architectural candidate choices. These are not family counts. Two focused
cases and scoped Ruff/Basedpyright pass; no new capture or world run.

Continue BetterEnd provider coverage before attributes. An exploratory full
archive inspection found seven additional biome templates outside those six
lists: blossoming_spires/house and old_bulbis_gardens/fallen_tree_1 through 3 and
tree_stump_1 through 3. The seven packaged structures.json lists, village,
pillar and portal components, other generation entries and shared modifiers
still need supported dispositions. Do not infer inactivity from no literal
class-string match. The 63-choice result only closes those six configured lists,
not the whole provider. Reuse the existing formation, lake and feature captures.
No canonical-family denominator is accepted yet. Finish all provider rows,
publish named grouping decisions, then complete the eleven attributes and the
required final review/delivery gate. Do not add an unrelated measurement system.

Ritchie's Projectile Library provider coverage now passes. Its complete 34-class
capture 50bc747 using 0cbba5c reproduced exactly. The reused provider test has
12 passing cases. Preserve the packaging finding: both mixin JSON files lack
NeoForge TOML and manifest declarations; their source is not activation proof.
No baseline repair. Projectile/chunk-loading and network support adds no authored
family. Counts: 47 resolved providers, 89 open. Continue the provider queue before
canonical grouping and attributes. Do not expand into projectile physics testing.


Bundle API and Shield API provider coverage now passes. Complete 30-class capture
a14b5e0 using 49dd5dd reproduced exactly. The reused small-utility test has eleven
passing cases. Its initial added cases confused client subscribers with @Mod
entries; test and prose now distinguish them. Both providers handle player items,
rendering and combat/inventory support, with no independent structure family.
Keep Shield API's actual common/client mixin declaration without repairing it.
Counts: 46 resolved providers, 90 open. Continue provider candidate completeness
before canonical grouping and detailed attributes. No additional measurement.


Ocean's Delight provider coverage now passes. Its complete 15-class source is
delivered in 2b575d8 using 75232ba and independently reproduced. Full payload and
four existing aquatic-mob loot declarations are bound by the focused scope test;
scoped checks pass. No independent structure family added. Retain loot provenance
for elder guardian, guardian, squid and glow squid in later attributes. Counts:
44 resolved providers, 92 open. Continue candidate completeness before attributes;
do not expand this provider into food balance or unrelated gameplay tests.


Almanac, Library Ferret and Structure Layout Optimizer provider coverage now
passes. Their complete 38-class capture is delivered in 8c60e03 using 4f65e40;
all three independently reproduced. The reused small-utility test has nine passing
cases, with scoped checks passing. These add no independent authored family;
Ferret's abstract consumer generation and the optimizer's assembly changes retain
explicit roles. Do not audit their geometry or unrelated gameplay further.
Counts: 43 resolved providers, 93 open. Continue the exact provider queue before
attributes or a final family denominator claim. Source commands and role details
are in sources/small-utility-providers.md under evidence/item-8.


Six small utility providers now have supported dispositions: AI Improvements,
AttributeFix, Leaves Be Gone, Let Me Despawn, Sparse Structures and Structure
Pool API. Selector 39ef785 and complete 69-class capture 69119c6 are delivered;
all six captures reproduced byte for byte. The six-case full-payload test passes
with scoped checks. No independent families added. Sparse Structures and the
pool API retain explicit modifying roles; entity/leaf effects remain attributable
later. Counts: 40 resolved providers, 96 open. Continue candidate completeness
before detailed attributes, reusing captures and existing consumer relationships.


CTOV provider coverage now passes: complete payload, 78 existing roots, 181 pools
and 2,093 current-path templates accounted for. Outside its root graphs, 1,005
templates have condition-failing compatibility references and 128 are disconnected
components. Nineteen disconnected pools and 27 roots with missing resources are
preserved, not repaired. Seven focused cases pass. Reuse the existing source,
selection, bundle and scope checks. Counts: 34 resolved providers, 102 open.
Candidate completeness remains the immediate deliverable before attributes;
887 registry roots and 421 provisional groups still do not establish final families.


CTOV bundled compatibility resources now have a passing focused check in
test_ctov_bundled_resources.py. Mushroom ZIP contains five processor documents
and metadata identical to loose copies; Savage and Ravage has eleven old-path
outpost components. Two .jso files only reference existing roots and are outside
the JSON catalog. Do not enable, migrate or count these as families. Remaining
CTOV coverage: ordinary full payload and disconnected/missing components with
modifier relationships. Code, frozen selection and bundle checks must be reused.
Counts unchanged: 33 resolved, 103 open. No baseline or family-decision changes.

CTOV frozen callback/modifier selection now has a focused passing regression.
It binds 74 callback-selected roots (63 villages and eleven outposts) to the
registry; mesa outpost and three underground-size roots remain outside that
callback list, not deleted from the inventory. Of 1,019 catalog modifier JSON
records, 63 pass mod conditions (21 each Chef's Delight, Farmer's Delight,
Village Taverns); 956 fail. Reuse test_ctov_provider_selection.py and source
82ac234. Remaining provider coverage: full payload and compatibility ZIP/directories,
disconnected/missing components and modifier relationships. Counts unchanged:
33 resolved, 103 open. No new parser, runtime or baseline change.

CTOV twelve-class entry/component capture delivered in 82ac234 using 61663b4;
independent extraction reproduced at evidence/raw/item8/ctov-provider-r1.
Startup adds configured existing roots to vanilla sets through Lithostitched;
the compatibility processor transforms existing blocks. Outpost selection uses
the callback's own list, not enabledpillageroutpost. Preserve the unused helper
return-descriptor mismatch without claiming a reproduced runtime failure.
Remaining coverage: bundled compatibility directories/ZIP, modifier-driven
components outside root graphs, explicit disconnected/missing dispositions,
and frozen configuration binding. Both packaged mixin lists are empty. Reuse
this source and existing CTOV regressions. Counts unchanged: 33 resolved,
103 open. No new parser, measurement framework or baseline change.

AdoraBuild provider coverage now passes. Seven-class source delivered in 6aac21f
using 6fcc20c and reproduced independently. All 106 existing roots, 110 pools
and 121 templates accounted for; no disconnected components. Preserve missing
minecraft:basalt_chambers/chambers on basalt_chambers_large_1. Two focused cases
and scoped checks pass. No family grouping or baseline change. Counts: 33
provider dispositions, 103 open. Continue the exact provider queue before
attributes; do not repeat AdoraBuild code or introduce another resource parser.

Integrated Stronghold provider coverage now passes. All nine classes delivered
in 0bca5a4 using f70a1a0 and reproduced independently. One existing root, 44
connected pools, three disconnected templates and two missing armory references
are accounted for. Both suppression/locate mixins have explicit dispositions;
do not treat their artificial locate position as an observation. Two focused
cases and scoped checks pass after accounting for the external minecraft:empty
pool. Counts: 32 provider dispositions, 104 open. Continue the named queue before
family attributes; do not repeat this provider capture or repair the baseline.

Moog shared-library provider candidate coverage now passes. Registration and
lifecycle boundaries delivered in ee8e2c0 using f28c96b. The full payload and
declared entry/service/mixin routes are bound by test_moog_library_provider_scope.py;
five focused cases and scoped checks pass. No independent family is added by
the library. Reuse all eight capture directories and do not expand this provider
into geometry or registry-container internals. Effective consumer attributes
remain later work. Counts: 31 dispositions, 105 open. Continue the named provider
queue before resuming family attributes or claiming a final family denominator.

User again requires the actual complete family denominator, not repeated reports
that provider coverage is open. The immediate deliverable remains the complete
candidate list with explicit family/variant decisions and named ambiguities.
Track closed/open providers separately; 887 registry roots and 421 provisional
groups are not the final family denominator. Do not resume detailed attributes
until this deliverable is established. Reuse evidence and stop at relevant
generation boundaries rather than tracing every library helper.

Moog direct helpers delivered in cd015c3 using 266938e, reproduced at
evidence/raw/item8/moog-direct-boundaries-r1. MixinUtils reads existing tagged
starts, DebugFlags initially defaults false, EnhancedBeardifierHelper adapts
terrain around existing starts, and the service resolves ResourcefulRegistriesImpl.
Do not repeat those inspections. NeoForgeResourcefulRegistry remains the direct
registration boundary. Whole-provider reconciliation is not yet closed; counts
remain 30 dispositions and 106 open. No family count or completion claim follows
from this source capture alone.

All sixteen declared Moog mixins delivered in a7af1d6 using c388784 and reproduced
at evidence/raw/item8/moog-declared-mixins-r1. Ten accessors, six behavioral hooks.
StructurePoolMixin raises a codec weight bound to 5000, not content injection;
optional injection remains distinct from runtime activation. Remaining direct
boundaries: registry/service dispatch, MixinUtils, EnhancedBeardifierHelper and
DebugFlags. Do not repeat mixin capture or expand into geometry/noise internals.
Count unchanged: 30 provider dispositions, 106 open. Continue candidate coverage.

Moog callback/reload/command capture delivered in 5a83e4c using 6d7a961,
reproduced byte for byte at evidence/raw/item8/moog-provider-callbacks-r1. The
entry callback bootstrap omission is resolved. TrialSpawnerConfigManager loads
JSON compound values, logging/skipping invalid entries. DebugCommand calls flags
and reports status; keep-jigsaw downstream behavior remains with the pending
mixin. Continue declared mixins and registry/service dispatch. Count unchanged:
30 provider dispositions, 106 open. Do not repeat callback or reload inspection.

Moog shared library entry/registry capture delivered in 88bafe0 using e5341ca;
eight classes reproduced at evidence/raw/item8/moog-provider-entries-r1. Provider
still open: declared mixins, callback bootstrap targets, registry/service dispatch,
trial-spawner reload and debug command remain. Non-verbose callback output does
not bind every invokedynamic target. Do not repeat the four closed Moog data
providers or trace unrelated geometry/noise utilities. Count remains 30/136
supported provider dispositions, 106 open. See source README for exact next scope.

YUNG Extras provider coverage now passes. Remaining seven classes delivered in
4d7edec using 04db73f; all 29 classes and full payload accounted for. All 62
templates are assigned, 59 by JSON and three by existing code links. Nine focused
cases and scoped checks pass. No new family grouping or runtime. Queue updated:
30 dispositions, 106 open. Continue remaining providers; do not repeat Extras
source interpretation or mistake configured-feature counts for families.

YUNG Bridges provider coverage now passes. Remaining seven classes captured in
a20bccf using dfca574; full 31-class payload is accounted for. Existing feature,
template and processor evidence reused. Seven focused cases and scoped checks
pass. Preserve SuppressLogMixin's far-chunk-warning limitation. Three disconnected
wood templates remain excluded from active candidates. Queue: 29 dispositions,
107 open. Do not repeat this provider capture or infer canonical families from
22 configurations/eleven referenced templates. Continue coverage before attributes.

Better Village provider closure reuses seven-class source 45ab692 and existing
contribution regression. Full payload accounted for: 246 replacements, four
disabled/absent compatibility targets, two named disconnected snowy streets.
Both focused cases and scoped checks pass. No new family or capture. Exact queue
updated to 28 provider dispositions and 108 open. Continue coverage before
attributes; do not repeat this provider pass.

WDA provider scope now passes with all six classes captured in 1b230be using
f3ac5ab, reproducible at evidence/raw/item8/wda-provider-scope-r1. Forty packaged
roots all use vanilla jigsaw; no extra root from the custom registered type.
Twelve disconnected pools, 54 disconnected templates, six non-structure functions
and missing references on four roots have explicit dispositions. Focused test
passes; scoped checks pass after an unused noqa correction. Queue updated:
27 supported provider dispositions, 109 open. Do not recapture WDA or repair its
baseline components. Continue provider coverage before detailed attributes.

User requires resolution of the unknown candidate denominator. The exact open
provider queue in evidence/item-8/provider-scope.md now names all 110 remaining
archives, existing capture directories and next checks. Together with 26 closed
dispositions it reconciles the retained manifest. This is a work queue, not
acceptance evidence. Resolve it before detailed attributes; stop helper tracing
once the candidate boundary is supported. No new measurement system is needed.

Towns and Towers scope now passes: 60 roots, 187 pools, 837 base templates;
three disconnected pools and 23 disconnected templates explicitly accounted for.
The optional three-template Waystones pack requires an absent captured mod ID.
Preserve missing-reference dispositions on eight existing roots without baseline
repair. The focused test and scoped checks pass. Counts: 26 provider dispositions,
110 remaining. Continue remaining providers; do not repeat these wrapper captures
or count tags as roots. Shared Cristel Lib loading remains its own provider scope.

Seven Seas provider scope now passes: five roots, ten pools, 36 templates and
its sole logging-only class are accounted for. Preserve the already recorded
small_yacht_spawner_3 missing component; no baseline repair or new family.
Focused test and scoped static checks pass after the NBT-extension and indentation
corrections. Counts: 25 dispositions, 111 remaining. Next Towns and Towers:
entry source delivered in 1608481; use resource_identity to avoid counting
structure tags as roots, and reconcile its Waystones pack/disconnected resources.

Village Taverns full-provider scope now passes: all fifteen top-level classes,
bundled Tiny Config entry, parent/nested files and five component links are
accounted for. The focused test and scoped static checks pass after recognizing
the inspected villager-hat .png.mcmeta asset and formatting. provider-scope.md
now records 24 dispositions of 136, leaving 112 to reconcile. Stop Tavern source
expansion and continue other retained providers using existing evidence first.

Bundled Tiny Config entry and ConfigManager captures now reproduce using 0b01353
in sources/tiny-config-entry. NeoForge entry calls an empty common init;
ConfigManager handles JSON I/O and optional caller callbacks, not independent
generation registration. Do not recapture these. Finish remaining Tavern entry
classes and full archive accounting. Counts remain 23 dispositions, 113 open.

Necessary capture-path adjustment: Village Taverns bundles executable Tiny Config
classes, while the existing javap capture only reads top-level JARs. The narrow
Tiny Config selector retains the existing identity format, verifies both frozen
parent and nested payload, and uses a cleaned temporary classpath. This directly
closes an otherwise unsupported entry path in the candidate-completeness gate;
it adds no measurement system or general recursive capture framework.

Tavern Defaults and block-registration captures now reproduce using 297edcb in
sources/tavern-registration-scope. Defaults links the same five village/tavern
identities as packaged additions; fallback integer arguments must not replace
the packaged Lithostitched weight. Block registration adds barrel block/item and
a creative-tab entry. Remaining full scope includes other relevant entry classes
and bundled tiny-config behavior. No full Tavern closure yet; counts stay 23/113.

Village Taverns entry/mixin source is captured reproducibly using d8d1107 in
sources/tavern-provider-entries. Its StructurePoolAPI injection is conditional on
Lithostitched absence; do not double-count fallback and packaged additions.
Mixins affect potion compatibility and bartender scheduling. Full provider
closure still needs remaining registration helpers/defaults and bundled
tiny-config entry accounting. Counts remain 23 dispositions and 113 to reconcile.

Chef's Delight now has a full-provider component-only disposition. All six
classes are captured, with the remaining four delivered in 23ee872. Full file
accounting and the existing component-content test pass, as do scoped static
checks. provider-scope.md now records 23 of 136 dispositions; 113 remain to
reconcile. Continue remaining code providers and injection relationships.
Do not repeat Chef's Delight source or trade/house analysis.

Explorify's data scope is accounted for: 23 roots, 57 pools, 165 current templates
and 165 identical legacy copies. Thirteen disconnected pools and thirty
disconnected templates are explicitly named in provider-scope.md. The focused
test and scoped static checks pass after formatting. There are now 22 explicit
provider dispositions of 136, leaving 114 to reconcile. The data-only batch is
finished. Next: remaining code-provider roles and injection relationships,
reusing delivered captures before adding source selections.

Moog Nether data scope is now reconciled: all 52 roots, 168 pools and 459
templates accounted for, including 12 disconnected pools, 162 unselected version
alternatives and nine other disconnected templates. Four reused provider cases
and scoped static checks pass. provider-scope.md records 21 of 136 dispositions;
115 remain. Continue Explorify, then code-provider roles and injections. Do not
repeat the four closed Moog data-provider checks without a relevant change.

Voyager's data-provider boundary is now accounted for: 129 roots, 149 pools,
327 templates; 51 unselected version alternatives and 41 named disconnected
templates outside the root graph. The reused three-provider test passes with
scoped static checks. provider-scope.md now records 20 of 136 explicit provider
dispositions, with 116 to reconcile. Continue Explorify and Moog Nether unmatched
resources, then remaining retained-provider roles; shared Moog implementation
coverage is separate from these closed data-provider boundaries.

Moog End and Soaring candidate boundaries now reuse the existing pool traces:
all packaged roots and pools linked, and all unmatched templates explicitly
unselected by the existing versioned-element logic. Two focused cases and scoped
static checks pass. provider-scope.md now has 19 explicit provider dispositions,
with 117 remaining to reconcile. Explorify, Moog Nether and Voyager still have
unmatched resources. Do not repeat the closed End/Soaring pass or call their
25/35 roots canonical-family counts.

Candidate-boundary reconciliation now includes the RS Farmer's Delight add-on:
all 13 templates link to 12 already registered RS village targets; 11 processor
lists modify components rather than create roots. The focused full-archive test
passes, with scoped static checks passing after type/string corrections.
provider-scope.md has 17 explicit provider dispositions; 119 remain to reconcile
with existing evidence. This is not a family count. Continue the five data-only
structure providers and remaining code providers before detailed attributes.

Construction-provider entry captures are delivered in 007ff06. The nine Macaw
constructors and full-payload checks now support explicit no-independent-family
dispositions in evidence/item-8/provider-scope.md. Nine focused cases and scoped
static checks pass. Do not recapture those entry points. Continue whole-stack
provider roles and unexplained resources before detailed family attributes;
the 136-archive search index still does not prove candidate completeness.


User priority correction: candidate completeness FIRST. The 136-archive keyword
search index is not proof of a bounded candidate universe. Current gate and
supported provider dispositions are in evidence/item-8/provider-scope.md under
"Candidate-completeness gate and supported provider dispositions". Use existing
evidence to give every mod supported roles and explain potentially structural
unmatched templates, pools and hooks. Do not complete individual attributes or
canonical grouping before this whole-stack gate. Seven loot-data-only add-ons
now have full-payload exclusion proofs, not keyword-based exclusions.
Totem packaged-eligibility disposition is dc45426, published in c21d68e. It is
inactive under captured dimension memberships; no further helper tracing needed.


Scope-pass sources are delivered: BetterEnd building lists/crashed ship in
9695ae5, BOP anomaly/monolith/bone spine in 846bc09, Deep Aether totem in b0194ce,
and Explorations scarecrow in ac990fd. All reproduce exactly. Their concrete
results and remaining scope decisions are in evidence/item-8/provider-scope.md,
under "Reconciliation checkpoint at ac990fd". Do not recapture these classes or
resume detailed helper tracing. Next bind the existing configured/placed and
biome relationships, reconcile mixed BetterEnd designs, and finish the provider
queue and Moog/village canonical boundaries. No final family count is accepted.

### Continuation update - 2026-09-05

Whole-stack candidate enumeration is now delivered by d475f15 and dd8cc26;
the existing extractor's source join is 21eaef5. Current scope reconciliation
queue and provider counts are in evidence/item-8/provider-scope.md. This is the
priority, superseding Farmer's Delight-first attribute work below. All retained
archives have named candidate rows; resolve those rows and canonical alternatives
before returning to granular attribute tracing. The scan does not itself prove
the final family count. User explicitly requires that count to be established.


Priority correction requested by the user: finish the whole retained-provider
scope pass before further individual component tracing. Existing packaged
catalogs cover every archive but do not enumerate code-only generation hooks
across all archives. Extend the existing source extractor with a narrow code
reference inventory, including nested JARs, to make this missing coverage pass
reproducible. This is needed to establish the finite remaining provider list;
packaged-data-only inspection cannot close that demonstrated gap. Reference
matches are review candidates, not family counts or semantic absence proofs.
No new framework, schema, measurement run or exhaustive helper tracing.


Current progress and definition of done are reconciled in evidence/item-8/README.md
under "Current delivery work at 934dbcb". That section supersedes older next-step
instructions below. Chef's Delight direct content is integrated and published
in c3b345f and 934dbcb; inventory reproduction is exact and family rows unchanged.
Next is Farmer's Delight/provider coverage, then canonical reconciliation and
required attributes. The user requests frequent concrete updates on completed
work and what remains. Do not imply a known remaining-family count while coverage
is open, or use generic INCOMPLETE rows as a progress measure.

Chef's Delight provider component relationship and frozen weights are recorded
in c51df00; source injection capture is d6e6740. It appends to runtime templates,
not rawTemplates. Both plains additions read cookHousePlains. Do not repeat
those captures or assume packaged/raw pool serialization contains the added
houses. Next: reconcile runtime-only village component content with consumers
and continue Farmer's Delight/provider coverage. No standalone house families
were added. Frozen settings are recorded as inputs, not measured runtime counts.

Resumed after user pause. Archive-list coverage check delivered in b06a842:
both packaged catalogs match all retained candidate and platform identities.
Five inventory-source tests and scoped static checks pass. This is archive
coverage, not complete provider contribution coverage. Village Taverns has an
explicit component disposition in c8577f6, reusing existing village/IDAS links;
no new family rows. Continue remaining provider reconciliation. Chef's Delight
and Farmer's Delight packaged village components are candidate next consumers;
their injection relationships must be checked against existing evidence before
new source work. Do not resume exhaustive Bronze helper tracing by default.

Scope reassessment following the user's expansion concern: repeated helper
tracing has become too granular. SPECS Item 8 requires eleven inventory
attributes, not exhaustive implementation reconstruction, measured encounter
populations, balance or discovery-distance experiments. Preserve source limits
without turning every possible runtime qualification into a new acceptance
gate. Before any further capture, name the unresolved required attribute and
why existing evidence cannot answer it. No new framework or measurement system.

Bronze trap, processor callback and conditional surface-clue findings are
integrated in d4482a1; the generated inventory reproduces exactly. Source
captures are in 0ae8368, 4ce02d8 and 63009b4; assembly findings in 6fb0d0c.
Do not repeat them. Next priority is retained-provider coverage using existing
manifest, packaged catalogs and contribution records, then outstanding family
attributes. Bronze remains incomplete; its open implementation questions must
be assessed against the required attribute before further tracing.

Bronze template/marker attribution is integrated in ca135b3. Its six template
candidates and processor inputs are bound by the focused test from 677365d;
placement/mimic/loot source captures are in a45a37c, assembly captures in
7489c02. Two focused tests and scoped static checks pass. Inventory changes
only the Bronze row and decision identity. Do not repeat these captures or
catalog joins. Next: finish builder/surface-ruins interpretation, inherited
chest placement and processor callback binding, relevant sentry/trap behavior,
and required geometry/placement/visibility. Silver and Gold remain afterward.
No new world measurement or measurement system has been added.

Aether cloud provider and direct content have a working terrain/cloud
disposition in 6ab0446; entry/writer captures are in e2dd34b. Its registry row
remains for coverage, not an accepted authored family. The focused test and
scoped static checks pass; inventory reproduction is exact. Do not repeat the
provider/writer join. Continue BronzeDungeonBuilder and direct dungeon pieces,
then Silver and Gold assembly/content dependencies. No new world measurement.

Aether custom roots still lack generator attribution. Select the retained
Aether archive's BronzeDungeonStructure, SilverDungeonStructure,
GoldDungeonStructure, LargeAercloudStructure and LargeAercloudChunk with the
existing extractor. The cloud writer is needed to resolve whether that registry
root is a structure family or terrain contribution. Inspect direct dependencies
before assigning content; do not add a new baseline or measurement system.

Monument processor effects are integrated in 077fcd2 using dc9ac0a's reproduced
captures. The inventory preserves downward support extent, state-only pillar
writes, surface finalization and unseeded ordering as source findings with
runtime/geometry limits. Two focused tests and scoped static checks pass;
inventory reproduction is exact. Do not repeat these processor captures or
candidate-content joins. Continue unresolved engine/registration dependencies
only where required for an attribute, and the remaining provider coverage.

Trace the five custom processor/predicate implementations referenced by the
monument lists, plus RSProcessors to bind their registered identities. Pillars
affect vertical extent, surface delegation affects archaeology loot, and the
Y predicate affects lava placement. Noise/random replacements are current
inputs to these same lists. Use the existing extractor and no new measurement.
Do not infer the structure_surface_processor class from a filename: the archive
contains CappedStructureSurfaceProcessor, so verify the registration binding.

Monument packaged encounter and loot inputs are integrated in 62f005a and the
inventory reproduces exactly. Do not repeat candidate entity/chest joins.
Processor documents add jungle archaeology loot and downward pillar paths;
their custom implementations remain untraced. Reuse existing catalogs and
extractor to resolve only effects needed for content and geometry attribution.
Six affected tests and scoped static checks pass. No world measurement or
Item 8 completion claim.

Monument fitters and their interface are delivered in 58cbbfa. The interface
is abstract, correcting the earlier default-opening assumption. The focused
catalog test reconciles 76 candidate pools and 88 templates; it passes with
scoped static checks. Inspect the five referenced nonempty processor lists and
candidate template content next. Preserve wall_2's unassigned source relationship
and graph-reachability uncertainty; do not count components as families.

Monument entry and building captures are delivered in 5fceeb4 and reproduced
exactly. Follow the eight named Fit*Room classes and MonumentRoomFitter's
default opening creation. Their pool references are the remaining direct
component-selection gap. Use verbose output for concatenation recipes, then
join existing catalogs. Do not repeat entry capture or add a layout simulator.

Inspect the missing Repurposed Structures monument entry, assembly and base-piece
paths using the existing extractor. The working monument decision explicitly
lacks custom layout/content attribution. Select MonumentStructure, MonumentPieces
and its MonumentBuilding/MonumentPiece classes; retain verbose pool-name bindings
for the two piece classes. This closes a required family attribution gap without
adding a new extractor, schema or world measurement.

Mansion candidate content and source placement are integrated in 8ba362c.
Child template entities, chest loot references and selected spider spawner
inputs are tested; surface anchoring and the foundation envelope limitation
are explicit. The working inventory reproduces byte for byte. Do not repeat
these catalog joins. Exact layout reachability, runtime loading, geometry,
external effects and discoverability remain open. Continue the remaining
custom-generation and provider-coverage work in the evidence README.

The remaining delivery work is now listed in evidence/item-8/README.md, under
"Remaining delivery work at 4a8478b". Use the existing family and contribution
records to resolve that list; do not add a progress measurement system. Provider
coverage is still incomplete, so the list is not a claim that every remaining
family has already been identified. Integrate the delivered mansion findings
next, then continue the listed custom-generation and coverage gaps.

Mansion spawner/processor inputs are bound in 4a8478b. Ten focused tests and
scoped Ruff/Basedpyright pass. The selector type declarations now admit these
two existing JSON consumers. The unrelated village bamboo crop processor
collision remains open for its own consumers. Do not repeat this mansion input
check or claim successful runtime reload/spawning from its packaged inputs.

Mansion candidate-pool reconciliation is tested in 77e7d0e: 376 candidate
pools, 592 parent templates and five shared child templates are present.
Keep candidate selection distinct from layout reachability and placement.
Inspect the referenced mushroom/spawner processors and spawner data manager
using the existing extractor to resolve their direct content effects.

The ordinary mansion layout capture in aaeaabc omits invokedynamic string
recipes needed for exact pool IDs. Enable existing verbose output for the
layout and three floor selectors. This fixes that concrete attribution gap;
preserve the ordinary attempt. MirroringSingleJigsawPiece is already captured
under pool-codecs and should be reused, not recaptured.

Mansion entry/foundation paths are preserved in 80b4fc4. Follow the direct
LayoutGenerator and its RoomCollection/FirstFloor/SecondFloor/ThirdFloor
selectors to bind component pools. Existing saved-piece envelopes exclude
possible foundation extension. Reuse existing catalogs and tracing tools.

Continue Repurposed Structures mansion custom-generation attribution with
MansionStructure, MansionPieces and MansionStructurePiece. Existing pool traces
do not resolve this custom path. Reuse the extractor and template catalogs;
inspect delegated layout code only as needed for component/content attribution.

Slime Cave custom components and encounters are integrated in 0feca29, with
processor attribution in 9f7b811. The focused test binds its single template,
six slime markers, one spawner marker and chest loot-table selection. Existing
world envelopes agree with the 15-by-15-by-12 template bounds. Do not repeat
generator, marker or material-processor tracing. Continue visual-discoverability
and relevant global-effect gaps, other custom families and provider coverage.
Five affected tests and scoped checks passed. No new measurement; Item 8 open.

Slime Cave's custom structure and piece are preserved in d3543c5. One rotated
template supplies slime and spawner markers. Inspect its DeepslateProcessor
before final effective-content attribution, then bind the existing template
catalog in a focused test and integrate the required attributes. Do not repeat
generator/marker tracing or create a new measurement system.

The provider review confirms Explorations Slime Cave still lacks custom
generation/component attribution in the existing inventory. Inspect its
SlimeCaveStructure and SlimeCaveStructurePiece using the existing extractor.
This closes a concrete required-provider gap; no new framework or measurement.

Stone-generation paths have working terrain dispositions in 6e61b10.
The delegated ore writer is preserved in 332d9d5 and writes only the supplied
stone state. Do not repeat cluster/ore writer tracing. Continue broader provider
coverage and unresolved required family attributes. All 32 affected tests and
scoped static checks passed. No new measurement; Item 8 remains incomplete.

Stone cluster captures are delivered in a17831b. The direct cluster writer
places one configured block state. NewStoneTypes also delegates to Zeta
OreGenerator; inspect that existing dependency before its final terrain
disposition. No further cluster-writer tracing or new measurement is needed.

Inspect BigStoneClustersModule, NewStoneTypesModule, experimental
VanillaStoneClustersModule and BigStoneClusterGenerator (including its direct
anonymous writer). These retained paths need terrain/family reconciliation.
Reuse the existing extractor; no new measurement or infrastructure is required.

Blossom trees and water petals have working vegetation dispositions in
0c1cf13. Selected blossom definitions are vanilla trees with no decorators,
verified by the test delivered in 22a27c0. Do not repeat this boundary or trace
unrelated tree materials. Continue other provider paths, including the still
unreconciled stone-cluster contributions, and required family attributes.
All 32 affected tests and scoped static checks passed. No new measurement.
Item 8 remains incomplete; no final review or merge is claimed.

Check BlossomTreesModule and CherryGroveWaterPetalsModule with their direct
generators through the existing extractor. Provider coverage requires a
source-backed vegetation or family disposition for these paths; names alone
are insufficient. Do not expand into unrelated tree materials or crafting.

Corundum and Permafrost have working terrain-contribution dispositions in
4e2b6fe, with fill dispatch captured in 632fe6c. Their inspected styles decorate
existing surfaces and replace terrain materials, without additional authored
structure families. Do not repeat the fill chain to establish this same boundary.
Broader coverage, effective tags/configuration and world occurrence remain
limited as recorded. Continue other provider paths. All 31 affected tests passed.

Inspect CorundumModule, PermafrostModule and their two underground styles using
the existing extractor. These sources are needed to distinguish additional
families from terrain contributions in Quark coverage. No new framework or
measurement is needed. Preserve uncertainty if a delegated generator remains
unresolved; do not classify from module names alone.

The optional spike-decoration investigation is dispositioned in de6b0dc.
Keep both conditional materials and exact selection UNKNOWN. Do not capture
CompressedBlocksModule merely to choose between the two decorations: the source
branches rejoin before identical spawner/chest operations and preserve geometry.
This does not waive required family attributes, provider coverage or world
observations. Return to broader coverage and unresolved gameplay-relevant inputs.
All 31 affected tests passed; no new source capture or measurement was added.

Shared direction geometry is resolved in 239f150 from capture 49df38d.
HORIZONTALS is NORTH, SOUTH, WEST, EAST. Nether spikes request a 3-by-3 footprint;
Fallen Log side decoration is perpendicular, giving possible 5-by-3 or 6-by-3
envelopes with end decoration. Do not repeat array or geometry analysis. Continue
remaining decoration/configuration dependencies and broader provider coverage.
All 35 affected tests passed. Item 8 remains incomplete.

Select only Zeta MiscUtil to bind HORIZONTALS. Its actual array contents affect
two current consumers, Nether spike footprint and Fallen Log orientation and
decoration. Existing captures reference but do not define this array. Reuse the
existing extractor; do not interpret unrelated utility methods or add a new
measurement system.

Nether obsidian spikes are integrated as one working family in 4151e8c, with
ordinary and large encounter variants explicit. The large variant authors a
blaze spawner and chest using the selected minecraft:chests/nether_bridge table,
bound by 7455ffc. Source geometry and initial settings are captured in f566496.
Do not repeat generator or shared Zeta mapping. Remaining direct dependencies
are CompressedBlocksModule decoration and MiscUtil.HORIZONTALS contents, plus
relevant global loot/ambient spawning and world attribution. Broader provider
coverage remains incomplete. All 35 affected tests passed; no new measurement.

Continue Quark provider coverage with NetherObsidianSpikesModule and
ObsidianSpikeGenerator through the existing extractor. These direct sources are
needed to decide landmark-family inclusion and the required placement/content
attributes; the registry-root inventory cannot account for their direct feature
path. Capture only these two classes, including annotations and callback targets.
Do not repeat shared Zeta configuration or Monster Box investigations.

Monster Box now links the preserved central Overworld sample in 21b40f3.
All 64 sampled full chunks have no Monster Box block states or matching block
entities. Keep this negative result and do not enlarge the sample just to obtain
a hit. Positive occurrence and live encounter remain unobserved. No more
Monster Box enablement, activation or loot source tracing is needed. Return to
broader retained-provider coverage and remaining family attributes. The existing
projection can serve other current families; do not decode the same sample again.
All 35 affected tests passed. Item 8 remains incomplete.

The existing central-block extractor now permits Overworld selection while
preserving its End default and the same fixed X/Z survey bounds. This is needed
because the retained End projection cannot establish Monster Box occurrence;
the existing world-bound and context outputs also omit placed block content.
Reuse the hash-bound ordinary run-a archive, not a new server or world. This is
a second consumer of the existing projection, not a new measurement framework.
An observation can establish presence in the sampled area only; absence there
must not become a claim that the family never generates.

Monster Box initial enablement is resolved in c221e11. The captured category
has no required mod, the selected annotation converter supplies no overlap
candidates, and ConfigManager applies enabled category settings before module
settings during the preserved initial refresh. Both frozen toggles are true.
Do not repeat enablement, field mapping, activation or loot investigations.
Saved-world attribution, relevant ambient spawning and broader provider coverage
remain open. All 31 focused tests passed; no new measurement was added.

Monster Box enablement follow-up selects only ZetaCategory and
ZetaLoadModuleAnnotationData through the existing extractor. The captured
setEnabled path checks category requirements and overlap, but the preserved
sources do not define those inputs. Frozen category and module toggles are true.
These two definitions are needed to distinguish configured from effective
enablement for Item 8 applicability; no new measurement or evidence framework
is warranted. Scoped extractor checks pass. Capture and inspect these inputs
before claiming effective enablement.

Monster Box is integrated as one working encounter family in `0e582dd`.
Generation, activation, selected mobs/rewards, callback targets and initial
frozen settings are preserved in the existing Monster Box source directories.
Do not repeat those investigations. Effective category/overlap enablement,
ambient spawning and saved-world attribution remain open. All 31 focused tests
passed. Broader provider coverage and Item 8 completion remain open; no new
measurement system was added.

Fallen Logs are integrated as one working family in `ec8a1e9`, with generator
and decoration interpretation in `41bda20`. Do not repeat those interpretations.
Configuration mapping, effective tags, hollow-log dependency and world
attribution remain open. Monster Box block/entity behavior is the next direct
encounter-content gap; its module and generator are already captured. Thirty
focused tests passed. Broader retained-provider coverage remains incomplete.

Fairy Ring and associated buried ore are one working family in `79c866d`.
The captured generator interpretation is delivered in `db36cc4`; do not repeat
its geometry analysis or split the deposit into another family. Configuration
callback binding, effective tags, delegated flower effects and world attribution
remain open. Fallen Logs and Monster Box source captures are already preserved
in sources/quark-landmark-encounter-generators under evidence/item-8. Continue
those interpretations and broader coverage. Thirty focused tests passed.

Spiral Spires generation-setting binding is resolved in `c96729d`. The inventory
joins source mapping, frozen/captured file equality and the initial-refresh log.
Do not repeat the configuration-name or field-binding investigation for this
family. World occurrence, natural spawning, other Quark consumers and broader
provider coverage remain open. Thirty focused tests passed. No new runtime or
measurement system was used.

Configuration binding sources are preserved in `sources/zeta-config-binding`,
`sources/quark-spire-config-annotations` and `sources/zeta-config-event-fields`
under evidence/item-8. The latter README binds the initial refresh call to the
existing registry-r1 debug log and resolves nested leaf annotation names.
Do not repeat event execution or leaf predicate tracing. Reconcile parent
section naming and frozen-file provenance using existing artifacts, then update
the inventory's configuration attribution. No runtime field dump or spire
observation is claimed. Broader provider coverage remains open.

Spire biome filter semantics are integrated in `4233dec`, using compound and
component captures delivered in `fb71580` and `e0792bc`. The default empty tag
blacklist passes and the explicit allowlist admits End Highlands only. Do not
repeat predicate tracing. Effective configuration binding, world attribution,
other Quark consumers and broader provider coverage remain open. Thirty focused
tests and scoped checks passed. No new measurement system was added.

Spiral spire is one working landmark family in `0288f13`; repeated spires and
random geometry remain instances/variants. Chorus vegetation is accounted for
without a separate structure family. Source-derived attributes reference the
existing captures and geometry derivation. Configuration binding, biome
predicates and saved-world attribution remain open. Thirty focused tests and
scoped checks passed. Do not reopen the procedural-versus-template distinction
merely because the generator is outside the structure registry.

Spiral spire geometry and direct contents are interpreted in `4586c78`, using
existing captured code. Conservative requested-write envelope is 35x97x35,
not an occupied measurement. Full geometry formulas and preflight limitations
are in spiral_spire_geometry. This resolves the geometry portion of the older
zeta_resolution.remaining note. Configuration binding, biome predicates,
provider/family boundary disposition and other consumers remain open. Thirty
focused tests and scoped checks passed; no new measurement was added.

Zeta/selected Quark call-chain attribution and frozen settings are integrated
in `d961290`. Inherited Generator unwraps ServerLevel and dispatches into the
captured multi-chunk implementation. Frozen radii are 7 and 15; effective field
binding remains open, alongside complete spire geometry, biome predicates,
other Quark consumers and Forgified Fabric callbacks. Thirty focused tests and
scoped checks passed after a test typing correction. Do not repeat captured
library tracing. Item 8 and broader provider coverage remain incomplete.

Shared applicability sources are delivered in `1d6be84`. Source search uses
ceil(radius/16) neighboring chunks; DimensionConfig's LevelAccessor overload
requires a Level. Resolve the inherited Generator.canGenerate/generate caller
before interpreting this as disabling WorldGenRegion generation. Capture only
that exact base class through the existing extractor.

Quark generator capture is delivered in `a7af165`. Both reject source positions
closer than 1050 to origin, but that alone does not bound generated parts.
Resolve MultiChunkFeatureGenerator and DimensionConfig through the existing
extractor, then reconcile frozen radii and dimensions. These are direct
applicability dependencies, not permission to expand unrelated library tracing.

Quark registrations are delivered in `c4cb9ec`; Zeta DeferredFeature execution
link is in `de0cdac`. Inspect the directly registered ChorusVegetationGenerator
and SpiralSpireGenerator next using the existing extractor. Their actual block
placement and eligibility checks are needed for non-registry provider coverage
and End interactions; no broader library tracing is justified by module names.

Zeta handlers are delivered in `1b650ca`. Exploratory class-reference search
located Quark consumer modules. Inspect ChorusVegetationModule and
SpiralSpiresModule registrations plus Zeta DeferredFeature's execution link
using the existing extractor. These are concrete consumer paths relevant to End
generation; module names alone do not establish applicability. Other Quark
consumers remain in broader provider coverage, and the exploratory search is
not accepted as an exhaustive consumer inventory.

Zeta modifier source is delivered in `3138b23`. It appends a deferred feature
per decoration stage and delegates spawning separately. Continue with its exact
WorldGenHandler and ZetaSpawnModifier dependencies through the existing extractor;
these resolve the concrete generation and natural-mob paths. Do not recapture
the modifier or generalize the extraction framework.

Trace Zeta's exact org/violetmoon/zetaimplforge/world/ZetaBiomeModifier class
with the existing extractor. Its retained JSON names a code-backed modifier
without feature targets, so this class directly addresses the effective-biome
gap. Add only the retained archive and exact class selection; no new extraction
framework or runtime measurement is needed.

Effective biome follow-up is now concrete in `bb42eb0`: retained Zeta and
Forgified Fabric biome-modifier documents delegate to code without declaring
feature targets. Their exact identities are in effective_biome_gap. Resolve
relevant implementations/callbacks before claiming packaged End feature lists
are final. Do not infer they change End content merely because they exist.
Thirty focused tests and scoped checks passed. Item 8 remains incomplete.

Platform caller attribution is integrated in `6032002`, source `ccc5c2f`.
EndPlatformFeature.place forwards level/origin/false to the static hooked method.
Frozen configuration selects the custom generator. Nominal bounds for the
packaged fixed origin are X=97..103, Y=35..56, Z=-3..3, including air. No saved
placement is inferred. Thirty focused tests and scoped checks passed. The caller
gap is closed; do not recapture it. Continue effective retained-stack feature
modifications and remaining attributes, then broader provider coverage.

Resolve the concrete platform caller gap with the exact vanilla
EndPlatformFeature class using the existing extractor. The class is in the
pinned mapped server archive and absent from the pinned patched server archive.
Add only this mapped-class exception without shifting the historic first-48
selection. This is necessary to bind the packaged feature to the captured static
hook; it does not introduce another measurement or validation framework.

Packaged End placed/configured feature rules are integrated in `7144dd8`.
Return gateways use motion-blocking height plus 3..9, supporting a source-derived
surface placement and discoverability description. Platform fixed origin
(100,49,0) lies outside the existing block projection; do not treat that bounded
projection as platform evidence. Thirty focused tests and scoped checks passed.
Next verify the vanilla platform feature caller-to-hook connection and effective
retained-stack feature modifications. Do not repeat packaged placement extraction.
Item 8 and full provider coverage remain open.

Packaged End biome entrypoints are preserved in `9025a02`. All catalog biome
references to end_platform, end_spike and end_gateway_return are linked to
registered biomes and captured End-only possible-biome membership. This is
packaged eligibility evidence, not complete effective runtime feature lists or
proof of every lifecycle caller. Thirty focused tests passed; scoped checks
passed after correcting test typing. Next reconcile effective feature/caller
applicability and remaining family attributes. No new measurement system was
added and Item 8 remains incomplete.

Direct encounter content is assigned to the three Better End Island families
in `02b5164`. Empty stored entity/spawner/loot-source lists bind to member
templates; arena code-created crystals and dragon are recorded separately.
Intended hostility is a source-derived design interpretation. Natural spawning,
external retained-stack effects and other lifecycle rewards remain unresolved.
Twenty-nine focused tests and scoped checks passed. Continue dimension/biome
applicability and remaining placement/discoverability attributes, using preserved
sources before adding any new extraction. Full provider coverage remains open.

Better End Island working families are grouped in `5f73e5a`: arrival platform,
gateway and dragon arena. The arena includes spike and podium components and
their lifecycle variants. The existing catalog test verifies every packaged
template is assigned exactly once. Twenty-nine focused tests and scoped checks
passed. Next complete applicable family attributes from existing evidence and
continue cross-provider coverage. Do not repeat completed source tracing or the
bounded End extraction. These groups are not a final accepted global count.

Central-End projection is delivered in `f295bec`, extractor `aff8997`, and
linked to decisions in `ca53b4b`. Reproduction matches exactly. Actual saved
materials are recorded, but section counts do not identify exact templates or
prove podium generation. Do not repeat the extraction or treat this bounded
observation as complete provider coverage. Settle Better End Island family
boundaries from the existing generation paths, retaining observation limits,
then continue outstanding provider coverage. Twenty-nine focused tests and
scoped builder checks passed. Item 8 remains incomplete.

World attribution gap confirmed: Item 7 provider disposition is indirect-only
for Better End Island, and decoded ChunkRecord omits block contents. Use a fixed
central-End projection from the existing restored ordinary run-a world. It reuses
Item 7 Anvil/NBT/packed readers, binds four regions to their delivered manifest,
and emits per-section actual block counts plus block-entity type/coordinates.
This limited offline extraction is necessary to inspect generated content not
represented by saved structure starts; no new server, survey framework or
archive is needed. Do not infer family identity from unused palette entries.

Runtime activation is integrated in `2299fd0`, using the existing downloaded
registry-r1 archive. Debug log records the relevant mixin applications, actual
NeoForge service selections, both mod containers and config loading. Captured
Better End Island config exactly matches frozen bytes. Runtime/source derivation
selects betterEnd=true, spike anchor Y=70 and loader radius 42. Exact member
hashes and log lines are in decisions; no new server run or archive was needed.
Twenty-nine focused tests and scoped builder checks passed. Inventory SHA-256:
`9de6189328999382fae37cc1a45888422112856ebdc20c152159ae11e4469d5c`.
Next reconcile generated-world observations and settle family records. Do not
repeat activation/source tracing. Item 8 and full provider coverage remain open.

Activation and respawn interpretation is integrated in `a7feb3f`. The source
chain connects NeoForge constructor, Common/config initialization and packaged
services. SUMMONING_PILLARS and END now carry direct spike/podium rebuild and
dragon-source attribution. WorldgenUtils surface selection is resolved as an
END_STONE scan. Twenty-nine focused tests and scoped builder checks passed.
Inventory SHA-256: `da8cecc81ca80eeb5cd3b8a894cf6547689881582205aa6b78e20d7bc6937a7e`.
Next reconcile preserved runtime loaded-mod evidence and generated-world
observations, then settle family records. Do not repeat completed source reads
or expand unused helper internals. Item 8 remains incomplete.

Activation/respawn source capture now reproduces exactly under
sources/better-end-island-activation (extractor fd83868). It preserves eight
classes and the two packaged service declarations; previous mixin metadata
entries are unchanged. NeoForge constructor calls Common.init then config init;
platform helper delegates to ModList.isLoaded. Respawn stage 5 calls the existing
portal helper and requests dragon creation; stage 3 invokes Feature.END_SPIKE.
Complete their scoped interpretation next, using these captures rather than
recapturing. Inventory remains at 1bb1b8e attribution; Item 8 is incomplete.

Resolve remaining direct Better End Island activation dependencies through the
existing extractor: respawn enum and stages 3/5 (spike/portal references), surface
origin helper, NeoForge entrypoint, Services and its two NeoForge implementations.
Preserve their exact META-INF service declarations in the existing metadata
capture so implementation presence is not mistaken for ServiceLoader selection.
These close variant invocation and frozen-config/runtime binding gaps; no new
measurement, schema or validator is introduced.

Podium invocation is integrated in `1bb1b8e`, source helper `48c6ceb`. Frozen
true/true tower settings select the custom podium in both dragon-history states.
Initial scan, missing-portal recovery, tracked-dragon death and reset now have
explicit variant dispositions and placement-success limitations. Twenty-nine
focused tests and scoped builder checks passed. Inventory SHA-256:
`e51be54e048cc8147e5d08d9eb6865368848913cc4e3a0b714399ff265d7987d`.
Next reconcile respawn-animation callers, initialization/runtime binding and
generated-world observations. ExitPortalUtils and EndDragonFightMixin invocation
interpretation are complete for their recorded scope; do not recapture them.
WorldgenUtils surface helper remains untraced if needed for origin applicability.
Item 8 remains incomplete; final families and full provider coverage remain open.

EndDragonFightMixin reset directly invokes the initial full podium when
spawnCentralTowerInitially is true. Initial state scanning, missing-portal
recovery and dragon death instead delegate to ExitPortalUtils.spawnPortal.
Capture that single exact helper with the existing extractor to resolve which
podium variants those calls select. This directly closes a configuration and
variant reachability gap; no new evidence framework or measurement is needed.

Better End Island template reconciliation is integrated in `e8982e8`, with
source dependency capture `46c2bf2`. All 41 packaged templates are linked
(36 spike pieces, three podium variants, platform and gateway), not counted
as families. Spike indices, crystal offsets and applicable block replacement
are resolved. Twenty-nine focused tests and scoped checks passed. Inventory
SHA-256: `fb8e1b31eca3bc8050d8103e0078ff949b12b14cc53daf8f3a0d3e63383b5c10`.
Next interpret the already captured EndDragonFightMixin podium invocation
and runtime/initialization applicability. Its reset method contains the direct
podium constructor call; other portal calls may identify an exact helper. Do
not repeat template extraction or completed processor/offset interpretation.
Item 8 remains incomplete; no new measurement system was added.

Resolve concrete spike/podium inventory gaps with the existing extractor: verbose
bootstrap constants for the two generators, SpikeCacheLoader for variant indices,
EndSpikeMixin for crystal offsets, BlockReplaceProcessor for generated contents,
EndDragonFightMixin for podium invocation, and BetterEndIslandCommon for the
betterEnd height switch. Existing nonverbose captures omit concatenated template
paths; the selected helpers are direct unresolved dependencies. This is the
smallest existing-path extension for those gaps, not a new measurement system.

Spike/podium generator interpretation is integrated in `8d11e68`. Direct
End Crystal requests, placement rules, variant selection and failure limits
are recorded. Twenty-eight focused tests and scoped checks passed. Inventory
SHA-256: `54b4dd382725ea6e48181b4e077feadcdc466c2b98d56221bb094ac4c2312579`.
Next resolve exact concatenated template names and reachable spike indices,
then podium invocation and the shared BlockReplaceProcessor. Reuse the existing
extractor; no new measurement system is needed. Do not repeat the completed
generator interpretation. Item 8 remains incomplete.

SpikeFeatureMixin and full BetterSpikeFeature/BetterEndPodiumFeature captures
now reproduce exactly under sources/better-end-island-spike-podium. Both spike
hooks replace vanilla behavior without a local config condition. The place hook
passes whether the accessor is a WorldGenRegion. Interpret the preserved full
generators next; do not recapture them. Podium invocation remains untraced.
Inventory is unchanged, and Item 8 remains incomplete.

Continue Better End Island provider coverage with SpikeFeatureMixin,
BetterSpikeFeature and BetterEndPodiumFeature. These three exact source classes
resolve untraced generation beyond the completed platform/gateway paths. Reuse
the existing extractor and processor captures; no new measurement system is
needed. Podium invocation and additional helpers may require subsequent tracing
only when these classes identify a concrete missing dependency.

Better End Island packaged mixin declarations are integrated in `68169a6`.
The previously ignored metadata artifact is durably retained by `e74e6b2`.
Twenty-eight focused tests and scoped checks passed. Inventory SHA-256:
`d59bdebe1e92f570af4eab73ad11fb60f01f5c4f57dbaebbbbaa524deb01c5c0`.
Proceed to spike/podium hooks and generators. The declaration establishes
packaged application intent, not direct runtime transformation. Item 8 remains
incomplete; no new runtime or measurement system was added.

Better End Island frozen configuration is integrated in `c1169fa`, with all
six keys mapped to runtime fields. Both vanilla platform/gateway switches are
false. Twenty-seven focused tests and scoped checks passed. Inventory SHA-256:
`82b5d02452470cde6a3036624979863f2485827c9e679d703698101354618c5b`.
Continue mixin activation and spike/podium generation coverage. Do not repeat
configuration binding work. Item 8 remains incomplete.

The three Better End Island configuration classes are now captured and
reproduced exactly. ConfigModuleNeoForge registers the frozen COMMON filename
and bakeConfig maps its values to the fields read by the hooks. Both vanilla
platform/gateway toggles are false in the frozen file and constructor defaults.
Integrate this binding from sources/better-end-island-configuration, then resolve
mixin activation and spike/podium paths. Inventory remains at `69d3e14`; do not
repeat configuration extraction. Item 8 remains incomplete.

Bind the frozen Better End Island TOML to its runtime fields through the exact
BEIConfigNeoForge, ConfigModule and ConfigModuleNeoForge classes. The platform
and gateway hooks already identify the controlling fields. Reuse the existing
extractor for these three classes; this resolves a configuration evidence gap
without a new runtime or measurement system.

Better End Island processor effects are resolved in `69d3e14`, source capture
`763bd43`. DragonEggProcessor preserves existing eggs; ObsidianProcessor varies
obsidian with the clamped dragon-kill count. Twenty-six focused tests and scoped
checks passed. Inventory SHA-256:
`1b1b7b3e61f6b86c2d0e0ed7f32e01ce420d6700702872b18025bdad0015fd5f`.
Next resolve frozen configuration binding/mixin activation and spike/podium
paths. Do not recapture or reinterpret the two completed processors. Item 8
remains incomplete; prior registry and feature family records are unchanged.

Resolve Better End Island platform/gateway processed contents by capturing the
two directly invoked processors, ObsidianProcessor and DragonEggProcessor, with
the existing exact-class extractor. Template entities alone cannot establish
their block/reward effects. No new measurement system or generalized tooling is
needed for this explicit content gap.

Better End Island platform/gateway generator attribution is delivered in
`189240a`. The third non-registry contribution records two template links,
envelopes, placement offsets, processor order and failure limits. Twenty-five
focused tests and scoped checks passed. Inventory SHA-256:
`8e571bbcf2a382dd9d0a82735de2dc3e43296e8f4aaa8c4490ddfd00a7468111`.
Next inspect ObsidianProcessor/DragonEggProcessor and frozen configuration
binding, then spike/podium paths. Do not repeat platform/gateway generator reads.
Prior family records are unchanged. Item 8 remains incomplete.

Full-provider reconciliation resumes with YUNG Better End Island. Its packaged
JSON catalog has only two block-tag resources, while the retained JAR contains
custom platform, gateway, spike and podium code. Trace the platform/gateway
mixins and corresponding generators using four exact classes in the existing
extractor. Registry-only coverage cannot resolve these generation paths. This is
a required provider gap, not a new measurement system. Keep prior YUNG family
work intact; do not recapture the completed Extras/Bridges classes.

Feature-family content attribution is delivered in `532fb28`. Extras members
now link template entities/block entities/chest loot; wells separately record
processor archaeology loot. Bridges carries its scoped direct encounter findings.
Twenty-four focused tests and scoped checks passed. Inventory SHA-256:
`d064a47129cf9b538ca11a9f8398bcbe33f8113f7246cec26d0d14025afd03d4`.
Continue effective content, hostility/discoverability and full provider coverage.
Item 8 remains incomplete. No new measurements or source captures were added.

Feature-family biome and dimension scope is delivered in `4b1e33a`. Each
family now links its resolved addition-modifier biomes and captured dimension
overlap. Only overworld overlaps; this does not claim observed generation.
Twenty-three focused tests and scoped checks passed. Inventory SHA-256:
`759e4b2149d0fb7e2b33b8a06d9152a7c90983035761979c7e50f936379fc6dc`.
Continue content/hostility/discoverability attribution and full provider coverage.
Registry and feature family memberships are unchanged. Item 8 remains incomplete.

The eleven YUNG feature families now have member-bound template lists and XYZ
envelopes, delivered in `62b6af5`. Bridge/swamp support extensions and buried
well placement remain explicit limitations. Twenty-two focused tests and scoped
checks passed. Inventory SHA-256:
`b45003452d05e67634dce0128ffda651384b12957c5eb40ea8dcf2d6519d47e6`.
Registry groups and family membership are unchanged. Continue dimension/biome
and content attribution for these families, and full retained-provider coverage.
Item 8 remains incomplete; no new measurement system was added.

Feature-family reconciliation in `0a17e78` assigns Extras 62 configured variants
to ten working families and Bridges 22 variants to one. Single/double swamp arches
are one family; bridge material/damage/length/axis remain variants. Twenty-one
focused tests and scoped quality checks passed. Registry rows remain 421 groups
and 887 roots; no final pack-wide family count is claimed. Inventory SHA-256:
`a582e44e1a23ee2f7701616bc1264346112745aa805bcf131232d74df0a1a585`.
Continue full provider coverage and remaining family attributes. These feature
family records retain their separate generation path; do not count selector or
unlinked packaged templates as families. Item 8 remains incomplete.

Both YUNG initialization findings are integrated in `f569bde`; the generated
inventory now links all corresponding source captures. Twenty focused tests and
scoped checks passed. Inventory SHA-256:
`c6d84d64ce8570bbe4e3a388a9d1a8a0997e29e88474233088b5ca4a75e0a4a7`.
Extras scope now reflects completed template links and direct generator rules.
Continue provider coverage and canonical family reconciliation; do not repeat
empty module-loader inspection. Item 8 remains incomplete with 421 provisional
registry groups and 887 roots. No new measurement system was added.

Initialization captures in `3ff1893` show Extras/Bridges NeoForge loaders
delegate to IModulesLoader.loadModules. The newly preserved default methods
contain only return. This branch does not register configuration controls; do
not repeat these captures. Auto-registration/data and wider provider coverage
still need reconciliation. Inventory remains at `7343614` with SHA-256
`878db7626144c928e32a1b5a6eeef52fa8cc934d3ed1a2d8dfed2ec2bcfaa318`.
No new runtime or measurement system was added. Item 8 remains incomplete.

No Extras/Bridges-named path was found in the frozen configuration tree, but
this is not an absence-of-controls conclusion. Resolve the initialization path
using four exact classes with the existing extractor: Extras common/NeoForge
entrypoints and both NeoForgeModulesLoader implementations. Existing Bridges
entrypoints delegate to the module loader and are already captured. This is a
specific configuration attribution gap; no new measurement system is needed.

Extras remaining desert terrain and empty custom processor paths are resolved
in `d06f076`: chillzone, giant torch, small ruins and obelisk. Nineteen focused
tests and scoped checks passed. Inventory SHA-256:
`878db7626144c928e32a1b5a6eeef52fa8cc934d3ed1a2d8dfed2ec2bcfaa318`.
Do not repeat these direct generator reads. Continue configuration/provider
coverage, canonical family reconciliation and required effective attributes.
The 421 provisional registry groups and 887 roots are unchanged. Item 8 remains
incomplete. No runtime or new measurement system was added.

Extras swamp placement and appearance rules are delivered in `5f52351`. All
six feature types now have terrain-check offsets, processor binding, support
column limits and masonry/candle effects recorded. These cover 46 configured
feature variants, not 46 families. Nineteen focused tests and scoped quality
checks passed. Inventory SHA-256:
`a88bb2864dbbbf4af04006deece95a825a7ed41f905156f9d1b96bbacbbb371d`.
Continue remaining desert effects, configuration/provider coverage and canonical
family reconciliation. Swamp template height must not be used as full support
height. No new capture or measurement system was added. Item 8 remains incomplete.

Extras well archaeology and placement rules are delivered in `b8c4a7e`, with
processor constructor evidence in `0389282`. The regenerated inventory SHA-256 is
`8c5c53f1135cbaa6c038d1e89260c15a4fbba58ccc4bf0ad3ed0fb575300ce86`. Eighteen affected tests and scoped checks passed.
Both marker loot paths, conditional brushable assignment and the six-block-deep
template anchor are recorded. Registry membership remains 421 provisional groups
and 887 roots. Continue swamp/other generator effects, configuration/provider
coverage and canonical-family reconciliation. Do not recapture the processor
module or repeat well interpretation. Item 8 remains incomplete.

The twelve-class Extras capture is delivered in `4303da0`. DesertWellProcessor
adds suspicious-sand loot absent from stored template block entities. The
generator references FeatureProcessorModule.DESERT_WELL_PROCESSOR, so capture
that exact module with the existing extractor to verify the constructor binding
before attributing processor effects to generated wells. This resolves a specific
loot-source gap without a new measurement system. Swamp processor interpretation
also shows support columns can extend below the template envelope; integration
remains pending.

The remaining Extras generator capture selects twelve exact classes: the nine
uncaptured desert/swamp generator or base classes and three processor/interface
classes. These implement the remaining eight configured feature types. Existing
template records cannot reveal their custom effects. Reuse the existing extractor
and preserve this source increment; no new framework or runtime is needed.


Extras code-linked envelopes are delivered in `bb970de`: chillzone 3x4x4,
giant_torch 4x7x4 and ruins_0 4x5x4. All 62 packaged template envelopes now have
verified linked records, without claiming occupied world sizes or family counts.
Seventeen affected tests and scoped checks passed. Inventory SHA-256:
`c7fa2fed220886d952ea872056cd9fcf0899719e431b70923fc21be72b4835ea`.
All 421 registry family rows and 887 roots remain unchanged. Continue effective
content/terrain, family and configuration/provider reconciliation. Item 8 remains
incomplete. No new extraction or measurement system added.


Extras code-based links are delivered in `4bb656f`. Registration annotations,
constructor bindings, configured type fields and template calls resolve the
three previously open links. All 62 packaged templates now have a traced feature
link (59 JSON-explicit, three code-based), not 62 accepted families. Seventeen
affected tests and scoped quality checks passed. Inventory SHA-256:
`6354d013331c716f3091e87ce3b49fa03a766471a7a8cd2167bfc0bf0c50e5d9`.
All 421 registry family rows and 887 roots remain unchanged. Do not repeat the
registration capture. Continue terrain/content, family reconciliation and
configuration/provider coverage. Item 8 remains incomplete.


Extras FeatureModule now requires verbose javap output: the initial capture
omitted field annotations, leaving exact feature-ID binding unproven. Enable
verbose output for that exact existing class and preserve a separate capture;
keep the prior raw capture intact. No generalized extraction option is needed.


Extras desert class-to-template calls are delivered in `0f8e610`. The three
classes pass fixed IDs through centered placement, with above-ground anchors
for chillzone/torch and the ground anchor for ruins. Placement success is
discarded by the shared helper. Sixteen affected tests and scoped checks passed.
Inventory SHA-256:
`55fd39f5efd49aee91e1a922eacc763291a09dc9892ba4175c1802bd741eeb0d`.
All 421 registry family rows and 887 roots remain unchanged. The non-verbose
FeatureModule capture lacks registration annotations: preserve a verbose capture
of that exact class to finish feature-ID binding. Remaining terrain/content and
configuration work remains open. Item 8 is incomplete; no new measurement added.


The next Extras source capture selects five exact classes using the existing
extractor: feature registration, AbstractNbtFeature and the three empty-config
desert generators. JSON cannot establish their template links or custom effects.
This is the smallest source increment needed to resolve those demonstrated gaps;
no new evidence class, schema, validator or runtime is introduced.


Extras packaged contents are delivered in `bae0ae4`: 62 empty entity lists,
three chests across chillzone/ruins_0 and eight campfires across giant_torch/
swamp_pillar_2. Both chest loot resources resolve. There are no stored spawner
block entities; custom generator effects are not yet resolved. Fifteen affected
tests and scoped quality checks passed. Inventory SHA-256:
`c27dbad3867324ff9110ef5f0dfe04a5e6b3dfd4867e8af9205cb9b3c431ff3a`.
All 421 registry family rows and 887 roots remain unchanged. Next inspect Extras
custom generators, especially the three empty-config desert features, and
configuration registration. Item 8 remains incomplete. No new extraction or
measurement system was added.


Extras explicit template membership is delivered in `2957779`. All 59 explicit
location references resolve, with nominal XYZ sizes recorded. Three empty-config
generators (desert_chillzone, desert_giant_torch, desert_ruins_0) require code
attribution; similarly named packaged templates are not assumed linked or unused.
Fourteen affected tests and scoped quality checks passed after one assertion wrap.
Inventory SHA-256:
`f66b81d0def7ecf9de36eb82f036ef646ed9b343930b92f8f030a9546ab1c060`.
All 421 registry family rows and 887 roots remain unchanged. Continue Extras
custom-generator/content attribution and configuration registration. Four
packaged templates have block entities (chillzone, giant_torch, ruins_0 and
swamp_pillar_2); their effective content is not yet attributed. Item 8 remains
incomplete; no new extraction or measurement system added.


Extras biome scope is delivered in `397812a`. Desert additions and declared
vanilla well removal share three resolved desert biomes; swamp additions have
two. All intersect only the captured overworld list, with no required missing
tag members. This is packaged scope, not observed generation/removal. Thirteen
affected tests and scoped quality checks passed. Inventory SHA-256:
`7a1110e2734dd4f04a4084ed2ffbe9aa3be0a6af9fc61ffd5518ff40c831aba0`.
All 421 registry family rows and 887 roots remain unchanged. Continue Extras
template/custom-generator attribution and effective configuration registration;
bridge configuration and wider provider coverage remain open. Item 8 remains
incomplete, with no new capture or measurement system added.


YUNG Extras entry points are delivered in `fe1fb1e`. Two NeoForge additions
reference 16 desert and 46 swamp placed features, matching all 62 same-ID
configured/placed runtime entries. There are zero yungsextras structure roots.
The third modifier declares vanilla desert-well removal. Neither 62 features
nor 11 generator types are accepted family counts. Twelve affected tests and
scoped quality checks passed. Inventory SHA-256:
`9fcd6b648bd22c311a0d9f167c0013cb500e3817ed6c06406666e0dc719cadac`.
All 421 registry family rows and 887 roots remain unchanged. Continue Extras
template/custom-generator attribution and configuration/biome scope. Bridge
standalone configuration and wider provider coverage also remain open. Item 8
is incomplete; no new capture or measurement system was added.


Bridge biome/modifier constraints are delivered in `c19f9d5`. Existing merged
tags resolve six registered river biomes with no required missing members;
only the captured overworld possible-biome list overlaps. All 22 variants
have terrain, chance=3 rarity and RNG initialization in that order. This is
not observed generation frequency. Eleven affected tests and scoped quality
checks passed. Inventory SHA-256:
`f2497cb9bd2118ce0e1910cd2a203d9d51ea21d83636cb7f3addf2601b3c2a97`.
All 421 registry family rows and 887 roots remain unchanged. Next reconcile
standalone bridge configuration registration and remaining provider coverage.
Item 8 remains incomplete; no new capture or measurement system was added.


Bridge terrain placement is delivered in `e8503b5`. The source now binds bank
height/occlusion/count checks, the liquid span rectangle and first-candidate
search. The liquid predicate is not water-specific. It supports surface-crossing
intent, not observed visibility or frequency. Eleven affected tests and scoped
Ruff/Basedpyright passed. Inventory SHA-256:
`71f820a7edd7337111c7e8b8a031e0ef11a99babdea3152b440f7a3ccd459ed5`.
All 421 registry family rows and 887 roots remain unchanged. Next reconcile
bridge configuration/biome controls and other provider coverage. Item 8 remains
incomplete; no new source capture, runtime or measurement system was added.


Direct bridge encounter and loot attribution is delivered in `544d5de`.
The fourteen captured processor/module/interface classes have no direct entity,
spawner or container-loot calls; existing templates have empty entity/block-entity
lists. This resolves direct contribution only, not natural mobs, delegated
behavior or external retained-mod effects. Ten affected tests and scoped Ruff
and Basedpyright passed. Inventory SHA-256:
`53d49ef90e2b842f8b6321ef74b8fbc1e06537de934201b149c9e00533e0f08e`.
All 421 registry family rows and 887 roots remain unchanged. Next finish bridge
placement/configuration and other provider coverage. Item 8 remains incomplete;
no new capture or measurement system was added.


Bridge support geometry is delivered in `733c0cf`. Captured code places the
marker then descends through air/liquid at fixed X/Z while Y > 0. Template
height is the body envelope, not the terrain-dependent total support height.
Block-write success is not checked by this helper. Nine affected tests passed;
scoped Ruff and Basedpyright pass after splitting one compound assertion.
Inventory SHA-256:
`5410d6d5ae2e6e5ad584dece89db3396c70c561056de5d9e47545c97fcd3a9e7`.
All 421 registry family rows and 887 roots remain unchanged. Continue other
bridge processor effects, placement/configuration and provider coverage. Item 8
is incomplete. No new runtime, source capture or measurement system added.


Bridge generation ordering and success limits are delivered in `955936c`.
The contribution now binds sea-level anchoring, axis rotation and the twelve
post-template processors. The discarded template-placement boolean means feature
success is not proof that every block was placed. Scoped Ruff and Basedpyright
pass; the existing eight affected tests passed before the formatting-only wrap.
Inventory SHA-256:
`05295953bfbab2da42d0ef9f9feac58a4013ab14313718f59c9151fb192e1966`.
All 421 registry family rows and 887 roots remain unchanged. Continue bridge
processor effects and configuration/placement questions, then other provider
gaps. No new measurement system or runtime was added. Item 8 remains incomplete.


YUNG bridge template membership is delivered in `01edbb8`. Eleven referenced
layouts now have nominal XYZ sizes; three packaged wood layouts (13_0,
13_0_broken, 15_0) are explicitly unreferenced by the verified selector. All
fourteen templates have empty entity/block-entity lists, which do not establish
effective generated contents before custom marker/processor handling is checked.
Seven affected tests passed; scoped checks pass after two test line wraps.
Inventory SHA-256:
`38eb038f5c04562162292988e8d55c407ea6f78cc489cdac8a0c5db9f69d3938`.
All 421 registry family rows / 887 roots remain unchanged. Next inspect bridge
custom generation/marker handling and configuration controls; no bridge-named
frozen config was found, which is not proof that controls are absent. Continue
other non-registry/provider gaps afterward. Item 8 remains incomplete. No new
runtime, extraction or measurement system was added.


YUNG's Bridges feature contribution is delivered in `6309287`. The existing
non_registry_content field now holds verified contributions from the same pinned
decision file. This minimal extension is necessary because structure-only groups
cannot represent feature-based bridges with no structure IDs; no new schema,
framework or measurement system was added. Runtime feature dumps and packaged
NeoForge modifier/selector bind 22 configured variants to 11 template IDs. These
are not separate accepted families. All 77 affected tests passed; bridge and
scoped checks passed after test-only typing/import fixes. Inventory SHA-256:
`da35ac84a7e3c198fc648088f7001b8cfad29ab311f6e3bf16d84738e0176c97`.
All 421 structure-registry groups / 887 roots are unchanged. Next reconcile
YUNG bridge configuration, template content and custom placement, plus other
non-registry providers (YUNG Extras and End Island are concrete follow-ups).
Canonical/provider coverage and remaining attributes still prevent Item 8 closure.
Do not repeat delivered lake/mountain source work. No runtime added.


Lake direct encounter/loot attribution is delivered in `a4548bf`, using helper
capture `28ed678`. Eleven captured classes show no direct authored entity,
explicit spawner configuration or container-loot assignment. BlockFixer adjusts
vegetation/crystals/fluids and schedules fluid ticks. The five content fields
explicitly preserve unresolved dynamic material-provider and external effects;
this is not proof of zero effective spawners or mobs. All 75 affected tests and
scoped checks passed. Inventory SHA-256:
`65d6dd6270f40edae66a5401a4e3aafe3f3aba5d4adccf9f6703b0dd00c8958f`.
Only lake direct-content fields and grouping evidence changed. Still 421 working
groups / 887 roots. Continue material/provider coverage and remaining canonical
families/attributes. Do not repeat unchanged lake/mountain source captures or
checks. Item 8 remains incomplete; no runtime or measurement system added.


Lake placement and visual shore cues are delivered in `8292695`. All five roots
preserve the base precheck and their distinct center/neighbor conditions. The
two piece algorithms retain different shore/dust/plant cues; actual visibility
is unmeasured. All 74 affected tests and scoped checks passed. Inventory SHA-256:
`25e78dd6bbe34e3ac2c6ee60c1bda55119ae79772c2f69c6c32fc29270a48247`.
Only lake placement/cues and grouping evidence changed; still 421 working groups
and 887 roots. Continue remaining direct lake content, provider/canonical coverage
and required attributes. The narrative report now labels its obsolete zero-mod
completion claims as historical and links to the current incomplete inventory. Item 8 is incomplete;
no new runtime, measurement system or downstream work was added.


Mountain base placement precheck is integrated in `b52dfa9`. The independent
FeatureBaseStructure Y >= 10 check precedes the root-specific Y > 5 / Y > 50
checks. Both sampling stages remain explicit. All 73 affected tests and scoped
checks passed. Inventory SHA-256:
`e7c1a4fefa8ba492c93cef684994c60509cf8849a44934500d6563d7413fee80`.
Only mountain placement and its grouping decision changed. Still 421 working
groups / 887 roots. Continue lake/custom content and canonical/provider coverage;
Item 8 remains incomplete. LakePiece inspection shows biome top-material lookup
via EndBiome.findTopMaterial and direct jungle-grass/umbrella-moss rim placement;
these are leads for the remaining lake attribution, not accepted full contents.
No new measurement system, runtime or downstream work was added.


BetterEnd mountain direct encounter/loot attribution is delivered in `1ee796e`.
The seven preserved generator/base/piece classes contain no direct authored mob,
spawner or container-loot path; both definitions have empty spawn overrides.
Five content/intent fields now record this scoped attribution. Natural spawning,
block drops and external injections remain distinct, not disproven. All 73
affected tests and scoped checks passed. Inventory SHA-256:
`24e6dfa796602032aedb3e97642453fa92b9ceeace619f70df51797a4b3383aa`.
Only mountain content fields and their grouping decision changed; still 421
working groups and 887 roots. Next integrate the inspected FeatureBaseStructure
precheck (sampled Y >= 10) alongside the separately sampled root thresholds,
then continue lake/custom content and provider/canonical coverage. The existing
README records the precheck finding and exact reproduction. Item 8 is incomplete;
no new runtime, measurement system or downstream work was added.


BetterEnd mountain placement and visual cues are delivered in `a485c80`, using
piece source capture `01d4f63`. Both variants now record surface height selection,
distinct minimum Y thresholds and source-derived crystal/layered-stone cues.
Observed visibility remains unmeasured. MountainPiece uses radius for its Y
bounding box; saved envelopes are not occupied height. Existing size evidence
and all other family rows are unchanged. The affected suite passed 71 tests;
after separating the new test to satisfy lint, four BetterEnd cases and scoped
Ruff/Basedpyright passed. Inventory SHA-256:
`175fd05691be098c8e5904482325772757cdf9185a5017b3d765429e920f67ea`.
Still 421 working groups and 887 roots. Continue required content attribution,
remaining canonical/provider coverage and attributes. Item 8 remains incomplete;
no new runtime, measurement system or downstream work was added.


BetterEnd mountain grouping is delivered in `8ca1e21`. Ordinary and painted
mountains are variants of one formation family. Separate generator/piece types,
biome restrictions, height thresholds and material paths remain preserved in
source evidence. All 71 affected tests passed; after an assertion line wrap,
three focused BetterEnd cases and scoped checks pass. Working total: 421 groups
with 887 registered roots. Inventory SHA-256:
`d04abd3d02744ce7af0ac2ae286642ceaedca036efa603a9db08122b78280072`.
Reproduction and limitations are in the final BetterEnd section of
`evidence/item-8/README.md`. Lake/mountain grouping questions are resolved, but
piece contents, actual geometry and other required attributes remain open.
Continue provider/canonical coverage and attribute completion. No new extraction,
measurement system, runtime or downstream work was added. Item 8 is incomplete.


BetterEnd lake grouping is delivered in `f90d6da`. Five registered lake types
are variants of one lake-formation family. Normal/rare EndLake classes share
base generation; megalake/small-megalake use LakePiece with distinct parameters.
Both algorithms, all definitions, biome constraints and original observation
links are retained. Piece content and effective attributes remain open, as do
mountain relationships. All 70 affected tests and scoped checks pass. Current
working total: 422 groups with 887 registered roots. Inventory SHA-256:
`620b2c61a0890bd4e2e387c4dd4f6e907682c653f752a8835a728eea6133ec2a`.
Reproduction is in the final BetterEnd section of `evidence/item-8/README.md`.
Continue remaining canonical/provider reconciliation and required attributes.
Item 8 is incomplete; no runtime, measurement framework or downstream work added.


BetterEnd lake/mountain registration and generator sources are captured under
`evidence/item-8/sources/betterend-formations-code`. The existing extractor now
selects nine exact classes from retained BetterEnd, including verbose registration
bootstrap bindings. Identity manifest SHA-256:
`150df9fc0a941cc523bca51a782c39fcd0f08a32b11af77a64cf6f248c170961`.
Initial source inspection: normal/rare EndLake subclasses only forward construction
and override type(); MegaLakeSmall has its own generatePieces. Mountain and
painted mountain use separate piece classes. Integrate relationships only after
comparing these preserved implementations and settings. No new measurement system
was added: packaged definitions do not expose the code needed for these open
family decisions, so the existing source extraction path supplies it. Extraction
and scoped checks pass. Inventory and its 426 working groups remain unchanged.
Commands and limitations are in the source directory README.


MVS mining relationship and encounter attribution are delivered in `7c1d6c6`.
Compact mine-with-campsite and modular mineshaft remain separate families;
shared villager pieces are components. Both now record packaged hostile intent
and authored/template/spawner versus natural-source distinctions. The compact
site has skeleton spawner content; the network has bogged/creeper/skeleton
spawner sources plus authored bogged/evoker/skeleton entities. No live population
is claimed. All 69 affected tests and scoped checks pass. Count remains 426.
Inventory SHA-256:
`bf56126ef196c73126ab1da8880b4027c5f8c98b3b2e6331df5ebbc47a182e31`.
Commands and limitations are in the final MVS section of `evidence/item-8/README.md`.
The explicit MVS rock/pond/camp/island/mining relationship questions are resolved;
other design reconciliation, BetterEnd, non-registry coverage and required
attributes still need completion. No new measurements, tuning or downstream work.


MVS floating-island grouping is delivered in `18ecfe4`. Two roots form one
family with distinct loot and habitation variants; the large-house layout
retains three shared villager components. Definitions differ only by start pool,
with surface-heightmap offset 60, size 1 and no terrain adaptation. All five
reachable templates and original evidence links are retained. Working total:
426 groups with 887 registered roots. All 68 affected tests and scoped checks pass.
Inventory SHA-256:
`87667133ab2560dfa6120872a0023dcf761217e2f81080a631925808fa9d6a34`.
Reproduction and limitations are in the final MVS section of
`evidence/item-8/README.md`. Continue MVS mining/design reconciliation, BetterEnd,
non-registry provider coverage and outstanding attributes. Item 8 is not complete.
No runtime experiment, new measurement system or downstream work was added.


MVS surface campsite grouping is delivered in `aa01ac1`. Campsite, fire camp
and horse campsite are one family with all three exact definitions/templates
preserved. Mine with campsite remains separate due to its lower spawner-bearing
mining component and shared villager pieces. The modular mineshaft relationship
is still open. Working total: 427 groups with 887 registered roots.
All 67 affected tests and scoped checks pass. Inventory SHA-256:
`d38983b380fedb771dbe47aefb274e287a9dfa355e37d4b9a617babac68df33e`.
Reproduction and limitations are in the final MVS section of
`evidence/item-8/README.md`. Continue unresolved MVS island/mining relationships,
BetterEnd, non-registry coverage and required attributes. Item 8 remains active;
no configuration changes, new measurement system or downstream work.


MVS rock/pond grouping decisions are delivered in `bdcee2c`. Boulder and
stone-rock roots become one rock family; mushroom and oak pond roots become
one pond family. Exact definitions, seven rock template alternatives, four pond
components and distinct pond loot references are preserved. Working total is
429 groups with 887 registered roots. All 66 affected tests passed; after an
annotation-only fix the two affected cases and scoped checks also pass.
Inventory SHA-256:
`151e5afe848e375cfdc7ef42887ec8e43c311250a45882a52645362de1c2e9ed`.
Reproduction is in the final MVS section of `evidence/item-8/README.md`.
Remaining MVS camps/island relationships, BetterEnd, provider coverage and
required attributes are still open. Item 8 remains incomplete; no tuning or
downstream work. No additional measurement system was introduced.


CTOV canonical village reconciliation is delivered in `5bb0942`. One civilian
village family now contains 22 named architectural/placement designs and all 66
size/design roots; hostile outposts remain separate. Exact definitions, missing
references, tavern links, biome/loot coverage and observed-start indexes remain
preserved. This supersedes CTOV broader grouping being open in older checkpoints.
Working total: 431 groups, still 887 registry roots, not final Item 8 acceptance.
All 67 affected tests and scoped checks pass. Inventory SHA-256:
`21481771b21790e45a616efbef2d7b958fe719302b4bcf4e0dc8683e749760e5`.
Decision SHA-256:
`4d545b2a01ea7d142a4fbd15f7917a836559a6fd48634c04526c44aefedf6483`.
Commands and rationale are in the final CTOV section of `evidence/item-8/README.md`.
Continue remaining family reconciliation (including MVS/BetterEnd), non-registry
provider coverage and outstanding attributes. No downstream work or tuning.


CTOV content/start-placement attributes are delivered in `f937ea9`.
The 23 current CTOV groups now record authored entity IDs, hostile versus
natural-override sources, resolved-template spawner absence and heightmap start
intent. Villages have empty spawn overrides; outposts have authored ravagers
and four separate natural-override monster types. Underground village starts
use a -14 surface-relative offset, not the zero offset of the other designs.
Missing components and runtime transformations remain limitations. All 64
affected tests and scoped checks passed. Inventory SHA-256:
`f51b1333d6e322ab60f9f7f051958ce683a482bf9c553faafa02efd24d2b7e97`.
See the final CTOV section of `evidence/item-8/README.md` for reproduction.
Item 8 remains incomplete; continue canonical grouping, non-registry coverage
and remaining attributes. No new runtime, measurement framework or tuning.


CTOV village definitions and missing-component bindings are delivered in
`21fdbe0`. All 66 village roots across 22 working design groups are now bound
to exact packaged definitions and existing pool traces. Existing outpost checks
cover the other 12 CTOV roots. All 63 affected tests and scoped checks pass.
Inventory SHA-256:
`9205723b5e8748e56aeac40190d15365aa2b198a98c79e81ecb37409a0c5112e`.
Reproduction commands and limitations are in the final CTOV section of
`evidence/item-8/README.md`. Canonical relationships between village designs,
non-registry provider coverage and outstanding required attributes remain open.
No family count, configuration, runtime or measurement-system change.


Integrated Villages/IDAS suppression sources are delivered in `9d88842`, with
family integration in `feb9da7`. Integrated Villages suppresses seven exact keys:
the five vanilla villages and both Terralith fortified villages. It does not
suppress the jigsaw type generally. IDAS adds a desert-pyramid suppression hook;
its three Ice and Fire targets are absent from the runtime structure registry.
All 72 affected tests and scoped checks pass. Inventory SHA:
`98ac8b670b5383ae61c62c4cde95c31959d822dcc13701de5ca1df59edbfc144`.
Decision SHA: `0eeb35394a6ac67eb052b79c5045d79c9e11b55c8eb827910a9f857460de7dd5`.
Commands, exact scope and source identities are in
`evidence/item-8/sources/integrated-suppression.md`. The pending hook checks below
are superseded. Preserve tavern/Better Village potential component relationships
without treating suppressed vanilla villages as normal generated encounters.
No configuration, runtime or measurement framework changed. Continue remaining
provider/family coverage and required attributes, avoiding inactive-generator
detail. Item 8 remains incomplete, including final review and verified main merge.

Six additional vanilla normal-generation dispositions are resolved in `f1f4649`,
using suppression sources delivered in `40922f3`: desert pyramid, jungle pyramid,
fortress, ocean monument, stronghold and swamp hut. Five frozen settings enable
their cancellation hooks; the stronghold hook is unconditional after type match.
All 69 affected tests and scoped checks pass. Inventory SHA:
`385100c3e7f984662e7e9eaad598d4b858553a13c5965caabb29f764b2d61816`.
Decision SHA: `216306ee257892d8bb21d0b25a9b0ce797dbaa1fa00c9f6b6a449168783a7167`.
Exact source selections, checks and boundaries are recorded in
`evidence/item-8/sources/yung-suppression.md`. Do not dissect these inactive vanilla
generators further merely to fill descriptions. Keep registry presence, compatible
biomes and existing vanilla source descriptions separate from active generation.
Next verify Integrated Villages' Disable Vanilla Villages=true hook and IDAS's
Disable Vanilla Desert Pyramid=true hook. Their frozen labels were inspected,
but cancellation behavior has not yet been bound. Continue other provider and
attribute gaps afterward. No new runtime measurement system was added. Item 8
remains incomplete, including final Codex review and verified main merge.

Village Taverns parent attribution is delivered in `1e7dd7c`. The existing
family records now link 25 reachable tavern templates to 66 registry roots in
22 working groups, including IDAS castle. Twenty-six conditioned modifiers are
included in the preserved trace; the CTOV dark-forest tavern has no traced parent
despite its registered target pool. Do not treat that case as a missing pool or
count components as new families. All 63 affected tests and scoped checks pass.
Inventory SHA: `e0fddbb286ce87c8a23285d7af33eac42563db754f8ad833d1826080d4c50327`.
Decision SHA: `f74b70a63144b337d3483dba03e50a3193bcf82b06eeeb1112d3f6898e7c3236`.
Commands and scope are in the final Village Taverns section of
`evidence/item-8/README.md`. This reuses existing catalog/trace evidence and the
builder; no new measurement system or general relationship framework was added.
Continue remaining provider coverage and family attributes. CTOV's final family
relationships, other non-registry content and effective generation remain open.
Item 8 is incomplete, with final review and main merge still pending.

Vanilla mineshaft normal-generation suppression is explicit for both registered
roots in `9e8f032`. Existing configuration, binding code and required mixin
metadata support the disposition; no vanilla piece extraction or new server
measurement was needed. All 62 affected tests and scoped checks pass. Inventory:
`3ac3368b6de3d939f9ac78d117eb0397bbe0c2092967b72e71b6d2b4223d13f3`.
Decision SHA: `303874189f6806bc565d51e5cc234c2b57279cc7c621b161646de5c098400c23`.
Commands are in `evidence/item-8/sources/mineshafts-code/README.md`.
Keep registered IDs and biome compatibility despite suppression; command placement
and pre-existing worlds are outside the normal-generation claim. Prior vanilla
mineshaft dissection instructions are superseded. Prioritize remaining provider
coverage and required attributes; inspect deeper code only for a concrete unresolved
field. The user requested clearer progress explanations and avoidance of excessive
generator detail. Item 8 remains incomplete and its review/main-merge gate is open.

Jungle temple source is delivered in `8397ebc`, and nine-attribute integration
in `b4c5e6f`. The jungle_pyramid registry root and jungle_temple generator type
remain one family. Both chest and dispenser loot paths are recorded, with saved
flags storing helper results. Nominal dimensions are 12 by 15 and height 10;
the explicit Y -4 foundation lies below that nominal height. No full generated
height or actual visibility is claimed. All 62 affected tests and scoped checks
pass after correcting the focused test's constructor selector. Inventory SHA:
`055f6b523673db40380f2b670e920c1b6320c45c03e611fb29168e89700b9285`.
Decision SHA: `3650c5d8f0406b623cf85007f2c5f1351f18eeaea634f8a25a13107ce22d10e7`.
Commands and the test failure disposition are under
`evidence/item-8/sources/vanilla-jungle-temple-code/README.md`.
No new measurement system was added. Continue the remaining custom generators
(vanilla fortress, mineshafts, monument, mansion and stronghold among them),
provider/family reconciliation and effective retained-mod gaps. Do not repeat
the delivered jungle temple or desert pyramid source extractions. Item 8 remains
incomplete, including its final review and main-merge gate.

Desert pyramid content integration is delivered in `f9fe8a1`. Seven attributes
now distinguish the TNT trap, chest-result flags, archaeology selection/clipping,
vanilla entity/spawner absence, authored form and mixed surface/underground
placement. All 63 affected tests and scoped checks pass. Existing geometry
fields remain UNKNOWN because there is no retained full-start envelope observation;
the nominal 15-block piece height is not total generated height. Both loot
constants are bound to the existing BuiltInLootTables source. Inventory SHA:
`960a8759842f2a0a267fba6eae526c8e59062d08e6148c33fad7d5d498b1e133`.
Decision SHA: `78b6dcd53d7e3c855b6e64477c0773601c3b83138705ea122eb6cc48be955378`.
Commands are in `evidence/item-8/sources/vanilla-desert-pyramid-code/README.md`.
The pending content instructions below are superseded. Continue remaining direct
generators and provider reconciliation, without re-extracting desert pyramid
sources. Approximate full geometry, actual visibility and effective retained-mod
behavior remain open. No measurement system was added. Item 8 remains incomplete.

The desert pyramid constructor binding is resolved in
`evidence/item-8/sources/vanilla-desert-pyramid-binding-code`: bootstrap entry 0
targets DesertPyramidPiece, and SinglePieceStructure invokes that callback once
at the chunk origin after its below-sea-level rejection check. Manifest SHA:
`f83997815e0225442cdcd1819b3b7b1c210c8296da1b22191c7bba31df5e3b1c`.
The focused binding test and scoped checks pass. The verbose structure's class
and archive identities match the earlier ordinary disassembly. No new measurement
system was added. Continue remaining cellar geometry/candidate logic and both
loot-source paths before family integration; do not repeat the resolved binding.
Inventory and decision hashes are unchanged. Item 8 remains incomplete.


Desert pyramid source inspection now preserves its piece and structure-level
archaeology path under `evidence/item-8/sources/vanilla-desert-pyramid-code`.
Manifest SHA: `89770d3b09f15c47e801b2889bf431d3f5e823c047cc8025c1fd433932e405d9`.
Extraction and scoped checks pass. The source distinguishes TNT/pressure-plate
placement, chest-result flags, cellar construction and clipped archaeology
selection. Inventory and decision hashes remain those of the swamp-hut increment.
Next resolve the SinglePieceStructure callback using existing verbose javap
support, inspect the remaining cellar/placement logic, and integrate the family
with both loot paths. The source README records exact remaining work. No new
measurement system is required; Item 8 remains incomplete.


Swamp hut source and shared ScatteredFeaturePiece placement code are delivered
in `ab64119`; family integration is `5498f16`. Nine attributes now record its
7 by 9 nominal footprint, 7-block piece height excluding downward supports,
authored witch/cat attempts, distinct natural-spawn overrides, no container-loot
or spawner path, visual form and surface placement. Flags are set before entity
creation and do not prove successful spawning. Both source manifests and the
packaged overrides are bound by the focused test. All 62 affected tests and
scoped checks pass. Inventory SHA:
`d93524bb47e54899420a239639a7799f24f698ff0e8e104264d2b6eb7fe0ae14`.
Decision SHA: `ce6e76b57b9b5a015cd05472a95ea23510a67c99d2c544949ef9931097d69ef1`.
Commands and limitations are in `evidence/item-8/sources/vanilla-swamp-hut-code/README.md`.
The shared placement class resolves actual constructor dimensions and height
adjustment, and can be reused for the remaining desert pyramid and jungle temple.
No measurement system was added. Continue those direct generators and provider
reconciliation; actual visibility and effective retained-mod behavior remain open.
Item 8 is not complete and has not reached its final review/merge gate.


Buried treasure geometry is resolved in `d59a52e` from the existing direct piece
source: a one-block chest target, with potential direct infill enclosed by a
3 by 3 footprint and 2-block height. The solid support below cannot enter the
air/liquid replacement branch. These are source-derived write bounds, not an
observed sample or guaranteed changed-block count. Three affected tests and
scoped checks pass. Rebuilt inventory SHA:
`9840227ee2568964048442f5549adc215ad8e345a1e0fea1662a7d77c9c3f5bb`.
Decision SHA: `6c0e1ee405a80290bc0d38675250a8486a283655a27595b9f21ab8609cb5631a`.
Commands and derivation are in the buried treasure source README. No new
measurement system was added. Continue the remaining direct generators and
provider gaps; actual world observations and effective mod transformations are
not supplied by this geometry derivation. Item 8 remains incomplete.


Buried treasure source (`90eb4d4`) and family integration (`9f68b51`) resolve
its direct piece path without inventing template or pool components. Seven
attributes now record authored content, placement and lack of a generated
landmark. Search failure and discarded createChest result remain explicit:
a start record does not prove a surviving loot chest. Existing observed
geometry, dimensions and world links are preserved. All 62 affected tests and
scoped checks pass. Inventory SHA:
`5e426fa4293e0a222ec010598921bac7ad8d550ee44b8571326fb47b57703efa`.
Decision SHA: `873cac500cf01735864b85e9f5db35ef99085ae3d33990b45774f1eb6d836b3c`.
Commands and limitations are in
`evidence/item-8/sources/vanilla-buried-treasure-code/README.md`.
Continue remaining direct generators, including desert pyramid, jungle temple
and swamp hut, plus provider reconciliation and effective retained-mod gaps.
Actual visibility is not implied by authored visual cues. Item 8 remains open.


Ruined portal source inspection (`07dda51`) and family integration (`84faa88`)
resolve thirteen template alternatives across all seven roots, retained as one
family. Six attributes record authored content and per-root placement modes.
Each template has one ruined-portal loot chest and no authored entities or
spawner blocks. The five jigsaws reference only minecraft:empty pools; their
metadata are preserved without inventing extra families or final block states.
Observed geometry remains intact because terrain additions exceed template
bounds. All 62 affected tests and scoped Ruff/Basedpyright checks pass.
Inventory SHA: `fdd49f9bb42cd4169fa57f946bae28f43b7045a67f44bbc91d292d9874c1c3e7`.
Decision SHA: `b8e7afa9e0bce110f88071c2eefdabd1f0c4500a93c0f2f1c1e6b4f4dde1f305`.
Commands and limitations are in
`evidence/item-8/sources/vanilla-ruined-portal-code/README.md`.
Continue the remaining custom generators and provider gaps. Vanilla buried
treasure, desert pyramid, jungle temple and swamp hut are remaining direct
piece generators. Retained-mod transformations and visual discoverability
remain open. No new measurement system was added; Item 8 is not complete.


Ocean ruin source inspection (`9cdff83`) and family integration (`ddecb9b`)
resolve all 48 references, with 12 warm and 36 cold templates kept inside one
family. Six source-backed attributes now include authored drowned, chest and
archaeology loot paths. Cold brick/cracked/mossy layers must not be counted as
separate families or independent rewards. Existing observed geometry, dimension
and world-observation links remain intact. All 62 affected tests and scoped
checks passed. Rebuilt inventory SHA:
`bcc6a0988f1abf235b2f1b5f6eab4b6cc793e24bf02c4a1adabc4201eb45317c`.
Decision SHA: `e0c453f708bf61c484ec379d3c3d7924733f587a109699a6dccbcb9e6bf5023b`.
Commands and limitations are in
`evidence/item-8/sources/vanilla-ocean-ruin-code/README.md`.
Continue remaining custom generators and provider reconciliation. Vanilla ruined
portals are a next bounded source candidate. Visual discoverability and effective
retained-mod transformations remain open. No new measurement system was added.
Item 8 is incomplete and its final review/merge gate is still pending.


Nether fossil source inspection and family integration are delivered in
`fab790e` and `9e13390`. All fourteen template references resolve as alternatives
within one family. Seven source-backed attributes are recorded and all 62 affected
tests pass, with scoped Ruff and Basedpyright passing. Rebuilt inventory SHA:
`d2be7cc46dd728e03729370881c10747960302a91770644fc98a8bbcc87bb573`.
Decision SHA: `d1af44e8dd07c4ab772e223d52f16984520eb5ba6517db884bc0d06c99c69593`.
Commands, source identities and limitations are in
`evidence/item-8/sources/vanilla-nether-fossil-code/README.md`.
The next bounded custom-generator candidate is vanilla ocean ruins. Preserve
remaining effective-mod, hostility and visual-discoverability gaps. Item 8 is
still incomplete; do not treat this family increment as the exit gate.

User constraint reaffirmed: a new measurement system is allowed only when
strictly necessary and worth its time and effort. Identify the specific Item 8
requirement, explain why existing evidence and tools cannot resolve it, and
weigh the expected result against implementation and execution cost before
adding one. This increment reused existing extraction and inventory paths.


Dimension membership is integrated: builder/tests `89b8830`, inventory `702ec5c`.
Inventory SHA:
`ae7f0a16a86929ad24361ab9befa80aebf5e51100c72bc9ba44a64f8f8bafba2`.
Decision SHA remains
`06cff81b09d0caa84837c979acd85bfa207b9037ab27e3e9134853ba6811a89d`.
All 61 affected tests and scoped checks pass. Every registered root has a
per-root biome-compatibility result; three IDAS tag gaps stay unknown and nine
roots have no overlap. Six of those have empty resolved lists; the three Deep
Aether roots target sacred_lands, absent from live dimension membership. No
family-level observation conflicts with the joined dimensions. Exact cases,
commands and boundaries are in `evidence/item-8/runtime/README.md`.
Only dimension fields and input identities change; groupings, other attributes
and observation links are preserved. Delivery refs verified. The pending join
below is superseded. Do not rerun collection or repeat this join. Continue the
remaining custom-generator content/geometry and provider gaps, with vanilla
Nether fossils a next bounded source inspection. Biome overlap does not close
all placement conditions or Item 8, and zero-overlap roots must remain inventoried.

Live dimension membership is captured and durably delivered. `77b6eec` preserves
rejected dimension-r1/r2 receipts and successful dimension-r3 output; `cd04324`
binds it to the original frozen capture. Output SHA:
`08fa8185cd2c3f54b5255b2e8f86946c4b37ed471fb1991d0f82c835ffe20c7c`.
All ten expected dimensions are covered; r3 preflight and all seven registry
records exactly match registry-r1, configuration comparison passes, and the
correlated flush/clean exit pass. The 20 lifecycle/runner tests, focused capture
test and scoped checks pass. The probe is an optional read in the existing
lifecycle, with no extra retained mod or class transformer. r1 lacked queued
failure diagnostics; `d4e107d` preserves them. r2 exposed client-only subclass
reflection, fixed in `428819f` by invoking the public BiomeSource base API.
r3 at that revision is the successful live regression. No probe process remains.

Raw custody is delivered through `e9a91c2` and `5b742a5`: archive SHA
`29c9b189483f96f29d45a62d79556fdf10655729cf901204def50789578b5cb7`, 261 files,
with successful local and downloaded restores. Tag
`item-8-dimensions-raw-2026-09-05-r1` resolves to
`cd043241a1beabaa47acd9657790af1e987e9dd0`. Runtime and custody READMEs contain
exact commands, failure dispositions, identities and boundaries. This supersedes
the pending collection instructions below. Next integrate membership with the
existing per-root biome constraints in the inventory, retaining unknowns and
placement-condition limits. Do not repeat the completed collection. The inventory
and decision hashes below remain unchanged, and Item 8 remains incomplete.

Dimension eligibility is the next shared gap. Source inspection `36f7e0b`
establishes that Lithostitched's saved delegate omits runtime injected/replaced
biome lists, and the manager also accepts event-supplied injectors. Manifest SHA:
`b48129fffa046624fb15e6381edb678001d491c4be8ddcd03e2c5ec440f8afaa`.
The existing NeoForge dump command was inspected too: it writes registry keys
with optional numeric IDs, not values or dimension memberships. Manifest SHA:
`fa8eff257d4a41da1edf9a092326af303160207c616ec4266c750a35a5d244d5`.
Reproduction and boundaries are in the two source READMEs under
`evidence/item-8/sources/lithostitched-biome-injector-code` and
`evidence/item-8/sources/neoforge-dump-command-code`. Extraction and scoped
checks passed; source refs were pushed and verified. No new runtime collector
was added and inventory identities below are unchanged.

Do not rerun the unchanged registry dump or infer effective dimension membership
from saved delegate presets. Next choose the smallest runtime-object read that
resolves possible biome membership across the frozen dimensions, reusing the
existing materialization and lifecycle. This closes an explicit Item 8 attribute
gap shared by families; avoid reconstructing every dynamic biome provider in a
new static emulator. Confirm the chosen read preserves the frozen identities
and distinguishes possible membership from successful structure generation.
The source investigation narrows the collection method, not the completion gate.

Igloo integration is delivered: `3a102c3` records three components and seven
attributes, and `ca0fa30` delivers the inventory. All 59 affected tests passed;
scoped checks and the final focused test passed after one explicit regex-result
type annotation. Source README records geometry derivation and reproduction.
Decision SHA:
`06cff81b09d0caa84837c979acd85bfa207b9037ab27e3e9134853ba6811a89d`.
Inventory SHA:
`9f2fa36230e5520571b71f9535b3d1291527c939ec9fee4867e04bfaefc06d01`.
Only igloo attributes/grouping and the decision input identity change; raw world
evidence and trace are unchanged. Remote refs verified. The pending igloo
integration below is superseded. Continue remaining custom generators and
provider/family gaps without repeating this source work. Effective retained-mod
effects, remaining attributes and final Item 8 closure remain open.

Igloo generation source is delivered in `74efeb4`, using the existing extractor
extended in `3a174ef`. Both remote refs were verified. Its manifest SHA is
`5104752aa5eb795053f75e8d62731b7ea7d79af1f9cacfdccfe2e55f9336838e`.
See `evidence/item-8/sources/vanilla-igloo-code/README.md` for reproduction,
component selection, placement and chest assignment. Scoped Ruff/basedpyright
passed. The next step is the existing frozen-template reconciliation and igloo
family integration, not re-extraction. Inventory and decision hashes below are
unchanged. Initial catalog inspection found basement villager and zombie-villager
entities and a brewing-stand item; retain and verify those in the focused content
check before making accepted family claims. Do not infer no authored mobs from
the chest-only marker handler. Item 8 remains incomplete.

The user permits an additional measurement system only when strictly necessary
and worth its time and effort. Identify a specific unsatisfied exit requirement
and why existing evidence/tools cannot prove it before adding such a system.
This igloo source increment required none.

Shipwreck integration is delivered: `4363af9` records both root-specific template
arrays and seven source-backed attributes; `3c30ead` delivers the inventory.
Decision SHA:
`da5faabb91380aaa6fc09b36a941ded23a633dc50888705eb0a5776e2f8a3bb3`.
Inventory SHA:
`7f15e3abd77c380cfccfc836f677027f65d94782fac7ebf2ed033af010f1dcee`.
The trace is unchanged. All 59 affected checks passed; the final focused check
and scoped Ruff/basedpyright passed after narrow type/iteration cleanup.
Nominal dimensions now cover the template alternatives rather than only observed
sample sizes. Original world_observations links and raw bounds remain unchanged.
The earlier instruction to integrate shipwreck content is superseded. Continue
the remaining family/provider gaps; retained-mod effects, hostility, visual
discoverability and final cross-source closure are not inferred from this work.
Delivered refs were verified.

Shipwreck source work is delivered: extractor `5e750e4`, evidence `5f82e86`,
catalog check `db53fd6`. Manifest SHA:
`313d8031a873de27b39ca5fa8fed9ab1ea1f3694fc56db8afcd7127a3e4415b8`.
See `evidence/item-8/sources/vanilla-shipwreck-code/README.md` for commands,
nominal dimensions, burial semantics and chest markers. Generation selects one
template from 11 beached or 20 ocean alternatives; all resolve. All palettes
were checked after correcting an initial single-palette assumption. No authored
entities or ordinary/trial-spawner blocks occur in these templates. Three chest
loot-key mappings reuse the End city BuiltInLootTables evidence.
Next integrate shipwreck per-root components and family attributes, including
the source-derived single-template size envelope. Do not repeat extraction or
add a runtime measurement for this nominal geometry. Retained-mod effects and
other final gates remain open. Source/test/scoped checks passed and refs verified.
The current inventory and decision hashes below remain unchanged.

End city component and four content attributes are integrated in `027c263`,
with inventory delivery `5fa7b83`. Its 19 vanilla template references resolve;
the family record preserves the unreferenced tower_floor and the boundary for
retained-mod transformations. Mob sources, loot sources, generated-spawner
disposition and authored/natural attribution now reflect the marker evidence.
Decision SHA:
`2a9e4ceb4fab1710d405bb40ce5b91a63756f60333381ba54251c5785a26036d`.
Inventory SHA:
`ed35e7543958e6441e0fb73487b28722a8d5349b0589f4418850abcc55cccf16`.
The trace is unchanged. Validation passed after narrowing one stale test that
required every custom generator's components to remain unknown; the other 58
checks had passed and the affected focused rerun passed. Scoped checks passed.
End city geometry and remaining effective attributes are still open. Do not
repeat the completed component/marker work. Delivered refs were verified.

End city source extraction is delivered: tool `888f3b8`, evidence `a73fd28`,
frozen-template check `f5348b7`. Manifest SHA:
`ca7cb2c777ad0fc638e28cded50a78ab048ca26ad243eeb564fa72be7cac943c`.
See `evidence/item-8/sources/vanilla-end-city-code/README.md` for exact commands
and dispositions. The vanilla generator references 19 of 20 packaged templates;
`tower_floor` is unreferenced. Sentry markers create shulkers, Chest markers
assign end-city treasure, and Elytra markers create an elytra item frame.
Normal template entities are ignored by placement settings. The focused frozen
catalog check and scoped Ruff/basedpyright passed. Delivered refs were verified.
Next integrate these dispositions into the existing End city family attributes;
do not repeat extraction or mistake template markers for observed city counts.
The family decisions, inventory and trace hashes below remain unchanged.

Conditional trial-chamber mob attribution is now in the machine-readable family
attribute, delivered in `343095a` and inventory rebuild `f441595`. The existing
attribute override was sufficient; no builder logic or new schema was added.
All 68 affected template/family tests and scoped Ruff/basedpyright passed.
Decision SHA:
`fda5d5c1b1ea4a33d2a5a099fd51ecd24b760a921008107f9f89d2758de1cb75`.
Inventory SHA:
`2f915136cf8ff69430a4be1e099f675ea9e7a928175c7621c51f485d3020740d`.
Trace SHA remains `703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5`.
Only this family's grouping evidence and mob-source attribute changed beyond
the decision input hash. Raw omitted ominous-list entries remain available and
are explicitly cross-referenced by the conditional mob-source disposition.
The previous instructions to incorporate this disposition are superseded.

Do not interpret the trace's 69 no-direct-pool roots as 69 wholly uninspected
generators. Current decisions already have six source-based attributes for the
13 Better Mineshafts roots and the spider dungeon; other attributes still need
closure. Inspect existing decisions before repeating custom-generation work.
The next useful unresolved source paths include vanilla end cities and the
remaining custom families. Overall canonical grouping, provider coverage, final
attributes, review and main merge remain open. Delivered refs were verified.

Initial vanilla trial-spawner attribution is now resolved conditionally.
Lifecycle source `bb9582a`, extractor selection `2c43578` and frozen-catalog
check `c5531da` show initialization from normal potentials before player
detection can make these initially non-ominous spawners ominous. The five mob
IDs are breeze, spider, cave spider, silverfish and slime. Slime has two Size
variants (1 and 2) with weights 3 and 1; an initial one-entry test premise failed
and was corrected to preserve those values. Ten focused tests and scoped
Ruff/basedpyright passed. All delivered refs were verified.
See `evidence/item-8/sources/vanilla-trial-spawner-lifecycle-code/README.md`.
Manifest SHA:
`658728eebd2eec80ac69ecf077c4ca305efa3102a3f4d2b2c9655ca95d962aab`.
The current trace and inventory hashes remain unchanged. Do not repeat the
vanilla lifecycle work: apply this conditional disposition when assembling
effective family attributes, while retaining the boundary for mod transforms
and arbitrary saved states. Continue broader custom-generation/provider gaps.

Trial-spawner selection code is delivered in `776dcdb`, extracted with `ed49f84`.
See `evidence/item-8/sources/vanilla-trial-spawner-code/README.md` for the exact
command, method/offset references and limitations. Manifest SHA:
`aa43a73247921fd7ece2e3a71d811c0bddba492a6ea04e198825fc111082449e`.
An omitted potential list decodes empty. The ominous transition preserves
existing next-spawn data when that list is empty; it does not copy normal-mode
potentials into the ominous configuration. Exact entity attribution remains
conditional on prior lifecycle state. Do not repeat these three class extractions
or replace the five unresolved entries with unconditional normal-mode IDs.
The current inventory and trace hashes below remain unchanged. Next finish the
conditional attribution using the existing lifecycle/source path and move on to
the remaining custom-generation and provider coverage gaps. No new measurement
system was added. Extraction and scoped Ruff/basedpyright passed; refs verified.

The ID-less vanilla trial-spawner omission is fixed in `74b748c`, with trace
delivery `f539e25` and inventory rebuild `cc819fe`. All 14 affected packaged
templates identify the trial spawner through the palette, not NBT `id`.
The existing decoder now preserves that identity separately from unchanged NBT.
No new measurement system or server run was necessary. The user's constraint
is explicit: add another measurement system only when strictly necessary and
worth its time and effort. Continue to prefer the existing evidence paths.

Current trace SHA:
`703eed7b5d558b54a62985c7f919d0254e8de613292364c514c5b47b298accc5`.
Current decisions SHA:
`8a311905415a0b0b855c39961e5f816113a3017171f02dcb85ea371a2be627fb`.
Current inventory SHA:
`05232e50f2e151da2ed21e6aebe5c6c589e58ab87c86020625303d5364770b42`.
These supersede the hashes in the modifier checkpoint below. The 84 affected
decoder/consumer checks passed, followed by 69 checks against regenerated
evidence. Scoped Ruff and basedpyright passed. Delivered refs were verified.
Only trial-chamber generated-spawner attributes change beyond source hashes.
Five omitted ominous spawn-potential lists remain explicitly unresolved. Inspect
the existing game-code path for their effective semantics before claiming closure.
The earlier suggestion that vanilla configurations were registry references was
not established; the affected templates contain inline configuration compounds.
Broader provider coverage, 69 custom-generation roots, final grouping and all
required family attributes still need closure, followed by review and main merge.

Modifier evidence regeneration is delivered: trace and dependent decision/pin
updates in `755fbd8`, inventory rebuild in `7cd7893`. The committed-source
trace reproduction matched the pilot byte for byte. The trace changes only
input identities and modifier-report entries; all structure reachability and
template contents remain unchanged. The 429 family-decision substitutions and
431 inventory substitutions are source hashes only. All 71 affected family,
pool and modifier checks passed, with scoped Ruff/basedpyright passing after
two narrow test-style corrections. Delivered refs were verified.

Current trace SHA:
`9bac83e23b19826a872a3d760ca44bdcf6e24b3ef9df3a2693c9737ec28f3a0d`.
Current decisions SHA:
`3ebb87bee8c663dc488b164b14a7f328d65fa17b4becb381aebc9c9db217de65`.
Current inventory SHA:
`9fdf722bfe1346e0747687760203281b2121cf344ae2e94fb314a83511aa7441`.
The old instructions below to regenerate the modifier report are superseded.
No selected packaged modifier remains marked untraced, but this does not close
all provider hooks or family attributes. Continue the broader inventory gaps,
including the 69 custom-generation roots and effective spawner/mob/loot sources.
The working 452-group inventory remains incomplete; review and main merge are
still required. Do not redo completed modifier source checks.

Selected feature contributions are resolved in `bcacd6a`: the terminal
configuration check covers 11 component types and 44 configured block IDs,
with tree/root/state-provider implementation dispositions in
`evidence/item-8/sources/regions-unexplored-feature-code/README.md`.
The final random-block provider was extracted with `5ae4555`; it selects a
configured block's default state (or air if empty). These 34 modifiers add or
remove vegetation/ground cover/ash vents, not a distinct structure family.
Placement, frequency and whole-provider coverage are not claimed.

Trace integration is delivered in `1ffa075`. It binds the relevant config and
source identities and records all 37 formerly untraced selected modifiers as
inspected non-family contributions, retaining each complete modifier document.
The executed pilot command was:
`uv run -m tools.trace_item8_structure_pools --output evidence/raw/item8/pool-traces-modifier-dispositions.json.gz`.
Pilot SHA `9bac83e23b19826a872a3d760ca44bdcf6e24b3ef9df3a2693c9737ec28f3a0d`.
Only top-level inputs and pool_modifiers differ from the current committed
trace. The report contains 956 condition exclusions, 68 pool additions,
one alias replacement and 37 inspected non-family contributions. Twenty-one
affected tests and scoped tool checks passed. Pushed refs were verified.

Next reproduce that pilot from the committed tool, publish the trace, update
the existing family-decision hash references and builder pins, and rebuild the
inventory. Update the frozen-report regression to require the new dispositions.
The current committed trace, family decisions and inventory still have their
previous identities until that atomic generated-evidence migration is done.
Do not repeat the completed modifier source inspection. Broader provider/family
coverage, 69 custom generators, attributes and final review/merge remain open.

Feature configuration binding is delivered in `48fef4a`, with source selection
`78eca8f`. All 34 declared predicates map to enabled toggles in frozen common
config SHA `300dda462e31f6f1bcce0d67308e4939d1b461a03c8cc92ba805f7ac9d1cb66c`.
`ConfigPredicate` delegates to `RUCommonConfig.test`, which resolves the
`vanilla_changes/` key suffix in its toggle map. The existing reference test
now verifies every key and its true value. Focused test and scoped checks pass.
Source identities SHA:
`1b447725ac61174b8cf0f35ed5457291460c54938c49b9d8296809781a87ba8d`.
See `evidence/item-8/sources/regions-unexplored-feature-config-code/README.md`.
The retained ground-cover provider changes only AMOUNT and horizontal FACING
on its configured block. Predicate truth does not establish world placement.
Next reconcile tree/root/decorator and remaining state-provider content, then
write the combined modifier dispositions. Do not repeat configuration tracing.
Inventory generation, broader Item 8 closure and review/merge remain open.

Feature reference closure is delivered in `a774424`. The focused test
`tests/item8/test_feature_modifier_references.py` follows all 30 additions and
four removals through 34 placed and 41 configured feature resources, including
inline branches. Six endpoint types remain for final content disposition:
simple block, tree, saguaro cactus, palm tree, bamboo tree and giant lily.
The latter four code bodies are already retained under
`regions-unexplored-feature-code`. Finish implementation/provider/decorator
inspection and config applicability rather than repeating reference extraction.
Ten affected tests and scoped checks passed. Commands and limitations are in
`evidence/item-8/sources/lithostitched-feature-modifier-code/README.md`.
The machine trace/inventory remains unchanged pending final dispositions.

Surface-rule reference closure is delivered in `7b7c886`. The focused test
`tests/item8/test_surface_rule_contribution.py` follows all 52 referenced
Regions Unexplored Overworld rule documents in the pinned catalog and verifies
their 42 terrain-block terminal types, including both config branches. The
existing resource selector now accepts surface-rule resources; no runtime
measurement or new extraction system was added. Nine affected tests and scoped
Ruff/basedpyright passed. The evidence README under
`lithostitched-platform-modifier-code` records the command and limits.
The surface rule contributes terrain palette changes, not an extra family.
Config activation is unnecessary for this limited claim because both branches
are covered. Compiler, street processor and surface-rule source dispositions
are now ready for the combined report update; the 34 feature addition/removal
modifiers still need their content/config checks. The machine trace/inventory
has not yet been regenerated. Item 8 remains incomplete.

NeoForge dispatch and surface lifecycle are resolved in source evidence
`236b3e5`, extracted with selectors `59df00e` and `643c1d4`. See
`evidence/item-8/sources/lithostitched-platform-modifier-code/README.md` for
commands, identities and runtime log bindings. The NeoForge lifecycle mixin
appends converted Lithostitched biome modifiers; the dedicated-server mixin
calls surface application before level loading. Raw log lines 13027 and 12905
confirm the respective mixins. Surface merging preserves other generator
settings and orders PREPEND, original, APPEND rules. No observed final surface
tree or feature placement is claimed. Scoped checks passed and delivery was
verified. The earlier next-hook instruction below is now superseded.

Next finish the referenced feature/rule bodies and configuration predicates,
then apply the accumulated modifier dispositions together. Do not add a new
measurement system for this static contribution check. Broader family coverage,
attributes, custom generators, trial-spawner config references, final gate,
review and main merge remain incomplete; the goal remains active.

Feature implementation inputs are delivered in `78dce5f` (Regions Unexplored)
and `cea115f` (Lithostitched), extracted by existing tool selection `d0043b6`.
Each source directory has the executed reproduction command and scope:
`evidence/item-8/sources/regions-unexplored-feature-code` and
`evidence/item-8/sources/lithostitched-feature-modifier-code`.
Identities SHA respectively:
`d27de44a59aedb2dd41e12dcc0f35db1328207314c8cbe59dae6120de5b9953b` and
`b7138be0cec7822f8e4fb19c6c9175e3ac1ba7ab174cb58015c34be488b9aaa1`.
Both groups contain seven exact classes. Scoped Ruff/basedpyright, extraction
and identity checks passed; pushed refs were verified. These are implementation
inputs, not final modifier dispositions or a new measurement system.

The giant-lily generator checks four water/air positions and can write four
lily blocks before returning false. Preserve that source-level behavior; do
not equate a false feature return with absent blocks, and do not repair the
frozen mod. Weighted-selector and composite generators delegate to their
configured placed features. Reference surface rules delegate to referenced
rules; the Regions Unexplored config rule selects between its two rule bodies.

Next follow the platform hooks: `AddFeaturesModifier.apply` runs only on
Fabric, with a separate `createNeoforgeModifier` path, while
`AddSurfaceRuleModifier.apply` is empty. Those methods do not prove the
modifiers inactive on this NeoForge stack. Exact next classes located but not
yet retained/inspected are Lithostitched's
`mixin/common/ServerLifecycleHooksMixin`,
`impl/worldgen/modifier/NeoforgeModifierHolder`, and
`worldgen/surface/SurfaceRuleManager`. The tree/root-placer implementations are
retained but their full contribution inspection and feature/rule reference
closure remain open. The 37-entry machine report is still pending the combined
update described below; do not represent this source acquisition as completion.

Village street processor source closure is delivered in `3c19575`, with exact
selectors in `c23bbab` and registration selection in `eb0cb28`. The six retained
classes and reproduction commands are under
`evidence/item-8/sources/lithostitched-street-processor-code` and
`lithostitched-processor-registration-code`. They establish conditional silt/peat
path and grass substitutions, preserving positions and NBT. This contribution
adds no family, pool, template, authored entity, spawner or loot reference.
This does not claim observed activation of the biome/config conditions.
Processor identities SHA:
`b813d2393bfb7ff410451e5cee65a6036187abe438405bb2a1d9cd00e5f5cafc`.
Registration identities SHA:
`803ac1e2b0d9992d51c5e5246db7ff88683fe0f7de21ec6f4e9881d240da991f`.
Scoped Ruff/basedpyright and identity inspection passed; the pushed evidence
ref was verified. No new measurement system or runtime capture was added.

Pool compilation source closure is delivered in `3fa8f5b`, generated with tool
`45e194d`. The three exact classes under
`evidence/item-8/sources/lithostitched-pool-compilation-code` show raw pairs
copied into weighted entries holding the same element. Shuffling changes order
but introduces no template or family. Identities SHA:
`c69e16e8ae53df5fa0d817126b3b62d739e7780292576c1891e3084054ee556e`.
The extraction and scoped quality checks passed. Do not build a shuffle simulator
for this possible-content requirement. The machine-readable report remains
unchanged pending the remaining modifier dispositions; combine those report
updates to avoid repeated whole-inventory reference migrations.

The remaining selected modifier checks are Regions Unexplored's 30 feature
additions, four feature removals and one Overworld surface-rule injection.
Their modifier bodies have been inspected. Follow placed/configured feature
references and surface-rule references before assigning final dispositions.
The feature documents include simple blocks, patches/flowers, weighted
selectors, trees, a giant lily and a composite swamp-tree feature. The latter
also contains a conditional bioshroom placement, so names alone are insufficient.
The surface-rule injection prepends `regions_unexplored:overworld`; its body
references further surface, subsurface, swamp and cave rules. These references
are not yet fully closed. Reuse the preserved catalog and existing inspection
tool; do not simulate placement merely to establish possible content.

Correction to the prior checkpoint: `ReferenceStructureProcessor` is the class
bound to the JSON `lithostitched:reference`, not `UnboundReferenceProcessor`.
Inventory, family decisions and trace identities remain as recorded below.
The machine report still has 37 untraced modifier entries pending the combined
update, including the compiler and street processor now resolved in source
evidence. Broader Item 8 closure remains open.

Trial alias correction is delivered: shared tag/alias decoder `749c1a2`, trace
integration `f4efdcc`, generated trace and decision bindings `48df0e9`, rebuilt
inventory `073cfb3`. The existing tag merger is now named `tag_inputs` and
accepts the current resource kind; all former biome callers were updated.
The biome source output reproduced byte-for-byte. Eleven decoder/tag tests,
22 affected pool/tag tests and three affected family checks passed; scoped
Ruff and basedpyright passed. Both trace builds matched byte-for-byte.

The trace now applies the selected replacement and follows the merged tags,
including `regions_unexplored:trial_chambers/ashen`. It preserves original
aliases, replacement aliases/document, shared-index binding groups and tag
source identities. It makes no tag-order or joint-frequency claim. The output
regression verifies ashen template reachability and both normal and ominous
entity IDs. Other registered-root traces are unchanged. Trial chambers remain
one family; only its inventory content changed beyond source-hash substitutions.
The modifier report has one included alias replacement and 37 other selected
modifier types still untraced.

Trace SHA:
`b78541655c69fbc3599a670ccc424d60dd08cbb642bd796a9b69bcb9c1f223d9`.
Decisions SHA:
`3fc8ed59195ee040f746b9aeef957d1d4a72293016bab2a13b5e5b37eda518bc`.
Inventory SHA:
`d5b51f2f140e2d88bf77d9f3dac5168f0b4dfacd827ae9cf1908d42abbf4d369`.
Reproduction commands and scope are in the alias-code README under evidence.

Continue the remaining modifier dispositions. The internal raw-template
compiler delegates to `StructureTemplatePoolMixin.compileRawTemplates`; that
class and `StructurePoolAccess` were located but not yet retained/inspected.
Use the existing exact-class selector. Regions Unexplored's street processor
reference and other feature/surface modifiers remain open. Also resolve vanilla
trial-spawner configuration references: the inventory currently reports explicit
inline ashen IDs, not all effective vanilla trial encounters. Do not mistake
that partial source list for exhaustive mob-source closure. Broader family
grouping, custom generation, provider coverage, attributes, final gate, clean
review and main merge remain incomplete. No new measurement system was added.

Trial alias source semantics are delivered in `fab1b99`; tool selection was
added in `0b43dfd`/`484ff42`. The existing inspection tool now optionally selects
exact classes so new evidence does not duplicate old disassemblies or revise
unrelated identities. Four exact classes were retained under
`evidence/item-8/sources/lithostitched-alias-code`. Identities SHA:
`eea3af78139809c0a2452a0027bfe83fac321380574b3a10ba3d8dcc16c1691b`.
All four matched the corresponding initial broad extraction; scoped Ruff and
basedpyright passed. Reproduction and method details are in that directory's
README. No new measurement system or runtime capture was added.

The alias gap is material: Regions Unexplored adds
`regions_unexplored:trial_chambers/ashen` to the melee pool tag. The current
accepted trace still omits that replacement path. `SetPoolAliasesModifier`
replaces vanilla jigsaw aliases when append=false. `RandomEntries` draws one
index using the first holder-set size, then applies that index across the
aliases and holder sets. Preserve this shared-index relationship, especially
ranged/slow-ranged. Its `allTargets` method returns an empty stream and is not
valid evidence of absent targets. The lookup mixin keeps the last duplicate
alias entry. Do not infer ordered tag membership or joint spawn frequency from
a sorted union of possible targets.

Next correct the existing trace using the replacement and additive pool-tag
sources, with a focused regression proving the ashen contribution and preserved
source/correlation evidence. Existing biome tag merging is currently hardcoded
to biome tags; reuse that logic where appropriate rather than adding a parallel
tag framework. Raw-template compilation runs at priority 2147483647 and calls
each pool's `compileRawTemplates`; the delegate implementation still needs
inspection. The accepted trace, family decisions and working inventory remain
unchanged by this source inspection. Broader Item 8 closure remains open as
listed below.

Better Village attribution is delivered: tool `cd2d54f`, seven-class code
evidence `45ab692`, family decision/test `9595c52`, working inventory `18c7466`.
No extra family or compatibility simulator was introduced. The existing
vanilla village decision attributes its 246 packaged replacements, 244 reachable
selected templates, the two untraced snowy streets, disabled compatibility
entries and the active placement hook. The four compatibility targets are all
absent from the captured Mod List and their packaged entries are disabled.
The decoration mixin downgrades a loading error log to debug; preserve that
limitation when interpreting logs. Other placement modifiers remain unresolved.

The focused source-bound regression passed; scoped Ruff and basedpyright
passed after correcting test JSON annotations and line lengths. Only the
vanilla village record and top-level decision hash changed in the generated
inventory. Commands are in `evidence/item-8/sources/bettervillage-code/README.md`.
Code identities SHA:
`91e8ac8a00856a802878445dc09ad73001779602300558a472dc88444cef8020`.
Decisions SHA:
`ac85610fd8f09a8fd4c35cbecfe924ce1e8c01313fa64587000da6d5cd7e50e3`.
Inventory SHA:
`f8f649f13b19f4ed97f3c234be1346298239dc9ebc977f6eacb3ef2c1f9171ed`.

Next inspect the remaining selected modifier types before claiming complete
effective content. The current report retains 38 as untraced. In particular,
`lithostitched:set_trial_chambers_pool_aliases` replaces aliases (`append=false`)
using internal random entries from trial-spawner pool tags. The existing trace
still uses structure-definition aliases, so verify that replacement and its
tag targets rather than assuming the original aliases remain effective.
Regions Unexplored's `processor_list/village_path_fix` appends a reference
processor to three vanilla street processor lists. Its Overworld surface rule
and feature modifiers need appropriately scoped dispositions. The internal
raw-template compilation modifier also remains to inspect. Reuse existing
decoders and source evidence. No new measurement system is currently indicated.
Registry assignment remains 887 IDs in 452 working groups; canonical grouping,
custom generation, all-provider coverage, required attributes, final gate,
review and main merge remain incomplete.

Village additions are integrated and delivered: trace implementation `1f7be67`,
generated trace/reference update `2d6fbfb`, rebuilt inventory `e22c24f`.
The trace now selects resource layers, filters NeoForge conditions and appends
potential links for all 68 applicable additions using the existing decoder.
Every addition is reachable from a registered root, verified by the new frozen
trace regression. All five vanilla village variants reach their corresponding
tavern template. Source identities, full modifier documents, weights, limits,
missing templates and unsupported elements are preserved. The report accounts
for 956 condition exclusions, 38 untraced modifier types and six excluded
resource layers. These are potential links, not ordered assembly or probabilities.

The corrected trace SHA is
`7b0f61a66e46d78e206244271d2a1da0c846429d5a48a7e8bb05d852f6ec3632`.
The 429 references to its old hash were updated without changing grouping
decisions or other decision fields. Decisions SHA is
`d642467b969b8a1cfbed8f90038684a847d13a13792a34d17da73e5c7e693996`.
The rebuilt inventory SHA is
`35a7f81081529b34c96948ced6dc7fb3d2580788d5ea9d13f4a7ed5b3410cd4c`.
Both trace builds and both inventory builds matched byte-for-byte. The affected
pool/resource suite passed 22 tests, the new frozen trace test passed, and all
57 family-decision tests passed. Scoped Ruff and basedpyright passed. Commands
and generated-reference migration rationale are in the existing source README
at `evidence/item-8/sources/neoforge-condition-code/README.md`.

Continue Better Village contribution attribution using existing source
inspection. Initial inspection shows its templates already use the vanilla
namespace, so check existing selected template provenance before adding any
pool-replacement machinery. `Main` and `StructureSetMixin` describe a placement
override for sets containing the five vanilla village roots. The frozen config
enables it with spacing 45, separation 20 and salt 10387312; the captured debug
log records its activation at line 18029. These initial code observations still
need promotion through the existing tracked inspection tool before an acceptance
claim. Inspect its compatibility listener/metadata path and loaded dependencies
to determine whether further content processing applies. Do not infer from its
absence of registry roots that it is irrelevant, or assume that it adds pools.
Other modifier types and custom generation remain open. Canonical grouping,
all retained-provider dispositions, required attributes, final gate, review and
main merge remain incomplete. No new measurement system or server run was added.

Modifier condition resolution is delivered in `12bd9d1`, with pinned loader
code in `515f29b` and tool selection in `c35af5e`/`7ca24fd`. The existing resource
selection module now reads the captured NeoForge Mod List and evaluates the
two observed condition forms. The hash-bound log contains 212 mod IDs, including
nested dependencies. Of 1,024 packaged pool additions, 68 pass: 26 conditioned
on Village Taverns, 21 on Chef's Delight and 21 on Farmer's Delight. The other
956 fail their conditions. These are additions to existing families, not new
families or a claim of observed placement. Three affected tests passed; scoped
Ruff and basedpyright passed. The frozen-catalog regression retains the exact
filtering logic, counts and log/catalog identities. Restore the existing r1
raw archive before running that test on another checkout.

The patched NeoForge RegistryDataLoader wraps entry decoding in ConditionalOps;
its condition list is AND, `neoforge:or` is OR, and `mod_loaded` queries ModList.
Lithostitched gathers registry and event modifiers, then sorts by priority;
addition priority defaults to 1000. Do not invent equal-priority ordering.
Existing Lithostitched disassemblies remained byte-identical while two classes
were added. The updated identities SHA is
`f3aecd612d8fdfe23649887ea70032cdc4fc5b0db00276ae3c0e718bdadf0a75`.
New condition-code and patched-loader identities are
`6dfe814d7ed7691ed4f80d460e14c7b274881ecbfee8eb29837edf51e237ba43`
and `1bcc020827e31e893e47baf01e173e915197bd755f5034fd18ef38c1d828b1be`.
Commands and limitations are in `sources/neoforge-condition-code/README.md`.

Next integrate the 68 condition-passing additions into the existing pool trace,
preserving modifier source identities, limited delegates, weights and excluded
conditions. Select resource layers before treating additions as effective.
Potential graph reachability is not ordered assembly or placement probability.
Keep other modifier types and Better Village's code-driven changes explicit.
The accepted pool trace and inventory still have NOT been regenerated. Final
family grouping, custom generation, retained-provider coverage, required
attributes, final gate, clean review and main merge remain open. No new server
run, archive revision or measurement system was needed for this increment.

Limited-element decoding is delivered through `06b1ae2`. The existing
inspection tool added three exact Lithostitched classes in `4fe823b`; generated
code evidence is in `fc6adee` under `sources/lithostitched-pool-additions-code`.
The identities SHA-256 is
`c20cbe69f4af335c21b228e602fc383c8fc0a15fc7130b27b083ac6c439e7b5b`.
The pinned code shows weighted pool additions and delegate forwarding of size,
jigsaw connectors, bounding box and placement. The limited codec retains
positive limit and optional minimum depth. The parser follows its delegate and
retains other wrapper fields as a terminal constraint record. Thirteen affected
pool-link/trace tests and scoped Ruff/basedpyright checks passed. Unsupported
nested delegates remain unresolved; missing delegates fail explicitly. The
existing explicit-codec complexity exception now includes the branch-count
rule rather than introducing a helper solely for that limit. Initial lint
also required an explicit raw regex in the regression test; both were resolved.

The accepted inventory and pool-trace artifact have NOT been regenerated:
modifier application and conditions remain open. Catalog inspection found
1,024 `lithostitched:add_template_pool_elements` resources (mostly CTOV
conditional integrations), within 1,068 Lithostitched modifiers overall.
Do not apply every packaged addition or patch only the five taverns silently.
Resolve applicable mod-loaded conditions from the frozen runtime identity,
inspect loading/application order as needed, and retain excluded or unsupported
modifier dispositions. Extend the existing tracing path. Other modifier types
and Better Village's code-driven changes remain explicit next work. No new
measurement system was introduced. Registry assignment remains 887 IDs in
452 working groups, with Item 8 final gate/review/main merge still open.

Runtime registry assignment is delivered through `8dd7f9c`, built from
`4ad283f`. All 887 captured IDs have exactly one working group; the unassigned
list is empty. The 34 vanilla roots form 21 working groups, preserving village,
portal, shipwreck, mineshaft and ocean-ruin variants. Each vanilla root has one
packaged structure definition in the retained catalog; this does not resolve
runtime hooks. Twenty-four vanilla custom paths remain explicitly untraced.
The ancient city retains its missing wall-stairs template. Vanilla mineshafts
link the existing suppression-code identity and frozen config, not an assumed
active vanilla generator. Trial aliases remain components of one chamber family.

The reused vanilla/Repurposed source checks and the new exact-once whole-registry
check passed (three affected tests, 54 deselected). Scoped Ruff/basedpyright
checks passed. Two builds were byte-identical; all 431 prior family records
remained unchanged. Inventory SHA-256:
`3061fe38349012e43e0bc35e998cc266b7470cd41d3e1efbe3a990f27c8a92ae`.
There are 452 WORKING groups, not an accepted canonical family count.

Next close a demonstrated non-registry contribution gap in the existing trace:
Village Taverns declares five `lithostitched:add_template_pool_elements`
modifiers targeting vanilla desert/plains/savanna/snowy/taiga house pools.
Each adds a weight-5 `lithostitched:limited` element, limit 1, whose delegate is
its corresponding tavern template. Mod-loaded conditions are preserved in the
packaged catalog. The current trace selects packaged pools but does not apply
these modifiers or decode their delegate wrapper. Resolve effective conditions
and modifier application, then attribute injected templates to the village
family. Better Village has four packaged compat JSON resources and requires
its code path to establish pool changes. Registry absence proves neither mod
is irrelevant. Reuse the current catalog and tracing path: this concrete gap
does not justify a new measurement system. Finish all retained-provider
contributions, custom generators, canonical grouping and required attributes.
Item 8 final gate, clean review and main merge remain open.

Aether/Deep Aether and BetterEnd are delivered in separate source/output
increments: `d883abe`/`b006a3f` and `664d235`/`8e21c9f`. All eight registered
Aether/Deep Aether roots and fourteen BetterEnd roots are assigned. The six
packaged Aether ruined-portal definitions absent from the runtime registry are
not added to active coverage. Five Aether/Deep Aether and thirteen BetterEnd
custom paths remain explicitly untraced, not empty-content claims. Bronze,
silver, gold and brass dungeon processor references remain literal source data.
BetterEnd lakes, mountains and related formation roots need code-based variant
reconciliation before a canonical family total can be accepted. BetterEnd's
village preserves missing `street_decoration/work_01` and
`terminators/stree_terminator_01` templates. No new Aether-root observations
exist; existing BetterEnd observations are linked to bridges, normal/rare lakes,
ice stars, mountains, painted mountains, small islands and sulphuric caves.

The existing authored-root check was reused, including all custom definition
fields and explicit untraced membership. Seventeen affected cases passed for
Aether/Deep Aether and eighteen for BetterEnd; 37 unaffected tests were
deselected. Scoped Ruff/basedpyright checks passed. The first Aether lint run
reported 51 statements above limit 50; combining identical key-set assignments
resolved it without adding a helper or weakening assertions. Each output was
built twice with identical bytes and unchanged earlier family records.
Current inventory SHA-256:
`22c5dc22866931048869066a27ee046dd4e492fca4e2dcd30205b29b85c689fa`.
Totals: 431 working groups, 853 assigned IDs, 34 unassigned, all vanilla.
Continue vanilla packaged-definition precedence and variant assignment, then
non-registry contributions, custom generators, canonical reconciliation and
required attributes. No new measurement system was added. Item 8 final gate,
review and main merge remain open.

Illager Invasion, Creating Space and Supplementaries are delivered in separate
source/output increments: `63df576`/`d30900f`, `b08ad94`/`fe209a5`, and
`1c77ad2`/`9111d69`. Five illager designs have explicit authored hostile intent
bound to reachable entity components; this is not an observed population.
Four space designs preserve distinct heightmaps, offsets and reused vanilla
bastion legs as components. Two Supplementaries designs preserve custom spawn
boxes, climate/sea-level conditions and frozen config references. Galleon
spawn-box markers are not ordinary block spawners. Road-sign observations 374,
407, 754 and 787 are linked; the other ten new roots have no retained observations.

The full focused family file passed 50 tests for Illager Invasion and 51 for
Creating Space. After the Supplementaries addition, all seven affected provider
cases passed (45 unaffected tests deselected). Scoped Ruff/basedpyright checks
passed for each source increment. Supplementaries initially exceeded the test
complexity limit; the unnecessary conditional around an existing shared-catalog
missing-pool assertion was removed, preserving the assertion. Each output was
built twice with identical bytes and unchanged earlier family records.
Current inventory SHA-256:
`06b6070c2b605abb48f26120ed6c7f364a8d9438f8dd8bb8c0433efcd7dd1d96`.
Totals: 409 working groups, 831 assigned IDs, 56 unassigned. Continue vanilla
(34), BetterEnd (14), Aether (4) and Deep Aether (4). Custom generators without
start pools must remain explicit until inspected, not become empty-content
claims. Non-registry contributions, canonical reconciliation and required
attributes remain open. No measurement system was added. Item 8 is not ready
for final gate, clean review or main merge.

Terralith is delivered through `0c06094`, built from `7b386d2`. All 28
registry roots are assigned once across 16 working groups. Shared cabin and
witch-hut roots are not separate families. The underground-prefixed witch hut
uses surface heightmap projection and an empty resolved biome tag. Seasonal
towers and biome rubble remain variants. Missing fortified-desert village
farmer and toolsmith templates remain explicit. No retained world observations
exist for these Terralith roots; this does not prove general non-generation.
Forty-eight focused tests and scoped Ruff/basedpyright checks passed; two builds
were identical and all 382 prior family records unchanged. Inventory SHA-256:
`1d4e2b8911051d33fa2d32b4c1996605502843ff40311133c3180e43ca63b59b`.
Totals: 398 working groups, 820 assigned IDs, 67 unassigned. Continue vanilla
(34), BetterEnd (14), Illager Invasion (5), Aether (4), Deep Aether (4), Creating
Space (4) and Supplementaries (2). Several remaining roots are custom terrain
or dungeon generators without start pools; do not invent empty traces for them.
Non-registry contributions, canonical reconciliation and required effective
attributes remain open. No new measurement system was added. Final Item 8 gate,
review and main merge remain open.

AdoraBuild is delivered through `d0ad289`, built from `306e678`. All 106
registry roots are assigned exactly once across 31 working groups. Material,
biome and size variants remain grouped with their complete definitions: 45
standalone houses, seven watercraft and separate tree-house, frozen-shelter,
temple, prison and other designs. The buried sand castles remain separate
from the tiny beach castle. Library size labels are not measured dimensions.
The basalt chamber trace retains its missing `minecraft:basalt_chambers/chambers`
pool. Existing observations link basalt chambers, houses, Nether fortresses
and prisons; absence of other observations does not establish disabled content.
Forty-seven focused tests and scoped Ruff/basedpyright checks passed; two builds
were identical and all 351 prior family records unchanged. Inventory SHA-256:
`52ab64d7cc5c4d672c397fb3f5475fae36445a7fc1d5d44268e9cb0a41e55714`.
Totals: 382 working groups, 792 assigned IDs, 95 unassigned. Remaining registry
providers are vanilla, Terralith, BetterEnd, Aether, Deep Aether, Creating Space,
Illager Invasion and Supplementaries. Continue their assignment, non-registry
contributions, custom generation and canonical/attribute reconciliation.
No measurement system was added. Final Item 8 gate, review and main merge remain open.

IDAS is delivered through `60e419b`, built from `1a65a9e`. All 84 runtime
registry roots are assigned exactly once across 62 working design groups.
Nine groups retain portal, statue, den, desert camp, desert market, dig site,
lumber camp, ship and underground camp variants. Smaller ship wreckage remains
separate. Full definitions preserve optional dependency gates, adaptive pool
switches, spawn overrides, height, waterlogging and terrain settings. Missing
ancient-mine, desert-pyramid and dread-citadel pools remain explicit. Current
traces follow declared start pools; adaptive replacement and dependency-gate
behavior still require resolution. Authored references to absent mods are not
proof of live entities. The existing provider test was reused, not duplicated.
Forty-six focused tests and scoped Ruff/basedpyright checks passed; two builds
were identical and all 289 prior family records unchanged. Inventory SHA-256:
`ba5e3e9b1c3d476ce4ef034bafd99f7455e71a41c1e650c929000cba7cb5ebb7`.
Totals: 351 working groups, 686 assigned IDs, 201 unassigned. Continue AdoraBuild
and remaining providers, then non-registry contributions, canonical design
reconciliation and required effective attributes. This assignment increment
adds no measurement system. Final Item 8 gate, review and main merge remain open.

Towns & Towers is delivered through `a0c9c6e`, built from `2177cc2`.
All 60 registry roots are assigned exactly once across eight working groups:
fort, tower and camp outposts, villages, ocean outposts, ocean villages, ocean
wreckage and the desert mimic. Full definitions and nested exclusive IDs remain
intact. Their `kaisyn` pools are components, not additional families. Missing
references remain explicit, including the Nilotic outpost's `minecraft:emptY`
pool. Fixed ocean heights are not classified from their generation step.
Forty-five focused tests and scoped quality checks passed; two builds were
identical and all prior family records unchanged. Inventory SHA-256:
`22113611f09ead1c9940c110f4c9c4a23247804bf966d2ed03f8470ba41ccff9`.
Totals: 289 working groups, 602 assigned IDs, 285 unassigned. Continue remaining
providers, non-registry contributions, canonical reconciliation and required
attributes. Final Item 8 gate, review and main merge remain open. The user's
latest constraint permits another measurement system only when strictly
necessary and worth its time and effort. This increment reused existing sources
and processing; it needed no new measurement system.

CTOV outposts are delivered through `c5c8c7a`, built from `07bcde5`. Twelve
biome roots form one outpost family; badlands and mesa definitions are exact
duplicates with the same start pool. All 78 CTOV registry entries are assigned
exactly once, across the prior 22 village groups and this outpost group. Missing
Savage & Ravage targets, several allay cages, dark-forest targets and mountain
towers pool remain attached to their variants. No retained outpost observations
exist. Forty-four focused tests and scoped quality checks passed; two builds
were identical and prior family records unchanged. Inventory SHA-256:
`bf3591f06e0c51ad963910d4ea75560d33a9fc33601e83e0b05c6f1744379722`.
Totals: 281 working groups, 542 assigned IDs, 345 unassigned. Continue remaining
providers, non-registry contributions, custom generators and required attributes.
CTOV registry assignment does not close missing-resource behavior, broader
village-family reconciliation or Item 8's final gate/review/main merge.

Repurposed design variants are delivered through `0555981`, built from `5022316`.
All 107 registry entries are assigned exactly once across 17 design groups.
Sixteen new groups preserve complete variant definitions, including generator,
height, burial, liquid, spawn-override and boundary differences. Eight mansions
and four monuments remain explicitly untraced custom paths. Namespace coverage
does not close their content, effective attributes or the final canonical gate.
Forty-three focused tests and scoped quality checks passed; two builds were
identical and all prior family records unchanged. The generated expansion is
isolated in its own commit and reuses existing evidence. Inventory SHA-256:
`909b0b9b7873581f6f36e97cca4a847637f94d3f2c3f2a07a3a0f42893323c33`.
Totals: 280 working groups, 530 assigned IDs, 357 unassigned. Retained observations
link to igloos, mineshafts, outposts, pyramids, ruins, shipwrecks and temples;
none link to the other new Repurposed groups. Continue remaining providers
(including IDAS, AdoraBuild, Towns & Towers and CTOV outposts), non-registry
contributions, custom generators and shared effective attributes. Preserve the
Nether pyramid's simultaneous LOWEST_LAND and search_for_highest_land fields
until code resolves their meaning. Final Item 8 gate/review/main merge remain open.

Repurposed witch huts are delivered through `fa401f2`, built from `c5f5dd6`.
Six biome/material roots share one family, common generation settings and
7 by 8 by 9 packaged template envelopes. Authored witches/cats remain distinct
from the piece-bounded spawn overrides; intended hostile encounter is supported
by both sources without asserting an observed population. No retained world
observations exist. Forty-two focused tests and scoped quality checks passed;
two builds were identical and earlier family records unchanged. Inventory SHA:
`5d36573d8314454c8663c139fe16c37ffdf04535eecc122787a96d989f34c7ba`.
Totals: 264 working groups, 429 assigned IDs, 458 unassigned; 101 Repurposed
roots remain. Continue Repurposed design variants and their custom generators,
other providers, non-registry contributions and shared effective attributes.
Eight Repurposed mansion definitions use custom generation without direct
start pools; do not pretend that the existing pool trace covers them. Final
canonical reconciliation, Item 8 attributes/gate/review/main merge remain open.

Voyager's remaining 64 roots are delivered through `dd2c364`, built from
`f4fdcc2`. All 129 runtime registry entries are assigned exactly once across
73 working groups. This completes namespace assignment, not canonical-family
reconciliation. Full generation settings and existing traces are bound by the
reused source check. Forty-one focused tests and scoped quality checks passed;
two builds were identical and all 199 earlier family records remained equal.
The large generated JSON expansion is isolated in its own commit because it
joins every remaining root to existing biome/template/world evidence. It adds
no evidence framework or measurement system. Inventory SHA-256:
`7ff1ac25e82012bd5b01b9c57a493e0930a4c669638cbc5c96aee8670ddad7d0`.
Totals: 263 working groups, 423 assigned IDs, 464 unassigned.

Reconcile the explicitly open Voyager relationships: boulder/stone_rock,
floating islands, ponds, camps and related house/ruin designs. Cathedral retains
`minecraft:mvs/cathedral_common` loot references requiring disposition. Large
warped tower retains two missing explicit spawner entity IDs; do not infer them.
Ocean tower uses OCEAN_FLOOR_WG and a maximum-Y allowance, so its generation step
does not establish surface exposure. Continue other providers and non-registry
contributions alongside shared effective attributes. Final canonical inventory,
required attributes, Item 8 gate, clean review and main merge remain open.

Voyager carts and igloos are delivered through `925a781`, built from `631cb1a`.
Six roots form two working groups. Carts preserve authored wandering traders,
SAVE markers and variant loot differences. Igloos preserve shared vanilla
villager pieces and the small igloo's explicit stray spawner in its lower piece.
These are packaged possibilities, not observed populations. Cart observations
187, 385, 584 and 765 are linked; neither igloo has retained observations.
Forty focused tests and scoped quality checks passed. Two builds were identical
and every prior family record stayed equal despite Git's textual diff alignment.
Inventory SHA-256:
`bbf81fb86557b271d964e271a77617a98838c6386d9d1c96f0c92cf37250bede`.
Totals: 199 working groups, 359 assigned IDs, 528 unassigned; 64 mvs roots remain.
Continue remaining Voyager roots, shared effective attributes, other providers
and non-registry contributions. Final canonical reconciliation, required
attributes, Item 8 gate, clean review and main merge remain open.

Voyager wells are delivered through `4f36c29`, built from `c4646fc`. Seventeen
roots form one working family with twenty templates, including upper/lower
components and alternative lower pieces. Full definitions preserve the Nether
generator and HIGHEST_LAND, rare-well terrain checks and each biome constraint.
Loot references remain attributed to their individual templates. The existing
version-aware trace selects the small tower's `1_21_4` path for Minecraft 1.21.1;
that path name is not an incompatibility finding. Twelve world observations
are linked. Thirty-nine focused tests and scoped quality checks passed; two
builds were byte-identical and earlier families unchanged. Inventory SHA-256:
`9565140a4d36dc9412c8e9a8fb24ba2311308642ffbe0d84532b52de86989a7b`.
Totals: 197 working groups, 353 assigned IDs, 534 unassigned; 70 mvs roots remain.
Continue remaining Voyager designs, including carts and igloos, shared effective
attributes, remaining providers and non-registry contributions. No additional
measurement system was needed. Item 8's final gate, review and main merge remain
open, as do canonical reconciliation and required effective attributes.

Voyager living trees are delivered through `a85bc74`, built from `7389ff9`.
Nine roots form one working family with fifteen alternative templates. Full
definitions retain biome differences and big oak's terrain range/radius checks;
big oak alone has a packaged loot reference. Approximate dimensions use the
existing template envelopes, explicitly including air/padding and rotation
limitations, not a new measurement system. World observations 92 and 495 remain
linked. Thirty-eight focused tests and scoped quality checks passed; two builds
were byte-identical and prior family records unchanged. Inventory SHA-256:
`163351577120afb31aaa850979a94cf907154a9b45875d19de9ac632fbb7d460`.
Totals: 196 working groups, 336 assigned IDs, 551 unassigned; 87 mvs roots remain.
Continue Voyager wells, carts and other designs, shared effective attributes,
remaining providers and non-registry contributions. Canonical reconciliation,
required attributes and the final Item 8 gate/review/main merge remain open.

Voyager stalls and End scraps are delivered through `0f0b9e9`, built from
`d077750`. Eight roots form two working families with their original template
sizes and loot differences preserved. End scrap variant 2 additionally uses
the mod's scrap loot table. Neither group has retained world observations.
Thirty-seven focused tests and scoped quality checks passed; reproduction was
byte-identical and prior family records remained equal. Inventory SHA-256:
`8909751d6e6079de9776ae8c866f9b04344a29ca1b9863275ce9a29df115d6e0`.
Totals: 195 working groups, 327 assigned IDs, 560 unassigned; 96 mvs roots remain.
Continue related Voyager designs and shared attribute resolution, then remaining
providers and non-registry contributions. User reiterated that an additional
measurement system is permitted only when strictly necessary and worth its
time and effort. These groups reuse existing catalogs and tests. No final
Item 8 gate, clean review or main merge is claimed.

Voyager dead trees are delivered through `7851498`, built from `0ce48c8`.
Eight roots form one working family with sixteen tree/trunk component templates.
Original definitions preserve mangrove's omitted liquid restriction. Validation
rejected the draft's no-markers claim: acacia, acacia_trunk and birch each have a
SAVE-mode structure block with empty metadata. The claim and source check were
corrected; processing of these markers remains unresolved. The initial focused
file run had 34 passes and one failure; both affected modular-variant cases
passed after the correction, with scoped quality checks clean. Reproduction was
byte-identical and all earlier family records remained equal. Four world
observations are linked. Inventory SHA-256:
`8fa79003674c71660161dadcf7adc7c2481f8e4ef12793adfcfb0ca77870ad45`.
Totals: 193 working groups, 319 assigned IDs, 568 unassigned; 104 mvs roots remain.
Continue remaining Voyager designs and attributes, then remaining providers.
No final Item 8 gate, review or main merge is claimed.

Voyager log piles and lanterns are delivered through `4396e1f`, built from
`12d4090`: six log-pile roots form one working family and eleven lantern roots
form another, with biome and template-size variants preserved. The existing
Moog variant check now serves both namespaces. Thirty-four focused tests and
scoped quality checks passed. Inventory reproduction was byte-identical and
prior families unchanged. Lantern observations 182, 410, 579 and 790 are linked;
no retained log-pile observations exist. Inventory SHA-256:
`afbf14517c724580bdeb08d7a923f7fbc273b3495f7c0ce81f83e2498e4b7bc7`.
Totals: 192 working groups, 311 assigned IDs, 576 unassigned; 112 mvs roots remain.
Next compare the eight dead trees and their trunk components. Mangrove omits
cannot_spawn_in_liquid, whereas the other seven explicitly set it true; preserve
that difference and use the already-retained generic codec evidence as needed.
Continue remaining providers and required attributes. No final Item 8 gate,
clean review or main merge is claimed.

All 52 mns registry entries are assigned through `d278fc7`, built from `5640516`.
The final 22 roots have explicit settings, resolved component traces and content
attribution. There are 28 working Nether design groups, not a final canonical
family total. Shared arena mob templates and fortress room alternatives remain
components. All prior family records stayed equal; reproduction was byte-identical.
Thirty-two focused tests and scoped quality checks passed. A wording correction
clarifies that the fortress's 196 reachable templates are alternatives, not a
claim that each assembly uses all of them. Several arena and fortress templates
contain spawner records with empty explicit entity IDs; those remain unresolved.
Inventory SHA-256: `c42e514859242a327fcc501a8edca380a9347b1ff79a4c6602d4b9b6ebc2c201`.
Totals: 190 working groups, 294 assigned registry IDs, 593 unassigned. Continue
remaining providers, including Moog Voyager, and shared attribute resolution.
Do not equate namespace assignment with canonical grouping, complete generation
coverage or finished per-family attributes. No final Item 8 gate/review/merge.

Ruin fragments are reconciled through `0f500c9`, built from `61d6501`.
The former `mns:very_small_ruins` working group is now `mns:ruin_fragments`,
covering thirteen registry IDs and twelve templates after adding six larger
wall, pillar and rubble variants. Identical definitions except start pools and
empty authored-content fields are source-checked; the duplicate root remains
explicit. Forty-eight retained observations are linked and qualified geometry
estimates updated. Thirty-one focused tests and scoped quality checks passed;
reproduction was byte-identical and unrelated groups remained unchanged.
Inventory SHA-256: `cab8caba7b568a35bbcc7ad3fbf7fa61fa7e8fe26b1eda231b8708e871021677`.
Totals: 168 working groups, 272 assigned IDs, 615 unassigned; 22 mns roots remain.
Continue the remaining Nether designs and shared behavior, then other providers.
Required attributes, canonical reconciliation and final Item 8 delivery remain
incomplete. No final gate, review or main merge is claimed.

Observed layout estimates are delivered through `be1171c`, built from `62be1ff`.
Inventory SHA-256:
`fc73778e20d09b91e4424b905995882c4c68469ac90c7c42c39cfdc5c3ea6109`.
The existing builder now reports qualified approximate X/Z envelopes and heights
for 25 working families with retained full-start-chunk observations. This uses
the existing bounds evidence, not a new measurement system. Paired X/Z values
preserve rotations; duplicates are removed. Partial start chunks are excluded
from these estimates, but their raw observations remain linked. Saved-piece
extents include air and padding, do not prove component chunks are populated,
and are not occupied dimensions or family-wide limits. The underground temple's
2 by 2 by 2 envelope remains visible rather than silently removing an unusual
observation. Existing explicit geometry overrides remain unchanged.
Thirty-one focused tests and scoped quality checks passed. The inventory
reproduced byte for byte; only the two geometry fields changed. Family counts
remain 168 working groups, 266 assigned IDs, 621 unassigned. Other required
attributes, provider coverage, canonical grouping and final delivery gates are
still open. User reiterated that new measurement systems are allowed only when
strictly necessary and worth their time and effort. Batch related source
inspection and resolve common behavior across consumers; avoid repeating small
research cycles or demanding occupied-voxel precision for approximate fields.

Medium Nether houses are delivered through `8d778dc`, built from `298911d`.
Inventory SHA-256:
`0b255191173f24467ac1fe8f337372e6d0ee08b4df1fd2e3cae8400fe242b088`.
Two roots form one working family; twelve retained observations are linked.
The joined output preserves three empty spawner entity objects in the first
template and two in the second as unresolved, alongside the first template's
explicit piglin spawner. Template-authored piglin/brute entities remain distinct
from spawner sources. Thirty focused tests and scoped quality checks passed;
the inventory reproduced byte for byte with prior families unchanged. Totals:
168 working groups, 266 assigned IDs, 621 unassigned; 28 mns roots remain open.

`37e0c78` extends the existing extractor by two class prefixes to inspect
GenericNetherJigsawStructure, its direction enum and YRangeAllowance.
`d3e8c20` retains the reproducible archive-scoped output in
`evidence/item-8/sources/moog-nether-generator-code`. The existing extractor
emits the superclass and pool codecs too; its complete identity manifest is
preserved without adding a filtering framework. This directly supports the
open Item 8 placement attributes for the Nether families. Scoped quality checks
passed and output matched the pilot. postLayoutAdjustments centers pieces,
selects fixed height or GeneralUtils highest/lowest land, applies offsets and
height bounds, then moves pieces. GeneralUtils terrain methods and inherited
layout behavior still need inspection before claiming complete placement.
Continue remaining Nether designs, provider coverage and attributes. Large and
warped house relationships remain undecided. No final Item 8 gate, clean review
or main merge is claimed.

Circular Nether ruins are delivered through `d62ade9`, built from `2ba75aa`.
Inventory SHA-256:
`f24fa7c214ee95359b1b2607cb14e097152653febad7da73b8291c893195a7d6`.
Two circle roots map to one working family with separate biome, geometry,
spawner and loot attribution. The joined output retains wither skeleton and
houses loot on blackstone, and piglin/brute spawners without packaged loot on
nether brick. Four retained observations are linked. Twenty-nine focused tests
and scoped quality checks passed; the inventory reproduced byte for byte and
prior families remained unchanged. Totals: 167 working groups, 264 assigned IDs,
623 unassigned; 30 mns roots remain unassigned. Continue houses, arenas and
remaining Nether designs, then other providers and required attributes. The
retained Moog JAR also contains GenericNetherJigsawStructure and its direction
enum, YRangeAllowance, and PieceLimitedJigsawManager; the existing disassembler
can be extended narrowly when resolving the already-open custom placement
attributes. No final gate, clean review, main merge or complete attributes are
claimed.

Nether well grouping is delivered through `2cb05ba`, built from `d320686`.
Inventory SHA-256:
`0b16127f113e6339b3095c7aaa31b1e9899c931cecaea64cf6ade639b6a9366c`.
Three well roots map to one working family, preserving the small lava well
without packaged loot and two medium variants with lower loot-bearing pieces.
The lower pieces are not counted as families. Seven retained world observations
are linked. Twenty-eight focused tests and scoped quality checks passed after
adding the repository-required type annotations to the new focused test.
Inventory reproduction was byte-identical and earlier groups stayed unchanged.
Current totals: 166 working groups, 262 assigned registry entries, 625 unassigned;
32 mns roots remain unassigned. Continue circles, houses, arenas and other Nether
design relationships, then remaining providers and required attributes. Circle
source inspection found distinct spawners and loot: blackstone has a wither
skeleton spawner and houses loot references; nether brick has piglin/brute
spawners and no packaged loot references. Their grouping remains undecided.
No custom generator behavior, full attribute completion, final Item 8 gate,
review or main merge is claimed.

Nether bridges and medium fungi are delivered through `541acfa`, with source
increments `70196ea` and `a49dbc8` and generated joins `d635337` and `541acfa`.
Current inventory SHA-256:
`11838c9dc3feb6b53c621ef49fc90e81182d063082b0900e448aa9e5e1c50e68`.
Six bridge shapes map to one working family. Four crimson/warped fungus shapes
map to one working family with explicit biome variants. Source-bound tests
verify common definitions, exact registry membership, individual template
sizes, resolved traces and absence of template-authored entities, loot,
spawners and generation markers. These absences do not establish effective
natural spawning or generator behavior. Bridge world observations 117 and 517,
and fungus observations 122 and 522, are linked from the retained bounds.
Twenty-seven focused tests and scoped Ruff/basedpyright checks passed. Both
joins reproduced byte for byte and preserved all prior families. Current totals:
165 working groups, 259 assigned registry entries, 628 unassigned; 35 mns roots
remain unassigned. Continue Nether wells, circles, houses, arenas and remaining
design relationships, then other providers and non-registry generation.
Canonical relationships and the required per-family attributes remain open.
No final Item 8 gate, report, review or main merge is claimed.

Very Small Nether Ruins grouping is delivered through `7e883a8`, built from
`cfe63fe`. Inventory SHA-256:
`53d6ea7bba9c7accdd3d4b075ad27fba5a50f3d530458555ac216d6c19ca98a6`.
Seven registry entries map to one working ruin family with six distinct
templates. The unnumbered `mns:very_small_nether_brick` definition exactly
duplicates `mns:very_small_blackstone`, including its start pool, and reaches
`mns:ruins/very_small_blackstone_1`. Both IDs remain for placement accounting;
the duplicate does not create another family or template. The direct source
check binds this finding, common definitions, variant dimensions and coverage.
Fourteen retained world observations are linked. Twenty-five focused tests and
scoped quality checks passed. The inventory reproduced byte for byte and prior
groups remained equal. Current totals: 163 working groups, 249 assigned entries,
638 unassigned. Forty-five mns roots remain unassigned. Continue their bridge,
fungus, well, arena and other design/variant relationships, then other providers
and required attributes. Relationships to larger ruins, effective custom Nether
placement and gameplay remain unresolved. No final gate, report, review or main
merge is claimed.

Soaring river grouping is delivered through `0c08c16`, built from `977b343`.
Inventory SHA-256: `d6c506ffc79c56888ae7ca2caa3120c9b611908275ec9467f778f48c4db659f9`.
All 35 mss registry entries map once to 27 working families. Birch and Cherry
River are biome/layout variants of one river landmark; original definitions and
template dimensions remain distinct. The source check binds the retained codec
false default for omitted cannot_spawn_in_liquid, preserves the omitted field
in Cherry River's definition, and verifies other definition differences are
limited to biome and pool. Neither river has a retained world observation.
Twenty-four focused tests and scoped quality checks passed after correcting an
unused-call-result warning in the test. Inventory reproduction was byte-identical
and prior groups remained equal. Current totals: 162 working groups, 242 assigned
registry entries and 645 unassigned. Continue remaining Moog namespaces mns/mvs,
other retained providers, non-registry relationships and required attributes.
Broader canonical relationships, effective placement and gameplay remain open;
no final gate, report, clean review or main merge is claimed.

Twenty-five non-tree, non-river Soaring designs are assigned by `1d47dc4` and
joined in `7efb67c`. Inventory SHA-256:
`8987fb9ff136039ca913d5f2732ede93d81b05abec850d12691cc3ce3b0ffed6`.
Current totals: 161 working groups, 240 assigned entries and 647 unassigned.
The test covers all singleton mss roots except the two rivers, preserves their
definition settings and verifies disjoint reachable template sets. These are
working design assignments; broader house/tower/landscape relationships remain
provisional. Twenty-three focused tests and scoped quality checks passed. The
inventory reproduced byte for byte and all earlier groups remained equal.

`d764903` extends the existing disassembler to the shared Moog generator and
enum. `2688751` preserves its full archive-scoped ten-class output and identities
under `evidence/item-8/sources/moog-generator-code`. Extraction reproduced its
pilot. The generator codec defaults omitted `cannot_spawn_in_liquid` to false,
resolving Cherry River's omission against Birch River's explicit false. Their
biome references and authored layouts still differ; river grouping and a direct
source-bound decision remain next work. Use the generator for other Moog custom
placement attribution as needed, without treating an option default as proof of
full runtime behavior. Continue remaining providers, non-registry generation and
required attributes. Item 8 still needs its final report/gate, clean review and
verified main merge. No runtime or tuning was performed.

Soaring Structures tree grouping is delivered through `91b4135`, built from
`3006f48`. Inventory SHA-256:
`69367cacd7678a253866695295b57e6a2c5184616952203d83b2fa4e4e855a3e`.
Eight `mss:tree_*` roots map to one tree-landmark family. Definitions are identical
except start pools; each pool selects its matching single template with empty
processors and fallback. Per-template dimensions preserve shape/size differences.
The source check also verifies no packaged entities, loot references, spawner
blocks or generation markers in these eight templates. This is not an effective
runtime spawn or loot claim. World observations 282, 411, 671 and 791 are linked.
Twenty-two focused tests and scoped quality checks passed. The inventory
reproduced byte for byte and previous groups remained equal. Totals are now
136 working groups, 215 assigned registry entries and 672 unassigned entries.
The other 27 mss roots remain unassigned. Continue their design/variant comparison,
remaining providers and required attributes. Frozen runtime custom placement,
occupied geometry, discoverability and non-registry generation remain open;
no final gate, report, review or main merge is claimed.

Mega Ship grouping is delivered through `4b4686f`, built from `2a2eeea`.
Inventory SHA-256: `6b545d5176bbdd6a8a26c50d770924dd9f277aa1eb094c90fc26c1c7fad6e728`.
All 25 mes registry entries now map once to 18 working families. Mega Ship is
one modular family with eight material, attachment and wreck variants. Full
per-variant definitions preserve distinct spawn overrides, height and terrain
settings. Common initial/middle/end module roles and bounds support grouping;
they do not prove identical occupied geometry or gameplay. Five airborne and
three wreck forms remain distinguished. Entity and loot references retain
template ownership. No Mega Ship has a retained Item 7 observation.
Twenty-one focused tests and scoped Ruff/basedpyright checks passed. The
inventory reproduced byte for byte and earlier groups remained unchanged.
Current totals: 135 working groups, 207 assigned registry entries, 680 unassigned.
Continue remaining Moog providers (mns, mss, mvs), other providers, non-registry
generation and required attributes. Effective custom placement, occupied size,
discoverability and gameplay attribution remain open. Item 8 has not passed its
final gate, report, clean review or verified main merge.

Seventeen non-Mega-Ship Moog End designs are assigned by `cf3083f` and joined
in `dad9743`. Inventory SHA-256:
`8a548b710b53676b3baf3850a005fa741770bd916339018dc0cb3333eeb28d5b`.
Current coverage is 134 working groups, 199 assigned entries and 688 unassigned.
The eight `mes:mega_ship*` roots remain unassigned pending material, layout and
wreck variant comparison. Other mes roots have disjoint reachable templates;
spike, scrap, monolith, prairie and pillar alternatives remain grouped.
Custom terrain-height declarations are recorded without claiming effective
placement. Starlight Voyager joins world observations 242 and 632; the other
sixteen designs have no observations in the retained sample, not proof of
absence. Twenty focused tests passed and the inventory reproduced byte for byte
without changing previous groups. Scoped Ruff and basedpyright now pass.

Quality-check correction: the prior Spider Dungeon line-length fix introduced
implicit string concatenation rejected by basedpyright. `719aef7` changed it to
explicit concatenation, which conflicted with Ruff. `5ee73d6` resolved both with
a short component reference, and its direct test passed. Earlier assertions of
all final scoped checks passing for that expression were overstated. The Moog
coverage test also exceeded the complexity threshold initially; replacing its
two exclusion branches with the existing local prefix mapping resolved that
without adding a helper or framework. Continue Mega Ship grouping, remaining
providers, non-registry relationships and attributes. Item 8 remains incomplete;
no final report/gate, clean review or main merge is claimed.

Spider Dungeon source attributes are delivered through `979b60d`, built from
`0cb388e`. Inventory SHA-256:
`c4c0ff970dac5e72b4a382dab3283a8925d2b344cd438ed9f5b5f0aedeaa9e4a`.
The family now records tunnel/nest/egg-room component relationships, authored
spider and cave-spider spawner sources, the egg-room chest table, the separate
natural-spawn override, hostile intent and underground generation designation.
Source identities and direct checks bind these claims. Nineteen focused tests
and scoped quality checks passed; the inventory reproduced byte for byte with
only the Spider Dungeon family changed. Counts, occupied dimensions, visual
discoverability and effective loot integration remain unresolved. Registry
coverage is unchanged at 117 working groups, 182 assigned entries and 705
unassigned entries. Continue remaining providers, non-registry generation and
required attributes; final gate, report, clean review and main merge remain open.

Remaining registered YUNG roots are assigned by `d8a3b93` and joined in
`548e338`. Inventory SHA-256:
`62d3eeb923216554112386152a174abfa5a71c132b01a6839ece0a09175db620`.
Current totals are 117 working groups, 182 assigned entries and 705 unassigned.
Eighteen focused grouping tests and scoped quality checks passed. The inventory
reproduced byte for byte and prior groups remained equal. Missing Zombie Dungeon
and fortress templates and the Stronghold spiral-stairs pool remain explicit.
This covers registered roots only, not YUNG Bridges/Extras feature generation.

`d7c955f` extends the existing disassembler for seven Better Dungeons custom
classes; `3d16811` retains the reproducible text under
`evidence/item-8/sources/betterdungeons-code`. Its README records commands and
source findings. Spider Dungeon starts with BigTunnel and constructs tunnel,
nest and egg-room components. Nest code places cave-spider spawners; EggRoom
code branches between its loot-table chest and a spider spawner. These findings
still need source-bound family attribute decisions and direct checks. Do not
infer generated counts or unconditional placement. Small Nether Dungeon checks
an enabled config before its custom placement path; effective configuration and
assembly remain to be attributed. Continue required attributes and remaining
provider/non-registry coverage. No runtime was launched, no baseline was tuned,
and the Item 8 exit gate, report, review and verified main merge remain open.

Explorify root mapping is delivered through `fe80f07`, built from `de8bac8`.
Inventory SHA-256: `d2a5c7df744e7c96cbadc4da794a3990d6ba67c41c7c410520b09df9063daf8e`.
`3e75d3e` and `0fc3bb1` assign and join eleven independent authored designs.
`de8bac8` consolidates twelve guide-post, supply-cache and watchtower biome
entries into three groups. Source definitions, template dimensions, loot
differences and exact coverage of all 23 Explorify registry entries are tested.
Eleven focused grouping tests and scoped Ruff/basedpyright checks pass. Initial
test typing and assertion-style failures were corrected before delivery.
Both generated increments reproduced byte for byte and preserved earlier groups.
Current totals are 105 working groups, 170 assigned registry entries and 717
unassigned entries. These are not a final canonical family count. Continue the
remaining providers, non-registry generation relationships and required family
attributes. The final gate, report, clean final review and verified main merge
remain open. No runtime was launched and the frozen baseline was not modified.

Current inventory is delivered through `85111fd`, built from `fd9705a`.
SHA-256: `83f56c9ecaa8f76f853ffd0081a12537849489e4a30dea3edae099caf298250d`.
`3b4f770` and `2f1dbda` parse and attribute ordinary/trial spawner base entity
sources; `6a19784` delivers their inventory output. Modes and source templates
remain distinct, missing/custom cases retain source paths, and generation
markers remain separate. Sixteen focused parser/assembly checks passed and the
output reproduced exactly. No default entities or generated counts are inferred.
`fd9705a` assigns all ten Explorations roots, including Slime Cave's explicit
custom-generation gap and Underground Temple's two missing templates. Variants
and components remain grouped. Nine focused grouping checks and scoped quality
checks passed; the generated join reproduced its pilot exactly. The current
unassigned registry list has 740 entries; this is not a canonical family count.
Continue remaining provider coverage and required attributes. Custom Slime Cave
and Underground Temple generation need source inspection despite existing Item 7
observations. Raw registry custody remains verified under the existing release.
The full gate, final report, clean final review and verified merge remain open.

Current inventory is delivered through `2882825`, using source `729ccdd`.
SHA-256: `6b2d8684f03af14ddd095b2c8a42c6c88bafa93f18e8f4ce8eade8f6ce355f32`.
`1c92c0a` delivers compact packaged loot field/value attribution with source
templates, built by `a590403`. `2882825` adds authored entity base IDs and source
templates, including passengers and explicit unresolved entity records. Exact
NBT paths remain in the existing content trace. Eight focused tests and scoped
quality checks passed; both outputs reproduced their pilots byte for byte.
Existing explicit family attribute decisions remain intact. These source lists
do not assert effective loot, spawn success, enemy classification or populations.
Continue spawner/marker and natural-spawn attribution, other required attributes
and remaining provider coverage. Raw registry custody remains verified. The
complete inventory, final report/gate, clean final review and verified merge
remain required by the active goal.

Loot attribution scope reassessment: the first `136ee84` output duplicated
over thirteen thousand source-reference lines in the inventory. That is larger
than Item 8's loot-source requirement needs. Keep exact NBT paths in the existing
content trace and summarize distinct field/value pairs with source-template
owners in the inventory. Preserve list-valued references and distinguish
container LootTable from entity DeathLootTable. This direct change in the existing
builder avoids another evidence class or framework. The detailed pilot and its
reproduction remain local historical outputs, not accepted inventory artifacts.

WDA root coverage is now delivered through `380e572`, using source decisions
from `559edc0`, `d20b0c6`, `007d1f9` and `6540055`. All forty registered WDA
layouts are assigned once. The existing authored-design test now covers WDA
and Integrated Villages, with full namespace coverage for both. For WDA it
also verifies disjoint reachable template sets across the complete namespace.
Start pools, placement settings and missing components are source-bound.
Seven focused tests and scoped quality checks passed. The generated inventory
reproduced its pilot byte for byte. Current inventory SHA-256:
`cfe53234f8bed18b3f494b16de318cd2c95c3dc875e54c3a520a196477a9d83d`.
The large generated join was isolated from implementation changes. Root coverage
does not resolve effective placement or remaining required attributes. Continue
remaining providers and attribute attribution using the existing source catalogs,
template content and world observations. Raw registry custody remains verified
under the existing r1 release; no new runtime or archive was needed for WDA.
Final inventory coverage, report, full gate, clean review and verified merge
remain outstanding. Do not advance Items 9 through 11.

Current inventory is delivered through `376e8e6`, built from `585de70`.
SHA-256: `abb98a78d9d0fa1deb465dfc8a4db4f2c2e6555a937b515b085597e16a55c3e1`.
All twelve Integrated Villages registered designs now have working groups,
distinct start pools, declared generation constraints and missing components.
Broader village-family relationships and gameplay attributes remain open.
Six focused tests and scoped quality checks passed; output reproduced exactly.
WDA root inspection has begun but no WDA grouping decision is delivered yet.

Registry raw durability is now resolved through `63cb1f8`. This archive was
required by the existing evidence gate to preserve the previously local logs,
configuration and source metadata. It reuses the existing archive and restore
CLI and unchanged schema; no new framework or runtime experiment was added.
Release/tag `item-8-registry-raw-2026-09-05-r1` binds custody revision `376e8e6`.
Archive `item8-registry-r1-376e8e6.tar.gz`, SHA-256
`03f60f97ba2d22f6ae86b600a1cf0d267896209254493e2730cc2f814f1d3645`,
contains 241 files and is 603232 bytes. Local and downloaded restores verified
all files; the world-context projection reproduced from downloaded level.dat.
Use `evidence/item-8/raw-custody/README.md` for retrieval commands and receipts.
This supersedes older registry raw-delivery-pending statements below. It does
not close family coverage, required attributes, final gate, review or merge.
Continue those requirements using the existing inventory and source catalogs.

Inventory work is delivered through `451e5ce`, using decisions from `93d526c`.
Current inventory SHA-256:
`2df2e12859eb6baacd304205a24e8f0506c4b1adbef63637e0398fd43296bf3f`.
`7100c21` and `bddaba7` deliver Seven Seas main hull extents, authored spawner
types, loot references and ocean-surface setup, retaining all effective-world
limitations. Source checks caught and corrected an omitted Victory Frigate
skeleton entry. `5629b2b` and `f1fa7d1` preserve the pinned Minecraft missing
template lookup and attachment paths: a missing template becomes empty and has
no connectors. This is base code evidence, not proof of post-transform runtime
behavior or a miss probability. Do not modify the frozen baseline to repair it.
Integrated Stronghold is now one family with connected room components, its
piece-bound natural silverfish/enderman spawn override, and packaged Y=15 start.
Two missing armory templates remain explicit. Five focused tests and scoped
quality checks passed; each inventory update reproduced its pilot byte for byte.
Continue remaining provider grouping and attributes in the existing inventory.
Integrated Stronghold's authored content, processors, replacement relationship,
occupied size and visibility are still open. The current Item 7 start subset
contains no observation for it. Raw durability, complete coverage and attributes,
final report and gate, clean final Codex review and verified main merge remain
required. No Item 8 completion is claimed and no server process is running.

Inventory work is delivered through `787523b`. `bf153ea` lets source-bound
attribute decisions populate the existing inventory while protecting membership,
observation references and incomplete status. `e6704a7` records Better
Mineshafts hostile-room intent, cave-spider/zombie-villager spawner paths, base
loot constant, authored/natural distinction and underground generation setup.
Effective injections, occupied size and surface visibility remain unresolved.
`eef10dd` enumerates all five Seven Seas vessel roots with distinct main hulls
and start pools; spawner components are not extra families. Four focused tests
passed and updated inventory runs reproduced byte for byte. Current inventory
SHA-256: `3a53d5cf7e64251d08f1d52408d27f4666fb72798ab5fb526afefd421199f8d9`.
The existing trace preserves Small Yacht's missing `small_yacht_spawner_3`
template. Resolve that source gap and continue vessel attributes using the
main hull, spawner and loot records. None of the five has an observation in
the current Item 7 structure-start subset. The working inventory remains
incomplete. Raw delivery, remaining providers/attributes, final report and gate,
clean review and verified merge are still outstanding. No runtime is running.

The working inventory deliverable now exists at `evidence/item-8/inventory.json`,
delivered by `1c9c3a1`, built with `f2eaf2b`. It is explicitly incomplete and
lists unassigned registry IDs, unresolved non-registry content and unknown
attributes. SHA-256:
`58a200ca9ad7809f807cb73b6e3e72aed4cd1e1a9107723c9fcaa1640c62652d`.
Source `cbbfd01` consolidates CTOV's 66 village size entries into 22 proven
size groups in `family-decisions.json`; broader relationships between different
village designs remain unresolved before any canonical total. The inventory
joins these groups and Better Mineshafts to current biome constraints, potential
template content and Item 7 world observations. Three focused tests and scoped
quality checks passed; committed-source output reproduced its pilot exactly.
Use the existing builder and deliverable for further family/attribute work.
Do not interpret field presence, content references or piece envelopes as
resolved effective attributes. The final report, raw durability, full gate,
clean Codex review and verified merge are still outstanding. The goal remains
active with no blocker or completion claim.

Content attribution is now delivered by `2de3c84`. Current trace artifact:
`evidence/item-8/sources/pool-traces-content.json.gz`, SHA-256
`facb6f7bbafb6836e7eaa694535b975c2ee2deab1e36ab85930f1c11c7a471c8`.
Source `333f1d4` extends the existing trace with reachable-template content;
`2d62944` indexes authored entities/passengers, spawner NBT, generation markers
and loot references without asserting processing or placement. Six focused
tests and scoped quality checks passed, and committed-source output reproduced
the pilot byte for byte. Empty authored entity compounds remain explicit
unresolved rows, including the observed Moog mineshaft stable case documented
in the source README. Prior alias-only output remains historical and requires
its original source for reproduction. Use the new content trace to assemble
the required family mob/spawner/loot attributes, together with source spawn
overrides, custom generator code and effective processors. No complete family
inventory, Item 8 gate pass, PR review or merge is claimed. Raw durability and
all remaining family attributes are still required by the active goal.

Biome integration is now delivered through `c468308`. Source `e22815d` derives
Supplementaries' two tags from frozen parent/leaf toggles and inspected code.
Sources `71ee444` and `60c1ed1` resolve the seven competing vanilla biome tags
using the original runtime debug log's final expanded sorting record, line
17812, rather than JAR-name order. The existing structure input index retains
the exact record, its raw hash, and the Item 3 metadata-bound archive mapping.
It now resolves source-derived constraints for 884 of 887 registry IDs; the
three IDAS lumber-camp missing tags remain explicit. Ten focused tests and
scoped quality checks passed. Both dynamic-tag and pack-order outputs reproduced
their pilots byte for byte. Current structure-input SHA-256:
`fcd9e53c1802b8ab2f03785baacce7a032ae525446f24e1172dbdeee868367ef`.
Rebuilding now also needs the preserved original registry `debug.log`, whose
identity and command are recorded in the source README. Raw durability remains
pending. This resolves biome source questions, not dimension eligibility,
generation status, the remaining family attributes, or Item 8 completion.
Continue the canonical provider/family inventory and required attributes using
the existing catalogs, custom-generation inspection and Item 7 observations.
No new runtime experiment, schema or evidence class was added for this fix.
The active goal still requires the full local gate, durable evidence, clean
final Codex review, nonsquash merge and verified `origin/main` delivery.

Supplementaries' missing packaged tag source is now identified and preserved in
`evidence/item-8/sources/supplementaries-tags-code`. Inspector source `5a5f752`
records the dynamic generator, tag names and feature-supplier/config bindings.
The output reproduced byte for byte. Enabled road signs add `#minecraft:is_overworld`
to `supplementaries:has_road_signs`; enabled galleons add `#minecraft:is_ocean`
to `supplementaries:has_galleons`. Feature suppliers also AND parent toggles.
The saved runtime enables `supplementaries:generated_pack`. The source README
records the frozen config hash and exact paths. Next, integrate these derived
contributions into the existing biome input path with code/config provenance;
the current structure-input artifact still reports them as missing packaged tags.
Do not interpret that static absence as disabled generation. Item 8 remains open.

Structure biome constraints are now generated by `0be5021` in the existing
`structure-inputs.json`. All 887 registry IDs have rows, with 825 packaged
constraints resolved against the captured biome registry. Every Better
Mineshafts variant resolves. Null rows retain missing required references or
reachable unresolved tag contributions. Supplementaries' two missing packaged
tags require checking dynamic construction; they are not automatically disabled.
The three IDAS lumber-camp tag failures remain. Several vanilla, CTOV, WDA and
Explorify constraints need mod replacement order. Ten focused tests and scoped
quality checks passed; output reproduced byte for byte. Source-derived biome
constraints do not prove dimension eligibility or observed generation. Continue
family attributes and the remaining provider inventory; Item 8 remains incomplete.

Biome tag contribution indexing is now delivered by source `0ab3718` in the
existing `evidence/item-8/sources/structure-inputs.json`. The `biome_tags` field
preserves source references, deterministic additive/vanilla-to-single-mod
merges, and explicit unresolved conditions, removals, non-root packs or unknown
replacement order. The output reproduced byte for byte; seven focused inventory
and tag-merge tests and scoped quality checks passed. Use these inputs with the
runtime-aware resolver, propagating any reachable unresolved contribution even
when its reference is optional. Do not interpret null merged values as absence.
Final family-level constraints and the overall Item 8 gate remain incomplete.

Biome resolution increment: `3bc5d96` exposes the existing Item 7 tag resolver as
`resolve_biome_tag` with optional `registered_biomes` filtering. Item 7's default
packaged-reference behavior is unchanged. With a runtime registry supplied,
absent optional biome IDs are excluded, absent required IDs remain explicit
failures, and invalid nested tags do not contribute partial contents. Seven
focused restriction/resolution tests and scoped Ruff/basedpyright checks passed.
This is reusable calculation code, not a completed effective-biome artifact.
Resolve tag contributions, conditions and pack precedence before applying it to
the full family inventory; do not equate the old packaged restriction audit with
runtime biome membership.

Better Mineshafts grouping is now recorded in
`evidence/item-8/family-decisions.json`: its 13 retained structure IDs belong to
one specialized-generator family with biome/material/decoration/support variants.
Vanilla normal and mesa mineshafts remain separate from this family and carry
the previously derived suppressed-generation distinction. The focused family
test verifies exact namespace coverage, definition commonality, source hashes
and disassembly identities. The test and scoped quality checks passed.
This is the grouping decision only. Complete the family's outstanding attributes
and the other providers before any Item 8 gate or canonical total is claimed.

Vanilla mineshaft suppression follow-up: source `9669fb1` extends the existing
inspector with annotated mixin disassembly and exact loader/mixin declarations.
The updated `sources/mineshafts-code` evidence demonstrates that the frozen
disable setting causes the head injection into `ChunkGenerator.tryGenerateStructure`
to return false for vanilla `StructureType.MINESHAFT`. Treat the vanilla normal
and mesa IDs as registered but suppressed in normal generation on this
source-and-configuration basis, not as independently observed callback runs.
The separate locate warning only checks the direct normal-mineshaft ID.
Portable extraction reproduced byte for byte and scoped quality checks passed.
The source README now supersedes the earlier uninspected-hook statement below.
Continue with canonical grouping and outstanding attributes; Item 8 is not closed.

Latest custom-generation evidence: `b4b38e0` delivers
`evidence/item-8/sources/mineshafts-code`, generated with `c51973c` and reproduced
byte for byte. The existing inspector now accepts `--archive` and selects Better
Mineshafts world-generation/configuration classes. Source proves code-authored
cave-spider and zombie-villager spawners and abandoned-mineshaft loot references.
It also exposes an important size limitation: the initial VerticalEntrance box
uses maximum build height. Do not promote its saved box height to occupied
structure height. The evidence README records findings and remaining work.
The actual vanilla-replacement hook is still uninspected; the retained JAR has
`DisableVanillaMineshaftsMixin` and `LocateVanillaMineshaftCommandMixin` for that
follow-up. Family grouping and final attributes remain incomplete. No runtime
process is live, and no Item 8 completion or review is claimed.

Latest delivered trace correction: `fba2e84` retains
`evidence/item-8/sources/pool-traces-aliases.json.gz`. Use it instead of the
preserved first `pool-traces.json.gz`. Implementation `dc96708` follows declared
positive-weight alias alternatives, keeps alias IDs separate from actual pools,
and preserves original weighted groups without claiming joint occurrence.
Trial Chambers' four alias references now resolve to its declared spawner
templates. Focused tests and scoped quality checks passed; committed-source
output reproduced the pilot byte for byte. The remaining custom-generation and
missing-resource cases still require disposition before final family attributes.

Later delivered increment: `1d2659e` adds
`evidence/item-8/sources/world-bounds.json.gz`. It contains 792 saved structure
starts from the eight hash-verified Item 7 r14 decoded streams. Every piece box,
inclusive envelope, source line, seed, run and chunk status is retained. The
extraction command in `bf623f1` reproduced the pilot byte for byte. Calculation
tests and scoped Ruff/basedpyright passed. Use this artifact to bind observed
family dimensions; it does not prove full placement of every intersecting chunk
or global size limits. No new server experiment was needed. Pool aliases and
custom-generation contents remain unresolved; proceed with their source
inspection and the actual family inventory, not another evidence framework.

Item 8 remains IN PROGRESS on `codex/item-8-completion`. Selected resource
precedence is implemented in `b135beb`; it preserves known vanilla replacements
and unresolved optional-pack exclusions. Pool tracing is implemented in
`9fae9cf` and its frozen-input command in `f9fb51f`.
`evidence/item-8/sources/pool-traces.json.gz` was reproduced byte for byte and
records 818 direct start-pool traces plus 69 explicit custom-generation cases.
These are registry entries, not canonical families. The source README records
identities, reproduction and limitations. Focused tracing tests, Ruff and
basedpyright passed. No server or extraction process is running.

Next: resolve aliases, custom generation and dynamic injection in the existing
inventory path; retain unresolved optional references until their activation is
proved. Bind Item 7 actual generated-world bounds and observations, then complete
canonical families and all Item 8 attributes. Runtime raw log/configuration and
level.dat durability remains outstanding. No local exit gate, clean final Codex
review, pull request merge or Item 8 completion is claimed. The Item 7 review
exception remains specific to Item 7. Do not begin Items 9, 10 or 11.

### Item 8 implementation checkpoint

Latest delivered state: `34fceec4566223c2d5f869955d1a84fdac00a546` on
`codex/item-8-completion`. The privacy correction described below is delivered:
the current JSON and template catalogs are
`evidence/item-8/sources/packaged-json-redacted.json.gz` and
`evidence/item-8/sources/templates-redacted.json.gz`. The original JSON catalog
was removed from the current tree, with history preserved. Source hashes and
omitted-field paths remain explicit. The source README records reproduction.
`structure-inputs.json` now binds to the redacted JSON artifact. Its builder
preserves all 887 runtime IDs, candidate definitions and packaged placement sets,
plus 22 source-proven CTOV size-variant groups. None of these counts is a final
canonical family count. No extraction process remains running. Continue with
effective-resource resolution, pool/template relationships and source-backed
family attributes, plus remaining runtime log/configuration custody.

Later continuation: the template pilot completed with exit zero. Its output is
`evidence/raw/item8/templates-pilot1.json.gz`, SHA-256
`9ffec196748525b0dc115a57e8141a67755e6c9d66ce056fbca667d8cb8ff3c0`.
Do not restart or poll its old process as live. The output is not publishable as
is: packaged templates contain authored profile/owner UUIDs and password fields.
The delivered JSON catalog also contains three authored profile components.
AGENTS.md's prohibition on player UUIDs requires a narrow correction to these
derived catalogs before further acceptance. This concrete publication boundary
cannot be fixed by family grouping or existing configuration-secret redaction.
Use `tools.redact_item8_catalog` to preserve original archive/member identities,
record omitted field paths, and emit publishable derivatives. Keep original raw
catalogs outside ordinary Git. Correct the delivered JSON artifact and its index
bindings without rewriting existing Git history. This is a privacy correction,
not another runtime experiment or a new family acceptance gate.

This checkpoint supersedes the older branch and `READY, not started` statements
below. Item 8 is IN PROGRESS on `codex/item-8-completion`, delivered through
`0315f21629843e1fe5eae93eafb3e26f6702819f`. No Item 8 completion gate or review is
claimed. The user-authorized Item 7 review exception below remains unchanged.

- The exact retained-136 registry capture completed under source `367ba59`.
  Seven registry dumps and the original receipt are committed under
  `evidence/item-8/runtime/registry-r1`. They contain 887 structure registry IDs,
  not an accepted family count. Full logs and configuration still require durable
  delivery from `evidence/raw/item8/registry-r1` before closure.
- The packaged JSON catalog and reproduction instructions are committed under
  `evidence/item-8/sources`. Competing definitions and optional-pack paths remain
  separate. The empty CTOV process-list tag remains an explicit parse failure.
- Source `4cb8ce5` extends the same extractor to template NBT, preserving size,
  palettes, block-state counts, block entity NBT, and authored entities. Its 27
  Item 8 tests passed. Scoped Ruff and basedpyright passed. Re-extraction of the
  JSON catalog remained byte-identical to the committed artifact.
- Template pilot command: `uv run -m tools.extract_item8_sources --kind template
  --output evidence/raw/item8/templates-pilot1.json.gz`. The pilot was started
  before the equivalent implementation was committed. At this checkpoint its
  exec session `97479` and process `627414` are live, with log at
  `evidence/raw/item8/templates-pilot1.log`. Poll the existing session or inspect
  that process before deciding whether it terminated. Do not restart because an
  observation call times out. No template output has been accepted yet.
- Remaining: finish template extraction; deliver full runtime custody; resolve
  runtime resources, variants, replacements, injected buildings and feature-based
  structures into canonical families; bind Item 7 generated-world observations;
  complete every Item 8 attribute; validate the full gate; complete a clean final
  Codex PR review loop and verified nonsquash merge. No Item 9, 10, or 11 work.

### User-authorized Item 8 continuation

The user explicitly authorized proceeding to Item 8 after being informed that GitHub does not show a final clean Codex review of Item 7's merged head. This is a user-authorized exception to the review prerequisite for the already delivered Item 7, not evidence that the missing review occurred. Item 7's completion receipt was rebuilt byte for byte and its 210 tests passed during the continuation audit. Preserve its accepted r14 evidence without another custody revision. The earlier statement below that no review work remains must be read with this explicit exception.

Item 8 is now authorized. Its end-to-end goal includes the complete specification inventory, reproducible evidence, atomic delivery, a completed clean Codex review cycle covering its final changes, and verified merge into `main`. The Item 7 exception does not apply to Item 8. Do not mark Item 8 complete from tests, a merge, an older review, or documentation alone.

### Item 7 scope-control incident

Item 7 exceeded the intended completion-efficiency boundary during repeated r10 and r11 review repair. A real flush-correlation defect required a narrow empirical replacement, but locally defensible validators, receipts, custody revisions, and repeat checks accumulated without a hard comparison against the smallest `SPECS.md` exit gate. Do not repeat that pattern. Treat scope growth itself as blocking: before adding any new evidence class, schema, receipt, validator, archive revision, review framework, or broader regression surface, prove that the demonstrated defect cannot be fixed inside the existing path and record the reason here. Otherwise reject the addition.

Item 7 is complete. PR #15 merged accepted branch head `a57a00cf59005f59ad4694e3c1b0c6acc644754e` into `main` as merge commit `a0f2fc275d2e72081ee5a9200e8309f0e3e720a0`, and `origin/main` was fetched and verified to contain that head. No Item 7 review, custody, release, or merge work remains. The r14 release is retained raw evidence, not the repository completion boundary; the verified merge commit is the completion boundary. Do not create r15 or reopen Item 7 merely because the later completion-validator correction is not contained in the raw-evidence tag. The first r12 recovery attempt remains rejected: concurrent servers collided on the configured port, one completed flush was killed by the runner's post-stop process timeout, and interruption left child process groups alive until explicitly terminated.

This section supersedes the dated status and restart instructions below. Preserve the rest of this file as recovery history. `SPECS.md` remains the dependency-ordered requirements authority, and `Adventure-Engineering-Pack-Execution-Ledger.md` remains the status and evidence vocabulary authority.

### Git and delivery state

- `origin/main` contains verified Item 7 merge commit `a0f2fc275d2e72081ee5a9200e8309f0e3e720a0`. The active branch is `experiment/item-8-structure-inventory`, created directly from that verified ref. No Item 8 implementation or evidence change has been made.
- PR #11 merged Item 5 delivery as `398bf59b3a89669ec402026d52250c2b86e54047`.
- PR #12 merged the initial Item 6 generated-default capture as `895ed1d999cd22ca511035e666ad8ac308ae63c1`.
- PR #14 merged the completed Item 6 audit as `f38ea66ecc28911c33d525dcde26434853673ad3`. Its final Codex review completed against `96a914c8a457d2f23698cdaeba18c6ed899b56d1` and reported no major issues. The GitHub API currently exposes no thumbs-up reaction on that cycle, so do not claim that reaction; preserve this as a review-record discrepancy unless later evidence resolves it.
- `eb84d842a7b108863dcdd4c86435a875f8a0c575` only renamed `CLAUDE.md` to `AGENTS.md` after the Item 6 merge.
- PR #15 is merged. Its accepted head is `a57a00cf59005f59ad4694e3c1b0c6acc644754e`, and its merge commit is `a0f2fc275d2e72081ee5a9200e8309f0e3e720a0`.
- The retained Item 7 raw-evidence release is `https://github.com/copeugne/mcpack/releases/tag/item-7-raw-evidence-2026-09-04-r14`. Annotated tag object `4b5fefe4a58f310bbd47796772520e6d3288f480` resolves to raw-evidence producer revision `4497b3f650990f501b594b82e933c40eaf5540ac`. All four assets restored successfully and one fresh complete remote download matched every committed size and SHA-256. The later completion-validator correction is committed in the merged branch and does not alter those raw bytes, manifests, restores, or publication.
- Historical rejected reviews and custody attempts remain under `evidence/item-7/review/`. They are failure history, not active continuation work.
- Preserve the existing untracked `.codegraph`, `.omo/`, and `mcpack-reconstructed-28(1).bundle` paths. Committed evidence belongs under `evidence/`; acceptance-relevant source, tools, tests, and exact commands must remain tracked for reproduction.

### Current gate status

| Item | Current status | Evidence-bound meaning |
|---:|---|---|
| 1 | `COMPLETE` | The design contract and Earned Sandbox Freedom Doctrine remain binding. |
| 2 | `COMPLETE` | Reconstructed baseline evidence, clean-room proof, durable retrieval, and Git receipts pass. |
| 3 | `COMPLETE` | All 190 candidates have dispositions; the exact 136-candidate retained dedicated-server set passed its scoped static and lifecycle gate. |
| 4 | `COMPLETE` | The isolated four-seed environment and backup/restore gate pass. |
| 5 | `COMPLETE` | The versioned measurement protocol, strict evidence tooling, and pinned-Temurin pilot gate pass. Spark overhead remains `UNKNOWN`, and the pilot is not a performance baseline. |
| 6 | `COMPLETE` | The untouched retained-stack configuration is frozen and audited. The manifest contains 228 paths, with 88 audited and 140 explicitly out of scope. No tuning was performed. |
| 7 | `COMPLETE` | The exit gate, retained raw evidence, source-bound recovery, completion receipt, merged PR #15, and delivered `origin/main` ref are verified. |
| 8 | `READY`, not started | The Item 7 dependency is satisfied. Branch `experiment/item-8-structure-inventory` exists at the verified merge commit, but no Item 8 implementation or evidence work has begun. |
| 9 | `BLOCKED` by Item 8 | Reclassify every verified family exactly once only after Item 8 passes. |
| 10 | `BLOCKED` by Items 7 through 9 | Regenerate and preserve predeclared density evidence only after the preceding gates pass. |
| 11 | `BLOCKED` | Do not implement, run, repair, or lint Item 11 before the final Items 2 through 10 audit passes. It also requires at least two blind human operators. |

The Item 7 completion command returns `PASS` and records 138 exact artifacts in `evidence/item-7/completion.json`, whose SHA-256 is `0ef7c83438ab2a2cfe67eadc858e806ada9c9eecc213d883649ae3e8493cb1d3`. The world archive inventory binds 716 files at SHA-256 `7907bfd705bb8b1b7e794133e634e59ba1d3a694210353da65193eff7dd79027`. The source-bound v3 save audit covers all 12 archived worlds and has SHA-256 `087ebb0a5b019fb5138fd6975598176c07495eb81954f0d4bc4ce524502893b3`. Final validation passed with 210 Item 7 tests, 891 repository tests, clean static checks, and byte-identical save-audit and completion rebuilds. PR #15 and delivered-ref verification are complete.

### Exact continuation point

1. Treat `evidence/item-7/completion.json` and `docs/items/Item-7-Baseline-Worldgen-Audit.md` as the current acceptance summary. The former zero-mod report is superseded historical context.
2. Preserve the measured semantic nondeterminism. Run A and Run B differ outside the central End; input drift and comparator artifacts were refuted, but the causal provider remains `UNKNOWN`. Do not tune the frozen Item 6 configuration inside Item 7.
3. Preserve the confirmed Better Caves generation failure, the unresolved YUNG's Bridges and YUNG's Extras identifiers, and the 1,166 unresolved warning signatures as downstream work. Do not infer compatibility from server readiness.
4. Do not reopen Item 7 or create another custody revision without new evidence that invalidates its explicit exit gate.
5. Item 8 continuation is explicitly authorized under the checkpoint above.
6. Item 8 must combine verified runtime registries, packaged data, configuration evidence, logs, and generated-world observations. It must resolve canonical families without double-counting aliases, pieces, pools, or templates, and it must carry Item 7 run identity and unknowns forward.

Recovery Gate R-1 remains open for Items 8 through 10 and their final cross-item audit after Item 7 delivery completes.

**Prepared:** 2026-09-01
**Live checkpoint updated:** 2026-09-01
**Canonical repository:** `https://github.com/copeugne/mcpack`
**Verified remote branch:** `main`
**Verified remote HEAD before this handoff commit:** `3d1f33551700c9804503d0e27edddce35ea285c4`
**Verified commit count before this handoff commit:** 41
**Primary status:** Item 2 is complete and published. Item 3 is incomplete and stopped after exact acquisition plus top-level and embedded-JAR inspection. Items 4–10 have not been advanced. Item 11 is not authorized.

---

## 0. Historical Validated Checkpoint - Read Before the Older Handoff

As of 2026-09-01, this section superseded older status statements in this file wherever they conflicted. The remainder of the file preserves the recovery history, design contract, and execution context that remained applicable at that checkpoint.

### 0.1 Exact stop boundary

The user explicitly stopped execution while Item 3 was in progress and requested this handoff. Do not continue from Item 4. Resume at the unfinished Item 3 compatibility evaluation, using the committed acquisition and JAR-inspection evidence described below.

The live plan at the stop boundary is:

1. **Complete:** Complete and publish Item 2 baseline evidence, validation, and recovery milestone.
2. **In progress:** Validate all 190 Item 3 candidate artifacts, dependencies, conflicts, sides, and embedded overlaps.
3. **Pending:** Publish Item 3 compatibility matrix, audit report, decisions, limitations, reproduction, and exit gate.
4. **Pending:** Build and validate Item 4 deterministic isolated test environments, controls, and backup/restore boot.
5. **Pending:** Implement and validate Item 5 profiling and gameplay-measurement methodology.
6. **Pending:** Execute Item 6 generated-configuration audit without tuning.
7. **Pending:** Execute Item 7 deterministic terrain/worldgen interaction inspection with preserved evidence.
8. **Pending:** Execute Item 8 runtime-backed structure-family inventory.
9. **Pending:** Execute Item 9 evidence-backed provisional tier classification.
10. **Pending:** Execute Item 10 checkpointed density generation, integrity validation, analysis, and reporting.
11. **Pending:** Run final cross-item QA, push atomic commits/tags, and determine whether Item 11 is authorized.

### 0.2 Git and working-tree state

Before this handoff edit, local `main`, `origin/main`, and `origin/HEAD` all resolved to `3d1f33551700c9804503d0e27edddce35ea285c4`. The tracked working tree was clean. The following untracked paths were deliberately not committed:

- `.codegraph` — pre-existing user artifact;
- `mcpack-reconstructed-28(1).bundle` — pre-existing user recovery bundle;
- `.ulw-notepad.md` — live-session symlink to transient agent state, not project evidence.

Do not delete, stage, or commit the first two paths. The live-session symlink may disappear when that agent session ends and is not a repository requirement.

All relevant Item 2 and Item 3 implementation, tests, committed evidence, source maps, and acquisition procedures through the stop boundary are already committed and pushed. There were no additional uncommitted project sources to rescue when this handoff was prepared.

The handoff commit is marked by annotated tag `item-3-jar-inspection-checkpoint-2026-09-01`. This is a durable partial-work checkpoint only; it does not mark Item 3 complete.

### 0.3 Item 2 — complete from primary empirical evidence

Item 2 passed its reconstructability exit gate. The accepted target is Minecraft 1.21.1, NeoForge 21.1.249, and Eclipse Temurin 21.0.12.1+1-LTS. The zero-mod server booted, flushed, stopped, restarted the existing world, was archived, independently restored, and booted again. The full installed archive was not redistributed because it contains third-party binaries; exact official acquisition plus the public state overlay is the reproducible equivalent.

Relevant pushed commits:

- `884beec` — strict evidence validation;
- `7afacb4` — exact platform provisioning;
- `40ebd9ac4beb3258d1ab3b88e7941da0bf5f5548` — reconstructed baseline evidence;
- `5fce47f1f11a6ffeb1ef7b1dddfafdb7dc6eab29` — Item 2 closeout.

Validated tags and durable assets:

- `item-2-evidence-assets-2026-09-01` targets `40ebd9a` and publishes:
  - `pristine-baseline-v0-state.tar.gz`, 1,275,395 bytes, SHA-256 `d7880902d37011075a3548404ffe84f0073ef5da7788b6244a24204dd3531663`;
  - `item2-raw-evidence-2026-09-01.tar.gz`, 389,164 bytes, SHA-256 `e97ffe0f036e66be301604de867154a1532f20a5b8cc896c4ed93330e5ae239d`.
- `item-2-baseline-recovery-2026-09-01` resolves to `5fce47f1f11a6ffeb1ef7b1dddfafdb7dc6eab29`.

Primary Item 2 evidence is under `evidence/item-2/`; raw runtime evidence and exact acquisition records are under `evidence/raw/item2/` in the reconstructable evidence layout. Do not modify the frozen Item 2 control while finishing Item 3.

### 0.4 Item 3 — committed progress, not completion

Exactly 190 candidate filenames have exact file-level primary-source identities: 176 from Modrinth and 14 from CurseForge. All 190 exact artifacts were acquired into ignored audit storage and verified against publisher hashes where supplied or official file sizes where publisher hashes were unavailable. The acquisition set totals 699,397,290 bytes.

All 190 outer archives passed ZIP integrity, path-safety, and expected SHA-256 checks. The inspection classified 188 outer archives as mods and 2 as libraries. Thirty-nine candidates contain embedded JARs; 204 embedded JARs were inspected, and no archive-integrity issue was reported. These facts prove artifact identity and parseability only. They do not prove loader compatibility, dedicated-server compatibility, dependency closure, conflict freedom, gameplay correctness, or acceptable performance.

Relevant pushed commits, in order:

- `3da9f40` — exact candidate audit model and validator foundation;
- `ca807f97ddc1e36f3e1418e5ce97bdc601ef621a` — exact source identities and raw-source manifest;
- `4c40642` — remote source-evidence verification;
- `ac3b9f5` — exact candidate acquisition and identity manifest;
- `e217570` — top-level candidate JAR metadata inspection;
- `3d1f33551700c9804503d0e27edddce35ea285c4` — embedded-JAR metadata inspection.

Validated Item 3 source-evidence milestone:

- annotated tag `item-3-primary-source-evidence-2026-09-01` resolves to `ca807f97ddc1e36f3e1418e5ce97bdc601ef621a`;
- release asset `item3-primary-source-raw-2026-09-01.tar.gz` is 20,124,166 bytes with SHA-256 `f2bf2902ade83adb3c8e7aac9bb1527000a04833267325666a6e934984a9ef04` and 771 archive members;
- `evidence/item-3/source-evidence-durability.json` records a passing fresh-download, hash, size, and tar-listing verification.

Machine-readable committed evidence:

- `evidence/item-3/source-identity-matrix.json` — exact primary file identities;
- `evidence/item-3/raw-source-manifest.json` — 767 preserved primary-response files, 122,432,761 bytes;
- `evidence/item-3/source-evidence-durability.json` — release retrieval and integrity receipt;
- `evidence/item-3/artifact-acquisition-manifest.json` — exact 190-file acquisition identities and computed hashes;
- `evidence/item-3/jar-inspection.json` — outer and embedded archive/metadata inspection.

Reproduction sources:

- `candidate-mods/item3-curseforge-file-map.json`;
- `candidate-mods/item3-search-query-overrides.json`;
- `src/mcpack_evidence/item3*.py`;
- `src/mcpack_evidence/raw_manifest.py`;
- `tests/item3/`;
- `tools/build_candidate_source_matrix.py`;
- `tools/collect_candidate_modrinth.py`;
- `tools/collect_candidate_curseforge.py`;
- `tools/build_raw_evidence_manifest.py`;
- `tools/acquire_candidate_artifacts.py`;
- `tools/inspect_candidate_jars.py`.

The exact candidate JARs are intentionally not committed to Git. Their ignored local acquisition path at the stop boundary is `downloads/item3/candidates/`. Reacquire them with the committed acquisition tool and verify the regenerated acquisition manifest before relying on them. The committed primary-response bundle contains no candidate JARs.

### 0.5 Named hazard evidence

These are verified static facts, not final enablement decisions:

- `DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar` is exact Modrinth version `erk04BGa`, 244,981 bytes, SHA-256 `549040fbd81d1b33aea38681109685e86d63985785246a831112c4ba5740d2df`. Its embedded NeoForge metadata identifies `dungeons_arise_seven_seas`, Minecraft range `[1.20,1.22)`, and NeoForge range `[21,)`; Minecraft 1.21.1 falls inside the declared static range. The broad filename and changing platform labels remain hazards requiring an explicit audited disposition.
- `adorabuild-structures-2.11.0-neoforge-1.21.3.jar` is exact Modrinth version `l7GS6bZj`, 657,734 bytes, SHA-256 `6f399680da36dbb95b9a0dbf8b600f173e650be4d6bc25f50fcac792dcce081e`. Its embedded NeoForge metadata identifies `adorabuild_structures`, Minecraft range `[1.21,1.21.3]`, and NeoForge range `[21.0.0-beta,)`; Minecraft 1.21.1 falls inside the declared static range. The filename naming 1.21.3 must not be silently ignored, but it is not by itself proof of incompatibility.
- `cc-tweaked-1.21.1-forge-1.116.1.jar` contains NeoForge metadata and declares NeoForge `[21.1.9,21.2)`. Its filename alone is not loader evidence.
- `sliceanddice-forge-4.2.4.jar` contains NeoForge metadata and declares Minecraft `[1.21.1,)`, NeoForge `[21,)`, and required dependencies including Kotlin for Forge `[5.8,)` and Create `[6.0.9,7.0.0)`.
- `modelfix` contains a malformed dotted dependency-table owner (`1.21-1.10`) and is client-side. Preserve this as a metadata hazard; do not repair upstream metadata or infer that the loader enforces the orphaned declarations.
- `kotlinforforge-5.11.0-all.jar` is an outer `FMLModType: LIBRARY`; its nested metadata supplies the `kotlinforforge` mod identity. A top-level-only audit is insufficient.
- Forgified Fabric API exposes both top-level and nested module identities. Do not treat a multi-loader artifact's inactive Fabric metadata branch as an active NeoForge hard dependency without proving the loader behavior.

### 0.6 Evidence categories at the stop boundary

**Verified from primary evidence:** exact source records for all 190 candidates; exact acquired bytes and computed hashes; publisher hash/size checks; outer and embedded ZIP integrity; parsed metadata documents; Item 2 server lifecycle and restore evidence; published release-asset integrity.

**Reconstructed documentation:** reports and protocols inherited from the recovered 28-commit history remain context only unless superseded by the new Item 2 or Item 3 acceptance evidence above.

**Provisional conclusions:** a declared Minecraft or NeoForge range containing the target is a static compatibility signal, not an enablement decision; embedded-library overlaps are potential conflict signals until loader selection and runtime behavior are evaluated.

**Untested assumptions:** no candidate has yet been accepted for the dedicated-server stack; the full 190-candidate set has not been booted and should not be; server/client classifications, dependency closure, conflict behavior, optional integrations, and actual runtime compatibility are unfinished.

**Missing evidence:** the final 190-row compatibility matrix; a machine-readable dependency/conflict/embedded-overlap evaluation; authoritative loader-semantics citations with retrieval dates; focused runtime boot evidence for retained clusters and named hazards; the human-readable Item 3 audit; decision-log entries; limitations and reproduction closeout; Item 3 exit-gate assessment; a final Item 3 recovery tag. Items 4–10 remain pending behind this gate.

### 0.7 Exact restart instructions

1. Read `SPECS.md` completely, then read this entire handoff and `INFRASTRUCTURE-INSTALLATION-AND-SERVER-TESTING.md` completely. The infrastructure document is supplementary and does not supersede `SPECS.md` ordering.
2. Run `git fetch origin main --tags`, verify branch/upstream/history/tags, and confirm `HEAD == origin/main` before editing.
3. Preserve `.codegraph` and `mcpack-reconstructed-28(1).bundle` unchanged.
4. Verify the committed Item 3 evidence and reacquire ignored candidate artifacts if the local audit cache is absent.
5. Resume by grounding NeoForge dependency/version-range/side and Jar-in-Jar semantics, plus Fabric metadata semantics, in authoritative primary sources. Record exact URLs and retrieval date.
6. Add failing-first tests for the compatibility evaluator. Evaluate active NeoForge metadata separately from inactive Fabric metadata on multi-loader artifacts.
7. Produce the dependency graph, side classifications, missing required dependencies, conflicts, optional integrations, and embedded-library overlap report for all 190 exact candidates.
8. Keep every candidate disabled until its disposition is supported. Perform focused isolated runtime boots only for evidence-supported retained clusters; do not mutate the frozen Item 2 control.
9. Publish the machine-readable compatibility matrix and human audit, with explicit decisions for every candidate and both named hazards. Complete the Item 3 decision log, limitations, reproduction record, and exit-gate assessment.
10. Inspect every diff, commit in small conventional increments, push each commit immediately, and create a validated Item 3 recovery tag only after the full Item 3 exit gate passes.
11. Do not begin Item 4 until every applicable Item 3 subitem and gate is genuinely complete.

The last known full validation after the embedded-metadata commit was 28 passing tests plus clean scoped Ruff, formatting, and basedpyright checks for `src/mcpack_evidence`, `tests`, and the Item 3 tools. Fifteen Ruff findings in later reconstructed tools pre-date this work and were deliberately not mixed into Item 3. Re-run the applicable checks after any new change rather than treating this statement as current proof.

---

## 1. Instructions to the Receiving Agent

Read this file completely before acting. Then read, in this order:

1. `RECOVERY-NOTICE.md`
2. `Adventure-Engineering-Pack-Execution-Ledger.md`
3. `docs/design/design-contract.md`
4. `docs/design/earned-sandbox-freedom.md`
5. `docs/recovery/reconstruction-manifest.md`
6. The report or protocol for the exact item being resumed

Do not infer completion from commit messages, report prose, or a successful server launch. The current repository is a transparent reconstruction of a lost working repository. It contains genuine surviving documents, reconstructed tools/protocols, and explicitly non-authoritative result summaries. Raw evidence that was lost must be regenerated.

Work chronologically and dependency-first. Ask the user only when a missing answer is genuinely load-bearing. When the user is absent, log an unknown or a reversible provisional decision rather than silently inventing a value. Continue autonomously whenever the next action is authorized and reversible.

Every change must be:

- atomic;
- validated;
- committed with a conventional, descriptive message;
- pushed immediately to the canonical GitHub repository;
- followed by verification that local `HEAD` equals `origin/main`.

Large or expensive evidence must also receive a durable archive, checksum manifest, and Git tag before downstream work proceeds. Never allow authoritative work to exist only in `/workspace/scratch`, `/tmp`, or another transient directory.

---

## 2. Project Goal

Build the user's long-lived Minecraft Java 1.21.1 NeoForge pack and dedicated server as an **engineering-driven multiplayer adventure sandbox**.

The pack should evoke the engineering freedom and multiplayer chaos that attracted the user to Michael Reeves's “pisspack,” while rejecting spellcasting, wizard progression, mandatory RPG leveling, inflated legendary loot, and generic damage-sponge combat.

Engineering is the principal capability-progression system. Exploration supplies reasons to engineer. Combat creates expedition pressure. Logistics, infrastructure, factories, computers, vehicles, trains, aircraft, weapons, and siege systems should all have durable roles.

The candidate JAR list is a tentative first draft, not a target manifest. Mods may be added, removed, replaced, or rejected whenever evidence and the design contract justify it. Do not optimize around preserving the candidate list.

---

## 3. Binding Design Contract

These decisions are non-negotiable unless the user explicitly revises them.

### 3.1 Identity and progression

- Engineering-driven multiplayer adventure sandbox.
- Engineering is the primary capability progression.
- Exploration exists partly to give engineering sustained purpose.
- Combat is expedition pressure, not the primary progression system.
- Logistics and infrastructure are meaningful gameplay and progression.
- RPG elements remain lightweight and subordinate to adventure.
- Prefer horizontal capability expansion over vertical stat escalation.
- No mandatory character levels.
- No mandatory skill trees.
- No wizard or spell progression.
- No generic legendary-loot treadmill.
- No uncontrolled attribute inflation.
- No routine damage-sponge enemies.
- Create Enchantment Industry may remain only when it functions as engineering, not spell progression.
- Basic Create, CC:Tweaked, transportation, trains, and Aeronautics must remain normally obtainable rather than rare dungeon-RNG gates.

### 3.2 Aesthetic and dimensions

- Mostly grounded industrial presentation.
- Overt fantasy beyond vanilla requires a specific gameplay justification.
- Fantasy creatures, dimensions, vanilla-like enchanting, and non-spell rewards are not automatically banned.
- Aether, Deep Aether, BetterEnd, and other dimension candidates remain undecided until their roles are tested against the pack identity.

### 3.3 Multiplayer and lifecycle

- Cooperative PvE is primary.
- PvP is optional and consensual.
- Unwanted griefing must receive technical protection.
- Normal target: 2–6 concurrent players.
- Understood peak: 10 players.
- Adventure & Engineering v1 may require a fresh world.
- The launched v1 world is persistent afterward, with no scheduled resets.

### 3.4 Transportation roles

- Walking: local and early exploration.
- Horse/boat: local and regional mobility.
- Trains: persistent, high-throughput regional logistics and infrastructure.
- Aircraft: flexible long-range expedition travel.
- Aircraft must improve exploration materially without erasing adventure or making trains pointless.
- Underground topology is expected to counterbalance aircraft naturally.

---

## 4. Earned Sandbox Freedom Doctrine

This doctrine resolves all breaching, automation, sequence-breaking, and bypass questions.

1. A powerful bypass is valid when the capability required was meaningfully earned.
2. Required effort may come from engineering complexity, infrastructure, materials, energy/fuel, knowledge, travel, setup time, logistics, risk, or upkeep.
3. Power should be proportional to investment.
4. Legitimately obtained capabilities remain real; do not negate them with arbitrary blacklists, universal unbreakable blocks, invisible restrictions, or special-case prohibitions.
5. Players may breach, mine, tunnel, fly, bombard, automate, remotely operate, extract, industrialize, or sequence-break when the solution satisfies the earned-effort rule.
6. Authored routes and encounters are not sacred.
7. If a loop is too cheap, rebalance its inputs, throughput, risk, setup, renewability, or upkeep rather than simply banning engineering.
8. Bugs, duplication glitches, corruption, crashes, desynchronization, permission escapes, and implementation errors are not earned capabilities.
9. Freedom never authorizes unwanted PvP, destruction, theft, surveillance, or denial of service against other players.
10. Shared-server stability may impose the least restrictive constraint necessary to prevent disproportionate harm.
11. Engineering may eventually compress or dominate parts of the adventure loop after substantial investment; it must not erase the loop trivially or prematurely.

Use this doctrine as an explicit acceptance criterion in every later design and exploit audit.

---

## 5. Platform and Scale Facts

| Field | Binding/current value |
|---|---|
| Minecraft | Java Edition 1.21.1 |
| Loader | NeoForge 21.1.249 |
| Java | Eclipse Temurin JDK 21.0.12.1+1 LTS, x86-64 HotSpot |
| Baseline gameplay mods | Zero |
| Baseline `mods/` | Empty |
| EULA | User explicitly accepted; `eula=true` authorized |
| Construction heap | `-Xms1G -Xmx4G`; not a final production allocation |
| Current build host | Linux x86-64, 9 logical CPUs, about 21 GiB RAM, about 30 GiB initially free |
| Server | Dedicated modded Java server; production provider/hardware still unknown |
| Normal concurrency | 2–6 players |
| Peak concurrency | 10 players |
| World policy | Fresh v1 permitted; persistent afterward |

Previously reported pristine-baseline identities, which must be regenerated rather than blindly trusted:

- Path: `instances/pristine-baseline-v0`
- Reconstruction/proof seed: `8953077177248245348`
- Manifest: 133 files, 189,135,287 bytes
- Manifest-file SHA-256: `a257c6fc10e743de53a1dfb67ae123b147739b553d41a116985492f654dfc519`
- Snapshot SHA-256: `856f4ca927e9831c93771aa03adecdb186cb916ef134de32501720c507e74555`
- 72 publisher-hash-verified installer inputs were reported.
- First boot and one existing-world restart were reported successful.

Those results survived only as documentation after the workspace-loss incident. They are useful reconstruction targets, not current acceptance evidence.

---

## 6. Candidate Mod/JAR Context

The repository contains the exact proposed filename inventory at:

- `candidate-mods/current-jars-2026-09-01.txt`

It contains 190 filenames:

- 188 proposed enabled;
- 2 proposed disabled;
- the two disabled entries were Distant Horizons and Xaero's Minimap in the supplied list.

The surviving audits are:

- `docs/audits/Baseline-JAR-Inventory-Audit-v0.1.md`
- `docs/audits/Candidate-Identity-Compatibility-Audit-v0.3.md`

Previously reported audit facts:

- 190/190 candidate identities resolved.
- 176 resolved through Modrinth and 14 through official CurseForge records.
- 62/176 Modrinth candidates had a newer compatible release at audit time.
- 22 candidates used alpha/beta metadata.
- Five declared required dependency edges were missing across two dependency groups.
- Archers, Rogues, Armory, and Arsenal requested Spell Engine.
- LambDynamicLights requested Fabric API.
- 21 candidates were client-required/server-unsupported.
- Seven more were client-required/server-optional.
- Client and dedicated-server manifests must therefore be separate.

Named version hazards from the governing specification still require explicit verification:

- `DungeonsAriseSevenSeas-1.21.x-1.0.4-neoforge.jar`
- `adorabuild-structures-2.11.0-neoforge-1.21.3.jar`
- every broadly labelled `1.21.x` JAR;
- every JAR naming a different Minecraft point release;
- every Forge-labelled JAR used under NeoForge;
- Fabric-derived components and Forgified Fabric API relationships;
- overlapping embedded libraries.

Separate engineering-anchor experiments were previously reported, but they are not baseline admission or final selection:

| System | Experiment version |
|---|---|
| Create | 6.0.10 |
| Create Aeronautics | 1.3.2, replacing proposed 1.3.0 |
| CC:Tweaked | 1.120.2, replacing proposed 1.119.0 |
| Sable | 2.0.5, replacing proposed 2.0.1 |

The four direct JARs plus 15 embedded dependencies were reportedly server-tested separately. That experiment must be regenerated before it is accepted as evidence.

Do not automatically add Spell Engine merely to preserve the combat candidates. The no-spell design direction may instead justify removing or replacing those mods. Decide from requirements and evidence, not candidate-list inertia.

---

## 7. Git and Recovery History

### 7.1 Incident

The original project repository contained 28 local commits but had no remote. It existed only in transient scratch storage. Workspace reclamation deleted:

- the original Git object database;
- raw evidence;
- original scripts and schemas;
- server instances;
- world snapshots;
- generated region files;
- detailed validators and logs.

Surviving durable materials were later recovered from Library. They included more than initially recognized: the ledger, candidate audits/list, Items 4–11 reports/runbooks, and related documentation.

### 7.2 Reconstruction truth

The published 28 commits are a deliberate replacement history, not the original byte-identical commits.

- Original hashes and exact early commit contents cannot be recovered.
- The final 18 original short hashes/subjects are recorded in `RECOVERY-NOTICE.md`.
- The replacement history preserves those known subjects in chronological positions where possible.
- Reconstructed scripts and JSON protocols are functional scaffolds, not claimed byte-identical originals.
- Files under `evidence/reconstruction/` explicitly declare when raw evidence is unavailable and an item must be rerun.
- Never cite a reconstructed summary as proof that a measurement gate passed.

### 7.3 Verified canonical remote

The remote was freshly cloned and verified while preparing this handoff:

```text
Repository: https://github.com/copeugne/mcpack
Branch: main
HEAD: d0f3d22e3c235c451d9ebcb517ea345bbfa2e8f5
Commit count: 28
Tracked files: 36
Tag: reconstructed-28 -> d0f3d22e3c235c451d9ebcb517ea345bbfa2e8f5
Tag: pre-reconstruction-e0eed6d -> e0eed6d53770622a47ae78fc4cceaad21bdbcd50
Working tree after fresh clone: clean
```

The `pre-reconstruction-e0eed6d` tag preserves the repository's initial placeholder commit before the reconstruction history replaced `main`.

### 7.4 Current 28-commit history

```text
174eece chore: initialize adventure engineering pack
9068223 docs: record reconstruction provenance
3d8a44e docs: establish pack design contract
fa556e6 docs: preserve tentative jar inventory
0667683 docs: audit tentative jar inventory
97bd948 docs: resolve candidate identities
efc5a69 build: pin pristine platform identity
47b5e7a test: define controlled seed environment
4f6cb22 test: define reproducible measurement methodology
a92098d docs: audit pristine configuration baseline
cdfe800 test: characterize pristine terrain control
38ec6d9 docs: inventory pristine structure families
ff43d82 docs: classify pristine structure families
30ed5e7 test: add structure density measurement harness
c880316 test: harden structure survey recovery
06856e8 test: define exploration pacing protocol
f33caaa docs: prepare exploration pacing runbook
e35622b test: validate final repaired chunk state
287bb92 perf: stream structure density analysis
e132602 test: verify exploration observation artifacts
87d58ab test: initialize exploration run manifests
7d737a6 perf: decode integrity NBT selectively
b703b4e test: cross-check selective NBT decoding
5fa6bac test: atomically checkpoint density runs
8238d13 test: resume checkpointed density surveys
9c3d522 test: record density generation integrity failures
d58736d test: record baseline structure density evidence
d0f3d22 docs: close baseline density audit
```

---

## 8. Evidence Hierarchy

### 8.1 Binding authority

1. Explicit user decisions in the design contract and Earned Sandbox Freedom Doctrine.
2. The current execution ledger's status vocabulary and no-assumption rule.
3. Freshly generated raw evidence with hashes, manifests, versioned protocols, and validation.
4. Surviving original reports as historical/reconstruction guidance.
5. Reconstructed tools and summaries as scaffolding only.

### 8.2 What is currently authoritative

- Pack identity and user preferences.
- Platform targets: Minecraft 1.21.1, NeoForge 21.1.249, Java target.
- Candidate filename inventory as a proposal.
- Development seed identities.
- Git remote state and reconstruction provenance.
- The fact that raw evidence was lost.
- The requirement to rerun Items 2–10.
- Item 11's need for real human observation.

### 8.3 What is not current acceptance evidence

- Any commit subject implying a measurement passed.
- `evidence/reconstruction/*.json` result counts.
- Previously reported hashes without regenerated matching artifacts.
- Reconstructed Python tools merely compiling.
- Surviving final reports by themselves.
- A server launching successfully.
- Candidate filenames claiming compatibility.

### 8.4 Completion rule

An item becomes `COMPLETE` only when:

1. every required input is identified;
2. every subitem is resolved;
3. raw evidence is retained and linked;
4. the exit gate explicitly passes;
5. failures have dispositions;
6. downstream assumptions are updated;
7. exact configuration/protocol versions are recorded;
8. the commit and evidence are pushed/archived durably.

Unknown values remain `UNKNOWN`. Resolve them only through explicit user decisions, artifact inspection, authoritative sources, controlled experiments, reproducible measurement, or derivation from already verified facts.

---

## 9. Current Master Status

| Item | Status | Meaning now |
|---:|---|---|
| 1 | `COMPLETE` | Design contract and sandbox doctrine survived and remain binding. |
| 2 | `BLOCKED` | Prior baseline result summarized; binaries, manifest, snapshot, and restore evidence must be regenerated. |
| 3 | `BLOCKED` | Candidate audit documents survived; source evidence/current availability must be regenerated/reverified. |
| 4 | `BLOCKED` | Seed identities/report survived; snapshots, scripts, and restore receipts must be rebuilt. |
| 5 | `BLOCKED` | Method report survived; protocols, schemas, fixtures, and tools need reconstruction verification. |
| 6 | `BLOCKED` | Report survived; machine-readable config evidence must be regenerated. |
| 7 | `BLOCKED` | Reported repeated samples survived; raw samples and verification must be regenerated. |
| 8 | `BLOCKED` | Report survived; structure matrix and registry verification evidence must be rebuilt. |
| 9 | `BLOCKED` | Classification report survived; family matrix and validator must be rebuilt. |
| 10 | `BLOCKED` | Final report/results survived; raw worlds, regions, logs, analysis, and validators must be rerun. |
| 11 | `BLOCKED` | Depends on recovered Item 10, then requires at least two blind human operators. |
| 12–18 | `UNSTARTED` | Strictly depend on completed Item 11 evidence. |
| 19–37 | `UNSTARTED` | Requirements/system design after verified baseline forensics. |
| 38–47 | `UNSTARTED` | Candidate feasibility, stack construction, encounters, loot, and engineering freeze. |
| 48 | `UNSTARTED` | Exact progression implementation; must be split into atomic gates. |
| 49–50 | `UNSTARTED` | Performance hardening and lifecycle validation. |
| 51 | `UNSTARTED` | Adventure v1 release freeze. |

Repository reconstruction is complete. **Scientific/evidence recovery is not complete.** Recovery Gate R-1 stays open until Items 2–10 have qualifying evidence again.

---

## 10. Previously Reported Item 7–9 Findings

Use these to detect gross reconstruction regressions, not as substitute evidence.

### Item 7 — pristine worldgen control

- Four deterministic seed roles.
- 50 stable-height/biome samples per seed.
- 200 samples total.
- Two independent final runs reportedly repeated every raw sample and derived statistic exactly.
- Zero relevant generation-problem lines were reported.
- No terrain, biome, or structure candidates were installed in that control.

### Item 8 — vanilla structure inventory

- 34 structure registry entries.
- 34 exact biome-tag bindings.
- 20 placement sets.
- Grouped into 21 gameplay families.
- Every declared loot source reportedly resolved against embedded vanilla data.

### Item 9 — provisional classification

- 4 ambient/Tier 0 families.
- 1 civilization family.
- 8 Tier 1 families.
- 1 Tier 2 family.
- 5 Tier 3 families.
- 2 Tier 4 families.
- No family was finally declared redundant or selected for removal.

---

## 11. Item 10 — Reported Baseline Density Result

### 11.1 Status

Previously measured, now `BLOCKED` because raw reproducibility artifacts were lost.

### 11.2 Frozen/reconstructed method

- Four deterministic Overworld seeds.
- Nested stages per seed:
  - Stage 1: 4,096 chunks.
  - Stage 2: 8,192 chunks.
  - Stage 3: 16,384 chunks.
  - Stage 4: 32,768 chunks.
- Aggregate ceiling: 131,072 chunks.
- Continue until every provisional category has at least 30 observations or Stage 4 ceiling is reached.
- Sparse categories at the ceiling are right-censored.
- Denominator: saved chunks whose status is exactly `minecraft:full`.
- Count: unique non-`INVALID` structure start keyed by registry ID and authoritative start chunk.
- Integrity requirements:
  - stored coordinate matches Anvil slot;
  - clean `save-all flush` and shutdown;
  - independent offline exact-slot scan;
  - no unreadable or coordinate-shifted accepted targets.

Relevant reconstructed files:

- `measurement/structure-density-v0.1.json`
- `tools/analyze_structure_density.py`
- `tools/structure-density-harness.md`
- `docs/recovery/structure-survey-recovery.md`
- `docs/recovery/atomic-checkpoint-policy.md`
- `docs/recovery/resume-policy.md`
- `docs/recovery/selective-nbt-decoder.md`

Treat these as requirements/scaffolding and validate them before use.

### 11.3 Reported aggregate findings

| Metric | Starts | Per 1,000 chunks |
|---|---:|---:|
| All structures | 1,007 | 7.6828 |
| Actionable locations | 831 | 6.3400 |
| Static hostile-location proxy | 762 | 5.8136 |
| Tier 2 proper dungeons | 100 | 0.7629 |
| Tier 3 major expeditions | 47 | 0.3586 |
| Villages | 31 | 0.2365 |
| Tier 4 objectives | 4 | 0.0305, right-censored |

Mineshafts accounted for:

- 476 starts;
- 47.3% of all starts;
- 57.3% of actionable starts;
- 73.3% of Tier 1 starts.

This is the central interpretation: geometric structure density was not obviously low, but much of it was underground, underwater, buried, or otherwise poorly discoverable. Static density cannot establish good player pacing.

### 11.4 Per-seed reported rates per 1,000 chunks

| Seed role | All | Actionable | Combat proxy | Tier 2 | Tier 3 | Villages |
|---|---:|---:|---:|---:|---:|---:|
| Ordinary | 7.7820 | 6.5308 | 5.8289 | 0.8240 | 0.0916 | 0.1831 |
| Mountainous | 5.2490 | 4.4861 | 3.9978 | 0.5188 | 0.8240 | 0.3662 |
| Ocean-heavy | 9.9487 | 7.9651 | 7.4463 | 0.8240 | 0.3357 | 0.2441 |
| Biome-diverse | 7.7515 | 6.3782 | 5.9814 | 0.8850 | 0.1831 | 0.1526 |

### 11.5 Reported quality controls and failures

Reported accepted final run: `item10-chunkpregen-full-r19`.

Reported accepted integrity:

- 32,768 full/correct target slots per seed.
- Zero final coordinate mismatches.
- Zero final unreadable slots.
- 200/200 height checks.
- 10,190/10,190 selective/full NBT field checks.
- 192/200 biome boundary comparisons were explicitly non-acceptance checks.

Reported rejected approaches/failures:

- Loaded/ticket probes did not prove final saved status.
- Heightmap presence did not prove `minecraft:full`.
- Immediate Chunky shutdown left 1,637/4,096 chunks non-full.
- Live `save-all flush` was not a per-tile serialization oracle.
- A broad completion regex matched the wrong line.
- Chunk Pregenerator area mode did not cover the exact requested rectangle.
- r18 diverse seed had one unreadable slot, three shifted coordinates, and only 28,863 full/correct targets.
- r19's first mountain process was interrupted before checkpoint and excluded.

The rerun must preserve failed attempts and dispositions instead of deleting inconvenient evidence.

### 11.6 What Item 10 did not prove

- It did not measure actual player-visible discovery.
- The combat number was a static location proxy, not observed combat.
- It did not evaluate the tentative 190-JAR stack.
- It did not justify adding/removing structure mods.
- It did not justify changing Sparse Structures or spacing.
- It did not establish dungeon mechanical quality.

Do not select solutions until Items 11–18 identify root causes.

---

## 12. Item 11 — Human Exploration Pacing Gate

### 12.1 Purpose

Item 10 asks where structures exist. Item 11 asks what a player actually sees and experiences while traveling.

A structure can exist without being visible, be visible without being actionable, or be actionable while still producing excessive dead travel or repetition. Headless scans cannot decide human visual recognition, perceived actionability, or meaningful-interaction time.

### 12.2 Test matrix

- Four seeds:
  - ordinary: `42`;
  - mountainous: `6671238423019257953`;
  - ocean-heavy: `95920844204830198`;
  - biome-diverse: `-3503646078644842058`.
- Three transport modes:
  - foot;
  - standardized horse;
  - vanilla boat using natural water only.
- Two endpoint types:
  - 3,600 seconds/60 minutes;
  - 10,000 horizontal path blocks.
- Three replicates per applicable seed × mode × endpoint cell.
- Maximum 72 valid human runs.
- Boat cells may be reviewed `not-applicable` only if the assigned route lacks a continuous natural navigable-water corridor.
- Foot and horse cells are not waived for ordinary terrain difficulty.

### 12.3 Operators

- At least two human operators.
- Each operator tests every transport mode.
- Operators remain blind to structure coordinates, Item 10 evidence, prior route observations, and seed-map results beyond the declared seed role.
- No `/locate`, spectator mode, free camera, debug structure display, or seed-map website.
- An operator cannot repeat a route they have already seen, even in another transport mode.

The unresolved human question is whether the user can be one operator and recruit a second. Do not ask it until Recovery Gate R-1 is near completion unless scheduling lead time justifies asking earlier.

### 12.4 Route bearings

- Fixed-time replicates: 0°, 120°, 240°.
- Fixed-distance replicates: 60°, 180°, 300°.
- Follow the assigned bearing within ±45°, permitting terrain/interaction detours and then resuming the bearing.

### 12.5 Required artifacts per valid run

- Complete client video.
- Five-second position trace.
- Event log.
- Dedicated server log.
- Post-run world archive.
- Run manifest conforming to `measurement/exploration-run.schema.json`.
- SHA-256 identities for external artifacts and manifest.
- Blind reviewer decision and annotations.

### 12.6 Metrics

- Visual discoveries per hour and per 1,000 path blocks.
- Actionable discoveries.
- Hostile encounter episodes.
- Proper dungeons and major structures.
- Villages.
- Meaningful activity time.
- Adventure Activity Ratio.
- Dead-travel percentage.
- Unique structure families per hour.
- Time to first repeated family.
- Repeats per 10,000 blocks.
- Median, range, and IQR by cell.

### 12.7 Current tooling

- `measurement/exploration-pacing-v0.1.json`
- `measurement/exploration-run.schema.json`
- `tools/create_exploration_run.py`
- `tools/analyze_exploration_pacing.py`
- `docs/items/Item-11-Baseline-Exploration-Pacing-Runbook.md`

These are reconstructed. Compile and test them, then validate that they implement the full surviving runbook before collecting human evidence.

Item 11 cannot be replaced with simulated clients, bots, structure scans, or the agent's subjective guess.

---

## 13. Governing 51-Item Dependency Spine

The original user specification is a chronological, dependency-ordered adventure-system plan. Preserve this order unless a documented dependency correction is required.

1. Design contract.
2. Baseline freeze.
3. Exact version/dependency audit.
4. Controlled test environment.
5. Measurement/profiling methodology.
6. Configuration audit.
7. Terrain/worldgen interaction audit.
8. Structure-family inventory.
9. Initial structure classification.
10. Structure and encounter density measurement.
11. Exploration pacing and repetition measurement.
12. Discoverability measurement.
13. Dungeon-quality measurement.
14. Enemy/combat-quality measurement.
15. Loot and salvage-economy audit.
16. Multiplayer persistence/depletion audit.
17. Baseline performance measurement.
18. Baseline root-cause report; diagnose without selecting final solutions.
19. Final adventure structure taxonomy.
20. Transportation-scale model.
21. Target adventure cadence.
22. Dungeon-topology requirements.
23. Dungeon-objective variety.
24. Dungeon persistence/repeatability policy.
25. Difficulty model.
26. Enemy roles and encounter archetypes.
27. Elite/miniboss/boss philosophy.
28. Loot economy.
29. Reward renewability and automation rules.
30. Engineering ↔ adventure integration.
31. Discovery/navigation progression.
32. Multiplayer expedition and loot rules.
33. Civilization/settlement roles.
34. Dimension roles.
35. Combat-mod boundaries.
36. Destructibility, breaching, and automation-bypass policy.
37. Expedition preparation, failure, and recovery.
38. Early candidate-mod feasibility screening.
39. Controlled structure-redundancy experiments.
40. Provisional content/worldgen stack freeze.
41. Proposed underground dungeon-layer integration and evaluation.
42. Combined provisional worldgen remeasurement.
43. Sparse Structures/Structure Essentials spacing and overlap tuning.
44. Encounter orchestration before AI enhancement.
45. Incremental AI/elite evaluation.
46. Multiplayer container/persistence foundation, including Lootr if justified.
47. Adventure-relevant engineering/combat stack freeze.
48. Exact loot, renewability, discovery, civilization, engineering, logistics, death, and failure implementation.
49. Final candidate performance hardening.
50. Early/mid/late/mature-server, exploit, redundancy, and regression validation.
51. Adventure v1 definition-of-done validation and freeze.

Later candidate names in the spec—Dungeon Crawl, Lootr, In Control!, Improved Mobs, Enhanced AI, Zombie Awareness, Mob Champions, Guard Villagers—are hypotheses, not mandated inclusions. A candidate must solve a documented measured problem and pass capability, compatibility, gameplay, performance, and redundancy gates.

---

## 14. Required Whole-Pack Plan Expansion

The 51-item source is strong for adventure/dungeon/exploration but insufficient as the complete engineering modpack master plan. Before release, add explicit tracks for:

1. Engineering capability inventory and ownership matrix.
2. Engineering tier/prerequisite graph.
3. Recipe/progression reachability proof.
4. Resource-generation and processing-loop balance.
5. Kinetic/power/fuel economy.
6. Logistics throughput tiers.
7. Train economics and persistent infrastructure role.
8. Aircraft construction, payload, fuel, range, speed, crash/loss, and recovery.
9. Stationary versus mobile factory boundaries.
10. Siege/ammunition economy.
11. CC:Tweaked/peripheral security, abuse, resource, and networking boundaries.
12. Chunkloading ownership, quotas, offline behavior, and recovery.
13. Contraption/vehicle assembly, restart, cross-chunk, crash, and persistence tests.
14. Numeric server performance budgets.
15. Numeric client FPS/frame-time/startup budgets.
16. Network bandwidth, latency, jitter, loss, disconnect, and desynchronization tests.
17. Client/server manifest separation.
18. Registry, tag, recipe, advancement, datapack, and loot-conflict audits.
19. Packaging, installer/import, distribution-channel, and licensing verification.
20. New-world/migration/upgrade policy and removed-registry handling.
21. Startup/shutdown, crash recovery, watchdog, disk exhaustion, monitoring, and log rotation.
22. Backup retention, restore-time objective, and real restore drills.
23. PvP, claims, anti-griefing, permissions, operator, and allowlist policy.
24. Onboarding, recipe-viewer, ponder/manual, advancement, and knowledge-delivery policy without a quest railroad.
25. Accessibility, remappable controls, subtitles/cues, localization scope, and text legibility.
26. Semantic pack versioning, staging, changelog, rollout, rollback, and compatibility windows.
27. Release rollback drill covering world, server, configs, mods, and clients.

Item 48 must be split into independently versioned implementation and validation gates. Items 49–50 need corrective-loop ownership: every failure routes to a specific design/configuration owner, rollback point, retest scope, and regression subset.

---

## 15. Immediate Recovery Plan for the New Agent

### Step 0 — establish durable working state

```bash
git clone https://github.com/copeugne/mcpack.git
cd mcpack
git fetch --tags --prune
test "$(git rev-parse HEAD)" = "d0f3d22e3c235c451d9ebcb517ea345bbfa2e8f5"
test "$(git rev-list --count HEAD)" -eq 28
git status --short --branch
```

Confirm write access with a harmless, authorized workflow before starting expensive work. Do not generate new evidence until commits can be pushed and large artifacts can be archived durably.

### Step 1 — add this handoff to the repository

Add, validate, commit, and push this file as the first new atomic commit. Do not rewrite the reconstructed 28 commits.

Suggested commit:

```text
docs: add new-session project handoff
```

### Step 2 — validate reconstructed scaffolding

- Compile every Python tool.
- Parse every JSON file.
- Verify schema behavior with positive and negative fixtures.
- Compare reconstructed code to surviving report requirements.
- Record gaps instead of assuming behavioral equivalence.
- Push tool corrections atomically before any measurement run.

### Step 3 — rerun Item 2

- Acquire exact official Minecraft/NeoForge/Java inputs.
- Verify publisher hashes and versions.
- Build pristine zero-mod server.
- Generate default configuration with authorized EULA.
- Boot fresh world, save/flush/stop, restart same world, save/flush/stop.
- Freeze manifest and archive.
- Restore into a separate tree.
- Verify every path, size, and SHA-256.
- Record host identity and construction JVM flags.
- Archive evidence durably.
- Update ledger from `BLOCKED` to `COMPLETE` only after exit-gate proof.
- Tag and push.

### Step 4 — rerun Item 3

- Revalidate all 190 candidate identities against current official project metadata.
- Record exact game/loader/environment support.
- Resolve required and optional dependencies.
- Separate client/server candidates.
- Recheck suspicious 1.21.x and 1.21.3-labelled files.
- Preserve source URLs, retrieval times, licenses, hashes, and audit output.
- Do not download or admit the entire candidate pool automatically.

### Step 5 — rerun Items 4–6

- Regenerate the four deterministic seed snapshots.
- Rebuild repeatable deletion/restoration procedures.
- Rebuild measurement schemas, fixtures, and validator tests.
- Reaudit pristine config/defaults without changing them.
- Perform and retain an actual restore boot.
- Commit/push/tag each independently complete item.

### Step 6 — rerun Items 7–9

- Regenerate and independently repeat terrain/biome samples.
- Rebuild exact structure registry/biome/placement/loot inventory.
- Rebuild 21-family matrix and validator.
- Reapply provisional classification with deficiency/redundancy flags.
- Do not make final retention/removal choices yet.

### Step 7 — rerun Item 10

- Validate the generation harness on small pilots first.
- Preserve all failed pilots and dispositions.
- Generate the four exact nested stage rectangles.
- Require saved `minecraft:full` status and coordinate-correct Anvil slots.
- Cross-check selective NBT decode against a trusted full decoder.
- Use atomic checkpoints and clean resume rules.
- Run independent offline validation.
- Archive worlds/regions/logs separately with SHA-256 manifest.
- Produce stage analyses and final report.
- Compare new results with the historical reported result; explain differences rather than forcing a match.
- Only then return Item 10 to `COMPLETE`.

### Step 8 — prepare Item 11 human work

- Validate tools/runbook.
- Ask the user whether they can serve as one operator and recruit a second.
- Prepare blind route packets and pristine per-run restore process.
- Do not expose Item 10 coordinates to operators.
- Collect, review, hash, analyze, archive, commit, and push manifests/results.

### Step 9 — resume original dependency spine

Proceed to Item 12 only after Item 11's full human-observation exit gate passes.

---

## 16. Durability and Git Policy

The prior loss must not recur.

1. GitHub is canonical.
2. A local commit is not complete until pushed.
3. After every push:

   ```bash
   git fetch origin main
   test "$(git rev-parse HEAD)" = "$(git rev-parse origin/main)"
   git status --short --branch
   ```

4. Commit protocols before experiments.
5. Never put secrets, tokens, addresses, allowlists, or player UUIDs into Git.
6. Large raw evidence stays outside normal Git but receives:
   - immutable archive name;
   - SHA-256 manifest;
   - size and file count;
   - matching Git commit/tag;
   - durable storage in at least two independent locations when practical;
   - a tested restore.
7. Tag each completed numbered item, for example `item-10-baseline-density-rerun`.
8. Create and durably save a verified full Git bundle after each phase.
9. Never delete failed evidence merely because it is inconvenient.
10. If push or archive persistence fails, stop downstream work until durability is restored.

---

## 17. High-Priority Unknowns

Do not ask all of these immediately. Resolve them at the owning dependency gate.

### Platform/release

- Final client and server pack formats.
- Distribution channels.
- Licensing/redistribution eligibility.
- Version/channel scheme.
- Upgrade and rollback compatibility windows.
- Supported client operating systems and hardware tiers.

### Production operations

- Hosting provider/model.
- CPU and dedicated/shared allocation.
- Physical RAM and final heap.
- Storage type, capacity, and I/O limits.
- OS/kernel.
- Uptime and maintenance expectations.
- Backup frequency, retention, size, duration, restore-time objective.
- World border and pregeneration policy.
- Monitoring/alert thresholds.
- Crash restart/watchdog.
- Log retention/redaction.
- Disk-growth budget.
- Claims, operator, allowlist, and permission details.

### Performance

- Idle/normal/combat MSPT budgets.
- Fresh-chunk latency/backlog budget.
- Sustainable aircraft speed.
- Memory/leak and GC budgets.
- Entity/block-entity tick budgets.
- Save-pause budget.
- Client FPS/frame-time/startup budgets.
- Network latency/jitter/loss/bandwidth assumptions.

### Engineering/adventure

- Full engineering inventory and capability ownership.
- Progression and recipe reachability graph.
- Power/fuel/logistics economies.
- Train/aircraft capability and cost boundaries.
- Chunkloading/offline-processing policy.
- CC:Tweaked security.
- Final structure thresholds/cadence/activity targets.
- Dungeon topology, persistence, objectives, and discovery.
- Difficulty, boss, loot, renewability, and multiplayer semantics.
- Dimension roles.
- Death/grave/vehicle recovery.
- Item 11 operator availability.

---

## 18. Things the New Agent Must Not Do

- Do not claim the reconstructed 28 commits are the original history.
- Do not mark Items 2–10 complete from surviving reports alone.
- Do not fabricate missing logs, worlds, hashes, samples, or validator output.
- Do not install all 190 candidates as the baseline.
- Do not treat filenames as compatibility proof.
- Do not choose final structure mods before baseline root-cause analysis.
- Do not solve poor cadence by making giant structures common.
- Do not add spell systems or a wizard progression path.
- Do not turn rare dungeon RNG into a gate for foundational engineering.
- Do not use universal indestructible dungeon blocks to protect authored routes.
- Do not ban a proportionately earned engineering bypass merely because it is powerful.
- Do not add AI stacks before testing encounter composition with existing AI.
- Do not stack redundant AI/difficulty systems.
- Do not use health/damage inflation as the default difficulty lever.
- Do not assume Lootr resets physical dungeons.
- Do not treat per-player loot multiplication as automatically harmless.
- Do not proceed to dependent items when an explicit test/decision gate has failed.
- Do not store authoritative work only in transient scratch storage.
- Do not ask the user non-load-bearing questions that can be measured, inspected, logged, or deferred.

---

## 19. Repository Map

| Path | Role |
|---|---|
| `Adventure-Engineering-Pack-Execution-Ledger.md` | Canonical status, decisions, unknowns, blockers, and next steps |
| `RECOVERY-NOTICE.md` | Truth about original loss and reconstructed Git history |
| `candidate-mods/current-jars-2026-09-01.txt` | Exact tentative filename pool |
| `docs/audits/` | Surviving candidate identity/JAR audits |
| `docs/design/` | Binding design contract and sandbox doctrine |
| `docs/items/` | Surviving Item 4–11 reports/runbooks |
| `docs/recovery/` | Reconstructed recovery/checkpoint/decoder contracts |
| `evidence/reconstruction/` | Explicitly non-authoritative historical summaries and rerun markers |
| `measurement/` | Reconstructed Item 10/11 protocols and schema |
| `platform/pristine-platform.json` | Reported platform target; requires regenerated evidence |
| `test-environment/seed-suite.json` | Development seed identities |
| `tools/` | Reconstructed analysis and run-manifest tooling |

---

## 20. Final Handoff Directive

Resume at **Recovery Gate R-1**, not Item 11 and not mod selection.

The first goal is to make the baseline scientifically reproducible again while preserving the user's design decisions and freedom doctrine. Rebuild Items 2–10 in dependency order, push every atomic change immediately, archive expensive evidence durably, and keep reconstructed historical results visibly separate from new acceptance evidence.

Once Item 10 is genuinely complete again, execute Item 11 with at least two blind human operators. Only then continue Items 12–51.

The project succeeds when it becomes a coherent engineering sandbox whose adventure layer gives factories, logistics, computers, vehicles, trains, aircraft, weapons, and siege equipment meaningful reasons to exist—without magic progression, arbitrary player restrictions, shallow structure spam, or an RPG loot treadmill.
