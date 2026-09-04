# Infrastructure, Installation, and Server-Testing Execution Prompt

## Assignment

You are continuing the `mcpack` project from:

- Repository: `https://github.com/copeugne/mcpack`
- Governing specification: `SPECS.md`
- Continuity record: `MCPACK-NEW-SESSION-HANDOFF.md`

This prompt is specifically about creating the complete, reproducible infrastructure needed to install, run, inspect, test, measure, stop, restore, and rebuild the Minecraft pack. It supplements `SPECS.md`; it does not replace or reorder it.

Read `SPECS.md` and `MCPACK-NEW-SESSION-HANDOFF.md` completely before acting. `SPECS.md` is the authoritative chronological and dependency-ordered task list. The infrastructure created here must support the current Items 2–10 work and remain suitable for all later validation phases.

Be thorough, comprehensive, meticulous, rigorous, methodical and systematic.

Do not merely document suggested commands. Implement, execute, test, and validate the infrastructure. A script existing in the repository is not proof that it works. A server process starting is not proof that the environment is reproducible, compatible, healthy, measurable, or restorable.

## Non-Negotiable Rules

1. Inspect the repository, host, available permissions, package manager, network access, installed tools, and current filesystem before changing anything.
2. Do not assume that reconstructed documentation is empirical evidence.
3. Do not assume a package, command, directory, credential, API, container runtime, or graphical environment exists.
4. Detect prerequisites explicitly and record their versions.
5. Prefer reproducible, pinned, checksum-verified installation over mutable `latest` downloads.
6. Never silently substitute versions or artifacts.
7. Use authoritative distribution sources and primary documentation.
8. Respect artifact licenses, API terms, authentication requirements, and redistribution restrictions.
9. Never commit credentials, access tokens, cookies, private download URLs, personal paths, or machine-specific secrets.
10. Do not expose secrets in terminal output, logs, manifests, process arguments, or Git history.
11. Make all scripts idempotent where reasonably possible.
12. Make destructive operations require an explicit, validated target and protect preserved baselines and evidence.
13. Never use broad destructive paths, unresolved globs, or unvalidated variables.
14. Stop the server gracefully before manipulating live world data unless the tested operation explicitly requires an online snapshot.
15. Preserve raw logs and evidence for every validation run.
16. Keep production, baseline-control, experimental, and disposable test environments separate.
17. Treat the candidate JAR inventory as tentative, not mandatory.
18. Do not install client-only mods on a dedicated server merely because they appear in the candidate list.
19. Do not omit a required server-side dependency merely because the client can launch.
20. Ask the user only for a genuinely load-bearing choice or authority that cannot be resolved safely. Log non-load-bearing provisional decisions and continue.

## Expected Platform Pins

The handoff currently records these expected platform pins:

- Minecraft `1.21.1`
- NeoForge `21.1.249`
- Eclipse Temurin Java `21.0.12.1+1`
- EULA acceptance already granted by the user
- Baseline heap target: `-Xms1G -Xmx4G`

Verify these values against the repository and authoritative sources before relying on them. If repository evidence disagrees, stop treating either value as authoritative, document the discrepancy, resolve it from primary evidence, and commit the resolution. Never drift to a newer release merely because it is easier to download.

## Required Outcome

Create an infrastructure layer from which another competent agent on a clean Linux environment can:

1. Clone the repository.
2. Run one documented bootstrap entry point.
3. Install or acquire all permitted host prerequisites.
4. Install the exact Java runtime without replacing the host's unrelated Java installation.
5. Acquire and verify the exact NeoForge installer/server artifacts.
6. Acquire or stage the exact permitted mod artifacts.
7. Separate server-required, client-required, shared, disabled, quarantined, and unresolved artifacts.
8. Materialize a pristine baseline server.
9. Accept the EULA using the user's recorded authorization.
10. Generate or install exact configuration files and datapacks.
11. Start the server with pinned JVM arguments.
12. Detect readiness reliably.
13. Execute administrative and measurement commands through a controlled interface.
14. Generate deterministic test worlds.
15. Stop the server gracefully.
16. Restart the same world and prove persistence.
17. Back up and restore the world and prove the restored copy boots.
18. Reset a disposable world safely and regenerate it from its manifest.
19. Collect logs, crash reports, timings, Spark results, hashes, and run metadata.
20. Reproduce the same environment in a fresh clean-room workspace.

