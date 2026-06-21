from typing import Dict, List


class PowerShellLoggingManager:

    def __init__(self, policy_config: Dict):
        self.policy = policy_config

    def generate_powershell_logging_commands(self) -> List[str]:
        commands = []

        if self.policy["script_block_logging"]:
            commands.append(
                'Set-GPRegistryValue -Name "PowerShell Logging" '
                '-Key "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\PowerShell\\ScriptBlockLogging" '
                '-ValueName "EnableScriptBlockLogging" -Type DWord -Value 1'
            )

        if self.policy["module_logging"]:
            commands.append(
                'Set-GPRegistryValue -Name "PowerShell Logging" '
                '-Key "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\PowerShell\\ModuleLogging" '
                '-ValueName "EnableModuleLogging" -Type DWord -Value 1'
            )

        if self.policy["transcription"]:
            commands.append(
                'Set-GPRegistryValue -Name "PowerShell Logging" '
                '-Key "HKLM\\SOFTWARE\\Policies\\Microsoft\\Windows\\PowerShell\\Transcription" '
                '-ValueName "EnableTranscripting" -Type DWord -Value 1'
            )

        return commands