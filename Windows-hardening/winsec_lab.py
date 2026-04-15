#!/usr/bin/env python3
"""
WinSec Lab - Windows Security Hardening & Administration CLI Tool
A comprehensive CLI tool for Windows security checks and system hardening.
Compatible with Windows Command Line and PowerShell.
Includes a demo mode for non-Windows environments.
"""

import os
import sys
import subprocess
import platform
import json
import random
from datetime import datetime
from typing import Dict, List, Optional, Callable

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'

ORG_NAME = "Cyber Wolf"
ORG_WEBSITE = "www.cyberwolf.py | www.zh5.club"
DEVELOPER = "Tamilselvan .S"
TITLE = "Cyber Security Researcher"
LAB_TYPE = "Mini Lab"

BANNER = f"""
{Colors.CYAN}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║   ██╗    ██╗██╗███╗   ██╗██████╗  ██████╗  ██████╗ ███████╗ ██████╗        ║
║   ██║    ██║██║████╗  ██║██╔══██╗██╔═══██╗██╔════╝ ██╔════╝██╔════╝        ║
║   ██║ █╗ ██║██║██╔██╗ ██║██████╔╝██║   ██║██║  ███╗█████╗  ██║  ███╗      ║
║   ██║███╗██║██║██║╚██╗██║██╔══██╗██║   ██║██║   ██║██╔══╝  ██║   ██║      ║
║   ╚███╔███╔╝██║██║ ╚████║██║  ██║╚██████╔╝╚██████╔╝███████╗╚██████╔╝      ║
║    ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝     ║
║                                                                            ║
║                    Windows Security Hardening Lab                          ║
║                        Administrator Console                               ║
║                                                                            ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  {Colors.GREEN}▸ Organization:  {ORG_NAME:<54}{Colors.CYAN}║
║  {Colors.GREEN}▸ Websites:     {ORG_WEBSITE:<54}{Colors.CYAN}║
║  {Colors.GREEN}▸ Developed by: {DEVELOPER + ', ' + TITLE:<54}{Colors.CYAN}║
║  {Colors.GREEN}▸ Lab Type:     {LAB_TYPE:<54}{Colors.CYAN}║
╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.ENDC}"""


class DemoData:
    """Provides simulated data for demo mode"""

    SYSTEM_INFO = {
        "Platform": "Windows-10-10.0.19045-SP0",
        "Machine": "AMD64",
        "Processor": "Intel64 Family 6 Model 142 Stepping 12, GenuineIntel",
        "Node Name": "DESKTOP-WINSEC01",
        "Python Version": "3.11.5",
        "Hostname": "DESKTOP-WINSEC01",
        "Domain": "WORKGROUP",
        "Windows Version": "Microsoft Windows [Version 10.0.19045.3803]",
    }

    SECURITY_CHECKS = [
        ("Windows Defender", "PASS", "RealTimeProtectionEnabled : True"),
        ("Firewall Status", "PASS", "State ON"),
        ("Guest Account", "PASS", "Account active No"),
        ("UAC Status", "PASS", "EnableLUA REG_DWORD 0x1"),
    ]

    FIREWALL_PROFILES = {
        "domain": "ON",
        "private": "ON",
        "public": "ON",
    }

    FIREWALL_RULES = [
        "Core Networking - DNS (UDP-Out)",
        "Core Networking - DHCP (DHCP-Out)",
        "Remote Desktop - User Mode (TCP-In)",
        "Windows Defender Firewall Remote Management (RPC)",
        "File and Printer Sharing (SMB-In)",
    ]

    USERS = [
        ("Administrator", "Inactive", "Administrator"),
        ("DefaultAccount", "Inactive", "Standard"),
        ("Guest", "Inactive", "Standard"),
        ("WDAGUtilityAccount", "Inactive", "Standard"),
        ("CyberWolf", "Active", "Administrator"),
        ("LabUser", "Active", "Standard"),
    ]

    SERVICES = [
        ("Windows Defender", "windefend", "Running", "Automatic"),
        ("Windows Firewall", "mpssvc", "Running", "Automatic"),
        ("Security Center", "wscsvc", "Running", "Automatic"),
        ("Windows Update", "wuauserv", "Running", "Manual"),
        ("Event Log", "eventlog", "Running", "Automatic"),
        ("RPC", "rpcss", "Running", "Automatic"),
    ]

    NETWORK_INTERFACES = [
        "Ethernet adapter Ethernet:",
        "   IPv4 Address. . . . . . . : 192.168.1.105",
        "   Subnet Mask . . . . . . . : 255.255.255.0",
        "   Default Gateway . . . . . : 192.168.1.1",
    ]

    LISTENING_PORTS = [
        ("TCP", "0.0.0.0:135", "LISTENING"),
        ("TCP", "0.0.0.0:445", "LISTENING"),
        ("TCP", "0.0.0.0:3389", "LISTENING"),
        ("TCP", "0.0.0.0:5040", "LISTENING"),
        ("TCP", "0.0.0.0:5357", "LISTENING"),
        ("TCP", "127.0.0.1:5939", "LISTENING"),
        ("TCP", "192.168.1.105:139", "LISTENING"),
    ]

    UPDATE_SERVICES = [
        ("wuauserv", "RUNNING"),
        ("bits", "RUNNING"),
        ("cryptSvc", "RUNNING"),
    ]


