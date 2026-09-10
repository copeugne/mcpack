# Failed continuous shaft query custody

The failed r2 capture is preserved, not accepted as a completed motion experiment.
Producer: `2bdf8c7f3c0497033763a262a3731ce24ef18e82`.
The [release](https://github.com/copeugne/mcpack/releases/tag/item13-shaft-motion-r2-2bdf8c7f)
and fetched tag bind this exact revision.

Archive `item13-shaft-motion-r2-2bdf8c7f.tar.gz`: 507,064 bytes, SHA-256
`e1597acafd69bbd497e076f6721285f209e7000a4a6c7fb6601a4d84aa44ddd8`.
The [manifest](archive-manifest.json) contains all 11 raw files, 5,581,901 bytes.
[Local](local-restore.json) and [downloaded](download-restore.json) restores verified
all members; the downloaded manifest is byte-identical. Original capture, archive,
restores and failed experimental instance remain preserved and are not reused.

Unlike accepted r1, this failed capture never reached configuration collection.
It contains the input projection, probe/classes and complete available logs, but
no post-run configuration audit or accepted output world. A focused log search for
password/token/secret assignments found zero matches. No raw bytes were rewritten.
The original accepted world remains under its existing custody.

Executed commands, with absent restore targets:

```sh
uv run python -m tools.archive_item7_evidence create --root evidence/raw/item13/shaft-motion-r2 --archive evidence/raw/item13/shaft-motion-r2-custody/item13-shaft-motion-r2-2bdf8c7f.tar.gz --manifest evidence/item-13/shaft-motion/r2-custody/archive-manifest.json --revision 2bdf8c7f
uv run python -m tools.archive_item7_evidence restore --archive evidence/raw/item13/shaft-motion-r2-custody/item13-shaft-motion-r2-2bdf8c7f.tar.gz --manifest evidence/item-13/shaft-motion/r2-custody/archive-manifest.json --target evidence/raw/item13/shaft-motion-r2-custody/restored-local --receipt evidence/item-13/shaft-motion/r2-custody/local-restore.json
gh release download item13-shaft-motion-r2-2bdf8c7f --repo copeugne/mcpack --dir evidence/raw/item13/shaft-motion-r2-custody/downloaded
cmp evidence/item-13/shaft-motion/r2-custody/archive-manifest.json evidence/raw/item13/shaft-motion-r2-custody/downloaded/archive-manifest.json
uv run python -m tools.archive_item7_evidence restore --archive evidence/raw/item13/shaft-motion-r2-custody/downloaded/item13-shaft-motion-r2-2bdf8c7f.tar.gz --manifest evidence/item-13/shaft-motion/r2-custody/archive-manifest.json --target evidence/raw/item13/shaft-motion-r2-custody/restored-download --receipt evidence/item-13/shaft-motion/r2-custody/download-restore.json
git fetch origin tag item13-shaft-motion-r2-2bdf8c7f
git rev-parse item13-shaft-motion-r2-2bdf8c7f
```

The authoritative [temple report](../../fixed-blocks/explorations-underground-temple-report.md)
records the timeout and its limits. This is failure custody, not Item13 completion.
