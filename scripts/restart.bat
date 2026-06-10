@echo off
chcp 65001 > nul
cd /d "%~dp0\.."

echo Перезапуск demo-стенда...
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d
echo Готово!
pause