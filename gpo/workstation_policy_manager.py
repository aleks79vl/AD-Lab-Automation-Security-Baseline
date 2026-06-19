from typing import Dict, List


class WorkstationPolicyManager:

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

    def generate_disable_control_panel_command(self) -> str:
        return (
            f'Set-GPRegistryValue '
            f'-Name "{self.gpo_name}" '
            f'-Key "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer" '
            f'-ValueName "NoControlPanel" '
            f'-Type DWord '
            f'-Value 1'
        )

    def generate_disable_cmd_command(self) -> str:
        return (
            f'Set-GPRegistryValue '
            f'-Name "{self.gpo_name}" '
            f'-Key "HKCU\\Software\\Policies\\Microsoft\\Windows\\System" '
            f'-ValueName "DisableCMD" '
            f'-Type DWord '
            f'-Value 2'
        )

    def generate_disable_powershell_commands(self) -> List[str]:
        return [
            (
                f'Set-GPRegistryValue '
                f'-Name "{self.gpo_name}" '
                f'-Key "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer" '
                f'-ValueName "DisallowRun" '
                f'-Type DWord '
                f'-Value 1'
            ),
            (
                f'Set-GPRegistryValue '
                f'-Name "{self.gpo_name}" '
                f'-Key "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\DisallowRun" '
                f'-ValueName "1" '
                f'-Type String '
                f'-Value "powershell.exe"'
            ),
            (
                f'Set-GPRegistryValue '
                f'-Name "{self.gpo_name}" '
                f'-Key "HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\Explorer\\DisallowRun" '
                f'-ValueName "2" '
                f'-Type String '
                f'-Value "pwsh.exe"'
            )
        ]

    def generate_workstation_policy_commands(self) -> List[str]:
        commands = []

        if self.policy["auto_lock_seconds"]:
            commands.append(self.generate_auto_lock_command())

        if self.policy["disable_control_panel"]:
            commands.append(self.generate_disable_control_panel_command())

        if self.policy["disable_cmd"]:
            commands.append(self.generate_disable_cmd_command())

        if self.policy["disable_powershell"]:
            commands.extend(self.generate_disable_powershell_commands())

        return commands