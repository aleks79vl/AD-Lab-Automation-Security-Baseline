from typing import Dict, List


class ServerPolicyManager:

    def __init__(self, policy_config: Dict):
        self.policy = policy_config
        self.gpo_name = policy_config["gpo_name"]

    def generate_auto_lock_command(self) -> str:
        seconds = self.policy["auto_lock_seconds"]

        return (
            f'Set-GPRegistryValue '
            f'-Name "{self.gpo_name}" '
            f'-Key "HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" '
            f'-ValueName "InactivityTimeoutSecs" '
            f'-Type DWord '
            f'-Value {seconds}'
        )

    def generate_disable_guest_account_command(self) -> str:
        return (
            f'Set-GPRegistryValue '
            f'-Name "{self.gpo_name}" '
            f'-Key "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Lsa" '
            f'-ValueName "LimitBlankPasswordUse" '
            f'-Type DWord '
            f'-Value 1'
        )

    def generate_restrict_anonymous_enumeration_command(self) -> str:
        return (
            f'Set-GPRegistryValue '
            f'-Name "{self.gpo_name}" '
            f'-Key "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Lsa" '
            f'-ValueName "RestrictAnonymous" '
            f'-Type DWord '
            f'-Value 1'
        )

    def generate_smb_signing_required_commands(self) -> List[str]:
        return [
            (
                f'Set-GPRegistryValue '
                f'-Name "{self.gpo_name}" '
                f'-Key "HKLM\\SYSTEM\\CurrentControlSet\\Services\\LanmanServer\\Parameters" '
                f'-ValueName "RequireSecuritySignature" '
                f'-Type DWord '
                f'-Value 1'
            ),
            (
                f'Set-GPRegistryValue '
                f'-Name "{self.gpo_name}" '
                f'-Key "HKLM\\SYSTEM\\CurrentControlSet\\Services\\LanmanWorkstation\\Parameters" '
                f'-ValueName "RequireSecuritySignature" '
                f'-Type DWord '
                f'-Value 1'
            )
        ]

    def generate_server_policy_commands(self) -> List[str]:
        commands = []

        if self.policy["auto_lock_seconds"]:
            commands.append(self.generate_auto_lock_command())

        if self.policy["disable_guest_account"]:
            commands.append(self.generate_disable_guest_account_command())

        if self.policy["restrict_anonymous_enumeration"]:
            commands.append(self.generate_restrict_anonymous_enumeration_command())

        if self.policy["smb_signing_required"]:
            commands.extend(self.generate_smb_signing_required_commands())

        return commands