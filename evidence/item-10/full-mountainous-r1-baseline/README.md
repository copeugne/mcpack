# Mountainous repetition-1 baseline

Status: GENERATED, CONFIGURATION VERIFIED, RAW CUSTODY VERIFIED;
FULL OBSERVER ACCEPTANCE UNRESOLVED. Protocol: `item10-full-v1`.
Seed: `6671238423019257953`; generation source:
`ee0a82b8350221d4e434e3603aa455d5cc7b83aa`.

The unchanged [run receipt](run.json) records all eleven selections, readiness,
correlated save flush and clean stop with Java exit 0 after 611.564 seconds.
Compared with ordinary repetition-2 baseline, `run.preflight` differs only in
`seed` and `seed_role`; `probe` and lifecycle `selections` are equal. All 228
frozen files and eleven declared Chunky files pass capture. This does not prove
full occurrence coverage or the selected saved-chunk denominator.

## Raw custody

The stopped world backup contains 501 files totaling 436,845,509 bytes.
`world.tar.gz` is 172,652,056 bytes, SHA-256
`75ccb3e089119d5ebca970c83cecfeddbd5b37425c9f4acce41c62403046f1e1`.
The [world restore](world-restore.json) verified all 501 files into a new world.

The immutable [release](https://github.com/copeugne/mcpack/releases/tag/item10-full-mountainous-r1-baseline-ee0a82b8)
contains the outer archive and [manifest](archive-manifest.json). Its fetched tag
resolves to the generation source above. Archive size is 173,171,024 bytes,
SHA-256 `5106e752030685c31e5f5b28433b8bc40d6ff91909e8f95b7e2d6d2525aa0db8`;
312 files total 199,944,401 uncompressed bytes. [Local](local-restore.json) and
[downloaded](download-restore.json) restores verified all members; the downloaded
manifest matches byte-for-byte. No server restart was required for offline restore.

## Missing gateway capture

Comparing archive `files[].relative_path` sets against ordinary repetition-2
baseline finds exactly one absent raw member and no new member:
`trace.jsonl.classes/com/yungnickyoung/minecraft/betterendisland/world/feature/BetterEndGatewayFeature.class`.
There are 49 captured target classes. Calling the existing `collection_attempts`
with manifest-bound class/trace hashes and `require_complete_observer=True`
rejects with `collection does not bind the complete declared observer class set`.
The same iterator in diagnostic mode consumes 32,822 complete attempts and passes
its installation, hash, event pairing and healthy-shutdown checks. That diagnostic
pass does not waive the frozen 50-class requirement or establish zero gateways.
No full census was launched after this early rejection.

The frozen observer's `premain` registers a transformer whose `islandFeature`
predicate includes this exact class. It writes incoming bytes and an installation
event on targeted class definition; its exception path emits installation_failed.
The retained [provider source](../../item-8/sources/better-end-island-platform-gateway/README.md)
shows the custom gateway is invoked conditionally from a vanilla feature mixin.
An unexercised/lazily loaded class is therefore plausible, but full acceptance
requires resolving this distinction without silently weakening coverage or
hunting for a positive gateway in another world. The protocol and reader are
unchanged. Further experiments are paused at this coverage question.

## Reproduction

Use the existing [custody procedure](../full-ordinary-r1-without-sparse/README.md#reproduction)
with this run's name, revision, archive and world hash. Parents must exist and
outputs must be absent. Executed generation and archive commands:

```sh
uv run --no-sync python -m tools.run_item10_probe --name full-mountainous-r1-baseline --mode probe --preset item10 --role mountainous --arm baseline --repetition 1
uv run --no-sync python -m tools.archive_item7_evidence create --root evidence/raw/item10/full-mountainous-r1-baseline --archive evidence/raw/item10/item10-full-mountainous-r1-baseline-ee0a82b8.tar.gz --manifest evidence/item-10/full-mountainous-r1-baseline/archive-manifest.json --revision ee0a82b8350221d4e434e3603aa455d5cc7b83aa
```

The direct trace check derives class names by stripping `trace.jsonl.classes/`
and `.class` from manifest members, takes their SHA-256 values and the manifest's
trace SHA-256, and consumes `collection_attempts` completely with the ten protocol
dimensions. Run the complete-observer mode and diagnostic mode separately; do not
present the latter as acceptance. Existing Java fixture tests in
`tests/item10/test_placement_probe.py` and `probe-fixture/IslandFixture.java` are
available for a bounded investigation of the class-loading distinction.
