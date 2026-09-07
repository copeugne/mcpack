# Repurposed mansion and monument completion

## Quantified remaining work and capture declaration

After 8e4400bb these two families have seven unresolved entries, not five.
Both existing approximate_vertical_size attributes contain UNKNOWN values and
must remain counted as open. Across Item 8 that corrects 474 remaining entries
to 476. Their foundation limitations are valid but do not resolve height.

Three descriptive entries can use existing source evidence: mansion visibility,
monument visibility and monument placement. Four size entries need representative
assembled observations. Neither the main world-bounds catalog nor the additional
original Item 8 chunks.jsonl captures contains a start for either family's roots.

Predeclare one fresh ordinary seed42 Overworld run targeting, in order,
repurposed_structures:mansion_oak and repurposed_structures:monument_desert.
Request81 chunks around each located target through the existing gap runner.
Require readiness, both matching completions, correlated save-all flush, clean
exit and frozen configuration acceptance. Preserve failures and raw warnings.
Accept saved envelopes only after archive, local restore, remote delivery and
fresh downloaded restore. One example per family is not all-variant extrema,
occupied volume or total foundation extent. No new measurement tool is required.

```sh
uv run -m tools.run_item7_gap_targets \
  --pristine instances/pristine-baseline-v0 \
  --artifact-manifest evidence/item-3/artifact-acquisition-manifest.json \
  --retained-manifest evidence/item-3/runtime/retained-server-candidates.txt \
  --seed-suite test-environment/seed-suite.json \
  --frozen-config evidence/item-6/frozen \
  --frozen-manifest evidence/item-6/generated-config-manifest.json \
  --config-audit evidence/item-6/config-audit.json \
  --java-home downloads/item2/temurin/extracted/jdk-21.0.12.1+1 \
  --target instances/item8/repurposed-mansion-monument-geometry-r1 \
  --log-path evidence/raw/item8/repurposed-mansion-monument-geometry-r1/console.log \
  --captured-config evidence/raw/item8/repurposed-mansion-monument-geometry-r1/configuration \
  --receipt evidence/raw/item8/repurposed-mansion-monument-geometry-r1/run.json \
  --timeout-seconds 900 \
  --structure repurposed_structures:mansion_oak \
  --structure repurposed_structures:monument_desert
```
