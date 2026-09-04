# Item 6 sanitization receipt validation gate

Commit under test: uncommitted phase-B implementation on `codex/item-6-completion`

## RED proof

- Scenario: focused receipt validation must import a dedicated callable boundary.
- Invocation: `uv run pytest -q tests/item6/test_sanitization_receipt.py`
- Binary observable: collection fails because `mcpack_evidence.item6_sanitization` is absent.
- Result: collection error, exit 2, captured in `item6-sanitization-receipt-red.txt`.

## GREEN boundary behavior

- Scenario: parse one valid receipt and reject unknown or missing fields, changed counts/path/pointer/replacement/type, malformed JSON, missing or symlinked receipt, missing or symlinked target, and a target without the sentinel.
- Invocation: `uv run pytest -q tests/item6/test_sanitization_receipt.py`
- Binary observable: valid input returns `SanitizationReceipt`; every adversarial variant raises `SanitizationReceiptValidationError`.
- Result: `17 passed`.

## Regression and static checks

- Invocation: `uv run pytest -q tests/item6`
- Binary observable: exit code 0.
- Result: `402 passed`.
- Invocation: `uv run pytest -q`
- Binary observable: exit code 0.
- Result: `529 passed`.
- Invocation: `uv run ruff format --check src/mcpack_evidence/item6_sanitization.py tests/item6/test_sanitization_receipt.py && uv run ruff check src/mcpack_evidence/item6_sanitization.py tests/item6/test_sanitization_receipt.py`
- Binary observable: exit code 0.
- Result: passed.
- Invocation: `uv run basedpyright src/mcpack_evidence/item6_sanitization.py tests/item6/test_sanitization_receipt.py`
- Binary observable: `0 errors, 0 warnings`.
- Result: passed.
- Invocation: `uv run tools/freeze_item6_config.py validate --root evidence/item-6/frozen --manifest evidence/item-6/generated-config-manifest.json --audit evidence/item-6/config-audit.json`
- Binary observable: exact CLI output `validated Item 6 frozen configuration and audit` and exit code 0.
- Result: passed.
- Invocation: `git diff --check`
- Binary observable: exit code 0.
- Result: passed.

Secret handling: this phase parses neither a source credential nor a source credential digest. The only accepted target value is the literal redaction sentinel.
