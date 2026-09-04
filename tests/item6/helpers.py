# pyright: standard
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from types import ModuleType

ROOT = Path(__file__).parents[2]
FROZEN = ROOT / "evidence/item-6/frozen"
MANIFEST = ROOT / "evidence/item-6/generated-config-manifest.json"
AUDIT = ROOT / "evidence/item-6/config-audit.json"

SPEC = importlib.util.spec_from_file_location(
    "freeze_item6_config", ROOT / "tools/freeze_item6_config.py"
)
assert SPEC is not None
assert SPEC.loader is not None
MODULE = ModuleType(SPEC.name)
SPEC.loader.exec_module(MODULE)
capture = MODULE.capture
validate = MODULE.validate


def write_audit(tmp_path: Path, audit: dict, name: str = "audit.json") -> Path:
    path = tmp_path / name
    path.write_text(json.dumps(audit), encoding="utf-8")
    return path
