# subnet_calc: Modular IPv4 Subnet Calculator

Learning-oriented calculator. Core bit math is implemented manually and verified against Python's `ipaddress` module; three functions are left for you.

## Run
```bash
python subnet_calc.py 192.0.2.77/26
pip install pytest && pytest -q
```

## Your tasks
1. `required_prefix()`: size a subnet for N hosts
2. `same_subnet()`: AND-with-mask comparison
3. `vlsm_plan()`: largest-first VLSM allocation

Stretch goals: `summarize()` (route aggregation), IPv6 support, a `--split N` option, a table output mode that prints binary alongside decimal.

## Documentation to write when finished
- Why the network and broadcast addresses are reserved
- Why VLSM allocates largest-first
- A worked VLSM design with a diagram for a small office (redact to RFC 5737 ranges)
