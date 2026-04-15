#!/bin/bash
# Kali Linux Basics Lab Launcher
# Organization: Cyber Wolf
# Websites: www.cyberwolf.py | www.zh5.club
# Developer: Tamilselvan .S, Cyber Security Researcher

clear

echo ""
echo "  ╔══════════════════════════════════════════════════════════════════════════════╗"
echo "  ║                                                                              ║"
echo "  ║              Kali Linux Basics Lab - Command Laboratory                      ║"
echo "  ║                         Cyber Wolf Mini Lab                                  ║"
echo "  ║                                                                              ║"
echo "  ║              www.cyberwolf.py | www.zh5.club                                ║"
echo "  ║                   Developed by Tamilselvan .S                               ║"
echo "  ║                    Cyber Security Researcher                                 ║"
echo "  ║                                                                              ║"
echo "  ╚══════════════════════════════════════════════════════════════════════════════╝"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo ""
    echo "Please install Python 3:"
    echo "  sudo apt update"
    echo "  sudo apt install python3"
    echo ""
    read -p "Press Enter to exit..."
    exit 1
fi

echo "[OK] Python 3 detected"
echo "[OK] Initializing Kali Linux Basics Lab..."
echo ""
sleep 2

# Run the lab
python3 kalilab.py

# Check exit status
if [ $? -ne 0 ]; then
    echo ""
    echo "[ERROR] An error occurred while running the lab."
    read -p "Press Enter to exit..."
fi
