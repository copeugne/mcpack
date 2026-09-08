# First full ordinary baseline

Status: GENERATED, CONFIGURATION REVALIDATED; census, custody and location
acceptance remain pending. Generation source: `7b977af6`. Seed: `42`.

The original [run receipt](run.json) is preserved unchanged. All eleven declared
generation selections finished, the correlated flush passed, and Java exited
cleanly with code 0 after 497.453 seconds. This is 46,475 requested generation
chunks, not yet proof of the 45,056 selected saved-chunk denominator.

The harness then rejected configuration capture because its Item 7 default
allowlist included only three dimension task files. The exact difference was
the seven Chunky task files for Aether and the six Creating Space dimensions.
No frozen configuration file was missing. The capture boundary now derives the
full allowlist from the already-fixed Item 10 selections; Item 7 defaults and
explicit single-dimension overrides remain unchanged. It still rejects missing
or unexplained files and semantic drift in all 228 frozen files.

[Configuration revalidation](configuration-revalidation.json) accepts the stopped
instance. Its new sanitized capture matches all 239 original captured files
byte-for-byte: 228 frozen files plus 11 Chunky files. The original rejection was
not rewritten, the configuration was not tuned, and the world was not regenerated.
Focused validation: `uv run --no-sync pytest -q
tests/item7/test_worldgen_config_capture.py tests/item7/test_worldgen_lifecycle.py
tests/item10/test_collection_runner.py` (37 passed); focused Ruff and type checks
also pass. Negative cases retain rejection of a missing task or unexplained file.

## Revalidation command

The following executed command requires the preserved stopped instance and an
absent `config-revalidation` output. Do not overwrite the retained outputs.

```sh
uv run --no-sync python - <<'PY'
import json
from pathlib import Path
from mcpack_evidence.item7_config import capture_runtime_configuration
from mcpack_evidence.item7_runtime import WorldgenRequest, sha256_file
from mcpack_evidence.item7_selections import ITEM10_SELECTIONS
raw = Path('evidence/raw/item10/full-ordinary-r1-baseline')
request = WorldgenRequest(
    pristine=Path('instances/pristine-baseline-v0'),
    artifact_manifest=Path('evidence/item-3/artifact-acquisition-manifest.json'),
    retained_manifest=Path('evidence/item-3/runtime/retained-server-candidates.txt'),
    seed_suite=Path('test-environment/seed-suite.json'),
    frozen_config=Path('evidence/item-6/frozen'),
    frozen_manifest=Path('evidence/item-6/generated-config-manifest.json'),
    config_audit=Path('evidence/item-6/config-audit.json'),
    java_home=Path('downloads/item2/temurin/extracted/jdk-21.0.12.1+1'),
    role='ordinary', target=Path('instances/item10/full-ordinary-r1-baseline'),
    log_path=raw/'console.log', captured_config=raw/'config-revalidation/captured-config',
    mode='item10', selections=ITEM10_SELECTIONS, timeout_seconds=14400,
)
receipt = capture_runtime_configuration(request)
original = {p.relative_to(raw/'captured-config').as_posix(): sha256_file(p)
            for p in (raw/'captured-config').rglob('*') if p.is_file()}
new = {p.relative_to(request.captured_config).as_posix(): sha256_file(p)
       for p in request.captured_config.rglob('*') if p.is_file()}
assert original == new
result = {'original_diagnostic_sha256': sha256_file(raw/'diagnostic.json'),
          'unchanged_captured_files': len(original), 'configuration': receipt.model_dump()}
with (raw/'configuration-revalidation.json').open('x') as output:
    json.dump(result, output, indent=2)
    output.write('\n')
PY
```

The initial direct trace pass finds 50 incoming classes, 28,908 complete attempts
and 108,596 write events. These are raw attempt/write counts, not location counts.
World backup completed with 503 files totaling 428,092,106 bytes; its archive is
162,363,995 bytes with SHA-256
`3aa87e98bf90e00aaa20101412d429c2b163b36a0bff45aee51f42164b6c4580`.
Trace size is 22,100,158 bytes. Durable archive publication, restore and complete
saved-world analysis must follow before another world starts.
