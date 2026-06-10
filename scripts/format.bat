@echo off
chcp 65001 > nul
cd /d "%~dp0\.."

echo ========================================
echo  Форматирование кода через Black
echo ========================================
call venv\Scripts\activate.bat
black .
pause