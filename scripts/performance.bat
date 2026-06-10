@echo off
cd /d "%~dp0\.."
echo Running Lighthouse via npx (requires Node.js)
npx lighthouse http://localhost:8000 --output html --output-path reports/lighthouse_report.html
echo Report saved to reports/lighthouse_report.html
pause