import ipaddress
import random

import pytest

import subnet_calc as sc


# ---------- Pre-written: core math verified against the stdlib ----------
@pytest.mark.parametrize("cidr", [
    "192.0.2.0/24", "192.0.2.77/26", "198.51.100.130/25", "203.0.113.5/30",
    "203.0.113.5/31", "203.0.113.5/32", "10.0.0.0/8", "0.0.0.0/0",  # sanitize: ignore
])
def test_core_matches_stdlib(cidr):
    mine = sc.Subnet.from_cidr(cidr)
    ref = ipaddress.ip_network(cidr, strict=False)
    assert sc.int_to_ip(mine.network) == str(ref.network_address)
    assert sc.int_to_ip(mine.mask) == str(ref.netmask)
    assert sc.int_to_ip(mine.wildcard) == str(ref.hostmask)
    assert sc.int_to_ip(mine.broadcast) == str(ref.broadcast_address)
    assert mine.total_addresses == ref.num_addresses


def test_random_cidrs_match_stdlib():
    rng = random.Random(1234)
    for _ in range(500):
        ip = sc.int_to_ip(rng.getrandbits(32))
        prefix = rng.randint(0, 32)
        mine = sc.Subnet.from_cidr(f"{ip}/{prefix}")
        ref = ipaddress.ip_network(f"{ip}/{prefix}", strict=False)
        assert sc.int_to_ip(mine.network) == str(ref.network_address)
        assert sc.int_to_ip(mine.broadcast) == str(ref.broadcast_address)


def test_worked_example_slash26():
    s = sc.Subnet.from_cidr("192.0.2.77/26")
    d = s.describe()
    assert d["network"] == "192.0.2.64"
    assert d["netmask"] == "255.255.255.192"
    assert d["broadcast"] == "192.0.2.127"
    assert (d["first_host"], d["last_host"]) == ("192.0.2.65", "192.0.2.126")
    assert d["usable_hosts"] == 62


def test_edge_prefixes():
    assert sc.Subnet.from_cidr("192.0.2.0/31").usable_hosts == 2   # RFC 3021
    assert sc.Subnet.from_cidr("192.0.2.9/32").usable_hosts == 1   # host route


@pytest.mark.parametrize("bad", ["192.0.2.0", "192.0.2.256/24", "192.0.2/24",
                                 "192.0.2.0/33", "a.b.c.d/8", "192.0.2.0/x"])
def test_invalid_input_rejected(bad):
    with pytest.raises(ValueError):
        sc.Subnet.from_cidr(bad)


def test_contains():
    s = sc.Subnet.from_cidr("192.0.2.64/26")
    assert s.contains("192.0.2.100")
    assert not s.contains("192.0.2.130")


# ---------- YOUR TASKS: these fail until you implement them ----------
@pytest.mark.xfail(raises=NotImplementedError, reason="student TODO", strict=False)
@pytest.mark.parametrize("hosts,prefix", [
    (2, 30), (30, 27), (62, 26), (63, 25), (254, 24), (255, 23),
])
def test_required_prefix(hosts, prefix):
    assert sc.required_prefix(hosts) == prefix


@pytest.mark.xfail(raises=NotImplementedError, reason="student TODO", strict=False)
def test_required_prefix_rejects_bad_input():
    with pytest.raises(ValueError):
        sc.required_prefix(0)


@pytest.mark.xfail(raises=NotImplementedError, reason="student TODO", strict=False)
def test_same_subnet():
    assert sc.same_subnet("192.0.2.65", "192.0.2.126", 26)
    assert not sc.same_subnet("192.0.2.126", "192.0.2.130", 26)


@pytest.mark.xfail(raises=NotImplementedError, reason="student TODO", strict=False)
def test_vlsm_plan_example():
    plan = sc.vlsm_plan("192.0.2.0/24", {"A": 50, "B": 20, "C": 2})
    assert plan == [("A", "192.0.2.0/26"), ("B", "192.0.2.64/27"),
                    ("C", "192.0.2.96/30")]


@pytest.mark.xfail(raises=NotImplementedError, reason="student TODO", strict=False)
def test_vlsm_plan_no_overlap_and_fits():
    plan = sc.vlsm_plan("198.51.100.0/24", {"Sales": 100, "Eng": 60, "Mgmt": 10, "WAN": 2})
    nets = [ipaddress.ip_network(c) for _, c in plan]
    parent = ipaddress.ip_network("198.51.100.0/24")
    assert all(n.subnet_of(parent) for n in nets)
    for i, a in enumerate(nets):
        for b in nets[i + 1:]:
            assert not a.overlaps(b)


@pytest.mark.xfail(raises=NotImplementedError, reason="student TODO", strict=False)
def test_vlsm_plan_raises_when_too_big():
    with pytest.raises(ValueError):
        sc.vlsm_plan("192.0.2.0/26", {"A": 50, "B": 50})
