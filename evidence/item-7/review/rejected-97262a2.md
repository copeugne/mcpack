# Item 7 rejected exact-SHA review

Reviewed revision: `97262a21b0b76c253f57e32b8665e48d0a63f822`

Verdict: `REJECTED`

This review is preserved because a passing local completion receipt did not establish delivery readiness. The review found the following valid blockers:

1. Fresh-clone tests depended on ignored candidate JARs, including Chunky, so the documented focused test suite was not self-contained.
2. Archive creation and restore validated paths before reopening them, allowing a path-swap race between validation, hashing, archiving, or restoration.
3. Raw-world staging did not hold a Java-compatible POSIX record lock on `session.lock` and used hardlinks, so the staged bytes were neither isolated from source mutation nor proven to come from a stopped world.
4. Provider evidence models silently ignored unknown fields instead of rejecting schema drift.
5. `src/mcpack_evidence/item7_nbt.py` and `tests/item7/test_item7_archive.py` exceeded the project 250 pure-line limit.
6. The documented Ruff and basedpyright commands included unrelated reconstructed later-item code and could not substantiate an Item 7 quality claim.

The runtime audit on the same revision passed the completion CLI, lifecycle-receipt, tamper-rejection, and process-cleanup surfaces, but explicitly reported that the full Item 7 suite failed in a clean detached worktree because the ignored JAR prerequisites were absent. That limitation confirms blocker 1 rather than overriding it.

Disposition:

- `9d1ff11` made runtime fixtures self-contained.
- `9a352eb` rejected unknown provider-evidence fields.
- `6160db3` pinned symlink-free file descriptors through archive hashing, writing, and restoration.
- `c63e5ac` added Java-compatible world locks and independent-copy staging.
- `df6e511` split the oversized decoder and archive test fixtures.
- `a88d057` scoped the documented quality gate to Item 7.
- `b13344e` removed the remaining provider-cache dependency from clean tests.
- `1dc67fe` bound versioned release evidence paths.
- `4e6b440` published corrected r2 manifests, restores, publication identity, and completion evidence.

The rejected revision is not approval. A fresh review must bind the full final candidate SHA.
