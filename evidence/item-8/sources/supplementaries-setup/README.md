# Supplementaries common setup callbacks

Extractor 9e9c74bf647a19aa276b74f1982f21d45ce631e2. Manifest SHA-256:
cbab9d898accfb9bedc9ab98c56e9b85f08747a062353dd8350d5699dbfad049.
Independent r1 matches every generated file. Verbose disassembly retains
bootstrap targets for the actual registered setup callbacks.

ModSetup.init registers setup, asyncSetup and tagDependantSetup. The asynchronous
callback initializes the already inspected block processor. The tag-dependent
callback recomputes the already inspected road-sign destination cache. These
links do not introduce another independent family. Compatibility setup and
additional-placement delegates still require their own contribution roles.

```sh
uv run -m tools.inspect_item8_pool_elements --archive supplementaries-neoforge-1.21.1-3.6.8.jar --class-name net/mehvahdjukaar/supplementaries/reg/ModSetup.class --output evidence/raw/item8/supplementaries-setup-r1
```
