from pathlib import Path


class ComplianceReportManager:

    def generate_compliance_report(self,security_baseline_commands):
        report_lines = []
        report_lines.append("Security Compliance Report")
        report_lines.append("=" * 40)

        checks = {
            "Password Policy":
                len(security_baseline_commands["password_policy"]) > 0,

            "Workstation Security":len(security_baseline_commands["workstation_security"]) > 0,

            "Server Security":
                len(security_baseline_commands["server_security"]) > 0,

            "Defender Policy":len(security_baseline_commands["defender_policy"]) > 0,

            "Account Lockout Policy":len(security_baseline_commands["account_lockout_policy"]) > 0,

            "Audit Policy":len(security_baseline_commands["audit_policy"]) > 0,

            "PowerShell Logging":len(security_baseline_commands["powershell_logging"]) > 0
        }

        passed_checks = 0

        for check_name, result in checks.items():

            status = "PASS" if result else "FAIL"

            if result:
                passed_checks += 1

            report_lines.append(f"{check_name:.<30} {status}")

        score = int((passed_checks / len(checks)) * 100)

        report_lines.append("")
        report_lines.append(f"Compliance Score: {score}%")
        reports_dir = Path("reports")
        reports_dir.mkdir(exist_ok=True)
        report_file = (reports_dir /"security_compliance_report.txt")
        report_file.write_text("\n".join(report_lines))

        return report_file