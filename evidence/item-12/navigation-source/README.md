# Navigation source inspection

The missing fact is whether burial implies command dependence for trial chambers.
Existing Item 8 architecture establishes internal copper lighting and rooms but
not an external entrance. Its preserved packaged JSON already establishes the
map destination: `sources/packaged-json-redacted.json.gz`, resources[4673], path
`data/minecraft/tags/worldgen/structure/on_trial_chambers_maps.json`, SHA-256
`8646a96af3bfd7f53715e46fc45121262a4cecf7491ea291077600f196e1f895`, names
`minecraft:trial_chambers`. No tag re-extraction was needed.

[VillagerTrades.txt](VillagerTrades.txt) supplies the missing producer fact.
At bytecode offset 3048 the normal trade initializer selects CARTOGRAPHER;
offsets 3145 onward create its level-3 listings. Offsets 3198 through 3217
construct TreasureMapForEmeralds with ON_TRIAL_CHAMBERS_MAPS and the trial chamber
map decoration. This is a packaged survival lead, so absence of a visible surface
entrance does not establish a need for admin /locate. Actual trading, modded trade
interception, map search success and player acquisition time remain NOT MEASURED.
The risk assessment is conditional on this packaged path operating, not a runtime
trade acceptance claim. No Item 13 or loot-economy work is performed.

The frozen Supplementaries config enables random adventurer maps, but the existing
[Item 8 map lookup assessment](../../item-8/sources/supplementaries-map-lookup/README.md)
retains the null-returning Quark integration limitation. Do not promote that setting
to successful map delivery. Quark's config describes biome navigation, not proof
of a lead to each buried canonical family. For other families without a verified
specific lead, record elevated or unresolved risk, not proven command necessity.

Reproduction uses the pinned mapped-server input and javap already used by the
existing source extractor. Read-only binary hash checks permit the existing
hardlinked operational library; world evidence still uses strict no-hardlink
custody readers. The initial generic extractor invocation rejected this class
because its fixed allowlist did not include it; a subsequent world-file reader
rejected the operational library hardlink. Neither attempt produced accepted
source evidence. The direct inspection below avoids expanding either tool.

```sh
uv run --no-sync python - <<'PY'
from pathlib import Path
import subprocess, hashlib
from tools.inspect_item8_pool_elements import MAPPED_SERVER, ROOT
assert hashlib.sha256(MAPPED_SERVER.path.read_bytes()).hexdigest() == MAPPED_SERVER.sha256
result = subprocess.run([
    str(ROOT/'downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap'),
    '-p', '-c', '-constants', '-classpath', str(MAPPED_SERVER.path),
    'net.minecraft.world.entity.npc.VillagerTrades'], check=True, capture_output=True)
assert hashlib.sha256(MAPPED_SERVER.path.read_bytes()).hexdigest() == MAPPED_SERVER.sha256
assert result.stdout == Path('evidence/item-12/navigation-source/VillagerTrades.txt').read_bytes()
PY
```

Mapped-server SHA-256:
`26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71`.
The full disassembly is retained unchanged, including the separate experimental
trade branch, so the selected normal branch can be reviewed in context.