## Infrastructure Scope

### 1. Host Discovery

Record, in machine-readable and human-readable form:

- Distribution and release
- Kernel and architecture
- CPU model, logical CPUs, physical cores when discoverable, and relevant instruction-set constraints
- Physical RAM, available RAM, swap, and cgroup/container limits
- Storage filesystem, available capacity, and whether storage is local, networked, rotational, or solid-state when discoverable
- Effective user and groups without recording irrelevant personal data
- Available privilege-escalation mechanism
- Package manager and configured repositories
- Shell and shell version
- Existing Java installations
- Git and Git LFS availability
- Container runtime availability, if any
- Network reachability to every required authoritative artifact host
- Open ports and conflicts relevant to Minecraft, RCON, query, voice chat, and profiling
- System clock, timezone, and time-synchronization status
- File-descriptor and process limits
- Any execution sandbox, CPU quota, memory quota, or network restriction

The discovery process must be read-only. Save its output as evidence before provisioning.

### 2. Host Prerequisite Installation

Implement a bootstrap process that checks for and, when authorized and supported, installs the exact required host tools. This may include:

- CA certificates
- A secure download client
- Git and Git LFS
- Archive and compression tools
- Cryptographic hashing tools
- JSON and YAML processing tools
- Process and port inspection tools
- Filesystem synchronization tools
- Python or another scripting runtime only where repository tooling genuinely requires it
- A controlled RCON or console client if used by the harness
- Spark prerequisites and supporting diagnostic utilities

Requirements:

- Detect the package manager instead of assuming `apt`.
- Separate required packages from optional operator conveniences.
- Pin package versions where practical, or record the resolved repository version and repository snapshot limitations.
- Support an unprivileged fallback for project-local tools when safe and practical.
- Do not mutate the user's global Java selection.
- Record every installed package and version.
- Make repeated bootstrap runs converge without destructive side effects.
- Include a dry-run or check-only mode.
- Fail with an actionable diagnostic when installation authority is unavailable.

### 3. Java Runtime Provisioning

Implement exact Java provisioning that:

- Obtains the approved Java 21 runtime from an authoritative source.
- Verifies filename, release, architecture, download source, size, and SHA-256 or stronger digest.
- Verifies archive extraction succeeded.
- Installs it into a project-controlled toolchain location unless the exact runtime is already present and verified.
- Exports or resolves a project-specific `JAVA_HOME` without overwriting the user's global configuration.
- Verifies `java -version` and records its complete output.
- Rejects an unsupported major version, architecture, vendor mismatch where vendor is pinned, or corrupted runtime.
- Records JVM implementation and garbage collector defaults relevant to later benchmarking.
- Makes launch scripts invoke the pinned Java binary directly rather than relying on ambient `PATH` ordering.

### 4. NeoForge Server Provisioning

Implement the exact NeoForge server installation workflow:

- Resolve the authoritative installer URL for the pinned version.
- Download to a content-addressed cache when permitted.
- Verify the installer artifact against authoritative checksums or independently recorded SHA-256 evidence.
- Run the installer using the pinned Java runtime.
- Capture complete installer output and exit status.
- Verify expected libraries, launch metadata, argument files, and server files were produced.
- Prove a second run does not corrupt or unpredictably replace the installation.
- Record every generated path needed to reconstruct the server.
- Never commit third-party binaries when redistribution is disallowed.
- Commit acquisition metadata and a reproducible retrieval process instead.

