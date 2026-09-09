#!/usr/bin/env bash
set -euo pipefail
# Run from repository root. Outputs must be absent.
out=${1:?Supply an absent output directory}
[ ! -e "$out" ] || { echo 'Output already exists' >&2; exit 1; }
server=instances/pristine-baseline-v0/libraries/net/minecraft/server/1.21.1-20240808.144430/server-1.21.1-20240808.144430-srg.jar
combat=downloads/item3/candidates/bettercombat-neoforge-2.3.2+1.21.1.jar
printf '%s  %s\n' 26ca9c40d7e1681190b428583c38816852218e78df3f8bdb60a59a78503aec71 "$server" | sha256sum -c -
printf '%s  %s\n' afb1f28271ee3b622947f533aa754bb22ed67edd4940a3e9fdf2cca1edb7b8a9 "$combat" | sha256sum -c -
javap=downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap
mkdir "$out"
for type in world.item.SwordItem world.item.Tiers world.item.Items world.entity.player.Player world.entity.ai.attributes.Attributes world.entity.LivingEntity world.entity.monster.Zombie world.entity.monster.Spider world.entity.monster.AbstractSkeleton world.level.BaseSpawner world.damagesource.CombatRules; do
  "$javap" -p -c -classpath "$server" "net.minecraft.$type" > "$out/$type.txt"
done
for type in PlayerAttackHelper; do
  "$javap" -p -c -classpath "$combat" "net.bettercombat.logic.$type" > "$out/$type.txt"
done
unzip -p "$combat" data/bettercombat/weapon_attributes/sword.json > "$out/sword.json"
unzip -p "$combat" data/minecraft/weapon_attributes/iron_sword.json > "$out/iron_sword.json"
gzip -n "$out/"*.txt
(cd "$out" && sha256sum ./*.txt.gz ./*.json > SHA256SUMS)
