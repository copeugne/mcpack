"""Exact candidate artifact acquisition and publisher-hash verification."""

from __future__ import annotations

import hashlib
import http.client
import os
import time
import urllib.parse
from datetime import UTC, datetime
from pathlib import Path
from typing import TYPE_CHECKING, ClassVar, Literal

from pydantic import BaseModel, ConfigDict, Field

if TYPE_CHECKING:
    from mcpack_evidence.item3_source_models import SourceCandidate


class ArtifactVerificationError(ValueError):
    """A downloaded artifact differs from its exact publisher record."""


class VerifiedArtifactFile(BaseModel):
    """Computed identity after size and publisher-hash verification."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    size_bytes: int = Field(ge=0)
    computed_sha256: str = Field(pattern=r"^[0-9a-f]{64}$")
    verified_publisher_hashes: dict[str, str]


class AcquiredArtifact(BaseModel):
    """One exact local candidate artifact and its verification result."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    candidate_filename: str
    upstream_filename: str
    platform: Literal["modrinth", "curseforge"]
    source_url: str
    local_path: str
    acquisition: Literal["downloaded_verified", "cache_verified"]
    identity: VerifiedArtifactFile


class ArtifactAcquisitionManifest(BaseModel):
    """Complete local acquisition result for the Item 3 candidate set."""

    model_config: ClassVar[ConfigDict] = ConfigDict(frozen=True, extra="forbid")

    schema_version: Literal["item3-artifact-acquisition-v1"]
    generated_at: str
    candidate_count: int = Field(gt=0)
    total_size_bytes: int = Field(gt=0)
    artifacts: tuple[AcquiredArtifact, ...]


_ALLOWED_HOSTS = frozenset({"cdn.modrinth.com", "edge.forgecdn.net", "mediafilez.forgecdn.net"})
_PUBLISHER_HASH_ALGORITHMS = frozenset({"sha1", "sha512"})
_HTTP_OK = 200
_HTTP_FOUND = 302
_RETRY_DELAYS = (1.0, 2.0, 4.0)
_FORGE_PATH_PARTS = 5


def verify_artifact_file(
    path: Path,
    expected_size: int,
    publisher_hashes: dict[str, str],
) -> VerifiedArtifactFile:
    """Verify exact size and all supported publisher hashes for one file."""
    unsupported = set(publisher_hashes) - _PUBLISHER_HASH_ALGORITHMS
    if unsupported:
        message = f"unsupported publisher hash algorithms: {sorted(unsupported)}"
        raise ArtifactVerificationError(message)
    actual_size = path.stat().st_size
    if actual_size != expected_size:
        message = f"size mismatch: expected {expected_size}, found {actual_size}"
        raise ArtifactVerificationError(message)
    sha1 = hashlib.sha1(usedforsecurity=False)
    sha256 = hashlib.sha256()
    sha512 = hashlib.sha512()
    with path.open("rb") as stream:
        while block := stream.read(1024 * 1024):
            sha1.update(block)
            sha256.update(block)
            sha512.update(block)
    computed = {"sha1": sha1.hexdigest(), "sha512": sha512.hexdigest()}
    for algorithm, expected in publisher_hashes.items():
        if computed[algorithm] != expected.lower():
            message = f"{algorithm} mismatch for {path.name}"
            raise ArtifactVerificationError(message)
    return VerifiedArtifactFile(
        size_bytes=actual_size,
        computed_sha256=sha256.hexdigest(),
        verified_publisher_hashes=publisher_hashes,
    )


def acquire_candidate(candidate: SourceCandidate, root: Path) -> AcquiredArtifact:
    """Download or reverify one exact candidate without substituting its filename."""
    if Path(candidate.candidate_filename).name != candidate.candidate_filename:
        message = f"unsafe candidate filename: {candidate.candidate_filename}"
        raise ArtifactVerificationError(message)
    root.mkdir(parents=True, exist_ok=True)
    destination = root / candidate.candidate_filename
    artifact = candidate.artifact
    acquisition: Literal["downloaded_verified", "cache_verified"]
    if destination.is_file():
        identity = verify_artifact_file(
            destination,
            artifact.size_bytes,
            artifact.publisher_hashes,
        )
        acquisition = "cache_verified"
    else:
        partial = destination.with_name(f"{destination.name}.partial")
        _download_with_retries(artifact.download_url, partial)
        identity = verify_artifact_file(partial, artifact.size_bytes, artifact.publisher_hashes)
        _ = partial.replace(destination)
        acquisition = "downloaded_verified"
    return AcquiredArtifact(
        candidate_filename=candidate.candidate_filename,
        upstream_filename=artifact.exact_filename,
        platform=candidate.platform,
        source_url=artifact.download_url,
        local_path=destination.as_posix(),
        acquisition=acquisition,
        identity=identity,
    )


