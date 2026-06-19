from ad.user_manager import UserManager


def test_generate_create_user_command():
    manager = UserManager("DC=thm,DC=local", "thm.local")

    user = {
        "username": "phillip",
        "first_name": "Phillip",
        "last_name": "Brown",
        "ou": "IT",
        "password": "Password123!"
    }

    command = manager.generate_create_user_command(user)

    assert 'ConvertTo-SecureString "Password123!"' in command
    assert "New-ADUser" in command
    assert '-Name "Phillip Brown"' in command
    assert '-GivenName "Phillip"' in command
    assert '-Surname "Brown"' in command
    assert '-SamAccountName "phillip"' in command
    assert '-UserPrincipalName "phillip@thm.local"' in command
    assert '-AccountPassword $password' in command
    assert '-Enabled $true' in command
    assert '-Path "OU=IT,DC=thm,DC=local"' in command
    assert '-ChangePasswordAtLogon $true' in command
    