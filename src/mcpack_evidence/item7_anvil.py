from __future__ import annotations

import gzip
import re
import struct
import zlib
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import BinaryIO, Final, Literal, final, override

from mcpack_evidence.item7_nbt import (
    ChunkRecord,
    ChunkSource,
    NbtDecodeError,
    decode_chunk_nbt,
)

type CompressionName = Literal["gzip", "zlib", "raw", "lz4"]

_SECTOR_BYTES: Final = 4096
_HEADER_BYTES: Final = _SECTOR_BYTES * 2
_REGION_NAME: Final = re.compile(r"^r\.(-?\d+)\.(-?\d+)\.mca$")
_COMPRESSION_NAMES: Final[dict[int, CompressionName]] = {
    1: "gzip",
    2: "zlib",
    3: "raw",
    4: "lz4",
}


@final
class RegionDecodeError(Exception):
    __slots__ = ("path", "reason", "slot")

    def __init__(self, path: Path, slot: int | None, reason: str) -> None:
        super().__init__(reason)
        self.path = path
        self.slot = slot
        self.reason = reason

    @override
    def __str__(self) -> str:
        location = self.path.as_posix()
        if self.slot is not None:
            location = f"{location} slot {self.slot}"
        return f"{location}: {self.reason}"


@dataclass(frozen=True, slots=True)
class RegionContext:
    dimension: str
    relative_path: str
    min_y: int
    build_height: int


@dataclass(frozen=True, slots=True)
class _Slot:
    index: int
    sector_offset: int
    sector_count: int
    timestamp: int


def _fail(path: Path, slot: int | None, reason: str) -> RegionDecodeError:
    return RegionDecodeError(path=path, slot=slot, reason=reason)


def _region_coordinates(path: Path) -> tuple[int, int]:
    match = _REGION_NAME.fullmatch(path.name)
    if match is None:
        raise _fail(path, None, "region filename does not contain signed coordinates")
    return int(match.group(1)), int(match.group(2))


def _slots(path: Path, stream: BinaryIO) -> tuple[_Slot, ...]:
    size = path.stat().st_size
    if size == 0:
        return ()
    if size < _HEADER_BYTES or size % _SECTOR_BYTES != 0:
        raise _fail(path, None, "region size is not a complete Anvil sector sequence")
    header = stream.read(_HEADER_BYTES)
    if len(header) != _HEADER_BYTES:
        raise _fail(path, None, "region header is truncated")
    sector_total = size // _SECTOR_BYTES
    occupied = {0, 1}
    rows: list[_Slot] = []
    for index in range(1024):
        location = int.from_bytes(header[index * 4 : index * 4 + 4], "big")
        if location == 0:
            continue
        sector_offset = location >> 8
        sector_count = location & 0xFF
        if sector_offset < 2 or sector_count == 0 or sector_offset + sector_count > sector_total:
            raise _fail(path, index, "slot extent lies outside the region file")
        sectors = set(range(sector_offset, sector_offset + sector_count))
        if occupied & sectors:
            raise _fail(path, index, "slot sectors overlap another allocation")
        occupied.update(sectors)
        timestamp_offset = _SECTOR_BYTES + index * 4
        timestamp = int.from_bytes(header[timestamp_offset : timestamp_offset + 4], "big")
        rows.append(_Slot(index, sector_offset, sector_count, timestamp))
    return tuple(rows)


def _lz4_length(payload: bytes, offset: int, initial: int) -> tuple[int, int]:
    length = initial
    if initial != 15:
        return length, offset
    while True:
        if offset >= len(payload):
            raise NbtDecodeError("truncated LZ4 length extension")
        extension = payload[offset]
        offset += 1
        length += extension
        if extension != 255:
            return length, offset


def _lz4_block(payload: bytes, expected_size: int) -> bytes:
    output = bytearray()
    offset = 0
    while offset < len(payload):
        token = payload[offset]
        offset += 1
        literal_length, offset = _lz4_length(payload, offset, token >> 4)
        literal_end = offset + literal_length
        if literal_end > len(payload):
            raise NbtDecodeError("truncated LZ4 literal sequence")
        output.extend(payload[offset:literal_end])
        offset = literal_end
        if offset == len(payload):
            break
        if offset + 2 > len(payload):
            raise NbtDecodeError("truncated LZ4 match offset")
        match_offset = int.from_bytes(payload[offset : offset + 2], "little")
        offset += 2
        if match_offset == 0 or match_offset > len(output):
            raise NbtDecodeError("invalid LZ4 match offset")
        match_length, offset = _lz4_length(payload, offset, token & 0x0F)
        for _ in range(match_length + 4):
            output.append(output[-match_offset])
    if len(output) != expected_size:
        raise NbtDecodeError("LZ4 block decompressed to the wrong size")
    return bytes(output)


