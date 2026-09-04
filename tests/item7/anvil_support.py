from __future__ import annotations

import gzip
import struct
import zlib
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path

SECTOR_BYTES = 4096


@dataclass(frozen=True, slots=True)
class ChunkFixture:
    slot: int
    chunk_x: int
    chunk_z: int
    compression: int
    external: bool = False


def packed_values(values: tuple[int, ...], bits: int) -> list[int]:
    per_word = 64 // bits
    words = [0] * ((len(values) + per_word - 1) // per_word)
    for index, value in enumerate(values):
        words[index // per_word] |= value << ((index % per_word) * bits)
    return [word if word < 2**63 else word - 2**64 for word in words]


def named(name: str) -> bytes:
    encoded = name.encode()
    return struct.pack(">H", len(encoded)) + encoded


def tag(tag_id: int, name: str, payload: bytes) -> bytes:
    return bytes([tag_id]) + named(name) + payload


def compound(name: str, children: tuple[bytes, ...]) -> bytes:
    return tag(10, name, b"".join(children) + b"\x00")


def string(name: str, value: str) -> bytes:
    return tag(8, name, named(value))


def integer(name: str, value: int) -> bytes:
    return tag(3, name, struct.pack(">i", value))


def long_array(name: str, values: list[int]) -> bytes:
    return tag(12, name, struct.pack(">i", len(values)) + struct.pack(f">{len(values)}q", *values))


def list_tag(name: str, element_id: int, values: tuple[bytes, ...]) -> bytes:
    return tag(9, name, bytes([element_id]) + struct.pack(">i", len(values)) + b"".join(values))


def chunk_nbt(chunk_x: int, chunk_z: int) -> bytes:
    palette = list_tag(
        "palette",
        8,
        (named("minecraft:plains"), named("minecraft:forest")),
    )
    biomes = compound(
        "biomes",
        (
            palette,
            long_array("data", packed_values(tuple(index % 2 for index in range(64)), 1)),
        ),
    )
    section = tag(1, "Y", b"\x00") + biomes + b"\x00"
    box = tag(11, "BB", struct.pack(">i6i", 6, 0, 60, 0, 15, 80, 15))
    child = box + b"\x00"
    start = compound(
        "minecraft:village_plains",
        (
            string("id", "minecraft:village_plains"),
            list_tag("Children", 10, (child,)),
        ),
    )
    return compound(
        "",
        (
            integer("DataVersion", 3955),
            integer("xPos", chunk_x),
            integer("zPos", chunk_z),
            string("Status", "minecraft:full"),
            compound(
                "Heightmaps",
                (long_array("WORLD_SURFACE", packed_values((65,) * 256, 9)),),
            ),
            list_tag("sections", 10, (section,)),
            compound("structures", (compound("starts", (start,)),)),
        ),
    )


def lz4_stream(payload: bytes) -> bytes:
    extension_length = len(payload) - 15
    extensions = bytes([255]) * (extension_length // 255)
    extensions += bytes([extension_length % 255])
    compressed = bytes([0xF0]) + extensions + payload
    block = b"LZ4Block" + bytes([0x20])
    block += struct.pack("<III", len(compressed), len(payload), 0)
    return block + compressed + b"LZ4Block" + bytes(13)


def compressed(payload: bytes, method: int) -> bytes:
    compressors: dict[int, Callable[[bytes], bytes]] = {
        1: gzip.compress,
        2: zlib.compress,
        3: lambda value: value,
        4: lz4_stream,
    }
    try:
        return compressors[method](payload)
    except KeyError as error:
        raise AssertionError(method) from error


def write_region(path: Path, fixture: ChunkFixture) -> None:
    payload = compressed(chunk_nbt(fixture.chunk_x, fixture.chunk_z), fixture.compression)
    external_bit = 0x80 if fixture.external else 0
    stored = bytes([fixture.compression | external_bit])
    if fixture.external:
        _ = path.with_name(f"c.{fixture.chunk_x}.{fixture.chunk_z}.mcc").write_bytes(payload)
    else:
        stored += payload
    sector_count = (len(stored) + 4 + SECTOR_BYTES - 1) // SECTOR_BYTES
    header = bytearray(SECTOR_BYTES * 2)
    struct.pack_into(">I", header, fixture.slot * 4, (2 << 8) | sector_count)
    struct.pack_into(">I", header, SECTOR_BYTES + fixture.slot * 4, 123456)
    body = struct.pack(">I", len(stored)) + stored
    body += bytes(sector_count * SECTOR_BYTES - len(body))
    _ = path.write_bytes(header + body)