### 5. Mod and Dependency Acquisition

Build a manifest-driven artifact acquisition system. For every candidate or retained artifact, record:

- Canonical mod name
- Mod ID when known
- Exact filename
- Exact version
- Minecraft version
- Loader and loader version compatibility
- Source project and authoritative download page/API
- Direct artifact source where terms permit recording it
- File size
- SHA-256 or stronger hash
- Required dependencies and accepted version ranges
- Optional dependencies and enabled integrations
- Side classification: dedicated server, client, or both
- Status: retained, disabled, quarantined, rejected, unresolved, or superseded
- Redistribution status
- Reason for the status

The acquisition system must:

- Download only explicitly manifested artifacts.
- Verify every downloaded artifact before staging it.
- Refuse hash mismatches.
- Refuse filename collisions with different content.
- Avoid scraping or bypassing authentication controls.
- Support manual-placement instructions for artifacts that cannot be automatically acquired.
- Detect missing dependencies before server launch.
- Detect duplicates, embedded-library overlap, loader mismatch, and obvious wrong-point-release artifacts.
- Preserve disabled candidates outside the live server `mods` directory.
- Produce a resolved enabled manifest for each experiment.
- Never treat a successful download as proof of compatibility.

### 6. Server, Client, and Shared Artifact Separation

Define and enforce separate artifact sets for:

- Dedicated server
- Test client
- Shared client/server content
- Client-only quality-of-life and rendering
- Server-only administration and profiling
- Disabled candidates
- Quarantined compatibility failures
- Experimental branches

Generate the live directories from manifests instead of maintaining ambiguous hand-copied folders. Verify that:

- The dedicated server has no unnecessary rendering, shader, UI, minimap, animation, or client-only JARs.
- The test client includes every required shared dependency.
- Disabled files cannot be accidentally loaded.
- Experimental artifacts cannot leak into the pristine baseline.
- The manifest and materialized directory agree byte-for-byte.

### 7. Canonical Directory Layout

Adapt to the existing repository rather than duplicating an equivalent structure. If no adequate layout exists, establish a documented structure covering:

- Bootstrap and provisioning scripts
- Pinned toolchains
- Artifact manifests
- Download cache metadata
- Pristine baseline template
- Materialized server instances
- Test-client profile metadata
- Shared configurations
- Server configurations
- Client configurations
- Datapacks
- Test seeds and world manifests
- Disposable generated worlds
- Preserved control worlds
- Backups
- Restore-test targets
- Runtime logs
- Crash reports
- Profiling evidence
- Structure-survey evidence
- Run manifests
- Decision records
- Machine-readable status reports

Generated binaries, caches, worlds, logs, credentials, and large evidence must be ignored appropriately by Git. Their manifests, hashes, provenance, schemas, and retrieval instructions must be committed.

### 8. Configuration Materialization

Implement deterministic configuration materialization:

- Copy or generate `eula.txt` only from the user's recorded acceptance.
- Generate `server.properties` from a versioned source template.
- Pin the intended world seed, level name, difficulty, game mode, command permissions, network settings, and world-generation settings per test profile.
- Keep secrets and private network bindings outside committed templates.
- Materialize NeoForge common, server, and client configurations into their correct locations.
- Install datapacks before the relevant world's first generation when required.
- Record configuration hashes in every run manifest.
- Detect uncommitted runtime-generated configuration drift.
- Preserve pristine generated defaults separately from intentional overrides.
- Do not normalize or rewrite unknown configuration formats destructively.

### 9. JVM and Launch Configuration

Provide versioned launch profiles for at least:

- Pristine baseline smoke test
- Candidate-stack compatibility test
- Fresh-world generation test
- Structure-density survey
- Active-combat profiling
- Backup/restore validation
- Expected normal concurrency
- Expected peak concurrency

Each profile must explicitly define:

