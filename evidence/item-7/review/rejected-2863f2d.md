# Item 7 GitHub review rejection at 2863f2d

## Reviewed candidate

- Pull request: `https://github.com/copeugne/mcpack/pull/15`.
- Exact reviewed commit: `2863f2d01c7446fe757b54593ea311bcacf35adb`.
- GitHub review: `5116118114`, submitted at `2026-09-04T17:37:34Z`.
- Review result: rejected with three valid findings. No thumbs-up was present.

## Findings and dispositions

| Comment | Priority | Finding | Disposition |
| --- | --- | --- | --- |
| `3936497504` | P1 | Completion trusted accepted analysis JSON after checking only its identity and broad accounting. | Fixed by `8345df789416527917787707047bb22ffe164b1a`. Completion now rebuilds every Run A analysis from its selected JSONL with the tracked analyzer and requires complete model equality. |
| `3936497509` | P1 | Completion trusted the repeat-comparison receipt without rebuilding its normalized hashes, counts, equality flags, and first mismatch from Run A and Run B sources. | The comparator was extracted once in `69a4f7e159d0c4305cd7f20150e340813427d1dc`; completion was changed to rebuild the complete receipt from accepted selection JSONL in `d51d1762793cd2be5e91fd56c172b378d1d1106b`. |
| `3936497513` | P2 | A stale queued generic save confirmation could satisfy `save-all flush` in main, gap, and control lifecycles. | Fixed by `dbec2eec71808dabd88bfe5fe1179f621367742a`. Each runner now takes an atomic output-sequence checkpoint while sending the command and requires a post-checkpoint `Saving the game` followed by `Saved the game` before stopping. |

The lifecycle finding was reproduced independently for all three affected runners before the fix. The analysis and repeat findings were each reproduced with a forged derived result that passed the old validator before their new regression tests were made green.

## Retained raw evidence assessment

The lifecycle implementation defect did not require discarding the retained worlds. The tracked validator at `tools/validate_item7_save_sequence.py`, introduced by `0686e164f5fdf93cff8eeb3939e5bf7e1a695fb8` and hardened through `f10d87bf4f85d35a3fe6e2cb68a8db95094b0e17`, inspected every accepted main, gap, control, and successful pilot console log.

`evidence/item-7/save-sequence-r9.json` records 12 of 12 passing lifecycles. For each lifecycle, the final required work marker precedes `Saving the game`, which precedes `Saved the game`. Every log observation records its byte size and SHA-256 and is verified against `evidence/item-7/archive/r9/core-manifest.json`, SHA-256 `dc82af8eaba1f7799ae2c7d2681e25e775aa4c3fea227fa2394af5a202690d53`. That manifest binds the raw core archive `mcpack-item7-raw-core-r9.tar.gz`, SHA-256 `2229673778123d8b7737048610d9c171aea9b49900724acc0f35ac48eed25773`.

Reproduction command:

```sh
uv run tools/validate_item7_save_sequence.py \
  --core /home/lonestar/Desktop/Projects/mcpack-item7-r9-delivery/restored/core \
  --manifest evidence/item-7/archive/r9/core-manifest.json
```

## Post-fix empirical validation

- `uv run pytest -q tests/item7` passed with 196 tests after the three fixes and archive-binding hardening.
- Scoped Ruff checks passed.
- Scoped basedpyright passed with zero errors, warnings, or notes.
- A clean completion rebuild parsed the restored r9 selected JSONL through the new analysis and repeat source-binding paths, returned `PASS`, and was byte-identical to `evidence/item-7/completion.json`.
- Both completion files had SHA-256 `76603b037d38534f56a4a2625666032b60929d7efe74c0a434b73310858c4c69`.

The r9 raw payload remains valid, but r9 source custody predates these corrected producers. A new custody revision is therefore required before Item 7 can return to exact-SHA local review and the GitHub review loop. This report supersedes the local acceptance reports for `c7babd9596594bab4f151a50cdc2ccb180c7aa18` and `2863f2d01c7446fe757b54593ea311bcacf35adb`.

Temporary `.omo/evidence` debug records are not authoritative evidence and are not committed.
