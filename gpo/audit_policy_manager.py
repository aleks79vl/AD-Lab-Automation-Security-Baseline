from typing import Dict, List


class AuditPolicyManager:

    def __init__(self, policy_config: Dict):
        self.policy = policy_config

    def generate_audit_policy_commands(self) -> List[str]:
        commands = []

        if self.policy["logon_events"]:
            commands.append('auditpol /set /subcategory:"Logon" /success:enable /failure:enable')

        if self.policy["account_logon_events"]:
            commands.append('auditpol /set /subcategory:"Credential Validation" /success:enable /failure:enable')

        if self.policy["account_management"]:
            commands.append('auditpol /set /subcategory:"User Account Management" /success:enable /failure:enable')
            commands.append('auditpol /set /subcategory:"Security Group Management" /success:enable /failure:enable')

        if self.policy["directory_service_changes"]:
            commands.append('auditpol /set /subcategory:"Directory Service Changes" /success:enable /failure:enable')

        if self.policy["policy_changes"]:
            commands.append('auditpol /set /subcategory:"Audit Policy Change" /success:enable /failure:enable')

        if self.policy["object_access"]:
            commands.append('auditpol /set /subcategory:"File System" /success:enable /failure:enable')

        if self.policy["process_creation"]:
            commands.append('auditpol /set /subcategory:"Process Creation" /success:enable /failure:enable')

        return commands