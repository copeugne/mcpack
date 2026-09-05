# Pool compilation content disposition

The previously retained `CompileRawTemplatesModifier` invokes each pool's
`compileRawTemplates` at priority 2147483647. This evidence follows that call
through the mixin, container and weighted-entry constructor.

Executed successfully using tool `45e194d`, into an absent output directory:

```sh
uv run -m tools.inspect_item8_pool_elements --archive lithostitched-1.7.10+beta4-neoforge-21.1.jar --class-name dev/worldgen/lithostitched/mixin/common/StructureTemplatePoolMixin.class --class-name dev/worldgen/lithostitched/worldgen/structure/LithostitchedTemplates.class --class-name 'dev/worldgen/lithostitched/worldgen/structure/LithostitchedTemplates$WeightedEntry.class' --output evidence/item-8/sources/lithostitched-pool-compilation-code
```

Scoped Ruff and basedpyright passed. The three disassembly hashes match the
identity records; the tool verified the retained archive before extraction.

The mixin iterates existing raw template pairs and passes each existing element
and weight to `LithostitchedTemplates.add`. That method constructs a weighted
entry with the same element, the current list index and the supplied weight.
The constructor stores those values, also recording whether a delegating
element is prioritized. It does not manufacture a new element or template.

The shuffle path copies the entries, assigns random ordering weights, sorts
them and returns their stored elements. It affects selection order, which this
Item 8 potential-content trace does not simulate. Compilation therefore does
not require another family, template edge or measurement implementation.
This disposition concerns possible content only. It does not establish
selection probabilities, placement success, restart behavior or pacing.

The current machine-readable modifier report still labels compilation untraced.
Apply this disposition with the remaining modifier updates, avoiding repeated
whole-inventory hash migrations for individual report-only changes. Other
modifiers, effective spawner configurations and overall Item 8 closure remain
open.
