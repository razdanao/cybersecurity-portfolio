# Windows Deployment Services Lab Study

> **Type:** Hands-on lab study. **Status:** DRAFT — NOT STARTED. No PXE boot or image deployment is claimed.

## Purpose

Plan a disposable Windows deployment lab using Windows Deployment Services (WDS) and Preboot Execution Environment (PXE). The supplied reference describes WDS role and image setup but does not provide independently verifiable results in this portfolio. This plan keeps deployment activity inside virtual machines.

## Scope and safety

- Use a host-only or otherwise isolated virtual network. Never attach the lab's DHCP or PXE services to a shared network.
- Use disposable virtual client machines and test media that you are authorized to use.
- Record the Windows Server and client versions. WDS behavior and support depend on the Windows versions and deployment configuration; consult current Microsoft documentation before choosing media or procedures.
- Keep source images, answer files, administrator credentials, product keys, and recovery keys out of screenshots and source control.
- If DHCP and WDS share a server, follow Microsoft's current co-hosting guidance to avoid a port 67 conflict.

## Planned procedure

1. Draw the isolated lab network and decide whether DHCP and WDS will run on one server or separate servers.
2. Install the required server roles and management tools on a disposable server. Configure the WDS image store for the lab.
3. Check Microsoft's current WDS boot-image support and hands-free deployment hardening guidance for the exact server and client versions. If studying supported PXE behavior, use an authorized custom boot image. Do not use installation-media `boot.wim` as a WDS Windows 11 or Windows Server 2025 deployment workflow; Microsoft documents those workflows as blocked. Plan migration before the Windows Server release after 2025, where WDS is marked for deprecation.
4. Configure PXE responses so only the intended lab clients can boot into the deployment environment.
5. Start one disposable client VM using PXE. Confirm it contacts the expected DHCP/PXE services and downloads the expected boot image.
6. Stop at the deployment screen unless a full installation is specifically part of the lab. If installing, target only the disposable VM disk and record the exact image and options selected.
7. Remove temporary images or test accounts when finished and confirm the lab DHCP/WDS services are disconnected from shared networks.

## Evidence checklist

- Network diagram showing the lab boundary and DHCP/WDS placement.
- Role and service status with hostnames and account names redacted.
- Image version/source and checksum, where appropriate and safe to publish.
- PXE client boot evidence and the server response, with addresses and identifiers redacted.
- If an install is performed, guest version and a successful post-install check.
- Cleanup steps, troubleshooting notes, and limitations.

Do not mark this lab complete until the procedure is run and evidence supports each statement. A server role shown as installed is not proof that PXE deployment succeeded.

## Troubleshooting

- **Client does not start PXE:** Check VM firmware/network boot order, virtual network attachment, and whether the client is allowed to receive a PXE response.
- **Client receives no address:** Check DHCP service, scope, VLAN/host-only segment, address pool, and relay configuration if used.
- **Client gets an address but cannot locate WDS:** Check PXE discovery path, DNS where required, server configuration, firewall, and DHCP/WDS topology.
- **WDS and DHCP are co-hosted:** Review the “do not listen on DHCP port 67” setting and other Microsoft guidance for the exact configuration; do not change port behavior by guesswork.
- **Boot image starts but download fails:** Check TFTP reachability, boot image architecture, file paths, firewall rules, and server logs.
- **Client reaches the installer but sees no target image:** Confirm the installation image is added, compatible, enabled, and available to the selected client group.
- **Deployment targets the wrong disk:** Stop immediately and re-check the VM disk mapping before continuing. Never test imaging against a host or real workstation.

## Source and attribution

The exercise topic is adapted from the supplied *Personal Technical Reference & System Administration Guide* (four pages) and *Windows Server Infrastructure Technical Guide* (six pages). Their named hosts, domains, addresses, accounts, screenshots, and completion statements are not copied as evidence. WDS/PXE concepts and current limitations are checked against Microsoft's [WDS boot support guidance](https://learn.microsoft.com/en-us/windows/deployment/wds-boot-support), [PXE deployment requirements](https://learn.microsoft.com/en-ca/windows/deployment/configure-a-pxe-server-to-load-windows-pe), and [DHCP/WDS co-hosting guidance](https://learn.microsoft.com/en-us/troubleshoot/windows-server/setup-upgrade-and-drivers/wds-server-may-not-start).
