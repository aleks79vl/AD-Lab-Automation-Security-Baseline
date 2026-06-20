from typing import Dict, List


class AccountLockoutPolicyManager:

    def __init__(self, policy_config: Dict):
        self.policy = policy_config
        self.domain = policy_config["domain"]

    def generate_account_lockout_policy_commands(self) -> List[str]:
        return [
            (
                f'Set-ADDefaultDomainPasswordPolicy -Identity "{self.domain}" '
                f'-LockoutThreshold {self.policy["lockout_threshold"]} '
                f'-LockoutDuration 00:{self.policy["lockout_duration_minutes"]}:00 '
                f'-LockoutObservationWindow 00:{self.policy["lockout_observation_window_minutes"]}:00'
            )
        ]