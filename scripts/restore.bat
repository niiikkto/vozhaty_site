@echo off
chcp 65001 > nul
cd /d "%~dp0\.."

echo Восстановление базы данных SQLite...
echo Список доступных бэкапов в папке backups:
dir backups\*.sqlite /b

set /p BACKUP_FILE="Введите имя файла для восстановления (например, backup_20260611_1430.sqlite): "

if exist "backups\%BACKUP_FILE%" (
    copy /Y "backups\%BACKUP_FILE%" db.sqlite3
    echo ✅ База данных восстановлена из файла: %BACKUP_FILE%
) else (
    echo ❌ Файл не найден!
)
pause