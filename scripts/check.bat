@echo off
chcp 65001 > nul
cd /d "%~dp0\.."

echo ========================================
echo  Проверка кода линтером Ruff
echo ========================================
call venv\Scripts\activate.bat
ruff check .
pause