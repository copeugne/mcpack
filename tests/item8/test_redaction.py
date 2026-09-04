from __future__ import annotations

from mcpack_evidence.item8_redaction import redact_authored_fields


def test_redaction_preserves_gameplay_data_and_records_omissions() -> None:
    paths: list[str] = []
    result = redact_authored_fields(
        {
            "id": "minecraft:zombie",
            "UUID": [1, 2, 3, 4],
            "equipment": [{"minecraft:profile": {"id": [1, 2, 3, 4], "name": "author"}}],
            "nbt": {"OwnerUUID": "authored-owner", "Password": "authored-value"},
            "LootTable": "example:chests/tower",
        },
        paths,
    )
    assert result == {
        "id": "minecraft:zombie",
        "UUID": "<redacted-authored-identity-or-credential>",
        "equipment": [{"minecraft:profile": "<redacted-authored-identity-or-credential>"}],
        "nbt": {
            "OwnerUUID": "<redacted-authored-identity-or-credential>",
            "Password": "<redacted-authored-identity-or-credential>",
        },
        "LootTable": "example:chests/tower",
    }
    assert paths == ["/UUID", "/equipment/0/minecraft:profile", "/nbt/OwnerUUID", "/nbt/Password"]
