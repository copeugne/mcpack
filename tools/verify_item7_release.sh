#!/usr/bin/env bash
set -euo pipefail

# How to run:
#   tools/verify_item7_release.sh REPOSITORY TAG MANIFEST_DIRECTORY PUBLICATION DOWNLOAD_DIRECTORY

if [[ $# -ne 5 ]]; then
  echo "usage: verify_item7_release.sh REPOSITORY TAG MANIFEST_DIRECTORY PUBLICATION DOWNLOAD_DIRECTORY" >&2
  exit 2
fi

repository=$1
tag=$2
manifest_directory=$3
publication=$4
download_directory=$5
if [[ ! -d $manifest_directory || -L $publication || ! -f $publication || -e $download_directory ]]; then
  echo "manifest directory must exist and download directory must be absent" >&2
  exit 2
fi

mapfile -d '' manifests < <(
  find "$manifest_directory" -maxdepth 1 -type f -name '*-manifest.json' -print0 | sort -z
)
if [[ ${#manifests[@]} -ne 4 ]]; then
  echo "exactly four archive manifests are required" >&2
  exit 1
fi

mapfile -t revisions < <(for manifest in "${manifests[@]}"; do jq -r .revision "$manifest"; done | sort -u)
if [[ ${#revisions[@]} -ne 1 || ! ${revisions[0]} =~ ^[0-9a-f]{40}$ ]]; then
  echo "archive manifests do not share one full revision" >&2
  exit 1
fi

tag_ref=$(gh api "repos/$repository/git/ref/tags/$tag")
tag_object=$(jq -r '.object.sha' <<<"$tag_ref")
tag_type=$(jq -r '.object.type' <<<"$tag_ref")
if [[ $tag_type == tag ]]; then
  tag_detail=$(gh api "repos/$repository/git/tags/$tag_object")
  tag_commit=$(jq -r 'select(.object.type == "commit") | .object.sha' <<<"$tag_detail")
elif [[ $tag_type == commit ]]; then
  tag_commit=$tag_object
else
  tag_commit=
fi
if [[ $tag_commit != "${revisions[0]}" ]]; then
  echo "remote tag does not resolve to the archive revision" >&2
  exit 1
fi

release=$(gh release view "$tag" --repo "$repository" \
  --json tagName,url,isDraft,isPrerelease,publishedAt,assets)
jq -e --arg tag "$tag" \
  '.tagName == $tag and (.isDraft | not) and (.isPrerelease | not)
   and (.publishedAt | type == "string") and (.assets | length == 4)
   and all(.assets[]; .state == "uploaded")' <<<"$release" >/dev/null
release_url=$(jq -r .url <<<"$release")
published_at=$(jq -r .publishedAt <<<"$release")
jq -e \
  --arg repository "$repository" \
  --arg tag "$tag" \
  --arg tag_object "$tag_object" \
  --arg revision "${revisions[0]}" \
  --arg release_url "$release_url" \
  --arg published_at "$published_at" \
  '.schema_version == "item7-raw-evidence-publication-v1"
   and .repository == $repository and .tag == $tag
   and .tag_object_sha == $tag_object and .source_revision == $revision
   and .release_url == $release_url and .published_at == $published_at
   and .downloaded_bytes_verified == true and (.assets | length == 4)' \
  "$publication" >/dev/null

for manifest in "${manifests[@]}"; do
  name=$(jq -r .archive_name "$manifest")
  size=$(jq -r .archive_size_bytes "$manifest")
  expected_sha=$(jq -r .archive_sha256 "$manifest")
  asset_url=$(jq -r --arg name "$name" '.assets[] | select(.name == $name) | .url' <<<"$release")
  jq -e --arg name "$name" --argjson size "$size" \
    '[.assets[] | select(.name == $name and .size == $size and .state == "uploaded")] | length == 1' \
    <<<"$release" >/dev/null
  jq -e --arg name "$name" --argjson size "$size" --arg sha "$expected_sha" \
    --arg manifest "$manifest" --arg url "$asset_url" \
    '[.assets[] | select(.name == $name and .size_bytes == $size and .sha256 == $sha
      and .manifest == $manifest and .url == $url)] | length == 1' "$publication" >/dev/null
done

mkdir "$download_directory"
gh release download "$tag" --repo "$repository" --dir "$download_directory"
for manifest in "${manifests[@]}"; do
  name=$(jq -r .archive_name "$manifest")
  expected_size=$(jq -r .archive_size_bytes "$manifest")
  expected_sha=$(jq -r .archive_sha256 "$manifest")
  archive=$download_directory/$name
  if [[ -L $archive || ! -f $archive || $(stat -c '%s' "$archive") != "$expected_size" ]]; then
    echo "downloaded archive size or type differs: $name" >&2
    exit 1
  fi
  actual_sha=$(sha256sum "$archive" | awk '{print $1}')
  if [[ $actual_sha != "$expected_sha" ]]; then
    echo "downloaded archive hash differs: $name" >&2
    exit 1
  fi
done

printf 'verified %s release assets at revision %s\n' "${#manifests[@]}" "${revisions[0]}"
