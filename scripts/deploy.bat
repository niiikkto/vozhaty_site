@echo off
chcp 65001 > nul
cd /d "%~dp0\.."

echo ========================================
echo   Запуск demo-стенда проекта "Вожатка"
echo ========================================
echo.

REM Проверяем, есть ли .env.demo
if not exist .env.demo (
    echo Ошибка: файл .env.demo не найден!
    echo Создайте его из .env.demo.example
    pause
    exit /b 1
)

echo 1. Сборка и запуск контейнеров...
docker compose -f docker-compose.prod.yml up --build -d

echo.
echo 2. Проверка статуса контейнеров...
docker compose -f docker-compose.prod.yml ps

echo.
echo ========================================
echo   Demo-стенд запущен!
echo   Адрес: http://localhost:8000
echo ========================================
pause