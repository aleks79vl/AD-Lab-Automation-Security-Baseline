from gpo.server_policy_manager import ServerPolicyManager


def test_generate_server_policy_commands():
    policy = {
        "gpo_name": "Server Baseline",
        "auto_lock_seconds": 300,
        "disable_guest_account": True,
        "restrict_anonymous_enumeration": True,
        "smb_signing_required": True
    }

    manager = ServerPolicyManager(policy)

    commands = manager.generate_server_policy_commands()
    combined_commands = "\n".join(commands)

    assert "Set-GPRegistryValue" in combined_commands

    assert '-Name "Server Baseline"' in combined_commands

    assert "InactivityTimeoutSecs" in combined_commands

    assert "LimitBlankPasswordUse" in combined_commands

    assert "RestrictAnonymous" in combined_commands

    assert "RequireSecuritySignature" in combined_commands
    