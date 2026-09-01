from __future__ import annotations

import hashlib
from typing import TYPE_CHECKING

import pytest

from mcpack_evidence.item3_acquisition import (
    ArtifactVerificationError,
    validate_artifact_redirect,
    verify_artifact_file,
)

if TYPE_CHECKING:
    from pathlib import Path


def test_verifies_size_and_all_publisher_hashes(tmp_path: Path) -> None:
    # Given
    artifact = tmp_path / "candidate.jar"
    body = b"exact artifact bytes"
    _ = artifact.write_bytes(body)
    publisher_hashes = {
        "sha1": hashlib.sha1(body, usedforsecurity=False).hexdigest(),
        "sha512": hashlib.sha512(body).hexdigest(),
    }

    # When
    identity = verify_artifact_file(artifact, len(body), publisher_hashes)

    # Then
    assert identity.size_bytes == len(body)
    assert identity.computed_sha256 == hashlib.sha256(body).hexdigest()
    assert identity.verified_publisher_hashes == publisher_hashes


def test_rejects_publisher_hash_mismatch(tmp_path: Path) -> None:
    # Given
    artifact = tmp_path / "candidate.jar"
    _ = artifact.write_bytes(b"wrong bytes")

    # When / Then
    with pytest.raises(ArtifactVerificationError, match="sha1"):
        _ = verify_artifact_file(artifact, 11, {"sha1": "0" * 40})


def test_accepts_same_path_forgecdn_redirect() -> None:
    # Given
    source = "https://edge.forgecdn.net/files/1/002/candidate.jar"
    target = "https://mediafilez.forgecdn.net/files/1/002/candidate.jar"

    # When
    accepted = validate_artifact_redirect(source, target)

    # Then
    assert accepted == target


def test_accepts_numeric_suffix_canonicalization() -> None:
    # Given
    source = "https://edge.forgecdn.net/files/6510/009/candidate.jar"
    target = "https://mediafilez.forgecdn.net/files/6510/9/candidate.jar"

    # When
    accepted = validate_artifact_redirect(source, target)

    # Then
    assert accepted == target


@pytest.mark.parametrize(
    "target",
    [
        "https://example.com/files/1/002/candidate.jar",
        "https://mediafilez.forgecdn.net/files/9/999/substitute.jar",
    ],
)
def test_rejects_redirect_host_or_path_substitution(target: str) -> None:
    # Given
    source = "https://edge.forgecdn.net/files/1/002/candidate.jar"

    # When / Then
    with pytest.raises(ArtifactVerificationError, match="redirect"):
        _ = validate_artifact_redirect(source, target)
