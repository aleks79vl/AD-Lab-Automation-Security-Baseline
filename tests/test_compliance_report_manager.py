from utils.compliance_report_manager import ComplianceReportManager


def test_generate_compliance_report():
    security_baseline_commands = {
        "password_policy": ["password command"],
        "workstation_security": ["workstation command"],
        "server_security": ["server command"],
        "defender_policy": ["defender command"],
        "account_lockout_policy": ["lockout command"],
        "audit_policy": ["audit command"],
        "powershell_logging": ["powershell logging command"]
    }

    manager = ComplianceReportManager()

    report_file = manager.generate_compliance_report(
        security_baseline_commands
    )

    report_content = report_file.read_text()

    assert report_file.exists()
    assert "Security Compliance Report" in report_content
    assert "Password Policy" in report_content
    assert "Workstation Security" in report_content
    assert "Server Security" in report_content
    assert "Defender Policy" in report_content
    assert "Account Lockout Policy" in report_content
    assert "Audit Policy" in report_content
    assert "PowerShell Logging" in report_content
    assert "PASS" in report_content
    assert "Compliance Score: 100%" in report_content