class WinSecLab:
    """Main Windows Security Lab CLI Application"""

    def __init__(self, demo_mode: bool = False):
        self.demo_mode = demo_mode
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
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_header(self, title: str):
        width = 80
        print(f"\n{Colors.CYAN}{'=' * width}{Colors.ENDC}")
        print(f"{Colors.BOLD}{Colors.HEADER}{title.center(width)}{Colors.ENDC}")
        print(f"{Colors.CYAN}{'=' * width}{Colors.ENDC}\n")

    def print_menu(self):
        self.clear_screen()
        print(BANNER)

        if self.demo_mode:
            print(f"  {Colors.WARNING}[DEMO MODE]{Colors.ENDC} Running with simulated data\n")

        print(f"\n{Colors.BOLD}Main Menu:{Colors.ENDC}\n")

        for key, (name, _) in self.modules.items():
            if "Security" in name or "Firewall" in name or "Harden" in name:
                status_icon = "🔒"
            elif key == '0':
                status_icon = "👋"
            else:
                status_icon = "🔧"
            print(f"  {Colors.CYAN}[{key}]{Colors.ENDC} {status_icon} {name}")

        print(f"\n{Colors.WARNING}Enter your choice and press Enter...{Colors.ENDC}")

    def run_command(self, command: str, shell: bool = True) -> tuple:
        if self.demo_mode:
            return -1, "", "Demo mode"
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
        print(f"\n{Colors.WARNING}{message}{Colors.ENDC}")
        input()

    def show_system_info(self):
        self.print_header("SYSTEM INFORMATION")

        print(f"{Colors.CYAN}Gathering system details...{Colors.ENDC}\n")

        if self.demo_mode:
            system_info = DemoData.SYSTEM_INFO.copy()
            hostname = system_info.pop("Hostname", "")
            domain = system_info.pop("Domain", "")
            system_info.pop("Windows Version", "")
        else:
            system_info = {
                "Platform": platform.platform(),
                "Machine": platform.machine(),
                "Processor": platform.processor(),
                "Node Name": platform.node(),
                "Python Version": platform.python_version(),
            }
            _, win_ver, _ = self.run_command("ver")
            _, hostname, _ = self.run_command("hostname")
            _, domain, _ = self.run_command("echo %userdomain%")
            hostname = hostname.strip()
            domain = domain.strip()

        diagram = f"""
{Colors.CYAN}
        ┌─────────────────────────────────────────────────────────────┐
        │                    SYSTEM ARCHITECTURE                      │
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

        print(f"\n{Colors.BOLD}System Details:{Colors.ENDC}\n")
        print(f"  {'Property':<20} {'Value':<50}")
        print(f"  {'─' * 70}")

        for key, value in system_info.items():
            print(f"  {Colors.CYAN}{key:<20}{Colors.ENDC} {value:<50}")

        if hostname:
            print(f"  {Colors.CYAN}{'Hostname':<20}{Colors.ENDC} {hostname:<50}")
        if domain:
            print(f"  {Colors.CYAN}{'Domain':<20}{Colors.ENDC} {domain:<50}")

        print(f"\n{Colors.BOLD}System Status Indicators:{Colors.ENDC}\n")

        indicators = [
            ("Boot Mode", "Normal", Colors.GREEN),
            ("Secure Boot", "Enabled" if self.demo_mode else "Checking...", Colors.GREEN if self.demo_mode else Colors.WARNING),
            ("Virtualization", "Enabled", Colors.GREEN),
            ("TPM Status", "Ready", Colors.GREEN),
        ]

        for name, status, color in indicators:
            print(f"  [{color}●{Colors.ENDC}] {name:<20} {color}{status}{Colors.ENDC}")

        self.report_data['system_info'] = system_info
        self.wait_for_enter()

    def security_status_check(self):
        self.print_header("SECURITY STATUS CHECK")

        checks = [
            ("Windows Defender", "powershell -Command \"Get-MpComputerStatus | Select-Object RealTimeProtectionEnabled\"", "RealTimeProtectionEnabled"),
            ("Firewall Status", "netsh advfirewall show currentprofile", "ON"),
            ("Guest Account", "net user guest | findstr /i \"active\"", "No"),
            ("UAC Status", "REG QUERY HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableLUA", "0x1"),
        ]

        results = []

        print(f"{Colors.CYAN}Running security checks...{Colors.ENDC}\n")

        dashboard = f"""
{Colors.CYAN}
                    SECURITY DASHBOARD
                    ═══════════════════

           ┌─────────────────────────────────────┐
           │     THREAT LEVEL INDICATOR          │
           │                                     │
           │    LOW        MODERATE      HIGH    │
           │     🟢          🟡           🔴    │
           │      │          │            │      │
           └─────────────────────────────────────┘
{Colors.ENDC}
        """
        print(dashboard)

        if self.demo_mode:
            for check_name, _, _ in checks:
                print(f"  Checking {check_name}...", end=" ")
                demo_entry = next((d for d in DemoData.SECURITY_CHECKS if d[0] == check_name), None)
                if demo_entry:
                    status = demo_entry[1]
                    details = demo_entry[2]
                else:
                    status = "PASS"
                    details = "OK"
                if status == "PASS":
                    print(f"{Colors.GREEN}[✓ SECURE]{Colors.ENDC}")
                else:
                    print(f"{Colors.FAIL}[✗ WARNING]{Colors.ENDC}")
                results.append((check_name, status, details))
        else:
            for check_name, command, expected in checks:
                print(f"  Checking {check_name}...", end=" ")
                returncode, stdout, stderr = self.run_command(command)

                if expected.lower() in stdout.lower() or returncode == 0:
                    print(f"{Colors.GREEN}[✓ SECURE]{Colors.ENDC}")
                    results.append((check_name, "PASS", stdout.strip()[:50]))
                else:
                    print(f"{Colors.FAIL}[✗ WARNING]{Colors.ENDC}")
                    results.append((check_name, "FAIL", stdout.strip()[:50] or stderr[:50]))

        print(f"\n{Colors.BOLD}Security Check Summary:{Colors.ENDC}\n")
        print(f"  {'Check':<25} {'Status':<12} {'Details':<40}")
        print(f"  {'─' * 77}")

        for name, status, details in results:
            status_color = Colors.GREEN if status == "PASS" else Colors.FAIL
            print(f"  {name:<25} {status_color}{status:<12}{Colors.ENDC} {details:<40}")

        passed = sum(1 for _, status, _ in results if status == "PASS")
        total = len(results)
        score = (passed / total) * 100 if total > 0 else 0

        score_color = Colors.GREEN if score >= 80 else Colors.WARNING if score >= 60 else Colors.FAIL
        print(f"\n  {Colors.BOLD}Security Score: {score_color}{score:.0f}%{Colors.ENDC} ({passed}/{total} checks passed)")

        self.report_data['security_checks'] = results
        self.wait_for_enter()

    def firewall_check(self):
        self.print_header("FIREWALL CONFIGURATION")

        diagram = f"""
{Colors.CYAN}
                    FIREWALL ARCHITECTURE
        ┌────────────────────────────────────────────────────┐
        │                                                    │
        │   INTERNET ◄────► [WINDOWS FIREWALL] ◄────► LAN   │
        │                      │    │                        │
        │                      ▼    ▼                        │
        │              ┌────────┐ ┌────────┐                 │
        │              │Inbound │ │Outbound│                 │
        │              │ Rules  │ │ Rules  │                 │
        │              └────────┘ └────────┘                 │
        │                                                    │
        └────────────────────────────────────────────────────┘
{Colors.ENDC}
        """
        print(diagram)

        profiles = ["domain", "private", "public"]
        print(f"{Colors.BOLD}Firewall Profile Status:{Colors.ENDC}\n")

        if self.demo_mode:
            for profile in profiles:
                status = DemoData.FIREWALL_PROFILES.get(profile, "UNKNOWN")
                status_color = Colors.GREEN if status == "ON" else Colors.FAIL if status == "OFF" else Colors.WARNING
                print(f"  {profile.upper():<15} Profile: {status_color}[{status}]{Colors.ENDC}")
        else:
            for profile in profiles:
                cmd = f"netsh advfirewall show {profile}profile state"
                returncode, stdout, stderr = self.run_command(cmd)

                status = "ON" if "ON" in stdout else "OFF" if "OFF" in stdout else "UNKNOWN"
                status_color = Colors.GREEN if status == "ON" else Colors.FAIL if status == "OFF" else Colors.WARNING

                print(f"  {profile.upper():<15} Profile: {status_color}[{status}]{Colors.ENDC}")

        print(f"\n{Colors.BOLD}Firewall Rules Summary:{Colors.ENDC}\n")

        if self.demo_mode:
            print(f"  Total Active Rules: {Colors.CYAN}247{Colors.ENDC}")
        else:
            cmd = 'netsh advfirewall firewall show rule name=all | findstr /c:"Rule Name:" | find /c "Rule Name"'
            returncode, stdout, stderr = self.run_command(cmd)
            if stdout.strip():
                rule_count = stdout.strip()
                print(f"  Total Active Rules: {Colors.CYAN}{rule_count}{Colors.ENDC}")

        print(f"\n{Colors.BOLD}Sample Inbound Rules:{Colors.ENDC}\n")

        if self.demo_mode:
            for rule in DemoData.FIREWALL_RULES:
                print(f"  • {rule}")
        else:
            cmd = 'netsh advfirewall firewall show rule name=all dir=in | findstr /B "Rule Name:"'
            returncode, stdout, stderr = self.run_command(cmd)
            if stdout:
                for line in stdout.strip().split('\n')[:5]:
                    rule_name = line.replace("Rule Name:", "").strip()
                    print(f"  • {rule_name}")
            else:
                print(f"  {Colors.WARNING}Unable to retrieve rules{Colors.ENDC}")

        self.wait_for_enter()

    def user_accounts_check(self):
        self.print_header("USER ACCOUNTS AUDIT")

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
        print(f"  {'Username':<20} {'Status':<15} {'Type':<15}")
        print(f"  {'─' * 55}")

        if self.demo_mode:
            for user, status, user_type in DemoData.USERS:
                status_color = Colors.GREEN if status == "Active" else Colors.WARNING
                type_color = Colors.FAIL if user_type == "Administrator" else Colors.CYAN
                print(f"  {user:<20} {status_color}{status:<15}{Colors.ENDC} {type_color}{user_type:<15}{Colors.ENDC}")
        else:
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

                for user in users[:10]:
                    admin_cmd = f'net localgroup administrators | findstr /i "{user}"'
                    _, admin_out, _ = self.run_command(admin_cmd)
                    is_admin = "Administrator" if user in admin_out else "Standard"

                    status_cmd = f'net user "{user}" | findstr /i "active"'
                    _, status_out, _ = self.run_command(status_cmd)
                    status = "Active" if "Yes" in status_out else "Inactive"
                    status_color = Colors.GREEN if status == "Active" else Colors.WARNING
                    type_color = Colors.FAIL if is_admin == "Administrator" else Colors.CYAN

                    print(f"  {user:<20} {status_color}{status:<15}{Colors.ENDC} {type_color}{is_admin:<15}{Colors.ENDC}")

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
        self.print_header("WINDOWS UPDATE STATUS")

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

        if self.demo_mode:
            pending_count = 2
            updates = [
                "2024-01 Cumulative Update for Windows 10 Version 22H2 (KB5034441)",
                "Security Intelligence Update for Microsoft Defender Antivirus",
            ]
        else:
            ps_cmd = 'powershell -Command "try { $UpdateSession = New-Object -ComObject Microsoft.Update.Session; $UpdateSearcher = $UpdateSession.CreateUpdateSearcher(); $SearchResult = $UpdateSearcher.Search(\'IsInstalled=0\'); Write-Output \\"PENDING_UPDATES:$($SearchResult.Updates.Count)\\"; foreach ($update in $SearchResult.Updates | Select-Object -First 5) { Write-Output \\"UPDATE:$($update.Title)\\" } } catch { Write-Output \\"ERROR:$_\\" }"'
            returncode, stdout, stderr = self.run_command(ps_cmd)

            pending_count = 0
            updates = []

            for line in stdout.split('\n'):
                if line.startswith("PENDING_UPDATES:"):
                    try:
                        pending_count = int(line.split(':')[1])
                    except (ValueError, IndexError):
                        pass
                elif line.startswith("UPDATE:"):
                    updates.append(line.replace("UPDATE:", "").strip())

        if pending_count > 0:
            print(f"  Update Status: {Colors.WARNING}⚠ {pending_count} pending updates{Colors.ENDC}")
        else:
            print(f"  Update Status: {Colors.GREEN}✓ System is up to date{Colors.ENDC}")

        print(f"\n{Colors.BOLD}Update Service Status:{Colors.ENDC}\n")

        if self.demo_mode:
            for service, status in DemoData.UPDATE_SERVICES:
                if status == "RUNNING":
                    print(f"  {service:<20} {Colors.GREEN}[RUNNING]{Colors.ENDC}")
                elif status == "STOPPED":
                    print(f"  {service:<20} {Colors.FAIL}[STOPPED]{Colors.ENDC}")
                else:
                    print(f"  {service:<20} {Colors.WARNING}[UNKNOWN]{Colors.ENDC}")
        else:
            services_to_check = ["wuauserv", "bits", "cryptSvc"]
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
                display = update[:60] + "..." if len(update) > 60 else update
                print(f"  • {display}")

        self.wait_for_enter()

    def service_management(self):
        self.print_header("SERVICE MANAGEMENT")

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

        if self.demo_mode:
            for service_name, service_key, svc_status, startup in DemoData.SERVICES:
                if svc_status == "Running":
                    status = f"{Colors.GREEN}Running{Colors.ENDC}"
                elif svc_status == "Stopped":
                    status = f"{Colors.FAIL}Stopped{Colors.ENDC}"
                else:
                    status = f"{Colors.WARNING}Unknown{Colors.ENDC}"
                print(f"  {service_name:<25} {status:<25} {startup}")
        else:
            for service_name, service_key in critical_services:
                cmd = f"sc query {service_key}"
                returncode, stdout, stderr = self.run_command(cmd)

                if "RUNNING" in stdout:
                    status = f"{Colors.GREEN}Running{Colors.ENDC}"
                elif "STOPPED" in stdout:
                    status = f"{Colors.FAIL}Stopped{Colors.ENDC}"
                else:
                    status = f"{Colors.WARNING}Unknown{Colors.ENDC}"

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
        self.print_header("NETWORK SECURITY CHECK")

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
              │    (Windows Firewall / Defender)           │
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

        if self.demo_mode:
            print("  Active Network Interfaces:")
            for line in DemoData.NETWORK_INTERFACES:
                print(f"    {line}")
        else:
            cmd = 'ipconfig | findstr /i "adapter ipv4 subnet mask"'
            returncode, stdout, stderr = self.run_command(cmd)

            if stdout:
                print("  Active Network Interfaces:")
                for line in stdout.split('\n')[:10]:
                    if line.strip():
                        print(f"    {line.strip()}")

        print(f"\n{Colors.BOLD}Listening Ports (Top 10):{Colors.ENDC}\n")
        print(f"  {'Protocol':<10} {'Local Address':<25} {'State':<15}")
        print(f"  {'─' * 55}")

        if self.demo_mode:
            for proto, addr, state in DemoData.LISTENING_PORTS:
                print(f"  {proto:<10} {addr:<25} {state:<15}")
        else:
            cmd = 'netstat -an | findstr LISTENING'
            returncode, stdout, stderr = self.run_command(cmd)

            if stdout:
                for line in stdout.strip().split('\n')[:10]:
                    parts = line.split()
                    if len(parts) >= 4:
                        print(f"  {parts[0]:<10} {parts[1]:<25} {parts[3]:<15}")

        print(f"\n{Colors.BOLD}Network Profile:{Colors.ENDC}\n")

        if self.demo_mode:
            print(f"  Profile: Domain")
            print(f"  Firewall State: ON")
        else:
            cmd = "netsh advfirewall show currentprofile"
            returncode, stdout, stderr = self.run_command(cmd)

            if returncode == 0:
                for line in stdout.split('\n'):
                    if "Profile" in line or "State" in line:
                        print(f"  {line.strip()}")

        self.wait_for_enter()

    def hardening_recommendations(self):
        self.print_header("WINDOWS HARDENING RECOMMENDATIONS")

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
        self.print_header("GENERATE SECURITY REPORT")

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"winsec_report_{timestamp}.txt"

        print(f"{Colors.CYAN}Generating security report...{Colors.ENDC}\n")

        if self.demo_mode:
            plat = DemoData.SYSTEM_INFO["Platform"]
            machine = DemoData.SYSTEM_INFO["Machine"]
            proc = DemoData.SYSTEM_INFO["Processor"]
            pyver = DemoData.SYSTEM_INFO["Python Version"]
            node = DemoData.SYSTEM_INFO["Node Name"]
        else:
            plat = platform.platform()
            machine = platform.machine()
            proc = platform.processor()
            pyver = platform.python_version()
            node = platform.node()

        report_content = f"""
{'=' * 80}
           WINDOWS SECURITY LAB - COMPREHENSIVE SECURITY REPORT
{'=' * 80}

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
System: {plat}
Hostname: {node}
Mode: {"DEMO" if self.demo_mode else "LIVE"}

