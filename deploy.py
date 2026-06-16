from ad.ou_manager import OUManager
from utils.config_loader import load_config
from utils.logger import log_info, log_error
from utils.report_writer import save_commands


def main():
    try:
        config = load_config()

        domain_dn = config["domain_dn"]
        ous = config["ous"]

        ou_manager = OUManager(domain_dn)
        commands = ou_manager.generate_create_ou_commands(ous)

        log_info("Starting OU command generation")

        print("\nGenerated PowerShell commands:\n")

        for command in commands:
            print(command)
            log_info(f"Generated command: {command}")

        output_file = save_commands(commands, "ou_commands.ps1")

        print(f"\nCommands saved to: {output_file}")
        log_info(f"Commands saved to: {output_file}")

        log_info("OU command generation completed")

    except Exception as error:
        log_error(f"Deployment failed: {error}")
        print(f"[ERROR] {error}")


if __name__ == "__main__":
    main()