def build_acquisition_manifest(
    artifacts: tuple[AcquiredArtifact, ...],
) -> ArtifactAcquisitionManifest:
    """Build a persisted acquisition receipt in candidate inventory order."""
    return ArtifactAcquisitionManifest(
        schema_version="item3-artifact-acquisition-v1",
        generated_at=datetime.now(UTC).isoformat(),
        candidate_count=len(artifacts),
        total_size_bytes=sum(row.identity.size_bytes for row in artifacts),
        artifacts=artifacts,
    )


def validate_artifact_redirect(source_url: str, target_url: str) -> str:
    """Accept only CurseForge's same-artifact edge-to-media CDN redirect."""
    source = urllib.parse.urlsplit(source_url)
    target = urllib.parse.urlsplit(target_url)
    if (
        source.scheme != "https"
        or source.hostname != "edge.forgecdn.net"
        or target.scheme != "https"
        or target.hostname != "mediafilez.forgecdn.net"
        or not _equivalent_forgecdn_path(source.path, target.path)
        or target.query != source.query
    ):
        message = f"untrusted artifact redirect: {source_url} -> {target_url}"
        raise ArtifactVerificationError(message)
    return target_url


def _equivalent_forgecdn_path(source_path: str, target_path: str) -> bool:
    source = source_path.split("/")
    target = target_path.split("/")
    if (
        len(source) != _FORGE_PATH_PARTS
        or len(target) != _FORGE_PATH_PARTS
        or source[1] != "files"
        or target[1] != "files"
        or source[2] != target[2]
        or source[4] != target[4]
        or not source[3].isdigit()
        or not target[3].isdigit()
    ):
        return False
    return int(source[3]) == int(target[3])


def _download_with_retries(url: str, partial: Path) -> None:
    for attempt, retry_delay in enumerate(_RETRY_DELAYS):
        try:
            _download(url, partial)
        except (ConnectionError, OSError, TimeoutError):
            partial.unlink(missing_ok=True)
            if attempt == len(_RETRY_DELAYS) - 1:
                raise
            time.sleep(retry_delay)
        else:
            return


def _download(url: str, partial: Path) -> None:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname not in _ALLOWED_HOSTS:
        message = f"untrusted artifact URL: {url}"
        raise ArtifactVerificationError(message)
    connection = create_https_connection(parsed.hostname)
    target = parsed.path if not parsed.query else f"{parsed.path}?{parsed.query}"
    connection.request("GET", target, headers={"User-Agent": "mcpack-evidence/0.1"})
    response = connection.getresponse()
    if response.status == _HTTP_FOUND:
        location = response.getheader("Location")
        response.close()
        connection.close()
        if location is None:
            raise ConnectionError(response.status)
        _download(validate_artifact_redirect(url, location), partial)
        return
    if response.status != _HTTP_OK:
        connection.close()
        raise ConnectionError(response.status)
    try:
        with partial.open("wb") as stream:
            while block := response.read(1024 * 1024):
                _ = stream.write(block)
    finally:
        response.close()
        connection.close()


def create_https_connection(hostname: str) -> http.client.HTTPSConnection:
    """Create an HTTPS connection that honors the standard HTTPS proxy environment."""
    proxy_url = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    if not proxy_url:
        return http.client.HTTPSConnection(hostname, timeout=120)
    proxy = urllib.parse.urlsplit(proxy_url)
    if proxy.scheme != "http" or proxy.hostname is None:
        message = "HTTPS_PROXY must be an HTTP proxy URL with a hostname"
        raise ArtifactVerificationError(message)
    connection = http.client.HTTPSConnection(proxy.hostname, proxy.port or 80, timeout=120)
    connection.set_tunnel(hostname)
    return connection
