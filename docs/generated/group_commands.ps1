New-ADGroup -Name "IT Admins" -GroupScope Global -GroupCategory Security -Path "OU=IT,DC=thm,DC=local"
New-ADGroup -Name "Sales Users" -GroupScope Global -GroupCategory Security -Path "OU=Sales,DC=thm,DC=local"
New-ADGroup -Name "Marketing Users" -GroupScope Global -GroupCategory Security -Path "OU=Marketing,DC=thm,DC=local"
New-ADGroup -Name "Management Users" -GroupScope Global -GroupCategory Security -Path "OU=Management,DC=thm,DC=local"
