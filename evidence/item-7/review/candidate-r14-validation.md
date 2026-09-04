# Item 7 r14 Candidate Validation

**Candidate revision:** `d0907824e4b3929c3580028b5702d4b794dc5061`
**Verdict:** `PASS`

## Release and custody

The annotated tag `item-7-raw-evidence-2026-09-04-r14` has object SHA-1 `4b5fefe4a58f310bbd47796772520e6d3288f480` and resolves to source revision `4497b3f650990f501b594b82e933c40eaf5540ac`. All four release assets were uploaded. All four archives were restored into absent targets and verified file by file before publication.

The tracked verifier downloaded the complete published release into an absent directory and matched every asset size and SHA-256:

```sh
tools/verify_item7_release.sh copeugne/mcpack item-7-raw-evidence-2026-09-04-r14 evidence/item-7/archive/r14 evidence/item-7/archive/r14/publication.json /home/lonestar/Desktop/Projects/mcpack-item7-r14-release-download-1
```

Result: `verified 4 release assets at revision 4497b3f650990f501b594b82e933c40eaf5540ac`.

## Quality gates

```sh
uv run pytest -q tests/item7
uv run pytest -q
uv run ruff format --check src/mcpack_evidence/item7_*.py tools/*item7*.py tests/item7
uv run ruff check src/mcpack_evidence/item7_*.py tools/*item7*.py tests/item7
uv run basedpyright src/mcpack_evidence/item7_*.py tools/*item7*.py tests/item7
bash -n tools/capture_item7_visual_qa.sh
bash -n tools/stage_item7_raw_evidence.sh
bash -n tools/verify_item7_release.sh
```

Results:

- 210 Item 7 tests passed.
- 891 repository tests passed.
- Ruff reported 127 files already formatted and no lint findings.
- basedpyright reported zero errors, warnings, or notes.
- All three Item 7 shell scripts passed syntax checks.

## Deterministic save-audit rebuild

```sh
uv run tools/validate_item7_save_sequence.py \
  --core /home/lonestar/Desktop/Projects/mcpack-item7-r14-delivery/restored/core \
  --manifest evidence/item-7/archive/r14/core-manifest.json \
  --world-inventory evidence/item-7/world-archive-inventory.json \
  > /tmp/item7-save-sequence-r14-final.json
cmp evidence/item-7/save-sequence-r14.json /tmp/item7-save-sequence-r14-final.json
sha256sum evidence/item-7/save-sequence-r14.json /tmp/item7-save-sequence-r14-final.json
```

Both files have SHA-256 `087ebb0a5b019fb5138fd6975598176c07495eb81954f0d4bc4ce524502893b3`.

An earlier combined-gate invocation omitted the required `--world-inventory` option and exited with CLI usage status 2 after the test and static-check stages had already passed. No evidence or repository file changed. The command above is the corrected tracked invocation and passed byte for byte.

## Deterministic completion rebuild

```sh
uv run python tools/build_item7_completion.py \
  --raw-root /home/lonestar/Desktop/Projects/mcpack-item7-r14-delivery/restored/core \
  --protocol evidence/item-7/protocol/worldgen-audit-v1.json \
  --provider-catalog evidence/item-7/provider-catalog.json \
  --provider-coverage /home/lonestar/Desktop/Projects/mcpack-item7-r14-delivery/restored/core/run-a/provider-coverage.json \
  --provider-disposition /home/lonestar/Desktop/Projects/mcpack-item7-r14-delivery/restored/core/provider-disposition.json \
  --restriction-audit evidence/item-7/biome-restriction-audit.json \
  --world-archive-inventory evidence/item-7/world-archive-inventory.json \
  --repeat-comparison /home/lonestar/Desktop/Projects/mcpack-item7-r14-delivery/restored/core/repeat-comparison.json \
  --warning-audit /home/lonestar/Desktop/Projects/mcpack-item7-r14-delivery/restored/core/warning-audit.json \
  --warning-disposition /home/lonestar/Desktop/Projects/mcpack-item7-r14-delivery/restored/core/warning-disposition.json \
  --control-comparison /home/lonestar/Desktop/Projects/mcpack-item7-r14-delivery/restored/core/control-comparison.json \
  --visual-manifest /home/lonestar/Desktop/Projects/mcpack-item7-r14-delivery/restored/core/visual-qa/captures/capture-manifest.tsv \
  --visual-review evidence/item-7/visual/integrity-review.json \
  --visual-review evidence/item-7/visual/fidelity-review.json \
  --archive-manifest evidence/item-7/archive/r14/core-manifest.json \
  --archive-manifest evidence/item-7/archive/r14/run-a-worlds-manifest.json \
  --archive-manifest evidence/item-7/archive/r14/run-b-worlds-manifest.json \
  --archive-manifest evidence/item-7/archive/r14/auxiliary-worlds-manifest.json \
  --restore-receipt evidence/item-7/archive/r14/core-restore.json \
  --restore-receipt evidence/item-7/archive/r14/run-a-worlds-restore.json \
  --restore-receipt evidence/item-7/archive/r14/run-b-worlds-restore.json \
  --restore-receipt evidence/item-7/archive/r14/auxiliary-worlds-restore.json \
  --publication evidence/item-7/archive/r14/publication.json \
  --save-sequence-audit evidence/item-7/save-sequence-r14.json \
  --output /tmp/item7-completion-r14-final.json
cmp evidence/item-7/completion.json /tmp/item7-completion-r14-final.json
sha256sum evidence/item-7/completion.json /tmp/item7-completion-r14-final.json
```

The builder returned `PASS`, recorded 138 exact artifacts, and reproduced SHA-256 `0ef7c83438ab2a2cfe67eadc858e806ada9c9eecc213d883649ae3e8493cb1d3` byte for byte.

## Narrow validator regression and correction

The first r14 completion attempt exposed a validator regression introduced by `f4b915a`. The accepted analyses contain 12 anomaly keys, including the separately generated unresolved key `impossible_biome_restrictions`; the refactor incorrectly derived an 11-key expected set from `ANOMALY_SPECS`. The r11 and r14 analysis bytes were identical, and the tracked analyzer rebuilt the affected analysis byte for byte. Commit `3fb3f17` restored the complete explicit 12-key contract. The focused completion-run test and the final source rebuild passed afterward.

## Working tree boundary

The tracked working tree was clean at the candidate revision. The pre-existing `.codegraph`, `.omo/`, and `mcpack-reconstructed-28(1).bundle` paths remained untracked and untouched.
