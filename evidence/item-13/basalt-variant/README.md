# Missing Basalt central netherite outcome

Status: PREDECLARED, not yet a runtime result. Item 13 only.

The [family report](../fixed-blocks/basalt-chambers-report.md) exhausts two
untouched-baseline assemblies and all six accepted omit-Sparse central components.
Seven centers are debris and one is lodestone. Existing Item 7/8 evidence provides
no additional occurrence. The sole missing central material is netherite block.

Smallest experiment: one forced placement of the existing7x7x7
`adorabuild_structures:basalt_chambers/ancient_debris` component with registered
`adorabuild_structures:randomize_ancient_debris`, NONE rotation/mirror, placement
flags2 and random seed42. Do not place a whole assembly or regenerate a survey.
This tests the material outcome and saved authored cells, not natural occurrence,
assembly frequencies, external access, route play, combat or acquired loot.
The exact source template/processor hashes are already in the family report.

Reuse the temple diagnostic's coordinate predictor and capture path. Add only the
specific single-component mode, leaving the four-case temple mode available with
its existing defaults. The missing outcome justifies a third supported template,
its7-block height/centerY+3 and registered processor choice; it does not justify a
new runtime framework. Select the first netherite prediction in the existing
256-origin grid(32*(i%16),160,32*(i/16)),i=0..255. Cross-check the predictor against
all eight retained natural/control center outcomes before selecting. Prediction
is source-derived, not observed. No rerolls after a failed runtime prediction.

Fresh experiment materialization: reuse the accepted ordinary r1 baseline world
through copy_temple_source, with full source pre/post and copied inventory hashes
under the existing POSIX locks. Use frozen136-JAR/Item6 configuration, pinned
Temurin/NeoForge and1G/4G heap. Each retry requires unique instance/output paths.
Never mutate either baseline restore or a previous experiment. Require readiness,
the existing processed-console barrier, asynchronous chunk preparation off-thread,
actual placement readback, correlated save-all flush, clean stop and unchanged
frozen configuration. Keep existing600/120 lifecycle,45-second attach and30-second
case bounds. A failure is retained, not reinterpreted as material coverage.

Readback covers the7-cube plus3 padding:13^3=2,197 cells. Before placing, require
all343 target cells air. Retain the actual central state and every padded cell.
After clean shutdown, archive and hash-verify a fresh stopped-world restore, then
compare all2,197 cells to immediate readback before accepting the outcome. Jigsaw
blocks may remain in this direct component diagnostic; do not treat them as an
assembled playable dungeon or infer connections. Material comparison uses the
source-authored non-jigsaw/non-structure_void mask, as in the control comparison.

Budget:2 GiB disposable instance,20 MiB raw capture,3 GiB total custody tree and
5 GiB free floor. The last successful four-case temple capture took140.95 seconds
and about1.10 GB instance storage. This one-case capture has fewer readback cells,
but retains the same startup cost; no faster runtime is assumed. Preserve failed
attempts. Raw durability uses the existing manifest, immutable release, download
and restore procedure, not a new evidence format.

Definition of done for this gap: predicted netherite verified in live placement
and stopped restored blocks; full padded readback equality; frozen identity and
clean lifecycle; retained raw/custody; source-supported tool/drop differences and
conditional family-model integration. This does not close other Item13 families
or waive final PR review, clean thumbs-up, merge and fetched-main verification.

## Selected diagnostic and producer verification

The source predictor agrees with all eight retained centers. Its first qualifying
grid index7 selects origin(224,160,0), center(227,163,3). Retained
[selection.json](selection.json) SHA-256 is
`d05f481ee6b03efc5fc869da634a210e68b20d26f8dd6b63e07c689848e81e2f`.
The original no-argument selector reproduces the four-temple selection byte for
byte. Compilation with the capture runner's explicit classpath and pinned javac
passes -Xlint:all -Werror. An initial manual compilation without that explicit
classpath failed on the host's invalid inherited classpath; no server was launched
and the actual runner already supplies its own classpath. Python runner lint/types
pass. No source-selector prediction is claimed as runtime evidence.

Reproduce selection and use the existing material probe:

