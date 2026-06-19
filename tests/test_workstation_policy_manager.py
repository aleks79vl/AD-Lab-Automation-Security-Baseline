from gpo.workstation_policy_manager import WorkstationPolicyManager


def test_generate_workstation_policy_commands():
    policy = {
        "gpo_name": "Workstation Baseline",
        "auto_lock_seconds": 300,
        "disable_control_panel": True,
        "disable_cmd": True,
        "disable_powershell": True
    }

    manager = WorkstationPolicyManager(policy)

    commands = manager.generate_workstation_policy_commands()
    combined_commands = "\n".join(commands)

    assert "Set-GPRegistryValue" in combined_commands
    assert '-Name "Workstation Baseline"' in combined_commands
    assert "InactivityTimeoutSecs" in combined_commands
    assert "-Value 300" in combined_commands
    assert "NoControlPanel" in combined_commands
    assert "DisableCMD" in combined_commands
    assert "DisallowRun" in combined_commands
    assert "powershell.exe" in combined_commands
    assert "pwsh.exe" in combined_commands
    