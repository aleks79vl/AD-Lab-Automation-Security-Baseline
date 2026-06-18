from typing import Dict, List


class GPOManager:

    def __init__(self, domain_dn: str):
        self.domain_dn = domain_dn

    def generate_create_gpo_command(self, gpo_name: str) -> str:
        return f'New-GPO -Name "{gpo_name}"'

    def generate_link_gpo_command(self, gpo_name: str, target_ou: str) -> str:
        return (
            f'New-GPLink '
            f'-Name "{gpo_name}" '
            f'-Target "OU={target_ou},{self.domain_dn}"'
        )

    def generate_gpo_commands(self, gpos: List[Dict]) -> List[str]:
        commands = []

        for gpo in gpos:
            gpo_name = gpo["name"]
            target_ou = gpo["target"]

            commands.append(
                self.generate_create_gpo_command(gpo_name)
            )

            commands.append(
                self.generate_link_gpo_command(gpo_name, target_ou)
            )

        return commands