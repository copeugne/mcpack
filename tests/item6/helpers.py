# pyright: standard
from __future__ import annotations

import importlib.util
import json
import shutil
from dataclasses import dataclass
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).parents[2]
FROZEN = ROOT / "evidence/item-6/frozen"
MANIFEST = ROOT / "evidence/item-6/generated-config-manifest.json"
AUDIT = ROOT / "evidence/item-6/config-audit.json"
LIFECYCLE = ROOT / "evidence/item-6/first-boot-lifecycle.json"
MATERIALIZATION = ROOT / "evidence/item-6/materialization.json"
RETAINED = ROOT / "evidence/item-3/runtime/retained-server-candidates.txt"

SPEC = importlib.util.spec_from_file_location(
    "freeze_item6_config", ROOT / "tools/freeze_item6_config.py"
)
assert SPEC is not None
assert SPEC.loader is not None
MODULE = ModuleType(SPEC.name)
SPEC.loader.exec_module(MODULE)
capture = MODULE.capture
validate = MODULE.validate


@dataclass(frozen=True, slots=True)
class Item6RepositoryFixture:
    """Paths for one repository-shaped mutable Item 6 validation fixture."""

    root: Path
    frozen: Path
    manifest: Path
    audit: Path
    lifecycle: Path
    materialization: Path
    retained: Path


def copy_item6_repository(tmp_path: Path) -> Item6RepositoryFixture:
    """Copy the bound Item 6 inputs into their canonical repository paths."""
    repository = tmp_path / "repository"
    frozen = repository / "evidence/item-6/frozen"
    shutil.copytree(FROZEN, frozen)
    manifest = repository / "evidence/item-6/generated-config-manifest.json"
    audit = repository / "evidence/item-6/config-audit.json"
    lifecycle = repository / "evidence/item-6/first-boot-lifecycle.json"
    materialization = repository / "evidence/item-6/materialization.json"
    retained = repository / "evidence/item-3/runtime/retained-server-candidates.txt"
    retained.parent.mkdir(parents=True)
    for source, destination in (
        (MANIFEST, manifest),
        (AUDIT, audit),
        (LIFECYCLE, lifecycle),
        (MATERIALIZATION, materialization),
        (RETAINED, retained),
    ):
        _ = shutil.copy2(source, destination)
    return Item6RepositoryFixture(
        root=repository,
        frozen=frozen,
        manifest=manifest,
        audit=audit,
        lifecycle=lifecycle,
        materialization=materialization,
        retained=retained,
    )


def rebind_audit(fixture: Item6RepositoryFixture) -> None:
    """Bind a copied audit to the current copied manifest bytes."""
    audit = json.loads(fixture.audit.read_text(encoding="utf-8"))
    audit["configuration_identity"] = f"sha256:{MODULE.sha256(fixture.manifest)}"
    fixture.audit.write_text(json.dumps(audit), encoding="utf-8")


def write_audit(tmp_path: Path, audit: dict, name: str = "audit.json") -> Path:
    path = tmp_path / name
    path.write_text(json.dumps(audit), encoding="utf-8")
    return path
