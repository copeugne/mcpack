# Item 6 final PR gate

Reviewed implementation: `4629fd278e1d7ba3185da0d25e4119210de3dca7`

## Local validation

| Gate | Result |
| --- | --- |
| Item 6 suite | PASS, 552 tests |
| Full suite | PASS, 679 tests |
| Ruff on 58 changed Python files | PASS |
| basedpyright on `src`, `tests`, and the public CLI | PASS, 0 errors, 0 warnings, 0 notes |
| Public Item 6 validation CLI | PASS |

## Exact-SHA review ledger

| Lane | Verdict | Source |
| --- | --- | --- |
| Goal and constraint review | PASS | `item6_final2_goal` final report |
| Code quality review | PASS | `item6_final2_code` final report |
| Security and trust-boundary review | PASS | `item6_final2_security` final report |
| Hands-on QA | PASS | `item6_final2_qa` final report |
| Context, documentation, and history review | PASS | `item6_final2_context` final report |
| H1, coordinated evidence rebinding | REFUTED | `item6_final2_h1` final report |
| H2, masked diagnostics or rejected canonical behavior | REFUTED | `item6_final2_h2` final report |
| H3, stale code or incorrect pinned identity | REFUTED | `item6_final2_h3` final report |

The three review reproductions for baseline-seed rebinding, retained-candidate substitution,
and generation-stage swapping failed before the manifest seal and pass after it. The fix is
one immutable manifest identity check plus three focused regressions. No Item 7 behavior is
included.

## Credential-path review fix

Reviewed implementation: `724071e4b96a89761700c246b683c81150fb2cea`

| Gate | Result |
| --- | --- |
| Item 6 suite | PASS, 553 tests |
| Full suite | PASS, 680 tests |
| Ruff on 58 changed Python files | PASS |
| basedpyright on `src`, `tests`, and the public CLI | PASS, 0 errors, 0 warnings, 0 notes |
| Public Item 6 validation CLI | PASS |
| Goal, code, security, QA, and context review lanes | PASS |
| H1, escaped-key bypass | REFUTED |
| H2, byte-preservation regression | REFUTED |
| H3, stale loaded implementation | REFUTED |

The exact escaped-target-key reproduction and an alternate key escape are rejected before
capture creates an output or receipt. Canonical UTF-8 capture remains byte-exact outside the
credential token.

## Parent-traversal review fix

Reviewed implementation: `882ad986f9f19ea705b8bda0e93cae33b8811d91`

| Gate | Result |
| --- | --- |
| Item 6 suite | PASS, 554 tests |
| Full suite | PASS, 681 tests |
| Ruff on 58 changed Python files | PASS |
| basedpyright on `src`, `tests`, and the public CLI | PASS, 0 errors, 0 warnings, 0 notes |
| Public Item 6 validation CLI | PASS |
| Goal, code, security, QA, and context review lanes | PASS |
| H1, alternate parent-traversal bypass | REFUTED |
| H2, ordinary capture or collision regression | REFUTED |
| H3, stale loaded implementation | REFUTED |

Absolute-shaped and relative nested parent traversal are rejected before capture creates a
directory or receipt, and an existing empty victim remains untouched. Ordinary capture and
direct existing-output preservation remain valid.
