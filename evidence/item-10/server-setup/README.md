# Local player server profiles

The user requested two separate profiles on 2026-09-08 and confirmed that they
will join from this computer using the official Minecraft Launcher.

| Profile | Instance directory | Local multiplayer destination |
| --- | --- | --- |
| Free roaming | `instances/item10-player-profiles/free-roaming` | `localhost:25565` |
| Item 10 task | `instances/item10-player-profiles/task` | `localhost:25566` |

Both use separate worlds, the ordinary seed, the frozen Item 6 configuration,
Minecraft 1.21.1, NeoForge 21.1.249 and pinned Temurin with a 1 to 4 GiB heap.
The 136 retained JARs plus the existing verified Chunky instrument are reused.
Only network binding, port, authentication, console-network access and MOTD are
set explicitly for local operation. Authentication remains enabled. Gameplay
configuration, difficulty and game mode are unchanged. Neither profile is a
pregenerated Item 10 sample or evidence of gameplay compatibility.

## Reproduction

From the repository root, with the already documented Item 3 acquisition paths
and pristine platform present, the executed setup command is:

```sh
uv run --no-sync python -m tools.setup_item10_play_servers \
  --target instances/item10-player-profiles \
  --java-home downloads/item2/temurin/extracted/jdk-21.0.12.1+1
```

The tool reuses Item 7's hash-verified preflight and frozen-config application,
without executing its generation selections. It refuses an existing target;
that rejection was exercised after creation. Never remove a player world to
make this setup command run again. Use a new explicitly selected target instead.

Start one profile at a time from a terminal:

```sh
instances/item10-player-profiles/free-roaming/start.sh
```

or:

```sh
instances/item10-player-profiles/task/start.sh
```

Each generated start script invokes the pinned Java executable directly and
uses its own instance directory. Wait for `Done` before joining. To stop, send
`save-all flush` in the server console, wait for `Saved the game`, then send
`stop` and wait for process exit. For recorded tests, bracket the flush with
unique `say` markers and wait for each response, as in the setup extracts.

## Verified setup surface

Both profiles reached `Done`, acknowledged their before marker, completed one
save-flush sequence, acknowledged their after marker and stopped with exit code
0. They were run sequentially and are now stopped. Exact preflight digests are
in the two `*-preflight.json` files. The `*-lifecycle.txt` files retain selected
raw log lines with full source hashes and sizes. Complete operational logs remain
in the instance directories. These extracts are setup evidence, not the durable
raw-world evidence required to close Item 10. No player joined during this check.

The extracts select only the JVM/version, readiness, explicit marker, flush,
all-dimensions-saved and stopping messages from `logs/latest.log`. Their source
paths and hashes permit direct inspection without treating omitted warnings as
resolved. The full retained-stack warnings were not re-audited in this setup.
Focused Ruff lint and formatting checks pass for the setup tool. The initial
string-concatenation and formatting findings were corrected before delivery.

The official client profiles are still being prepared. The existing local
Minecraft 1.21.10 client is not compatible with this server's frozen version.
Follow the [official NeoForge client procedure](https://docs.neoforged.net/user/docs/client/)
with the pinned 21.1.249 installer, not a newer default version.

Persistent space after server setup is about 1.4 GiB. A read-only estimate using
Minecraft 1.21.1's asset index 17 (SHA-1
`dda7c8d44a8c7e3f5db430d657106af4e5bdc715`) found 2,098 of 3,888 unique
objects absent or of the wrong size in the existing client cache. Their declared
sizes sum to 648,853,008 bytes. The index was fetched from its URL in
`downloads/item2/minecraft/1.21.1.json` and its SHA-1 verified. This is a local
size/existence estimate, not verification of existing object contents. It excludes
the 26,836,906-byte client JAR, libraries, installer intermediates and runtime.
No client download or launcher-profile mutation has been performed. A persistent
storage location or explicit disposable-file disposition has been requested.
Sustained exploration, client downloads and Item 10 evidence need that budget.
The task world must be kept separate from free roaming and must not be called
an accepted observation run until its protocol and recording conditions are met.
