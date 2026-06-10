@echo off
chcp 65001 > nul
cd /d "%~dp0\.."

echo ========================================
echo   Статус контейнеров:
echo ========================================
docker compose -f docker-compose.prod.yml ps

echo.
echo ========================================
echo   Последние логи (80 строк):
echo ========================================
docker compose -f docker-compose.prod.yml logs --tail=80

pause