- Pinned Java binary
- Minimum and maximum heap
- Garbage collector and JVM flags
- NeoForge launch arguments
- Server directory
- Port assignments
- World/profile identity
- Logging destination
- Readiness timeout
- Graceful-shutdown timeout
- Test-specific environment variables

Do not apply fashionable or copied JVM flags without evidence. Record why every non-default flag exists. Keep benchmark flags stable within a comparison series.

### 10. Server Lifecycle Commands

Implement documented, tested commands or scripts for:

- `bootstrap`
- `doctor` or prerequisite validation
- `acquire-artifacts`
- `verify-artifacts`
- `materialize-instance`
- `start`
- `status`
- `wait-ready`
- `send-command`
- `save`
- `stop`
- `restart`
- `tail-logs`
- `collect-evidence`
- `create-world`
- `reset-disposable-world`
- `backup`
- `restore`
- `verify-restore`
- `clean-generated-files`

Requirements:

- Use PID files or an equally reliable process identity mechanism.
- Reject stale or mismatched PID state safely.
- Do not consider an open TCP port alone sufficient readiness evidence.
- Detect the actual successful server-ready log event and confirm the process remains alive.
- Surface crash reports, missing dependencies, mixin failures, registry errors, datapack errors, and watchdog termination.
- Use a controlled console or authenticated local RCON path for commands.
- Do not expose RCON publicly.
- Execute `save-all flush` or its validated equivalent before backup and shutdown when appropriate.
- Send `stop` and wait for clean termination before escalating.
- Never use unconditional force-kill as the normal shutdown path.
- Preserve the complete log from process start through termination.

### 11. Port and Network Isolation

Assign ports deterministically per instance and test branch. Cover where applicable:

- Minecraft server
- RCON
- Query
- Voice chat
- Profiling or metrics endpoints

Verify port availability before launch. Bind administrative interfaces to loopback unless a documented test requires otherwise. Do not disable host security controls or expose the test server to the public internet merely to simplify testing.

### 12. Deterministic World Management

For ordinary, mountainous, ocean-heavy, and biome-diverse test cases:

- Record exact seed values.
- Record dimension and world-generation settings.
- Record configuration, datapack, mod-manifest, Java, NeoForge, and script commit hashes.
- Materialize each run under a unique deterministic run ID.
- Prevent reuse of a world generated under a different manifest.
- Preserve untouched controls.
- Make deletion/reset available only for explicitly disposable worlds.
- Validate the exact target before resetting.
- Record generation radius, expected chunk count, completion state, and integrity checks.
- Preserve failed worlds when they contain diagnostic value.

### 13. Automated Smoke-Test Sequence

Implement and execute at least this sequence:

1. Validate repository cleanliness or intentionally recorded changes.
2. Run host discovery.
3. Run prerequisite doctor checks.
4. Verify the pinned Java runtime.
5. Verify NeoForge installation integrity.
6. Verify every enabled artifact hash.
7. Verify dependency closure and side classification.
8. Materialize a fresh disposable server instance.
9. Materialize EULA and configuration files.
10. Launch the server.
11. Detect readiness within a documented timeout.
12. Confirm expected Minecraft and NeoForge versions from runtime evidence.
13. Confirm the effective mod list from runtime evidence.
14. Confirm datapacks and registries load without fatal errors.
15. Create or load the intended deterministic world.
16. Execute a harmless console command and capture the response.
17. Trigger a save and verify world files change coherently.
18. Stop the server gracefully.
19. Confirm clean process termination.
20. Restart the same world.
21. Confirm the world loads and persisted state remains.
22. Stop it again cleanly.
23. Archive the complete run manifest and evidence.

The smoke test must fail if the server crashes, never reaches readiness, loads the wrong version, omits required mods, reports fatal registry/datapack errors, or cannot stop cleanly.

Do not blindly fail on every textual occurrence of `WARN` or `ERROR`; classify known benign messages separately and preserve the raw log. Every suppression requires a documented exact signature and rationale.

