# Item 6 capture surgical-redaction gate

- Scenario: source text is structurally verified, then only `/validator/if/password`’s JSON string span changes.
- RED invocation: `uv run pytest -q tests/item6/test_capture_contract.py -k surgically`
- RED binary observable: captured bytes equal source bytes with only the target token replaced; malformed, non-string, duplicate, nonstandard, and overflow forms leave no output or receipt.
- RED result: `6 failed, 2 passed, 28 deselected`; whole-document reserialization changed unrelated bytes and accepted unsafe JSON forms. Preserved in `item6-capture-surgical-red.txt`.
- GREEN invocation: `uv run pytest -q tests/item6/test_capture_contract.py -k surgically`
- GREEN result: `10 passed, 28 deselected`, including escaped-key and second-password lexical ambiguity rejection.
- Regression invocation: `uv run pytest -q tests/item6/test_capture_contract.py && uv run pytest -q tests/item6 && uv run pytest -q`
- Regression result: `38 passed`; `444 passed`; `571 passed`.
- Static invocations: `uv run ruff format --check src/mcpack_evidence/item6_capture.py src/mcpack_evidence/item6_capture_sanitization.py tests/item6/test_capture_contract.py`; `uv run ruff check src/mcpack_evidence/item6_capture.py src/mcpack_evidence/item6_capture_sanitization.py tests/item6/test_capture_contract.py`; `uv run basedpyright src/mcpack_evidence/item6_capture.py src/mcpack_evidence/item6_capture_sanitization.py tests/item6/test_capture_contract.py`
- Static result: formatted; all checks passed; `0 errors, 0 warnings, 0 notes`.
- Real CLI invocation: `uv run pytest -q tests/item6/test_capture_contract.py::test_capture_cli_writes_exact_public_layout` and `uv run tools/freeze_item6_config.py validate --root evidence/item-6/frozen --manifest evidence/item-6/generated-config-manifest.json --audit evidence/item-6/config-audit.json`
- Real CLI binary observable/result: capture’s output, adjacent receipt, stdout, and stderr exclude the synthetic source marker; capture layout test and validation command exit 0, with validator output `validated Item 6 frozen configuration and audit`.
- Scope/result: `item6_capture.py` is 157 lines and `item6_capture_sanitization.py` is 109 lines; `git diff --check` exits 0.
