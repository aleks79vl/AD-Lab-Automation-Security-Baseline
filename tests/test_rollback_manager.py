from rollback.rollback_manager import RollbackManager


def test_generate_rollback_commands():
    config = {
        "domain_dn": "DC=thm,DC=local",
        "users": [
            {
                "username": "phillip"
            }
        ],
        "computers": [
            {
                "name": "PC-001"
            }
        ],
        "groups": [
            {
                "name": "IT Admins"
            }
        ],
        "gpos": [
            {
                "name": "Workstation Baseline"
            }
        ],
        "ous": [
            "IT"
        ]
    }

    manager = RollbackManager()

    commands = manager.generate_rollback_commands(config)
    combined_commands = "\n".join(commands)

    assert "Remove-ADUser" in combined_commands
    assert '-Identity "phillip"' in combined_commands

    assert "Remove-ADComputer" in combined_commands
    assert '-Identity "PC-001"' in combined_commands

    assert "Remove-ADGroup" in combined_commands
    assert '-Identity "IT Admins"' in combined_commands

    assert "Remove-GPO" in combined_commands
    assert '-Name "Workstation Baseline"' in combined_commands

    assert "Remove-ADOrganizationalUnit" in combined_commands
    assert 'OU=IT,DC=thm,DC=local' in combined_commands
    