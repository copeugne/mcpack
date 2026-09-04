# Item 7 runtime audit at 785af20

- Exact revision: `785af200f51c28c7cd3183401ca306c589c8ee49`.
- Verdict: `FAIL`.
- Confidence: `HIGH`.

## Finding

`MEDIUM`: `build_save_sequence_audit` serialized `str(manifest_path)`. Equivalent relative and absolute invocations therefore emitted different JSON bytes even though the manifest identity was unchanged.

## Disposition

Commit `4e9d737` stores the manifest basename, adds a relative-versus-absolute regression, advances the save audit to v2, and requires matching unpredictable tokens around every save sequence. The old r11 audit is not accepted by the stronger gate.

The reviewer otherwise reproduced 197 Item 7 tests, the inventory, save audit, completion receipt, archive identities, export identity, and clean process state.
