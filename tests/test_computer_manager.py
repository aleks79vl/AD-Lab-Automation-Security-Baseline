from ad.computer_manager import ComputerManager


def test_generate_create_computer_command():
    manager = ComputerManager("DC=thm,DC=local")

    computer = {
        "name": "PC-001",
        "ou": "Workstations"
    }

    command = manager.generate_create_computer_command(computer)

    assert "New-ADComputer" in command
    assert '-Name "PC-001"' in command
    assert '-SamAccountName "PC-001$"' in command
    assert '-Path "OU=Workstations,DC=thm,DC=local"' in command
    assert "-Enabled $true" in command

    