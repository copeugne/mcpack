# Post-baseline plan consolidation

Decision date: 2026-09-10. Status: user-authorized specification amendment;
implementation of requirements 19-51 remains UNSTARTED. This does not start or
complete Item 19 and does not change the active Item 13 scope or Items 14-18.

## Authority and purpose

The user requested keeping work through Item 18 uncompressed, then consolidating
the remaining tasks while preserving their substance and essence. The subsequent
instruction explicitly authorized making the changes now and documenting them
from code, the web or commits/PRs. This amendment implements that request using
the actual versioned repository specification, not external mod recommendations.

The source is [SPECS.md at the delivered PR40 main revision](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md),
commit 3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf. This is the immutable input
for the source mapping and baseline-preservation comparison below. The amendment
changes the post-baseline specification, its ledger reference and this provenance
record. It does not alter earlier requirements or empirical evidence.

## What changed

[SPECS.md](../../SPECS.md#post-baseline-delivery-seven-work-packages) replaces the
33 later administrative items with seven delivery packages. Legacy numbers remain
stable requirement IDs. The ledger links package execution while retaining its
legacy status ranges; those rows do not require separate delivery workflows.
Items 1-18, their evidence requirements and their current branch-specific amendments
are outside this change. Existing ledger governance and whole-pack audit obligations
are not waived by the shorter adventure plan.

A single package report can serve its constituent requirements. Shared observations,
source evidence and affected checks need not be duplicated. There is no mandatory
protocol, validator, PR or completion-record commit per legacy ID. Internal scientific
and implementation gates remain; coherent commits/PRs can divide an irreducibly large
package without creating unrelated administrative tasks. Package E explicitly keeps
48A-F as implementation increments with affected regression, satisfying the ledger's
existing atomization requirement.

Seven packages: A design (19-37), B candidate selection (38-40), C dungeon/worldgen
(41-43), D encounters (44-45), E rewards/integration (46-48), F performance/lifecycle
(49-50), G release (51). All begin after the original Item 18 gate; chronological
internal dependencies remain explicit. This is workflow compression, not completion,
mod selection, baseline remeasurement or authorization for runtime experiments.

## Requirement provenance

Every row below points directly to the original requirement at the immutable source
commit. The same numbered subsection in current SPECS.md is its consolidated
successor. Subsections 48A-F and 50A-G remain explicit inside their parent items.
The old source is an audit reference, not a second executable task queue.

| Legacy source | Package | Retained requirement |
| --- | --- | --- |
| [19](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L544) | A | Define the Final Adventure Structure Taxonomy |
| [20](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L583) | A | Define the Transportation-Scale Model |
| [21](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L610) | A | Define Target Adventure Cadence |
| [22](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L636) | A | Define Dungeon Topology Requirements |
| [23](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L658) | A | Define Dungeon Objective Variety |
| [24](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L683) | A | Define Dungeon Persistence and Repeatability Policy |
| [25](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L707) | A | Define the Difficulty Model |
| [26](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L739) | A | Define Enemy Role and Encounter Archetypes |
| [27](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L771) | A | Define Elite, Miniboss, and Boss Philosophy |
| [28](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L789) | A | Define the Loot Economy |
| [29](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L820) | A | Define Reward Renewability and Automation Rules |
| [30](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L842) | A | Define Engineering and Adventure Integration |
| [31](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L876) | A | Define Discovery and Navigation Progression |
| [32](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L903) | A | Define Multiplayer Expedition and Loot Rules |
| [33](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L929) | A | Define Civilization and Settlement Roles |
| [34](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L948) | A | Define Dimension Roles |
| [35](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L966) | A | Define Combat-Mod Boundaries |
| [36](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L990) | A | Define Destructibility, Breaching, and Automation-Bypass Policy |
| [37](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L1020) | A | Define Expedition Preparation, Failure, and Recovery |
| [38](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L1047) | B | Perform Early Candidate-Mod Feasibility Screening |
| [39](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L1072) | B | Run Controlled Structure-Redundancy Experiments |
| [40](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L1101) | B | Freeze the Provisional Content and Worldgen Stack |
| [41](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L1120) | C | Integrate and Evaluate the Proposed Underground Dungeon Layer |
| [42](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L1149) | C | Re-Measure the Combined Provisional Worldgen Stack |
| [43](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L1175) | C | Iteratively Tune Sparse Structures and Structure Essentials |
| [44](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L1207) | D | Implement Encounter Orchestration and Test Composition Alone |
| [45](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L1235) | D | Evaluate AI and Elite Layers Incrementally |
| [46](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L1290) | E | Implement Multiplayer Container and Persistence Rules |
| [47](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L1316) | E | Freeze the Adventure-Relevant Engineering and Combat Stack |
| [48](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L1336) | E | Implement Loot, Discovery, Civilization, and Engineering Integration |
| [49](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L1413) | F | Validate Performance of the Final Candidate System |
| [50](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L1463) | F | Run Early-, Mid-, Late-, and Mature-Server Validation |
| [51](https://github.com/copeugne/mcpack/blob/3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf/SPECS.md#L1571) | G | Validate Definition of Done and Freeze Adventure v1 |

## Retained acceptance boundaries

- All 19-37 roles, duration targets, transport/cadence dimensions, dungeon objectives,
  persistence, difficulty, reward/automation, engineering, discovery, multiplayer,
  settlement, dimension, weapon, breaching and recovery policies remain mandatory.
  Material product choices require a concrete ratified proposal, not invented values.
- All named candidate checks and controlled removal comparisons remain in 38-40.
  Named candidates are not automatically accepted or re-enabled after prior rejection.
- Dungeon acceptance still precedes combined-stack measurement and spacing tuning
  (41 -> 42 -> 43). A rejected dungeon layer does not silently pass the missing gap.
- Composition-only testing still precedes incremental AI and elite evaluation (44 ->
  45). Individual comparisons, conditional candidates and server/gameplay costs remain.
- Container semantics and the final item-provider stack precede exact rewards
  (46 -> 47 -> 48). All six implementation domains retain focused regression.
- All performance cases, retained tooling checks, growth/backup/restore work, seven
  gameplay/redundancy/regression domains and final release criteria remain in 49-51.
  Modeled scope for an earlier baseline item does not automatically substitute for
  later gameplay tests.
- Frozen identities, raw-evidence durability, failure dispositions, review/fix loops,
  completed clean Codex review/thumbs-up, merge and verified main delivery remain
  governed by AGENTS.md. Administrative grouping cannot make an unknown value pass.

## Verification and limits

Direct comparison confirms the entire prefix before Phase III, including Items 1-18,
is byte-identical to the source commit. Prefix SHA-256: c39f508db24ccecb1961ffe526790aa2ee6e586f46eac3053d8b4014851fe0ac.
All 33 legacy headings occur exactly once in the replacement, and all 32 explicit
original dependency sets (19-50) match. Item 51 retains the all-prior-work release
gate. The post-baseline specification goes from 1220 to 487 lines, including
the execution rules and dependency map. These counts prove structure/preservation
boundaries, not semantic completeness by themselves.

A direct reading of the original checklists against each replacement subsection
checked named systems, numeric targets, scenarios, prohibitions, internal order and
release criteria. The provenance table and PR diff make that judgment reviewable.
No runtime/code tests are required for this documentation-only amendment. Focused
checks cover unchanged baseline bytes, IDs, dependencies, local links, punctuation,
whitespace and ledger consistency. No new validator or test framework is added.

The initial dependency comparison reported a textual difference for Item 20:
original "11-12 and 19" versus "11-12, 19". Normalizing that conjunction yields the
same dependency set; there was no missing dependency or specification correction.

Reproduce the mechanical boundary checks from repository root:

```sh
uv run python - <<'CHECK'
from pathlib import Path
import re, subprocess
old = subprocess.check_output(['git','show','3a086467fcd25fffd3b39ed3112d5cb49a0a7bdf:SPECS.md'], text=True)
new = Path('SPECS.md').read_text()
assert old.split('# PHASE III')[0] == new.split('# POST-BASELINE DELIVERY')[0]
assert [int(n) for n in re.findall(r'^### (\d+)\.',new,re.M)] == list(range(19,52))
current = {int(n):d for n,d in re.findall(r'^\| (\d+) \| (.*?) \|$',new,re.M)}
for m in re.finditer(r'^## (\d+)\. .*?\n(.*?)(?=^## \d+\.|\Z)',old,re.M|re.S):
    n = int(m[1])
    dep = re.search(r'### Depends On\n- (Items? .*?)\n',m[2])
    if n >= 19 and dep:
        expected = re.sub(r'Items? |\.$','',dep[1]).replace(chr(8211),'-').replace(' and ', ', ')
        assert current[n] == expected, (n,current[n],expected)
assert len(re.findall(r'^## Package ',new,re.M)) == 7
assert not any(c in new.split('# POST-BASELINE DELIVERY')[1] for c in (chr(8211),chr(8212)))
print('Unchanged baseline prefix; 33 IDs; retained dependencies; seven packages: PASS')
CHECK
git diff --check
```

This command deliberately verifies against the amendment's source. A later accepted
change to Items 1-18 requires its own provenance rather than rewriting this historical
preservation claim.

A read-only prospective integration check found that replacing future ledger rows
adjacent to baseline status changes would create a merge conflict. The edit was
narrowed to the governing-plan explanation and the already-atomized Item 48 note.
The seven delivery packages remain authoritative in SPECS.md. This avoids coupling
the plan amendment to unrelated baseline status edits.
