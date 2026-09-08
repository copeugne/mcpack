# Extras fixed-frame diagnostic r1

The [predeclared diagnostic](../protocol.md#extras-r1-bounded-natural-diagnostic)
ran at `6edb9ab5aedea384b9bffbe61a0ee66a74b6b24e` with fresh hash-verified frozen
runtime/configuration. The [run record](diagnostic.json) records all four
81-chunk selections, correlated save and clean exit 0 in 89.041 seconds, without
a process-group kill. The instance is stopped and preserved.

## Result and limits

[Archive-bound trace validation](trace-validation.json) passes. All fifteen Extras
and fourteen bridge hooks are in the required incoming-class set. No Extras or
bridge attempt occurred, so positive capture remains UNMET. There is no saved
Extras block corroboration and no accepted Extras density. Do not expand this
frame to hunt for a positive result. The mixed trace has 1,289 attempts and 543
writes, with zero unfinished attempts. These are raw observations, including halo
activity, not selected-area occurrence counts. Incoming identities and all event
relationships are checked by the existing reader. It rejects unexpected Extras
or bridge events for this bounded zero-attempt diagnostic. No Item 11 work ran.

## Raw custody and reproduction

[Archive manifest](archive-manifest.json): 295 files,
7,874,218 uncompressed bytes. Immutable archive
`item10-extras-pilot-r1-6edb9ab5.tar.gz`: 5,670,934 bytes,
SHA-256 `f982e883c5a04ed4d1e9a4f10aba5f9b60a31ad264684a8143536fb37ce6b536`.
The [release](https://github.com/copeugne/mcpack/releases/tag/item-10-extras-pilot-2026-09-08-r1)
contains the archive and manifest. The fetched tag matches the exact source
commit. The downloaded manifest is byte-identical; [raw restore](download-restore.json)
verified all members. Trace SHA-256 is `bbbfebc8993b97775079fcaea90215e8a84c5d5a6b844e6de08f3a976755eb14`.

[World backup](world-backup.json): 103 files, archive
5,380,492 bytes, SHA-256 `c2a016f91510c3fdb9b3510ee0a1053e96301b845573164e4e3d2f9bf15e1428`.
[World restore](world-restore.json) passed. Every sorted restored filepath, size
and SHA-256 matched the backup world_files list without booting. session.lock is
excluded. Local custody is `evidence/raw/item10/extras-pilot-r1-custody`.
Reproduce into absent destinations using the executed commands with placeholders:

```sh
gh release download item-10-extras-pilot-2026-09-08-r1 --dir DOWNLOAD
uv run --no-sync python -m tools.archive_item7_evidence restore --archive DOWNLOAD/item10-extras-pilot-r1-6edb9ab5.tar.gz --manifest evidence/item-10/extras-pilot-r1/archive-manifest.json --target RESTORED_RAW --receipt RESTORE_RECEIPT.json
uv run --no-sync python -m tools.manage_item4_environment restore --archive RESTORED_RAW/world.tar.gz --sha256 c2a016f91510c3fdb9b3510ee0a1053e96301b845573164e4e3d2f9bf15e1428 --target RESTORED_WORLD
uv run --no-sync python -m tools.validate_item10_trace --extras-r1 RESTORED_RAW
```

The reader extension reuses the bridge mixed-trace path with the exact additional
Extras installation set. All 69 retained-trace tests pass, including the actual
archive, missing hooks, unexpected feature events, missing attempts, malformed
writes, unhealthy shutdown and changed class bytes. External raw absence is an
explicit prerequisite skip. Focused Ruff and basedpyright pass. All seven prior
feature trace reports reproduce unchanged. Collector preservation tests and
retained-class transformations are recorded in the
[probe report](../placement-probe.md#extras-template-and-processor-preparation).
This diagnostic does not close Item 10 or prove natural Extras placement.
The full Item 7/10 gate passes all 404 tests in 94.53 seconds.

PR33's subsequent finding `3955590865` identifies exceptional-exit cleanup missing
from the shared feature observer. This successful diagnostic contains no such
exception, but its synthetic tests did not cover a caught exception followed by
another placement on the same thread. Fix that shared behavior before further
experiments; passing existing tests does not resolve the finding. Raw custody and
this zero-attempt trace result are unchanged.

The shared exceptional-exit fix from PR33 now applies to all eleven Extras
feature entrypoints. Extras recovery fixtures cover caught template and processor
exceptions followed by another placement on the same thread, including original
processor exception object identity. All 22 affected bridge/Extras tests and
focused Ruff/basedpyright checks pass. This resolves the demonstrated observer
state leak in the Extras branch without changing this diagnostic's raw evidence.
The final Extras branch gate, including the integrated exception fix, passes all
408 Item 7/10 tests in 99.62 seconds. PR review and main delivery remain required.

## Reviewed main delivery

[PR34](https://github.com/copeugne/mcpack/pull/34) delivered reviewed head
`cba277cbc65885867ce91344447733420103ac07`. The cycle requested by
[5581561706](https://github.com/copeugne/mcpack/pull/34#issuecomment-5581561706)
completed at `2026-09-08T08:15:48.843560Z`, as recorded in the
[review summary](https://github.com/copeugne/mcpack/pull/34#issuecomment-5581564874).
The [clean result](https://github.com/copeugne/mcpack/pull/34#issuecomment-5581638645)
identifies that head. Inspection found no inline or review findings and verified
the Codex connector bot's thumbs-up reaction on the pull request.

The accepted head merged as `0c98eeecfaf2cf6ffd6bd7671783f9d76530f893`.
Fetched `origin/main` equals that merge and contains the reviewed head, verified
with `git merge-base --is-ancestor`. This closes the review/delivery prerequisite
above for this bounded diagnostic only. Full Item 10 collection remains incomplete.
