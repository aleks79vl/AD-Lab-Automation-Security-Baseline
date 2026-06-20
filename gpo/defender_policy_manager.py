from typing import Dict, List


class DefenderPolicyManager:

    def __init__(self, policy_config: Dict):
        self.policy = policy_config
        self.gpo_name = policy_config["gpo_name"]

    def generate_defender_policy_commands(self) -> List[str]:
        commands = []

        if self.policy["real_time_protection"]:
            commands.append(
                f'Set-GPRegistryValue -Name "{self.gpo_name}" '
                f'-Key "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" '
                f'-ValueName "DisableRealtimeMonitoring" -Type DWord -Value 0'
            )

        if self.policy["cloud_protection"]:
            commands.append(
                f'Set-GPRegistryValue -Name "{self.gpo_name}" '
                f'-Key "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Spynet" '
                f'-ValueName "SpynetReporting" -Type DWord -Value 2'
            )

        if self.policy["sample_submission"]:
            commands.append(
                f'Set-GPRegistryValue -Name "{self.gpo_name}" '
                f'-Key "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Spynet" '
                f'-ValueName "SubmitSamplesConsent" -Type DWord -Value 1'
            )

        if self.policy["behavior_monitoring"]:
            commands.append(
                f'Set-GPRegistryValue -Name "{self.gpo_name}" '
                f'-Key "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" '
                f'-ValueName "DisableBehaviorMonitoring" -Type DWord -Value 0'
            )

        if self.policy["script_scanning"]:
            commands.append(
                f'Set-GPRegistryValue -Name "{self.gpo_name}" '
                f'-Key "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows Defender\\Real-Time Protection" '
                f'-ValueName "DisableScriptScanning" -Type DWord -Value 0'
            )

        return commands
    