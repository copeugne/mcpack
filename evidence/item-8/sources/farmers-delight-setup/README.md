# Farmers Delight common setup

Extractor f83e06de35fdff66ca7bf4a3e32a1df809c70b68. Manifest SHA-256:
d112ad28ee2983a420b8432cf1f1fe82686a297437bc089968d5fa32d55e5918.
Independent r1 matches every generated file.

The main loader delegates common setup to this class. Its queued work registers
dispenser behavior and extends villager food/item sets. It does not create an
independent generation route. Combine this source with the provider capture;
this single delegate is not whole-provider acceptance.

```sh
uv run -m tools.inspect_item8_pool_elements --archive FarmersDelight-1.21.1-1.3.2.jar --class-name vectorwing/farmersdelight/common/CommonSetup.class --output evidence/raw/item8/farmers-delight-setup-r1
```
