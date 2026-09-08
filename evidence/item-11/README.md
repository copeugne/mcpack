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
