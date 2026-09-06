# Architectury spawn packet membership boundary

Extractor bb4fd5eb. Independent r1 reproduction matches source and manifest
bytes. Manifest SHA-256:
cb2e12853d525539a7b353dbe9656a6981d22ff735cfb170e25469fc605431e0

```sh
uv run -m tools.inspect_item8_pool_elements --archive architectury-13.0.8-neoforge.jar --class-name dev/architectury/networking/SpawnEntityPacket.class --output evidence/raw/item8/architectury-spawn-packet-r1
```

register adds a client-bound payload type. create accepts an existing entity
and server tracker, rejects logical-client use and returns a client-bound packet.
This synchronizes an existing entity; it does not register independent generated
content. No further packet codec or generic network inspection is required for
membership.
