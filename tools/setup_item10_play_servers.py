"""Create the two isolated servers requested for later player sessions."""

from __future__ import annotations

import argparse
import json
import shlex
from pathlib import Path

from mcpack_evidence.item7_runtime import (
    WorldgenRequest,
    prepare_worldgen,
    replace_property,
    validate_java_runtime,
)
from mcpack_evidence.item7_selections import PILOT_SELECTIONS


def main() -> None:
    """Reuse the verified materializer without running a worldgen experiment."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--java-home", type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    target = args.target.resolve()
    java, _ = validate_java_runtime(args.java_home)
    if target.exists():
        parser.error(f"target must be absent: {target}")
    target.mkdir(parents=True)
    for name, port in (("free-roaming", 25565), ("task", 25566)):
        instance = target / name
        request = WorldgenRequest(
            pristine=root / "instances/pristine-baseline-v0",
            artifact_manifest=root / "evidence/item-3/artifact-acquisition-manifest.json",
            retained_manifest=root / "evidence/item-3/runtime/retained-server-candidates.txt",
            seed_suite=root / "test-environment/seed-suite.json",
            frozen_config=root / "evidence/item-6/frozen",
            frozen_manifest=root / "evidence/item-6/generated-config-manifest.json",
            config_audit=root / "evidence/item-6/config-audit.json",
            java_home=args.java_home.resolve(),
            role="ordinary",
            target=instance,
            log_path=instance / "setup-console.log",
            captured_config=instance / "setup-captured-config",
            selections=PILOT_SELECTIONS,
            timeout_seconds=900,
        )
        # Preflight only: the Item 7 pilot selection is never executed here.
        receipt = prepare_worldgen(request)
        properties = instance / "server.properties"
        data = properties.read_bytes()
        for key, value in (
            ("server-ip", "127.0.0.1"),
            ("server-port", str(port)),
            ("online-mode", "true"),
            ("enable-rcon", "false"),
            ("enable-query", "false"),
            ("motd", f"mcpack {name}"),
        ):
            data = replace_property(data, key, value)
        properties.write_bytes(data)
        (instance / "setup-preflight.json").write_text(
            receipt.model_dump_json(indent=2) + "\n", encoding="utf-8"
        )
        launch = instance / "start.sh"
        launch.write_text(
            "#!/bin/sh\nset -eu\n"
            f"cd {shlex.quote(str(instance))}\n"
            f"exec {shlex.quote(str(java))} -Xms1G -Xmx4G "
            "@libraries/net/neoforged/neoforge/21.1.249/unix_args.txt nogui\n",
            encoding="utf-8",
        )
        launch.chmod(0o755)
        print(json.dumps({"profile": name, "created": True, "port": port}))


if __name__ == "__main__":
    main()
