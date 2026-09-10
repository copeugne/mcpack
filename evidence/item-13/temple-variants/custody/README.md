# Temple variant diagnostic raw custody

Status: external publication, member restores and nested downloaded-world
verification VERIFIED. This record concerns the bounded
Item 13 material diagnostic, not full Item 13 completion or Item 14.

The [archive manifest](archive-manifest.json) retains280 files,185,056,700 raw
bytes, as `item13-temple-variants-2f653748.tar.gz` (163,794,775 bytes; SHA-256
e987543979a3e4f0fdb9f4a90895b9cbab00fbd3db7beb07f82252d2b27c87c6).
The [release](https://github.com/copeugne/mcpack/releases/tag/item13-temple-variants-2f653748)
tag was fetched and resolves to successful producer
2f653748a6f46d48be14a9537677a0454bcd6f46. Each rejected attempt retains its own
capture.json producer identity; the tag does not claim that r5 produced those bytes.

Included inputs are the entire r1..r5 capture directories plus the successful
stopped-world archive, backup inventory, local world-restore result and saved-block
comparison. Counts per attempt are11,3,11,11,240 files. r2's copied latest/debug
logs came from materialization; r2 never launched a server. Failed instances
remain preserved locally. No failed world is substituted for the accepted r5 world.
No template, processor, world data or raw log was rewritten for publication.
A targeted credential-assignment check found no additional secrets in capture
logs/configuration. Existing configuration sanitization remains in force. The
archive contains the generated probe binaries, not retained candidate JARs or Java.

[Local member restore](local-restore.json) and [downloaded member restore](download-restore.json)
verify every member in separate absent targets. The downloaded manifest matches
byte for byte. The nested world archive is162,749,467 bytes, SHA-256
451c9de1804e859f8daf18cfb545a4879cd994cf677ef9e1a46cf1949a40a37c;
its503-file inventory excludes session.lock. The backup receipt's SHA-256 is
cf6d6b5fc690fbceab9941ad1b0bc4b4a74d192e4ae1597469e4b5a9039836d1.
The saved reader permits an explicit backup path for downloaded custody, while
requiring this exact receipt hash. It does not rely on the original instance.

Reproduction uses existing archive/restore tools. Run from the repository root;
new output paths must be absent. The staging step copied the following inputs
without modifying their originals:

```sh
uv run python - <<'PY'
from pathlib import Path
import shutil
root = Path('evidence/raw/item13/temple-r5-custody')
stage = root / 'publish'
stage.mkdir()
for n in range(1, 6):
    shutil.copytree(Path(f'evidence/raw/item13/temple-variants-r{n}'), stage / f'r{n}')
for name in ('world.tar.gz', 'world-backup.json', 'world-restore.json', 'saved-verification.json'):
    shutil.copyfile(root / name, stage / name)
assert not any(path.is_symlink() for path in stage.rglob('*'))
PY
timeout 120 uv run python -m tools.archive_item7_evidence create --root evidence/raw/item13/temple-r5-custody/publish --archive evidence/raw/item13/temple-r5-custody/item13-temple-variants-2f653748.tar.gz --manifest evidence/item-13/temple-variants/custody/archive-manifest.json --revision 2f653748a6f46d48be14a9537677a0454bcd6f46
timeout 120 uv run python -m tools.archive_item7_evidence restore --archive evidence/raw/item13/temple-r5-custody/item13-temple-variants-2f653748.tar.gz --manifest evidence/item-13/temple-variants/custody/archive-manifest.json --target evidence/raw/item13/temple-r5-custody/restored-local --receipt evidence/item-13/temple-variants/custody/local-restore.json
gh release download item13-temple-variants-2f653748 --repo copeugne/mcpack --dir evidence/raw/item13/temple-r5-custody/downloaded
cmp evidence/item-13/temple-variants/custody/archive-manifest.json evidence/raw/item13/temple-r5-custody/downloaded/archive-manifest.json
timeout 120 uv run python -m tools.archive_item7_evidence restore --archive evidence/raw/item13/temple-r5-custody/downloaded/item13-temple-variants-2f653748.tar.gz --manifest evidence/item-13/temple-variants/custody/archive-manifest.json --target evidence/raw/item13/temple-r5-custody/restored-download --receipt evidence/item-13/temple-variants/custody/download-restore.json
timeout 120 uv run python -m tools.manage_item4_environment restore --archive evidence/raw/item13/temple-r5-custody/restored-download/world.tar.gz --sha256 451c9de1804e859f8daf18cfb545a4879cd994cf677ef9e1a46cf1949a40a37c --target evidence/raw/item13/temple-r5-custody/downloaded-world > evidence/item-13/temple-variants/custody/download-world-restore.json
timeout 120 uv run python -m evidence.item-13.temple-variants.verify_saved evidence/raw/item13/temple-r5-custody/downloaded-world/world --backup evidence/raw/item13/temple-r5-custody/restored-download/world-backup.json > evidence/raw/item13/temple-r5-custody/download-saved-verification.json
cmp evidence/item-13/temple-variants/r5-saved-verification.json evidence/raw/item13/temple-r5-custody/download-saved-verification.json
git fetch origin tag item13-temple-variants-2f653748
git rev-parse item13-temple-variants-2f653748
```

The large deterministic member manifest is isolated with this single diagnostic's
custody outcome. Its size follows from retaining all attempts and the successful
world using the existing archive contract, not a new schema or review framework.


The [downloaded world restore](download-world-restore.json) passes503 files. Its
full inventory verifies before and after reading, all15,562 saved cells agree,
and the result is byte-identical to [the accepted comparison](../r5-saved-verification.json).
No server was started during custody verification. The complete local custody
tree uses1,902,181,338 bytes, below its3-GiB allocation. The original world,
local archive/restores and verified external release supply redundant preservation.
This closes diagnostic custody only; Item 13's broader coverage and review/merge
gates remain IN PROGRESS.
