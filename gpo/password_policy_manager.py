class PasswordPolicyManager:

    def __init__(self, policy_config):
        self.policy = policy_config

    def generate_password_policy_command(self):

        return (
            f'Set-ADDefaultDomainPasswordPolicy '
            f'-Identity "thm.local" '
            f'-MinPasswordLength {self.policy["min_length"]} '
            f'-ComplexityEnabled $true '
            f'-PasswordHistoryCount {self.policy["password_history_count"]} '
            f'-MaxPasswordAge {self.policy["max_password_age_days"]}.00:00:00 '
            f'-MinPasswordAge {self.policy["min_password_age_days"]}.00:00:00 '
            f'-LockoutThreshold {self.policy["lockout_threshold"]} '
            f'-LockoutDuration 00:{self.policy["lockout_duration_minutes"]}:00 '
            f'-LockoutObservationWindow 00:{self.policy["lockout_observation_window_minutes"]}:00'
        )