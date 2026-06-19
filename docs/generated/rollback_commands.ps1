Remove-ADUser -Identity "claire" -Confirm:$false
Remove-ADUser -Identity "mark" -Confirm:$false
Remove-ADUser -Identity "sophie" -Confirm:$false
Remove-ADUser -Identity "phillip" -Confirm:$false
Remove-ADComputer -Identity "SRV-APP01" -Confirm:$false
Remove-ADComputer -Identity "SRV-FILE01" -Confirm:$false
Remove-ADComputer -Identity "PC-003" -Confirm:$false
Remove-ADComputer -Identity "PC-002" -Confirm:$false
Remove-ADComputer -Identity "PC-001" -Confirm:$false
Remove-ADGroup -Identity "Management Users" -Confirm:$false
Remove-ADGroup -Identity "Marketing Users" -Confirm:$false
Remove-ADGroup -Identity "Sales Users" -Confirm:$false
Remove-ADGroup -Identity "IT Admins" -Confirm:$false
Remove-GPO -Name "Server Baseline" -Confirm:$false
Remove-GPO -Name "Workstation Baseline" -Confirm:$false
Remove-ADOrganizationalUnit -Identity "OU=Workstations,DC=thm,DC=local" -Recursive -Confirm:$false
Remove-ADOrganizationalUnit -Identity "OU=Servers,DC=thm,DC=local" -Recursive -Confirm:$false
Remove-ADOrganizationalUnit -Identity "OU=Management,DC=thm,DC=local" -Recursive -Confirm:$false
Remove-ADOrganizationalUnit -Identity "OU=Marketing,DC=thm,DC=local" -Recursive -Confirm:$false
Remove-ADOrganizationalUnit -Identity "OU=Sales,DC=thm,DC=local" -Recursive -Confirm:$false
Remove-ADOrganizationalUnit -Identity "OU=IT,DC=thm,DC=local" -Recursive -Confirm:$false
Remove-ADOrganizationalUnit -Identity "OU=THM,DC=thm,DC=local" -Recursive -Confirm:$false
