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

## Official client profiles

Created `mcpack: free-roaming` and `mcpack: task` in the official launcher's
`launcher_profiles.json`. Their game directories are respectively
`instances/item10-client-profiles/free-roaming` and
`instances/item10-client-profiles/task`. Both select `neoforge-21.1.249`, pinned
Temurin and `-Xms1G -Xmx4G`. Existing profile entries and other JSON fields were
compared against the local pre-edit backup and preserved. The launcher was
closed before mutation. The backup remains in the ignored client target.

Executed setup, after installing NeoForge using the
[official client procedure](https://docs.neoforged.net/user/docs/client/):

```sh
uv run --no-sync python -m tools.setup_item10_play_clients \
  --target instances/item10-client-profiles \
  --minecraft "$HOME/.minecraft" \
  --java-home downloads/item2/temurin/extracted/jdk-21.0.12.1+1
```

Close the launcher before this command. It refuses an existing target or profile.
Do not remove an existing game directory to rerun it. The rejection was exercised
on the created target. Focused Ruff lint and formatting pass. Each destination's
108 JAR hashes were independently compared with the accepted acquisition manifest.
The frozen configuration validator passed before copying `config` and
`defaultconfigs`; the sanitized Resourceful web secret file is omitted, as in the
server materializer. Client-generated settings and compatibility remain unverified.

The [client candidate list](client-candidates.txt), SHA-256
`02b9e1a1c88bf1c4fe3527960e06eb25cd3fecb736b237e9e1de0babf156c122`,
is provisional client scope, not a change to the accepted dedicated-server set.
It uses 102 of the retained 136 candidates whose publisher client-side declaration
is not unsupported in `../../item-3/source-identity-matrix.json`. Actual required
client/shared dependency declarations in `../../item-3/jar-inspection.json` add
Lithostitched, Repurposed Structures and Structure Pool API despite publisher side
labels. Three client dependencies are added from the accepted acquisition cache:
Athena, EMI and Simply Tooltips. Simply Tooltips was rejected for the dedicated
server; this explicit client-only inclusion does not restore it to either server.
The existing dedicated-server evaluator is not evidence of client compatibility.
No Simply More, Sable, Aeronautics, Every Compat or Spell Engine family was added.
Exact per-JAR sizes and hashes are in `../../item-3/artifact-acquisition-manifest.json`.

The pinned NeoForge installer SHA-256 is
`d88b448eab73cd65bdf1720844a4828262de30a15fc71bd04dd81acc61c5399a`.
An initial attempt failed because no launcher profile file existed. After creating
an empty profile container, the second attempt exited 0 and installed
`neoforge-21.1.249`. Both console logs remain under ignored
`evidence/raw/item10/client-setup/`. They are operational diagnostics, not accepted
Item 10 measurement evidence. The official launcher subsequently populated its
standard release/snapshot entries; those entries were preserved by client setup.

Reopen the launcher and select the desired profile under Installations. First Play
may download assets and requires the user's normal authenticated account. Join
the matching destination in the table only after its server reports readiness.
A client launch and server join have not yet been verified. Neither the profiles
nor server startup prove client compatibility or any Item 10 metric.

The prior 1.4 GiB storage blocker was relieved by user cleanup and explicitly
authorized removal of eight byte-identical duplicate evidence directories,
retaining their matching copies. About 15 GiB is available after client profile
materialization. The prior asset-index estimate was 648,853,008 bytes missing or
wrong-sized, excluding libraries and installation workspace. The launcher manages
remaining downloads. Full measurement storage still needs a bounded plan.
The task world is separate from free roaming and cannot be called an accepted
observation run until its protocol and recording conditions are met.

## Recording proposal withdrawn

The user rejected long gameplay recording and the subsequent proposed combat
logger on 2026-09-08. No capture or combat logger was started. Installed recording
tools are not evidence of an adequate measurement workflow. The two local play
profiles remain available for the user's separate play request; neither implies
an approved measurement session or acceptance of Item 10 combat density.

## Additional duplicate cleanup

On 2026-09-08 the user requested further byte-identical duplicate cleanup.
Sixteen `evidence/raw/item10/*-custody/downloaded/*.tar.gz` copies, totaling
543,806,172 logical bytes, were removed only where the same basename existed
in the parent custody directory and both SHA-256 and full byte comparison
matched. Original local archives, restored evidence, worlds and release copies
remain. Immediate filesystem free space did not establish physical recovery
from this deletion, so the logical total is not claimed as reclaimed space.

For repeated regular JARs of at least 1 MiB under instance `libraries` paths,
Linux `FIDEDUPERANGE` on Btrfs shared identical extents without deleting paths,
changing contents or coupling subsequent writes. Files retain separate inodes
and copy-on-write behavior. SHA-256 grouping preceded the kernel's own byte
comparison; each destination was rehashed afterward. All 1,020 destinations
matched and all ioctl statuses were zero, reporting 10,063,571,124 deduplicated
bytes. This is not a claim that all those bytes immediately became free.

Measured available space rose from 3,889,635,328 to 10,711,359,488 bytes across
this operation. Btrfs inspection of the Extras instance libraries reported
141.17 MiB shared and 34.81 MiB exclusive afterward. No configuration, world,
raw observation, tracked file, protected artifact or player profile was removed
by library deduplication. Full collection storage remains unresolved against
the provisional 30 GiB working-space estimate.
