from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
from typing import TYPE_CHECKING, Final, TypedDict, final, override

from mcpack_evidence import item7_runtime
from mcpack_evidence.item7_selections import PILOT_SELECTIONS

if TYPE_CHECKING:
    from collections.abc import Callable

ROOT = Path(__file__).parents[2]
FROZEN = ROOT / "evidence/item-6/frozen"
FROZEN_MANIFEST = ROOT / "evidence/item-6/generated-config-manifest.json"
CONFIG_AUDIT = ROOT / "evidence/item-6/config-audit.json"
SEEDS = ROOT / "test-environment/seed-suite.json"
RETAINED = ROOT / "evidence/item-3/runtime/retained-server-candidates.txt"
CHUNKY = ROOT / "downloads/item3/candidates/Chunky-NeoForge-1.4.23.jar"


class ArtifactIdentity(TypedDict):
    size_bytes: int
    computed_sha256: str


class ArtifactRecord(TypedDict):
    candidate_filename: str
    local_path: str
    identity: ArtifactIdentity


class AcquisitionDocument(TypedDict):
    artifacts: list[ArtifactRecord]


def _digest(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def record_pids(killed: list[int]) -> Callable[[int, int], None]:
    def record(pid: int, signal_number: int) -> None:
        del signal_number
        killed.append(pid)

    return record


def record_pid_signals(killed: list[tuple[int, int]]) -> Callable[[int, int], None]:
    def record(pid: int, signal_number: int) -> None:
        killed.append((pid, signal_number))

    return record


def fake_launch(process: FakeProcess) -> Callable[..., FakeProcess]:
    def launch(*args: str, **kwargs: str | bool | int | Path | None) -> FakeProcess:
        del args, kwargs
        return process

    return launch


def pipe_less_launch(process: PipeLessProcess) -> Callable[..., PipeLessProcess]:
    def launch(*args: str, **kwargs: str | bool | int | Path | None) -> PipeLessProcess:
        del args, kwargs
        return process

    return launch


def runtime_request(tmp_path: Path, *, role: str = "mountainous") -> item7_runtime.WorldgenRequest:
    pristine = tmp_path / "pristine"
    _ = (pristine / "mods").mkdir(parents=True)
    _ = (pristine / "world").mkdir()
    _ = (pristine / "world/level.dat").write_bytes(b"stale")
    _ = (pristine / "server.properties").write_text("level-name=old\n", encoding="utf-8")
    _ = (pristine / "run.sh").write_text("#!/bin/sh\n", encoding="utf-8")
    artifacts = tmp_path / "artifacts"
    _ = artifacts.mkdir()
    records: list[ArtifactRecord] = []
    for index, name in enumerate(RETAINED.read_text(encoding="utf-8").splitlines()):
        content = f"retained-{index}".encode()
        path = artifacts / name
        _ = path.write_bytes(content)
        records.append(
            {
                "candidate_filename": name,
                "local_path": str(path),
                "identity": {"size_bytes": len(content), "computed_sha256": _digest(content)},
            }
        )
    chunky = artifacts / item7_runtime.CHUNKY_FILENAME
    _ = chunky.write_bytes(CHUNKY.read_bytes())
    records.append(
        {
            "candidate_filename": item7_runtime.CHUNKY_FILENAME,
            "local_path": str(chunky),
            "identity": {
                "size_bytes": chunky.stat().st_size,
                "computed_sha256": item7_runtime.sha256_file(chunky),
            },
        }
    )
    acquisition = tmp_path / "acquisition.json"
    document: AcquisitionDocument = {"artifacts": records}
    _ = acquisition.write_text(json.dumps(document), encoding="utf-8")
    retained = tmp_path / "retained.txt"
    _ = retained.write_bytes(RETAINED.read_bytes())
    java_home = tmp_path / "java"
    _ = (java_home / "bin").mkdir(parents=True)
    java = java_home / "bin/java"
    _ = java.write_text(
        "#!/bin/sh\necho 'Temurin-21.0.12.1+1 (build 21.0.12.1+1-LTS)' >&2\n",
        encoding="utf-8",
    )
    _ = java.chmod(0o755)
    return item7_runtime.WorldgenRequest(
        pristine=pristine,
        artifact_manifest=acquisition,
        retained_manifest=retained,
        seed_suite=SEEDS,
        frozen_config=FROZEN,
        frozen_manifest=FROZEN_MANIFEST,
        config_audit=CONFIG_AUDIT,
        java_home=java_home,
        role=role,
        target=tmp_path / "instance",
        log_path=tmp_path / "runtime.log",
        captured_config=tmp_path / "captured-config",
        selections=PILOT_SELECTIONS,
        timeout_seconds=30,
    )


class RecordingPipe(io.StringIO):
    @override
    def close(self) -> None:
        return None


@final
class FakeProcess:
    def __init__(self, lines: tuple[str, ...], stdin: io.StringIO | None = None) -> None:
        self.pid: int = 43210
        self.stdin: io.StringIO = stdin or RecordingPipe()
        self.stdout: io.StringIO = io.StringIO("".join(lines))
        self._return_code: int | None = None

    def poll(self) -> int | None:
        return self._return_code

    def wait(self, timeout: float | None = None) -> int:
        del timeout
        self._return_code = 0
        return 0


@final
class PipeLessProcess:
    def __init__(self) -> None:
        self.pid: int = 43210
        self.stdin: None = None
        self.stdout: io.StringIO = io.StringIO()

    def poll(self) -> None:
        return None

    def wait(self, timeout: float | None = None) -> int:
        del timeout
        return 0


class BrokenPipe(RecordingPipe):
    @override
    def write(self, value: str) -> int:
        del value
        raise BrokenPipeError


READY_LINES: Final = (
    '[Server thread/INFO]: Done (12.345s)! For help, type "help"\n',
    "[Chunky] Task finished for minecraft:overworld. Processed: 81 chunks (100.00%)\n",
    "[Chunky] Task finished for minecraft:the_nether. Processed: 81 chunks (100.00%)\n",
    "[Chunky] Task finished for minecraft:the_end. Processed: 81 chunks (100.00%)\n",
    "[Chunky] Task finished for minecraft:the_end. Processed: 81 chunks (100.00%)\n",
    "[Server thread/INFO]: Saved the game\n",
)
