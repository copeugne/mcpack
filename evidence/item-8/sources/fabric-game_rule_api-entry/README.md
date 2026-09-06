# Fabric game_rule_api entry roles

Captured with 5049826 and independently reproduced exactly. Manifest SHA-256:
e4413cde1f7946aaabaedd73db4fcbe27ab5c7285cb3eb9d2017071e2ca7702d.

```sh
uv run -m tools.inspect_item8_pool_elements --archive forgified-fabric-api-0.116.7+2.2.4+1.21.1.jar --nested-archive META-INF/jars/fabric-game-rule-api-v1-1.0.53+36d727be19.jar --class-name net/fabricmc/fabric/mixin/gamerule/GameRuleCommandAccessor.class --class-name net/fabricmc/fabric/mixin/gamerule/GameRuleCommandVisitorMixin.class --class-name net/fabricmc/fabric/mixin/gamerule/GameRulesAccessor.class --class-name net/fabricmc/fabric/mixin/gamerule/GameRulesIntRuleAccessor.class --class-name net/fabricmc/fabric/mixin/gamerule/GameRulesKeyMixin.class --class-name org/sinytra/fabric/game_rule_api/generated/GeneratedEntryPoint.class --output evidence/raw/item8/fabric-game_rule_api-entry-r1
```

Empty generated loader. Common mixins expose rule maps/int values/custom categories and forward enum-rule command registration. No independent generation path.

Complete payload and declared-hook coverage are verified by the existing Fabric
provider check. This capture is not whole-provider or effective-loot acceptance.
