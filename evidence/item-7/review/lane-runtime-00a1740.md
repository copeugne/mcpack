# Item 7 runtime debugging audit at 00a1740

- Exact reviewed revision: `00a174015de96c9219565034428df2421a42c66e`.
- Verdict: `PASS`.
- Confidence: `HIGH`.

The audit used a clean Git export and the tracked CLI, builders, and tests. It tested these hypotheses:

1. Archive creation or restoration could redirect output, follow a symlink, or accept a replaced target. A real CLI round trip and 14 adversarial archive cases passed.
2. Directory-descriptor handling could lose entries or restore unsafe files. A real r8 auxiliary restore produced 217 files, zero symlinks, and zero `session.lock` files.
3. Inventory or completion could accept stale or tampered inputs. Both tracked builders reproduced the committed files byte for byte, and strict scalar and completion tamper cases rejected.
4. Lifecycle receipts could overclaim readiness, save, stop, or cleanup. All ten applicable receipts passed their assertions, and no Java process survived.
5. A focused check could hide a regression. `uv run pytest -q` passed all 867 repository tests.

The exact inventory and completion commands are preserved in `candidate-r8-validation.md`. Their results were:

- Inventory: 716 files, SHA-256 `331bde517e6fb072a4aa0a66fb77b733559b27f92098f8fc1f236405bbe02f3e`.
- Completion: `PASS`, 125 artifacts, SHA-256 `c369178431abba0c17404b9723a47fa66e945c305b5477c63bd5a9a6ec281582`.

No new Minecraft generation was launched in this read-only audit. The accepted lifecycle receipts and exact-SHA tests cover the required runtime boundaries. No actionable findings.
