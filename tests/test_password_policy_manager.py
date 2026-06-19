from gpo.password_policy_manager import PasswordPolicyManager


def test_generate_password_policy_command():
    policy = {
        "min_length": 12,
        "complexity_enabled": True,
        "password_history_count": 24,
        "max_password_age_days": 90,
        "min_password_age_days": 1,
        "lockout_threshold": 5,
        "lockout_duration_minutes": 30,
        "lockout_observation_window_minutes": 30
    }

    manager = PasswordPolicyManager(policy)

    command = manager.generate_password_policy_command()

    assert "Set-ADDefaultDomainPasswordPolicy" in command
    assert '-Identity "thm.local"' in command
    assert "-MinPasswordLength 12" in command
    assert "-ComplexityEnabled $true" in command
    assert "-PasswordHistoryCount 24" in command
    assert "-MaxPasswordAge 90.00:00:00" in command
    assert "-MinPasswordAge 1.00:00:00" in command
    assert "-LockoutThreshold 5" in command
    assert "-LockoutDuration 00:30:00" in command
    assert "-LockoutObservationWindow 00:30:00" in command
    