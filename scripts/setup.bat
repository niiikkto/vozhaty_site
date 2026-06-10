@echo off
chcp 65001 > nul
cd /d "%~dp0\.."

echo ========================================
echo  Установка проекта Вожатка
echo ========================================

echo 1. Создание виртуального окружения...
python -m venv venv

echo 2. Активация окружения и установка зависимостей...
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
pip install ruff black

echo 3. Выполнение миграций...
python manage.py migrate

echo 4. Готово!
echo Запусти проект командой: scripts\run.bat
pause