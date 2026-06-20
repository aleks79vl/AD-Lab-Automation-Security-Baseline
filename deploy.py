from ad.ou_manager import OUManager
from ad.group_manager import GroupManager
from ad.user_manager import UserManager
from ad.computer_manager import ComputerManager
from ad.group_membership_manager import GroupMembershipManager
from gpo.gpo_manager import GPOManager
from gpo.password_policy_manager import PasswordPolicyManager
from gpo.workstation_policy_manager import WorkstationPolicyManager
from gpo.server_policy_manager import ServerPolicyManager
from gpo.defender_policy_manager import DefenderPolicyManager
from utils.validator import ConfigValidator
from utils.report_manager import ReportManager


from utils.config_loader import load_config
from utils.logger import log_creation, log_error
from utils.report_writer import save_commands


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
        password_policy = config["password_policy"]
        workstation_security = config["workstation_security"]
        server_security = config["server_security"]
        defender_policy = config["defender_policy"]

        ou_manager = OUManager(domain_dn)
        group_manager = GroupManager(domain_dn)
        user_manager = UserManager(domain_dn, domain_name)
        computer_manager = ComputerManager(domain_dn)
        membership_manager = GroupMembershipManager()
        gpo_manager = GPOManager(domain_dn)
        password_policy_manager = PasswordPolicyManager(password_policy)
        workstation_policy_manager = WorkstationPolicyManager(workstation_security)
        server_policy_manager = ServerPolicyManager(server_security)
        defender_policy_manager = DefenderPolicyManager(defender_policy)

        ou_commands = ou_manager.generate_create_ou_commands(ous)
        group_commands = group_manager.generate_create_group_commands(groups)
        user_commands = user_manager.generate_create_user_commands(users)
        computer_commands = computer_manager.generate_create_computer_commands(computers)
        membership_commands = membership_manager.generate_add_member_commands(memberships)
        gpo_commands = gpo_manager.generate_gpo_commands(gpos)
        password_policy_commands = [
            password_policy_manager.generate_password_policy_command()
        ]
        workstation_policy_commands = workstation_policy_manager.generate_workstation_policy_commands()
        server_policy_commands = server_policy_manager.generate_server_policy_commands()
        defender_policy_commands = (
            defender_policy_manager.generate_defender_policy_commands()
        )

        log_creation("Starting command generation")

        print("\nGenerated OU PowerShell commands:\n")

        for command in ou_commands:
            print(command)
            log_creation(f"Generated OU command: {command}")

        ou_output_file = save_commands(ou_commands, "ou_commands.ps1")
        print(f"\nOU commands saved to: {ou_output_file}")

        print("\nGenerated Group PowerShell commands:\n")

        for command in group_commands:
            print(command)
            log_creation(f"Generated Group command: {command}")

        group_output_file = save_commands(group_commands, "group_commands.ps1")
        print(f"\nGroup commands saved to: {group_output_file}")

        print("\nGenerated User PowerShell commands:\n")

        for command in user_commands:
            print(command)
            log_creation(f"Generated User command: {command}")

        user_output_file = save_commands(user_commands, "user_commands.ps1")
        print(f"\nUser commands saved to: {user_output_file}")


        for command in computer_commands:
            print(command)
            log_creation(f"Generated Computer command: {command}")

        computer_output_file = save_commands(computer_commands, "computer_commands.ps1")
        print(f"\nComputer commands saved to: {computer_output_file}")

        print("\nGenerated Group Membership PowerShell commands:\n")

        for command in membership_commands:
            print(command)
            log_creation(f"Generated Membership command: {command}")

        membership_output_file = save_commands(
            membership_commands,
            "group_membership_commands.ps1")

        print(f"\nGroup membership commands saved to: {membership_output_file}")

        for command in gpo_commands:
            print(command)
            log_creation(f"Generated GPO command: {command}")

        gpo_output_file = save_commands(gpo_commands, "gpo_commands.ps1")

        print(f"\nGPO commands saved to: {gpo_output_file}")

        for command in password_policy_commands:
            print(command)
            log_creation(f"Generated Password Policy command: {command}")

        password_policy_output_file = save_commands(
            password_policy_commands,
            "password_policy_commands.ps1"
            )

        print(f"\nPassword policy commands saved to: {password_policy_output_file}")

        for command in workstation_policy_commands:
            print(command)
            log_creation(f"Generated Workstation Security command: {command}")

            workstation_policy_output_file = save_commands(
            workstation_policy_commands,
            "workstation_security_commands.ps1"
            )

        print(f"\nWorkstation security commands saved to: {workstation_policy_output_file}")



        for command in server_policy_commands:
            print(command)
            log_creation(f"Generated Server Security command: {command}")

            server_policy_output_file = save_commands(
            server_policy_commands,
            "server_security_commands.ps1"
            )
        print(f"\nServer security commands saved to: {server_policy_output_file}")

        defender_policy_output_file = save_commands(
            defender_policy_commands,
            "defender_policy_commands.ps1"
            )

        print(f"\nDefender policy commands saved to: {defender_policy_output_file}")
        log_creation(f"Defender policy commands saved to: {defender_policy_output_file}")

        print("\nGenerated Defender Policy PowerShell commands:\n")

        for command in defender_policy_commands:
            print(command)
            log_creation(f"Generated Defender Policy command: {command}")

   

        log_creation("Command generation completed")

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
            ]
        
        report_manager = ReportManager()
            
        report_file = report_manager.generate_deployment_report(
            config,
            generated_files,
            "SUCCESS"
            )

        print(f"\nDeployment report saved to: {report_file}")
        log_creation(f"Deployment report saved to: {report_file}")

    except Exception as error:
        log_error(f"Deployment failed: {error}")
        print(f"[ERROR] {error}")


if __name__ == "__main__":
    main()