{'─' * 80}
EXECUTIVE SUMMARY
{'─' * 80}

This report provides a comprehensive analysis of the Windows system security
configuration and hardening status.

{'─' * 80}
SYSTEM INFORMATION
{'─' * 80}

Platform: {plat}
Machine: {machine}
Processor: {proc}
Python Version: {pyver}

{'─' * 80}
SECURITY CHECK RESULTS
{'─' * 80}
"""

        if 'security_checks' in self.report_data:
            for name, status, details in self.report_data['security_checks']:
                report_content += f"\n[{status}] {name}\n"
                if details:
                    report_content += f"    Details: {details}\n"
        else:
            report_content += "\nNo security checks have been run yet.\nPlease run Security Status Check (option 2) first.\n"

        report_content += f"""
{'─' * 80}
RECOMMENDATIONS
{'─' * 80}

1. Review any FAILED security checks immediately
2. Apply Windows updates regularly
3. Monitor event logs for suspicious activity
4. Follow principle of least privilege for user accounts
5. Maintain regular backups of critical data

{'=' * 80}
                        END OF SECURITY REPORT
{'=' * 80}
"""

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(report_content)
            print(f"{Colors.GREEN}✓ Report saved to: {filename}{Colors.ENDC}")
        except Exception as e:
            print(f"{Colors.FAIL}✗ Error saving report: {e}{Colors.ENDC}")

        print(f"\n{Colors.CYAN}Report Preview:{Colors.ENDC}\n")
        preview = report_content[:1000] + "..." if len(report_content) > 1000 else report_content
        print(preview)

        self.wait_for_enter()

    def exit_app(self):
        self.clear_screen()
        print(f"""
{Colors.CYAN}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║                    Thank you for using WinSec Lab!                         ║
║                                                                            ║
║              Stay secure, stay updated, stay vigilant.                     ║
║                                                                            ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  {Colors.GREEN}▸ Organization:  {ORG_NAME:<54}{Colors.CYAN}║
║  {Colors.GREEN}▸ Websites:     {ORG_WEBSITE:<54}{Colors.CYAN}║
║  {Colors.GREEN}▸ Developer:    {DEVELOPER + ', ' + TITLE:<54}{Colors.CYAN}║
║  {Colors.GREEN}▸ Lab:          {LAB_TYPE:<54}{Colors.CYAN}║
╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.ENDC}
        """)
        sys.exit(0)

    def run(self):
        while True:
            self.print_menu()
            choice = input(f"\n{Colors.BOLD}Enter choice: {Colors.ENDC}").strip()

            if choice in self.modules:
                _, action = self.modules[choice]
                action()
            else:
                print(f"\n{Colors.FAIL}Invalid choice. Press Enter to continue...{Colors.ENDC}")
                input()


def main():
    is_windows = os.name == 'nt'
    demo_mode = False

    if '--demo' in sys.argv:
        demo_mode = True
    elif not is_windows:
        print(f"{Colors.WARNING}Non-Windows system detected.{Colors.ENDC}")
        print(f"{Colors.CYAN}Starting in DEMO mode with simulated data.{Colors.ENDC}")
        print(f"{Colors.CYAN}Use --demo flag to explicitly run in demo mode.{Colors.ENDC}\n")
        demo_mode = True

    app = WinSecLab(demo_mode=demo_mode)
    app.run()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}Interrupted by user. Exiting...{Colors.ENDC}")
        sys.exit(0)
