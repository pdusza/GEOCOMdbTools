@echo off
echo STOP aller unn�tigen Dienste
rem net stop "SQL Full-text Filter Daemon Launcher (SQLEXPRESS)"
net stop "SQL Server (SQLEXPRESS)"
net stop "SQL Server Browser"
net stop "SQL Server VSS Writer"
rem cls
echo ==================================================
echo ==================================================
echo ==================================================
echo schliessen falls KEIN restart der Dienste
echo sonst irgend eine Taste
pause
cls
echo START aller unn�tigen Dienste
rem net start "SQL Full-text Filter Daemon Launcher (SQLEXPRESS)"
net start "SQL Server (SQLEXPRESS)"
net start "SQL Server Browser"
net start "SQL Server VSS Writer"
pause
