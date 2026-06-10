@echo off
chcp 65001 > nul
cd /d "%~dp0\.."

echo ========================================
echo  Запуск проекта в Docker
echo ========================================
docker compose up --build
pause