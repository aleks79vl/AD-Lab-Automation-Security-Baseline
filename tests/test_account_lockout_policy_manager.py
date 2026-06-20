from gpo.account_lockout_policy_manager import AccountLockoutPolicyManager


def test_generate_account_lockout_policy_commands():
    policy = {
        "domain": "thm.local",
        "lockout_threshold": 5,
        "lockout_duration_minutes": 15,
        "lockout_observation_window_minutes": 15
    }

    manager = AccountLockoutPolicyManager(policy)

    commands = manager.generate_account_lockout_policy_commands()
    command = commands[0]

    assert len(commands) == 1
    assert "Set-ADDefaultDomainPasswordPolicy" in command
    assert '-Identity "thm.local"' in command
    assert "-LockoutThreshold 5" in command
    assert "-LockoutDuration 00:15:00" in command
    assert "-LockoutObservationWindow 00:15:00" in command