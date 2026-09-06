# Explorations provider entry boundaries

Selector b454032 captures the complete 33-class archive. The existing scarecrow,
Slime Cave and deepslate interpretations remain in their earlier source records;
this pass resolves the remaining provider entries and component consumers.
The independent capture reproduced exactly before this README was added.
Archive SHA-256: 420d0373711877a5e1a86b7f9b4f54848f3debb2f116c2509a5cc4eb496c979e.
Identity manifest SHA-256:
7889daf6336c190cec169bc57eac369ebf863eb4c72e2b7895341aa12b4e9b8f.

```sh
uv run -m tools.inspect_item8_pool_elements \
  --archive explorations-neoforge-1.21.1-1.6.2.jar \
  --output evidence/raw/item8/explorations-provider-r1
```

NeoforgeExplorations loads ModRegistry and attaches ServerAboutToStartEvent.
The callback loads and verifies configuration, then calls addStatuesToVillages.
The two service implementations provide DeferredRegister registration and platform
access. The declared mixins expose pool entries and tree-decorator registration.

ModRegistry registers the scarecrow feature, underground-temple and slime-cave
structure types, slime-cave piece, lantern and cave-vine decorators, and deepslate,
stone-brick-aging and wool-replacement processors. The temple uses its configured
start pool and JigsawPlacement. The Slime Cave's single template and marker
behavior were already resolved; neither type is an additional family merely
because it has a custom codec. The processors transform existing piece blocks.

WorldGenHelper reads the configured village/statue lists, resolves each target
pool and constructs legacy single elements with the empty processor list and
RIGID projection. It updates both expanded and raw weighted lists. A missing
compatible pool causes that addition to return without mutation. Frozen statue
entries target plains, savanna, snowy and taiga village houses pools, with four
statues in each. These are components of consuming villages, not four new roots.

LanternDecorator chooses positions below leaf blocks and writes chains and
lanterns. The packaged large_mushroom tree uses this decorator. Its leaf-position
shuffle uses Collections.shuffle without the generation RandomSource argument;
do not claim deterministic decoration from this source or repair it here.
CaveVineDecorator supplies hanging vegetation to a consuming tree; no packaged
configured feature in this archive uses it. Keep any external consumer separate.

The source capture supports provider reconciliation, not observed placement,
successful block writes or final family attributes. Preserve the underground
temple's missing references and the named mushroom/decoration grouping question
in provider-scope.md rather than silently modifying the frozen content.
