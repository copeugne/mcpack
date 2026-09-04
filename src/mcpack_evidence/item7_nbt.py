from __future__ import annotations

import struct
from collections.abc import Mapping
from dataclasses import dataclass

from .item7_nbt_models import (
    BiomeSection,
    ChunkRecord,
    ChunkSource,
    Heightmap,
    StructureBox,
    StructureStart,
)

__all__ = (
    "BiomeSection",
    "ChunkRecord",
    "ChunkSource",
    "Heightmap",
    "StructureBox",
    "StructureStart",
    "decode_chunk_nbt",
)


@dataclass(frozen=True, slots=True)
class _Compound:
    values: Mapping[str, _NbtValue]


@dataclass(frozen=True, slots=True)
class _NumberArray:
    tag_id: int
    values: tuple[int, ...]


type _NbtValue = int | float | str | bytes | _Compound | tuple[_NbtValue, ...] | _NumberArray


class NbtDecodeError(Exception):
    __slots__: tuple[()] = ()


def _require(data: memoryview, offset: int, size: int) -> None:
    if offset < 0 or size < 0 or offset + size > len(data):
        raise NbtDecodeError("truncated NBT payload")


def _integer(data: memoryview, offset: int, width: int, *, signed: bool = True) -> tuple[int, int]:
    _require(data, offset, width)
    return int.from_bytes(data[offset : offset + width], "big", signed=signed), offset + width


def _text(data: memoryview, offset: int) -> tuple[str, int]:
    length, offset = _integer(data, offset, 2, signed=False)
    _require(data, offset, length)
    try:
        encoded = bytes(data[offset : offset + length]).replace(b"\xc0\x80", b"\x00")
        code_units = encoded.decode("utf-8", errors="surrogatepass")
        value = code_units.encode("utf-16", errors="surrogatepass").decode("utf-16")
    except UnicodeError as error:
        raise NbtDecodeError("NBT string is not valid modified UTF-8") from error
    return value, offset + length


def _array(data: memoryview, offset: int, width: int) -> tuple[tuple[int, ...], int]:
    count, offset = _integer(data, offset, 4)
    if count < 0:
        raise NbtDecodeError("NBT array length is negative")
    values: list[int] = []
    for _ in range(count):
        value, offset = _integer(data, offset, width)
        values.append(value)
    return tuple(values), offset


def _payload(tag_id: int, data: memoryview, offset: int) -> tuple[_NbtValue, int]:
    if tag_id in {1, 2, 3, 4}:
        return _integer(data, offset, (1, 2, 4, 8)[tag_id - 1])
    if tag_id in {5, 6}:
        width = 4 if tag_id == 5 else 8
        _require(data, offset, width)
        fmt = ">f" if tag_id == 5 else ">d"
        return struct.unpack_from(fmt, data, offset)[0], offset + width
    if tag_id == 7:
        array_values, offset = _array(data, offset, 1)
        return bytes(value & 0xFF for value in array_values), offset
    if tag_id == 8:
        return _text(data, offset)
    if tag_id == 9:
        _require(data, offset, 1)
        element_id = data[offset]
        count, offset = _integer(data, offset + 1, 4)
        if count < 0 or (element_id == 0 and count != 0):
            raise NbtDecodeError("invalid NBT list header")
        list_values: list[_NbtValue] = []
        for _ in range(count):
            value, offset = _payload(element_id, data, offset)
            list_values.append(value)
        return tuple(list_values), offset
    if tag_id == 10:
        compound_values: dict[str, _NbtValue] = {}
        while True:
            _require(data, offset, 1)
            child_id = data[offset]
            offset += 1
            if child_id == 0:
                return _Compound(compound_values), offset
            name, offset = _text(data, offset)
            compound_values[name], offset = _payload(child_id, data, offset)
    if tag_id in {11, 12}:
        array_values, offset = _array(data, offset, 4 if tag_id == 11 else 8)
        return _NumberArray(tag_id, array_values), offset
    raise NbtDecodeError(f"unsupported NBT tag id: {tag_id}")


def _root(payload: bytes) -> _Compound:
    data = memoryview(payload)
    _require(data, 0, 1)
    if data[0] != 10:
        raise NbtDecodeError("NBT root tag is not a compound")
    _, offset = _text(data, 1)
    value, offset = _payload(10, data, offset)
    if not isinstance(value, _Compound) or offset != len(data):
        raise NbtDecodeError("NBT root payload has trailing bytes")
    return value


def _required_int(root: _Compound, name: str) -> int:
    value = root.values.get(name)
    if not isinstance(value, int):
        raise NbtDecodeError(f"NBT field {name} is not an integer")
    return value


def _required_text(root: _Compound, name: str) -> str:
    value = root.values.get(name)
    if not isinstance(value, str):
        raise NbtDecodeError(f"NBT field {name} is not a string")
    return value


