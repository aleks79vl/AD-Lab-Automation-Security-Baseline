Set-GPRegistryValue -Name "Workstation Baseline" -Key "HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\System" -ValueName "InactivityTimeoutSecs" -Type DWord -Value 300
Set-GPRegistryValue -Name "Workstation Baseline" -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" -ValueName "NoControlPanel" -Type DWord -Value 1
Set-GPRegistryValue -Name "Workstation Baseline" -Key "HKCU\Software\Policies\Microsoft\Windows\System" -ValueName "DisableCMD" -Type DWord -Value 2
Set-GPRegistryValue -Name "Workstation Baseline" -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" -ValueName "DisallowRun" -Type DWord -Value 1
Set-GPRegistryValue -Name "Workstation Baseline" -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun" -ValueName "1" -Type String -Value "powershell.exe"
Set-GPRegistryValue -Name "Workstation Baseline" -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun" -ValueName "2" -Type String -Value "pwsh.exe"