def _lz4_stream(payload: bytes) -> bytes:
    output = bytearray()
    offset = 0
    while True:
        if offset + 21 > len(payload) or payload[offset : offset + 8] != b"LZ4Block":
            raise NbtDecodeError("invalid LZ4 block stream header")
        token = payload[offset + 8]
        compressed_size, raw_size, _checksum = struct.unpack_from("<III", payload, offset + 9)
        offset += 21
        if compressed_size == raw_size == 0:
            if offset != len(payload):
                raise NbtDecodeError("LZ4 block stream has trailing bytes")
            return bytes(output)
        end = offset + compressed_size
        if end > len(payload):
            raise NbtDecodeError("truncated LZ4 block stream")
        method = token & 0xF0
        if method == 0x10:
            block = payload[offset:end]
            if len(block) != raw_size:
                raise NbtDecodeError("raw LZ4 block has the wrong size")
        elif method == 0x20:
            block = _lz4_block(payload[offset:end], raw_size)
        else:
            raise NbtDecodeError(f"unsupported LZ4 block method: {method:#x}")
        output.extend(block)
        offset = end


def _decompress(name: CompressionName, payload: bytes) -> bytes:
    try:
        if name == "gzip":
            return gzip.decompress(payload)
        if name == "zlib":
            return zlib.decompress(payload)
        if name == "raw":
            return payload
        return _lz4_stream(payload)
    except (gzip.BadGzipFile, EOFError, zlib.error) as error:
        raise NbtDecodeError(f"invalid {name} chunk payload") from error


def _context(path: Path) -> RegionContext:
    return RegionContext("minecraft:overworld", path.name, -64, 384)


def _chunk_payload(
    path: Path, stream: BinaryIO, slot: _Slot
) -> tuple[bytes, CompressionName, bool]:
    _ = stream.seek(slot.sector_offset * _SECTOR_BYTES)
    prefix = stream.read(5)
    if len(prefix) != 5:
        raise _fail(path, slot.index, "chunk header is truncated")
    length = int.from_bytes(prefix[:4], "big")
    if length < 1 or length + 4 > slot.sector_count * _SECTOR_BYTES:
        raise _fail(path, slot.index, "chunk length exceeds its slot allocation")
    compression_id = prefix[4] & 0x7F
    name = _COMPRESSION_NAMES.get(compression_id)
    if name is None:
        raise _fail(path, slot.index, f"unsupported chunk compression id: {compression_id}")
    external = bool(prefix[4] & 0x80)
    if external:
        if length != 1:
            raise _fail(path, slot.index, "external chunk slot contains inline bytes")
        region_x, region_z = _region_coordinates(path)
        chunk_x = region_x * 32 + slot.index % 32
        chunk_z = region_z * 32 + slot.index // 32
        external_path = path.with_name(f"c.{chunk_x}.{chunk_z}.mcc")
        try:
            payload = external_path.read_bytes()
        except FileNotFoundError as error:
            reason = f"external chunk file is missing: {external_path.name}"
            raise _fail(path, slot.index, reason) from error
    else:
        payload = stream.read(length - 1)
        if len(payload) != length - 1:
            raise _fail(path, slot.index, "chunk payload is truncated")
    try:
        return _decompress(name, payload), name, external
    except NbtDecodeError as error:
        raise _fail(path, slot.index, str(error)) from error


def decode_region(path: Path, context: RegionContext | None = None) -> Iterator[ChunkRecord]:
    resolved_context = context or _context(path)
    region_x, region_z = _region_coordinates(path)
    with path.open("rb") as stream:
        slots = _slots(path, stream)
        for slot in slots:
            payload, compression, external = _chunk_payload(path, stream, slot)
            source = ChunkSource(
                dimension=resolved_context.dimension,
                region=resolved_context.relative_path,
                slot=slot.index,
                timestamp=slot.timestamp,
                compression=compression,
                external=external,
                min_y=resolved_context.min_y,
                build_height=resolved_context.build_height,
            )
            try:
                record = decode_chunk_nbt(payload, source)
            except NbtDecodeError as error:
                raise _fail(path, slot.index, str(error)) from error
            expected_x = region_x * 32 + slot.index % 32
            expected_z = region_z * 32 + slot.index // 32
            if (record.chunk_x, record.chunk_z) != (expected_x, expected_z):
                raise _fail(path, slot.index, "chunk coordinates disagree with the region slot")
            yield record


def world_regions(world: Path) -> tuple[tuple[Path, RegionContext], ...]:
    rows: list[tuple[Path, RegionContext]] = []
    for path in sorted(world.rglob("*.mca")):
        if path.parent.name != "region":
            continue
        relative = path.relative_to(world).as_posix()
        parts = path.relative_to(world).parts
        if parts[0] == "DIM-1":
            dimension, min_y, height = "minecraft:the_nether", 0, 256
        elif parts[0] == "DIM1":
            dimension, min_y, height = "minecraft:the_end", 0, 256
        else:
            dimension, min_y, height = "minecraft:overworld", -64, 384
        rows.append((path, RegionContext(dimension, relative, min_y, height)))
    return tuple(rows)
