# Item 7 security and evidence-integrity review at c7babd9

## Identity and verdict

- Reviewed revision: `c7babd9596594bab4f151a50cdc2ccb180c7aa18`.
- Verdict: `PASS`.
- Confidence: `HIGH`.
- Blocking findings: none.

## Adversarial verification

- 35 focused source-binding, archive, restore, publication, and release tests passed.
- All 188 Item 7 tests passed.
- A fresh inventory rebuild from the restored r9 Run A, Run B, and auxiliary trees returned `PASS`, bound 716 files, compared byte-identical to the committed inventory, and matched SHA-256 `e417d77272151a91153a94df993da058f174fb568be75a1e61e49916dbc1e994`.
- A fresh completion rebuild from the restored r9 core returned `PASS`, bound 137 unique artifacts, compared byte-identical to the committed receipt, and matched SHA-256 `76603b037d38534f56a4a2625666032b60929d7efe74c0a434b73310858c4c69`.
- Restored file counts matched every manifest: core 4,618, Run A 249, Run B 250, auxiliary 217. No symlink or `session.lock` was present.
- Every manifest path was sorted, unique, contained, and bound to source revision `fb901b1050f211cb88fe1fb9d074f5d7c1e17407`.
- The local and remote annotated tag object `f4a573dd5263caef541f4e0ff622469a356bd2b8` resolved to that source revision.
- The public r9 release was neither draft nor prerelease and exposed exactly the four assets recorded in `publication.json`, with matching names and sizes.

The accepted completion does not rely on `.omo`, session transcripts, or an untracked authoritative producer. The recorded GitHub and merge steps remain delivery gates rather than local acceptance evidence.
