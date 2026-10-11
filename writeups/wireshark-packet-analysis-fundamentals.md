# Building a Penetration Testing Lab: Kali Linux on VirtualBox

## Platform
Coursework exercise — Toronto School of Management, Cybersecurity Specialist Co-op (Module: Penetration Testing / Operating Systems)

## Goal
To build a working, isolated virtual machine running Kali Linux — the standard operating system for penetration testing — so security tools can be used and tested safely without touching my main computer.

## What I Did

### Choosing the tools
- **VirtualBox** is a free virtualization product that lets one computer run other operating systems as isolated "guest" machines. There are many alternatives (VMware, Hyper-V, and others), but VirtualBox is free and widely used for learning labs.
- **Kali Linux** is a Debian-based Linux distribution built for penetration testing, security auditing, digital forensics, and reverse engineering, with several hundred security tools included.

### Guest VM vs. host
I installed Kali **as a guest inside VirtualBox** rather than as the main operating system. That keeps it separated from my everyday system, lets it interact with other VMs on a virtual network, and — most usefully — allows snapshots, so I can revert to a known-good state after breaking something. VirtualBox isn't limited to Kali either; it can run most x86 operating systems, including Windows and the BSD family.

### My configuration
From the VirtualBox Manager, the finished VM was set up as follows:
- **Name:** Kali Linux (status: Running)
- **Memory:** about 24 GB allocated to the VM
- **Virtual disk:** a 105 GB VirtualBox disk image (.vdi), dynamically sized
- **Installer:** `kali-linux-2022.1-installer-amd64.iso` (about 2.8 GB) attached as a virtual optical drive
- **Acceleration:** VT-x/AMD-V with nested paging
- **Display:** VMSVGA graphics controller, 16 MB video memory
- **Network:** a single Intel PRO/1000 MT Desktop adapter in **NAT** mode, so the VM can reach the internet but isn't directly exposed to my local network

One small thing I'd change on a rebuild: the VM's operating-system type was left as a generic "Linux 2.4 (64-bit)" profile. Kali is Debian-based, so selecting **Debian (64-bit)** would match it more accurately and let VirtualBox apply better default settings.

### Troubleshooting
The VM froze repeatedly at first. After working through the usual fixes without success, the cause turned out to be in the computer's firmware: hardware virtualization support was switched off. I had to go into the BIOS and **enable SVM (AMD's virtualization setting)** before VirtualBox could run the VM properly. It was a useful reminder that when software acts strangely, the cause isn't always in the software — sometimes it's a setting several layers below it.

## How This Connects to Cybersecurity
Virtual machines are used throughout security work for a few practical reasons:
- **Access to tools across platforms** — a single laptop can host Kali for penetration testing alongside Windows and other targets
- **Safe testing** — new tools and techniques can be tried without risking the host system, and a snapshot makes recovery quick
- **Malware analysis** — when a VM is properly configured and isolated from the network, suspicious files can be examined without putting real systems at risk

That last point matters most: isolation is only as good as its configuration, and a misconfigured network or shared folder can quietly undo it.

## What I Want to Learn Next
My next goal with this lab is building skills in detecting and analyzing malware across different operating systems — which would mean setting up an intentionally isolated analysis environment and learning to examine suspicious files safely.

## Key Takeaways
Building the lab taught me more than the checklist suggests. Resource allocation, network mode, and virtualization settings all affect whether a VM runs well, and the BIOS fix was a good example of troubleshooting past the obvious layer. More importantly, a working Kali VM is the foundation for nearly everything else I want to practice — web application testing, network scanning, and the hands-on rooms on platforms like TryHackMe.

## Screenshot
**Kali Linux VM running in VirtualBox Manager, showing the full configuration**
<img width="958" height="565" alt="kali-virtualbox-manager" src="https://github.com/user-attachments/assets/e61ffd45-fb82-453d-9fc4-abdd218b5e62" />
