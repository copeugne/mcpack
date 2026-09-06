# Creating Space arrival delegate

Extractor 215a6a426e43e7c5e51584e9deab4dccda1bf196. Manifest SHA-256: 04e25ddcbb7b1105bcf0d27eb83c605dda16a97ec4d683d829f94d74e97da0e1. Independent r1 matches every generated file.

CustomTeleporter selects arrival coordinates and constructs a DimensionTransition with DO_NOTHING as its post-transition action. It does not load a template or place an arrival platform. This source closes the concrete delegated arrival boundary found in the rocket and common entity hooks.

```sh
uv run -m tools.inspect_item8_pool_elements --archive creatingspace-1.21.1-1.7.18.jar --class-name com/rae/creatingspace/content/rocket/CustomTeleporter.class --output evidence/raw/item8/creating-space-arrival-r1
```
