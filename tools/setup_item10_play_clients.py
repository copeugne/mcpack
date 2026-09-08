"""Materialize the two requested official-launcher client profiles."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path

from mcpack_evidence.item6_validation import validate
from mcpack_evidence.item7_runtime import validate_java_runtime


def verified_client_sources(root: Path, evidence: Path) -> list[Path]:
    """Resolve the client manifest against the accepted acquisition hashes."""
    acquisition = json.loads((evidence / "item-3/artifact-acquisition-manifest.json").read_text())
    artifacts = {row["candidate_filename"]: row for row in acquisition["artifacts"]}
    candidates = (evidence / "item-10/server-setup/client-candidates.txt").read_text().splitlines()
    if len(candidates) != len(set(candidates)):
        detail = "client candidate list contains duplicates"
        raise ValueError(detail)
    sources = []
    for name in candidates:
        row = artifacts[name]
        source = root / row["local_path"]
        expected = row["identity"]["computed_sha256"]
        if hashlib.sha256(source.read_bytes()).hexdigest() != expected:
            detail = f"client artifact hash mismatch: {name}"
            raise ValueError(detail)
        sources.append(source)
    return sources


def main() -> None:
    """Verify cached artifacts and preserve the existing launcher profile file."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--minecraft", type=Path, required=True)
    parser.add_argument("--java-home", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    target = args.target.resolve()
    minecraft = args.minecraft.resolve()
    if target.exists():
        parser.error(f"target must be absent: {target}")
    java, _ = validate_java_runtime(args.java_home)
    version = "neoforge-21.1.249"
    if not (minecraft / "versions" / version / f"{version}.json").is_file():
        parser.error("install pinned NeoForge into the official launcher first")
    profile_file = minecraft / "launcher_profiles.json"
    original = profile_file.read_bytes()
    launcher = json.loads(original)
    for name in ("free-roaming", "task"):
        if f"mcpack-item10-{name}" in launcher["profiles"]:
            parser.error(f"launcher profile already exists: {name}")
    evidence = root / "evidence"
    frozen = evidence / "item-6/frozen"
    validate(
        frozen,
        evidence / "item-6/generated-config-manifest.json",
        evidence / "item-6/config-audit.json",
    )
    sources = verified_client_sources(root, evidence)
    target.mkdir(parents=True)
    (target / "launcher_profiles.before.json").write_bytes(original)
    for name in ("free-roaming", "task"):
        instance = target / name
        mods = instance / "mods"
        mods.mkdir(parents=True)
        for source in sources:
            shutil.copyfile(source, mods / source.name)
        for directory in ("config", "defaultconfigs"):
            shutil.copytree(
                frozen / directory,
                instance / directory,
                ignore=shutil.ignore_patterns("resourceful-config-web.json"),
            )
        launcher["profiles"][f"mcpack-item10-{name}"] = {
            "name": f"mcpack: {name}",
            "type": "custom",
            "lastVersionId": version,
            "gameDir": str(instance),
            "javaDir": str(java),
            "javaArgs": "-Xms1G -Xmx4G",
        }
    # A closed launcher is required; detect changes during materialization too.
    if profile_file.read_bytes() != original:
        parser.error("launcher profiles changed during setup; prepared directories retained")
    pending = minecraft / "launcher_profiles.mcpack-pending.json"
    with pending.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(launcher, indent=2) + "\n")
    pending.replace(profile_file)
    print(f"Created two client profiles with {len(sources)} verified artifacts each")


if __name__ == "__main__":
    main()
