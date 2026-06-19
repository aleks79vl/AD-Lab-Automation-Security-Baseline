# Project Architecture

## Overview

This project uses a configuration-driven architecture.

The main configuration file is `config.json`.  
Python reads this file and generates PowerShell scripts for Active Directory deployment and security baseline configuration.

## Data Flow

config.json
↓
deploy.py
↓
Manager classes
↓
PowerShell commands
↓
docs/generated/*.ps1

## Main Components

| Component | Responsibility |
|---|---|
| deploy.py | Main deployment orchestrator |
| cleanup.py | Rollback command generator |
| config.json | Infrastructure configuration |
| OUManager | Generates OU creation commands |
| GroupManager | Generates AD group creation commands |
| UserManager | Generates AD user creation commands |
| ComputerManager | Generates AD computer creation commands |
| GroupMembershipManager | Generates user-to-group membership commands |
| GPOManager | Generates GPO creation and linking commands |
| PasswordPolicyManager | Generates domain password policy commands |
| WorkstationPolicyManager | Generates workstation hardening commands |
| ServerPolicyManager | Generates server hardening commands |
| RollbackManager | Generates rollback commands |

## Design Decisions

- Configuration is stored separately from code.
- Each manager has a single responsibility.
- Generated PowerShell scripts can be reviewed before execution.
- Deployment and rollback are separated for safety.
- Logs are generated for audit and troubleshooting.