def _packed(values: tuple[int, ...], size: int, bits: int) -> tuple[int, ...]:
    per_word = 64 // bits
    required = (size + per_word - 1) // per_word
    if len(values) < required:
        raise NbtDecodeError("packed NBT array is shorter than declared geometry")
    mask = (1 << bits) - 1
    return tuple(
        ((values[index // per_word] & ((1 << 64) - 1)) >> ((index % per_word) * bits)) & mask
        for index in range(size)
    )


def _heightmaps(root: _Compound, source: ChunkSource) -> tuple[Heightmap, ...]:
    value = root.values.get("Heightmaps")
    if value is None:
        return ()
    if not isinstance(value, _Compound):
        raise NbtDecodeError("NBT Heightmaps field is not a compound")
    bits = (source.build_height + 1).bit_length()
    rows: list[Heightmap] = []
    for name, raw in sorted(value.values.items()):
        if not isinstance(raw, _NumberArray) or raw.tag_id != 12:
            raise NbtDecodeError(f"heightmap {name} is not a long array")
        unpacked = _packed(raw.values, 256, bits)
        rows.append(Heightmap(name=name, values=tuple(v + source.min_y - 1 for v in unpacked)))
    return tuple(rows)


def _biomes(root: _Compound) -> tuple[BiomeSection, ...]:
    sections = root.values.get("sections")
    if sections is None:
        return ()
    if not isinstance(sections, tuple):
        raise NbtDecodeError("NBT sections field is not a list")
    rows: list[BiomeSection] = []
    for section in sections:
        if not isinstance(section, _Compound):
            raise NbtDecodeError("NBT section is not a compound")
        biomes = section.values.get("biomes")
        if biomes is None:
            continue
        if not isinstance(biomes, _Compound):
            raise NbtDecodeError("NBT section biomes field is not a compound")
        palette_value = biomes.values.get("palette")
        if not isinstance(palette_value, tuple):
            raise NbtDecodeError("NBT biome palette is not a list")
        if not all(isinstance(value, str) for value in palette_value):
            raise NbtDecodeError("NBT biome palette contains a non-string")
        palette = tuple(value for value in palette_value if isinstance(value, str))
        data = biomes.values.get("data")
        if data is None and len(palette) == 1:
            indices = (0,) * 64
        elif isinstance(data, _NumberArray) and data.tag_id == 12 and palette:
            indices = _packed(data.values, 64, max(1, (len(palette) - 1).bit_length()))
        else:
            raise NbtDecodeError("NBT biome data does not match its palette")
        rows.append(
            BiomeSection(section_y=_required_int(section, "Y"), palette=palette, indices=indices)
        )
    return tuple(sorted(rows, key=lambda row: row.section_y))


def _structures(root: _Compound) -> tuple[StructureStart, ...]:
    structures = root.values.get("structures")
    if structures is None:
        return ()
    if not isinstance(structures, _Compound):
        raise NbtDecodeError("NBT structures field is not a compound")
    starts = structures.values.get("starts")
    if not isinstance(starts, _Compound):
        raise NbtDecodeError("NBT structure starts field is not a compound")
    rows: list[StructureStart] = []
    for key, value in sorted(starts.values.items()):
        if not isinstance(value, _Compound):
            raise NbtDecodeError("NBT structure start is not a compound")
        start_id = _required_text(value, "id")
        if start_id == "INVALID":
            continue
        children = value.values.get("Children")
        if not isinstance(children, tuple):
            raise NbtDecodeError("NBT structure Children field is not a list")
        boxes: list[StructureBox] = []
        for child in children:
            if not isinstance(child, _Compound):
                raise NbtDecodeError("NBT structure child is not a compound")
            bounds = child.values.get("BB")
            if (
                not isinstance(bounds, _NumberArray)
                or bounds.tag_id != 11
                or len(bounds.values) != 6
            ):
                raise NbtDecodeError("NBT structure child BB is not a six-integer array")
            boxes.append(StructureBox(bounds=bounds.values))
        rows.append(StructureStart(structure_id=key, start_id=start_id, boxes=tuple(boxes)))
    return tuple(rows)


def decode_chunk_nbt(payload: bytes, source: ChunkSource) -> ChunkRecord:
    root = _root(payload)
    data_version = root.values.get("DataVersion")
    if data_version is not None and not isinstance(data_version, int):
        raise NbtDecodeError("NBT DataVersion field is not an integer")
    status = _required_text(root, "Status")
    return ChunkRecord(
        dimension=source.dimension,
        region=source.region,
        slot=source.slot,
        timestamp=source.timestamp,
        chunk_x=_required_int(root, "xPos"),
        chunk_z=_required_int(root, "zPos"),
        data_version=data_version,
        status=status,
        full=status == "minecraft:full",
        compression=source.compression,
        external=source.external,
        heightmaps=_heightmaps(root, source),
        biome_sections=_biomes(root),
        structure_starts=_structures(root),
    )
