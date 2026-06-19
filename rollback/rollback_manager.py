from typing import Dict, List


class RollbackManager:

    def generate_remove_user_command(self, username: str) -> str:
        return f'Remove-ADUser -Identity "{username}" -Confirm:$false'

    def generate_remove_group_command(self, group_name: str) -> str:
        return f'Remove-ADGroup -Identity "{group_name}" -Confirm:$false'

    def generate_remove_computer_command(self, computer_name: str) -> str:
        return f'Remove-ADComputer -Identity "{computer_name}" -Confirm:$false'

    def generate_remove_ou_command(self, ou_name: str, domain_dn: str) -> str:
        return (
            f'Remove-ADOrganizationalUnit '
            f'-Identity "OU={ou_name},{domain_dn}" '
            f'-Recursive '
            f'-Confirm:$false'
        )

    def generate_remove_gpo_command(self, gpo_name: str) -> str:
        return f'Remove-GPO -Name "{gpo_name}" -Confirm:$false'

    def generate_rollback_commands(
        self,
        config: Dict
    ) -> List[str]:

        commands = []

        for user in reversed(config["users"]):
            commands.append(
                self.generate_remove_user_command(user["username"])
            )

        for computer in reversed(config["computers"]):
            commands.append(
                self.generate_remove_computer_command(computer["name"])
            )

        for group in reversed(config["groups"]):
            commands.append(
                self.generate_remove_group_command(group["name"])
            )

        for gpo in reversed(config["gpos"]):
            commands.append(
                self.generate_remove_gpo_command(gpo["name"])
            )

        for ou in reversed(config["ous"]):
            commands.append(
                self.generate_remove_ou_command(
                    ou,
                    config["domain_dn"]
                )
            )

        return commands