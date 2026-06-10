@echo off
cd /d "%~dp0\.."
echo ========================================
echo Quality check for Vozhaty project
echo ========================================
call scripts\test.bat
call scripts\api-test.bat
call scripts\logs-check.bat
echo Quality check completed.
pause