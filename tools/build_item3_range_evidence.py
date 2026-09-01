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

_MAVEN_SHA256 = "91172bc294d6eab02fc9f45f4ea01fd0e418962d128cf489abea7b6957d988ee"
_COMMONS_LANG_SHA256 = "7b96bf3ee68949abb5bc465559ac270e0551596fa34523fddf890ec418dde13c"
_REQUEST_FIELD_COUNT = 3


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--requests", type=Path, required=True)
    parser.add_argument("--probe-source", type=Path, required=True)
    parser.add_argument("--maven-jar", type=Path, required=True)
    parser.add_argument("--commons-lang-jar", type=Path, required=True)
    parser.add_argument("--java", type=Path, default=Path(shutil.which("java") or "java"))
    parser.add_argument("--javac", type=Path, default=Path(shutil.which("javac") or "javac"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--results-output", type=Path)
    return parser.parse_args()


def main() -> None:
    """Compile the probe, evaluate every unique range, and write its receipt."""
    args = _arguments()
    _verify_oracle(args.maven_jar, _MAVEN_SHA256, "Maven Artifact 3.8.5")
    _verify_oracle(args.commons_lang_jar, _COMMONS_LANG_SHA256, "Commons Lang 3.14.0")
    cases = _read_requests(args.requests)

    with tempfile.TemporaryDirectory(prefix="mcpack-maven-probe-") as build_text:
        build = Path(build_text)
        classpath = f"{args.maven_jar}:{args.commons_lang_jar}"
        subprocess.run(  # noqa: S603 - explicit local executable and arguments
            [str(args.javac), "-cp", classpath, "-d", str(build), str(args.probe_source)],
            check=True,
        )
        probe_input = "".join(
            f"{case_id}\t{version}\t{specification}\n" for case_id, version, specification in cases
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
                "version": version,
                "range": specification,
                "status": results[case_id][0],
                "normalized_range_or_error": results[case_id][1],
            }
            for case_id, version, specification in cases
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    if args.results_output is not None:
        args.results_output.parent.mkdir(parents=True, exist_ok=True)
        args.results_output.write_text(completed.stdout, encoding="utf-8")


def _verify_oracle(path: Path, expected_sha256: str, label: str) -> None:
    actual = _sha256(path)
    if actual != expected_sha256:
        message = f"{label} SHA-256 mismatch: expected {expected_sha256}, found {actual}"
        raise ValueError(message)


def _read_requests(path: Path) -> list[tuple[str, str, str]]:
    cases: list[tuple[str, str, str]] = []
    seen: set[tuple[str, str]] = set()
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        fields = line.split("\t")
        if len(fields) != _REQUEST_FIELD_COUNT or not all(fields):
            message = f"invalid range request at {path}:{line_number}"
            raise ValueError(message)
        case_id, version, specification = fields
        pair = (version, specification)
        if pair in seen:
            message = f"duplicate range request at {path}:{line_number}: {pair}"
            raise ValueError(message)
        seen.add(pair)
        cases.append((case_id, version, specification))
    if not cases:
        message = f"no range requests in {path}"
        raise ValueError(message)
    return cases


if __name__ == "__main__":
    main()
