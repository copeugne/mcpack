# Item 7 r10 custody rejection

## Identity

- Tag: `item-7-raw-evidence-2026-09-04-r10`.
- Annotated tag object: `ff09be3ecf7e5449c5574878cb65ce8d47e62747`.
- Source revision: `264429400f83e6062bae7a430d62e7090c987b7e`.
- Release: `https://github.com/copeugne/mcpack/releases/tag/item-7-raw-evidence-2026-09-04-r10`.

The four release assets were rebuilt from a fresh verified r9 restoration, restored again successfully, and verified through two independent remote downloads. All 5,334 files and all archive byte identities match the retained r9 payload. The raw evidence is valid.

## Rejection reason

Revision `b924b9a` subsequently made the machine-readable retained save-sequence audit a required, source-rebuilt completion artifact. The immutable r10 tag predates that final completion producer. Therefore r10 cannot be the accepted source-custody boundary even though its raw payload and remote publication are valid.

The r10 tag and release remain immutable failed-attempt evidence. They must not be moved, rewritten, or described as the accepted Item 7 release. A later custody revision must point to source that contains `b924b9a` and must regenerate completion with the required save audit.
