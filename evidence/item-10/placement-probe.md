# Nonregistry placement probe diagnostic

Status: SYNTHETIC VALIDATION ONLY. No Minecraft generation run has used this
probe, and no nonregistry density is accepted from it.

The retained [scarecrow writer evidence](../item-8/sources/explorations-scarecrow-scope/README.md)
shows five direct WorldGenLevel.setBlock calls whose booleans are discarded.
A feature return is therefore insufficient proof of complete placement. This
is the concrete gap requiring instrumentation beyond the existing registry and
dimension reader. No new classification or provider audit was performed.

[Item10PlacementProbe](../../tools/Item10PlacementProbe.java) instruments only
ScarecrowFeature.place. It requires exactly one matching method and five matching
write call sites. It preserves each original write invocation and boolean and
records attempt origin/dimension, write position/state/flags/result, normal exit,
write exceptions, installation identity and unfinished attempts at shutdown.
It does not consume random values or change arguments. Runtime equivalence has
not been established. Exceptions outside write calls leave unfinished attempts;
those traces cannot be accepted as a complete census. Installation failures,
missing installation records, duplicate installations or missing shutdown are
also invalid evidence, even if the JVM continues running.

The pinned JDK's internal ASM is used through an explicit module export. Its
observational JVM flag and the compiled probe hash will need to be recorded as
an instrumentation overlay before any controlled experiment. No provider JAR is
modified. A future matched fresh-world control must compare generated content;
passing the fixture below is not a substitute for that experiment.

## Executed checks

```sh
uv run --no-sync pytest tests/item10/test_placement_probe.py -q
uv run --no-sync ruff check tests/item10/test_placement_probe.py
uv run --no-sync basedpyright tests/item10/test_placement_probe.py
```

The single fixture test passes using pinned Temurin 21.0.12.1+1. Compilation
uses `-Xlint:all -Werror`, an explicit classpath and the declared ASM export.
It verifies the retained Explorations archive and class hashes from the accepted
Item 8 identity, then successfully transforms that exact class. Separate JVMs
compare synthetic original and instrumented execution for normal writes, early
return and a thrown write exception. Return values, original call counts and
exception messages match; the refused write remains false and the exceptional
attempt remains explicitly unfinished. Ruff and type checks pass.

The fixture consumes write booleans to test preservation even though the actual
retained generator ignores them. It does not represent Minecraft terrain or
placement success. The first manual compile failed on an inherited invalid
classpath; the explicit classpath used in the reproducible test resolves that
build-input problem. No server was launched during this diagnostic.

Next: connect this bounded probe to the existing verified generation lifecycle,
predeclare the matched control and capture acceptance checks, and validate actual
Minecraft behavior before extending the hook set to other nonregistry writers.
