# pyright: standard
"""Contract tests for the Item 6 source-capture boundary."""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from tests.item6.helpers import ROOT, capture

_REDACTION_SENTINEL = "<redacted-generated-secret>"
_TEST_SOURCE_VALUE = "test-only-source-value"


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
    (instance / "config" / "resourceful-config-web.json").write_text(
        json.dumps(
            {
                "enabled": False,
                "port": 8080,
                "validator": {
                    "if": {
                        "password": _TEST_SOURCE_VALUE,
                        "type": "uuid",
                        "uuids": [],
                    },
                    "type": "if",
                },
            }
        ),
        encoding="utf-8",
    )
    (instance / "server.properties").write_text("level-name=world\n", encoding="utf-8")
    return instance


def _write_resourceful_config(instance: Path, payload: bytes) -> None:
    """Replace the capture source config with exact bytes for boundary tests."""
    _ = (instance / "config" / "resourceful-config-web.json").write_bytes(payload)


def test_capture_redacts_generated_credential_and_writes_safe_receipt(tmp_path: Path) -> None:
    """Capture substitutes the generated credential before evidence exists."""
    # Given: a complete source instance with the generated web-validator credential.
    instance = _make_instance(tmp_path)
    output = tmp_path / "output"
    receipt_path = tmp_path / "config-sanitization.json"

    # When: the capture boundary materializes frozen configuration evidence.
    capture(instance, output)

    # Then: a receipt exists before inspecting the redacted configuration payload.
    assert receipt_path.is_file()
    captured = json.loads(
        (output / "config" / "resourceful-config-web.json").read_text(encoding="utf-8")
    )
    expected = json.loads(
        (instance / "config" / "resourceful-config-web.json").read_text(encoding="utf-8")
    )
    expected["validator"]["if"]["password"] = _REDACTION_SENTINEL
    assert captured == expected
    assert captured["validator"]["if"]["password"] == _REDACTION_SENTINEL
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    assert receipt == {
        "files": [
            {
                "path": "config/resourceful-config-web.json",
                "redactions": [
                    {
                        "json_pointer": "/validator/if/password",
                        "replacement": _REDACTION_SENTINEL,
                        "value_type": "string",
                    }
                ],
            }
        ],
        "redaction_count": 1,
        "sanitized_file_count": 1,
        "schema_version": "item6-config-sanitization-v1",
    }
    receipt_text = receipt_path.read_text(encoding="utf-8")
    captured_text = (output / "config" / "resourceful-config-web.json").read_text(encoding="utf-8")
    captured_file_contents = tuple(
        path.read_text(encoding="utf-8") for path in output.rglob("*") if path.is_file()
    )
    assert all(_TEST_SOURCE_VALUE not in content for content in captured_file_contents)
    assert _TEST_SOURCE_VALUE not in captured_text
    assert _TEST_SOURCE_VALUE not in receipt_text
    assert "hash" not in receipt_text


def test_capture_surgically_replaces_only_credential_json_string_bytes(tmp_path: Path) -> None:
    """Capture preserves each verified source byte outside the target string token."""
    # Given: a valid configuration whose deliberate whitespace and key order are evidence bytes.
    instance = _make_instance(tmp_path)
    source = (
        b"{\r\n"
        b'  "untouched" : [ 1, 2.5, true ],\r\n'
        b'  "validator" : { "type" : "if", "if" : {\r\n'
        b'    "uuids" : [], "password" : "test-only-source-value", "type" : "uuid"\r\n'
        b"  } }\r\n"
        b"}\r\n"
    )
    _write_resourceful_config(instance, source)
    output = tmp_path / "output"

    # When: capture sanitizes the generated credential.
    capture(instance, output)

    # Then: exactly the password JSON string token changes and no source marker is retained.
    captured = (output / "config" / "resourceful-config-web.json").read_bytes()
    expected = source.replace(b'"test-only-source-value"', b'"<redacted-generated-secret>"')
    assert captured == expected
    assert _TEST_SOURCE_VALUE.encode() not in captured
    assert _TEST_SOURCE_VALUE.encode() not in (tmp_path / "config-sanitization.json").read_bytes()


@pytest.mark.parametrize(
    "payload",
    [
        b'{"validator":{"if":{"password":"test-only-source-value"}},"invalid":NaN}',
        b'{"validator":{"if":{"password":"test-only-source-value"}},"invalid":Infinity}',
        b'{"validator":{"if":{"password":"test-only-source-value"}},"invalid":-Infinity}',
        b'{"validator":{"if":{"password":"test-only-source-value"}},"invalid":1e309}',
        b'{"validator":{"if":{"password":"test-only-source-value","password":"other"}}}',
        b'{"validator":{"if":{"\\u0070assword":"test-only-source-value"}}}',
        b'{"validator":{"if":{"password":"test-only-source-value"}},"other":{"password":"other"}}',
        b'{"validator":{"if":{"password":false}}}',
        b'{"validator":{"if":{"password":"test-only-source-value"}',
    ],
)
def test_capture_surgically_rejects_ambiguous_or_nonstandard_credential_json(
    tmp_path: Path, payload: bytes
) -> None:
    """Unsafe JSON source forms cannot reach a capture output or receipt."""
    # Given: a complete source instance with one nonstandard or ambiguous JSON form.
    instance = _make_instance(tmp_path)
    _write_resourceful_config(instance, payload)
    output = tmp_path / "output"

    # When/Then: strict sanitization fails before either output artifact exists.
    with pytest.raises(ValueError, match="generated credential shape"):
        capture(instance, output)
    assert not output.exists()
    assert not (tmp_path / "config-sanitization.json").exists()


@pytest.mark.parametrize("payload", [None, "{}"])
def test_capture_rejects_missing_or_invalid_resourceful_credential_before_output(
    tmp_path: Path, payload: str | None
) -> None:
    """Missing or malformed credential input cannot leave a capture directory behind."""
    # Given: a complete instance whose target configuration is absent or lacks the password.
    instance = _make_instance(tmp_path)
    source = instance / "config" / "resourceful-config-web.json"
    if payload is None:
        source.unlink()
    else:
        _ = source.write_text(payload, encoding="utf-8")
    output = tmp_path / "output"

    # When/Then: capture rejects the unsafe shape before output exists.
    with pytest.raises(ValueError, match="resourceful-config-web"):
        capture(instance, output)
    assert not output.exists()
    assert not (tmp_path / "config-sanitization.json").exists()


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

    # Then: the command succeeds with exactly the public configuration inventory.
    assert completed.returncode == 0, completed.stderr
    assert _TEST_SOURCE_VALUE not in completed.stdout
    assert _TEST_SOURCE_VALUE not in completed.stderr
    captured = json.loads(
        (output / "config" / "resourceful-config-web.json").read_text(encoding="utf-8")
    )
    assert captured["validator"]["if"]["password"] == _REDACTION_SENTINEL
    receipt_text = (tmp_path / "config-sanitization.json").read_text(encoding="utf-8")
    assert _TEST_SOURCE_VALUE not in receipt_text
    assert "hash" not in receipt_text
    assert sorted(
        path.relative_to(output).as_posix() for path in output.rglob("*") if path.is_file()
    ) == [
        "config/resourceful-config-web.json",
        "config/settings.txt",
        "defaultconfigs/settings.txt",
        "server.properties",
        "world-serverconfig/settings.txt",
    ]
    assert (tmp_path / "config-sanitization.json").is_file()