### 14. Backup and Restore Validation

Implement and execute a real restore test:

- Identify exactly what must be backed up.
- Obtain a consistent save state.
- Create a timestamped or content-addressed archive.
- Record included paths, excluded paths, size, duration, and digest.
- Restore into a different validated target directory.
- Verify archive integrity before extraction.
- Prevent path traversal during extraction.
- Start the restored server without mutating the original.
- Confirm the expected world identity and persisted marker.
- Stop the restored server cleanly.
- Record restore duration and result.

A backup command succeeding is not an exit gate. The restored world must boot correctly.

### 15. Test-Client Infrastructure

Where Items 7–10 require visual inspection or real player interaction, create a reproducible test-client profile separate from the dedicated server:

- Exact Minecraft, NeoForge, Java, shared-mod, dependency, and client-only manifests
- Correct server address and test identity documentation without committed credentials
- Client configuration and resource-pack handling
- Logs and crash reports
- Screenshot naming convention containing seed, coordinates, dimension, run ID, and finding ID
- Procedure for joining the dedicated test server
- Procedure for verifying client/server mod compatibility
- Procedure for reproducing terrain and structure findings

If a graphical client cannot run in the current environment, do not fabricate visual validation. Complete all headless-capable work, prepare the exact client profile, document the blocker, and mark visual subitems incomplete.

### 16. Profiling and Measurement Infrastructure

Install and validate the tooling needed for `SPECS.md` Item 5 and later tests:

- Spark with the exact retained version and side classification
- Runtime commands for TPS, MSPT, tick health, entities, memory, garbage collection, chunk generation, and pathfinding evidence where technically available
- Stable warm-up and sampling periods
- Machine and cgroup metadata captured with each run
- Structured run manifests
- Raw profiler outputs
- Conversion or summarization scripts that never destroy raw evidence
- Repetition-safe output paths
- Timeout and interrupted-run handling

Benchmark comparisons must use equivalent host allocation, Java, JVM flags, configuration, seed, generation scope, and warm-up conditions. Record deviations rather than hiding them.

### 17. Failure Diagnostics

On failure, automatically preserve where available:

- Command and sanitized arguments
- Exit code and signal
- Start and end timestamps
- Complete stdout and stderr
- `latest.log`
- Debug log
- Crash report
- JVM fatal-error log
- NeoForge installer log
- Effective artifact manifest
- Configuration hashes
- World/run identity
- Available memory and disk space
- Process state
- Relevant open ports
- Last known server lifecycle state

Produce a concise failure summary pointing to raw evidence. Do not retry indefinitely or erase the failed instance before evidence collection.

#### Item 7 Operational Regressions to Prevent

The following requirements come from failures observed while completing Item 7:

- Do not run server instances concurrently when they share configured ports. Either allocate and verify distinct ports for every instance or run the instances sequentially.
- Correlate `save-all flush` with unique before and after console markers. Require exact marker matches and exactly one ordered `Saving the game` then `Saved the game` sequence between those markers. Reject missing, mismatched, reordered, or duplicate complete sequences.
- Launch every server in a dedicated process group. On timeout, interruption, or post-launch I/O failure, terminate and reap the complete process group so child Java processes cannot survive the harness.
- Make the post-`stop` clean-exit timeout explicit and configurable. Do not assume that 30 seconds is sufficient; the Item 7 retained-stack recovery required a 120-second allowance to avoid killing an otherwise valid shutdown.
- Before reopening or copying a preserved source world, verify its complete preboot file inventory byte-for-byte against the recorded world identity. Bind the recovery result to that source identity and the exact runtime artifact identity.
- Distinguish a raw-evidence custody tag from the final repository completion boundary. A verifier-only correction that does not change raw bytes, archive production, manifests, restores, or publication must not trigger another archive revision. The final merged commit must contain the corrected verifier and reproduce the accepted result.
- Before creating an evidence archive, verify that the existing staging path includes every required evidence directory. Fail if required evidence is omitted or if an unexplained path would be admitted.
- Define complete validation result contracts explicitly. Do not derive the required output set from a partial internal list when separately generated unresolved or method-limited results also belong to the accepted contract.

