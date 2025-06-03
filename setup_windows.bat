@echo off
REM Setup script for Windows users

echo Setting up Student Feedback System...

REM Check if Python is installed
python --version >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not in PATH. Please install Python 3.8 or higher.
    exit /b
)

REM Check if virtual environment exists
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Prompt user to configure .env file
if not exist .env (
    echo Creating .env file from template...
    copy .env.example .env
    
    REM Generate secret key
    echo Generating SECRET_KEY...
    python generate_secret_key.py
    
    echo.
    echo IMPORTANT: Edit the .env file and update the SECRET_KEY with the one generated above.
    echo.
    pause
)

REM Initialize the project
echo Initializing the project...
python init_project.py

echo.
echo Setup complete! Run 'python manage.py runserver' to start the development server.
echo Access the application at http://127.0.0.1:8000/
echo.

pause
