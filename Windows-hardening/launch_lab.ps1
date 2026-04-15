#requires -Version 3.0
<#
.SYNOPSIS
    WinSec Lab Launcher - PowerShell Edition
    Windows Security Hardening and Administration Console

.DESCRIPTION
    This script launches the WinSec Lab Python CLI tool.
    Provides an enhanced PowerShell experience with colored output.

.EXAMPLE
    .\launch_lab.ps1
    Launches the WinSec Lab interactive console
#>

[CmdletBinding()]
param()

$Host.UI.RawUI.WindowTitle = "WinSec Lab - Cyber Wolf Security Lab"

# WinSec Lab ASCII Banner
$banner = @"

    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                                                                              ║
    ║              WinSec Lab - Windows Security Hardening Lab                     ║
    ║                         Cyber Wolf Mini Lab                                  ║
    ║                                                                              ║
    ║                   www.cyberwolf.py | www.zh5.club                           ║
    ║                      Developed by Tamilselvan .S                            ║
    ║                       Cyber Security Researcher                              ║
    ║                                                                              ║
    ╚══════════════════════════════════════════════════════════════════════════════╝

"@

Write-Host $banner -ForegroundColor Cyan

# Check Python installation
try {
    $pythonVersion = python --version 2>&1
    Write-Host "[OK] Python detected: " -NoNewline -ForegroundColor Green
    Write-Host $pythonVersion -ForegroundColor White
} catch {
    Write-Host "[ERROR] Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.x from https://python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "[OK] Initializing WinSec Lab..." -ForegroundColor Green
Start-Sleep -Seconds 2

# Get script directory
$scriptPath = Split-Path -Parent $MyInvocation.MyCommand.Path
$labScript = Join-Path $scriptPath "winsec_lab.py"

if (-not (Test-Path $labScript)) {
    Write-Host "[ERROR] WinSec Lab script not found: $labScript" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}

# Run the lab
try {
    & python $labScript
} catch {
    Write-Host "[ERROR] Failed to run WinSec Lab: $_" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
