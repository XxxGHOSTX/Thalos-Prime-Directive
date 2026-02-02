@echo off
REM © 2026 Tony Ray Macier III. All rights reserved.
REM Thalos Prime™ is a proprietary system.

REM Thalos Prime Web Deployment Startup Script
REM Production-ready launcher for Windows

echo ╔══════════════════════════════════════════════════════════════════╗
echo ║                                                                  ║
echo ║  ████████╗██╗  ██╗ █████╗ ██╗      ██████╗ ███████╗            ║
echo ║  ╚══██╔══╝██║  ██║██╔══██╗██║     ██╔═══██╗██╔════╝            ║
echo ║     ██║   ███████║███████║██║     ██║   ██║███████╗            ║
echo ║     ██║   ██╔══██║██╔══██║██║     ██║   ██║╚════██║            ║
echo ║     ██║   ██║  ██║██║  ██║███████╗╚██████╔╝███████║            ║
echo ║     ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝            ║
echo ║                                                                  ║
echo ║              PRIME v3.0 - WEB DEPLOYMENT EDITION                ║
echo ║          Synthetic Biological Intelligence System               ║
echo ║                                                                  ║
echo ║        © 2026 Tony Ray Macier III. All rights reserved.        ║
echo ║                                                                  ║
echo ╚══════════════════════════════════════════════════════════════════╝
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.12+
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo ✓ Python found: %PYTHON_VERSION%
echo.

REM Check/install dependencies
echo 📦 Checking dependencies...
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo Installing Flask...
    pip install -q flask flask-cors
)

python -c "import numpy" >nul 2>&1
if errorlevel 1 (
    echo Installing NumPy...
    pip install -q numpy scipy
)

echo ✓ All dependencies ready
echo.

REM Create necessary directories
if not exist data mkdir data
if not exist logs mkdir logs
if not exist data\storage mkdir data\storage
echo ✓ Data directories ready
echo.

REM Setup environment
if not exist .env (
    echo 📝 Creating .env configuration...
    copy .env.example .env >nul
    echo ✓ Environment configured
) else (
    echo ✓ Environment already configured
)
echo.

REM Start the web interface
echo 🚀 Starting Thalos Prime Web Interface...
echo ==================================================================
echo.

REM Use boot_thalos.py for the immersive experience
python boot_thalos.py
