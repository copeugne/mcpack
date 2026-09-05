from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import cast


def test_desert_pyramid_callback_binds_the_frozen_piece() -> None:
    root = Path("evidence/item-8/sources/vanilla-desert-pyramid-binding-code")
    raw = (root / "identities.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == (
        "f83997815e0225442cdcd1819b3b7b1c210c8296da1b22191c7bba31df5e3b1c"
    )
    entries = cast("list[dict[str, str]]", json.loads(raw))
    code: dict[str, str] = {}
    for entry in entries:
        payload = (root / entry["disassembly"]).read_bytes()
        assert hashlib.sha256(payload).hexdigest() == entry["disassembly_sha256"]
        code[entry["class"].rsplit("/", 1)[1]] = payload.decode()
    original = Path("evidence/item-8/sources/vanilla-desert-pyramid-code/identities.json")
    assert hashlib.sha256(original.read_bytes()).hexdigest() == (
        "89770d3b09f15c47e801b2889bf431d3f5e823c047cc8025c1fd433932e405d9"
    )
    previous = cast("list[dict[str, str]]", json.loads(original.read_bytes()))
    structure = next(e for e in entries if e["class"].endswith("/DesertPyramidStructure.class"))
    old = next(e for e in previous if e["class"] == structure["class"])
    assert structure["class_sha256"] == old["class_sha256"]
    assert structure["archive_sha256"] == old["archive_sha256"]
    bootstrap = code["DesertPyramidStructure.class"].split("BootstrapMethods:", 1)[1]
    first = bootstrap.split("\n  1:", 1)[0]
    assert (
        'REF_newInvokeSpecial net/minecraft/world/level/levelgen/structure/structures/'
        'DesertPyramidPiece."<init>":(Lnet/minecraft/util/RandomSource;II)V'
    ) in first
    assert "InvokeDynamic #0:construct:" in code["DesertPyramidStructure.class"]
    assert "SinglePieceStructure$PieceConstructor.construct:" in code["SinglePieceStructure.class"]
