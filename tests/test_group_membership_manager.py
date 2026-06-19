from ad.group_membership_manager import GroupMembershipManager


def test_generate_add_member_command():
    manager = GroupMembershipManager()

    command = manager.generate_add_member_command(
        "phillip",
        "IT Admins"
    )

    assert "Add-ADGroupMember" in command
    assert '-Identity "IT Admins"' in command
    assert '-Members "phillip"' in command
    