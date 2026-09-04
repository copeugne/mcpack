#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "usage: capture_item7_visual_qa.sh LOOPBACK_BASE_URL OUTPUT_DIRECTORY" >&2
  exit 2
fi

base_url=${1%/}
output=$2
if [[ ! $base_url =~ ^http://127\.0\.0\.1:[0-9]+$ ]]; then
  echo "base URL must be a loopback-only HTTP origin" >&2
  exit 2
fi
if [[ -e $output ]]; then
  echo "output directory already exists: $output" >&2
  exit 2
fi

mkdir -p "$output"
manifest="$output/capture-manifest.tsv"
printf 'path\turl\tsha256\tsize_bytes\n' > "$manifest"

for run in run-a run-b; do
  for role in ordinary mountainous ocean-heavy biome-diverse; do
    for selection in overworld nether end-central end-outer; do
      for page in index.html topdown.svg cross-section-x.svg cross-section-z.svg; do
        relative="$run/$role/$selection/${page%.*}.png"
        target="$output/$relative"
        url="$base_url/$run/$role/gallery/$selection/$page"
        mkdir -p "${target%/*}"
        chromium \
          --headless \
          --disable-gpu \
          --disable-dev-shm-usage \
          --hide-scrollbars \
          --force-device-scale-factor=1 \
          --window-size=1440,1200 \
          --screenshot="$target" \
          "$url" >/dev/null 2>&1
        if [[ $(file --brief --mime-type "$target") != image/png ]]; then
          echo "capture is not PNG: $target" >&2
          exit 1
        fi
        printf '%s\t%s\t%s\t%s\n' \
          "$relative" \
          "$url" \
          "$(sha256sum "$target" | cut -d' ' -f1)" \
          "$(stat -c '%s' "$target")" >> "$manifest"
      done
    done
  done
done

printf 'captured %s Item 7 pages to %s\n' "$(($(wc -l < "$manifest") - 1))" "$output"
