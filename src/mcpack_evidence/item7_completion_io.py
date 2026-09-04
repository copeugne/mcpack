"""Strict portable file handling for Item 7 completion evidence."""

from __future__ import annotations

import hashlib
import json
import os
import tempfile
from pathlib import Path, PurePosixPath
from typing import TYPE_CHECKING, NoReturn, final, override

from pydantic import BaseModel, ValidationError

from mcpack_evidence.item6_json import StrictJsonError, parse_strict_json
from mcpack_evidence.item7_completion_models import ArtifactIdentity

if TYPE_CHECKING:
    from pydantic import JsonValue


@final
class CompletionError(Exception):
    """One Item 7 completion evidence invariant failed."""

    __slots__ = ("issue", "subject")

    def __init__(self, issue: str, subject: str) -> None:
        """Preserve a stable issue and affected evidence subject."""
        super().__init__(issue, subject)
        self.issue = issue
        self.subject = subject

    @override
    def __str__(self) -> str:
        return f"Item 7 completion failed: {self.issue}: {self.subject}"


def fail(issue: str, subject: str | Path | int) -> NoReturn:
    """Raise the typed completion boundary error."""
    raise CompletionError(issue, str(subject))


def sha256_file(path: Path) -> str:
    """Hash one regular non-symlink input."""
    require_regular(path)
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def require_regular(path: Path) -> None:
    """Reject absent, symlinked, and nonregular evidence inputs."""
    if path.is_symlink() or not path.is_file():
        fail("input is not a regular file", path)


def portable_path(path: str) -> str:
    """Accept only normalized repository or archive relative paths."""
    candidate = PurePosixPath(path)
    if candidate.is_absolute() or ".." in candidate.parts or candidate.as_posix() != path:
        fail("nonportable evidence path", path)
    return path


def identity(path: Path, logical_path: str) -> ArtifactIdentity:
    """Create a portable content identity without leaking the source root."""
    return ArtifactIdentity(
        path=portable_path(logical_path),
        sha256=sha256_file(path),
        size_bytes=path.stat().st_size,
    )


def strict_json(path: Path) -> JsonValue:
    """Load one strict JSON document from a regular file."""
    require_regular(path)
    try:
        return parse_strict_json(path.read_bytes())
    except (OSError, StrictJsonError) as error:
        issue = "invalid strict JSON"
        raise CompletionError(issue, str(path)) from error


def strict_model[T: BaseModel](path: Path, model: type[T]) -> T:
    """Parse one duplicate-key-free strict JSON document into an exact model."""
    value = strict_json(path)
    try:
        return model.model_validate_json(
            json.dumps(value, separators=(",", ":"), ensure_ascii=False), strict=True
        )
    except ValidationError as error:
        issue = "invalid evidence schema"
        raise CompletionError(issue, str(path)) from error


def write_atomic(path: Path, model: BaseModel) -> None:
    """Replace completion output only after the complete body is durable."""
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    temporary = Path(name)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as stream:
            _ = stream.write(model.model_dump_json(indent=2) + "\n")
            stream.flush()
            os.fsync(stream.fileno())
        _ = temporary.replace(path)
    except OSError as error:
        temporary.unlink(missing_ok=True)
        issue = "cannot write completion report"
        raise CompletionError(issue, str(path)) from error
