# Item 8 evidence plan

Status: IN PROGRESS. No family count or completion claim is accepted yet.

The infrastructure requirements in
`INFRASTRUCTURE-INSTALLATION-AND-SERVER-TESTING.md` apply to this work. Reuse the
existing host-discovery and platform doctor, pinned acquisition/materialization,
configuration capture, and lifecycle primitives. Record each new run's source
revision. Invoke pinned Java directly, check port availability, preserve full
logs and failures, and keep operational inputs out of committed evidence.

## Required proof and boundaries

The complete inventory covers every gameplay-relevant structure family in the
retained 136-JAR stack, including every provider named in SPECS.md Item 8 and
vanilla content. Runtime structure IDs are variants, not automatically families.
Canonical grouping must cite a shared gameplay identity and preserve all member
IDs. Pools, pieces, templates, aliases, replacement structures, injected village
buildings, and feature-based structures receive explicit relationships and are
not silently omitted or counted as independent structures.

Every family must record dimension, biome constraints, approximate footprint and
vertical size, intended hostility, mob source, loot source, generated spawners,
authored versus natural enemies, visual discoverability, and surface/underground
classification. Each claim cites its source and distinguishes observed values,
packaged intent, derivation, and unresolved limitations. Registration does not
prove placement, template size does not prove assembled footprint, and a missing
observation does not prove absence.

## Smallest evidence set

1. One fresh ordinary-seed runtime under the frozen Item 6 configuration, using
   the existing retained-136 materializer and NeoForge's built-in registry dump
   command. Capture structures, structure sets, template pools, configured and
   placed features, biomes, and dimension types. Preserve command responses,
   runtime identities, configuration parity, correlated flush, and clean stop.
2. A deterministic extraction from all hash-verified retained JARs and pinned
   vanilla/NeoForge data. Preserve resource ownership, competing definitions,
   placement and pool relationships, relevant template NBT, loot references,
   spawners, and authored entities. Resolve effective availability against the
   runtime dumps and configuration, not ZIP traversal order.
3. Reuse accepted Item 7 generated-world observations under their existing r14
   identities. Bind derived family observations to those retained sources.
   Collect additional targeted evidence only for a specific unresolved required
   attribute or provider; do not rerun the Item 7 survey or claim density.
4. One canonical machine inventory, its source-bound verification, and a matching
   narrative report. Preserve exact provider and family coverage, unresolved
   cases, failures, and differences from the obsolete zero-mod report.

## Frozen dependencies

- Minecraft 1.21.1, NeoForge 21.1.249, Temurin 21.0.12.1+1-LTS.
- Retained manifest: `evidence/item-3/runtime/retained-server-candidates.txt`,
  SHA-256 `78e5bdc0697299782a535400ad5b313c088e8db10cfe075085ae4c8a531e30cb`.
- Item 6 manifest: `evidence/item-6/generated-config-manifest.json`,
  SHA-256 `2e0aaeb0f84747a3cb17146eb435d34cc7d6703b9372211e8fc8cff2df2b436f`.
- Item 6 audit: `evidence/item-6/config-audit.json`,
  SHA-256 `181e0c299f44ded319d93c84f7b983738364b4090286251b00421fa041b989dd`.
- Item 7 completion: `evidence/item-7/completion.json`,
  SHA-256 `0ef7c83438ab2a2cfe67eadc858e806ada9c9eecc213d883649ae3e8493cb1d3`.
- Item 7 raw release: `item-7-raw-evidence-2026-09-04-r14`.

Preserve Item 7 nondeterminism, Better Caves failure, IDAS missing biome tags,
unresolved YUNG Bridges/Extras identities, and unresolved diagnostics. No tuning,
candidate readmission, tier assignment, or Item 9 through 11 execution is allowed.

## Validation and delivery

Validate required fields and exact coverage against the actual source universe,
all referenced identities, canonical grouping, and deterministic output. Focused
tests must exercise omissions, double counting, conflicting sources, and the
runtime lifecycle boundaries actually used. Inspect the human-facing inventory
for meaningful source-supported descriptions. Run affected quality checks once
the increment passes. Commit and push independently verifiable increments.

Open the Item 8 PR promptly when the local specification gate passes. Request
`@codex review`, inspect the completed cycle and all findings, fix valid findings
in separate commits, and request review again after fixes. Verify a completed
clean review covering the final changes and the required thumbs-up reaction.
Merge without squashing and verify the accepted head in fetched `origin/main`.
The Item 7 user exception does not waive any Item 8 review or evidence gate.