### 18. Clean-Room Reproducibility Test

After the primary environment works, prove reproducibility in a fresh directory and, where available, a clean container or separate clean Linux environment:

1. Start with only the repository, documented credentials supplied through the approved secret mechanism, and allowed artifact access.
2. Run the documented bootstrap entry point.
3. Acquire and verify all artifacts.
4. Materialize a new server instance.
5. Execute the automated smoke test.
6. Generate a deterministic test world.
7. Back it up.
8. Restore it to a separate location.
9. Boot the restored world.
10. Compare resolved manifests and hashes with the primary environment.

Record every difference. Do not claim clean-machine reproducibility if the test merely reuses an undocumented global cache, preinstalled runtime, inherited world, or mutable local file.

If only a container test is possible, disclose that it validates software reproducibility but not bare-metal performance. Do not use container measurements as equivalent to production performance without evidence.

## Required Repository Deliverables

Integrate with existing project conventions. At minimum, the repository must contain equivalents of:

- A single documented bootstrap entry point
- Host discovery and doctor commands
- Exact toolchain manifest
- Exact server-platform manifest
- Mod/artifact manifests by side and status
- Artifact acquisition and verification commands
- Instance materialization command
- Versioned launch profiles
- Lifecycle-management commands
- Safe deterministic world-management commands
- Automated smoke-test harness
- Backup and restore harness
- Clean-room validation procedure
- Configuration templates
- Secret-handling documentation
- Generated-data and evidence retention policy
- Troubleshooting guide
- Machine-readable test-result schema
- Human-readable infrastructure validation report

Do not force these exact filenames if the repository already has a coherent equivalent. Document the mapping between required capabilities and actual files.

## Documentation Requirements

Document from the perspective of a new Linux operator with repository access but no hidden machine state. Include:

- Supported Linux environments
- Minimum and recommended CPU, RAM, storage, and file-descriptor requirements
- Required network access
- Required privileges
- Exact bootstrap command
- Check-only command
- Artifact acquisition steps
- Manual artifact-placement steps when unavoidable
- Server materialization command
- First-start procedure
- Readiness verification
- Console/RCON procedure
- Graceful stop and restart
- Fresh-world creation
- Safe world reset
- Backup creation
- Restore validation
- Test-client creation and connection
- Profiling collection
- Evidence locations
- Common failure modes and exact diagnostics
- Full removal of only project-generated disposable infrastructure

Every command shown in documentation must either be executed successfully in the validation environment or clearly marked as an environment-specific example that remains unverified.

## Git and Durability Requirements

- Produce standard, small, atomic, logically scoped commits.
- Follow the repository's established commit-message convention; if none exists, use clear imperative conventional-style subjects consistently.
- Inspect staged and unstaged diffs before every commit.
- Do not combine host discovery, bootstrap implementation, artifact manifests, lifecycle scripts, test harnesses, and evidence reports into one oversized commit.
- Push every completed atomic commit promptly to `https://github.com/copeugne/mcpack`.
- Never leave important work only in transient storage.
- Do not rewrite published history.
- Preserve user changes and unrelated work.
- Keep secrets and generated binaries out of Git.
- Store large evidence durably and commit its digest, manifest, location, and retrieval procedure.
- Keep the working tree clean at completed checkpoints.
- Record exact commit IDs used by every test run.

Suggested commit boundaries, adjusted to actual repository state:

