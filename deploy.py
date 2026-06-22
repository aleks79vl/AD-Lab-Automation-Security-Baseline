from ad.ou_manager import OUManager
from ad.group_manager import GroupManager
from ad.user_manager import UserManager
from ad.computer_manager import ComputerManager
from ad.group_membership_manager import GroupMembershipManager

from gpo.gpo_manager import GPOManager
from gpo.security_baseline_manager import SecurityBaselineManager

from utils.config_loader import load_config
from utils.logger import log_creation, log_error
from utils.report_writer import save_commands
from utils.validator import ConfigValidator
from utils.report_manager import ReportManager


def main():
    try:
        config = load_config()

        validator = ConfigValidator(config)

        if not validator.validate():
            print("[ERROR] Config validation failed:")

            for error in validator.errors:
                print(f"- {error}")

            return

        domain_dn = config["domain_dn"]
        domain_name = config["domain"]
        ous = config["ous"]
        groups = config["groups"]
        users = config["users"]
        computers = config["computers"]
        memberships = config["memberships"]
        gpos = config["gpos"]

        ou_manager = OUManager(domain_dn)
        group_manager = GroupManager(domain_dn)
        user_manager = UserManager(domain_dn, domain_name)
        computer_manager = ComputerManager(domain_dn)
        group_membership_manager = GroupMembershipManager()
        gpo_manager = GPOManager(domain_dn)

        security_baseline_manager = SecurityBaselineManager(config)

        log_creation("Starting AD command generation")

        ou_commands = []

        for ou in ous:
            command = ou_manager.generate_create_ou_command(ou)
            ou_commands.append(command)
            log_creation(f"Generated OU command: {command}")

        group_commands = []

        for group in groups:
            command = group_manager.generate_create_group_command(group["name"],group["ou"])
            group_commands.append(command)
            log_creation(f"Generated Group command: {command}")

        user_commands = []

        for user in users:
            command = user_manager.generate_create_user_command(user)
            user_commands.append(command)
            log_creation(f"Generated User command: {command}")

        computer_commands = []

        for computer in computers:
            command = computer_manager.generate_create_computer_command(computer)
            computer_commands.append(command)
            log_creation(f"Generated Computer command: {command}")

        membership_commands = []

        for membership in memberships:
            command = group_membership_manager.generate_add_member_command(membership["user"],membership["group"])
            membership_commands.append(command)
            log_creation(f"Generated Membership command: {command}")

        gpo_commands = []

        for gpo in gpos:
            create_command = gpo_manager.generate_create_gpo_command(gpo["name"])

            link_command = gpo_manager.generate_link_gpo_command(gpo["name"],gpo["target"])

            gpo_commands.append(create_command)
            gpo_commands.append(link_command)

            log_creation(f"Generated GPO command: {create_command}")
            log_creation(f"Generated GPO link command: {link_command}")

        security_baseline_commands = (
            security_baseline_manager.generate_all_security_baseline_commands()
        )

        print("\nGenerated OU PowerShell commands:\n")
        for command in ou_commands:
            print(command)

        print("\nGenerated Group PowerShell commands:\n")
        for command in group_commands:
            print(command)

        print("\nGenerated User PowerShell commands:\n")
        for command in user_commands:
            print(command)

        print("\nGenerated Computer PowerShell commands:\n")
        for command in computer_commands:
            print(command)

        print("\nGenerated Group Membership PowerShell commands:\n")
        for command in membership_commands:
            print(command)

        print("\nGenerated GPO PowerShell commands:\n")
        for command in gpo_commands:
            print(command)

        print("\nGenerated Password Policy PowerShell commands:\n")
        for command in security_baseline_commands["password_policy"]:
            print(command)
            log_creation(f"Generated Password Policy command: {command}")

        print("\nGenerated Workstation Security PowerShell commands:\n")
        for command in security_baseline_commands["workstation_security"]:
            print(command)
            log_creation(f"Generated Workstation Security command: {command}")

        print("\nGenerated Server Security PowerShell commands:\n")
        for command in security_baseline_commands["server_security"]:
            print(command)
            log_creation(f"Generated Server Security command: {command}")

        print("\nGenerated Defender Policy PowerShell commands:\n")
        for command in security_baseline_commands["defender_policy"]:
            print(command)
            log_creation(f"Generated Defender Policy command: {command}")

        print("\nGenerated Account Lockout Policy PowerShell commands:\n")
        for command in security_baseline_commands["account_lockout_policy"]:
            print(command)
            log_creation(
                f"Generated Account Lockout Policy command: {command}"
            )

        print("\nGenerated Audit Policy PowerShell commands:\n")
        for command in security_baseline_commands["audit_policy"]:
            print(command)
            log_creation(f"Generated Audit Policy command: {command}")

        print("\nGenerated PowerShell Logging commands:\n")
        for command in security_baseline_commands["powershell_logging"]:
            print(command)
            log_creation(
                f"Generated PowerShell Logging command: {command}"
            )

        ou_output_file = save_commands(ou_commands,"ou_commands.ps1")
        group_output_file = save_commands(group_commands,"group_commands.ps1")
        user_output_file = save_commands(user_commands,"user_commands.ps1")
        computer_output_file = save_commands(computer_commands,"computer_commands.ps1")
        membership_output_file = save_commands(membership_commands,"group_membership_commands.ps1")
        gpo_output_file = save_commands(gpo_commands,"gpo_commands.ps1")
        password_policy_output_file = save_commands(security_baseline_commands["password_policy"],"password_policy_commands.ps1")
        workstation_policy_output_file = save_commands(security_baseline_commands["workstation_security"],"workstation_security_commands.ps1")
        server_policy_output_file = save_commands(security_baseline_commands["server_security"],"server_security_commands.ps1")
        defender_policy_output_file = save_commands(security_baseline_commands["defender_policy"],"defender_policy_commands.ps1")
        account_lockout_policy_output_file = save_commands(security_baseline_commands["account_lockout_policy"],"account_lockout_policy_commands.ps1")
        audit_policy_output_file = save_commands(security_baseline_commands["audit_policy"],"audit_policy_commands.ps1")
        powershell_logging_output_file = save_commands(security_baseline_commands["powershell_logging"],"powershell_logging_commands.ps1")

        generated_files = [
            str(ou_output_file),
            str(group_output_file),
            str(user_output_file),
            str(computer_output_file),
            str(membership_output_file),
            str(gpo_output_file),
            str(password_policy_output_file),
            str(workstation_policy_output_file),
            str(server_policy_output_file),
            str(defender_policy_output_file),
            str(account_lockout_policy_output_file),
            str(audit_policy_output_file),
            str(powershell_logging_output_file)
        ]

        report_manager = ReportManager()

        report_file = report_manager.generate_deployment_report(config,generated_files,"SUCCESS")

        print(f"\nDeployment report saved to: {report_file}")
        log_creation(f"Deployment report saved to: {report_file}")

        log_creation("AD command generation completed successfully")

    except Exception as error:
        log_error(f"Deployment generation failed: {error}")
        print(f"[ERROR] {error}")


if __name__ == "__main__":
    main()