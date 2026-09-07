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
