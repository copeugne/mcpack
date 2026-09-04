# mcpack Project Instructions

## Authority and startup

- Read `SPECS.md` before changing the repository. It is the chronological, dependency-ordered requirements authority.
- Treat `MCPACK-NEW-SESSION-HANDOFF.md` and `CLOUD_HANDOFF.md` as dated checkpoints. Preserve their recovery context, but verify all status claims against current Git history, committed evidence, reviews, and the latest item closure reports.
- Use `Adventure-Engineering-Pack-Execution-Ledger.md` for status vocabulary, evidence rules, decisions, unknowns, and blockers. Cross-check its item table against later commits because the ledger may lag delivered work.
- Before editing, fetch current refs and tags, then inspect the branch, upstream, working tree, staged and unstaged diffs, recent graph, and relevant path history.
- Preserve `.codegraph` and `mcpack-reconstructed-28(1).bundle`. Do not delete, stage, or commit them.
- Keep current branch names, commit IDs, pull request numbers, item status, active defects, and continuation instructions in handoff or ledger documents, not in this file.

## General engineering discipline

- Use `uv` for every Python command and dependency operation.
- Choose the simplest complete solution. Do not over-complicate or over-engineer.
- Do not add an abstraction, schema or validator, receipt, compatibility layer, generalized helper, fallback, or future-proofing unless the user or specification directly requires it, it fixes a reproduced defect, or it serves multiple current consumers.
- Prefer the smaller direct change in the existing path when it satisfies the current requirement.
- If implementation scope grows materially beyond the smallest expected change, pause and reassess the design before adding more machinery.
- Stop adding machinery once required behavior and proportionate validation pass.
- Reuse existing implementations and patterns. Do not create duplicate functions, classes, or variants.
- Do the actual required work. Do not substitute shortcuts, simplifications, or approximations.
- Do not fail silently or add unneeded speculative fallbacks. Errors and exceptions must be clear and descriptive.
- Apply critical thinking. Verify claims and challenge incorrect premises rather than agreeing mechanically.
- Quantitative claims require measurement or solid evidence. Do not invent or imply unsupported numbers.
- Do not use placeholder `pass` to conceal incomplete code. Fail explicitly with a clear exception and mark the implementation incomplete.
- Clarify material unknowns instead of inventing facts or silently assuming them.
- Make plans and implementation steps atomic, each with one independently verifiable outcome.
- Never use em dashes or en dashes in documentation, prose, or commit messages. Use punctuation such as a period, comma, colon, or parentheses instead.

## Product and design contract

- Build an engineering-driven multiplayer adventure sandbox.
- Engineering is the primary capability progression. Exploration gives engineering sustained purpose. Combat creates expedition pressure rather than replacing progression.
- Prefer horizontal capability expansion over levels, skill trees, stat inflation, damage sponges, spell progression, or a legendary-loot treadmill.
- Keep foundational Create, CC:Tweaked, transportation, trains, and Aeronautics capabilities normally obtainable rather than gated by rare dungeon RNG.
- Use a mostly grounded industrial presentation. Fantasy content beyond vanilla needs a specific gameplay justification. Player spell systems and wizard progression are excluded.
- Cooperative PvE is primary. PvP is optional and consensual. Protect players technically from unwanted griefing, theft, surveillance, and denial of service.
- Normal target concurrency is 2 to 6 players. Peak concurrency is 10 players.
- Adventure and Engineering v1 may start a fresh world. The launched v1 world is persistent afterward, with no scheduled resets.
- Preserve useful, distinct roles for walking, horses, boats, trains, and aircraft. Aircraft should improve long-range exploration without erasing adventure or train logistics.

## Earned sandbox freedom

