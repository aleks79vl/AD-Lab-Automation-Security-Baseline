from typing import List


class OUManager:
    def __init__(self, domain_dn: str):
        self.domain_dn = domain_dn

    def generate_create_ou_command(self, ou_name: str) -> str:
        return (
            f'New-ADOrganizationalUnit '
            f'-Name "{ou_name}" '
            f'-Path "{self.domain_dn}" '
            f'-ProtectedFromAccidentalDeletion $false'
        )

    def generate_create_ou_commands(self, ous: List[str]) -> List[str]:
        commands = []

        for ou in ous:
            command = self.generate_create_ou_command(ou)
            commands.append(command)

        return commands
