from __future__ import annotations

import shlex
import sys
from textwrap import dedent
from typing import TYPE_CHECKING

import pytest

from mcpack_evidence import item8_registry
from mcpack_evidence.item8_registry import REGISTRIES, read_registry, run_registry_lifecycle

if TYPE_CHECKING:
    from collections.abc import Callable
    from pathlib import Path


@pytest.fixture
def fake_java(tmp_path: Path) -> Callable[[str], Path]:
    def build(mode: str) -> Path:
        source = tmp_path / "fake_server.py"
        _ = source.write_text(
            dedent(f"""\
                import sys, time
                mode = {mode!r}
                print('[Server thread/INFO]: Done (1.0s)! For help, type "help"', flush=True)
                print('[Server thread/INFO]: Saved the game', flush=True)
                for line in sys.stdin:
                    command = line.strip()
                    if command.startswith('neoforge dump registry '):
                        if mode == 'eof': sys.exit(0)
                        if mode == 'silent': time.sleep(30)
                        registry = command.split()[3]
                        text = f"New file created with {{registry}} registry's contents is at x"
                        print(text, flush=True)
                    elif command.startswith('say '):
                        print('[Server] ' + command[4:], flush=True)
                    elif command == 'save-all flush':
                        print('Saving the game', flush=True)
                        print('Saved the game', flush=True)
                    elif command == 'stop':
                        print('last shutdown diagnostic', flush=True)
                        sys.exit(3 if mode == 'bad-exit' else 0)
                """),
            encoding="utf-8",
        )
        java = tmp_path / "java"
        _ = java.write_text(
            f"#!/bin/sh\nexec {shlex.quote(sys.executable)} {shlex.quote(str(source))}\n",
            encoding="utf-8",
        )
        java.chmod(0o700)
        return java

    return build


def test_capture_waits_for_all_dumps_and_correlated_flush(
    tmp_path: Path, fake_java: Callable[[str], Path]
) -> None:
    log = tmp_path / "console.log"
    result = run_registry_lifecycle(tmp_path, fake_java("pass"), log, 5)
    assert result.clean_stop
    assert not result.process_group_killed
    assert result.completed_registries == REGISTRIES
    assert result.commands[:7] == tuple(
        f"neoforge dump registry {registry} true false" for registry in REGISTRIES
    )
    assert result.commands[7].startswith("say mcpack-item7-flush-")
    assert result.commands[8] == "save-all flush"
    assert result.commands[-1] == "stop"
    assert "last shutdown diagnostic" in log.read_text()


@pytest.mark.parametrize("mode", ["eof", "bad-exit"])
def test_capture_rejects_early_eof_and_unclean_exit(
    tmp_path: Path, fake_java: Callable[[str], Path], mode: str
) -> None:
    result = run_registry_lifecycle(tmp_path, fake_java(mode), tmp_path / "console.log", 5)
    assert not result.clean_stop
    assert result.rejection_reason


def test_silent_server_timeout_kills_process_group(
    tmp_path: Path, fake_java: Callable[[str], Path]
) -> None:
    result = run_registry_lifecycle(tmp_path, fake_java("silent"), tmp_path / "console.log", 1)
    assert not result.clean_stop
    assert result.process_group_killed
    assert result.return_code != 0
    assert result.rejection_reason == "registry capture or clean shutdown timed out"


def test_existing_console_log_is_preserved(tmp_path: Path) -> None:
    log = tmp_path / "console.log"
    _ = log.write_text("preserved", encoding="utf-8")
    with pytest.raises(FileExistsError):
        _ = run_registry_lifecycle(tmp_path, tmp_path / "missing-java", log, 1)
    assert log.read_text() == "preserved"


@pytest.mark.parametrize("content", ["", "a:b\na:b\n", "z:b\na:b\n", "bad id\n", "4 - a:b\n"])
def test_registry_rejects_incomplete_or_ambiguous_keys(tmp_path: Path, content: str) -> None:
    path = tmp_path / "registry.txt"
    _ = path.write_text(content, encoding="utf-8")
    with pytest.raises(ValueError, match="invalid registry"):
        _ = read_registry(path)


def test_registry_preserves_namespaced_keys(tmp_path: Path) -> None:
    path = tmp_path / "registry.txt"
    _ = path.write_text("a:one\nb:two/variant\n", encoding="utf-8")
    assert read_registry(path) == ("a:one", "b:two/variant")
    assert item8_registry.registry_relative_path("minecraft:worldgen/structure") == (
        "dumps/registry/minecraft/worldgen_structure.txt"
    )


def test_registry_path_rejects_undeclared_input() -> None:
    with pytest.raises(ValueError, match="undeclared registry"):
        _ = item8_registry.registry_relative_path("../elsewhere")
