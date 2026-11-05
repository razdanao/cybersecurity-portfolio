#!/usr/bin/env python3
"""Count NBNS, LLMNR, and SSDP UDP packets by source IP in a PCAP/PCAPNG.

This is a local triage helper, not a protocol validator or security verdict.
It prints aggregate protocol/source/count rows and never prints packet payloads.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path
from typing import Iterable

try:
    from scapy.all import IP, IPv6, UDP, PcapReader
except ImportError as exc:  # pragma: no cover - exercised when dependency is absent
    print(
        "Scapy is required. Install it in a virtual environment with: "
        "python -m pip install scapy",
        file=sys.stderr,
    )
    raise SystemExit(2) from exc

PROTOCOL_PORTS = {
    137: "NBNS",
    5355: "LLMNR",
    1900: "SSDP",
}


def source_ip(packet) -> str | None:
    """Return the packet's IPv4/IPv6 source address, or None if unavailable."""
    if IP in packet:
        return str(packet[IP].src)
    if IPv6 in packet:
        return str(packet[IPv6].src)
    return None


def count_packets(packets: Iterable) -> Counter[tuple[str, str]]:
    """Count packets by protocol and source IP when either UDP port matches."""
    counts: Counter[tuple[str, str]] = Counter()

    for packet in packets:
        if UDP not in packet:
            continue

        src = source_ip(packet)
        if src is None:
            continue

        udp = packet[UDP]
        matched_protocols = {
            PROTOCOL_PORTS[port]
            for port in (int(udp.sport), int(udp.dport))
            if port in PROTOCOL_PORTS
        }
        for protocol in matched_protocols:
            counts[(protocol, src)] += 1

    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "capture",
        type=Path,
        help="path to a local PCAP or PCAPNG file (keep raw captures private)",
    )
    args = parser.parse_args()

    if not args.capture.is_file():
        parser.error(f"capture file not found: {args.capture}")

    try:
        with PcapReader(str(args.capture)) as reader:
            counts = count_packets(reader)
    except (OSError, ValueError) as exc:
        print(f"Unable to read capture: {exc}", file=sys.stderr)
        return 1

    writer = csv.writer(sys.stdout, lineterminator="\n")
    writer.writerow(("protocol", "source_ip", "packet_count"))
    for (protocol, source), packet_count in sorted(counts.items()):
        writer.writerow((protocol, source, packet_count))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
