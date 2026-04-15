#!/usr/bin/env python3
"""
Kali Linux Basics Lab - Core Linux Commands & System Administration
A comprehensive CLI tool for learning Linux fundamentals on Kali Linux.
Covers commands, files, permissions, and process handling.

Organization: Cyber Wolf
Websites: www.cyberwolf.py | www.zh5.club
Developer: Tamilselvan .S, Cyber Security Researcher
Lab Type: Mini Lab
"""

import os
import sys
import subprocess
import platform
import pwd
import grp
from datetime import datetime
from typing import Dict, List, Optional, Tuple

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
    UNDERLINE = '\033[4m'

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
║   ██╗  ██╗ █████╗ ██╗     ██╗    ██╗   ██╗███╗   ██╗██╗  ██╗               ║
║   ██║ ██╔╝██╔══██╗██║     ██║    ██║   ██║████╗  ██║██║ ██╔╝               ║
║   █████╔╝ ███████║██║     ██║    ██║   ██║██╔██╗ ██║█████╔╝                ║
║   ██╔═██╗ ██╔══██║██║     ██║    ██║   ██║██║╚██╗██║██╔═██╗                ║
║   ██║  ██╗██║  ██║███████╗██║    ╚██████╔╝██║ ╚████║██║  ██╗               ║
║   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝               ║
║                                                                              ║
║                    Linux Basics Command Laboratory                            ║
║                         Kali Linux Edition                                    ║
║                                                                              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  {Colors.GREEN}▸ Organization:  {ORG_NAME:<56}{Colors.CYAN}║
║  {Colors.GREEN}▸ Websites:     {ORG_WEBSITE:<56}{Colors.CYAN}║
║  {Colors.GREEN}▸ Developed by: {DEVELOPER + ', ' + TITLE:<56}{Colors.CYAN}║
║  {Colors.GREEN}▸ Lab Type:     {LAB_TYPE:<56}{Colors.CYAN}║
╚══════════════════════════════════════════════════════════════════════════════╝
{Colors.ENDC}"""

class KaliLab:
    """Main Kali Linux Basics Lab CLI Application"""
    
    def __init__(self):
        self.modules = {
            '1': ('Linux Core Commands', self.core_commands),
            '2': ('File System Navigation', self.filesystem_navigation),
            '3': ('File Permissions & Ownership', self.file_permissions),
            '4': ('Process Management', self.process_management),
            '5': ('User & Group Management', self.user_management),
            '6': ('Package Management (APT)', self.package_management),
            '7': ('Network Commands', self.network_commands),
            '8': ('Text Processing Tools', self.text_processing),
            '9': ('System Information', self.system_info),
            '0': ('Exit', self.exit_app),
        }
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('clear' if os.name != 'nt' else 'cls')
        
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
            icon = "📁" if "File" in name else "⚡" if "Process" in name else "👤" if "User" in name else "🔧"
            if key == '0':
                icon = "👋"
            print(f"  {Colors.CYAN}[{key}]{Colors.ENDC} {icon} {name}")
            
        print(f"\n{Colors.WARNING}Enter your choice and press Enter...{Colors.ENDC}")
        
    def run_command(self, command: str, shell: bool = True) -> tuple:
        """Execute shell command and return result"""
        try:
            result = subprocess.run(
                command, 
                shell=shell, 
                capture_output=True, 
                text=True,
                timeout=10
            )
            return result.returncode, result.stdout, result.stderr
        except Exception as e:
            return -1, "", str(e)
    
    def wait_for_enter(self, message: str = "Press Enter to continue..."):
        """Wait for user to press Enter"""
        print(f"\n{Colors.WARNING}{message}{Colors.ENDC}")
        input()

    # ==================== MODULE FUNCTIONS ====================
    
    def core_commands(self):
        """Linux core commands tutorial with examples"""
        self.print_header("LINUX CORE COMMANDS")
        
        # Command Structure Diagram
        diagram = f"""
{Colors.CYAN}
                    LINUX COMMAND STRUCTURE
        
                    ┌─────────────────────────────────────┐
                    │   command [options] [arguments]    │
                    └─────────────────────────────────────┘
                                    │
            ┌───────────────────────┼───────────────────────┐
            ▼                       ▼                       ▼
        ┌──────────┐          ┌──────────┐          ┌──────────┐
        │   ls     │          │  -la     │          │ /home   │
        │ (action) │          │ (flags)  │          │ (target) │
        └──────────┘          └──────────┘          └──────────┘
{Colors.ENDC}
        """
        print(diagram)
        
        commands = [
            {
                "cmd": "ls",
                "desc": "List directory contents",
                "examples": [
                    "ls           - Basic listing",
                    "ls -l        - Detailed listing",
                    "ls -la       - Show hidden files",
                    "ls -lh       - Human readable sizes",
                    "ls -ltr      - Sort by time (reverse)"
                ]
            },
            {
                "cmd": "cd",
                "desc": "Change directory",
                "examples": [
                    "cd /home     - Go to /home",
                    "cd ~         - Go to home directory",
                    "cd ..        - Go up one level",
                    "cd -         - Go to previous directory",
                    "cd /         - Go to root"
                ]
            },
            {
                "cmd": "pwd",
                "desc": "Print working directory",
                "examples": [
                    "pwd          - Show current path",
                    "pwd -P       - Show physical path (no symlinks)"
                ]
            },
            {
                "cmd": "cat",
                "desc": "Concatenate and display files",
                "examples": [
                    "cat file.txt        - Display file",
                    "cat -n file.txt     - Show with line numbers",
                    "cat file1 file2     - Concatenate files",
                    "cat > file.txt      - Create new file"
                ]
            },
            {
                "cmd": "mkdir/rmdir",
                "desc": "Create/remove directories",
                "examples": [
                    "mkdir dir           - Create directory",
                    "mkdir -p a/b/c      - Create nested dirs",
                    "rmdir dir           - Remove empty dir",
                    "rm -rf dir          - Remove dir and contents"
                ]
            },
            {
                "cmd": "cp/mv/rm",
                "desc": "Copy, move, remove files",
                "examples": [
                    "cp file1 file2      - Copy file",
                    "cp -r dir1 dir2     - Copy directory",
                    "mv file1 file2      - Rename/move file",
                    "rm file.txt         - Remove file",
                    "rm -i file.txt      - Remove with prompt"
                ]
            },
            {
                "cmd": "touch",
                "desc": "Create empty file or update timestamp",
                "examples": [
                    "touch file.txt      - Create empty file",
                    "touch -c file.txt   - Don't create if missing",
                    "touch -t 20240101 file.txt  - Set specific time"
                ]
            },
        ]
        
        for item in commands:
            print(f"{Colors.BOLD}{Colors.CYAN}▸ {item['cmd']}{Colors.ENDC} - {item['desc']}")
            print(f"{Colors.CYAN}{'─' * 70}{Colors.ENDC}")
            for ex in item['examples']:
                parts = ex.split(' - ')
                if len(parts) == 2:
                    print(f"  {Colors.GREEN}{parts[0]:<30}{Colors.ENDC} {parts[1]}")
                else:
                    print(f"  {Colors.GREEN}{ex}{Colors.ENDC}")
            print()
            
        # Live Demo
        print(f"{Colors.BOLD}Live System Information:{Colors.ENDC}\n")
        
        demos = [
            ("Current Directory", "pwd"),
            ("List Files", "ls -la"),
            ("Disk Usage", "df -h | head -5"),
        ]
        
        for name, cmd in demos:
            print(f"  {Colors.CYAN}{name}:{Colors.ENDC}")
            returncode, stdout, stderr = self.run_command(cmd)
            if returncode == 0 and stdout:
                for line in stdout.strip().split('\n')[:3]:
                    print(f"    {line}")
            print()
            
        self.wait_for_enter()

    def filesystem_navigation(self):
        """File system hierarchy and navigation"""
        self.print_header("FILE SYSTEM NAVIGATION")
        
        # Linux Filesystem Hierarchy
        diagram = f"""
{Colors.CYAN}
                    LINUX FILESYSTEM HIERARCHY (FHS)
        
                           ┌─────────┐
                           │    /    │  Root Directory
                           └────┬────┘
            ┌────────┬────────┼────────┬────────┬────────┐
            ▼        ▼        ▼        ▼        ▼        ▼
        ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
        │ /bin │ │/sbin │ │/etc  │ │/home │ │/var  │ │/tmp  │
        │  ↑   │ │  ↑   │ │  ↑   │ │  ↑   │ │  ↑   │ │  ↑   │
        │Essential│System │Config│  User │Variable│Temporary│
        │Commands │Admin  │Files │  Homes│  Data  │  Files  │
        └──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘
{Colors.ENDC}
        """
        print(diagram)
        
        directories = [
            ("/", "Root directory - top of filesystem"),
            ("/bin", "Essential user command binaries"),
            ("/sbin", "System administration binaries"),
            ("/etc", "Configuration files"),
            ("/home", "User home directories"),
            ("/root", "Root user's home directory"),
            ("/var", "Variable data (logs, mail, spool)"),
            ("/tmp", "Temporary files"),
            ("/usr", "User programs and data"),
            ("/opt", "Optional add-on software"),
            ("/mnt", "Mount point for filesystems"),
            ("/media", "Removable media mount points"),
            ("/dev", "Device files"),
            ("/proc", "Process information (virtual)"),
            ("/sys", "System information (virtual)"),
            ("/lib", "Essential shared libraries"),
            ("/boot", "Boot loader files"),
        ]
        
        print(f"{Colors.BOLD}Standard Directories:{Colors.ENDC}\n")
        print(f"  {'Path':<12} {'Description':<50}")
        print(f"  {'─' * 65}")
        
        for path, desc in directories:
            print(f"  {Colors.CYAN}{path:<12}{Colors.ENDC} {desc}")
            
        # Navigation Tips
        print(f"\n{Colors.BOLD}Navigation Shortcuts:{Colors.ENDC}\n")
        
        shortcuts = [
            ("~", "Home directory of current user"),
            (".", "Current directory"),
            ("..", "Parent directory"),
            ("-", "Previous working directory"),
            ("~username", "Home directory of specified user"),
        ]
        
        for shortcut, meaning in shortcuts:
            print(f"  {Colors.GREEN}{shortcut:<15}{Colors.ENDC} {meaning}")
            
        # Path Types
        print(f"\n{Colors.BOLD}Path Types:{Colors.ENDC}\n")
        
        print(f"  {Colors.WARNING}Absolute Path:{Colors.ENDC} Starts from root (/)")
        print(f"    Example: {Colors.CYAN}/home/user/documents/file.txt{Colors.ENDC}")
        print(f"\n  {Colors.WARNING}Relative Path:{Colors.ENDC} Starts from current directory")
        print(f"    Example: {Colors.CYAN}../documents/file.txt{Colors.ENDC}")
        print(f"    Example: {Colors.CYAN}./script.sh{Colors.ENDC}")
        
        self.wait_for_enter()

    def file_permissions(self):
        """File permissions and ownership tutorial"""
        self.print_header("FILE PERMISSIONS & OWNERSHIP")
        
        # Permission Structure Diagram
        diagram = f"""
{Colors.CYAN}
                    FILE PERMISSION STRUCTURE
        
                 ┌─────────────────────────────────────┐
                 │  -  rwx  r-x  r--  file.txt          │
                 │  │   │    │    │                      │
                 │  │   │    │    └─ Others (r--)        │
                 │  │   │    └────── Group (r-x)        │
                 │  │   └─────────── Owner (rwx)          │
                 │  └────────────── File type (-)         │
                 └─────────────────────────────────────┘
        
                 PERMISSION VALUES:
                 ┌─────────┬─────────┬─────────┐
                 │   r     │    w    │    x    │
                 │  read   │  write  │ execute │
                 │   4     │    2    │    1    │
                 └─────────┴─────────┴─────────┘
{Colors.ENDC}
        """
        print(diagram)
        
        print(f"{Colors.BOLD}Permission Notation:{Colors.ENDC}\n")
        
        notations = [
            ("-", "Regular file"),
            ("d", "Directory"),
            ("l", "Symbolic link"),
            ("c", "Character device"),
            ("b", "Block device"),
            ("r", "Read permission (4)"),
            ("w", "Write permission (2)"),
            ("x", "Execute permission (1)"),
            ("-", "No permission (0)"),
        ]
        
        print(f"  {'Symbol':<10} {'Meaning':<30}")
        print(f"  {'─' * 45}")
        for sym, meaning in notations:
            print(f"  {Colors.CYAN}{sym:<10}{Colors.ENDC} {meaning}")
            
        # Numeric Examples
        print(f"\n{Colors.BOLD}Numeric Permission Examples:{Colors.ENDC}\n")
        
        examples = [
            ("777", "rwxrwxrwx", "Full access for everyone"),
            ("755", "rwxr-xr-x", "Owner full, others read+execute"),
            ("644", "rw-r--r--", "Owner read+write, others read"),
            ("700", "rwx------", "Owner only access"),
            ("600", "rw-------", "Owner read+write only"),
            ("444", "r--r--r--", "Read-only for everyone"),
        ]
        
        print(f"  {'Numeric':<10} {'Symbolic':<15} {'Description':<35}")
        print(f"  {'─' * 65}")
        for num, sym, desc in examples:
            print(f"  {Colors.GREEN}{num:<10}{Colors.ENDC} {Colors.CYAN}{sym:<15}{Colors.ENDC} {desc}")
            
        # Commands
        print(f"\n{Colors.BOLD}Permission Commands:{Colors.ENDC}\n")
        
        commands = [
            ("chmod 755 file.txt", "Change file permissions"),
            ("chmod u+x script.sh", "Add execute for owner"),
            ("chmod go-w file.txt", "Remove write for group/others"),
            ("chown user:group file", "Change owner and group"),
            ("chown root file.txt", "Change owner to root"),
            ("chgrp users file.txt", "Change group to users"),
        ]
        
        for cmd, desc in commands:
            print(f"  {Colors.GREEN}{cmd:<30}{Colors.ENDC} {desc}")
            
        # Special Permissions
        print(f"\n{Colors.BOLD}Special Permissions:{Colors.ENDC}\n")
        
        special = [
            ("SUID (4000)", "s in owner execute - run as file owner"),
            ("SGID (2000)", "s in group execute - run as file group"),
            ("Sticky (1000)", "t in others - only owner can delete"),
        ]
        
        print(f"  {'Type':<15} {'Description':<50}")
        print(f"  {'─' * 70}")
        for perm_type, desc in special:
            print(f"  {Colors.WARNING}{perm_type:<15}{Colors.ENDC} {desc}")
            
        # Live Example
        print(f"\n{Colors.BOLD}Live Permission Examples:{Colors.ENDC}\n")
        
        returncode, stdout, stderr = self.run_command("ls -la /etc/passwd /bin/ls ~ | head -10")
        if returncode == 0 and stdout:
            for line in stdout.strip().split('\n'):
                print(f"  {line}")
                
        self.wait_for_enter()

    def process_management(self):
        """Process management and handling"""
        self.print_header("PROCESS MANAGEMENT")
        
        # Process States Diagram
        diagram = f"""
{Colors.CYAN}
                    PROCESS LIFECYCLE
        
              ┌─────────┐
              │  START  │
              └────┬────┘
                   ▼
              ┌─────────┐
              │ RUNNING │◄──────────────────┐
              └────┬────┘                   │
                   │                        │
         ┌─────────┼─────────┐              │
         ▼         ▼         ▼              │
    ┌────────┐ ┌────────┐ ┌────────┐      │
    │SLEEPING│ │STOPPED │ │ZOMBIE  │      │
    │(wait)  │ │(SIGSTOP)│ │(orphan)│      │
    └────┬───┘ └────┬───┘ └────────┘      │
         │        │                       │
         └────────┼───────────────────────┘
                  ▼
             ┌─────────┐
             │  EXIT   │
             │(SIGTERM)│
             └─────────┘
{Colors.ENDC}
        """
        print(diagram)
        
        print(f"{Colors.BOLD}Process States:{Colors.ENDC}\n")
        
        states = [
            ("R (running)", "Currently executing or in run queue"),
            ("S (sleeping)", "Waiting for event to complete"),
            ("D (disk sleep)", "Uninterruptible sleep (usually IO)"),
            ("T (stopped)", "Stopped by job control signal"),
            ("Z (zombie)", "Terminated but not reaped by parent"),
        ]
        
        print(f"  {'State':<15} {'Description':<50}")
        print(f"  {'─' * 70}")
        for state, desc in states:
            print(f"  {Colors.CYAN}{state:<15}{Colors.ENDC} {desc}")
            
        # Process Commands
        print(f"\n{Colors.BOLD}Process Commands:{Colors.ENDC}\n")
        
        commands = [
            {
                "title": "Viewing Processes",
                "cmds": [
                    ("ps", "Current terminal processes"),
                    ("ps aux", "All processes detailed"),
                    ("ps -ef", "Full format listing"),
                    ("top", "Interactive process viewer"),
                    ("htop", "Enhanced interactive viewer"),
                    ("pgrep name", "Find process by name"),
                    ("pidof name", "Get PID of process"),
                ]
            },
            {
                "title": "Managing Processes",
                "cmds": [
                    ("kill PID", "Terminate process by PID"),
                    ("kill -9 PID", "Force kill (SIGKILL)"),
                    ("killall name", "Kill by process name"),
                    ("pkill name", "Kill matching processes"),
                    ("kill -STOP PID", "Pause process"),
                    ("kill -CONT PID", "Resume process"),
                ]
            },
            {
                "title": "Background Jobs",
                "cmds": [
                    ("command &", "Run in background"),
                    ("Ctrl+Z", "Suspend current job"),
                    ("bg", "Resume job in background"),
                    ("fg", "Bring job to foreground"),
                    ("jobs", "List active jobs"),
                    ("disown", "Detach job from terminal"),
                ]
            },
        ]
        
        for section in commands:
            print(f"{Colors.CYAN}{section['title']}:{Colors.ENDC}")
            for cmd, desc in section['cmds']:
                print(f"  {Colors.GREEN}{cmd:<20}{Colors.ENDC} {desc}")
            print()
            
        # Live Process Demo
        print(f"{Colors.BOLD}Current System Processes:{Colors.ENDC}\n")
        
        demos = [
            ("Top CPU Processes", "ps aux --sort=-%cpu | head -6"),
            ("Process Count", "ps aux | wc -l"),
            ("Current User Processes", "ps aux | grep ^$USER | wc -l"),
        ]
        
        for name, cmd in demos:
            print(f"  {Colors.CYAN}{name}:{Colors.ENDC}")
            returncode, stdout, stderr = self.run_command(cmd)
            if returncode == 0 and stdout:
                for line in stdout.strip().split('\n'):
                    print(f"    {line}")
            print()
            
        self.wait_for_enter()

    def user_management(self):
        """User and group management"""
        self.print_header("USER & GROUP MANAGEMENT")
        
        # User Hierarchy
        diagram = f"""
{Colors.CYAN}
                    USER HIERARCHY IN LINUX
        
                        ┌─────────────┐
                        │    root     │
                        │  (UID: 0)   │
                        │   God Mode  │
                        └──────┬──────┘
                               │
          ┌────────────────────┼────────────────────┐
          ▼                    ▼                    ▼
    ┌──────────┐       ┌──────────┐       ┌──────────┐
    │ Sudoers  │       │ Regular  │       │ Service  │
    │  (admin) │       │  Users   │       │  Users   │
    │ UID 1000+│       │ UID 1000+│       │  UID 1-999│
    └──────────┘       └──────────┘       └──────────┘
{Colors.ENDC}
        """
        print(diagram)
        
        print(f"{Colors.BOLD}User Information Files:{Colors.ENDC}\n")
        
        files = [
            ("/etc/passwd", "User account information"),
            ("/etc/shadow", "Encrypted passwords (root only)"),
            ("/etc/group", "Group information"),
            ("/etc/sudoers", "Sudo privileges configuration"),
        ]
        
        print(f"  {'File':<20} {'Purpose':<45}")
        print(f"  {'─' * 70}")
        for f, purpose in files:
            print(f"  {Colors.CYAN}{f:<20}{Colors.ENDC} {purpose}")
            
        # User Commands
        print(f"\n{Colors.BOLD}User Management Commands:{Colors.ENDC}\n")
        
        commands = [
            {
                "title": "User Operations",
                "cmds": [
                    ("whoami", "Show current user"),
                    ("who", "Show logged in users"),
                    ("w", "Show who and what they're doing"),
                    ("id", "Show user/group IDs"),
                    ("last", "Show login history"),
                    ("finger user", "Show user info"),
                ]
            },
            {
                "title": "Creating Users (root)",
                "cmds": [
                    ("useradd name", "Create new user"),
                    ("useradd -m name", "Create user with home"),
                    ("passwd name", "Set user password"),
                    ("usermod -aG group user", "Add to group"),
                    ("userdel name", "Delete user"),
                    ("deluser name", "Delete user (Debian)"),
                ]
            },
            {
                "title": "Sudo Operations",
                "cmds": [
                    ("sudo command", "Run as root"),
                    ("sudo -i", "Interactive root shell"),
                    ("sudo -u user cmd", "Run as specific user"),
                    ("su -", "Switch to root"),
                    ("su - user", "Switch to user"),
                ]
            },
        ]
        
        for section in commands:
            print(f"{Colors.CYAN}{section['title']}:{Colors.ENDC}")
            for cmd, desc in section['cmds']:
                print(f"  {Colors.GREEN}{cmd:<25}{Colors.ENDC} {desc}")
            print()
            
        # Current User Info
        print(f"{Colors.BOLD}Current Session Information:{Colors.ENDC}\n")
        
        demos = [
            ("Current User", "whoami"),
            ("User ID Info", "id"),
            ("Logged In Users", "who"),
        ]
        
        for name, cmd in demos:
            print(f"  {Colors.CYAN}{name}:{Colors.ENDC}")
            returncode, stdout, stderr = self.run_command(cmd)
            if returncode == 0 and stdout:
                for line in stdout.strip().split('\n'):
                    print(f"    {line}")
            print()
            
        self.wait_for_enter()

    def package_management(self):
        """APT package management for Kali/Debian"""
        self.print_header("PACKAGE MANAGEMENT (APT)")
        
        # APT Workflow
        diagram = f"""
{Colors.CYAN}
                    APT PACKAGE MANAGEMENT WORKFLOW
        
        ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
        │ apt      │───▶│ apt      │───▶│ apt      │───▶│ apt      │
        │ update   │    │ search   │    │ install  │    │ remove   │
        └──────────┘    └──────────┘    └──────────┘    └──────────┘
             │                                               │
             ▼                                               ▼
        ┌────────────────┐                           ┌──────────┐
        │ Refresh pkg    │                           │ apt      │
        │ lists from     │                           │ purge    │
        │ repositories   │                           │ (remove  │
        └────────────────┘                           │ + config)│
                                                   └──────────┘
{Colors.ENDC}
        """
        print(diagram)
        
        print(f"{Colors.BOLD}Essential APT Commands:{Colors.ENDC}\n")
        
        commands = [
            {
                "title": "Package Information",
                "cmds": [
                    ("apt update", "Update package lists"),
                    ("apt list", "List available packages"),
                    ("apt list --installed", "List installed packages"),
                    ("apt search keyword", "Search for package"),
                    ("apt show pkg", "Show package details"),
                    ("apt-cache policy pkg", "Show version info"),
                ]
            },
            {
                "title": "Installing/Removing",
                "cmds": [
                    ("apt install pkg", "Install package"),
                    ("apt install -f", "Fix broken dependencies"),
                    ("apt remove pkg", "Remove package (keep config)"),
                    ("apt purge pkg", "Remove package + config"),
                    ("apt autoremove", "Remove unused packages"),
                    ("apt clean", "Clear downloaded packages"),
                ]
            },
            {
                "title": "System Upgrade",
                "cmds": [
                    ("apt upgrade", "Upgrade installed packages"),
                    ("apt full-upgrade", "Upgrade + handle deps"),
                    ("apt dist-upgrade", "Distribution upgrade"),
                    ("apt-get dselect-upgrade", "Advanced upgrade"),
                ]
            },
            {
                "title": "DPKG (Direct .deb)",
                "cmds": [
                    ("dpkg -i pkg.deb", "Install .deb package"),
                    ("dpkg -r pkg", "Remove package"),
                    ("dpkg -l", "List installed packages"),
                    ("dpkg -L pkg", "List files from package"),
                    ("dpkg -S file", "Find which pkg owns file"),
                ]
            },
        ]
        
        for section in commands:
            print(f"{Colors.CYAN}{section['title']}:{Colors.ENDC}")
            for cmd, desc in section['cmds']:
                print(f"  {Colors.GREEN}{cmd:<30}{Colors.ENDC} {desc}")
            print()
            
        # Kali Specific
        print(f"{Colors.BOLD}Kali Linux Specific:{Colors.ENDC}\n")
        
        kali_cmds = [
            ("apt install kali-linux-default", "Install default tools"),
            ("apt install kali-linux-large", "Install large toolset"),
            ("apt install kali-linux-everything", "Install all tools"),
            ("apt install kali-tools-top10", "Top 10 tools only"),
        ]
        
        for cmd, desc in kali_cmds:
            print(f"  {Colors.WARNING}{cmd:<35}{Colors.ENDC} {desc}")
            
        self.wait_for_enter()

    def network_commands(self):
        """Network commands for Kali Linux"""
        self.print_header("NETWORK COMMANDS")
        
        # Network Stack
        diagram = f"""
{Colors.CYAN}
                    NETWORK COMMAND LAYERS
        
              Application Layer (HTTP/FTP/SSH)
                       ▼
              ┌────────────────────────────────┐
              │        Transport Layer         │
              │    (TCP/UDP - ports)           │
              └──────────────┬─────────────────┘
                             ▼
              ┌────────────────────────────────┐
              │        Network Layer           │
              │    (IP - addressing)           │
              └──────────────┬─────────────────┘
                             ▼
              ┌────────────────────────────────┐
              │       Data Link Layer          │
              │    (MAC - interface)           │
              └────────────────────────────────┘
{Colors.ENDC}
        """
        print(diagram)
        
        print(f"{Colors.BOLD}Network Configuration Commands:{Colors.ENDC}\n")
        
        commands = [
            {
                "title": "Interface & IP",
                "cmds": [
                    ("ip addr", "Show IP addresses"),
                    ("ip link", "Show network interfaces"),
                    ("ip route", "Show routing table"),
                    ("ifconfig", "Legacy interface info"),
                    ("iwconfig", "Wireless interface info"),
                ]
            },
            {
                "title": "Connectivity Testing",
                "cmds": [
                    ("ping host", "Test connectivity"),
                    ("traceroute host", "Trace route path"),
                    ("tracepath host", "Trace without root"),
                    ("mtr host", "Dynamic traceroute"),
                ]
            },
            {
                "title": "DNS & Resolution",
                "cmds": [
                    ("nslookup host", "Query DNS server"),
                    ("dig host", "Detailed DNS query"),
                    ("host domain", "DNS lookup"),
                    ("whois domain", "Domain registration"),
                ]
            },
            {
                "title": "Network Scanning (Kali)",
                "cmds": [
                    ("nmap -sP network", "Ping sweep"),
                    ("nmap -sT target", "TCP connect scan"),
                    ("nmap -sS target", "SYN scan (root)"),
                    ("nmap -O target", "OS detection"),
                    ("nmap -sV target", "Service version"),
                    ("netdiscover", "ARP scanning"),
                ]
            },
            {
                "title": "Connection Monitoring",
                "cmds": [
                    ("netstat -tuln", "Show listening ports"),
                    ("ss -tuln", "Modern netstat"),
                    ("lsof -i", "List open files (network)"),
                    ("tcpdump -i eth0", "Capture packets"),
                ]
            },
        ]
        
        for section in commands:
            print(f"{Colors.CYAN}{section['title']}:{Colors.ENDC}")
            for cmd, desc in section['cmds']:
                print(f"  {Colors.GREEN}{cmd:<25}{Colors.ENDC} {desc}")
            print()
            
        # Network Files
        print(f"{Colors.BOLD}Important Network Files:{Colors.ENDC}\n")
        
        net_files = [
            ("/etc/hosts", "Local hostname mappings"),
            ("/etc/resolv.conf", "DNS server configuration"),
            ("/etc/network/interfaces", "Network interface config"),
            ("/etc/hostname", "System hostname"),
        ]
        
        print(f"  {'File':<30} {'Purpose':<40}")
        print(f"  {'─' * 75}")
        for f, purpose in net_files:
            print(f"  {Colors.CYAN}{f:<30}{Colors.ENDC} {purpose}")
            
        self.wait_for_enter()

    def text_processing(self):
        """Text processing and manipulation tools"""
        self.print_header("TEXT PROCESSING TOOLS")
        
        # Text Pipeline
        diagram = f"""
{Colors.CYAN}
                    TEXT PROCESSING PIPELINE
        
        ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
        │  cat     │───▶│  grep    │───▶│  sort    │───▶│  uniq    │
        │  file    │    │  filter  │    │  order   │    │  dedup   │
        └──────────┘    └──────────┘    └──────────┘    └──────────┘
                                                       │
                                                       ▼
        ┌──────────┐    ┌──────────┐             ┌──────────┐
        │  sed     │    │  awk     │             │  wc      │
        │  stream  │    │  process │             │  count   │
        │  editor  │    │  text    │             │          │
        └──────────┘    └──────────┘             └──────────┘
{Colors.ENDC}
        """
        print(diagram)
        
        print(f"{Colors.BOLD}Essential Text Processing Commands:{Colors.ENDC}\n")
        
        commands = [
            {
                "title": "Viewing & Searching",
                "cmds": [
                    ("cat file", "Display entire file"),
                    ("head -n 10 file", "Show first 10 lines"),
                    ("tail -n 10 file", "Show last 10 lines"),
                    ("tail -f file", "Follow file changes"),
                    ("less file", "Paged viewer (q to quit)"),
                    ("more file", "Simple pager"),
                ]
            },
            {
                "title": "Grep - Pattern Search",
                "cmds": [
                    ("grep 'pattern' file", "Search in file"),
                    ("grep -i 'pattern' file", "Case insensitive"),
                    ("grep -r 'pattern' dir/", "Recursive search"),
                    ("grep -n 'pattern' file", "Show line numbers"),
                    ("grep -v 'pattern' file", "Invert match"),
                    ("grep -E 'p1|p2' file", "Extended regex (OR)"),
                    ("egrep 'pattern' file", "Same as grep -E"),
                    ("fgrep 'pattern' file", "Fixed strings (no regex)"),
                ]
            },
            {
                "title": "Sed - Stream Editor",
                "cmds": [
                    ("sed 's/old/new/' file", "Replace first occurrence"),
                    ("sed 's/old/new/g' file", "Replace all"),
                    ("sed '/pattern/d' file", "Delete matching lines"),
                    ("sed '3d' file", "Delete line 3"),
                    ("sed -i 's/old/new/g' file", "Edit in place"),
                ]
            },
            {
                "title": "Awk - Text Processing",
                "cmds": [
                    ("awk '{print $1}' file", "Print first field"),
                    ("awk '{print $NF}' file", "Print last field"),
                    ("awk -F: '{print $1}' file", "Use : as delimiter"),
                    ("awk '/pattern/ {print}' file", "Print matching lines"),
                    ("awk '{sum+=$1} END {print sum}'", "Sum column"),
                ]
            },
            {
                "title": "Sorting & Counting",
                "cmds": [
                    ("sort file", "Alphabetic sort"),
                    ("sort -n file", "Numeric sort"),
                    ("sort -r file", "Reverse sort"),
                    ("uniq file", "Remove duplicate lines"),
                    ("uniq -c file", "Count duplicates"),
                    ("wc -l file", "Count lines"),
                    ("wc -w file", "Count words"),
                    ("wc -c file", "Count bytes"),
                ]
            },
            {
                "title": "Advanced Tools",
                "cmds": [
                    ("cut -d: -f1 file", "Extract field"),
                    ("paste file1 file2", "Merge files side-by-side"),
                    ("tr 'a-z' 'A-Z'", "Translate characters"),
                    ("diff file1 file2", "Compare files"),
                    ("comm file1 file2", "Compare sorted files"),
                ]
            },
        ]
        
        for section in commands:
            print(f"{Colors.CYAN}{section['title']}:{Colors.ENDC}")
            for cmd, desc in section['cmds']:
                print(f"  {Colors.GREEN}{cmd:<35}{Colors.ENDC} {desc}")
            print()
            
        # Pipeline Example
        print(f"{Colors.BOLD}Powerful Pipeline Example:{Colors.ENDC}\n")
        print(f"  {Colors.WARNING}cat /var/log/auth.log | grep 'Failed' | awk '{{print $11}}' | sort | uniq -c | sort -rn{Colors.ENDC}")
        print(f"  {Colors.CYAN}↑ Show failed login attempts and count by IP{Colors.ENDC}")
        
        self.wait_for_enter()

    def system_info(self):
        """System information for Linux/Kali"""
        self.print_header("SYSTEM INFORMATION")
        
        # System Architecture
        diagram = f"""
{Colors.CYAN}
                    LINUX SYSTEM ARCHITECTURE
        
        ┌─────────────────────────────────────────────────────────────┐
        │                      USER SPACE                             │
        │    Shells, Libraries, Applications (including Kali tools)    │
        └─────────────────────────┬───────────────────────────────────┘
                                  │ System Calls
        ┌─────────────────────────▼───────────────────────────────────┐
        │                    KERNEL SPACE                             │
        │   Process Mgmt │ Memory Mgmt │ File Systems │ Device Drivers│
        └─────────────────────────┬───────────────────────────────────┘
                                  │
        ┌─────────────────────────▼───────────────────────────────────┐
        │                      HARDWARE                               │
        │     CPU    │    Memory    │    Storage    │   Network     │
        └─────────────────────────────────────────────────────────────┘
{Colors.ENDC}
        """
        print(diagram)
        
        print(f"{Colors.BOLD}System Information Commands:{Colors.ENDC}\n")
        
        commands = [
            {
                "title": "Hardware Info",
                "cmds": [
                    ("uname -a", "Kernel info"),
                    ("hostnamectl", "System hostname info"),
                    ("lscpu", "CPU information"),
                    ("lsmem", "Memory information"),
                    ("lsblk", "Block devices"),
                    ("lspci", "PCI devices"),
                    ("lsusb", "USB devices"),
                    ("dmidecode", "DMI/BIOS info"),
                ]
            },
            {
                "title": "Resource Usage",
                "cmds": [
                    ("free -h", "Memory usage"),
                    ("df -h", "Disk usage"),
                    ("du -sh dir", "Directory size"),
                    ("uptime", "System uptime"),
                    ("vmstat", "Virtual memory stats"),
                    ("iostat", "CPU and I/O stats"),
                ]
            },
            {
                "title": "System Services",
                "cmds": [
                    ("systemctl status service", "Service status"),
                    ("systemctl list-units", "List active units"),
                    ("systemctl start service", "Start service"),
                    ("systemctl stop service", "Stop service"),
                    ("systemctl enable service", "Enable at boot"),
                    ("systemctl disable service", "Disable at boot"),
                ]
            },
        ]
        
        for section in commands:
            print(f"{Colors.CYAN}{section['title']}:{Colors.ENDC}")
            for cmd, desc in section['cmds']:
                print(f"  {Colors.GREEN}{cmd:<30}{Colors.ENDC} {desc}")
            print()
            
        # Kali Specific Info
        print(f"{Colors.BOLD}Kali Linux Specific Info:{Colors.ENDC}\n")
        
        demos = [
            ("OS Release", "cat /etc/os-release"),
            ("Kernel Version", "uname -r"),
            ("Architecture", "uname -m"),
            ("Hostname", "hostname"),
            ("Current User", "whoami"),
        ]
        
        for name, cmd in demos:
            print(f"  {Colors.CYAN}{name}:{Colors.ENDC}")
            returncode, stdout, stderr = self.run_command(cmd)
            if returncode == 0 and stdout:
                for line in stdout.strip().split('\n'):
                    print(f"    {line}")
            print()
            
        self.wait_for_enter()

    def exit_app(self):
        """Exit the application"""
        self.clear_screen()
        print(f"""
{Colors.CYAN}
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║              Thank you for using Kali Linux Basics Lab!                       ║
║                                                                              ║
║                    Keep learning, keep hacking ethically.                     ║
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
        app = KaliLab()
        app.run()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}Interrupted by user. Exiting...{Colors.ENDC}")
        sys.exit(0)