- Allow powerful engineering solutions, breaching, mining, tunneling, flight, bombardment, automation, remote operation, extraction, industrialization, and reasonable sequence breaking when capability and effort are proportionate to the result.
- Do not protect authored routes with arbitrary blacklists, universal indestructible blocks, or invisible restrictions.
- If a loop is too cheap, rebalance its inputs, throughput, risk, setup, renewability, or upkeep instead of simply banning engineering.
- Bugs, duplication, corruption, crashes, desynchronization, permission escapes, and disproportionate shared-server harm are not earned capabilities and may be constrained or fixed.

## Frozen technical identities

- Minecraft: Java Edition 1.21.1.
- Loader: NeoForge 21.1.249.
- Java: Eclipse Adoptium Temurin 21.0.12.1+1-LTS.
- Construction heap: `-Xms1G -Xmx4G`. This is not a final production allocation.
- Retained dedicated-server candidate manifest: `evidence/item-3/runtime/retained-server-candidates.txt`.
- Retained candidate count: exactly 136.
- Retained manifest SHA-256: `78e5bdc0697299782a535400ad5b313c088e8db10cfe075085ae4c8a531e30cb`.
- Pinned Temurin archive SHA-256: `ce79869e1307ed8ee1e2baa86a412b1eb5b75d10a01006d788a6f968bcfaee94`.
- Deterministic seed suite: ordinary `42`, mountainous `6671238423019257953`, ocean-heavy `95920844204830198`, biome-diverse `-3503646078644842058`.
- Do not silently re-enable Sable, bundled Aeronautics, Every Compat, the rejected Spell Engine family, Simply More, or Simply Tooltips. Reopen Item 3 and every affected downstream gate if new evidence contradicts the retained set.

## Evidence and completion rules

- Do not infer completion from a commit subject, report prose, filename, reconstructed summary, successful launch, or green tests alone.
- Reconstructed history and `evidence/reconstruction/` are context and scaffolding, not primary empirical acceptance evidence.
- Unknown values remain `UNKNOWN` until resolved by a user decision, artifact inspection, authoritative source, controlled experiment, reproducible measurement, or documented derivation from verified facts.
- An item is complete only when every input and subitem is resolved, raw evidence is retained and linked, the exit gate explicitly passes, failures have dispositions, downstream assumptions are updated, exact identities and protocol versions are recorded, and evidence is durably delivered.
- Preserve failed attempts, rejected pilots, uncertainty, and limitations. Never rewrite raw evidence to make it pass.
- Machine-readable and narrative outputs must agree exactly. Validators must bind claims to preserved artifacts and fail on omissions, unexplained files, escaped paths, changed hashes, unknown fields, or identity mismatches.
- A server reaching readiness proves only that lifecycle point. It does not prove gameplay, compatibility, persistence, performance, or scientific reproducibility.

## Dependency and experiment discipline

- Work chronologically and dependency-first. Do not proceed when an explicit dependency or decision gate has failed.
- Do not tune before Item 6 freezes and validates untouched generated defaults.
- Use fresh, hash-verified materialization for each controlled experiment. Do not reuse proof worlds or silently mutated configuration trees.
- Item 7 must inspect actual clean worlds for all four seeds under the exact frozen Item 6 identity. Item 4 and Item 5 boot logs are not Item 7 evidence.
- Item 8 must use verified runtime registries, packaged data, configuration evidence, logs, and generated-world observations. Do not double-count aliases, pieces, pools, or templates as families.
- Item 9 must classify every verified canonical family exactly once with rationale, evidence, confidence, and ambiguity.
- Item 10 must preserve predeclared sampling, raw observations, denominators, failures, censoring, uncertainty, and deterministic processing. Static density is not observed exploration pacing.
- After Item 10, audit Items 2 through 10 together for identity and narrative consistency. Reopen affected upstream and downstream gates when evidence conflicts.
- Do not implement, run, repair, or lint Item 11-specific workflows until Items 2 through 10 pass the cross-item audit. Item 11 requires real-client evidence from at least two blind human operators and cannot be replaced by bots or headless scans.

## Runtime and operational safety

