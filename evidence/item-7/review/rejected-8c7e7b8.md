# Item 7 rejected exact-SHA security review

Reviewed revision: `8c7e7b8bb5db79d826b78cab5a678605a8b5fc23`

Verdict: `REJECTED`

The goal, code-quality, context, hands-on QA, and runtime-debugging lanes passed this revision. The security lane found six valid delivery blockers, so the aggregate review failed:

1. World staging locked one directory identity but later reopened the world by pathname. Replacing that pathname after lock acquisition allowed attacker-controlled bytes to enter the stage.
2. Core staging validated the raw root and later reopened it through `shutil.copytree`. Replacing the root between those operations allowed attacker-controlled bytes to enter the stage.
3. Archive creation returned a temporary pathname, then reopened it for validation and publication. Replacing the output parent and temporary pathname could substitute an attacker archive.
4. Hardlinked source files were accepted. Mutation through a second link could change bytes during staging or archive construction.
5. Non-regular files were not handled as one fail-closed boundary. A FIFO could leave a partial core stage or cause a required world file to be silently omitted.
6. The release verifier resolved the tag from local `origin` while selecting the release from the caller-provided repository. A tag from one repository could therefore authorize release assets from another.

Disposition:

- Focused tests reproduced every finding before production changes.
- `fdd99d9` retains descriptor-bound source and output identities, holds the Java-compatible POSIX world lock on the pinned world, rejects hardlinks and special files, copies into unpublished temporary trees, and publishes archive outputs only through pinned directory descriptors.
- `c625d6e` resolves the tag and annotated-tag target through the GitHub API for the same explicit repository used to inspect and download the release.
- The focused regression surface passes with 30 tests. The complete Item 7 suite passes with 162 tests.
- The changed Python and shell surfaces pass Ruff formatting, Ruff checks, basedpyright, and shell syntax validation.
- The corrected verifier downloaded and verified all four real r2 assets at source revision `b13344e8eaa39528b61643bf24534d709cfff131`.

This rejected revision is not approval. The corrected candidate requires fresh exact-SHA review coverage and the complete GitHub review and merge gate.
