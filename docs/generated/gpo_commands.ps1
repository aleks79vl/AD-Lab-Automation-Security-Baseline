New-GPO -Name "Workstation Baseline"
New-GPLink -Name "Workstation Baseline" -Target "OU=Workstations,DC=thm,DC=local"
New-GPO -Name "Server Baseline"
New-GPLink -Name "Server Baseline" -Target "OU=Servers,DC=thm,DC=local"
