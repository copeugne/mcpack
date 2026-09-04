# Item 6 capture-side sanitization gate

Commit under test: uncommitted phase-A implementation on `codex/item6-secret-capture`

## RED proof

- Scenario: a normal capture must create a safe receipt and a malformed target must abort without output.
- Invocation: `uv run pytest -q tests/item6/test_capture_contract.py -k 'redacts_generated or invalid_resourceful'`
- Binary observable: receipt absent and malformed JSON accepted before implementation.
- Result: `2 failed, 23 deselected`, captured in `item6-capture-sanitization-red.txt`.

## GREEN capture behavior

- Scenario: a normal source instance is captured through the public CLI subprocess; missing and malformed target configurations abort without output.
- Invocation: `uv run pytest -q tests/item6/test_capture_contract.py -k 'redacts_generated or invalid_resourceful or capture_cli'`
- Binary observable: `config/resourceful-config-web.json` has `<redacted-generated-secret>` at `/validator/if/password`; the adjacent `config-sanitization.json` has one redaction, contains neither the synthetic source value nor any hash field, and CLI stdout and stderr do not contain the synthetic source value.
- Result: `4 passed, 22 deselected`.

## Regression and static checks

- Scenario: Item 6 capture contract and frozen-evidence regression.
- Invocation: `uv run pytest -q tests/item6/test_capture_contract.py tests/item6/test_frozen_config.py`
- Binary observable: exit code 0.
- Result: `36 passed`.
- Invocation: `uv run ruff format --check src/mcpack_evidence/item6_capture.py tests/item6/test_capture_contract.py && uv run ruff check src/mcpack_evidence/item6_capture.py tests/item6/test_capture_contract.py`
- Binary observable: exit code 0.
- Result: passed.
- Invocation: `uv run basedpyright src/mcpack_evidence/item6_capture.py tests/item6/test_capture_contract.py`
- Binary observable: `0 errors, 0 warnings`.
- Result: passed.
- Invocation: `git diff --check`
- Binary observable: exit code 0.
- Result: passed.
- Invocation: `uv run pytest -q tests/item6`
- Binary observable: exit code 0.
- Result: `377 passed`.

Secret handling: all captured evidence uses the literal redaction sentinel. This receipt intentionally stores no source credential, source hash, or source digest.
