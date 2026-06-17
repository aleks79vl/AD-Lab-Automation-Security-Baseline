from typing import Dict, List


class ComputerManager:

    def __init__(self, domain_dn: str):
        self.domain_dn = domain_dn

    def generate_create_computer_command(self, computer: Dict) -> str:
        computer_name = computer["name"]
        ou_name = computer["ou"]
        sam_account_name = f"{computer_name}$"

        return (
            f'New-ADComputer '
            f'-Name "{computer_name}" '
            f'-SamAccountName "{sam_account_name}" '
            f'-Path "OU={ou_name},{self.domain_dn}" '
            f'-Enabled $true'
        )

    def generate_create_computer_commands(self, computers: List[Dict]) -> List[str]:
        commands = []

        for computer in computers:
            command = self.generate_create_computer_command(computer)
            commands.append(command)

        return commands