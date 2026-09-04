#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = ["mcpack-evidence"]
# [tool.uv.sources]
# mcpack-evidence = { path = "..", editable = true }
# ///

# How to run:
#   uv run python tools/analyze_item7_world.py INPUT --output OUTPUT \
#     --run-id RUN --seed-role ROLE --selection NAME --dimension ID \
#     --expected-sha256 SHA256

"""Write deterministic Item 7 candidate metrics from decoded selection JSONL."""

from __future__ import annotations

import argparse
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import final

from mcpack_evidence.item7_analysis import analyze_jsonl
from mcpack_evidence.item7_analysis_models import AnalysisIdentity


@dataclass(frozen=True, slots=True)
class _Arguments:
    input: Path
    output: Path
    identity: AnalysisIdentity
    expected_sha256: str


@final
class _Namespace(argparse.Namespace):
    def __init__(self) -> None:
        """Supply typed placeholders that argparse replaces with required values."""
        super().__init__()
        self.input = Path()
        self.output = Path()
        self.run_id = ""
        self.seed_role = ""
        self.selection = ""
        self.dimension = ""
        self.expected_sha256 = ""


def _arguments(argv: tuple[str, ...]) -> _Arguments:
    parser = argparse.ArgumentParser(description="Analyze one decoded Item 7 dimension selection.")
    _ = parser.add_argument("input", type=Path)
    _ = parser.add_argument("--output", required=True, type=Path)
    _ = parser.add_argument("--run-id", required=True)
    _ = parser.add_argument("--seed-role", required=True)
    _ = parser.add_argument("--selection", required=True)
    _ = parser.add_argument("--dimension", required=True)
    _ = parser.add_argument("--expected-sha256", required=True)
    namespace = parser.parse_args(argv, namespace=_Namespace())
    return _Arguments(
        input=namespace.input,
        output=namespace.output,
        identity=AnalysisIdentity(
            namespace.run_id,
            namespace.seed_role,
            namespace.selection,
            namespace.dimension,
        ),
        expected_sha256=namespace.expected_sha256,
    )


def main(argv: tuple[str, ...]) -> int:
    """Analyze one selection and atomically replace the requested JSON output."""
    args = _arguments(argv)
    analysis = analyze_jsonl(args.input, args.identity, args.expected_sha256)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            "w",
            encoding="utf-8",
            newline="\n",
            prefix=f".{args.output.name}.",
            dir=args.output.parent,
            delete=False,
        ) as stream:
            temporary = Path(stream.name)
            _ = stream.write(analysis.model_dump_json(indent=2))
            _ = stream.write("\n")
        _ = temporary.replace(args.output)
    except OSError:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
        raise
    print(f"analyzed {analysis.denominators.chunk_count} chunks to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(tuple(sys.argv[1:])))
