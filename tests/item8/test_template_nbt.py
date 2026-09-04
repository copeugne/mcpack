from __future__ import annotations

import struct

import pytest

from mcpack_evidence.item7_nbt import NbtDecodeError, decode_compound_nbt
from tests.item7.anvil_support import compound, string, tag


def test_template_nbt_preserves_nested_compounds_and_arrays() -> None:
    body = compound(
        "",
        (
            tag(9, "size", b"\x03" + struct.pack(">iiii", 3, 4, 8, 12)),
            compound("entity", (string("id", "minecraft:zombie"),)),
            tag(11, "position", struct.pack(">iiii", 3, -1, 64, 2)),
            tag(7, "bytes", struct.pack(">i", 2) + b"\x00\xff"),
        ),
    )
    assert decode_compound_nbt(body) == {
        "size": [4, 8, 12],
        "entity": {"id": "minecraft:zombie"},
        "position": [-1, 64, 2],
        "bytes": [0, 255],
    }


def test_template_decoder_rejects_truncated_or_trailing_bytes() -> None:
    for payload in (b"\x0a\x00\x00", b"\x0a\x00\x00\x00extra"):
        with pytest.raises(NbtDecodeError):
            _ = decode_compound_nbt(payload)
