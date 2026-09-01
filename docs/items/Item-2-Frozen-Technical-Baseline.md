# Item 2 — Frozen Technical Baseline

**Status:** `COMPLETE` — local archive restore, fresh operational reconstruction, durable remote retrieval, and the Git checkpoint all pass.

**Scope:** this is a newly constructed zero-third-party-mod control for Minecraft Java 1.21.1. It is not a claim that the 190 candidate filenames were installed, compatible, or the eventual pack.

## Evidence status

| Class | Treatment in this record |
|---|---|
| Primary evidence | Local artifact bytes and digests, generated configuration copies, host discovery, NeoForge installer output, runtime logs, and local archives captured on 2026-09-01. |
| Reconstructed documentation | Prior handoff and surviving Item 4–10 reports are comparison context only. They do not establish this item. |
| Provisional conclusion | A zero-mod control is retained until Item 3 finishes the candidate-specific compatibility decision. |
| Untested assumption | The 2–6 normal and 10 peak player targets are handoff-recorded user decisions; no performance capacity result is claimed. |
| Missing evidence | No load-bearing Item 2 evidence. Client join, candidate compatibility, worldgen correctness, and performance remain downstream gates. |

The machine-readable execution record is [baseline-execution-record.json](../../evidence/item-2/baseline-execution-record.json). The untouched file-level baseline is [baseline-manifest.json](../../evidence/item-2/baseline-manifest.json); it enumerates 135 files and 251 directories, including every installed library file and retained runtime log with size and SHA-256. [reconstruction-manifest.json](../../evidence/item-2/reconstruction-manifest.json) excludes only transient `logs/` and pins all 131 operational files and 250 operational directories required for an exact clean materialization.

## Frozen identity

| Component | Verified identity | Evidence |
|---|---|---|
| Minecraft server | `1.21.1`, `server.jar`, 51,627,615 bytes, SHA-1 `59353fb40c36d304f2035d51e7d6e6baa98dc05c`, SHA-256 `e3bc55693e93cda0188f2e60aea28113fc647c5e85a15fa3d1b347349231b4bb` | Mojang 1.21.1 metadata and local digest. |
| Loader | NeoForge `21.1.249`, installer SHA-256 `d88b448eab73cd65bdf1720844a4828262de30a15fc71bd04dd81acc61c5399a` | Official NeoForged Maven SHA-256/SHA-512 sidecars and local digest. |
| Java | Eclipse Adoptium Temurin `21.0.12.1+1-LTS`, Linux x64 HotSpot, archive SHA-256 `ce79869e1307ed8ee1e2baa86a412b1eb5b75d10a01006d788a6f968bcfaee94` | Adoptium release/API metadata, sidecar, local digest, and pinned runtime `java -version`. |
| Mod set | Zero enabled JARs; zero disabled JARs; `mods/` exists and is empty. | Baseline manifest and materialized directory inspection. |
| EULA | `eula=true`, SHA-256 `ee27072e4a23e088522f740ddaab0c7c4145c186969e90a86254faa3a5ec5ce6` | Authorized materialization and copied config evidence. |
| Construction heap | `-Xms1G -Xmx4G` | `user_jvm_args.txt` and effective JVM-flags receipt. This is not a production allocation. |

The sources, retrieval date, exact filenames, hashes, distribution limitation, and acquisition procedure are machine-readable in [artifact-acquisition.json](../../evidence/item-2/artifact-acquisition.json). Retrieval date is `2026-09-01` for every listed primary source. Redistribution-restricted binaries are intentionally not committed; the record supplies a lawful reproducible acquisition route and hash checks instead.

## Runtime and installation observations

All four server scenarios used the pinned project-local Temurin binary directly with `@user_jvm_args.txt @libraries/net/neoforged/neoforge/21.1.249/unix_args.txt nogui`.

