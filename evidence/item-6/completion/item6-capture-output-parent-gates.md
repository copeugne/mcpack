# Item 6 capture output-parent symlink gate

- Scenario: direct and nested lexical output-parent links cannot redirect capture staging externally.
- RED invocation: `uv run pytest -q tests/item6/test_capture_contract.py -k symlinked_output_parent`
- RED binary observable: `CaptureValidationError` mentioning `output parent`; no external output, receipt, or staging directory.
- RED result: `2 failed` before the guard; preserved in `item6-capture-output-parent-red.txt`.
- GREEN invocation: `uv run pytest -q tests/item6/test_capture_contract.py -k symlinked_output_parent`
- GREEN result: `2 passed, 26 deselected`.
- Regression invocation: `uv run pytest -q tests/item6/test_capture_contract.py && uv run pytest -q tests/item6`
- Regression result: `28 passed`; `434 passed`.
- Static invocations: `uv run ruff format --check src/mcpack_evidence/item6_capture.py tests/item6/test_capture_contract.py`; `uv run ruff check src/mcpack_evidence/item6_capture.py tests/item6/test_capture_contract.py`; `uv run basedpyright src/mcpack_evidence/item6_capture.py tests/item6/test_capture_contract.py`
- Static result: formatted; all checks passed; `0 errors, 0 warnings, 0 notes`.
- Real CLI invocation: `uv run pytest -q tests/item6/test_capture_contract.py::test_capture_cli_writes_exact_public_layout` and `uv run tools/freeze_item6_config.py validate --root evidence/item-6/frozen --manifest evidence/item-6/generated-config-manifest.json --audit evidence/item-6/config-audit.json`
- Real CLI binary observable/result: capture emits no synthetic source value and materializes the documented layout; validator prints `validated Item 6 frozen configuration and audit`; both exit 0.
- Diff invocation/result: `git diff --check` exits 0.