1. Record host discovery and infrastructure requirements.
2. Add prerequisite doctor and bootstrap framework.
3. Add pinned Java provisioning and verification.
4. Add NeoForge acquisition and installation.
5. Add manifest-driven mod acquisition and side separation.
6. Add deterministic configuration and instance materialization.
7. Add server lifecycle and readiness controls.
8. Add deterministic test-world management.
9. Add automated smoke testing and diagnostics.
10. Add backup and verified restore testing.
11. Add test-client profile infrastructure.
12. Add profiling and evidence collection.
13. Add clean-room reproducibility validation.
14. Close documentation and infrastructure exit-gate evidence.

Do not create empty or artificial commits merely to match this list. Each commit must represent one coherent, validated change.

## Validation Matrix

Run and record at least these cases when technically possible:

| Case | Artifact set | World | Required result |
|---|---|---|---|
| Pristine platform | Zero gameplay mods | Fresh deterministic control | Boots, saves, stops, restarts |
| Candidate server | Server/shared candidates | Fresh deterministic test | Dependency and startup evidence |
| Wrong-side guard | Known client-only candidate | Disposable server | Rejected before live staging |
| Missing dependency | Controlled omitted dependency | Disposable server | Detected before or clearly at launch |
| Hash mismatch | Controlled altered fixture | None | Acquisition verification rejects it |
| Config drift | Controlled changed generated config | Existing test instance | Drift is reported |
| World reset guard | Preserved control target | Preserved world | Reset is refused |
| Backup/restore | Valid candidate instance | Persisted test marker | Restored copy boots with marker |
| Interrupted run | Disposable survey | Partial generation | Evidence preserved and run resumable |
| Clean-room rebuild | Resolved intended stack | Fresh deterministic test | Same resolved manifests and healthy boot |

Use safe fixtures for negative tests. Do not corrupt irreplaceable artifacts or preserved worlds.

## Definition of Done

This infrastructure assignment is complete only when all applicable statements are true:

- A clean Linux environment can be bootstrapped from committed instructions and scripts.
- Required host packages are detected, installed where authorized, and version-recorded.
- The exact pinned Java runtime is provisioned and invoked directly.
- The exact NeoForge server is acquired, verified, installed, and runtime-confirmed.
- Every enabled artifact is manifest-controlled and hash-verified.
- Server, client, shared, disabled, quarantined, and experimental artifacts are separated.
- The pristine baseline and experimental instances cannot overwrite one another.
- Configuration materialization is deterministic and drift-detectable.
- The EULA is materialized from the user's recorded acceptance.
- The server can start, reach verified readiness, execute a command, save, stop gracefully, restart, and preserve its world.
- Deterministic test worlds can be created and disposable ones reset safely.
- A backup has been created, restored elsewhere, booted, verified, and stopped.
- Test-client infrastructure exists for visual and human tests, or its environmental blocker is documented precisely.
- Profiling and evidence collection are operational.
- Failures preserve sufficient evidence for diagnosis.
- A clean-room rebuild has completed successfully, or a precise load-bearing blocker is recorded.
- Every claimed result points to raw evidence and a run manifest.
- Documentation contains no hidden prerequisites.
- All standard atomic commits have been pushed.
- The working tree is clean.

## Required Final Report

At completion, report:

1. Host and execution-environment facts
2. Installed packages and exact versions
3. Java and NeoForge provenance and hashes
4. Artifact acquisition and side-classification status
5. Implemented bootstrap and lifecycle commands
6. Smoke-test results
7. Backup and restore-test results
8. Clean-room reproducibility results
9. Test-client readiness
10. Profiling readiness
11. Evidence and log locations
12. Known limitations and unresolved blockers
13. Provisional decisions and their rationale
14. Exact commits and tags created
15. Confirmation that all work was pushed
16. A precise statement of which `SPECS.md` Items 2–10 infrastructure requirements are now satisfied and which remain incomplete

Continue autonomously until this definition of done is satisfied or a genuinely load-bearing blocker requires user input or additional authority. Do not stop after writing a plan. Implement and validate the infrastructure.