| Scenario | Exact observable | Raw evidence |
|---|---|---|
| Fresh boot | Minecraft `1.21.1` and NeoForge `21.1.249` logged; readiness `Done (3.777s)`; all dimensions saved; graceful stop logged. | `evidence/raw/item2/boot1/latest.log`, SHA-256 `b158c3f0b5ba12b6dbfeaf3a532a9122f2c0902e86d48c05a82220e621fda7b2` |
| Existing-world restart | Readiness `Done (0.871s)`; server `seed` response `8953077177248245348`; all dimensions saved; graceful stop logged. | `evidence/raw/item2/boot2/latest.log`, SHA-256 `66b687ab52b80ea48d7a0982e2ddedcb9a227fa8f88caaeccb4dd4f88895e798` |
| Restored-world boot | Readiness `Done (0.914s)`; server `seed` response `8953077177248245348`; flush and graceful stop logged; no matched fatal signature. | `evidence/raw/item2/restore-boot/latest.log`, SHA-256 `12a0f3f4e7d12a4a35f41ff44cfc98585b6a6241aa9e0fc9d6131912ceed8ad3`; debug SHA-256 `6121921877b0c8174ca4ba3a3738119c6a86ecee92fd232c3df056136b4dcbb4` |
| Fresh operational reconstruction | A new project-local Java extraction, new NeoForge target, and hash-verified state overlay matched all 131 operational file identities and 250 directories before boot; readiness `Done (0.852s)`, exact seed, runtime datapack list, flush, and exit 0 observed. | [clean-room-receipt.json](../../evidence/item-2/clean-room-receipt.json); latest log SHA-256 `a623201a1004259820b01928b522f96a48341d379d7fed67254b601f5a5819a9` |

The installer was also run twice in a fresh target. Both runs exited successfully. The two full tree manifests differ only in `neoforge-21.1.249-installer.jar.log`, a deliberately regenerated diagnostic log. With that path excluded, 106 operational files and 235 directories match byte-for-byte, normalized manifest SHA-256 `37b8c58475b8575b366ea4df70d7d329c766db50831925c3d91ead696134433f`. This is safe convergence with an explicit log exception, not an assertion of byte-identical complete trees.

Effective JVM evidence shows ergonomic G1GC, initial heap 1,073,741,824 bytes, maximum heap 4,294,967,296 bytes, G1 region 2,097,152 bytes, three concurrent GC threads, and 13 parallel GC threads. Raw receipt: `evidence/raw/item2/java/runtime-flags.txt`, SHA-256 `951a26d0b4a7e7131a8037b09cbe26033d9366b85bee8b3a5d6f989cbbe64d62`.

## Configuration, datapacks, and world generation

The copied configuration set is under [evidence/item-2/configs](../../evidence/item-2/configs). It includes `eula.txt`, `server.properties`, `user_jvm_args.txt`, `config/fml.toml`, `config/neoforge-common.toml`, and `config/neoforge-server.toml`; the manifest is the authoritative file/hash listing.

The generated world is named `world`; `level-seed=8953077177248245348`, `level-type=minecraft:normal`, `generator-settings={}`, and `generate-structures=true`. `world/datapacks/` exists and is empty; `initial-enabled-packs=vanilla`, `initial-disabled-packs=`. No custom datapack, custom world preset, or third-party world-generation configuration was installed in this control. The seed is a reconstruction/proof seed, not yet an Item 4 deterministic test-suite designation.

## Host and scale facts

Primary host discovery is [host-discovery.json](../../evidence/item-2/host-discovery.json). Captured facts include PikaOS 4, kernel `7.1.0-pikaos`, x86_64; AMD Ryzen 7 7840HS (8 cores, 16 logical CPUs); 27,091,542,016 bytes physical RAM; Btrfs storage on an NVMe device; project-local filesystem availability captured at 46,070,128,640 bytes; and the recorded current port states. The discovery record also contains cgroup, limits, package manager, runtime, container, clock, and authoritative-endpoint probes. All four required authoritative endpoints returned HTTP 200 after correcting the Mojang metadata path.

Normal concurrency is **2–6** and peak concurrency is **10**, as handoff-recorded user decisions. They remain planning inputs pending player-count and performance measurements; they are not evidence that this host can safely carry that load.

## Archives and raw evidence

