# Fabric attachment registration source roles

Extractor e94b87e. Independent r1 reproduction matches the manifest and every
disassembly byte. Manifest SHA-256: e5d85879d444086c19fa15921336c7e711185d212564b35501e8bc8eb58dda67.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-data-attachment-api-v1-1.4.5+26d408aa19.jar --class-name net/fabricmc/fabric/impl/attachment/AttachmentModImpl.class --class-name net/fabricmc/fabric/impl/attachment/AttachmentRegistryImpl.class --output evidence/raw/item8/fabric-attachment-registration-r1
```

The verbose AttachmentModImpl capture resolves the previously hidden callback
as AttachmentRegistryImpl.registerNeoTypes. It forwards the initially empty
attachment-type map to the supplied registration helper. Public registration
accepts caller-supplied IDs/types, either deferred or directly in ATTACHMENT_TYPES.
The other map translates existing Fabric/NeoForge attachment types. No default
site or world-generation route is registered. Reuse db84f92 for transfer behavior.
The older nonverbose entry capture is preserved; its class identity is unchanged.
