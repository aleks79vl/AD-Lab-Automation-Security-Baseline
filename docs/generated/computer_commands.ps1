New-ADComputer -Name "PC-001" -SamAccountName "PC-001$" -Path "OU=Workstations,DC=thm,DC=local" -Enabled $true
New-ADComputer -Name "PC-002" -SamAccountName "PC-002$" -Path "OU=Workstations,DC=thm,DC=local" -Enabled $true
New-ADComputer -Name "PC-003" -SamAccountName "PC-003$" -Path "OU=Workstations,DC=thm,DC=local" -Enabled $true
New-ADComputer -Name "SRV-FILE01" -SamAccountName "SRV-FILE01$" -Path "OU=Servers,DC=thm,DC=local" -Enabled $true
New-ADComputer -Name "SRV-APP01" -SamAccountName "SRV-APP01$" -Path "OU=Servers,DC=thm,DC=local" -Enabled $true
