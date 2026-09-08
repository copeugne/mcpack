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

## Representative slice

Ordinary repetition 1 baseline passes the first-world route gate. The
[accepted result](results/full-ordinary-r1-baseline.json.gz) binds the exact
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
