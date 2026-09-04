# pyright: standard
"""Sanitization and byte-preservation tests for the Item 6 capture boundary."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING

import pytest

from tests.item6.capture_fixtures import (
    _TEST_SOURCE_VALUE,
    _make_instance,
    _write_resourceful_config,
)
from tests.item6.helpers import capture

if TYPE_CHECKING:
    from pathlib import Path

_REDACTION_SENTINEL = "<redacted-generated-secret>"


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
