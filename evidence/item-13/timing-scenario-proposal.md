# Accepted complete-objective timing scenario

Status: ACCEPTED as a conditional modeled scenario on 2026-09-10. The user
approved this concrete proposal with "i approve" after its delivery at commit
9b863297a34f7792873b298697075967864db70f. Approval covers the declared provisional
allowances and reusable complete-task cost accounting. It does not waive timing,
validate pickup geometry, establish observed gameplay or complete Item 13.
Item 14 remains UNSTARTED.

## Objective and conditions

Reuse the [supplemental Circle evidence](fixed-blocks/mns-circle_nether_brick-report.md#complete-objective-timing-demonstration-v2),
including its exact saved identity, source mechanics and validated inspection
circuit. Start at the local southern entry station(368.5,33,85.5), disable both
spawners, defeat their spawned hostiles, collect both ancient-debris blocks into
inventory, and return alive to that station. Discovery and travel to this local
entry are outside the task. Inspection contact alone is not completion.

Actor: one adult player, full health and food, unenchanted iron armor/sword and
diamond pickaxe, sufficient durability, three accessible tool selections and
free inventory capacity. Full layout/target knowledge, no effects, criticals,
sweeps, external help, flight, teleportation, extra construction or healing.
Damage is permitted; survival is a success condition, not predicted by this
model. The actor mines both spawners before voluntarily attacking, then clears
the encounter, acquires the two rewards and exits. The existing trapdoor toggle,
one ore-cover removal and shift crossing are permitted.

Encounter starts with no pre-existing mobs, natural spawning excluded, and both
saved spawners active at Delay 0. This is a stipulated scenario, not the observed
population of the accepted world. Let p and b be successful ordinary unarmored
piglin and brute counts, independently 0..4. Counts are scenario inputs, not
probabilities. Both spawners must be disabled before 200 game ticks; otherwise
the single-batch population model is invalid. No extra passengers, equipment,
effects or reinforcements are included.

## Costs, sources and provisional allowances

All three columns are analyst-selected sensitivity cases. They are not percentiles,
empirical calibration, player skill categories or claims about typical behavior.
Use 20 TPS as a scenario condition. The underlying route speeds and combat duty
fractions are also modeled assumptions, even where reused from earlier evidence.

| Component | A | B | C | Basis and rationale |
| --- | ---: | ---: | ---: | --- |
| Upright travel speed, blocks/s | 5 | 4 | 3 | Existing movement sensitivity assumptions |
| Crouched travel speed, blocks/s | 1.5 | 1.2 | 0.9 | Existing movement sensitivity assumptions |
| Six navigation/decision events, seconds each | 0.5 | 1 | 1.5 | Provisional short known-layout pauses: initial orientation, selecting the spawner sequence, confirming disablement/combat transition, selecting the southern reward, selecting the northern route/reward, selecting return route |
| Six targeting/interaction events, seconds each | 0.25 | 0.5 | 1 | Provisional allowance to aim at each of five mined blocks plus operate the trapdoor; includes mining input initiation and inter-block input delay, excluding actual breaking work |
| Three tool selections, seconds each | 0.25 | 0.5 | 1 | Pickaxe before spawners, sword for combat, pickaxe for resources. Separate from aiming/navigation |
| Two acquisition events, seconds each | 1 | 2 | 4 | Provisional local pickup/inventory-confirmation budget, including any remaining pickup eligibility wait. Not a claim that every drop can be collected within it |
| End-of-task verification, seconds | 2 | 4 | 8 | Provisional check that both resources are held and no modeled hostiles remain before final return completion |
| Combat contact duty | 1 | 0.75 | 0.5 | Sensitivity for target switching, pursuit, attack repositioning and pauses within the combat phase; active attack work comes from pinned source |

These values deliberately span several multiples for input and acquisition costs
instead of presenting an unsupported universal action speed. They are accepted
provisional working budgets for a specified successful scenario. Increasing them
can invalidate the spawner deadline, so they cannot be adjusted independently
of encounter conditions.

Reuse 22 upright and four crouched blocks in the existing circuit. Provisionally
allocate four additional upright blocks per reward for approach to pickup contact
and return to the circuit: eight additional blocks total. This extra path is an
analyst-selected budget, NOT a validated pickup route. Its rationale is a short
local excursion from each already verified face-access station. Feasible pickup
within that budget is a conditional assumption, not a consequence of ray reach.
If it fails, censor the scenario; do not call the current route a proven harvest.
The approved scenario accepts this conditional budget; no pickup observation
is claimed.

Uninterrupted mining is the source-derived 276 ticks/13.8 seconds for two
spawners, one ore cover and two debris with the declared diamond pick. Source
attack work is 1.95p+5.85b seconds, divided by selected combat duty. These are
nominal mechanism calculations, not retained-runtime performance measurements.

## Schedule and avoidance of double counting

Use sequential task phases: approach and spawner disablement; combat; resource
work/acquisition; return and completion verification. Movement along the circuit
and the eight pickup blocks excludes combat pursuit, which is included only in
the contact-duty allowance. Navigation allowances represent stationary decisions,
not movement or aiming. Tool changes, targeting, actual mining and acquisition
are separate. Charge no extra attack-switch or pursuit constant on top of duty.
Combat begins and ends at the inner approach station; duty includes any return
from pursuit to that station. The six decision budgets also cover reorientation
and the four shift-pose transitions on the outbound/return route. No additional
pose latency is silently required outside those provisional allowances.
The ten-tick source pickup delay is included in acquisition allowances, not added
again; it may already expire during movement. There is no separate healing term
because healing is outside this successful scenario.

Initial orientation and spawner-sequence choice are two decision events before
the second disablement. Two mining-target events and one tool selection also
precede it. Thus, with upright speed u, decision allowance n, targeting a and
selection s, second disablement is modeled as D=4/u+1.9+2n+2a+s seconds.
A/B/C give 4.45/6.4/9.233333 seconds, all below the ten-second condition. C has
less than a second of margin. Unbudgeted mining interruption or displacement
can invalidate this condition; the model does not guarantee successful rushing.

Total successful-scenario time is:

T = 30/u + 4/c + 13.8 + 6n + 6a + 3s + 2k + v + (1.95p+5.85b)/d,

where c is crouched speed, k acquisition allowance, v verification and d duty.
All required phases have a numerical cost or explicit scenario exclusion.

| Worked result | A | B | C |
| --- | ---: | ---: | ---: |
| Noncombat budget, seconds | 31.7 | 43.1 | 62.2 |
| Two piglins and two brutes, seconds | 47.3 | 63.9 | 93.4 |
| Scenario grid p,b independently 0..4, seconds | 31.7..62.9 | 43.1..84.7 | 62.2..124.6 |

Report the worked example as approximately 47/64/93 seconds, and the entire
specified grid as approximately 32..125 seconds. Neither is a confidence interval,
guaranteed bound on gameplay, probability-weighted expectation or difficulty score.
Keep profile and composition visible; do not collapse them into one average.

## Failures, uncertainty and acceptance

Censor successful-completion timing on death, required healing, failed pickup
within the assumed path/budget, extra mobs/equipment, spawner disablement at or
after 200 ticks, input/mining interruption beyond allowances, invalid target
access, or tick-rate conditions outside the scenario. Report which condition
failed and elapsed time if actually observed; never fabricate such an observation.
An interruption already represented inside combat duty is not a second failure
or charge. There is no estimated survival or scenario-success probability.

This approval establishes a transparent conditional complete-task estimate
and a reusable cost-accounting method, alongside source/geometry evidence and
explicit failure conditions. It does not establish observed human timing, typical
first-clear time, guaranteed acquisition/survival, actual baseline entity counts
or completion of Item 13's family/variant coverage and review/delivery gates.
A future claim of validated pickup would require a focused pickup test for each
casing on fresh verified materialization; it is not established by this approval.

Reproduce all arithmetic without adding machinery:

```sh
uv run python - <<'SCENARIO'
profiles = [('A',5,1.5,.5,.25,.25,1,2,1),
            ('B',4,1.2,1,.5,.5,2,4,.75),
            ('C',3,.9,1.5,1,1,4,8,.5)]
for name,u,c,n,a,s,k,v,d in profiles:
    base = 30/u+4/c+13.8+6*n+6*a+3*s+2*k+v
    disable = 4/u+1.9+2*n+2*a+s
    assert disable < 10
    print(name,'noncombat',base,'p=b=2',base+15.6/d,
          'p=b=4',base+31.2/d,'second disable',disable)
SCENARIO
```
