#!/usr/bin/env bash
set -euo pipefail
printf '%s\n' '4f7853b7b6531f99d3f0592b2129291d2e0cf24b4ad5d1381b3883dbdcfbc52d  evidence/item-8/inventory.json' | sha256sum -c -
jq -en --slurpfile inventory evidence/item-8/inventory.json \
  --rawfile matrix evidence/item-9/classification.md '
  ($matrix | split("\n") | map(select(startswith("|"))) | .[2:] |
   map(split("|")[1:-1] | map(gsub("^ +| +$"; "")))) as $rows |
  ["village","ruin","tower","dungeon-mine","dungeon-tomb","dungeon-fort",
   "dungeon-mansion","dungeon-trial","house","ship","shrine","portal",
   "worksite","nature","camp","outpost","statue","bridge","cache","arena"] as $groups |
  if ($inventory[0].status == "COMPLETE") and
     ($rows | length == 448) and
     ([$rows[][0]] | sort) == ($inventory[0].families | keys) and
     all($rows[]; length == 7 and all(.[]; length > 0)) and
     all($rows[]; .[1] | IN("T0","C","T1","T2","T3","T4")) and
     all($rows[]; .[2] | IN("H","M","L")) and
     all($rows[]; .[3] == "-" or
         (.[3] | split(",") | all(.[]; IN("D","S","O")))) and
     all($rows[]; .[4] | split(",") | all(.[]; . as $g | $groups | index($g)))
  then {
    gate: "PASS",
    families: ($rows | length),
    roles: ($rows | group_by(.[1]) | map({key: .[0][1], value: length}) | from_entries),
    confidence: ($rows | group_by(.[2]) | map({key: .[0][2], value: length}) | from_entries),
    flags: {
      decoration: ([$rows[] | select(.[3] | split(",") | index("D"))] | length),
      shallow: ([$rows[] | select(.[3] | split(",") | index("S"))] | length),
      oversized: ([$rows[] | select(.[3] | split(",") | index("O"))] | length),
      themes: ([$rows[] | select(.[4] != "-")] | length),
      village_candidates: ([$rows[] | select(.[4] | split(",") | index("village"))] | length),
      ruin_candidates: ([$rows[] | select(.[4] | split(",") | index("ruin"))] | length),
      tower_candidates: ([$rows[] | select(.[4] | split(",") | index("tower"))] | length),
      dungeon_candidates: ([$rows[] | select(.[4] | split(",") | any(.[]; startswith("dungeon-")))] | length)
    }
  } else error("Item 9 population, required field or vocabulary mismatch") end'
git diff --check
