@echo off
chcp 65001 > nul
cd /d "%~dp0\.."

echo ========================================
echo  Запуск сервера Вожатка
echo ========================================
call venv\Scripts\activate.bat
python manage.py runserver
pause