| Archive | Local path | Bytes | SHA-256 | Content |
|---|---|---:|---|
| Complete frozen server | `evidence/raw/item2/frozen/pristine-baseline-v0.tar.gz` | 160,322,927 | `4e4df44f0e0258f3814b5f20d22befd948dff58f21a5e2290ec087df53214c44` | Full installed instance, libraries, configurations, and generated control world. |
| State overlay | `evidence/raw/item2/frozen/pristine-baseline-v0-state.tar.gz` | 1,275,395 | `d7880902d37011075a3548404ffe84f0073ef5da7788b6244a24204dd3531663` | Mutable configs, empty `mods/`, and world state; combine with a verified fresh NeoForge installation to reproduce the operational tree. |

All retained raw paths, sizes, and hashes are in [raw-evidence-inventory.json](../../evidence/item-2/raw-evidence-inventory.json). The redistributable state overlay and raw-evidence bundle are published at the `item-2-evidence-assets-2026-09-01` GitHub release. Both were downloaded into a fresh directory and matched the expected sizes, SHA-256 values, and tar integrity checks; the exact URLs and retrieval procedure are in [durable-storage-receipt.json](../../evidence/item-2/durable-storage-receipt.json).

The complete archive is intentionally not public because it contains redistribution-restricted Mojang and NeoForge software. Its exact local identity remains recorded, while the public state overlay, exact authoritative acquisition metadata, provisioning automation, reconstruction manifest, and passing clean-room receipt form the lawful equivalent reproducible snapshot.

## Decision log and limitations

The decisions, reversibility, and outstanding questions are in [decision-log.json](../../evidence/item-2/decision-log.json). The key safety decision is to keep all candidates out of this control until Item 3 resolves exact source, loader, side, dependency, and point-release compatibility. The candidate file at `candidate-mods/current-jars-2026-09-01.txt` is a separate tentative inventory; it must not be read as an enabled/disabled baseline manifest.

This record does not claim gameplay correctness, terrain correctness, structure density, client connectivity, or acceptable performance. It also does not independently verify the preserved Temurin detached-signature trust chain. The clean-room run used a fresh isolated target and Java extraction on the same discovered host with a verified content-addressed cache; it was not a cache-cold download or second physical host.

## Reproduction

1. Run `infrastructure/bin/platform-1.21.1 acquire --root . --cache <cache>`; the manifest-driven command downloads only the four exact entries and rejects size or SHA-256 mismatches.
2. Run `provision-java` with explicit cache and project-local Java paths; invoke that exact `bin/java`, never ambient `PATH` Java.
3. Run `materialize-pristine` with explicit empty target, installer-log, and verified state-overlay paths. The command retains installer logs outside the live instance, rejects unsafe overlay members, and does not install candidate JARs.
4. Run `verify-instance --target <target> --reconstruction-manifest evidence/item-2/reconstruction-manifest.json`; every operational path, size, hash, and directory must match and no unsupported path type may exist.
5. The untouched full archive can separately be checked with `sha256sum evidence/raw/item2/frozen/pristine-baseline-v0.tar.gz` before controlled extraction into an empty validated target.
6. Start from the target directory with the command in the runtime section. Wait for the `Done (` readiness line, issue `seed`, `save-all flush`, and `stop`; retain `latest.log` and `debug.log`.
7. For a restored-world check, extract only after validating the archive digest into a separate target, then repeat step 6 without modifying the original instance.

Suggested verification commands:

```bash
jq -e . evidence/item-2/*.json platform/pristine-platform.json
sha256sum evidence/raw/item2/frozen/pristine-baseline-v0.tar.gz
sha256sum evidence/raw/item2/frozen/pristine-baseline-v0-state.tar.gz
find evidence/raw/item2 -type f -exec sha256sum {} + | sort
```

## Exit-gate assessment

The Item 2 exit gate is **complete**. Exact primary evidence, a local archive restore, a fresh operational reconstruction, a fresh remote-asset retrieval, and the pushed/tagged evidence checkpoint are recorded in [exit-gate-assessment.json](../../evidence/item-2/exit-gate-assessment.json). This authorizes Item 3 only; it does not establish candidate compatibility or any later gameplay, world-generation, or performance gate.
