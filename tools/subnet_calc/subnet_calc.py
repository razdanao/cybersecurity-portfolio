#!/usr/bin/env python3
"""
subnet_calc: modular IPv4 subnet calculator (STARTER TEMPLATE).

Implemented for you: bit-level helpers and the Subnet class (core math done
manually with integers so you can see *why* each value is what it is).
YOUR TASKS: the three functions marked TODO below. Tests in tests/ define the
expected behaviour; the pre-written tests verify the core against Python's
stdlib `ipaddress` module.

Usage:
    python subnet_calc.py 192.0.2.77/26
    python subnet_calc.py 192.0.2.0/24 --json
Examples use RFC 5737 documentation ranges (192.0.2.0/24, 198.51.100.0/24,
203.0.113.0/24) so no real network is ever disclosed.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass

IPV4_BITS = 32
ALL_ONES = 0xFFFFFFFF


# --------------------------------------------------------------------------
# Layer 1: parsing and bit helpers
# --------------------------------------------------------------------------
def ip_to_int(ip: str) -> int:
    """'192.0.2.1' -> 3221225985. Each octet is 8 bits of a 32-bit integer."""
    parts = ip.strip().split(".")
    if len(parts) != 4:
        raise ValueError(f"Invalid IPv4 address: {ip!r}")
    value = 0
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            raise ValueError(f"Invalid octet {part!r} in {ip!r}")
        value = (value << 8) | int(part)
    return value


def int_to_ip(value: int) -> str:
    if not 0 <= value <= ALL_ONES:
        raise ValueError("Value outside IPv4 range")
    return ".".join(str((value >> shift) & 0xFF) for shift in (24, 16, 8, 0))


def prefix_to_mask(prefix: int) -> int:
    """/26 -> 255.255.255.192: `prefix` leading 1-bits, remainder 0-bits."""
    if not 0 <= prefix <= IPV4_BITS:
        raise ValueError("Prefix must be between 0 and 32")
    return (ALL_ONES << (IPV4_BITS - prefix)) & ALL_ONES


def to_binary(value: int) -> str:
    """Dotted binary, e.g. 11000000.00000000.00000010.01001101"""
    return ".".join(f"{(value >> s) & 0xFF:08b}" for s in (24, 16, 8, 0))


def parse_cidr(cidr: str) -> tuple[int, int]:
    """'192.0.2.77/26' -> (ip_as_int, 26)."""
    if "/" not in cidr:
        raise ValueError("Expected CIDR notation, e.g. 192.0.2.0/24")
    ip, prefix = cidr.split("/", 1)
    if not prefix.isdigit():
        raise ValueError(f"Invalid prefix: {prefix!r}")
    return ip_to_int(ip), int(prefix)


# --------------------------------------------------------------------------
# Layer 2: the Subnet model
# --------------------------------------------------------------------------
@dataclass(frozen=True)
class Subnet:
    """A subnet defined by its network address (host bits zeroed) and prefix."""

    network: int
    prefix: int

    @classmethod
    def from_cidr(cls, cidr: str) -> "Subnet":
        ip, prefix = parse_cidr(cidr)
        # WHY: AND with the mask zeroes the host bits, so 192.0.2.77/26
        # still resolves to its true network address 192.0.2.64.
        return cls(ip & prefix_to_mask(prefix), prefix)

    @property
    def mask(self) -> int:
        return prefix_to_mask(self.prefix)

    @property
    def wildcard(self) -> int:
        # Bitwise inverse of the mask (used in ACLs / OSPF network statements).
        return ~self.mask & ALL_ONES

    @property
    def broadcast(self) -> int:
        # Network address with all host bits set to 1.
        return self.network | self.wildcard

    @property
    def total_addresses(self) -> int:
        return 2 ** (IPV4_BITS - self.prefix)

    @property
    def usable_hosts(self) -> int:
        # /32 = single host route; /31 = point-to-point link (RFC 3021);
        # otherwise subtract the network and broadcast addresses.
        if self.prefix == 32:
            return 1
        if self.prefix == 31:
            return 2
        return self.total_addresses - 2

    @property
    def first_host(self) -> int:
        return self.network if self.prefix >= 31 else self.network + 1

    @property
    def last_host(self) -> int:
        return self.broadcast if self.prefix >= 31 else self.broadcast - 1

    def contains(self, ip: str) -> bool:
        return (ip_to_int(ip) & self.mask) == self.network

    def cidr(self) -> str:
        return f"{int_to_ip(self.network)}/{self.prefix}"

    def describe(self) -> dict:
        return {
            "cidr": self.cidr(),
            "network": int_to_ip(self.network),
            "netmask": int_to_ip(self.mask),
            "wildcard": int_to_ip(self.wildcard),
            "broadcast": int_to_ip(self.broadcast),
            "first_host": int_to_ip(self.first_host),
            "last_host": int_to_ip(self.last_host),
            "total_addresses": self.total_addresses,
            "usable_hosts": self.usable_hosts,
            "netmask_binary": to_binary(self.mask),
        }


# --------------------------------------------------------------------------
# Layer 3: YOUR TASKS
# --------------------------------------------------------------------------
def required_prefix(hosts_needed: int) -> int:
    """
    TODO 1: Return the longest prefix (smallest subnet) that can hold
    `hosts_needed` usable hosts on a conventional LAN subnet (network and
    broadcast addresses reserved, so the smallest answer is /30).

    Expected: 2 -> 30, 30 -> 27, 62 -> 26, 63 -> 25, 254 -> 24, 255 -> 23.
    Hint: you need 2**host_bits - 2 >= hosts_needed. Explain in a comment
    why the "- 2" exists. Raise ValueError for hosts_needed < 1 or > 2**32 - 2.
    """
    raise NotImplementedError("TODO 1")


def same_subnet(ip_a: str, ip_b: str, prefix: int) -> bool:
    """
    TODO 2: True if both addresses fall in the same subnet for this prefix.
    Use only integer AND with the mask (no ipaddress module). In a comment,
    explain why two hosts that differ in the network portion need a router
    to communicate (tie to ARP: ARP does not cross routers).
    """
    raise NotImplementedError("TODO 2")


def vlsm_plan(parent_cidr: str, requirements: dict[str, int]) -> list[tuple[str, str]]:
    """
    TODO 3: Variable-Length Subnet Masking.
    Given a parent block and {name: hosts_needed}, return a list of
    (name, subnet_cidr) with NON-OVERLAPPING subnets inside the parent.

    Algorithm: sort requirements largest-first (this avoids alignment gaps),
    size each with required_prefix(), then allocate sequentially from the
    parent's network address, advancing by each subnet's total_addresses.
    Raise ValueError if the plan does not fit in the parent block.

    Example: vlsm_plan("192.0.2.0/24", {"A": 50, "B": 20, "C": 2}) ->
        [("A", "192.0.2.0/26"), ("B", "192.0.2.64/27"), ("C", "192.0.2.96/30")]
    """
    raise NotImplementedError("TODO 3")


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------
def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="IPv4 subnet calculator")
    parser.add_argument("cidr", help="e.g. 192.0.2.77/26")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    args = parser.parse_args(argv)
    try:
        info = Subnet.from_cidr(args.cidr).describe()
    except ValueError as exc:
        parser.error(str(exc))
    if args.json:
        print(json.dumps(info, indent=2))
    else:
        for key, value in info.items():
            print(f"{key:>16}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
