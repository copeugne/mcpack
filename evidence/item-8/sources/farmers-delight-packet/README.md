# Farmers Delight server packet delegate

Extractor f528d11ad1388a822ab84181f21f05cd148d86fd. Manifest SHA-256:
084b325b82dc81640f4abd651edc56c91e260c1972f816298c57f6996b9f8fb2.
Independent r1 matches every generated file.

The registered server handler only sets the flip timestamp on the sending
player's currently used skillet item. It does not place blocks or generate sites.
This closes the specific callback delegated by the preserved ModNetworking entry.

```sh
uv run -m tools.inspect_item8_pool_elements --archive FarmersDelight-1.21.1-1.3.2.jar --class-name 'vectorwing/farmersdelight/common/network/ModNetworking$ServerPayloadHandler.class' --output evidence/raw/item8/farmers-delight-packet-r1
```
