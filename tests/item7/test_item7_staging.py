from __future__ import annotations

import os
import shutil
import subprocess
import time
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from tools.stage_item7_world import StageError, copy_world_boundary, stage

if TYPE_CHECKING:
    from collections.abc import Callable

ROOT = Path(__file__).parents[2]


def _world(root: Path) -> Path:
    world = root / "world"
    region = world / "region"
    region.mkdir(parents=True)
    _ = (world / "session.lock").write_bytes(b"lock")
    _ = (world / "level.dat").write_bytes(b"level")
    _ = (region / "r.0.0.mca").write_bytes(b"region")
    return world


def test_core_stage_uses_independent_files(tmp_path: Path) -> None:
    project = tmp_path / "project"
    raw = tmp_path / "raw"
    project.mkdir()
    raw.mkdir()
    source = raw / "evidence.json"
    _ = source.write_bytes(b"accepted")
    output = tmp_path / "stage"

    count, size = stage("core", project, raw, output)

    staged = output / source.name
    assert (count, size) == (1, len(b"accepted"))
    assert source.stat().st_ino != staged.stat().st_ino
    _ = source.write_bytes(b"mutated")
    assert staged.read_bytes() == b"accepted"


def test_world_stage_is_independent_and_excludes_session_lock(tmp_path: Path) -> None:
    instance = tmp_path / "instance"
    world = _world(instance)
    output = tmp_path / "stage/world"

    copy_world_boundary(instance, output)

    source = world / "region/r.0.0.mca"
    staged = output / "region/r.0.0.mca"
    assert source.stat().st_ino != staged.stat().st_ino
    assert not (output / "session.lock").exists()
    _ = source.write_bytes(b"mutated")
    assert staged.read_bytes() == b"region"


def test_world_stage_rejects_java_compatible_record_lock(tmp_path: Path) -> None:
    instance = tmp_path / "instance"
    world = _world(instance)
    ready = tmp_path / "ready"
    holder = subprocess.Popen(  # noqa: S603 - fixed repository lock helper.
        [  # noqa: S607 - uv resolves within the controlled test environment.
            "uv",
            "run",
            "python",
            str(ROOT / "tests/item7/lock_holder.py"),
            str(world / "session.lock"),
            str(ready),
        ],
        cwd=ROOT,
        stdin=subprocess.PIPE,
    )
    try:
        deadline = time.monotonic() + 5
        while not ready.exists() and time.monotonic() < deadline:
            time.sleep(0.01)
        assert ready.is_file()

        with pytest.raises(StageError, match="world is active"):
            copy_world_boundary(instance, tmp_path / "stage/world")
    finally:
        if holder.stdin is not None:
            _ = holder.stdin.write(b"x")
            holder.stdin.close()
        assert holder.wait(timeout=5) == 0


def test_shell_entrypoint_stages_core_boundary(tmp_path: Path) -> None:
    raw = tmp_path / "raw"
    raw.mkdir()
    _ = (raw / "evidence.json").write_bytes(b"accepted")
    output = tmp_path / "stage"

    result = subprocess.run(  # noqa: S603 - fixed repository staging tool.
        [  # noqa: S607 - bash resolves within the controlled test environment.
            "bash",
            str(ROOT / "tools/stage_item7_raw_evidence.sh"),
            "core",
            str(ROOT),
            str(raw),
            str(output),
        ],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert result.stdout == "staged 1 files using 8 bytes\n"
    assert (output / "evidence.json").read_bytes() == b"accepted"


def test_world_stage_pins_the_directory_that_owns_the_lock(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    instance = tmp_path / "instance"
    world = _world(instance)
    displaced = tmp_path / "locked-world"
    original_copy = shutil.copy2
    swapped = False

    def swap_before_copy(source: Path, destination: Path) -> Path:
        nonlocal swapped
        if not swapped:
            _ = world.rename(displaced)
            attacker = _world(instance)
            _ = (attacker / "level.dat").write_bytes(b"attacker")
            _ = (attacker / "region/r.0.0.mca").write_bytes(b"attacker-region")
            swapped = True
        return Path(original_copy(source, destination))

    monkeypatch.setattr(shutil, "copy2", swap_before_copy)
    output = tmp_path / "stage/world"

    copy_world_boundary(instance, output)

    assert (output / "level.dat").read_bytes() == b"level"
    assert (output / "region/r.0.0.mca").read_bytes() == b"region"


def test_core_stage_pins_the_validated_raw_root(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    project = tmp_path / "project"
    raw = tmp_path / "raw"
    displaced = tmp_path / "trusted-raw"
    project.mkdir()
    raw.mkdir()
    _ = (raw / "evidence.bin").write_bytes(b"trusted")
    original_copytree = shutil.copytree

    def swap_before_copy(
        source: Path,
        destination: Path,
        *,
        copy_function: Callable[[str, str], object],
        symlinks: bool,
    ) -> Path:
        _ = raw.rename(displaced)
        raw.mkdir()
        _ = (raw / "evidence.bin").write_bytes(b"attacker")
        return Path(
            original_copytree(
                source,
                destination,
                copy_function=copy_function,
                symlinks=symlinks,
            )
        )

    monkeypatch.setattr(shutil, "copytree", swap_before_copy)
    output = tmp_path / "stage"

    count, size = stage("core", project, raw, output)

    assert (count, size) == (1, len(b"trusted"))
    assert (output / "evidence.bin").read_bytes() == b"trusted"


def test_core_stage_rejects_hardlinked_source(tmp_path: Path) -> None:
    project = tmp_path / "project"
    raw = tmp_path / "raw"
    project.mkdir()
    raw.mkdir()
    source = raw / "evidence.bin"
    _ = source.write_bytes(b"trusted")
    os.link(source, tmp_path / "alias.bin")
    output = tmp_path / "stage"

    with pytest.raises(StageError, match="hardlink"):
        _ = stage("core", project, raw, output)

    assert not output.exists()


@pytest.mark.parametrize("mode", ["core", "world"])
def test_stage_rejects_special_files_without_partial_output(tmp_path: Path, mode: str) -> None:
    project = tmp_path / "project"
    raw = tmp_path / "raw"
    project.mkdir()
    raw.mkdir()
    if mode == "core":
        _ = (raw / "accepted").write_bytes(b"accepted")
        os.mkfifo(raw / "unsafe")
        output = tmp_path / "stage"
        with pytest.raises(StageError, match="regular"):
            _ = stage("core", project, raw, output)
    else:
        instance = tmp_path / "instance"
        world = _world(instance)
        (world / "level.dat").unlink()
        os.mkfifo(world / "level.dat")
        output = tmp_path / "stage/world"
        with pytest.raises(StageError, match="regular"):
            copy_world_boundary(instance, output)

    assert not output.exists()
