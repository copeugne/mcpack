# Missing template source behavior

Extraction source: `5629b2b`. The existing inspector reads the frozen mapped
Minecraft server archive from the Item 2 baseline, SHA-256
`26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71`.
The archive identity is also recorded in `evidence/item-2/baseline-manifest.json`.
Only text disassemblies are committed. `identities.json`, SHA-256
`3f237bac34103b26e4d8576c0c27eb40716ff7408074a4f6ddf38f4f1fcfe8b5`,
binds the four original classes and their disassemblies. The SinglePoolElement
disassembly includes bootstrap method handles; its local Classfile path is
replaced with the archive/member identity by the tracked inspector.

```sh
uv run -m tools.inspect_item8_pool_elements --archive server-1.21.1-20240808.144430-srg.jar --output evidence/raw/item8/missing-template-code-reproduction1
diff -qr evidence/raw/item8/missing-template-code-pilot1 evidence/raw/item8/missing-template-code-reproduction1
```

The committed-source output reproduced the pilot byte for byte. Scoped Ruff and
basedpyright checks passed. This extends existing code-inspection evidence
because the static missing reference alone cannot establish how it is consumed.
It does not introduce a new validator, experiment or evidence framework.

Small Yacht's packaged spawner pool has four positive-weight single-template
entries. The final one references
`dungeons_arise_seven_seas:small_yacht/small_yacht_spawner_3`, which is missing
from the selected template catalog. The pool member hash is
`c9da6d4b2d1db166db516aab31e33e09c2abd1c551b3d2966156336adc6588d5`.
The source pool and missing edge are retained in the existing packaged catalog
and `pool-traces-content.json.gz`.

In the preserved base implementation, SinglePoolElement resolves its resource
through StructureTemplateManager.getOrCreate. When no template is found, that
method caches a new StructureTemplate with empty palettes/entities and zero
size. Filtering its blocks returns an empty list. SinglePoolElement obtains
its jigsaw connectors through that filter, and JigsawPlacement.Placer iterates
connectors before attaching a candidate. Thus this base path supplies no
authored spawner or attachment connector from the missing resource. It is not
equivalent to a deliberate EmptyPoolElement that stops candidate selection.
Pool weight alone does not establish a one-in-four missing-spawner rate.

This is a source derivation from the frozen mapped Minecraft classes, not an
observed placement or a dump of classes after every mod transformation. It
does not prove that Small Yacht crashes, that every connector succeeds, or that
the full retained stack leaves these paths unchanged. Preserve the malformed
packaged reference and baseline identity. Effective placement and relevant mod
transformations remain to be checked before closing this family attribute.
