# Item 9 classification evidence

Status: COMPLETE. Decision version: item9-provisional-v1.

## Verified delivery

[PR20](https://github.com/copeugne/mcpack/pull/20) merged reviewed head
`5073af269d6e253edb0d314346d671acf7d294cf` as
`7cbe06c7d8b074fa6121c1143432d28d02996712` on 2026-09-07 at 22:29:52 UTC
(2026-09-08 local date). Fetched `origin/main` contains that exact head;
`git merge-base --is-ancestor 5073af269d6e253edb0d314346d671acf7d294cf origin/main`
returned zero. The [clean final review](https://github.com/copeugne/mcpack/pull/20#issuecomment-5576222112)
identifies this head; the review summary records completion at 22:28:55 UTC,
and the Codex bot returned a PR thumbs-up. Review records, inline comments and
discussion comments were inspected. The final cycle added no findings; all
three earlier valid findings have the dispositions below.

Item 9 is COMPLETE: exact family coverage, required classifications and flags,
source references and limitations, focused gate, durable evidence, clean review
and main merge are satisfied. Classification values and accepted Item 8 inputs
are unchanged by this delivery-status follow-up. Item 10 was not performed.

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

For mixed families, settlement architecture with localized abandoned/hostile
alternatives retains C. Standalone encounter designs with civilian alternatives
retain the encounter role, with M confidence and the alternative recorded.
This is an editorial primary-role decision, not a majority-by-frequency claim.
Pure transport infrastructure is T0 even when useful after a world objective;
the objective is not duplicated across its platform and gateway families.

The Integrated Stronghold T4 interpretation additionally cites the retained
template catalog `../item-8/sources/templates-redacted.json.gz`, resource
`data/integrated_stronghold/structure/portal_room/portal_room.nbt`, SHA-256
`62fbc4a9bd48be81244c774318184fda830cd1d247f8c2fdb5201fc7987f637a`.
Its palette contains `minecraft:end_portal_frame`; this supports intended
progression architecture, not a tested working portal. Better Strongholds'
accepted `stronghold-provider/README.md#stronghold-content-and-placement`
records its EndPortalFrameProcessor and frozen frame-fill chance. Effective
Eye targeting among retained replacements remains untested for both families.

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

At intake, 448 existing assessments awaited role/flag integration. All are now
integrated; no missing raw evidence prerequisite for provisional classification
was identified. Validation and reviewed delivery have both passed.
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

## Focused local gate

Run in Bash from the repository root. These are direct checks of the fixed
accepted inventory and hand-authored table, not a new schema or measurement
pipeline. The JSON output is a count/check summary, not a second classification.

```sh
bash evidence/item-9/check.sh

```

Initial inspection commands assumed `families` was an array and stopped with
`Cannot index object with number`; the accepted inventory is keyed by family ID.
A preliminary AWK count reused an array name as a scalar and stopped with
`illegal reference to array g`. Corrected direct inspection and the tracked gate
replace those failed probes; neither failure changed accepted evidence.

Manual review uses the Markdown table and the accepted source
attributes. It checks intended versus realized content, mixed variants,
progression claims and every affirmative deficiency flag. A final geometry check
removed the draft oversized flag from BetterEnd's shadow-forest mansion: its
17 by 16 by 24 template does not establish that claim. No Item 8 evidence changed.

Local gate result, 2026-09-08: PASS. Inventory SHA-256 check OK; 448 expected and
classified IDs match exactly, with all fields and controlled values valid.
Roles: T0 152, C 97, T1 84, T2 65, T3 47, T4 3.
Confidence: H 156, M 287, L 5. Flags: D 130, S 28, O 6; theme comparison coverage
448, village candidates 17, ruin candidates 56, tower candidates 53, dungeon
archetype candidates 88. Counts overlap across flag classes, not within primary
roles. All classifications and comparisons remain provisional.

The local exit gate and required clean Codex review/main delivery are satisfied.
No required provisional
classification claim remains unsupported; empirical quality, timing, actual
redundancy and functional behavior remain explicitly outside this gate.

## PR20 review dispositions

[First completed review](https://github.com/copeugne/mcpack/pull/20#issuecomment-5576140993),
head `96c16355f3c53fe7efd07f48e985f6dc4828c142`, reported two documentation issues.
No classification finding was reported.

1. P1, prohibited dash characters in the newly tracked historical archive.
   The character finding is valid, but rewriting the user's existing verbatim
   archive would lose fidelity and contradict preservation intent. The narrow
   fix removes only the duplicate archive from the tracked PR tree, leaving the
   local file untouched, and links the active handoff to the exact immutable
   prior Git blob at `be64d458`. Git already durably preserves those bytes.
2. P2, workstation changes described as if recoverable from the reviewed tree.
   The edits/deletion were real local observations, but cannot describe a clean
   checkout. The handoff now requires inspecting actual state and explicitly
   forbids recreating uncommitted changes from its text. No user edits are staged,
   restored or deleted by this correction.

Affected checks: the local archive still compares byte for byte with
`git show be64d458:MCPACK-NEW-SESSION-HANDOFF.md`; the current handoff's immutable
link resolves that same committed history. The active handoff is below 200 lines,
new Item 9/current-handoff prose contains no prohibited dash characters, and
`git diff --check` passes. Classification data and its passing gate are unchanged.
Those findings were superseded by the clean final review recorded above.

[Second completed review](https://github.com/copeugne/mcpack/pull/20#discussion_r3952891421),
head `d96f60357fa8e51c027ca4900e50ffa52622e7f4`, requested an executable tracked
entry point for the acceptance check. The same hash/jq/whitespace logic is moved
verbatim from the README into `evidence/item-9/check.sh`, with only a Bash shebang
added. This makes clean-checkout invocation direct and avoids manual code-block
extraction. No new checks, schema, evidence class, framework or classification
changes are introduced. The documented invocation passes with unchanged results.
