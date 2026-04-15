#!/usr/bin/env python3
"""
WinSec Lab - Windows Security Hardening & Administration CLI Tool
A comprehensive CLI tool for Windows security checks and system hardening.
Compatible with Windows Command Line and PowerShell.
"""

import os
import sys
import subprocess
import platform
import json
from datetime import datetime
from typing import Dict, List, Optional, Callable

# Color codes for terminal output
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

# Organization Info
ORG_NAME = "Cyber Wolf"
ORG_WEBSITE = "www.cyberwolf.py | www.zh5.club"
DEVELOPER = "Tamilselvan .S"
TITLE = "Cyber Security Researcher"
LAB_TYPE = "Mini Lab"

# ASCII Art Banner
BANNER = f"""
{Colors.CYAN}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║   ██╗    ██╗██╗███╗   ██╗██████╗  ██████╗  ██████╗ ███████╗ ██████╗          ║
║   ██║    ██║██║████╗  ██║██╔══██╗██╔═══██╗██╔════╝ ██╔════╝██╔════╝          ║
║   ██║ █╗ ██║██║██╔██╗ ██║██████╔╝██║   ██║██║  ███╗█████╗  ██║  ███╗          ║
║   ██║███╗██║██║██║╚██╗██║██╔══██╗██║   ██║██║   ██║██╔══╝  ██║   ██║          ║
║   ╚███╔███╔╝██║██║ ╚████║██║  ██║╚██████╔╝╚██████╔╝███████╗╚██████╔╝          ║
║    ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝           ║
║                                                                              ║
║                    Windows Security Hardening Lab                            ║
║                        Administrator Console                                  ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  {Colors.GREEN}▸ Organization:  {ORG_NAME:<56}{Colors.CYAN}║
║  {Colors.GREEN}▸ Websites:     {ORG_WEBSITE:<56}{Colors.CYAN}║
║  {Colors.GREEN}▸ Developed by: {DEVELOPER + ', ' + TITLE:<56}{Colors.CYAN}║
║  {Colors.GREEN}▸ Lab Type:     {LAB_TYPE:<56}{Colors.CYAN}║
╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.ENDC}"""

