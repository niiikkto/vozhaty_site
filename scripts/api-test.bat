@echo off
cd /d "%~dp0\.."
echo Checking API endpoints with curl...
curl -I http://localhost:8000/
curl -I http://localhost:8000/catalog/
curl -I http://localhost:8000/gallery/
curl -I http://localhost:8000/not-exist/
pause