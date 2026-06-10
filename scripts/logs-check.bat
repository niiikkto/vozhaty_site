@echo off
cd /d "%~dp0\.."
echo Saving last 50 lines of Docker logs...
docker compose logs --tail=50 > reports/logs_tail.txt
echo Logs saved to reports/logs_tail.txt
pause