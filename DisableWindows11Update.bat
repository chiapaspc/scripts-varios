@echo off
:: Bloquear actualización a Windows 11 usando el Registro
REG ADD "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate" /v TargetReleaseVersion /t REG_DWORD /d 1 /f
:: Solo se permitira la actualizacion 22H2
REG ADD "HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate" /v TargetReleaseVersionInfo /t REG_SZ /d "22H2" /f

:: Detener y deshabilitar el servicio de Windows Update (opcional)
sc stop wuauserv
sc config wuauserv start=disabled

echo La política de actualización ha sido configurada para quedarse en Windows 10.
echo El servicio de Windows Update ha sido detenido y deshabilitado.
pause