# WinSec Lab - Windows Security Hardening CLI Tool

**Organization:** Cyber Wolf  
**Websites:** [www.cyberwolf.py](http://www.cyberwolf.py) | [www.zh5.club](http://www.zh5.club)  
**Developed by:** Tamilselvan .S, Cyber Security Researcher  
**Lab Type:** Mini Lab

A comprehensive Python-based CLI tool for Windows security checks, system administration, and hardening recommendations. Features interactive ASCII diagrams and detailed system analysis.

## Features

- **System Information** - Detailed hardware and OS details with architecture diagrams
- **Security Status Check** - Comprehensive security assessment with scoring
- **Firewall Configuration** - Analyze firewall rules and profiles
- **User Accounts Audit** - Review accounts, permissions, and security recommendations
- **Windows Update Status** - Check pending updates and service health
- **Service Management** - Monitor critical Windows services
- **Network Security Check** - Analyze network configuration and open ports
- **Hardening Recommendations** - CIS/NIST-aligned security hardening guidelines
- **Generate Security Report** - Export comprehensive security reports

## Quick Start

### From Command Prompt (CMD)
```batch
launch_lab.bat
```

### From PowerShell
```powershell
.\launch_lab.ps1
```

### Direct Python Execution
```bash
python winsec_lab.py
```

## Requirements

- Windows 10/11 or Windows Server 2016+
- Python 3.6 or higher
- Administrator privileges (recommended for full functionality)

## Menu Options

| Option | Feature | Description |
|--------|---------|-------------|
| 1 | System Information | View detailed system specs with ASCII architecture diagram |
| 2 | Security Status Check | Run security checks with pass/fail scoring |
| 3 | Firewall Configuration | Review firewall profiles and rules |
| 4 | User Accounts Audit | Analyze user accounts and privileges |
| 5 | Windows Update Status | Check for pending updates |
| 6 | Service Management | Monitor critical system services |
| 7 | Network Security Check | Analyze network security layers |
| 8 | Hardening Recommendations | View hardening pyramid and guidelines |
| 9 | Generate Security Report | Export findings to text file |
| 0 | Exit | Close the application |

## Interactive Features

### ASCII Diagrams
Each module includes visual ASCII diagrams for better understanding:
- System Architecture diagrams
- Security Dashboards
- Network Layer representations
- Hardening Pyramids

### Navigation
- Press numbers 1-9 to select a module
- Press 0 to exit
- Press Enter to continue after viewing results

## Security Checks Performed

1. **Windows Defender** - Real-time protection status
2. **Firewall Status** - All profile states (Domain/Private/Public)
3. **User Accounts** - Admin vs Standard users, Guest account
4. **UAC Configuration** - User Account Control settings
5. **Windows Updates** - Pending update count
6. **Critical Services** - Defender, Firewall, Update services
7. **Network Ports** - Listening ports and protocols

## Hardening Standards Referenced

- CIS Benchmarks for Windows
- NIST SP 800-171
- DISA STIG Guidelines
- PCI DSS Requirements
- HIPAA Security Standards

## File Structure

```
LAB/
├── winsec_lab.py       # Main CLI application
├── launch_lab.bat      # Windows Command Prompt launcher
├── launch_lab.ps1      # PowerShell launcher
└── README.md           # This file
```

## Sample Output

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                    SECURITY DASHBOARD                                        ║
╚══════════════════════════════════════════════════════════════════════════════╝

  Checking Windows Defender...     [✓ SECURE]
  Checking Firewall Status...      [✓ SECURE]
  Checking Guest Account...        [✓ SECURE]
  Checking UAC Status...           [✓ SECURE]

  Security Score: 100% (4/4 checks passed)

Press Enter to continue...
```

## Troubleshooting

### Python Not Found
- Ensure Python is installed: https://python.org
- Add Python to your system PATH

### Permission Denied
- Run as Administrator for full functionality
- Some checks require elevated privileges

### Command Not Recognized
- Use the batch file for CMD
- Use the PowerShell script for PowerShell
- Or run directly with `python winsec_lab.py`

## License

This tool is for educational and authorized system administration use only.
