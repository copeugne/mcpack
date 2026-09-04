"""Inspect exact custom pool codecs with uv run -m tools.inspect_item8_pool_elements."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import cast
from zipfile import ZipFile

from mcpack_evidence.item8_sources import retained_sources

ROOT = Path(__file__).resolve().parents[1]
ARCHIVES = frozenset(
    {
        "YungsApi-1.21.1-NeoForge-5.1.6.jar",
        "integrated_api-1.7.3+1.21.1-neoforge.jar",
        "moogs_structures-neoforge-1.21.1-alpha-3.0.0.jar",
        "IllagerInvasion-v21.1.6-1.21.1-NeoForge.jar",
        "repurposed_structures-7.5.21+1.21.1-neoforge.jar",
        "worldweaver-21.0.24.jar",
    }
)
CLASSES = (
    "YungJigsawSinglePoolElement.class",
    "IASinglePoolElement.class",
    "VersionAwareSinglePoolElement.class",
    "MirroringSingleJigsawPiece.class",
    "SingleNoLiquidPoolElement.class",
    "LegacySingleNoLiquidPoolElement.class",
    "LegacyOceanBottomSinglePoolElement.class",
    "SingleEndPoolElement.class",
)
REGISTRATION_KEYS = (
    b"yung_single_element",
    b"integrated_api_single_pool_element",
    b"versioned_single_pool_element",
    b"mirroring_single_pool_element",
    b"single_end_pool_element",
    b"legacy_ocean_bottom_single_pool_element",
    b"single_pool_element",
)


def main() -> None:
    """Retain disassembly and exact class/archive identities for the observed custom types."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--output", type=Path, required=True)
    output = cast("Path", parser.parse_args().output)
    output.mkdir(parents=True, exist_ok=False)
    javap = ROOT / "downloads/item2/temurin/extracted/jdk-21.0.12.1+1/bin/javap"
    identities: list[dict[str, str]] = []
    for source in retained_sources(ROOT):
        if source.name not in ARCHIVES:
            continue
        if hashlib.sha256(source.path.read_bytes()).hexdigest() != source.sha256:
            message = f"custom pool source hash mismatch: {source.name}"
            raise ValueError(message)
        destination = output / source.name
        destination.mkdir()
        with ZipFile(source.path) as archive:
            for name in sorted(archive.namelist()):
                if not name.endswith(".class"):
                    continue
                payload = archive.read(name)
                if not name.endswith(CLASSES) and not any(
                    key in payload for key in REGISTRATION_KEYS
                ):
                    continue
                class_name = name.removesuffix(".class").replace("/", ".")
                result = subprocess.run(  # noqa: S603 - pinned javap and verified retained JAR.
                    [
                        str(javap),
                        "-p",
                        "-c",
                        "-constants",
                        "-classpath",
                        str(source.path),
                        class_name,
                    ],
                    check=True,
                    capture_output=True,
                )
                target = destination / f"{class_name}.txt"
                _ = target.write_bytes(result.stdout)
                identities.append(
                    {
                        "archive": source.name,
                        "archive_sha256": source.sha256,
                        "class": name,
                        "class_sha256": hashlib.sha256(payload).hexdigest(),
                        "disassembly": target.relative_to(output).as_posix(),
                        "disassembly_sha256": hashlib.sha256(result.stdout).hexdigest(),
                    }
                )
    _ = (output / "identities.json").write_text(
        json.dumps(identities, indent=2) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
