#!/usr/bin/env python3
"""Build deterministic input for the exact Item 3 Maven range probe."""

from __future__ import annotations

import argparse
from pathlib import Path

from mcpack_evidence.item3_jar_models import JarInspectionReport


def main() -> None:
    """Emit every unique installed-version and active NeoForge range pair."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--inspection", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = JarInspectionReport.model_validate_json(args.inspection.read_text(encoding="utf-8"))
    versions = _provided_versions(report)
    requests: set[tuple[str, str]] = set()
    for candidate in report.candidates:
        requests.update(
            ("4.0", declaration.version_range)
            for declaration in candidate.loader_declarations
            if declaration.source_path == "META-INF/neoforge.mods.toml"
        )
        dependencies = candidate.dependencies + tuple(
            dependency
            for library in candidate.embedded_libraries
            if "META-INF/neoforge.mods.toml" in library.nested_metadata_paths
            for dependency in library.nested_dependencies
        )
        for dependency in dependencies:
            if dependency.source_path != "META-INF/neoforge.mods.toml":
                continue
            installed = versions.get(dependency.mod_id, ())
            requests.update(
                (version, version_range)
                for version in installed
                for version_range in dependency.version_ranges
            )
    lines = (
        f"range_{index:04d}\t{version}\t{version_range}"
        for index, (version, version_range) in enumerate(sorted(requests), start=1)
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    _ = args.output.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _provided_versions(report: JarInspectionReport) -> dict[str, tuple[str, ...]]:
    values: dict[str, list[str]] = {
        "minecraft": ["1.21.1", "1.21"],
        "neoforge": ["21.1.249", "21.0.166"],
    }
    for candidate in report.candidates:
        for mod in candidate.mods:
            if mod.source_path != "META-INF/neoforge.mods.toml":
                continue
            version = mod.version
            if version == "${file.jarVersion}":
                version = candidate.manifest_implementation_version or "unknown"
            values.setdefault(mod.mod_id, []).append(version)
        for library in candidate.embedded_libraries:
            if "META-INF/neoforge.mods.toml" not in library.nested_metadata_paths:
                continue
            for mod_id in library.nested_mod_ids:
                values.setdefault(mod_id, []).append(library.artifact_version or "unknown")
    return {key: tuple(dict.fromkeys(rows)) for key, rows in values.items()}


if __name__ == "__main__":
    main()
