# Wet-step pilot raw custody

The native motion pilot's raw capture is durably retained and restored. This is
capture custody, not Item13 completion. Its source revision is
d11e4a535d628575d985d648d1c0c186b8d3b7bb.

The existing archive implementation retained all240 files totaling5,883,695 bytes.
Archive `item13-shaft-motion-r1-d11e4a53.tar.gz` is596,608 bytes, SHA-256
6d5b148683d395c6a986c0b7389851090369de3ffa71d63c274fd1c1926c9490.
The [manifest](archive-manifest.json) enumerates every member. Both the
[local restore](local-restore.json) and [downloaded restore](download-restore.json)
verified all240 members. The downloaded manifest is byte-identical.

The [evidence release](https://github.com/copeugne/mcpack/releases/tag/item13-shaft-motion-r1-d11e4a53)
contains the archive and manifest. Its fetched tag resolves exactly to the launch
revision above. Local original files, archive and restores remain preserved.
The original accepted world archive supplies the unchanged input; this capture
archive contains the probe, output, logs and configuration, not another accepted
world. The fresh experimental instance remains ignored and is not reused as an
experiment input.

Before publication, the existing config-sanitization receipt confirmed its one
generated Resourceful Config Web password was replaced with the declared sentinel.
RCON password is empty. A focused assignment search found only empty/redacted
credential fields. The first generic search over whitespace crossed an empty
property's newline; an exact RCON-property check resolved that false positive.
No raw capture was rewritten for publication. Committed console projection uses
the existing bind-endpoint redaction; its original hash remains in retention.

Executed reproduction commands require absent output targets:

```sh
mkdir -p evidence/raw/item13/shaft-motion-r1-custody evidence/item-13/shaft-motion/custody
uv run python -m tools.archive_item7_evidence create --root evidence/raw/item13/shaft-motion-r1 --archive evidence/raw/item13/shaft-motion-r1-custody/item13-shaft-motion-r1-d11e4a53.tar.gz --manifest evidence/item-13/shaft-motion/custody/archive-manifest.json --revision d11e4a53
uv run python -m tools.archive_item7_evidence restore --archive evidence/raw/item13/shaft-motion-r1-custody/item13-shaft-motion-r1-d11e4a53.tar.gz --manifest evidence/item-13/shaft-motion/custody/archive-manifest.json --target evidence/raw/item13/shaft-motion-r1-custody/restored-local --receipt evidence/item-13/shaft-motion/custody/local-restore.json
gh release download item13-shaft-motion-r1-d11e4a53 --repo copeugne/mcpack --dir evidence/raw/item13/shaft-motion-r1-custody/downloaded
cmp evidence/item-13/shaft-motion/custody/archive-manifest.json evidence/raw/item13/shaft-motion-r1-custody/downloaded/archive-manifest.json
uv run python -m tools.archive_item7_evidence restore --archive evidence/raw/item13/shaft-motion-r1-custody/downloaded/item13-shaft-motion-r1-d11e4a53.tar.gz --manifest evidence/item-13/shaft-motion/custody/archive-manifest.json --target evidence/raw/item13/shaft-motion-r1-custody/restored-download --receipt evidence/item-13/shaft-motion/custody/download-restore.json
git fetch origin tag item13-shaft-motion-r1-d11e4a53
git rev-parse item13-shaft-motion-r1-d11e4a53
```

The generated manifest is an irreducible member inventory, isolated with this
capture's custody evidence. No new archive or restore implementation was added.
The native result and its limits are in the authoritative temple report.
