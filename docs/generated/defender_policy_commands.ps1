Set-GPRegistryValue -Name "Defender Baseline" -Key "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" -ValueName "DisableRealtimeMonitoring" -Type DWord -Value 0
Set-GPRegistryValue -Name "Defender Baseline" -Key "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet" -ValueName "SpynetReporting" -Type DWord -Value 2
Set-GPRegistryValue -Name "Defender Baseline" -Key "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Spynet" -ValueName "SubmitSamplesConsent" -Type DWord -Value 1
Set-GPRegistryValue -Name "Defender Baseline" -Key "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" -ValueName "DisableBehaviorMonitoring" -Type DWord -Value 0
Set-GPRegistryValue -Name "Defender Baseline" -Key "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" -ValueName "DisableScriptScanning" -Type DWord -Value 0
