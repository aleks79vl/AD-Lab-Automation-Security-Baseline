from typing import List, Dict


class GroupMembershipManager:

    def generate_add_member_command(
        self,
        user_name: str,
        group_name: str
    ) -> str:

        return (
            f'Add-ADGroupMember '
            f'-Identity "{group_name}" '
            f'-Members "{user_name}"'
        )

    def generate_add_member_commands(
        self,
        memberships: List[Dict]
    ) -> List[str]:

        commands = []

        for membership in memberships:

            command = self.generate_add_member_command(
                membership["user"],
                membership["group"]
            )

            commands.append(command)

        return commands