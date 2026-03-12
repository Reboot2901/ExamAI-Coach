@echo off
echo =======================================
echo Starting ExamAI Coach...
echo =======================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not installed or not in PATH!
    pause
    exit /b
)

:: Run the Streamlit app
echo Launching Streamlit server...
streamlit run app.py

pause
