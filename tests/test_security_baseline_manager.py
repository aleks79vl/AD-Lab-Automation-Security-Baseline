from gpo.security_baseline_manager import SecurityBaselineManager


def test_generate_all_security_baseline_commands():
    config = {
        "password_policy": {
            "min_length": 12,
            "complexity_enabled": True,
            "password_history_count": 24,
            "max_password_age_days": 90,
            "min_password_age_days": 1,
            "lockout_threshold": 5,
            "lockout_duration_minutes": 30,
            "lockout_observation_window_minutes": 30
        },
        "workstation_security": {
            "gpo_name": "Workstation Baseline",
            "auto_lock_seconds": 300,
            "disable_control_panel": True,
            "disable_cmd": True,
            "disable_powershell": True
        },
        "server_security": {
            "gpo_name": "Server Baseline",
            "auto_lock_seconds": 300,
            "disable_guest_account": True,
            "restrict_anonymous_enumeration": True,
            "smb_signing_required": True
        },
        "defender_policy": {
            "gpo_name": "Defender Baseline",
            "real_time_protection": True,
            "cloud_protection": True,
            "sample_submission": True,
            "behavior_monitoring": True,
            "script_scanning": True
        },
        "account_lockout_policy": {
            "domain": "thm.local",
            "lockout_threshold": 5,
            "lockout_duration_minutes": 15,
            "lockout_observation_window_minutes": 15
        },
        "audit_policy": {
            "logon_events": True,
            "account_logon_events": True,
            "account_management": True,
            "directory_service_changes": True,
            "policy_changes": True,
            "object_access": True,
            "process_creation": True
        },
        "powershell_logging": {
            "script_block_logging": True,
            "module_logging": True,
            "transcription": True
        }
    }

    manager = SecurityBaselineManager(config)

    commands = manager.generate_all_security_baseline_commands()

    assert "password_policy" in commands
    assert "workstation_security" in commands
    assert "server_security" in commands
    assert "defender_policy" in commands
    assert "account_lockout_policy" in commands
    assert "audit_policy" in commands
    assert "powershell_logging" in commands

    assert len(commands["defender_policy"]) == 5
    assert len(commands["audit_policy"]) == 8
    assert len(commands["powershell_logging"]) == 3

    assert "Set-ADDefaultDomainPasswordPolicy" in commands["password_policy"][0]
    assert "EnableScriptBlockLogging" in "\n".join(commands["powershell_logging"])