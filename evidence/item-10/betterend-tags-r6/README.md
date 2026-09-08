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


## Tag-loader path inspection

The [source identities](source-identities.json) bind the following direct
inspection to the accepted Item 8 WorldWeaver archive SHA-256. Inspect each
listed class with the pinned JDK command, using dotted class names:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap -p -c -classpath downloads/item3/candidates/worldweaver-21.0.24.jar org.betterx.wover.tag.impl.TagManagerImpl
```

TagLoaderMixin.wover_modifyTags delegates its directory and ordinary tag-entry
map to TagManagerImpl.didLoadTagMap (offsets 172 to 180). That method looks up
the registry by directory (offsets 0 to 14), emits its bootstrap event, and adds
entries to the same map (offsets 17 to 30). The helper creates ordinary Minecraft
TagLoader.EntryWithSource records. The inspected path is normal tag loading,
not a separate block-predicate membership database.

The block registry's directory comes from Registries.tagsDirPath through
TagRegistryImpl.WithRegistry's constructor (offset 13). The raw log confirms
`tags/block` at line 1621. This refutes an unsupported assumption of a hardcoded
plural `tags/blocks` directory mismatch in these packaged constructors.
The prebuild log at line 1622 is before injection and is not final tag evidence.
The post-readiness command failure is the stronger observed result.

TagRegistryImpl.emitLoadEvent creates its context and emits BOOTSTRAP_EVENT
outside datagen (offsets 0 to 25). LibWoverTag registers three auto-provider
factories (offsets 29 to 50); WoverDataGenEntryPointImpl.registerAutoProvider
only appends a factory to AUTO_PROVIDERS. WoverTagProvider's four-argument
constructor merely stores its inputs (offsets 0 to 25). None of these inspected
operations itself subscribes BlockTagProvider.prepareBlockTags to the runtime
event. Consequently the existence of that datagen method cannot establish
runtime terrain availability. The exact missing registration/resource cause
remains unresolved; this inspection does not claim to exclude all callers.

The affected open claim is whether BetterEnd's building-list locations are
actually placeable under the frozen baseline, not whether their configured
feature IDs exist. Item 8 registry activation evidence and Item 9 provisional
classification remain reusable; neither proves the unmet terrain predicate.
Full Item 10 occurrence acceptance remains gated on resolving that distinction.
No upstream JAR, configuration, inventory or classification has been changed.

## Resolved provider registration boundary

The retained LibWoverTag constructor's invokedynamic at offset 19 is bound, in
its BootstrapMethods entry 0, to WoverDataGenEntryPoint.onGatherData with a
NeoForge GatherDataEvent parameter. Reproduce with the pinned javap command
above using `-p -v` and class `org.betterx.wover.entrypoint.LibWoverTag`.
It is a data-generation listener, not a runtime tag-bootstrap subscriber.

The newly listed classes in source-identities.json complete this specific path:
WoverDataGenEntryPoint.onGatherData calls initialize at offset 28; initialize
calls addDefaultGlobalProviders at 64 and onInitializeProviders at 72.
WoverDataGenEntryPointImpl.addDefaultGlobalProviders creates the registered
providers and passes them to PackBuilderImpl.instantiateAutoProvider. That
method stores providers and redirectors; AutoBlockTagProvider.redirect stores
matching tag providers, and its prepareTags lambda invokes their prepareTags
method at offset 47. Thus redirect machinery does not supply evidence of a
separate runtime call to the missing terrain provider.

This resolves the previously unidentified listener type. It does not prove that
no other mod supplies the tag or that every natural building attempt fails.
The next unresolved question is runtime population through other subscribers
or loaded resources, rather than whether this datagen registration suffices.
No server was run and no frozen input was changed for this inspection.