- Preserve lifecycle boundaries: wait for readiness, request `save-all flush`, wait for the matching save confirmation, request stop, require a clean exit, and kill the complete process group on timeout or post-launch I/O failure.
- Keep the Java-compatible POSIX record-lock implementation for world archives. BSD `flock` does not contend with Java `FileChannel` locks and is not a valid substitute.
- Exclude `session.lock` from stopped-world archives.
- Never claim a systemd timer is active without direct `systemctl` evidence.
- Operational proxies, trust stores, credentials, and local caches are temporary inputs and must not be committed.

## Git and durability

- GitHub `copeugne/mcpack` is canonical. Use `origin/main` as the delivery authority, not the aggregate `work` branch.
- Preserve atomic commits and valid history. Do not squash, rewrite, or move existing recovery tags.
- An atomic commit must be small, narrowly contained, independently understandable, independently verifiable, and easy to review.
- One commit must implement one behavior, fix, or evidence increment, together with its direct tests.
- A broad item label does not make a large mixed change or a massive change atomic.
- Split code, tests, generated or machine evidence, documentation, and review fixes into the smallest independently green and revertible increments wherever technically possible.
- Before every commit, inspect the staged diff and reject it if a reviewer cannot validate it as one compact unit.
- Isolate any irreducible large generated or evidence migration in its own commit, with a clear reason, the generation and verification command, and no unrelated changes.
- Never batch several completed steps into a late omnibus commit. Make commits continuously after each verified increment.
- When a task includes delivery, validate each atomic increment, push it through the authorized workflow, and verify the delivered ref before starting dependent work.
- Keep review fixes separate from substantive item milestones.
- When an item satisfies its local exit gate and appears ready for completion, push its branch and open a pull request targeting `main`. Do not mark the item complete merely because the pull request exists.
- Request a Codex review on the pull request with `@codex review` and wait for that review cycle to finish. An eyes reaction means the review is still in progress and is not approval.
- After each completed review, inspect the review result, inline comments, and discussion comments. Assess every finding for technical validity and relevance to the item rather than accepting or dismissing it mechanically.
- Fix every valid and relevant finding, validate the fixes, commit them separately from the substantive item milestone where practical, and push them to the same pull request.
- After pushing review fixes, request a fresh review with `@codex review`. Repeat the wait, inspection, triage, fix, validation, push, and review cycle until Codex returns a thumbs-up reaction and no valid, relevant, unresolved findings remain.
- Treat a thumbs-up reaction as the Codex review bot's clean result only after confirming that the corresponding review cycle has completed and introduced no comments. Do not infer approval from the absence of immediate comments, from an eyes reaction, or from an earlier review superseded by later commits.
- An item reaches completion only after its exit gate passes, its evidence is durably delivered, the pull request review loop is clean, and the accepted pull request is merged into `main` with the delivered ref verified.
- Do not commit candidate JARs, Minecraft or NeoForge binaries, worlds, secrets, tokens, addresses, allowlists, player UUIDs, proxy trust stores, downloaded toolchains, or operational caches.
- Store large raw evidence outside ordinary Git. Give it an immutable archive name, SHA-256 manifest, recorded size and file count, matching commit or tag, durable redundant storage where practical, and a tested restore.
- Stop downstream work if commits or evidence cannot be delivered durably.

## Prohibited shortcuts

- Do not install all 190 candidates as the baseline or treat the tentative filename pool as the target manifest.
- Do not treat filenames, Forge labels, Fabric metadata, broad `1.21.x` labels, or startup success as compatibility proof.
- Do not choose final structure mods before baseline root-cause analysis.
- Do not solve poor cadence by making giant structures common.
- Do not add AI stacks before testing encounter composition with existing AI, and do not stack redundant AI or difficulty systems.
- Do not use raw health or damage inflation as the default difficulty lever.
- Do not assume per-player loot resets physical dungeons or that reward multiplication is harmless.
- Do not fabricate missing logs, hashes, worlds, samples, measurements, citations, or validation results.
- Do not store authoritative work only in transient scratch space.
