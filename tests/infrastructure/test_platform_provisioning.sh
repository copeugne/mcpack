#!/usr/bin/env bash
set -euo pipefail

project_root=$(realpath -- "$(dirname -- "$0")/../..")
script="$project_root/infrastructure/bin/platform-1.21.1"
manifest="$project_root/infrastructure/manifests/platform-1.21.1.json"
temporary_root=$(mktemp -d /tmp/mcpack-platform-provisioning.XXXXXX)

cleanup() {
  status=$?
  trap - EXIT
  rm -rf -- "$temporary_root"
  exit "$status"
}
trap cleanup EXIT

[[ -x "$script" ]]
[[ -f "$manifest" ]]

"$script" inspect --root "$project_root" > "$temporary_root/inspect.json"
jq -e '
  .minecraft.version == "1.21.1" and
  .neoforge.version == "21.1.249" and
  .java.version == "21.0.12.1+1" and
  .artifact_count == 4 and
  (.minecraft.server_artifact_id == "minecraft-server") and
  (.neoforge.installer_artifact_id == "neoforge-installer")
' "$temporary_root/inspect.json" >/dev/null
jq -e '
  .schema_version == "mcpack-platform-manifest-v1" and
  (.artifacts | length) == 4 and
  ([.artifacts[].sha256] | sort) == [
    "a1d93b868fab29e5341985d76431401eaf29a3527686f300b0b78047f5081308",
    "ce79869e1307ed8ee1e2baa86a412b1eb5b75d10a01006d788a6f968bcfaee94",
    "d88b448eab73cd65bdf1720844a4828262de30a15fc71bd04dd81acc61c5399a",
    "e3bc55693e93cda0188f2e60aea28113fc647c5e85a15fa3d1b347349231b4bb"
  ]
' "$manifest" >/dev/null

cache="$temporary_root/cache"
mkdir -p -- "$cache/sha256/e3bc55693e93cda0188f2e60aea28113fc647c5e85a15fa3d1b347349231b4bb"
printf 'wrong artifact content' > "$cache/sha256/e3bc55693e93cda0188f2e60aea28113fc647c5e85a15fa3d1b347349231b4bb/server.jar"
truncate --size 51627615 "$cache/sha256/e3bc55693e93cda0188f2e60aea28113fc647c5e85a15fa3d1b347349231b4bb/server.jar"
if "$script" verify-cache --root "$project_root" --cache "$cache" > "$temporary_root/hash-mismatch.out" 2>&1; then
  printf 'verify-cache accepted an artifact with the expected pathname but wrong hash\n' >&2
  exit 1
fi
rg -F 'SHA-256 mismatch' "$temporary_root/hash-mismatch.out" >/dev/null

nonempty_target="$temporary_root/nonempty-target"
mkdir -p -- "$nonempty_target"
printf 'preserve me' > "$nonempty_target/sentinel"
if "$script" install-neoforge --root "$project_root" --cache "$cache" --java-home "$temporary_root/missing-java" --target "$nonempty_target" --installer-log "$temporary_root/installer.log" > "$temporary_root/target-rejection.out" 2>&1; then
  printf 'install-neoforge accepted a nonempty target\n' >&2
  exit 1
fi
[[ "$(<"$nonempty_target/sentinel")" == 'preserve me' ]]
rg -F 'target must be empty' "$temporary_root/target-rejection.out" >/dev/null
