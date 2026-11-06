# Linux/Ubuntu CLI Quick Reference (Security-Relevant Subset)

Status: **Final** (reference notes, no lab evidence required)

Own working notes on the Ubuntu command-line surface most relevant to security work — permissions, process/service control, users, and networking. Condensed and reorganized from general Ubuntu admin references rather than a full command listing; skip straight to a section when you need it.

## System state
| Command | Purpose |
|---|---|
| `uname -a` | Kernel/OS version in one line |
| `hostnamectl` | Hostname and OS details |
| `top` / `htop` | Live process view |
| `df -h` | Disk usage, human-readable |
| `free -m` | Memory usage in MB |
| `kill <pid>` | Terminate a process by ID |

## File permissions and ownership
| Command | Purpose |
|---|---|
| `chmod u+x <file>` | Make a file executable by its owner |
| `chmod 600 <file>` | Owner read/write only, common for private keys |
| `chown user:group <file>` | Change file owner/group |
| `find <dir> -name <pattern>` | Locate files by name pattern |
| `grep <pattern> <file>` | Search file content |

## Users and groups
| Command | Purpose |
|---|---|
| `sudo adduser <user>` / `sudo deluser <user>` | Create/remove a user |
| `sudo passwd -l <user>` / `-u <user>` | Lock/unlock an account |
| `sudo chage <user>` | Set password expiry policy |
| `id <user>` / `groups <user>` | Show a user's UID/GID and group membership |
| `w` | Who's currently logged in |

## Services and logs (systemd)
| Command | Purpose |
|---|---|
| `sudo systemctl status/start/stop <svc>` | Control and check a service |
| `journalctl -f` | Tail the system journal live |
| `journalctl -u <unit>` | Logs for one specific unit |

## Networking
| Command | Purpose |
|---|---|
| `ip addr show` | Interfaces and IP addresses |
| `ss -l` | Listening sockets (replaces `netstat -l`) |
| `ping <host>` | Basic reachability test |
| `cat /etc/netplan/*.yaml` | Current network config |

## Firewall (UFW)
| Command | Purpose |
|---|---|
| `sudo ufw status` | Current rules/state |
| `sudo ufw allow/deny <port\|service>` | Add a rule |
| `sudo ufw delete allow/deny <port\|service>` | Remove a rule |

## Remote access
| Command | Purpose |
|---|---|
| `ssh user@host` | Remote shell |
| `scp source user@host:dest` | Copy a file over SSH |

## Packages
| Command | Purpose |
|---|---|
| `sudo apt update && sudo apt upgrade` | Refresh package lists and apply updates |
| `sudo apt install/remove/purge <pkg>` | Install, remove, or remove-with-configs |
| `apt-cache policy <pkg>` | See installed vs. available versions — useful when checking if a package is patched |

## Notes for security work specifically
- `chmod 600` + `chown` are the two commands worth memorizing for key/secret files — see the [cryptography study guide](../../cryptography/study-guide.md) on key protection.
- `ss -l` and `ip addr show` are the fastest way to confirm what's actually listening before trusting a firewall rule.
- `journalctl -u <unit>` is usually faster than digging through `/var/log` by hand when triaging a specific service.
