"""Produce publishable source catalogs with uv run -m tools.redact_item8_catalog."""

from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING, cast

from mcpack_evidence.item8_redaction import redact_authored_fields

if TYPE_CHECKING:
    from pydantic import JsonValue


def main() -> None:
    """Preserve source hashes while explicitly omitting authored identities and credentials."""
    parser = argparse.ArgumentParser(description=__doc__)
    _ = parser.add_argument("--input", type=Path, required=True)
    _ = parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = cast("Path", args.input)
    output = cast("Path", args.output)
    raw = source.read_bytes()
    catalog = cast("dict[str, JsonValue]", json.loads(gzip.decompress(raw)))
    resources = catalog["resources"]
    if not isinstance(resources, list):
        message = "source catalog has no resources list"
        raise TypeError(message)
    for resource in resources:
        if not isinstance(resource, dict) or "redacted_fields" in resource:
            message = "invalid or previously redacted resource"
            raise ValueError(message)
        paths: list[str] = []
        resource["document"] = redact_authored_fields(resource["document"], paths)
        resource["redacted_fields"] = list(paths)
    catalog["redacted_from_sha256"] = hashlib.sha256(raw).hexdigest()
    payload = (json.dumps(catalog, sort_keys=True, separators=(",", ":")) + "\n").encode()
    with output.open("xb") as stream:
        _ = stream.write(gzip.compress(payload, mtime=0))


if __name__ == "__main__":
    main()
