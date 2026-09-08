# BetterEnd r6: terrain tag unavailable to command lookup

The archived `minecraft-latest.log` records:

- Line 2649: the platform fill succeeds with 256 blocks.
- Line 2650: exactly one `item10-fixture-air-true` output, no false-air output.
- Lines 2651 and 2653: both tag commands reject with
  `Unknown block tag 'wover:surfaces/terrain'`.
- Line 2655: feature placement fails.

The terrain marker text in command-error excerpts is not a successful `say`
response. Neither membership branch executed. This is an unavailable-tag result,
not a negative membership test. The [trace](trace.jsonl) records the commanded
attempt at `[8,81,8]`, matching ground, false return and no template invocation.
The positive-placement gate fails. No density observation is accepted.

## Source derivation and unresolved scope

In retained worldweaver-21.0.24.jar, CommonBlockTags static initialization
(offsets 344 to 354) creates TERRAIN with path `surfaces/terrain` through
TagRegistryImpl.makeWorldWeaverTag. That method uses LibWoverTag.C, initialized
with `ModCore.create("wover-tag", "wover")`. ModCore's constructor assigns its
second argument to namespace (offset 38); mk uses that namespace. Thus the
command identifier is the packaged predicate's intended identifier.
BlockTagProvider.prepareBlockTags adds END_STONE to END_STONES (offset 48),
then adds END_STONES optionally to TERRAIN (offsets 342 to 367).
Reproduce this direct immutable-artifact inspection using the pinned `javap -p -c`
on those five classes with the retained WorldWeaver JAR as classpath.

Packaged intent and command lookup disagree. Before another fixture, inspect
WorldWeaver's block-predicate/tag integration to determine whether the tag is
also unavailable there or exposed through a separate runtime path. Do not patch
tags, change configuration, label all related families inactive or claim zero
natural density from this diagnostic. Full collection remains gated. Any conflict
with Item 3/7/8 acceptance must reopen only the affected claims and downstream
assumptions, without repeating their completed general audits.

Source `6e93f50f26645a927a3ed58aacafb0536dba6e42`; [receipt](diagnostic.json) records clean lifecycle
completion in 88.444 seconds. The subsequent
Python string-parenthesization correction changes no command bytes; Ruff and
changed-file type checks pass. The diagnostic remains bound to its launch revision.

## Verified custody

[Release](https://github.com/copeugne/mcpack/releases/tag/item-10-betterend-tags-2026-09-08-r6).
Archive 5278182 bytes, SHA-256 `dfabf29c12629f301349da667e05372b204ef6496c44d4e15442eb798f2bc47f`.
[Download restore](download-restore.json) verifies 254 raw files; downloaded
manifest matches byte for byte. [World restore](world-restore.json) matches all
97 paths, sizes and hashes in [world backup](world-backup.json), without boot.
Existing archive tools used root `evidence/raw/item10/betterend-tags-r6` and
revision `6e93f50f`. Restore the downloaded archive with [manifest](archive-manifest.json),
then its nested world archive with SHA-256 `92397d08a356a6a59c95bfddd5f6d2497abd879b9d770a16744f4aaa5f75081d`.
