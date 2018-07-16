@echo off
REM Change the range to match what you want to scan below
set RANGE=10.10.11
goto check_Permissions

:check_Permissions
    echo Administrative permissions required. Detecting permissions...

    net session >nul 2>&1
    if %errorLevel% == 0 (
		echo Success: Administrative permissions confirmed.
    ) else (
        echo Failure: Current permissions inadequate. Run as administrator to get full access.
		pause
		exit /B 1
	)
echo This is your range: %RANGE% (it might take a while)
set CURRENTDIRECTORY=%~dp0
set FILELOCATION=%CURRENTDIRECTORY%ipaddresses.txt
echo IP addresses will output to: %FILELOCATION%
break>%FILELOCATION%
start powershell.exe -noprofile -command "&Get-Content -Path \"%FILELOCATION%\" -Wait"
REM pause

for /l %%i in (1, 1, 254) do (
	echo Pinging: %RANGE%.%%i
	ping -n 1 -w 1 %RANGE%.%%i | FIND /i "Reply">>%FILELOCATION%
)