```sh
downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/java evidence/item-13/temple-variants/SelectOrigins.java --basalt > /tmp/item13-basalt-selection.json
cmp evidence/item-13/basalt-variant/selection.json /tmp/item13-basalt-selection.json
uv run python -m evidence.item-13.collision.run --basalt-variant evidence/raw/item13/basalt-variant-r1 instances/item13-basalt-variant-r1
```

The runtime command requires a clean committed producer and absent output/instance
paths. Its inherited projection filename is temple-variants.json; the actual
case root, processor and material identify the Basalt diagnostic unambiguously.

Focused prelaunch lifecycle gate:23 tests pass in3.18 seconds, including the
processed-console barrier and failure/clean-stop behavior. No lifecycle code was
changed for this mode. Retain final producer identity in the capture before
relying on runtime output.

## r1 runtime result

Producer `19cd4a08ba0f5ea9044f42d492118c0d3dad4dfe` is pushed. The
[capture](r1-capture.json.gz) passes readiness, processed-console barrier,
correlated flush, clean exit0 and frozen identity/configuration in149.765 seconds.
The [projection](r1-temple-variants.json.gz) has one successful placement with
netherite at(227,163,3) and all2,197 padded cells; placement/readback took1.202879s.
Uncompressed projection SHA-256 is
`2dc771f684e577cd1a288a958768dd887be03354b79dfc29c04d9a1c889a47b2`.
No retry was needed. The [retention record](r1-retention.json) binds all five core
raw files and the explicit console bind-endpoint redaction; full originals remain
under evidence/raw/item13/basalt-variant-r1/. No runtime remains active.

Instance size is1,103,556,604 bytes across1103 files; raw capture is5,836,998 bytes
across240 files. Both declared limits pass. The stopped backup/restore and full
saved-cell comparison remain required before accepting the material/model gap.

```sh
uv run python -m evidence.item-13.collision.retain --basalt-attempt 1
uv run python -m tools.manage_item4_environment backup --world instances/item13-basalt-variant-r1/world --archive evidence/raw/item13/basalt-r1-custody/world.tar.gz --receipt evidence/raw/item13/basalt-r1-custody/world-backup.json
```

## Saved material verification

The stopped world archive is162,747,723 bytes, SHA-256
`d44157af4f6893e325170defb60c2fe33a8737b922e44b3216d09c2d9f553269`.
Its503-file inventory excludes session.lock. Backup receipt SHA-256 is
`d0a091ad4a80eed1d5745d9918ecab70dc4aa3d4645c751dc2c975319c3199f2`.
The [fresh restore](r1-world-restore.json) and
[saved comparison](r1-saved-verification.json) pass all2,197 cells with zero
differences and the expected central netherite block. The existing
[reader](../temple-variants/verify_saved.py) now has a specific --basalt mode with
these exact hashes and centerY163; its unchanged temple default still reproduces
all15,562 prior cells and the accepted result byte for byte.

```sh
uv run python -m tools.manage_item4_environment restore --archive evidence/raw/item13/basalt-r1-custody/world.tar.gz --sha256 d44157af4f6893e325170defb60c2fe33a8737b922e44b3216d09c2d9f553269 --target evidence/raw/item13/basalt-r1-custody/restored-world > evidence/raw/item13/basalt-r1-custody/world-restore.json
timeout 120 uv run python -m evidence.item-13.temple-variants.verify_saved --basalt evidence/raw/item13/basalt-r1-custody/restored-world/world > evidence/item-13/basalt-variant/r1-saved-verification.json
```

On the same271-cell authored mask used by the family report, the retained
mountainous r1 NONE-rotation debris center and the forced NONE-rotation component
differ only at local(3,3,3), now netherite_block. Decode the control at
index x+7*z+49*y and this padded projection at x+3+13*(z+3)+169*(y+3), for each
source block excluding structure_void/jigsaw. All270 other authored states match.
This comparison is supported by the exact template, control JSON and projection
hashes recorded in the family report and above. Terrain/structure_void and jigsaw
cells are deliberately excluded from this authored-material equivalence claim.
Saved verification establishes that the entire forced projection persisted too.

The [family report](../fixed-blocks/basalt-chambers-report.md) integrates the
source-supported mining/drop differences and complete conditional model totals.
Retainer/reader lint and types pass. Runtime, stopped-block verification and local
model integration pass; external raw custody remains required and is not implied
by these local checks. No full Item13 completion or final review is claimed.
