from ad.ou_manager import OUManager
from ad.group_manager import GroupManager
from utils.config_loader import load_config
from utils.logger import log_info, log_error
from utils.report_writer import save_commands


def main():
    try:
        config = load_config()

        domain_dn = config["domain_dn"]
        ous = config["ous"]
        groups = config["groups"]

        ou_manager = OUManager(domain_dn)
        group_manager = GroupManager(domain_dn)

        ou_commands = ou_manager.generate_create_ou_commands(ous)
        group_commands = group_manager.generate_create_group_commands(groups)

        log_info("Starting command generation")

        print("\nGenerated OU PowerShell commands:\n")

        for command in ou_commands:
            print(command)
            log_info(f"Generated OU command: {command}")

        ou_output_file = save_commands(ou_commands, "ou_commands.ps1")

        print(f"\nOU commands saved to: {ou_output_file}")

        print("\nGenerated Group PowerShell commands:\n")

        for command in group_commands:
            print(command)
            log_info(f"Generated Group command: {command}")

        group_output_file = save_commands(group_commands, "group_commands.ps1")

        print(f"\nGroup commands saved to: {group_output_file}")

        log_info("Command generation completed")

    except Exception as error:
        log_error(f"Deployment failed: {error}")
        print(f"[ERROR] {error}")


if __name__ == "__main__":
    main()
