# Creeper Overhaul player-login callback

Extractor 382fc1c9348fa3450a95d2a003d263c5488e3a8b. Manifest SHA-256:
abb86e8bdaf55aa9fd570fe47f21f2e30f19c50780019b3a7d4f63ee521096ec.
Independent r1 matches every generated file.

ServerCosmetics stores cosmetic visibility flags and sends their map to players.
The player-login callback delegates to that synchronization operation. It adds
no authored-site generation. No player data was collected for this source capture.

```sh
uv run -m tools.inspect_item8_pool_elements --archive CreeperOverhaul-neoforge-1.21.1-4.0.6.jar --class-name tech/thatgravyboat/creeperoverhaul/common/utils/ServerCosmetics.class --output evidence/raw/item8/creeper-overhaul-login-r1
```
