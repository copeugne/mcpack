# Railways handcar and setup capture

Extractor: cf398e31098d6cef59c25b1e57cd78d0640e3143.
Two classes reproduced byte-for-byte independently. This isolated generated
increment preserves the complete setup dispatch and player handcar assembly
implementation. No provider closure is implied.

```sh
uv run -m tools.inspect_item8_pool_elements --archive railways-0.2.1+neoforge-mc1.21.1.jar \
  --class-name com/railwayteam/railways/ModSetup.class \
  --class-name com/railwayteam/railways/content/handcar/HandcarItem.class \
  --output evidence/raw/item8/railways-assembly-r1
```
