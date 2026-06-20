from utils.report_manager import ReportManager


def test_generate_deployment_report():
    config = {
        "domain": "thm.local",
        "domain_dn": "DC=thm,DC=local",
        "ous": ["IT", "Sales"],
        "groups": [{"name": "IT Admins"}],
        "users": [{"username": "phillip"}],
        "computers": [{"name": "PC-001"}],
        "memberships": [{"user": "phillip", "group": "IT Admins"}],
        "gpos": [{"name": "Workstation Baseline"}]
    }

    generated_files = [
        "ou_commands.ps1",
        "user_commands.ps1"
    ]

    manager = ReportManager()

    report_file = manager.generate_deployment_report(
        config,
        generated_files,
        "SUCCESS"
    )

    report_content = report_file.read_text()

    assert report_file.exists()
    assert "Deployment Report" in report_content
    assert "Domain: thm.local" in report_content
    assert "Domain DN: DC=thm,DC=local" in report_content
    assert "OU Count: 2" in report_content
    assert "Group Count: 1" in report_content
    assert "User Count: 1" in report_content
    assert "Computer Count: 1" in report_content
    assert "Membership Count: 1" in report_content
    assert "GPO Count: 1" in report_content
    assert "Validation Status: SUCCESS" in report_content
    assert "- ou_commands.ps1" in report_content
    assert "- user_commands.ps1" in report_content
    