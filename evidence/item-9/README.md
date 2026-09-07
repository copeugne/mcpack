# Item 9 classification evidence

Status: IN PROGRESS. Decision version: item9-provisional-v1.

## Population and evidence

The sole population is the 448 keys of `families` in
[the accepted Item 8 inventory](../item-8/inventory.json), SHA-256
`4f7853b7b6531f99d3f0592b2129291d2e0cf24b4ad5d1381b3883dbdcfbc52d`.
PR18 accepted head `2023a22a84372483841f7ad286a868584df564fa` merged as
`326979dd2eee7da3f881f1316eb845fb16e8ea6b`; PR19 accepted head
`ad65a6eb6c2e3f85746bd696296f177be6d2e87d` merged as
`be64d458fee3539e5132049d871d1c32ebc3655b`. Both were verified through
GitHub PR metadata and fetched main ancestry on 2026-09-07. Local inventory
and family decisions match main. See [accepted delivery](../item-8/README.md).

The 18 `other_registry_groups` are excluded from classification, not forgotten
families. The 448 active families include 408 registry and 40 nonregistry
families. Components, aliases and internal variants remain within their accepted
families; no re-grouping is performed. The old 21-family zero-mod classification
at commit `ff43d826` is superseded context, not evidence for the retained stack.

Each row in [classification.md](classification.md) cites the exact inventory key
in its first column. Its evidence reference is `../item-8/inventory.json`,
`families["<family_id>"]`. Read the row's `intended_hostility`, `mob_source`,
`generated_spawners`, `loot_table_source`, `approximate_footprint`,
`approximate_vertical_size`, `visual_discoverability` and `grouping_decision`
together. These contain the accepted source descriptions, precise source paths,
hashes, variant distinctions and world-observation links. This direct reference
avoids copying raw Item 8 evidence or creating another extraction pipeline.

## Provisional rubric

Exactly one primary category is assigned per family:

| Code | Category | Source-supported decision rule |
| --- | --- | --- |
| T0 | Tier 0, ambient landmark | Environmental formation, ornament, abandoned shelter, navigation installation or incidental cache/salvage. Mere loot presence does not establish a dungeon. |
| C | Civilization | Authored civilian settlement, inhabited venue or explicitly furnished resupply/work/shelter design whose primary role is habitation or expedition staging. Services and safety are not assumed. |
| T1 | Tier 1, small encounter | Localized hostile, trap, creature-interaction or deliberate excavation/search objective. A single arena/boss room may remain localized; boss identity alone does not establish expedition scale. |
| T2 | Tier 2, proper dungeon | Connected hostile room/passage or multi-level encounter design supports traversal beyond one local encounter. This is a provisional structural role, not certification of meaningful play quality. |
| T3 | Tier 3, major expedition | Extensive connected hostile complex, substantial vertical/aquatic/airborne traversal, or comparable compound expedition design. Physical size alone is insufficient. |
| T4 | Tier 4, world objective | Explicit dimension-progression destination or central world boss objective supported by accepted source behavior. Portal-shaped decoration, generic bosses and large structures do not qualify by name. |

No Item 19 duration thresholds, difficulty scores, encounter frequencies, reward
values or final retention decisions are asserted. Tier boundaries describe the
accepted design, not a measured clear time. Mixed families retain one primary
role and explicitly record the alternate role in ambiguity. No variant count is
used as an observed probability.

Confidence is H (direct purpose and content agree), M (reasonable source-derived
primary role with tier/variant uncertainty), or L (known defect materially limits
the intended role). Every row inherits the ambiguity that realized encounters,
play duration, effective rewards, service operation and natural dangers are
unmeasured. Its final column records the additional family-specific ambiguity;
`standard` means only that inherited limitation, not absence of uncertainty.

## Required flags and comparison groups

Every row is assessed for all eight Item 9 flags. `-` means no affirmative
source-supported flag at this stage, not proof of quality or uniqueness.

- D: mostly decorative/ambient design. Utility or incidental loot may coexist.
- S: dungeon-like form with weak or absent authored gameplay beyond a cache or
  isolated encounter. This flags a concern, not a measured absence of enjoyment.
- O: substantial structure envelope with sparse supported internal encounter
  purpose. Environmental formations are not failed dungeons merely for being big.
- Comparison groups flag overlapping themes. Multiple rows in a group are
  explicit candidates for comparison, not duplicates of canonical identity.
- Groups `village`, `ruin`, `tower`, and `dungeon-*` additionally flag potential
  redundant village, ruin, tower and dungeon archetypes respectively. These four
  redundancy flags mean candidates for later comparison, never proven removals.

Comparison rationale: `village` shares settlement/resupply purpose; `ruin`
shares abandoned built exploration/cache purpose; `tower` shares vertical
landmark/encounter form; `dungeon-mine` shares abandoned mining passages;
`dungeon-tomb` shares enclosed burial/temple traversal; `dungeon-fort` shares
fortified hostile room networks; `dungeon-mansion` shares hostile domestic room
networks; `dungeon-trial` shares spawner/arena challenge infrastructure.
Other groups identify themes only: `house` (dwelling/staging), `ship`
(vessel/wreck), `shrine` (small monumental/cache installation), `portal`
(transport/frame), `worksite` (industrial/extraction), `nature` (environmental
formation), `camp` (temporary habitation), `outpost` (localized garrison),
`statue` (sculpture/column), `bridge` (crossing), `cache` (localized stored reward),
`arena` (localized combat space). A row can name several groups.

Distinct geometry, inhabitants, dimension, hazards and variant behavior in the
linked inventory are counterevidence to automatic redundancy. In particular,
Better Village and Village Taverns are already attributed components, not extra
families. Their existence does not add classification rows. Item 39, not Item 9,
will test removal effects. Gameplay shortcomings requiring observation remain
uncertain until their owning later gates.

## Work and definition of done

448 existing assessments await role/flag integration at intake; there is no
identified missing raw evidence prerequisite for provisional classification.
The work is 448 primary decisions and 3,584 flag dispositions, not that many
commits or tests. Batches: 49 AdoraBuild; 132 vanilla/YUNG/dimension and other
providers; 69 WDA/Explorify/Explorations; 62 IDAS; 136 Moog. The first batch tests
mixed inhabitants, trap-only caches, ornamental dungeon forms and broken assembly.

Done requires exact population coverage once, six valid primary categories,
evidence/rationale/confidence/ambiguity for every row, all eight flag classes
addressed, source limitations preserved, and explicit local gate results. Then
push, open a main PR, request and inspect completed Codex review cycles, resolve
valid findings, obtain a clean final review, merge and verify delivered main.
No Item 8 re-audit, server run, new measurement or Item 10 work is needed.
Validation is direct inventory/hash comparison and matrix coverage/field checks,
plus manual review of the classification and comparison rationale. No new schema,
validator framework, raw archive or broad regression suite is justified.
