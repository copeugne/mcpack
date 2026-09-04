# pyright: standard
"""Preflight, path safety, and collision tests for Item 6 capture."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest

from tests.item6.capture_fixtures import _make_instance
from tests.item6.helpers import capture


@pytest.mark.parametrize(
    "relative",
    [
        Path("config"),
        Path("defaultconfigs"),
        Path("world"),
        Path("world/serverconfig"),
        Path("server.properties"),
    ],
)
def test_capture_creates_no_output_when_required_source_is_missing(
    tmp_path: Path, relative: Path
) -> None:
    """A missing required source is rejected before capture creates the target."""
    # Given: one otherwise-valid instance lacks an exact required source.
    instance = _make_instance(tmp_path)
    source = instance / relative
    if source.is_dir():
        shutil.rmtree(source)
    else:
        source.unlink()
    output = tmp_path / "output"

    # When/Then: capture rejects it and leaves no output directory behind.
    with pytest.raises(ValueError, match="required"):
        capture(instance, output)
    assert not output.exists()


@pytest.mark.parametrize(
    "relative",
    [
        Path("config"),
        Path("defaultconfigs"),
        Path("world"),
        Path("world/serverconfig"),
    ],
)
def test_capture_rejects_required_directory_that_is_a_regular_file(
    tmp_path: Path, relative: Path
) -> None:
    """Required capture directories must be directories, not files."""
    # Given: one required directory is replaced with a regular file.
    instance = _make_instance(tmp_path)
    source = instance / relative
    shutil.rmtree(source)
    source.write_text("not a directory\n", encoding="utf-8")
    output = tmp_path / "output"

    # When/Then: capture rejects it before creating the output.
    with pytest.raises(ValueError, match="required directory"):
        capture(instance, output)
    assert not output.exists()


@pytest.mark.parametrize(
    "relative",
    [
        Path("config"),
        Path("defaultconfigs"),
        Path("world"),
        Path("world/serverconfig"),
    ],
)
def test_capture_rejects_required_directory_symlink(tmp_path: Path, relative: Path) -> None:
    """Required capture directories must not resolve through symlinks."""
    # Given: one required directory is replaced by a link to a real directory.
    instance = _make_instance(tmp_path)
    source = instance / relative
    shutil.rmtree(source)
    target = tmp_path / f"target-{relative.name}"
    target.mkdir()
    source.symlink_to(target, target_is_directory=True)
    output = tmp_path / "output"

    # When/Then: capture rejects the symlink before creating the output.
    with pytest.raises(ValueError, match="symlink"):
        capture(instance, output)
    assert not output.exists()


def test_capture_rejects_non_directory_instance(tmp_path: Path) -> None:
    """The capture root itself must be a real directory."""
    # Given: the instance argument names a regular file.
    instance = tmp_path / "instance"
    instance.write_text("not an instance\n", encoding="utf-8")
    output = tmp_path / "output"

    # When/Then: capture fails without creating the output.
    with pytest.raises(ValueError, match="instance"):
        capture(instance, output)
    assert not output.exists()


def test_capture_rejects_symlinked_instance(tmp_path: Path) -> None:
    """The capture root itself must not resolve through a symlink."""
    # Given: the instance argument is a symlink to a valid source tree.
    target = _make_instance(tmp_path)
    instance = tmp_path / "linked-instance"
    instance.symlink_to(target, target_is_directory=True)
    output = tmp_path / "output"

    # When/Then: capture rejects the link without creating the output.
    with pytest.raises(ValueError, match="non-symlink"):
        capture(instance, output)
    assert not output.exists()


@pytest.mark.parametrize("variant", ["missing", "directory", "symlink"])
def test_capture_rejects_invalid_server_properties(tmp_path: Path, variant: str) -> None:
    """Server properties must be a real regular file before capture starts."""
    # Given: server.properties has one invalid source shape.
    instance = _make_instance(tmp_path)
    source = instance / "server.properties"
    source.unlink()
    match variant:
        case "missing":
            pass
        case "directory":
            source.mkdir()
        case "symlink":
            target = tmp_path / "server.properties"
            target.write_text("level-name=linked\n", encoding="utf-8")
            source.symlink_to(target)
        case unreachable:
            pytest.fail(f"unexpected variant: {unreachable}")
    output = tmp_path / "output"

    # When/Then: capture rejects it before creating output.
    with pytest.raises(ValueError, match=r"server\.properties"):
        capture(instance, output)
    assert not output.exists()


def test_capture_preserves_existing_output_bytes(tmp_path: Path) -> None:
    """An existing target remains byte-identical on collision."""
    # Given: a valid instance and a pre-existing output sentinel.
    instance = _make_instance(tmp_path)
    output = tmp_path / "output"
    output.mkdir()
    sentinel = output / "sentinel.bin"
    sentinel.write_bytes(b"existing evidence\x00")

    # When/Then: collision fails and the existing target is untouched.
    with pytest.raises(FileExistsError, match="output already exists"):
        capture(instance, output)
    assert sentinel.read_bytes() == b"existing evidence\x00"
    assert sorted(path.name for path in output.iterdir()) == ["sentinel.bin"]


def test_capture_rejects_parent_traversal_before_collision(tmp_path: Path) -> None:
    instance = _make_instance(tmp_path)
    victim = tmp_path / "victim"
    victim.mkdir()
    output = tmp_path / "new-parent" / ".." / "victim"

    with pytest.raises(ValueError, match="parent traversal"):
        capture(instance, output)
    assert victim.is_dir()
    assert not tuple(victim.iterdir())
    assert not (tmp_path / "new-parent").exists()
    assert not (tmp_path / "config-sanitization.json").exists()


def test_capture_rejects_output_that_aliases_sanitization_receipt(tmp_path: Path) -> None:
    """The capture directory and adjacent receipt must be distinct paths."""
    # Given: the requested output has the fixed receipt filename.
    instance = _make_instance(tmp_path)
    output = tmp_path / "config-sanitization.json"

    # When/Then: aliasing fails before either artifact is created.
    with pytest.raises(ValueError, match="collides with sanitization receipt"):
        capture(instance, output)
    assert not output.exists()


@pytest.mark.parametrize("target_name", ["output", "config-sanitization.json"])
def test_capture_preserves_dangling_target_symlink(tmp_path: Path, target_name: str) -> None:
    instance = _make_instance(tmp_path)
    output = tmp_path / "output"
    target = tmp_path / target_name
    target.symlink_to("missing-target")

    with pytest.raises(FileExistsError, match="already exists"):
        capture(instance, output)
    assert target.is_symlink()
    assert target.readlink() == Path("missing-target")
    assert not tuple(tmp_path.glob(".*.capture-*"))


@pytest.mark.parametrize("relative", [Path("captured"), Path("config/captured")])
def test_capture_rejects_output_within_source_instance(tmp_path: Path, relative: Path) -> None:
    instance = _make_instance(tmp_path)
    output = instance / relative
    before = {
        path.relative_to(instance): path.read_bytes()
        for path in instance.rglob("*")
        if path.is_file()
    }

    with pytest.raises(ValueError, match="outside the source instance"):
        capture(instance, output)
    after = {
        path.relative_to(instance): path.read_bytes()
        for path in instance.rglob("*")
        if path.is_file()
    }
    assert after == before
    assert not output.exists()


@pytest.mark.parametrize("nested", [False, True])
def test_capture_rejects_symlinked_output_parent_before_staging(
    tmp_path: Path, nested: bool
) -> None:
    """A lexical output parent must never resolve through an external symlink."""
    # Given: the requested output parent or one of its lexical parents links externally.
    instance = _make_instance(tmp_path)
    external = tmp_path / "external"
    external.mkdir()
    linked_parent = tmp_path / "linked-output-parent"
    linked_parent.symlink_to(external, target_is_directory=True)
    output = (
        linked_parent / "captured"
        if not nested
        else linked_parent / "nested-output-parent" / "captured"
    )

    # When: capture preflights the user-controlled output location.
    with pytest.raises(ValueError, match="output parent"):
        capture(instance, output)

    # Then: no staging directory, output, or receipt can be materialized externally.
    assert not (external / "captured").exists()
    assert not (external / "nested-output-parent").exists()
    assert not (external / "config-sanitization.json").exists()


@pytest.mark.parametrize(
    "relative",
    [Path("config"), Path("defaultconfigs"), Path("world/serverconfig")],
)
def test_capture_rejects_nested_symlink_before_creating_output(
    tmp_path: Path, relative: Path
) -> None:
    """Copied source trees must not contain nested symlink entries."""
    # Given: one copied source tree contains a symlink to an external regular file.
    instance = _make_instance(tmp_path)
    target = tmp_path / f"external-{relative.name}.txt"
    target.write_text("external=value\n", encoding="utf-8")
    (instance / relative / "linked.txt").symlink_to(target)
    output = tmp_path / "output"

    # When/Then: capture rejects the tree and leaves no partial output behind.
    with pytest.raises(ValueError, match="symlink"):
        capture(instance, output)
    assert not output.exists()
