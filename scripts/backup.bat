@echo off
chcp 65001 > nul
cd /d "%~dp0\.."

if not exist backups mkdir backups

for /f "tokens=1-4 delims=/:. " %%a in ("%date% %time%") do set TS=%%c%%b%%a_%%d

copy db.sqlite3 backups\backup_%TS%.sqlite

echo ✅ Backup создан: backups\backup_%TS%.sqlite
pause