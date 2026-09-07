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
open. Remote publication and downloaded-archive restoration both passed.

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

## Remote delivery and retrieval

The immutable archive was published at
[Item 8 registry raw evidence r1](https://github.com/copeugne/mcpack/releases/tag/item-8-registry-raw-2026-09-05-r1).
`registry-r1-release.json` preserves the GitHub response before download. Its
single asset is uploaded, matches the archive size, and belongs to a published
non-draft release. The fetched tag and remote tag both resolve to the custody
revision above. The raw archive has local and GitHub copies; the local copies
share a host and are not independent redundant storage.

The following retrieval and restore commands succeeded at source `366858f`:

```sh
gh release view item-8-registry-raw-2026-09-05-r1 --repo copeugne/mcpack --json tagName,url,isDraft,isPrerelease,publishedAt,assets > evidence/item-8/raw-custody/registry-r1-release.json
gh release download item-8-registry-raw-2026-09-05-r1 --repo copeugne/mcpack --dir evidence/raw/item8/custody-r1/downloaded
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/custody-r1/downloaded/item8-registry-r1-376e8e6.tar.gz --manifest evidence/item-8/raw-custody/registry-r1-manifest.json --target evidence/raw/item8/custody-r1/restored-download --receipt evidence/item-8/raw-custody/registry-r1-downloaded-restore.json
uv run -m tools.extract_item8_world_context --level evidence/raw/item8/custody-r1/restored-download/world-metadata/level.dat --output evidence/raw/item8/custody-r1/downloaded-world-context.json
cmp evidence/item-8/runtime/registry-r1/world-context.json evidence/raw/item8/custody-r1/downloaded-world-context.json
git ls-remote origin refs/tags/item-8-registry-raw-2026-09-05-r1
```

The downloaded archive restored all 241 files with verified hashes. The saved
world-context projection reproduced byte for byte from the downloaded source.
For a new retrieval, change output paths to avoid overwriting preserved records.

## Dimension capture attempts r1 through r3

The same archive/restore implementation preserves all three complete capture
directories, including failed attempts. Archive `item8-dimensions-r1-r3-cd04324.tar.gz`
is 1446795 bytes, SHA `29c9b189483f96f29d45a62d79556fdf10655729cf901204def50789578b5cb7`.
It contains 261 files totaling 16993965 uncompressed bytes. The custody revision
is `cd043241a1beabaa47acd9657790af1e987e9dd0`; each capture retains its own original
source revision. The manifest and local restore are delivered in `e9a91c2`;
remote publication and downloaded restore evidence are delivered in `5b742a5`.

Contents include logs, capture records, the compiled measurement probe and build
logs, r3's dimension output and seven dumps, and its sanitized configuration.
No Minecraft/NeoForge binaries or world regions are included. r1's missing queued
console tail remains missing; r2 preserves the diagnostic that led to the fix.
The generated credential redaction follows the unchanged capture implementation.

Executed commands, using absent destination paths:

```sh
mkdir evidence/raw/item8/dimension-custody-r1
mkdir evidence/raw/item8/dimension-custody-r1/captures
cp -a evidence/raw/item8/dimension-r1 evidence/raw/item8/dimension-r2 evidence/raw/item8/dimension-r3 evidence/raw/item8/dimension-custody-r1/captures/
uv run -m tools.archive_item7_evidence create --root evidence/raw/item8/dimension-custody-r1/captures --archive evidence/raw/item8/dimension-custody-r1/item8-dimensions-r1-r3-cd04324.tar.gz --manifest evidence/item-8/raw-custody/dimensions-r1-r3-manifest.json --revision cd043241a1beabaa47acd9657790af1e987e9dd0
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/dimension-custody-r1/item8-dimensions-r1-r3-cd04324.tar.gz --manifest evidence/item-8/raw-custody/dimensions-r1-r3-manifest.json --target evidence/raw/item8/dimension-custody-r1/restored-local --receipt evidence/item-8/raw-custody/dimensions-r1-r3-local-restore.json
gh release view item-8-dimensions-raw-2026-09-05-r1 --repo copeugne/mcpack --json tagName,url,isDraft,isPrerelease,publishedAt,assets > evidence/item-8/raw-custody/dimensions-r1-r3-release.json
gh release download item-8-dimensions-raw-2026-09-05-r1 --repo copeugne/mcpack --dir evidence/raw/item8/dimension-custody-r1/downloaded
uv run -m tools.archive_item7_evidence restore --archive evidence/raw/item8/dimension-custody-r1/downloaded/item8-dimensions-r1-r3-cd04324.tar.gz --manifest evidence/item-8/raw-custody/dimensions-r1-r3-manifest.json --target evidence/raw/item8/dimension-custody-r1/restored-download --receipt evidence/item-8/raw-custody/dimensions-r1-r3-downloaded-restore.json
git ls-remote origin refs/tags/item-8-dimensions-raw-2026-09-05-r1
```

Both restores verified all 261 files. The remote tag resolves to the custody
revision. The published release's uploaded asset matches the manifest's size,
and the downloaded bytes passed the archive hash and member checks.
Release: [Item 8 dimension biome raw captures](https://github.com/copeugne/mcpack/releases/tag/item-8-dimensions-raw-2026-09-05-r1).
Local and GitHub copies provide separate storage; local copies share a host.
