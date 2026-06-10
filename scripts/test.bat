@echo off
cd /d "%~dp0\.."
echo Running smoke tests...
pytest tests/smoke/ -v
pause