# Frozen registry capture

`registry-r1/capture.json` and its seven dump files are the unmodified output of
`tools.run_item8_registry` at source revision
`367ba59d097fc3fe3284adb36cb4536bbc583663`. The receipt identifies the runtime,
configuration parity result, command sequence, and individual dump hashes.
Registry keys are not canonical families and do not prove actual placement.

The original command from the repository root was:

```sh
uv run -m tools.run_item8_registry \
  --pristine instances/pristine-baseline-v0 \
  --java-home downloads/item2/temurin/extracted/jdk-21.0.12.1+1 \
  --target instances/item8/registry-r1 \
  --output evidence/raw/item8/registry-r1 \
  --timeout-seconds 900
```

Use new target and output paths for any reproduction. The original source used a
120-second clean-exit deadline. Later source exposes the same default through
`--exit-timeout-seconds 120`; it does not alter the original receipt retroactively.
Readiness, all seven dump responses, correlated flush, and clean exit were
observed by the capture harness. Full console, latest and debug logs and captured
configuration remain at `evidence/raw/item8/registry-r1` pending durable delivery.
This partial delivery does not independently close the lifecycle or configuration
evidence requirements and does not pass Item 8.
