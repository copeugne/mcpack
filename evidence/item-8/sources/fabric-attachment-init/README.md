# fabric-attachment-init source roles

Extractor d3be53f. Independent r1 reproduction matches the manifest and every
disassembly byte. Manifest SHA-256: 9add3414f670243af4701ec42e118c410479a35c8064e2691745ad0bc2dcc7e4.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-data-attachment-api-v1-1.4.5+26d408aa19.jar --class-name net/fabricmc/fabric/impl/attachment/AttachmentEntrypoint.class --output evidence/raw/item8/fabric-attachment-init-r1
```

The initializer registers respawn, dimension-change and mob-conversion callbacks. transfer copies existing attachment values between existing holders, respecting serializer and copy-on-death conditions. AttachmentModImpl registration remains a separate open boundary.
