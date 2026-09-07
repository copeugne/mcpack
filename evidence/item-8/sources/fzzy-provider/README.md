# Fzzy Config entry boundaries

Extractor 92d4797bcfa358949a0cdb7954be417dfd538fda. Independent r1 reproduction matches all
disassemblies and the identity manifest. Manifest SHA-256:
a5d373218b1ed79fd349e2f329c911da42358bae5f67636bf2bdb5b859d12811

```sh
uv run -m tools.inspect_item8_pool_elements --archive fzzy_config-0.7.6+1.21+neoforge.jar --class-name me/fzzyhmstrs/fzzy_config/FzzyConfigNeoForge.class --class-name me/fzzyhmstrs/fzzy_config/FzzyConfigNeoForgeClient.class --output evidence/item-8/sources/fzzy-provider
```

Entry boundary evidence only. Configuration, command and registry delegates
still require membership disposition before provider closure.
