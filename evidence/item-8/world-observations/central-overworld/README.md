# Preserved central Overworld block observation

Projected at extractor revision 9e37e7e from the restored Item 7 run-a ordinary
world. No world was generated, modified or started. The extractor verifies the
pinned r14 manifest and all four region hashes/sizes before decoding. Source
identities are embedded in blocks.json. The output is 352963 bytes, SHA-256
8b19e927b6b5d1a4de5f210eb301402c7f5e9dca4d4eb210b2fa31219cde4d06.

```sh
uv run -m tools.extract_item8_end_blocks --restored-run-a ../mcpack-item7-r14-delivery/restored-final/run-a --dimension overworld --output evidence/raw/item8/overworld-9e37e7e-reproduction.json
cmp evidence/item-8/world-observations/central-overworld/blocks.json evidence/raw/item8/overworld-9e37e7e-reproduction.json
uv run pytest -q tests/item8/test_end_blocks.py
```

All 64 chunks at chunk X/Z -4 through 3 have full status. Each contains 24
decoded block-state sections covering Y -64 through 319. No used block state
or preserved block-entity ID is quark:monster_box. The focused evidence test
binds the output hash, complete coordinate/section sets, per-section totals and
this negative result. This is absence in one fixed saved sample, not proof of
global absence, disabled generation, encounter frequency or a failed generator.
The area was fixed before inspection. Do not expand it merely to obtain a hit.

The existing End default was rerun as evidence/raw/item8/end-default-9e37e7e.json
and matched the prior central-end/blocks.json byte for byte. The Overworld
projection reuses the same decoder and identity checks. The initial new test
passed, but its first type check rejected untyped JSON values; explicit existing
JsonValue casts resolved these errors, including the section-Y set type. All
four focused tests, Ruff and Basedpyright then passed.

The generated artifact is isolated from extractor changes because it preserves
the complete fixed projection, not just Monster Box search hits. It may support
other current family investigations without decoding this sample again.
