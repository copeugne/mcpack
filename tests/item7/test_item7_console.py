from __future__ import annotations

from mcpack_evidence.item7_console import FlushCorrelation, advance_correlated_flush
from tests.item7.runtime_support import RecordingPipe


def test_flush_correlation_rejects_wrong_duplicate_and_swapped_markers() -> None:
    stdin = RecordingPipe()
    commands: list[str] = []
    correlation = FlushCorrelation("token-before", "token-after")

    for line in (
        "[Server] token-before-extra\n",
        "Saved the game\n",
        "[Server] token-after\n",
    ):
        assert advance_correlated_flush(correlation, line, stdin, commands) == (False, None)
    assert commands == []

    assert advance_correlated_flush(correlation, "[Server] token-before\n", stdin, commands) == (
        False,
        None,
    )
    assert commands == ["save-all flush"]

    for line in (
        "[Server] token-before\n",
        "Saved the game\n",
        "[Server] token-after\n",
    ):
        assert advance_correlated_flush(correlation, line, stdin, commands) == (False, None)
    assert commands == ["save-all flush"]

    assert advance_correlated_flush(
        correlation, "Saving the game (this may take a moment!)\n", stdin, commands
    ) == (False, None)
    assert advance_correlated_flush(correlation, "[Server] token-after\n", stdin, commands) == (
        False,
        None,
    )
    assert advance_correlated_flush(correlation, "Saved the game\n", stdin, commands) == (
        False,
        None,
    )
    assert commands == ["save-all flush", "say token-after"]
    assert advance_correlated_flush(
        correlation, "[Server] wrong-token-after\n", stdin, commands
    ) == (False, None)
    assert advance_correlated_flush(correlation, "[Server] token-after\n", stdin, commands) == (
        True,
        None,
    )
    assert commands == ["save-all flush", "say token-after", "stop"]
