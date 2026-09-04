# pyright: standard
"""Contract tests for the Item 6 source-capture boundary."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from tests.item6.helpers import ROOT, capture


def _make_instance(tmp_path: Path) -> Path:
    """Create a complete minimal source instance for capture tests."""
    instance = tmp_path / "instance"
    for directory, payload in (
        (instance / "config", "config=value\n"),
        (instance / "defaultconfigs", "defaults=value\n"),
        (instance / "world" / "serverconfig", "world=value\n"),
    ):
        directory.mkdir(parents=True)
        (directory / "settings.txt").write_text(payload, encoding="utf-8")
    (instance / "server.properties").write_text("level-name=world\n", encoding="utf-8")
    return instance


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
    with pytest.raises(ValueError, match="non-symlink"):
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


def test_capture_cli_writes_exact_public_layout(tmp_path: Path) -> None:
    """The public CLI captures all and only the documented layout."""
    # Given: a valid source instance and absent target.
    instance = _make_instance(tmp_path)
    output = tmp_path / "captured"

    # When: the public command-line interface captures the source.
    completed = subprocess.run(  # noqa: S603
        (
            sys.executable,
            "tools/freeze_item6_config.py",
            "capture",
            "--instance",
            str(instance),
            "--output",
            str(output),
        ),
        check=False,
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    # Then: the command succeeds with exactly the public output inventory.
    assert completed.returncode == 0, completed.stderr
    assert sorted(
        path.relative_to(output).as_posix() for path in output.rglob("*") if path.is_file()
    ) == [
        "config/settings.txt",
        "defaultconfigs/settings.txt",
        "server.properties",
        "world-serverconfig/settings.txt",
    ]
