# Automated measurement scope amendment

Decision date: 2026-09-08. Status: AUTHORIZED, delivery review pending.
Contract identifier: `item10-automated-v1`.

The user explicitly directed: "No human phase in either 10 or 11 I see no point
for it, send it over." This supersedes the earlier human-session, recording and
two-blind-operator requirements for Items 10 and 11. No human workload is moved
to another item as a condition of their completion.

## Item 5 applicability

The frozen `measurement/item5/protocol-v1.json` and accepted Item 5 pilot evidence
remain unchanged as historical versioned artifacts. For Items 10 and 11, this
amendment and the revised SPECS replace their human collection contracts and the
generic player-case, warm-up, duration and repetition matrix applied to static
world measurements. They do not invalidate the recorded runtime measurements or
change the frozen runtime/configuration identity. Other Item 5 metrics retain
their existing scope unless separately amended.

The Item 5 methodology coverage gate is reopened narrowly for this contract
change until the revised definitions and affected downstream assumptions pass
review and durable delivery. Do not rerun its runtime pilots or Items 7 through
9 merely because their downstream consumer changed. Full Item 10 collection
still requires a frozen, complete sampling protocol and resolved occurrence
coverage. The existing pilot remains diagnostic evidence.

## Item 10 quantities

Measure generated location placements, not experienced gameplay. Use accepted
canonical families and preserve their provisional confidence and ambiguity.

| Quantity | Automated definition |
| --- | --- |
| Structure density | Verified registry starts plus validated nonregistry location occurrences, with lifecycle sites reported separately. |
| Actionable-candidate density | Locations assigned C or T1 through T4 by Item 9. This operational category excludes T0 incidental salvage; it does not prove realized utility or meaningful interaction. |
| Encounter-site density | Locations assigned T1 through T4. These include traps, creature interaction and search objectives; they are not a count of fights or even exclusively hostile sites. |
| Proper-dungeon density | Exclusive provisional T2 location count. |
| Major-expedition density | Exclusive provisional T3 location count. Report T4 world objectives separately rather than assuming every objective is a dungeon. |
| Village density | Locations whose accepted Item 9 comparison groups include `village`; retain role and ambiguity, including mixed or abandoned variants. |
| Spatial/biome/seed comparisons | Predeclared complete saved-world exposure, explicit coordinate conventions, boundary censoring and sparse-category limitations. |
| Sparse Structures contribution | Verified placement mechanism and a predeclared matched automated control for the observed distribution. No tuning of the accepted baseline. |

All densities use the selected full-chunk denominator for the same seed and
stratum. Raw observations, identity, failures, uncertainty, deterministic
processing, archive restore, review and merge gates remain mandatory. Static
hostility may be retained as a source descriptor but is never relabeled observed
combat. Actual fight frequency, human recognition, subjective actionability,
enjoyment and meaningful-interaction time are NOT MEASURED by this contract.

## Item 11 requirements boundary

Item 11 becomes automated route opportunity and repetition analysis. Its later
protocol must predeclare route geometry, transport capability assumptions,
endpoints, geometric visibility rules, and any travel-time model. It will report
route-adjacent candidate locations, geometric visibility proxies, candidate
category counts, gaps, family repetition and modeled travel costs. Report failed
or infeasible routes and transport limitations rather than substituting another
mode silently. Modeled time is not observed player travel time.

The human Adventure Activity Ratio and time to human recognition are not
acceptance requirements for Item 11. A route opportunity fraction, if used, must
have its own explicit numerator and denominator and must not be called measured
meaningful-interaction time. Do not infer subjective experience from static
geometry or automated traversal. No human evidence or blind operators are
required for Item 10 or Item 11 completion.

This document changes requirements only. It does not implement, run, repair or
lint Item 11 workflows. Item 11 execution remains gated on Item 10 delivery and
the cross-item identity/narrative audit of Items 2 through 10. Existing human
runbooks, schemas and reconstructed summaries are not active acceptance paths
for the revised Item 11 and must not be treated as proof of its completion.
