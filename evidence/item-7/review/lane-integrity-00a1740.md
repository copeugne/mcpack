# Item 7 security and evidence-integrity review at 00a1740

- Exact reviewed revision: `00a174015de96c9219565034428df2421a42c66e`.
- Verdict: `PASS`.
- Confidence: `HIGH`.

The focused archive, restore, publication, staging, release, inventory, and completion selection passed 52 tests. The cases are durably implemented in the tracked `tests/item7/test_item7_archive*.py`, `tests/item7/test_item7_completion*.py`, `tests/item7/test_item7_release_verifier.py`, and `tests/item7/test_item7_staging.py` modules. The complete reproducible superset is `uv run pytest -q tests/item7`, which passed 186 tests.

The review exercised nested symlink parents for target, receipt, archive, and manifest; competing targets; target and receipt-parent replacement races; source and output identity swaps; no-replace publication; poisoned directory offsets; special files and hardlinks; strict scalar rejection; and completion mutation cases. No escaped output was produced.

Direct inspection confirmed that create and restore operations require safely opened existing parents, use no-follow descriptor walks, verify staged contents, publish without replacement, recheck the target identity, and publish the receipt through a pinned directory.

The accepted restored r8 trees reproduced:

- 716-file world inventory SHA-256 `331bde517e6fb072a4aa0a66fb77b733559b27f92098f8fc1f236405bbe02f3e`.
- 125-artifact completion receipt SHA-256 `c369178431abba0c17404b9723a47fa66e945c305b5477c63bd5a9a6ec281582`.

Live GitHub metadata matched the annotated r8 tag, source revision, four release assets, and `publication-r8.json`. Exclusion and visual-provenance checks passed. No actionable findings.
