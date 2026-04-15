# Day 5 - Cyber Wolf Internship Lab Setup

**Organization:** Cyber Wolf  
**Websites:** [www.cyberwolf.py](http://www.cyberwolf.py) | [www.zh5.club](http://www.zh5.club)  
**Developer:** Tamilselvan .S, Cyber Security Researcher  
**Lab Type:** Mini Lab - Local Environment

---

## Overview

Welcome to **Day 5** of the Cyber Wolf Internship Program. This lab setup provides hands-on CLI tools for learning Windows hardening and Linux fundamentals. Both labs feature interactive ASCII diagrams, press Enter navigation, and comprehensive command references.

---

## Lab Structure

```
README.md            ← You are here
├                 
│
├── Windows-hardening/           # Windows Security Lab
│   ├── winsec_lab.py           # Main CLI application
│   ├── launch_lab.bat          # CMD launcher
│   ├── launch_lab.ps1          # PowerShell launcher
│   ├── requirements.txt        # Dependencies
│   └── README.md               # Windows lab documentation
│
└── Linux-basics/                # Kali Linux Lab
    ├── kalilab.py              # Main CLI application
    ├── launch_lab.sh           # Bash launcher
    ├── requirements.txt        # Dependencies
    └── README.md               # Linux lab documentation
```

---

## Quick Start Guide

### For Windows Users

**Prerequisites:**
- Windows 10/11 or Windows Server 2016+
- Python 3.6+
- Administrator privileges (recommended)

**Launch Methods:**

| Method | Command |
|--------|---------|
| **CMD** | `cd Windows-hardening && launch_lab.bat` |
| **PowerShell** | `cd Windows-hardening; .\launch_lab.ps1` |
| **Python Direct** | `python Windows-hardening\winsec_lab.py` |

**Windows Lab Features:**
- 🔒 System Information with architecture diagrams
- 🔒 Security Status Check with scoring
- 🔒 Firewall Configuration analysis
- 🔒 User Accounts Audit
- 🔒 Windows Update Status
- 🔒 Service Management
- 🔒 Network Security Check
- 🔒 Hardening Recommendations (CIS/NIST aligned)
- 🔒 Generate Security Reports

---

### For Linux/Kali Users

**Prerequisites:**
- Kali Linux or Debian-based distribution
- Python 3.6+
- Terminal with color support

**Launch Methods:**

| Method | Command |
|--------|---------|
| **Bash Launcher** | `cd Linux-basics && chmod +x launch_lab.sh && ./launch_lab.sh` |
| **Python Direct** | `python3 Linux-basics/kalilab.py` |

**Linux Lab Features:**
- 📁 Linux Core Commands (ls, cd, pwd, cat, etc.)
- 📁 File System Navigation (FHS hierarchy)
- 📁 File Permissions & Ownership (chmod, chown)
- 📁 Process Management (ps, top, kill, jobs)
- 📁 User & Group Management (sudo, users)
- 📁 Package Management (APT, dpkg)
- 📁 Network Commands (ip, ping, nmap, netstat)
- 📁 Text Processing Tools (grep, sed, awk)
- 📁 System Information

---

## Navigation Instructions

### How to Use Both Labs

1. **Start the Lab:** Use the appropriate launcher for your OS
2. **View Menu:** The main menu will display with numbered options
3. **Select Module:** Enter the number (1-9) and press **Enter**
4. **View Content:** Read the information and ASCII diagrams
5. **Continue:** Press **Enter** to return to main menu
6. **Exit:** Press **0** to exit the lab

### Common Navigation Keys

| Key | Action |
|-----|--------|
| `1-9` | Select module |
| `0` | Exit application |
| `Enter` | Continue / Return to menu |
| `Ctrl+C` | Force exit |

---

## Lab Modules Reference

### Windows Hardening Lab (9 Modules)

| # | Module | Description |
|---|--------|-------------|
| 1 | System Information | Hardware, OS details, architecture diagrams |
| 2 | Security Status Check | Security scoring with pass/fail results |
| 3 | Firewall Configuration | Domain/Private/Public profile analysis |
| 4 | User Accounts Audit | Admin vs Standard users, Guest account |
| 5 | Windows Update Status | Pending updates and service health |
| 6 | Service Management | Critical Windows services status |
| 7 | Network Security Check | Open ports, protocols, network layers |
| 8 | Hardening Recommendations | CIS/NIST/DISA hardening pyramid |
| 9 | Generate Security Report | Export findings to text file |

### Linux Basics Lab (9 Modules)

| # | Module | Description |
|---|--------|-------------|
| 1 | Linux Core Commands | Essential file and directory commands |
| 2 | File System Navigation | Linux FHS and navigation shortcuts |
| 3 | File Permissions & Ownership | chmod numeric/symbolic, special permissions |
| 4 | Process Management | Process lifecycle, ps, top, kill, bg/fg |
| 5 | User & Group Management | users, sudo, /etc/passwd structure |
| 6 | Package Management (APT) | apt, dpkg, Kali tool sets |
| 7 | Network Commands | ip, ping, nmap, tcpdump for security |
| 8 | Text Processing Tools | grep, sed, awk, sort, uniq pipelines |
| 9 | System Information | uname, lscpu, systemctl services |

---

## Important URLs & Resources

### Cyber Wolf Official

| Resource | URL | Purpose |
|----------|-----|---------|
| **Main Website** | www.cyberwolf.py | Organization portal |
| **Community** | www.zh5.club | Internship community |
| **Developer** | Tamilselvan .S | Lab creator |

### External References

| Standard | URL | Purpose |
|----------|-----|---------|
| **CIS Benchmarks** | https://www.cisecurity.org/cis-benchmarks | Windows hardening standards |
| **NIST 800-171** | https://csrc.nist.gov/publications/detail/sp/800-171/final | Security requirements |
| **DISA STIGs** | https://public.cyber.mil/stigs/ | DoD hardening guidelines |
| **Linux FHS** | https://refspecs.linuxfoundation.org/fhs.shtml | Filesystem hierarchy |
| **Kali Docs** | https://www.kali.org/docs/ | Kali Linux documentation |

---

## Dependencies

### Windows Lab
```
Python >= 3.6
Standard library only (os, sys, subprocess, platform, json, datetime, typing)
No external packages required
```

### Linux Lab
```
Python >= 3.6
Standard library only (os, sys, subprocess, platform, pwd, grp, datetime, typing)
No external packages required
```

---

## Installation & Setup

### Step 1: Download the Lab
Clone or download the LAB folder to your local machine.

### Step 2: Verify Python

**Windows:**
```cmd
python --version
```

**Linux:**
```bash
python3 --version
```

### Step 3: Run the Lab

Choose your operating system and run the appropriate launcher:

**Windows:**
```cmd
cd Windows-hardening
launch_lab.bat
```

**Linux:**
```bash
cd Linux-basics
chmod +x launch_lab.sh
./launch_lab.sh
```

---

## Troubleshooting

### Windows Issues

| Issue | Solution |
|-------|----------|
| Python not found | Install Python 3.6+ from python.org |
| Permission denied | Run as Administrator |
| Colors not showing | Use Windows Terminal or modern CMD |
| Commands fail | Check Windows version compatibility |

### Linux Issues

| Issue | Solution |
|-------|----------|
| Python not found | `sudo apt update && sudo apt install python3` |
| Permission denied | `chmod +x launch_lab.sh` |
| Import errors | Ensure you're using Python 3, not Python 2 |
| Display issues | Check terminal supports ANSI colors |

---

## Learning Path for Interns

### Week 1: Windows Security
- Day 1-2: Run all Windows lab modules
- Day 3-4: Practice commands in real Windows environment
- Day 5: Review hardening recommendations

### Week 2: Linux Fundamentals
- Day 1-3: Run all Linux lab modules
- Day 4-5: Practice commands in Kali VM

### Week 3: Practical Application
- Apply Windows hardening on test VM
- Practice Linux commands for CTF challenges
- Document findings and generate reports

---

## Contributing

This lab is part of the Cyber Wolf Internship Program. For updates or suggestions:

1. Contact: Tamilselvan .S
2. Website: www.cyberwolf.py
3. Community: www.zh5.club

---

## License & Disclaimer

**For Educational Purposes Only**

These labs are designed for educational and authorized system administration use only. Always:
- Practice in isolated environments
- Obtain proper authorization before testing
- Follow ethical hacking guidelines
- Comply with organizational security policies

---

## Info

**Developed by:** Tamilselvan .S  
**Title:** Cyber Security Researcher  
**Organization:** Cyber Wolf  
**Lab Type:** Mini Lab - Local Environment  
**Version:** Day 5 Internship Setup

---

**© Cyber Wolf - All Rights Reserved**

**Stay Secure. Stay Updated. Stay Vigilant.**
