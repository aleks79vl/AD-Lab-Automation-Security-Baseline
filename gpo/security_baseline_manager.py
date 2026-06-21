from typing import Dict, List

from gpo.password_policy_manager import PasswordPolicyManager
from gpo.workstation_policy_manager import WorkstationPolicyManager
from gpo.server_policy_manager import ServerPolicyManager
from gpo.defender_policy_manager import DefenderPolicyManager
from gpo.account_lockout_policy_manager import AccountLockoutPolicyManager
from gpo.audit_policy_manager import AuditPolicyManager
from gpo.powershell_logging_manager import PowerShellLoggingManager


class SecurityBaselineManager:

    def __init__(self, config: Dict):
        self.config = config

        self.password_policy_manager = PasswordPolicyManager(
            config["password_policy"]
        )

        self.workstation_policy_manager = WorkstationPolicyManager(
            config["workstation_security"]
        )

        self.server_policy_manager = ServerPolicyManager(
            config["server_security"]
        )

        self.defender_policy_manager = DefenderPolicyManager(
            config["defender_policy"]
        )

        self.account_lockout_policy_manager = AccountLockoutPolicyManager(
            config["account_lockout_policy"]
        )

        self.audit_policy_manager = AuditPolicyManager(
            config["audit_policy"]
        )

        self.powershell_logging_manager = PowerShellLoggingManager(
            config["powershell_logging"]
        )

    def generate_all_security_baseline_commands(self) -> Dict[str, List[str]]:
        return {
            "password_policy": [
                self.password_policy_manager.generate_password_policy_command()
            ],
            "workstation_security": (
                self.workstation_policy_manager.generate_workstation_policy_commands()
            ),
            "server_security": (
                self.server_policy_manager.generate_server_policy_commands()
            ),
            "defender_policy": (
                self.defender_policy_manager.generate_defender_policy_commands()
            ),
            "account_lockout_policy": (
                self.account_lockout_policy_manager.generate_account_lockout_policy_commands()
            ),
            "audit_policy": (
                self.audit_policy_manager.generate_audit_policy_commands()
            ),
            "powershell_logging": (
                self.powershell_logging_manager.generate_powershell_logging_commands()
            )
        }