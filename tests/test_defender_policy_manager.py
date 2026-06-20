from gpo.defender_policy_manager import DefenderPolicyManager


def test_generate_defender_policy_commands():
    policy = {
        "gpo_name": "Defender Baseline",
        "real_time_protection": True,
        "cloud_protection": True,
        "sample_submission": True,
        "behavior_monitoring": True,
        "script_scanning": True
    }

    manager = DefenderPolicyManager(policy)

    commands = manager.generate_defender_policy_commands()
    combined_commands = "\n".join(commands)

    assert len(commands) == 5
    assert "Set-GPRegistryValue" in combined_commands
    assert '-Name "Defender Baseline"' in combined_commands
    assert "DisableRealtimeMonitoring" in combined_commands
    assert "SpynetReporting" in combined_commands
    assert "SubmitSamplesConsent" in combined_commands
    assert "DisableBehaviorMonitoring" in combined_commands
    assert "DisableScriptScanning" in combined_commands