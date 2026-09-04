# Item 8 registry raw custody

This archive closes the explicitly required raw-retention gap for the existing
registry capture. It adds no experiment, schema or validation framework. The
existing Item 7 archive CLI and its unchanged v1 manifest/restore contracts are
reused for Item 8 data; their historical schema names do not make this Item 7
acceptance evidence.

Archive: `item8-registry-r1-376e8e6.tar.gz`.
SHA-256: `03f60f97ba2d22f6ae86b600a1cf0d267896209254493e2730cc2f814f1d3645`.
Size: 603232 bytes. Contents: 241 files, 6205038 uncompressed bytes.
The manifest inventories the complete capture directory: 228 captured config
files, seven registry dumps, three logs, capture and sanitization records, and
the preserved source `world-metadata/level.dat`. No world-region archive or
server binary is included. The configuration retains its recorded credential
redaction; the source logs and metadata are unchanged.

The custody revision is `376e8e619ed9c8aec49a81fbe833ed706ad6ca57`.
The original runtime source remains `367ba59d097fc3fe3284adb36cb4536bbc583663`.
The custody revision does not change the recorded capture identity or establish
Item 8 completion. Required provider coverage and gameplay attributes remain
open. Remote publication and downloaded-archive restoration are still pending.

Executed from the repository root at the custody revision:

```sh
mkdir -p evidence/item-8/raw-custody evidence/raw/item8/custody-r1
uv run -m tools.archive_item7_evidence create --root evidence/raw/item8/registry-r1 --archive evidence/raw/item8/custody-r1/item8-registry-r1-376e8e6.tar.gz --manifest evidence/item-8/raw-custody/registry-r1-manifest.json --revision 376e8e619ed9c8aec49a81fbe833ed706ad6ca57
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/custody-r1/item8-registry-r1-376e8e6.tar.gz --manifest evidence/item-8/raw-custody/registry-r1-manifest.json --target evidence/raw/item8/custody-r1/restored-local --receipt evidence/item-8/raw-custody/registry-r1-local-restore.json
```

Both commands succeeded. Restoration verifies archive size/hash, exact member
coverage, safe paths and each restored file's size/hash. Use absent output paths
for a reproduction; neither command overwrites an existing result. This is a
data restoration check, not a restored-server boot claim.
