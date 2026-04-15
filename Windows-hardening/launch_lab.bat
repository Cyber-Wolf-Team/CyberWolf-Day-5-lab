@echo off
title WinSec Lab - Cyber Wolf Security Lab
cls

echo.
echo  ╔══════════════════════════════════════════════════════════════════════════════╗
echo  ║                                                                              ║
echo  ║              WinSec Lab - Windows Security Hardening Lab                   ║
echo  ║                         Cyber Wolf Mini Lab                                  ║
echo  ║                                                                              ║
echo  ║              www.cyberwolf.py ^| www.zh5.club                                ║
echo  ║                   Developed by Tamilselvan .S                               ║
echo  ║                    Cyber Security Researcher                                 ║
echo  ║                                                                              ║
echo  ╚══════════════════════════════════════════════════════════════════════════════╝
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo.
    echo Please install Python 3.x from https://python.org
    echo.
    pause
    exit /b 1
)

echo [OK] Python detected
echo [OK] Initializing WinSec Lab...
echo.
timeout /t 2 /nobreak >nul

:: Run the lab
python winsec_lab.py

:: Pause on exit
if errorlevel 1 (
    echo.
    echo [ERROR] An error occurred while running the lab.
    pause
)
