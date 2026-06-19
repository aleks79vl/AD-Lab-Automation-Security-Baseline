from gpo.gpo_manager import GPOManager


def test_generate_create_gpo_command():
    manager = GPOManager("DC=thm,DC=local")

    command = manager.generate_create_gpo_command("Workstation Baseline")

    assert "New-GPO" in command
    assert '-Name "Workstation Baseline"' in command


def test_generate_link_gpo_command():
    manager = GPOManager("DC=thm,DC=local")

    command = manager.generate_link_gpo_command(
        "Workstation Baseline",
        "Workstations"
    )

    assert "New-GPLink" in command
    assert '-Name "Workstation Baseline"' in command
    assert '-Target "OU=Workstations,DC=thm,DC=local"' in command
    