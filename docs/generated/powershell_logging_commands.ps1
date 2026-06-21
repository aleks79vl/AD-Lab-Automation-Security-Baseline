Set-GPRegistryValue -Name "PowerShell Logging" -Key "HKLM\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ScriptBlockLogging" -ValueName "EnableScriptBlockLogging" -Type DWord -Value 1
Set-GPRegistryValue -Name "PowerShell Logging" -Key "HKLM\SOFTWARE\Policies\Microsoft\Windows\PowerShell\ModuleLogging" -ValueName "EnableModuleLogging" -Type DWord -Value 1
Set-GPRegistryValue -Name "PowerShell Logging" -Key "HKLM\SOFTWARE\Policies\Microsoft\Windows\PowerShell\Transcription" -ValueName "EnableTranscripting" -Type DWord -Value 1
