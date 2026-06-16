from typing import Dict, List


class UserManager:

    def __init__(self, domain_dn: str, domain_name: str):
        self.domain_dn = domain_dn
        self.domain_name = domain_name

    def generate_create_user_command(self, user: Dict) -> str:
        username = user["username"]
        first_name = user["first_name"]
        last_name = user["last_name"]
        ou = user["ou"]
        password = user["password"]

        full_name = f"{first_name} {last_name}"
        user_principal_name = f"{username}@{self.domain_name}"

        return (
            f'$password = ConvertTo-SecureString "{password}" -AsPlainText -Force; '
            f'New-ADUser '
            f'-Name "{full_name}" '
            f'-GivenName "{first_name}" '
            f'-Surname "{last_name}" '
            f'-SamAccountName "{username}" '
            f'-UserPrincipalName "{user_principal_name}" '
            f'-AccountPassword $password '
            f'-Enabled $true '
            f'-Path "OU={ou},{self.domain_dn}" '
            f'-ChangePasswordAtLogon $true'
        )

    def generate_create_user_commands(self, users: List[Dict]) -> List[str]:
        commands = []

        for user in users:
            command = self.generate_create_user_command(user)
            commands.append(command)

        return commands