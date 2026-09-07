# Item8 pre-PR preservation

Preserved implementation: e96cdc8b0587a93fbcb20e9d766773381f835249.
Published backup ref: refs/heads/codex/item8-preserved-e96cdc8b on origin,
verified by git ls-remote at that exact commit. Original branch and tags remain.
The user's history-consolidation authorization is recorded in the active handoff.
No history rewrite has occurred at this checkpoint.

Local backup directory outside the repository:
/home/lonestar/Desktop/Projects/mcpack-preservation-e96cdc8b.
This is same-disk preservation for recovery from ref/worktree changes, not an
off-device backup. Existing accepted raw archives remain on their GitHub releases;
this backup does not replace their hash manifests or tested restore receipts.
The full private workspace archive and all-ref bundle are not uploaded publicly.

| Artifact | Bytes | SHA-256 |
| --- | ---: | --- |
| history.bundle |74140500|35e5184524f4dba290db83f89dbc2f475fa854b95d9942a4ed626a537b7d8867|
| workspace-state.tar.gz |2132192096|1262c2851712c759634566494aa16b5a2e6e15d579b683a118e6ce8b69e58415|

The self-contained bundle contains108 refs, including tags, local branches and
worktree/ref recovery context. git bundle verify reports complete history. An
independent mirror clone restored the implementation ref exactly; git fsck --full
returned0 with no output. The bundle preserves objects even where mirror clone
ref layout differs from worktree-specific bundle heads.

Workspace archive includes AGENTS.md, .codegraph symlink, .omo, .debug-journal.md,
error.log, mcpack-reconstructed-28(1).bundle, evidence/raw, instances, and the
.codegraph target mcpack-c75967396b727ec8 from the user's codegraph directory.
It includes stopped worlds, failed attempts, configuration and logs. Regenerable
mods/libraries directories and JARs are excluded, as are dependency/interpreter
caches and downloads; pinned acquisition/materialization inputs remain in Git.
Originals are retained. No protected artifact was staged, deleted or rewritten.
Unstaged/staged binary patches,status.txt and refs.txt are also saved privately.

Whole archive byte/metadata comparison with originals returned0 and no differences,
as did the separate codegraph comparison. Personal state and the codegraph target
were extracted to restored-state; cmp verified AGENTS.md byte equality. The restored
symlink retains its original target; codegraph contents are separately present in
the extraction. No restored personal state was applied over the working copy.

## Commands and recovery

Commands run from the mcpack repository, using the exact backup directory above:

```sh
git push origin HEAD:refs/heads/codex/item8-preserved-e96cdc8b
git bundle create /home/lonestar/Desktop/Projects/mcpack-preservation-e96cdc8b/history.bundle --all
git bundle verify /home/lonestar/Desktop/Projects/mcpack-preservation-e96cdc8b/history.bundle
git clone --mirror /home/lonestar/Desktop/Projects/mcpack-preservation-e96cdc8b/history.bundle /home/lonestar/Desktop/Projects/mcpack-preservation-e96cdc8b/restored.git
git -C /home/lonestar/Desktop/Projects/mcpack-preservation-e96cdc8b/restored.git fsck --full
tar -I 'pigz -p 4 -6' -cf /home/lonestar/Desktop/Projects/mcpack-preservation-e96cdc8b/workspace-state.tar.gz --exclude='*/mods' --exclude='*/libraries' --exclude='*.jar' AGENTS.md .codegraph .omo .debug-journal.md error.log 'mcpack-reconstructed-28(1).bundle' evidence/raw instances -C /home/lonestar/.omo/codegraph/projects mcpack-c75967396b727ec8
tar -I pigz --compare -f /home/lonestar/Desktop/Projects/mcpack-preservation-e96cdc8b/workspace-state.tar.gz --exclude='mcpack-c75967396b727ec8'
tar -I pigz --compare -f /home/lonestar/Desktop/Projects/mcpack-preservation-e96cdc8b/workspace-state.tar.gz -C /home/lonestar/.omo/codegraph/projects mcpack-c75967396b727ec8
```

For recovery, verify SHA256SUMS, clone the bundle into a fresh destination, and
check out the preserved implementation ref. Extract workspace-state.tar.gz into
a separate empty directory; inspect before selectively restoring personal or raw
state. Restore the codegraph directory to its recorded target if needed. Use the
saved patches for tracked local edits rather than overwriting current work blindly.
Rematerialize excluded binaries/caches from pinned acquisition inputs. Existing
GitHub backup ref provides an independent source for the accepted implementation.

Remaining: coherent isolated PR history, final-tree equality (with provenance
documentation accounted separately), PR review loop and verified main delivery.

## Reviewed history consolidation plan

The61 exact ranges in history-consolidation-ranges.tsv combine adjacent source
selection, source capture and membership-test steps for one provider-disposition
outcome. Each range ends at its original accepted membership endpoint and contains
only chore/evidence/test increments; fixes and family assessment increments remain
separate. The reviewed ranges remove278 administrative commits. Other increments
are retained. This is bounded consolidation, not a new feature/evidence migration.

The committed tools/consolidate_item8_history.sh creates a new branch using the
original endpoint trees and verifies tree equality at every milestone and at the
final source head. It preserves original author metadata and records original
intervals; an old-to-new mapping retains every source commit reference. It refuses
an existing destination branch or changed main base. Originals, tags and backups
are untouched. It uses Git objects without a duplicate checkout because free disk
is limited. No accepted evidence, source identity or runtime behavior is rewritten.

Run with the committed source revision, a new codex/ branch and a fresh mapping
path outside ordinary Git, then deliver the mapping as provenance. History-only
changes with exact source-tree equality do not warrant repeating runtime captures
or unchanged tests. Final provenance additions must be identified separately.

## Completed isolated history preparation

Source head eab3ce95 (full source history retained on origin/codex/item-8-completion)
was reconstructed as52aa48f8c2acb4a2a51ef6cc7b850dac260ecc2c on codex/item8-final-pr.
Source1988 commits became1710 through61 reviewed ranges, removing278 administrative
commits. Every resulting milestone tree equals its preserved source endpoint;
final git diff --exit-code eab3ce95 codex/item8-final-pr returns0. Original tags and
refs remain unchanged. history-old-to-new.tsv maps all1988 source commits to their
resulting milestone, including folded intermediate commits. No content rewrite.

```sh
bash tools/consolidate_item8_history.sh eab3ce95 codex/item8-final-pr evidence/raw/item8/history-old-to-new.tsv
git diff --exit-code eab3ce95 52aa48f8c2acb4a2a51ef6cc7b850dac260ecc2c
```

The subsequent provenance commit adds only this completion record, the mapping
and the continuation checkpoint. It is accounted separately from the exact-tree
comparison. User AGENTS.md changes and protected untracked artifacts remain in
the working tree, unstaged. Remaining work is final PR review and main delivery.
