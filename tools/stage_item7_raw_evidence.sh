#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 4 ]]; then
  echo "usage: stage_item7_raw_evidence.sh MODE PROJECT_ROOT RAW_ROOT OUTPUT_DIRECTORY" >&2
  exit 2
fi

mode=$1
project=$2
raw=$3
output=$4
case "$mode" in
  core | run-a-worlds | run-b-worlds | auxiliary-worlds) ;;
  *)
    echo "unknown stage mode: $mode" >&2
    exit 2
    ;;
esac
if [[ ! -d $project || ! -d $raw || -e $output ]]; then
  echo "project and raw roots must exist, and output must be absent" >&2
  exit 2
fi

copy_entry() {
  local source=$1
  local destination=$2
  if [[ $(stat -c '%d' "$source") == $(stat -c '%d' "$destination") ]]; then
    cp --archive --link "$source" "$destination/"
  else
    cp --archive --reflink=auto "$source" "$destination/"
  fi
}

copy_contents() {
  local source=$1
  local destination=$2
  mkdir -p "$destination"
  if [[ $(stat -c '%d' "$source") == $(stat -c '%d' "$destination") ]]; then
    cp --archive --link "$source/." "$destination/"
  else
    cp --archive --reflink=auto "$source/." "$destination/"
  fi
}

copy_world_boundary() {
  local instance=$1
  local destination=$2
  mkdir -p "$destination"
  for relative in level.dat level.dat_old; do
    if [[ -f $instance/world/$relative ]]; then
      copy_entry "$instance/world/$relative" "$destination"
    fi
  done
  for relative in region DIM-1/region DIM1/region; do
    if [[ -d $instance/world/$relative ]]; then
      local parent
      parent=$(dirname "$relative")
      mkdir -p "$destination/$parent"
      copy_entry "$instance/world/$relative" "$destination/$parent"
    fi
  done
}

stage_run_worlds() {
  local run=$1
  for role in ordinary mountainous ocean-heavy biome-diverse; do
    copy_world_boundary \
      "$project/instances/item7/$run-$role" \
      "$output/$run-$role/world"
  done
}

mkdir -p "$output"
case "$mode" in
  core)
    copy_contents "$raw" "$output"
    mkdir -p "$output/pilot"
    copy_contents "$project/evidence/item-7/pilot" "$output/pilot"
    ;;
  run-a-worlds)
    stage_run_worlds run-a
    ;;
  run-b-worlds)
    stage_run_worlds run-b
    ;;
  auxiliary-worlds)
    for name in \
      control-ordinary \
      control-ordinary-failed-marker \
      gap-a-ordinary \
      gap-a-ordinary-rejected-config-contract \
      gap-b-ordinary \
      pilot-characterization \
      pilot-tracked-ordinary \
      pilot-tracked-ordinary-success; do
      copy_world_boundary "$project/instances/item7/$name" "$output/$name/world"
    done
    ;;
esac

if find "$output" \( -type l -o -type f \( -name '*.jar' -o -name 'session.lock' \) \) \
  -print -quit | grep -q .; then
  echo "forbidden runtime binary or session lock entered the stage" >&2
  exit 1
fi

printf 'staged %s files using %s bytes\n' \
  "$(find "$output" -type f | wc -l)" \
  "$(find "$output" -type f -printf '%s\n' | awk '{total += $1} END {print total + 0}')"
