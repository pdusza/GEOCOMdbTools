@echo off
@rem http://blog.alekel.de/-p=175
@echo =========  Firewallmodifikation für den SQL-Servers 2008R2  ===================
@echo === activated ===
@echo Enabling SQLServer default instance port 1433
netsh advfirewall firewall add rule name="SQLServer" dir=in action=allow protocol=TCP localport=1433

@echo Enabling port for SQL Server Browser Service's 'Browse' Button
netsh advfirewall firewall add rule name="SQL Admin Connection" dir=in action=allow protocol=TCP localport=1434

@echo Enabling von Port 1434 UDP für den SQL Browser Service
netsh advfirewall firewall add rule name="SQL Browser" dir=in action=allow protocol=UDP localport=1434

@echo Enabling conventional SQL Server Service Broker port 4022
netsh advfirewall firewall add rule name="SQL Service Broker" dir=in action=allow protocol=TCP localport=4022

@echo Enabling Transact-SQL Debugger/RPC port 135
netsh advfirewall firewall add rule name="SQL-Debugger/RPC" dir=in action=allow protocol=TCP localport=135

@echo Allowing multicast broadcast response on UDP (Browser Service Enumerations OK)
netsh advfirewall set multicastbroadcastresponse ENABLE

rem @echo =========  Ports for the Analysedienste  ==============
rem @echo Enabling SSAS-Standard Instance Port 2383
rem netsh advfirewall firewall add rule name="Analysis Services" dir=in action=allow protocol=TCP localport=2382
rem 
rem @echo Enabling SQL Server Browser Service Port 2382
rem netsh advfirewall firewall add rule name="SQL Browser for Analysis Services" dir=in action=allow protocol=TCP localport=2382
rem 
rem @echo =========  Ports for the Report Service  ==============
rem @echo Enabling HTTP Report Service port 80
rem netsh advfirewall firewall add rule name="HTTP Report Service" dir=in action=allow protocol=TCP localport=80
rem @echo Enabling HTTPS Report Service Port 443
rem netsh advfirewall firewall add rule name="HTTPS Report Service" dir=in action=allow protocol=TCP localport=443
rem 
rem @echo === not activated / Info ===
rem @echo Enabling Mirroring 
rem rem netsh advfirewall firewall add rule name="Mirroring EndPoint" dir=in action=allow protocol=TCP localport=5022
pause
