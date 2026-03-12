@echo off
echo =======================================
echo Installing ExamAI Coach Dependencies...
echo =======================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH!
    pause
    exit /b
)

echo Installing requirements from requirements.txt...
pip install -r requirements.txt

echo.
echo [SUCCESS] Dependencies installed! You can now use run.cmd to start the app.
pause
