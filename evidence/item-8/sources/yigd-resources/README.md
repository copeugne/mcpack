# Grave custom resource consumers

Extractor 2af842f99c45db8834a202febaeb8cc1558586f1. Independent r1 reproduction matches all files.
Manifest SHA-256: e4ded8871588e2161f81da4bf58624c3ccacd60a223a03b1f5b3aca6c701ec77.

```sh
uv run -m tools.inspect_item8_pool_elements --archive youre-in-grave-danger-neoforge-2.0.13.jar --class-name 'com/b1n_ry/yigd/util/YigdResourceHandler$GraveServerModelLoader.class' --class-name 'com/b1n_ry/yigd/util/YigdResourceHandler$GraveyardDataLoader.class' --class-name 'com/b1n_ry/yigd/util/YigdResourceHandler$GraveAreaOverrideLoader.class' --output evidence/item-8/sources/yigd-resources
```

Server grave shape, coordinate and drop-rule resource consumers.
