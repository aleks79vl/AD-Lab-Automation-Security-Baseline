from gpo.powershell_logging_manager import PowerShellLoggingManager


def test_generate_powershell_logging_commands():

    policy = {
        "script_block_logging": True,
        "module_logging": True,
        "transcription": True
    }

    manager = PowerShellLoggingManager(policy)

    commands = manager.generate_powershell_logging_commands()

    combined_commands = "\n".join(commands)

    assert len(commands) == 3

    assert "EnableScriptBlockLogging" in combined_commands
    assert "EnableModuleLogging" in combined_commands
    assert "EnableTranscripting" in combined_commands

    assert "Set-GPRegistryValue" in combined_commands