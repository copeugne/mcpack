# Supplementaries bundled Sable Companion service

Extractor bbae69f4aea21e52e0ea804ed365c8628600a967. Manifest SHA-256:
0e58be3a4ae7cc39891a83c05fd25707e7dafc44831648596ee5ea64dafef660.
Independent r1 matches every generated file.

Retains the service interface, default implementation and direct helpers for
provider membership interpretation. This does not re-enable Sable.

```sh
uv run -m tools.inspect_item8_pool_elements --archive supplementaries-neoforge-1.21.1-3.6.8.jar --nested-archive META-INF/jarjar/sable-companion-common-1.21.1-1.6.0.jar --class-name dev/ryanhcode/sable/companion/SableCompanion.class --class-name dev/ryanhcode/sable/companion/impl/DefaultSableCompanion.class --class-name 'dev/ryanhcode/sable/companion/impl/DefaultSableCompanion$DistHelper.class' --class-name dev/ryanhcode/sable/companion/impl/SableCompanionUtil.class --output evidence/raw/item8/supplementaries-sable-companion-r1
```
