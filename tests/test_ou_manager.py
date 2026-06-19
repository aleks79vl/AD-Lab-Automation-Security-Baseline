from ad.ou_manager import OUManager


def test_generate_create_ou_command():
    manager = OUManager("DC=thm,DC=local")

    command = manager.generate_create_ou_command("IT")

    assert 'New-ADOrganizationalUnit' in command
    assert '-Name "IT"' in command
    assert '-Path "DC=thm,DC=local"' in command
    assert '-ProtectedFromAccidentalDeletion $false' in command