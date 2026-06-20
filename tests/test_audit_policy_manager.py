from gpo.audit_policy_manager import AuditPolicyManager


def test_generate_audit_policy_commands():
    policy = {
        "logon_events": True,
        "account_logon_events": True,
        "account_management": True,
        "directory_service_changes": True,
        "policy_changes": True,
        "object_access": True,
        "process_creation": True
    }

    manager = AuditPolicyManager(policy)

    commands = manager.generate_audit_policy_commands()
    combined_commands = "\n".join(commands)

    assert len(commands) == 8
    assert "auditpol /set" in combined_commands
    assert 'subcategory:"Logon"' in combined_commands
    assert 'subcategory:"Credential Validation"' in combined_commands
    assert 'subcategory:"User Account Management"' in combined_commands
    assert 'subcategory:"Security Group Management"' in combined_commands
    assert 'subcategory:"Directory Service Changes"' in combined_commands
    assert 'subcategory:"Audit Policy Change"' in combined_commands
    assert 'subcategory:"File System"' in combined_commands
    assert 'subcategory:"Process Creation"' in combined_commands
    assert "/success:enable" in combined_commands
    assert "/failure:enable" in combined_commands
    