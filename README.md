# AD-Lab-Automation-Security-Baseline

Enterprise-style Active Directory deployment and security baseline automation toolkit.

This project automates the generation of PowerShell commands for Active Directory deployment, security baseline configuration, and rollback operations using a configuration-driven architecture.

---

## Features

- Organizational Unit (OU) deployment
- Active Directory group creation
- Active Directory user creation
- Active Directory computer creation
- Group membership automation
- Group Policy Object (GPO) deployment
- Domain password policy generation
- Workstation security baseline generation
- Server security baseline generation
- Rollback command generation
- Configuration-driven deployment
- Audit logging and reporting

---

## Architecture

```text
config.json
     ↓
deploy.py
     ↓
Managers
     ↓
PowerShell Scripts
     ↓
Active Directory
```

---

## Manager Components

| Component | Responsibility |
|------------|---------------|
| OUManager | Generate OU creation commands |
| GroupManager | Generate AD group creation commands |
| UserManager | Generate AD user creation commands |
| ComputerManager | Generate AD computer creation commands |
| GroupMembershipManager | Generate group membership commands |
| GPOManager | Generate GPO deployment commands |
| PasswordPolicyManager | Generate password policy commands |
| RollbackManager | Generate rollback commands |

---

## Usage

Generate deployment scripts:

```bash
python3 deploy.py
```

Generate rollback scripts:

```bash
python3 cleanup.py
```

Generated PowerShell files are saved to:

```text
docs/generated/
```

Logs are saved to:

```text
logs/
```

---

## Security Baseline

### Password Policy

- Minimum password length: 12 characters
- Password complexity enabled
- Password history: 24 passwords
- Maximum password age: 90 days
- Minimum password age: 1 day
- Account lockout threshold: 5 attempts
- Lockout duration: 30 minutes
- Observation window: 30 minutes

### Workstation Security

- Auto-lock screen after 5 minutes
- Disable Control Panel access
- Disable CMD for standard users
- Restrict PowerShell access

### Server Security

- Auto-lock screen after 5 minutes
- Require SMB signing
- Restrict anonymous enumeration
- Limit blank password usage

---

## Rollback Support

The project generates rollback PowerShell scripts that can remove:

- Organizational Units
- Users
- Groups
- Computers
- GPOs

Rollback scripts are generated separately from deployment scripts to reduce operational risk.

---

## Project Structure

```text
ad/
├── ou_manager.py
├── group_manager.py
├── user_manager.py
├── computer_manager.py
├── group_membership_manager.py

gpo/
├── gpo_manager.py
├── password_policy_manager.py

rollback/
├── rollback_manager.py

docs/
├── generated/
├── project_architecture.md
├── security_baseline.md

logs/
├── ad_creation.log

deploy.py
cleanup.py
config.json
README.md
```

---

## Project Highlights

- Configuration-driven architecture
- Modular manager design
- Security-focused Active Directory automation
- Deployment and rollback separation
- PowerShell command generation
- Audit logging
- Documentation and architecture diagrams

---

## Future Improvements

- Real GPO deployment generation
- Security auditing policies
- Windows Event Log collection
- CIS Benchmark alignment
- Splunk integration
- Security reporting dashboard
- Threat hunting configuration generation

---

## Status

Active development.
Current version includes Active Directory deployment, group management, security baseline generation, rollback support, and audit logging.