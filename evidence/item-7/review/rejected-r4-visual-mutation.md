# Rejected Item 7 r4 visual review inputs

The first two attempts to review the corrected r4 capture tree are rejected as acceptance evidence. Both attempts inspected a writable shared directory, and reviewer contact-sheet commands changed capture files after `capture-manifest.tsv` was written.

The first integrity pass found eight overwritten Overworld top-down captures. A concurrent fidelity pass later found a different three-file mismatch set after the shared directory changed again. These contradictory counts prove that neither verdict bound one immutable input state. The capture manifest correctly exposed both mutations.

No mutated capture was accepted or published. The underlying galleries passed their source, identity, hash, provenance, axes, units, scale, legend, limitation, and vector-origin checks, but the capture layer remained rejected.

The accepted replacement was built in a separate restored core tree with the committed corrected analyzer, renderer, and capture tool. It was staged with the descriptor-bound staging implementation, archived, restored to an absent target, and made read-only before review. Two independent reviewers then inspected all 128 captures at that same restored path. Both returned `PASS`, all 128 manifest hashes and sizes matched, all captures were 1440 by 1200 sRGB PNGs, and a post-review 321-file hash recheck found no changed bytes.

Accepted visual receipts are `evidence/item-7/visual/integrity-review.json` and `evidence/item-7/visual/fidelity-review.json`. Their shared capture manifest SHA-256 is `219e17ed50b6e5b919c16a2b5bef34b7820b251c7272074d5df91c5123260f91`.
