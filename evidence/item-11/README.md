# Item 11 automated route opportunities and repetition

Status: IN PROGRESS. No route measurements accepted yet.
The [predeclared protocol](protocol.md) defines the smallest complete deliverable:
64 fixed Overworld transects across sixteen accepted worlds, evaluated under
walking, horse and boat capability models. No new world generation or tuning.

## Dependencies and reusable evidence

Fetched main is `5ec24115b9394ef162bdff6f65a31180dbb7d7ff`. GitHub confirms PR36
MERGED with reviewed head `0201d5e7737ce033875a498317a8a470bcb1853e` contained in
main. The final review is linked in the active handoff. PR35 and PR36 deliver
Item 10 and the Items 2 through 10 audit. No audit or prior item is repeated.
The two housekeeping commits `1f70f395` and `022990e3` remain preserved ancestors
of the new branch, which merges current main without rewriting either history.
Their content is not claimed to have passed PR36 review.

Reuse [Item 10's accepted results and custody](../item-10/README.md),
[protocol](../item-10/protocol.md), [identity audit](../item-10/cross-item-audit.md),
[448-family inventory](../item-8/inventory.json), and
[provisional classification](../item-9/classification.md). The exact frozen
Minecraft, NeoForge, Java, retained runtime, configuration, observer and per-arm
identities are in the cross-item audit. Read-only analysis must bind to those
accepted per-world inputs. Baseline and omit-only Sparse controls stay separate.

Available and awaiting integration: accepted classified coordinates, registry
piece envelopes, nonregistry anchors, complete censuses, world manifests, restored
Anvil files, and existing Anvil/NBT/heightmap/palette decoders. All sixteen census
hashes match the committed accepted comparison. Existing Item 7 archive restoration
and Item 4 POSIX world locks provide the custody/lifecycle path. These establish
inputs, not route visibility or transport feasibility.

Genuinely missing: fixed-route measurements, ray-clear geometric proxies, transport
failure/prefix records, route coverage denominators, gaps and repetition, modeled
costs and sensitivity. The historical Item 11 runbook describes a superseded
zero-mod human study and references absent scripts. It is not usable measurement
logic or evidence. Existing Item 5 runtime travel records are not modeled route
costs under the amended contract.

## Definition of done

| Current Item 11 requirement | Minimum accepted evidence |
| --- | --- |
| Routes, endpoints and three capabilities predeclared | Protocol committed before extraction, complete fixed matrix. |
| Failed/infeasible routes and limitations | Every route/mode row retained, reasons and reachable prefixes. |
| Adjacent candidates and visibility | Hash-bound candidate joins, saved geometry and declared ray results. |
| Actionable, encounter, T2, T3, T4 and villages | Reused Item 9 membership and per-route counts, including zeroes. |
| Gaps and repetition over fixed distances | Ordered event observations, exact windows and censored boundaries. |
| Opportunity coverage | Explicit discrete geometric numerator and full/prefix denominators. |
| Modeled costs and intervals | Declared speeds/capabilities, sensitivity and infeasibility handling. |
| Distinct measurement claims | Placement, geometry and modeled accessibility reported separately. |
| Human exclusions | Recognition, fights, interaction time, enjoyment and human Activity Ratio NOT MEASURED. |
| Reproducibility and delivery | Tracked commands/logic, focused tests, manual result check, complete final gate, durable evidence, clean final Codex PR review, merge and verified main. |

Current batch: predeclaration and source integration. Next: ordinary r1 baseline
representative slice, then reassess measured resource cost before full expansion.
No Item 12 work is authorized in this task.

## Representative slice (initial acceptance, now reopened)

Ordinary repetition 1 baseline passes the first-world route gate. The
[initial result, now rejected](rejected-lock-attempt/results/full-ordinary-r1-baseline.json.gz) binds the exact
census, archive manifest, backup manifest, protocol and analyzer hashes. Complete
restored-world inventory checks pass before and after the locked read. The result
retains 9,216 top-cell observations, four routes, all three transport models,
three radii, three windows and ten category groups. Existing input/classification
identity regression plus eight route tests pass. Ruff and BasedPyright pass.

The [first pilot](pilot/ordinary-r1.json.gz) and [timing](pilot/attempt1.txt)
retain an interim result before adjacent-repeat modeled times were integrated.
It is not the accepted result. The complete [second timing](pilot/attempt2.txt)
is 43.722 seconds; accepted output is 325,480 bytes, SHA-256
`3f67cacc9d018f5489e94168c7646d8d8a44bd9c1ad5a5e3eab3dfda8b81b0a6`.
Linear projection is 699.552 seconds and 5,207,680 result bytes for sixteen worlds,
not a measured full-run cost. A mid-run process sample showed 256,372 KiB RSS;
this is not peak-memory measurement. The pilot is comfortably within the declared
2 GiB memory, 1 GiB output and provisional 160-minute runtime allowances.

Manual result inspection: all four fixed transects have water top cells and
MODEL_FEASIBLE boat corridors. Walking and horse are INFEASIBLE from the initial
station, with all failed stations preserved. This is consistent with the model's
no-swimming assumption, not a general claim that those modes cannot explore seed
42. At radius 64 and distance 768, adjacent counts are 65/82/119/59 in route
order east-north/east-south/south-east/south-west; ray-clear counts are 1/0/1/0.
Covered blocks are 120/0/56/0. Actionable ray-clear counts are zero on all four.
The contrast retains underground candidate density separately from geometric
visibility and modeled accessibility. No desirable-pacing claim is made.

The first test invocation failed because the new test directory lacked its package
marker; adding the existing repository package pattern resolved collection.
Initial syntax and type-check errors were corrected before representative reading.
These development failures did not modify raw worlds or produce accepted evidence.
No processing exception occurred in either representative invocation.

Reproduce the accepted representative slice into an absent output path:

```sh
uv run --no-sync python -m tools.analyze_route_opportunities \
  --name full-ordinary-r1-baseline --output /tmp/item11-ordinary-reproduction.json.gz
cmp evidence/item-11/results/full-ordinary-r1-baseline.json.gz /tmp/item11-ordinary-reproduction.json.gz
uv run --no-sync pytest -q tests/item11 tests/item10/test_collection_runner.py::test_committed_cross_item_identity_bindings
```

The invocation was executed with the committed result path; the `/tmp` example
is a new-output destination and its exact invocation is pending final reproduction.
Next batch: the other fifteen accepted worlds, retaining this same protocol and
analyzer identity. Full-report integration and final delivery remain incomplete.

## Reopened lock boundary and narrow correction

The initial representative acceptance above is **REOPENED and superseded**.
Code review during the first expansion found that `open_tree` opened and then
closed `session.lock` even though the result comprehension excluded its row.
POSIX record locks are process-associated: closing that other descriptor released
the lock held by `_world_backup_lock`. The
[direct failing test](validation/lock-regression-before.txt) reproduced a second
process acquiring the lock while the analysis context was still active.

The fix reuses Item 4's existing `_backup_paths`, which excludes `session.lock`
before opening anything, and Item 7's safe regular-file opening and descriptor
hashing. It preserves exact complete-file-inventory equality and rejects symlinks.
No new locking system, schema, validator or archive revision is introduced.
The [focused regression](validation/lock-regression-after.txt) now passes all nine
Item 11 tests, including a real competing POSIX lock probe. Affected Ruff and
BasedPyright pass. The first broad Item 7/10/11 suite passed 590 tests in 173.03
seconds before this correction; it is retained as earlier regression evidence,
not proof of the corrected lock boundary.

The original representative output and two completed biome-diverse r1 outputs
are retained in [rejected-lock-attempt/results](rejected-lock-attempt/results/).
The [interrupted biome-diverse r2 log](rejected-lock-attempt/timing/full-biome-diverse-r2-baseline.txt)
preserves the processing interruption. No server was running, and inventory
checks found no changed world bytes. Nevertheless these outputs cannot satisfy
the promised continuously held lock and are rejected as current acceptance.
The new representative read uses the same immutable world, sampling and models.

The [corrected representative result](results/full-ordinary-r1-baseline.json.gz)
now passes: 47.414 seconds and 325,474 bytes, SHA-256
`d59cc1ddfe3924ddef69e0efdde2d3477889401d7fd68fa16bcc12e13fd64672`.
A [complete comparison](validation/corrected-pilot-comparison.txt) confirms that
all measurements and other input identities equal the rejected prior result;
only the analyzer digest changes. The corrected lock probe proves exclusion
before opening. Expansion can resume under the corrected analyzer identity.

## Complete generated measurement matrix

All sixteen corrected invocations have passed their complete world-inventory
checks and deterministic route processing under analyzer source `ff77c6f6`.
The [result directory](results/) contains 19,351,171 compressed JSON bytes;
[producer outputs and timings](validation/full/) bind every result's SHA-256
and size. Successful invocation times sum to 896.573 seconds, with per-world
range 45.509 to 85.163 seconds. These are processing costs, not gameplay or
production-server performance. Diagnostics and clean reproduction are additional.
The generated matrix is isolated in its own commit because its binary JSON
artifacts are the inseparable outputs of the fixed matrix; source implementation
and direct regressions were already delivered in the preceding milestones.

The representative invocation above was followed by this executed collection
command. Existing outputs are deliberately refused; use absent output paths when
reproducing. No original world is regenerated or mutated by the analyzer.

```sh
uv run --no-sync python - <<'PY' > /tmp/mcpack-item11-remaining.txt
from tools.analyze_route_opportunities import accepted_inputs
print('\n'.join(n for n in accepted_inputs() if n != 'full-ordinary-r1-baseline'))
PY
while IFS= read -r name; do
  { time uv run --no-sync python -m tools.analyze_route_opportunities --name "$name" --output "evidence/item-11/results/$name.json.gz"; } > "evidence/item-11/validation/full/$name.txt" 2>&1 || exit 1
done < /tmp/mcpack-item11-remaining.txt
```

Verify identities directly from existing producer outputs, without another
measurement or an additional manifest:

```sh
uv run --no-sync python - <<'PY'
import hashlib,json
from pathlib import Path
from tools.analyze_route_opportunities import accepted_inputs
for name in accepted_inputs():
    result=Path('evidence/item-11/results')/(name+'.json.gz')
    record=json.loads((Path('evidence/item-11/validation/full')/(name+'.txt')).read_text().splitlines()[0])
    assert (record['world'],record['output_bytes'],record['sha256']) == (name,result.stat().st_size,hashlib.sha256(result.read_bytes()).hexdigest())
print('PASS: sixteen produced result identities')
PY
```
