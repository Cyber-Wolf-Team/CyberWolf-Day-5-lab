# Kali Linux Basics Lab - Command Laboratory

**Organization:** Cyber Wolf  
**Websites:** [www.cyberwolf.py](http://www.cyberwolf.py) | [www.zh5.club](http://www.zh5.club)  
**Developed by:** Tamilselvan .S, Cyber Security Researcher  
**Lab Type:** Mini Lab

A comprehensive CLI tool for learning Linux fundamentals on Kali Linux. Covers core commands, file system navigation, permissions, process handling, and more with interactive ASCII diagrams.

## Features

- **Linux Core Commands** - Essential commands (ls, cd, pwd, cat, cp, mv, rm, touch)
- **File System Navigation** - Linux FHS hierarchy and navigation shortcuts
- **File Permissions & Ownership** - chmod, chown, permission notation
- **Process Management** - ps, top, kill, background jobs
- **User & Group Management** - users, groups, sudo operations
- **Package Management (APT)** - apt, dpkg for Kali/Debian
- **Network Commands** - ip, ping, nmap, netstat for security testing
- **Text Processing Tools** - grep, sed, awk, sort, uniq, cut
- **System Information** - Hardware, resources, systemctl services

## Quick Start

### Make launcher executable and run:
```bash
chmod +x launch_lab.sh
./launch_lab.sh
```

### Or run directly with Python:
```bash
python3 kalilab.py
```

## Requirements

- Kali Linux or any Debian-based distribution
- Python 3.6 or higher
- Terminal with color support (for best experience)

## Menu Options

| Option | Feature | Description |
|--------|---------|-------------|
| 1 | Linux Core Commands | Essential file and directory commands |
| 2 | File System Navigation | Linux FHS and navigation shortcuts |
| 3 | File Permissions & Ownership | chmod, chown, permission examples |
| 4 | Process Management | ps, top, kill, background jobs |
| 5 | User & Group Management | users, sudo, permissions |
| 6 | Package Management (APT) | apt, dpkg for Kali/Debian |
| 7 | Network Commands | ip, ping, nmap, netstat |
| 8 | Text Processing Tools | grep, sed, awk, sort, uniq |
| 9 | System Information | Hardware, resources, services |
| 0 | Exit | Close the application |

## Interactive Features

### ASCII Diagrams
Each module includes visual ASCII diagrams:
- Command structure diagrams
- Filesystem hierarchy trees
- Permission structure charts
- Process lifecycle diagrams
- Network layer representations

### Navigation
- Press numbers 1-9 to select a module
- Press 0 to exit
- Press Enter to continue after viewing results

## Learning Path

### Beginner Level
1. Start with **Linux Core Commands** (Option 1)
2. Learn **File System Navigation** (Option 2)
3. Understand **File Permissions** (Option 3)

### Intermediate Level
4. Master **Process Management** (Option 4)
5. Learn **User Management** (Option 5)
6. Understand **Package Management** (Option 6)

### Advanced Level
7. Explore **Network Commands** (Option 7)
8. Master **Text Processing** (Option 8)
9. Check **System Information** (Option 9)

## Sample Commands Covered

### File Operations
```bash
ls -la                    # Detailed listing with hidden files
cd ~                      # Go to home directory
pwd                       # Show current path
cp -r source dest         # Copy directory
mv oldname newname        # Rename file
rm -rf directory          # Remove directory recursively
touch filename            # Create empty file
```

### Permissions
```bash
chmod 755 file.txt        # rwxr-xr-x
chmod u+x script.sh       # Add execute for owner
chown user:group file     # Change owner and group
```

### Process Management
```bash
ps aux                    # All processes
top                       # Interactive process viewer
kill -9 PID               # Force kill process
Ctrl+Z + bg               # Background job
```

### Network (Kali)
```bash
ip addr                   # Show IP addresses
nmap -sP 192.168.1.0/24   # Ping sweep
netstat -tuln             # Show listening ports
tcpdump -i eth0           # Capture packets
```

## File Structure

```
Linux-basics/
├── kalilab.py        # Main Python CLI application
├── launch_lab.sh     # Bash launcher script
└── README.md         # This file
```

## Troubleshooting

### Python Not Found
```bash
sudo apt update
sudo apt install python3
```

### Permission Denied on Launcher
```bash
chmod +x launch_lab.sh
```

### Colors Not Displaying
Ensure your terminal supports ANSI color codes. Most modern terminals do.

## About Cyber Wolf

Cyber Wolf is dedicated to providing quality cybersecurity education and tools for learning ethical hacking and system administration.

- **Website:** www.cyberwolf.py
- **Community:** www.zh5.club
- **Developer:** Tamilselvan .S

## License

This tool is for educational purposes only. Use responsibly and ethically.
