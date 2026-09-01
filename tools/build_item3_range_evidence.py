#!/usr/bin/env python3
"""Evaluate all Item 3 metadata ranges with the frozen Maven implementation."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inspection", type=Path, required=True)
    parser.add_argument("--probe-source", type=Path, required=True)
    parser.add_argument("--maven-jar", type=Path, required=True)
    parser.add_argument("--commons-lang-jar", type=Path, required=True)
    parser.add_argument("--java", type=Path, default=Path(shutil.which("java") or "java"))
    parser.add_argument("--javac", type=Path, default=Path(shutil.which("javac") or "javac"))
    parser.add_argument("--output", type=Path, required=True)
    return parser.parse_args()


def main() -> None:
    """Compile the probe, evaluate every unique range, and write its receipt."""
    args = _arguments()
    inspection: dict[str, Any] = json.loads(args.inspection.read_text(encoding="utf-8"))
    cases: list[tuple[str, str, str, str]] = []
    seen: set[tuple[str, str]] = set()
    targets = (
        ("minecraft_direct", "1.21.1"),
        ("minecraft_fallback", "1.21"),
        ("neoforge_direct", "21.1.249"),
        ("neoforge_fallback", "21.0.166"),
        ("builtin_language", "4.0"),
    )
    ranges = {
        value
        for candidate in inspection["candidates"]
        for value in (
            *candidate["minecraft_ranges"],
            *candidate["neoforge_ranges"],
            *candidate["loader_ranges"],
            *(value for dep in candidate["dependencies"] for value in dep["version_ranges"]),
        )
    }
    for specification in sorted(ranges):
        for target_id, version in targets:
            if (version, specification) in seen:
                continue
            seen.add((version, specification))
            cases.append((f"case-{len(cases):04d}", target_id, version, specification))

    with tempfile.TemporaryDirectory(prefix="mcpack-maven-probe-") as build_text:
        build = Path(build_text)
        classpath = f"{args.maven_jar}:{args.commons_lang_jar}"
        subprocess.run(  # noqa: S603 - explicit local executable and arguments
            [str(args.javac), "-cp", classpath, "-d", str(build), str(args.probe_source)],
            check=True,
        )
        probe_input = "".join(
            f"{case_id}\t{version}\t{specification}\n"
            for case_id, _, version, specification in cases
        )
        completed = subprocess.run(  # noqa: S603 - explicit local executable and arguments
            [str(args.java), "-cp", f"{build}:{classpath}", "MavenVersionRangeProbe"],
            check=True,
            input=probe_input,
            text=True,
            capture_output=True,
        )
    results = {}
    for line in completed.stdout.splitlines():
        case_id, status, detail = line.split("\t", maxsplit=2)
        results[case_id] = (status, detail)
    evidence = {
        "schema_version": "item3-maven-range-evidence-v1",
        "target": {"minecraft": "1.21.1", "neoforge": "21.1.249"},
        "oracle": {
            "implementation": "org.apache.maven.artifact.versioning.VersionRange",
            "maven_artifact_version": "3.8.5",
            "maven_artifact_sha256": _sha256(args.maven_jar),
            "commons_lang_version": "3.14.0",
            "commons_lang_sha256": _sha256(args.commons_lang_jar),
            "probe_source_sha256": _sha256(args.probe_source),
        },
        "cases": [
            {
                "id": case_id,
                "purpose": purpose,
                "version": version,
                "range": specification,
                "status": results[case_id][0],
                "normalized_range_or_error": results[case_id][1],
            }
            for case_id, purpose, version, specification in cases
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
