from __future__ import annotations

import fcntl
import sys
from pathlib import Path


def _main() -> int:
    lock_path = Path(sys.argv[1])
    ready = Path(sys.argv[2])
    with lock_path.open("r+b") as lock:
        fcntl.lockf(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        _ = ready.write_text("locked\n", encoding="utf-8")
        _ = sys.stdin.buffer.read(1)
        fcntl.lockf(lock, fcntl.LOCK_UN)
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
