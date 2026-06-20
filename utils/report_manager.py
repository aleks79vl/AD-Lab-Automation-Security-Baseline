from pathlib import Path
from datetime import datetime
from typing import Dict, List


class ReportManager:

    def __init__(self):
        self.report_dir = Path("reports")
        self.report_dir.mkdir(exist_ok=True)

    def generate_deployment_report(
        self,
        config: Dict,
        generated_files: List[str],
        validation_status: str
    ) -> Path:
        report_file = self.report_dir / "deployment_report.txt"

        report_content = f"""Deployment Report
=================

Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

Domain: {config.get("domain")}
Domain DN: {config.get("domain_dn")}

OU Count: {len(config.get("ous", []))}
Group Count: {len(config.get("groups", []))}
User Count: {len(config.get("users", []))}
Computer Count: {len(config.get("computers", []))}
Membership Count: {len(config.get("memberships", []))}
GPO Count: {len(config.get("gpos", []))}

Validation Status: {validation_status}

Generated Files:
"""

        for file in generated_files:
            report_content += f"- {file}\n"

        report_file.write_text(report_content)

        return report_file
