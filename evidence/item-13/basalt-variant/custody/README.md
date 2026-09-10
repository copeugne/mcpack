# Basalt netherite diagnostic raw custody

Status: VERIFIED external publication, complete local/download member restores,
and downloaded stopped-world comparison. This closes diagnostic durability only.

The [manifest](archive-manifest.json) binds244 files,168,675,651 uncompressed bytes.
Archive `item13-basalt-variant-19cd4a08.tar.gz` is162,445,839 bytes, SHA-256
`22882146274e98927bc4185bad1e435421db9335ade2ff9e93697d4d02bf2eab`.
The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item13-basalt-variant-19cd4a08)
contains that archive and the byte-identical manifest. Its fetched tag resolves to
producer `19cd4a08ba0f5ea9044f42d492118c0d3dad4dfe`.

Included inputs are all240 files of the successful r1 capture plus the stopped
world archive, complete backup inventory, local world restore and saved comparison.
No failed runtime attempt exists for this diagnostic. Original capture/instance
paths remain preserved. A targeted nonempty credential-assignment scan found no
additional secret assignment in capture logs/configuration. Probe binaries are
external raw evidence; candidate JARs and toolchains are not included in this archive.

[Local restore](local-restore.json) and [downloaded restore](download-restore.json)
verify every244 member in separate absent targets. The nested world archive is
162,747,723 bytes, SHA-256
`d44157af4f6893e325170defb60c2fe33a8737b922e44b3216d09c2d9f553269`.
Its503-file inventory excludes session.lock. Backup receipt SHA-256 is
`d0a091ad4a80eed1d5745d9918ecab70dc4aa3d4645c751dc2c975319c3199f2`.
The [downloaded world restore](download-world-restore.json) passes; its full
inventory verifies before/after reading and its2,197-cell comparison is
byte-identical to the [accepted result](../r1-saved-verification.json).
No server was started for these custody checks.

Reproduction uses the existing archive/restore tools. Output targets must be absent.
The executed staging step copied unchanged inputs:

```sh
uv run python - <<'PY'
from pathlib import Path
import shutil
root=Path('evidence/raw/item13/basalt-r1-custody');stage=root/'publish';stage.mkdir()
shutil.copytree(Path('evidence/raw/item13/basalt-variant-r1'),stage/'r1')
for name in ('world.tar.gz','world-backup.json','world-restore.json','saved-verification.json'):
    shutil.copyfile(root/name,stage/name)
assert not any(p.is_symlink() for p in stage.rglob('*'))
assert len([p for p in stage.rglob('*') if p.is_file()])==244
PY
timeout 120 uv run python -m tools.archive_item7_evidence create --root evidence/raw/item13/basalt-r1-custody/publish --archive evidence/raw/item13/basalt-r1-custody/item13-basalt-variant-19cd4a08.tar.gz --manifest evidence/item-13/basalt-variant/custody/archive-manifest.json --revision 19cd4a08ba0f5ea9044f42d492118c0d3dad4dfe
timeout 120 uv run python -m tools.archive_item7_evidence restore --archive evidence/raw/item13/basalt-r1-custody/item13-basalt-variant-19cd4a08.tar.gz --manifest evidence/item-13/basalt-variant/custody/archive-manifest.json --target evidence/raw/item13/basalt-r1-custody/restored-local --receipt evidence/item-13/basalt-variant/custody/local-restore.json
gh release download item13-basalt-variant-19cd4a08 --repo copeugne/mcpack --dir evidence/raw/item13/basalt-r1-custody/downloaded
cmp evidence/item-13/basalt-variant/custody/archive-manifest.json evidence/raw/item13/basalt-r1-custody/downloaded/archive-manifest.json
timeout 120 uv run python -m tools.archive_item7_evidence restore --archive evidence/raw/item13/basalt-r1-custody/downloaded/item13-basalt-variant-19cd4a08.tar.gz --manifest evidence/item-13/basalt-variant/custody/archive-manifest.json --target evidence/raw/item13/basalt-r1-custody/restored-download --receipt evidence/item-13/basalt-variant/custody/download-restore.json
timeout 120 uv run python -m tools.manage_item4_environment restore --archive evidence/raw/item13/basalt-r1-custody/restored-download/world.tar.gz --sha256 d44157af4f6893e325170defb60c2fe33a8737b922e44b3216d09c2d9f553269 --target evidence/raw/item13/basalt-r1-custody/downloaded-world > evidence/item-13/basalt-variant/custody/download-world-restore.json
timeout 120 uv run python -m evidence.item-13.temple-variants.verify_saved --basalt evidence/raw/item13/basalt-r1-custody/downloaded-world/world --backup evidence/raw/item13/basalt-r1-custody/restored-download/world-backup.json > evidence/raw/item13/basalt-r1-custody/download-saved-verification.json
cmp evidence/item-13/basalt-variant/r1-saved-verification.json evidence/raw/item13/basalt-r1-custody/download-saved-verification.json
git fetch origin tag item13-basalt-variant-19cd4a08
git rev-parse item13-basalt-variant-19cd4a08
```

The local custody tree uses1,850,232,946 bytes, below its3-GiB allocation.
Original world, local archives/restores and verified external release provide
redundant preservation. No new schema, archive framework or gameplay claim was
added. Full Item13 coverage and final reviewed main delivery remain IN PROGRESS.
