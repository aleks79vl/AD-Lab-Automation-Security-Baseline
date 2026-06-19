from ad.group_manager import GroupManager


def test_generate_create_group_command():
    manager = GroupManager("DC=thm,DC=local")

    group = {
        "name": "IT Admins",
        "ou": "IT"
    }

    command = manager.generate_create_group_command(
        group["name"],
        group["ou"]
    )

    assert "New-ADGroup" in command
    assert '-Name "IT Admins"' in command
    assert '-GroupScope Global' in command
    assert '-GroupCategory Security' in command
    assert '-Path "OU=IT,DC=thm,DC=local"' in command
    