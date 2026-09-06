# Bookshelf common initialization boundary

Extractor d2a5bc24. Independent r1 reproduction matches source and manifest
bytes. Manifest SHA-256:
5dd211d3d7a55d6f8fbb16ce18b92b1827db2f63b1bbe18aa3911a7f8b4baf82

```sh
uv run -m tools.inspect_item8_pool_elements --archive bookshelf-neoforge-1.21.1-21.1.81.jar --class-name net/darkhax/bookshelf/common/impl/BookshelfMod.class --class-name net/darkhax/bookshelf/common/api/registry/ContentProvider.class --output evidence/raw/item8/bookshelf-startup-r1
```

Common initialization checks repeated initialization and invalid legacy content
providers. ContentProvider supplies empty defaults rather than generation.
BookshelfContent overrides utility codec, description and command definitions
captured in bookshelf-provider. This closes independent-family membership;
consumer loot modification, fake-player damage and gameplay hooks remain
attribute inputs. No more generic registry, networking or condition tracing.
