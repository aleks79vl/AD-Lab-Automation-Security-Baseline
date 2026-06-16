from typing import List, Dict


class GroupManager:

    def __init__(self, domain_dn: str):
        self.domain_dn = domain_dn

    def generate_create_group_command(
        self,
        group_name: str,
        ou_name: str
    ) -> str:

        return (
            f'New-ADGroup '
            f'-Name "{group_name}" '
            f'-GroupScope Global '
            f'-GroupCategory Security '
            f'-Path "OU={ou_name},{self.domain_dn}"'
        )

    def generate_create_group_commands(
        self,
        groups: List[Dict]
    ) -> List[str]:

        commands = []

        for group in groups:

            command = self.generate_create_group_command(
                group["name"],
                group["ou"]
            )

            commands.append(command)

        return commands
    