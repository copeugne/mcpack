# Controlled test environment

`test-environment-v0.1` is an isolated, disposable dedicated-server configuration. It never reads a production instance. Every seed instance is created from the pinned NeoForge platform, Item 2 configuration evidence, the Item 3 acquisition manifest, and the 136-file retained manifest.

## Naming contract

- Configuration versions: `test-environment-vMAJOR.MINOR`.
- Experiment branches: `experiment/item-N-short-purpose`.
- Runtime instances: `instances/item4/<seed-role>`.
- Untouched controls: a newly materialized instance that has never booted.
- Backups: `backups/item4/<seed-role>-<checkpoint>.tar.gz` with a committed receipt.

Configs are versioned by their Item 2 evidence paths and this configuration version. Project datapacks, spawn rules, loot tables, and worldgen overrides have explicit empty inventories under `versions/test-environment-v0.1`; generated mod defaults are evidence for Item 6 and must not be tuned during Item 4.

## Materialize or regenerate

Acquire the pinned platform and candidates using the Item 2 and Item 3 procedures. Create the pristine NeoForge installation and overlay `evidence/item-2/configs/`. Then, for each role in `seed-suite.json`, run:

```bash
uv run python tools/manage_item4_environment.py materialize \
  --pristine instances/item4/pristine-platform \
  --artifact-manifest evidence/item-3/artifact-acquisition-manifest.json \
  --retained-manifest evidence/item-3/runtime/retained-server-candidates.txt \
  --seed-suite test-environment/seed-suite.json \
  --role ordinary \
  --target instances/item4/ordinary
```

The command refuses an existing target, verifies every retained artifact before hard-linking it, removes any `world/` copied from the pristine reconstruction, and only then writes `level-seed`. This guarantees first boot generates the selected role seed instead of silently reusing baseline region data. To regenerate, stop the server, delete the entire disposable role instance, and rerun the command. Do not delete only `world/` while retaining generated state when a clean control is required.

## Backup and restore

Stop and flush the server before backup:

```bash
uv run python tools/manage_item4_environment.py backup \
  --world instances/item4/ordinary/world \
  --archive backups/item4/ordinary-initial-world.tar.gz \
  --receipt evidence/item-4/ordinary-backup-receipt.json
uv run python tools/manage_item4_environment.py restore \
  --archive backups/item4/ordinary-initial-world.tar.gz \
  --sha256 320a63f709a2df2fc9d2abccbb547e9eace05d5b44074fcb501ba294f7f4b0bd \
  --target instances/item4/ordinary-restore
```

Restore refuses an existing target, verifies the archive hash before extraction, rejects links and unsafe archive members, and extracts below a new directory. Copy or rematerialize the versioned server files beside the restored `world/`, then boot, flush, and stop. The committed runtime receipt records the completed proof.

## Automated backup schedule

The committed `mcpack-item4-backup@.timer` runs daily at 03:15 UTC with a persistent catch-up and randomized delay. It invokes `item4-automated-backup`, which refuses an active Minecraft session lock and writes collision-free archives plus raw integrity receipts. Install the units on the isolated test host with:

```bash
sudo systemctl link /workspace/mcpack/infrastructure/systemd/mcpack-item4-backup@.{service,timer}
for role in ordinary mountainous ocean-heavy biome-diverse; do
  sudo systemctl enable --now "mcpack-item4-backup@${role}.timer"
done
systemctl list-timers 'mcpack-item4-backup@*'
```

The archives and per-run receipts remain in ignored operational storage. The unit takes a Java-compatible POSIX record lock and holds it throughout archive creation and receipt hashing; `session.lock` itself is excluded so opening/closing it cannot release the process-scoped record lock. The unit intentionally fails rather than copying a live world; lifecycle orchestration must flush and stop a server before its scheduled backup window.

## Rollback

Rollback never mutates the failed experiment in place. Stop it, preserve any required failure evidence, restore the selected hash-verified backup into a new target, attach the same configuration version, and boot-validate that new target. This keeps controls and failures independently auditable.
