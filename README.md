# AD-Lab-Automation-Security-Baseline

E# AD-Lab-Automation-Security-Baseline

Enterprise-style Active Directory deployment and security baseline automation toolkit.

This project automates the generation of PowerShell commands for Active Directory deployment, security baseline configuration, and rollback operations using a configuration-driven architecture.

---

## Features

- Organizational Unit (OU) deployment
- Active Directory Group creation
- Active Directory User creation
- Active Directory Computer creation
- Group Membership automation
- Group Policy Object (GPO) deployment
- Domain Password Policy generation
- Workstation Security Baseline generation
- Server Security Baseline generation
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

### Manager Components

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

## Project Highlights

- Configuration-driven architecture
- Modular manager design
- Security-focused Active Directory automation
- Deployment and rollback separation
- PowerShell command generation
- Audit logging
- Documentation and architecture diagrams



## Project Goals

This project automates the deployment and configuration of a Windows Active Directory lab environment using Python and PowerShell.

The toolkit is designed to:

- Create Organizational Units (OUs)
- Create Security Groups
- Create User Accounts
- Create Computer Accounts
- Deploy Group Policy Objects (GPOs)
- Apply Security Baselines
- Generate Audit Logs
- Support Rollback Operations

---

## Technologies

- Python 3
- PowerShell
- Active Directory
- Group Policy
- Windows Server
- Git
- GitHub

---

## Planned Features

### Active Directory

- OU deployment
- User creation
- Group creation
- Computer account creation

### Group Policy

- Restrict Control Panel
- Auto Lock Screen
- Password Policy
- Account Lockout Policy

### Security

- Logging
- Auditing
- Validation
- Rollback

---

## Project Structure

```text
ad/
gpo/
rollback/
utils/
logs/
docs/
screenshots/
```

---

## Status

Project in development.
