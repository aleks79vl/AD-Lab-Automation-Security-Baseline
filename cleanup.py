from rollback.rollback_manager import RollbackManager
from utils.config_loader import load_config
from utils.logger import log_info, log_error
from utils.report_writer import save_commands


def main():
    try:
        config = load_config()

        rollback_manager = RollbackManager()
        rollback_commands = rollback_manager.generate_rollback_commands(config)

        log_info("Starting rollback command generation")

        print("\nGenerated Rollback PowerShell commands:\n")

        for command in rollback_commands:
            print(command)
            log_info(f"Generated Rollback command: {command}")

        rollback_output_file = save_commands(
            rollback_commands,
            "rollback_commands.ps1"
        )

        print(f"\nRollback commands saved to: {rollback_output_file}")
        log_info(f"Rollback commands saved to: {rollback_output_file}")

        log_info("Rollback command generation completed")

    except Exception as error:
        log_error(f"Rollback generation failed: {error}")
        print(f"[ERROR] {error}")


if __name__ == "__main__":
    main()