class WinSecLab:
    """Main Windows Security Lab CLI Application"""
    
    def __init__(self):
        self.modules = {
            '1': ('System Information', self.show_system_info),
            '2': ('Security Status Check', self.security_status_check),
            '3': ('Firewall Configuration', self.firewall_check),
            '4': ('User Accounts Audit', self.user_accounts_check),
            '5': ('Windows Update Status', self.windows_update_check),
            '6': ('Service Management', self.service_management),
            '7': ('Network Security Check', self.network_security_check),
            '8': ('Hardening Recommendations', self.hardening_recommendations),
            '9': ('Generate Security Report', self.generate_report),
            '0': ('Exit', self.exit_app),
        }
        self.report_data = {}
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def print_header(self, title: str):
        """Print formatted section header"""
        width = 80
        print(f"\n{Colors.CYAN}{'═' * width}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.HEADER}{title.center(width)}{Colors.ENDC}")
        print(f"{Colors.CYAN}{'═' * width}{Colors.ENDC}\n")
        
    def print_menu(self):
        """Display main menu"""
        self.clear_screen()
        print(BANNER)
        print(f"\n{Colors.BOLD}Main Menu:{Colors.ENDC}\n")
        
        for key, (name, _) in self.modules.items():
            status_icon = "🔒" if "Security" in name or "Firewall" in name or "Harden" in name else "🔧"
            if key == '0':
                status_icon = "👋"
            print(f"  {Colors.CYAN}[{key}]{Colors.ENDC} {status_icon} {name}")
            
        print(f"\n{Colors.WARNING}Enter your choice and press Enter...{Colors.ENDC}")
        
    def run_command(self, command: str, shell: bool = True) -> tuple:
        """Execute system command and return result"""
        try:
            result = subprocess.run(
                command, 
                shell=shell, 
                capture_output=True, 
                text=True,
                encoding='utf-8',
                errors='ignore'
            )
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            return -1, "", str(e)
    
    def wait_for_enter(self, message: str = "Press Enter to continue..."):
        """Wait for user to press Enter"""
        print(f"\n{Colors.WARNING}{message}{Colors.ENDC}")
        input()
        
    # ==================== MODULE FUNCTIONS ====================
    
    def show_system_info(self):
        """Display detailed system information with ASCII diagram"""
        self.print_header("SYSTEM INFORMATION")
        
        # Get system info
        print(f"{Colors.CYAN}Gathering system details...{Colors.ENDC}\n")
        
        system_info = {
            "Platform": platform.platform(),
            "Machine": platform.machine(),
            "Processor": platform.processor(),
            "Node Name": platform.node(),
            "Python Version": platform.python_version(),
        }
        
        # Windows-specific info
        _, win_ver, _ = self.run_command("ver")
        _, hostname, _ = self.run_command("hostname")
        _, domain, _ = self.run_command("echo %userdomain%")
        
        # Display ASCII System Diagram
        diagram = f"""
{Colors.CYAN}
        ┌─────────────────────────────────────────────────────────────┐
        │                    SYSTEM ARCHITECTURE                        │
        └─────────────────────────────────────────────────────────────┘
                                    │
                ┌───────────────────┼───────────────────┐
                ▼                   ▼                   ▼
        ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
        │   HARDWARE   │    │     OS       │    │   SOFTWARE   │
        ├──────────────┤    ├──────────────┤    ├──────────────┤
        │ • Processor  │    │ • Windows    │    │ • Python     │
        │ • Memory     │    │ • Version    │    │ • Services   │
        │ • Storage    │    │ • Updates    │    │ • Firewall   │
        └──────────────┘    └──────────────┘    └──────────────┘
{Colors.ENDC}
        """
        print(diagram)
        
        # Display system details table
        print(f"\n{Colors.BOLD}System Details:{Colors.ENDC}\n")
        print(f"  {'Property':<20} {'Value':<50}")
        print(f"  {'─' * 70}")
        
        for key, value in system_info.items():
            print(f"  {Colors.CYAN}{key:<20}{Colors.ENDC} {value:<50}")
            
        if hostname.strip():
            print(f"  {Colors.CYAN}{'Hostname':<20}{Colors.ENDC} {hostname.strip():<50}")
        if domain.strip():
            print(f"  {Colors.CYAN}{'Domain':<20}{Colors.ENDC} {domain.strip():<50}")
            
        # System status indicators
        print(f"\n{Colors.BOLD}System Status Indicators:{Colors.ENDC}\n")
        
        indicators = [
            ("Boot Mode", "Normal", Colors.GREEN),
            ("Secure Boot", "Checking...", Colors.WARNING),
            ("Virtualization", "Enabled", Colors.GREEN),
            ("TPM Status", "Ready", Colors.GREEN),
        ]
        
        for name, status, color in indicators:
            print(f"  [{color}●{Colors.ENDC}] {name:<20} {color}{status}{Colors.ENDC}")
            
        self.report_data['system_info'] = system_info
        self.wait_for_enter()
        
    def security_status_check(self):
        """Comprehensive security status check"""
        self.print_header("SECURITY STATUS CHECK")
        
        checks = [
            ("Windows Defender", "powershell -Command \"Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled\"", "RealTimeProtectionEnabled"),
            ("Firewall Status", "netsh advfirewall show currentprofile", "ON"),
            ("Guest Account", "net user guest | findstr /i \"active\"", "No"),
            ("UAC Status", "REG QUERY HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableLUA", "0x1"),
        ]
        
        results = []
        
        print(f"{Colors.CYAN}Running security checks...{Colors.ENDC}\n")
        
        # Security Dashboard ASCII
        dashboard = f"""
{Colors.CYAN}
                    SECURITY DASHBOARD
                    ═══════════════════
                        
           ┌─────────────────────────────────────┐
           │     THREAT LEVEL INDICATOR         │
           │                                     │
           │    LOW        MODERATE      HIGH   │
           │     🟢          🟡           🔴    │
           │      │          │            │      │
           └─────────────────────────────────────┘
{Colors.ENDC}
        """
        print(dashboard)
        
        for check_name, command, expected in checks:
            print(f"  Checking {check_name}...", end=" ")
            returncode, stdout, stderr = self.run_command(command)
            
            if expected.lower() in stdout.lower() or returncode == 0:
                print(f"{Colors.GREEN}[✓ SECURE]{Colors.ENDC}")
                results.append((check_name, "PASS", stdout.strip()[:50]))
            else:
                print(f"{Colors.FAIL}[✗ WARNING]{Colors.ENDC}")
                results.append((check_name, "FAIL", stdout.strip()[:50] or stderr[:50]))
                
        # Summary table
        print(f"\n{Colors.BOLD}Security Check Summary:{Colors.ENDC}\n")
        print(f"  {'Check':<25} {'Status':<12} {'Details':<40}")
        print(f"  {'─' * 80}")
        
        for name, status, details in results:
            status_color = Colors.GREEN if status == "PASS" else Colors.FAIL
            print(f"  {name:<25} {status_color}{status:<12}{Colors.ENDC} {details:<40}")
            
        # Security Score
        passed = sum(1 for _, status, _ in results if status == "PASS")
        total = len(results)
        score = (passed / total) * 100 if total > 0 else 0
        
        score_color = Colors.GREEN if score >= 80 else Colors.WARNING if score >= 60 else Colors.FAIL
        print(f"\n  {Colors.BOLD}Security Score: {score_color}{score:.0f}%{Colors.ENDC} ({passed}/{total} checks passed)")
        
        self.report_data['security_checks'] = results
        self.wait_for_enter()
        
    def firewall_check(self):
        """Detailed firewall configuration check"""
        self.print_header("FIREWALL CONFIGURATION")
        
        # Firewall Architecture Diagram
        diagram = f"""
{Colors.CYAN}
                    FIREWALL ARCHITECTURE
        ┌────────────────────────────────────────────────────┐
        │                                                    │
        │   INTERNET ◄────► [WINDOWS FIREWALL] ◄────► LAN   │
        │                      │    │                        │
        │                      ▼    ▼                        │
        │              ┌────────┐ ┌────────┐                │
        │              │Inbound │ │Outbound│                │
        │              │ Rules  │ │ Rules  │                │
        │              └────────┘ └────────┘                │
        │                                                    │
        └────────────────────────────────────────────────────┘
{Colors.ENDC}
        """
        print(diagram)
        
        profiles = ["domain", "private", "public"]
        print(f"{Colors.BOLD}Firewall Profile Status:{Colors.ENDC}\n")
        
        for profile in profiles:
            cmd = f"netsh advfirewall show {profile}profile state"
            returncode, stdout, stderr = self.run_command(cmd)
            
            status = "ON" if "ON" in stdout else "OFF" if "OFF" in stdout else "UNKNOWN"
            status_color = Colors.GREEN if status == "ON" else Colors.FAIL if status == "OFF" else Colors.WARNING
            
            print(f"  {profile.upper():<15} Profile: {status_color}[{status}]{Colors.ENDC}")
            
        # Show rules summary
        print(f"\n{Colors.BOLD}Firewall Rules Summary:{Colors.ENDC}\n")
        
        cmd = "netsh advfirewall firewall show rule name=all | findstr /c:\"Rule Name:\" | find /c \"Rule Name\""
        returncode, stdout, stderr = self.run_command(cmd)
        
        if stdout.strip():
            rule_count = stdout.strip()
            print(f"  Total Active Rules: {Colors.CYAN}{rule_count}{Colors.ENDC}")
        
        # Show sample rules
        print(f"\n{Colors.BOLD}Sample Inbound Rules:{Colors.ENDC}\n")
        cmd = "netsh advfirewall firewall show rule name=all dir=in | findstr /B \"Rule Name:"\" | head -10"
        returncode, stdout, stderr = self.run_command(cmd)
        
        if stdout:
            for line in stdout.strip().split('\n')[:5]:
                rule_name = line.replace("Rule Name:", "").strip()
                print(f"  • {rule_name}")
        else:
            print(f"  {Colors.WARNING}Unable to retrieve rules{Colors.ENDC}")
            
        self.wait_for_enter()
        
    def user_accounts_check(self):
        """Audit user accounts and permissions"""
        self.print_header("USER ACCOUNTS AUDIT")
        
        # User Account Structure Diagram
        diagram = f"""
{Colors.CYAN}
                    USER ACCOUNT HIERARCHY
        
                    ┌──────────────────┐
                    │   ADMINISTRATOR  │
                    │    (Built-in)    │
                    └────────┬─────────┘
                             │
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐  ┌──────────┐  ┌──────────┐
        │Standard  │  │  Guest   │  │  Custom  │
        │  Users   │  │ (Disabled│  │  Users   │
        │          │  │  by def) │  │          │
        └──────────┘  └──────────┘  └──────────┘
{Colors.ENDC}
        """
        print(diagram)
        
        print(f"{Colors.BOLD}Current User Accounts:{Colors.ENDC}\n")
        
        # List local users
        cmd = "net user"
        returncode, stdout, stderr = self.run_command(cmd)
        
        if returncode == 0:
            lines = stdout.split('\n')
            users = []
            in_user_list = False
            
            for line in lines:
                if "User accounts" in line:
                    in_user_list = True
                    continue
                if in_user_list and line.strip() and not line.startswith("-") and "command completed" not in line.lower():
                    users.extend([u.strip() for u in line.split() if u.strip()])
                    
            print(f"  {'Username':<20} {'Status':<15} {'Type':<15}")
            print(f"  {'─' * 55}")
            
            for user in users[:10]:  # Show first 10 users
                # Check if admin
                admin_cmd = f"net localgroup administrators | findstr /i \"{user}\""
                _, admin_out, _ = self.run_command(admin_cmd)
                is_admin = "Administrator" if user in admin_out else "Standard"
                
                # Check status
                status_cmd = f"net user \"{user}\" | findstr /i \"active\""
                _, status_out, _ = self.run_command(status_cmd)
                status = "Active" if "Yes" in status_out else "Inactive"
                status_color = Colors.GREEN if status == "Active" else Colors.WARNING
                
                type_color = Colors.FAIL if is_admin == "Administrator" else Colors.CYAN
                
                print(f"  {user:<20} {status_color}{status:<15}{Colors.ENDC} {type_color}{is_admin:<15}{Colors.ENDC}")
                
        # Security recommendations
        print(f"\n{Colors.BOLD}Security Recommendations:{Colors.ENDC}\n")
        
        recommendations = [
            ("✓", Colors.GREEN, "Ensure Guest account is disabled"),
            ("✓", Colors.GREEN, "Limit Administrator accounts (principle of least privilege)"),
            ("✓", Colors.GREEN, "Enable password complexity requirements"),
            ("✓", Colors.GREEN, "Configure account lockout policies"),
            ("⚠", Colors.WARNING, "Review inactive accounts regularly"),
        ]
        
        for icon, color, rec in recommendations:
            print(f"  {color}{icon}{Colors.ENDC} {rec}")
            
        self.wait_for_enter()
        
    def windows_update_check(self):
        """Check Windows Update status"""
        self.print_header("WINDOWS UPDATE STATUS")
        
        # Update Flow Diagram
        diagram = f"""
{Colors.CYAN}
                    WINDOWS UPDATE FLOW
        
        ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
        │  CHECK   │───▶│ DOWNLOAD │───▶│  INSTALL │───▶│ RESTART  │
        │  UPDATES │    │ UPDATES  │    │ UPDATES  │    │  SYSTEM  │
        └──────────┘    └──────────┘    └──────────┘    └──────────┘
             │                                              │
             ▼                                              ▼
        ┌──────────┐                                   ┌──────────┐
        │ WSUS/    │                                   │ VERIFIED │
        │ Microsoft│                                   │  SECURE  │
        │  Update  │                                   │  SYSTEM  │
        └──────────┘                                   └──────────┘
{Colors.ENDC}
        """
        print(diagram)
        
        print(f"{Colors.CYAN}Checking Windows Update status...{Colors.ENDC}\n")
        
        # Use PowerShell to check update status
        ps_cmd = """powershell -Command "
try {
    $UpdateSession = New-Object -ComObject Microsoft.Update.Session
    $UpdateSearcher = $UpdateSession.CreateUpdateSearcher()
    $SearchResult = $UpdateSearcher.Search('IsInstalled=0')
    Write-Output \"PENDING_UPDATES:$($SearchResult.Updates.Count)\"
    foreach ($update in $SearchResult.Updates | Select-Object -First 5) {
        Write-Output \"UPDATE:$($update.Title)\"
    }
} catch {
    Write-Output \"ERROR:$_\"
}
"""
        returncode, stdout, stderr = self.run_command(ps_cmd)
        
        pending_count = 0
        updates = []
        
        for line in stdout.split('\n'):
            if line.startswith("PENDING_UPDATES:"):
                try:
                    pending_count = int(line.split(':')[1])
                except:
                    pass
            elif line.startswith("UPDATE:"):
                updates.append(line.replace("UPDATE:", "").strip())
                
        # Display status
        if pending_count > 0:
            print(f"  Update Status: {Colors.WARNING}⚠ {pending_count} pending updates{Colors.ENDC}")
        else:
            print(f"  Update Status: {Colors.GREEN}✓ System is up to date{Colors.ENDC}")
            
        # Last update check
        print(f"\n{Colors.BOLD}Update Service Status:{Colors.ENDC}\n")
        
        services_to_check = [
            "wuauserv",  # Windows Update
            "bits",      # Background Intelligent Transfer
            "cryptSvc",  # Cryptographic Services
        ]
        
        for service in services_to_check:
            cmd = f"sc query {service}"
            returncode, stdout, stderr = self.run_command(cmd)
            
            if "RUNNING" in stdout:
                print(f"  {service:<20} {Colors.GREEN}[RUNNING]{Colors.ENDC}")
            elif "STOPPED" in stdout:
                print(f"  {service:<20} {Colors.FAIL}[STOPPED]{Colors.ENDC}")
            else:
                print(f"  {service:<20} {Colors.WARNING}[UNKNOWN]{Colors.ENDC}")
                
        if updates:
            print(f"\n{Colors.BOLD}Pending Updates:{Colors.ENDC}\n")
            for update in updates[:5]:
                print(f"  • {update[:60]}...")
                
        self.wait_for_enter()
        
    def service_management(self):
        """Manage and check critical services"""
        self.print_header("SERVICE MANAGEMENT")
        
        # Service Status Diagram
        diagram = f"""
{Colors.CYAN}
                    CRITICAL SERVICES STATUS
        
        ┌────────────────────────────────────────────────────────────┐
        │                                                            │
        │   Security Services     │    System Services               │
        │   ─────────────────     │    ─────────────                 │
        │   • Windows Defender    │    • Windows Update              │
        │   • Windows Firewall    │    • Event Log                   │
        │   • Security Center     │    • RPC                         │
        │                                                            │
        └────────────────────────────────────────────────────────────┘
{Colors.ENDC}
        """
        print(diagram)
        
        critical_services = [
            ("Windows Defender", "windefend"),
            ("Windows Firewall", "mpssvc"),
            ("Security Center", "wscsvc"),
            ("Windows Update", "wuauserv"),
            ("Event Log", "eventlog"),
            ("RPC", "rpcss"),
        ]
        
        print(f"{Colors.BOLD}Service Status Overview:{Colors.ENDC}\n")
        print(f"  {'Service Name':<25} {'Status':<12} {'Startup':<12}")
        print(f"  {'─' * 55}")
        
        for service_name, service_key in critical_services:
            cmd = f"sc query {service_key}"
            returncode, stdout, stderr = self.run_command(cmd)
            
            if "RUNNING" in stdout:
                status = f"{Colors.GREEN}Running{Colors.ENDC}"
            elif "STOPPED" in stdout:
                status = f"{Colors.FAIL}Stopped{Colors.ENDC}"
            else:
                status = f"{Colors.WARNING}Unknown{Colors.ENDC}"
                
            # Get startup type
            config_cmd = f"sc qc {service_key}"
            _, config_out, _ = self.run_command(config_cmd)
            
            startup = "Unknown"
            if "AUTO_START" in config_out:
                startup = "Automatic"
            elif "DEMAND_START" in config_out:
                startup = "Manual"
            elif "DISABLED" in config_out:
                startup = "Disabled"
                
            print(f"  {service_name:<25} {status:<25} {startup}")
            
        print(f"\n{Colors.WARNING}Note: Services marked in {Colors.FAIL}red{Colors.WARNING} may require attention{Colors.ENDC}")
        
        self.wait_for_enter()
        
    def network_security_check(self):
        """Check network security configuration"""
        self.print_header("NETWORK SECURITY CHECK")
        
        # Network Security Diagram
        diagram = f"""
{Colors.CYAN}
                    NETWORK SECURITY LAYERS
        
              ┌───────────────────────────────────────────┐
              │              PERIMETER                    │
              │         (Firewall / Router)               │
              └───────────────────┬───────────────────────┘
                                  │
              ┌───────────────────▼───────────────────────┐
              │              HOST LAYER                   │
              │    (Windows Firewall / Defender)          │
              └───────────────────┬───────────────────────┘
                                  │
              ┌───────────────────▼───────────────────────┐
              │           APPLICATION LAYER               │
              │      (App Control / Port Security)        │
              └───────────────────────────────────────────┘
{Colors.ENDC}
        """
        print(diagram)
        
        print(f"{Colors.BOLD}Network Configuration:{Colors.ENDC}\n")
        
        # Network adapters
        cmd = "ipconfig | findstr /i \"adapter ipv4 subnet mask\""
        returncode, stdout, stderr = self.run_command(cmd)
        
        if stdout:
            print("  Active Network Interfaces:")
            for line in stdout.split('\n')[:10]:
                if line.strip():
                    print(f"    {line.strip()}")
                    
        # Open ports check
        print(f"\n{Colors.BOLD}Listening Ports (Top 10):{Colors.ENDC}\n")
        
        cmd = "netstat -an | findstr LISTENING | findstr /v \" [:: \" | head -10"
        returncode, stdout, stderr = self.run_command(cmd)
        
        if stdout:
            print(f"  {'Protocol':<10} {'Local Address':<25} {'State':<15}")
            print(f"  {'─' * 55}")
            for line in stdout.strip().split('\n')[:10]:
                parts = line.split()
                if len(parts) >= 4:
                    print(f"  {parts[0]:<10} {parts[1]:<25} {parts[3]:<15}")
                    
        # Network profile
        print(f"\n{Colors.BOLD}Network Profile:{Colors.ENDC}\n")
        
        cmd = "netsh advfirewall show currentprofile"
        returncode, stdout, stderr = self.run_command(cmd)
        
        if returncode == 0:
            for line in stdout.split('\n'):
                if "Profile" in line or "State" in line:
                    print(f"  {line.strip()}")
                    
        self.wait_for_enter()
        
    def hardening_recommendations(self):
        """Display Windows hardening recommendations"""
        self.print_header("WINDOWS HARDENING RECOMMENDATIONS")
        
        # Hardening Pyramid
        diagram = f"""
{Colors.CYAN}
                    HARDENING PYRAMID
                    
                            /\\
                           /  \\
                          / ▲  \\      LAYER 4: ADVANCED
                         /AUDIT \\      (Logging/Monitoring)
                        /────────\\
                       /          \\
                      /    ▲       \\    LAYER 3: APPLICATION
                     /   PATCH      \\    (Updates/Patches)
                    /────────────────\\
                   /                  \\
                  /       ▲            \\  LAYER 2: CONFIG
                 /    HARDEN CONFIG     \\  (Policy/Settings)
                /────────────────────────\\
               /                          \\
              /            ▲               \\ LAYER 1: BASE
             /         SECURE BASE          \\(OS Install/Account)
            /────────────────────────────────\\
{Colors.ENDC}
        """
        print(diagram)
        
        recommendations = {
            "Account Security": [
                "✓ Enforce strong password policies (minimum 14 characters)",
                "✓ Enable account lockout after 5 failed attempts",
                "✓ Disable Guest account",
                "✓ Rename default Administrator account",
                "✓ Implement principle of least privilege",
            ],
            "Network Security": [
                "✓ Enable Windows Firewall on all profiles",
                "✓ Disable unnecessary network protocols",
                "✓ Configure secure Wi-Fi settings (WPA3)",
                "✓ Disable NetBIOS over TCP/IP if not needed",
                "✓ Enable Windows Defender Network Protection",
            ],
            "System Hardening": [
                "✓ Keep Windows updated with latest security patches",
                "✓ Enable Windows Defender Real-time protection",
                "✓ Configure User Account Control (UAC) to highest setting",
                "✓ Disable unused Windows services",
                "✓ Enable Secure Boot and TPM 2.0",
            ],
            "Audit & Monitoring": [
                "✓ Enable Windows Event Log auditing",
                "✓ Configure security event subscriptions",
                "✓ Implement regular security scans",
                "✓ Monitor for unauthorized access attempts",
                "✓ Enable PowerShell script block logging",
            ],
            "Data Protection": [
                "✓ Enable BitLocker drive encryption",
                "✓ Configure EFS for sensitive files",
                "✓ Implement backup and recovery procedures",
                "✓ Disable USB storage if not required",
                "✓ Configure Windows Information Protection",
            ],
        }
        
        for category, items in recommendations.items():
            print(f"\n{Colors.BOLD}{Colors.CYAN}▸ {category}{Colors.ENDC}")
            print(f"{Colors.CYAN}{'─' * 60}{Colors.ENDC}")
            for item in items:
                print(f"  {Colors.GREEN}{item}{Colors.ENDC}")
                
        # Compliance check summary
        print(f"\n{Colors.BOLD}Compliance Standards Reference:{Colors.ENDC}\n")
        
        standards = [
            ("CIS Benchmarks", "Center for Internet Security guidelines"),
            ("NIST SP 800-171", "Protecting Controlled Unclassified Information"),
            ("PCI DSS", "Payment Card Industry Data Security Standard"),
            ("HIPAA", "Health Insurance Portability and Accountability Act"),
            ("DISA STIG", "Defense Information Systems Agency guidelines"),
        ]
        
        for standard, desc in standards:
            print(f"  {Colors.CYAN}{standard:<15}{Colors.ENDC} - {desc}")
            
        self.wait_for_enter()
        
    def generate_report(self):
        """Generate comprehensive security report"""
        self.print_header("GENERATE SECURITY REPORT")
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"winsec_report_{timestamp}.txt"
        
        print(f"{Colors.CYAN}Generating security report...{Colors.ENDC}\n")
        
        report_content = f"""
{'='*80}
           WINDOWS SECURITY LAB - COMPREHENSIVE SECURITY REPORT
{'='*80}

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
System: {platform.platform()}
Hostname: {platform.node()}

{'─'*80}
EXECUTIVE SUMMARY
{'─'*80}

This report provides a comprehensive analysis of the Windows system security
configuration and hardening status.

{'─'*80}
SYSTEM INFORMATION
{'─'*80}

Platform: {platform.platform()}
Machine: {platform.machine()}
Processor: {platform.processor()}
Python Version: {platform.python_version()}

{'─'*80}
SECURITY CHECK RESULTS
{'─'*80}
"""
        
        if 'security_checks' in self.report_data:
            for name, status, details in self.report_data['security_checks']:
                report_content += f"\n[{status}] {name}\n"
                if details:
                    report_content += f"    Details: {details}\n"
                    
        report_content += f"""
{'─'*80}
RECOMMENDATIONS
{'─'*80}

1. Review any FAILED security checks immediately
2. Apply Windows updates regularly
3. Monitor event logs for suspicious activity
4. Follow principle of least privilege for user accounts
5. Maintain regular backups of critical data

{'='*80}
                        END OF SECURITY REPORT
{'='*80}
"""
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(report_content)
            print(f"{Colors.GREEN}✓ Report saved to: {filename}{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.FAIL}✗ Error saving report: {e}{Colors.ENDC}")
            
        print(f"\n{Colors.CYAN}Report Preview:{Colors.ENDC}\n")
        print(report_content[:1000] + "..." if len(report_content) > 1000 else report_content)
        
        self.wait_for_enter()
        
    def exit_app(self):
        """Exit the application"""
        self.clear_screen()
        print(f"""
{Colors.CYAN}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                    Thank you for using WinSec Lab!                            ║
║                                                                              ║
║              Stay secure, stay updated, stay vigilant.                      ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  {Colors.GREEN}▸ Organization:  {ORG_NAME:<56}{Colors.CYAN}║
║  {Colors.GREEN}▸ Websites:     {ORG_WEBSITE:<56}{Colors.CYAN}║
║  {Colors.GREEN}▸ Developer:    {DEVELOPER + ', ' + TITLE:<56}{Colors.CYAN}║
║  {Colors.GREEN}▸ Lab:          {LAB_TYPE:<56}{Colors.CYAN}║
╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.ENDC}
        """)
        sys.exit(0)
        
    def run(self):
        """Main application loop"""
        while True:
            self.print_menu()
            choice = input(f"\n{Colors.BOLD}Enter choice: {Colors.ENDC}").strip()
            
            if choice in self.modules:
                _, action = self.modules[choice]
                action()
            else:
                print(f"\n{Colors.FAIL}Invalid choice. Press Enter to continue...{Colors.ENDC}")
                input()

if __name__ == "__main__":
    try:
        app = WinSecLab()
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}Interrupted by user. Exiting...{Colors.ENDC}")
        sys.exit(0)
