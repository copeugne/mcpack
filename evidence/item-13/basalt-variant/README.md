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
