# Python for Cybersecurity Study Guide

## Programming for Cybersecurity

A plain-language guide to the course topics: HTML, Python, automation, and basic network programming. It is a study aid, not a completed assignment or evidence of professional experience.

## Learning map

| Topic | Main idea | Security connection |
|---|---|---|
| HTML | Describes the structure of web pages | Read page structure, links, forms, and embedded content |
| Python fundamentals | Store data, make decisions, repeat work, and define functions | Build small, understandable analysis and automation tools |
| Files and libraries | Read, write, and reuse code | Process evidence carefully and use known dependencies |
| Networking | Connect a host and port using sockets | Understand services and test only approved systems |

## 1. HTML

HTML (HyperText Markup Language) labels the parts of a web page. It is markup: it describes content structure. CSS styles that content; JavaScript adds interactive behavior.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Security Notes</title>
  </head>
  <body>
    <h1>Security Notes</h1>
    <p>HTML describes page content.</p>
    <a href="https://example.com/">Example link</a>
  </body>
</html>
```

An element such as `<p>Text</p>` contains an opening tag, content, and a closing tag. Attributes add details: `href` gives a link destination, `src` gives a media source, `alt` describes an image, and `class` or `id` identifies an element. Some elements, including `img` and `input`, do not have closing tags. Nest elements in the correct order.

Useful elements: headings (`h1`-`h6`), paragraphs (`p`), emphasis (`em`, `strong`), links (`a`), lists (`ul`, `ol`, `li`), images (`img`), forms (`form`, `label`, `input`, `button`), and comments (`<!-- note -->`). Prefer meaningful elements over generic containers (`div`, `span`) when one fits.

**Security connection:** Inspect form destinations, link targets, and embedded content when reviewing a page. HTML does not validate submitted data on the server. Treat page content and links from outside sources as untrusted.

## 2. Python fundamentals

### Values, variables, and operators

Common types are `int` (whole number), `float` (decimal number), `str` (text), and `bool` (`True` or `False`). Assign a value with `=`; compare values with `==`. Names are case-sensitive, cannot contain spaces, cannot start with a number, and cannot be Python keywords. Descriptive `snake_case` names are easy to read.

```python
balance = 200
amount = 35
remaining = balance - amount
has_enough = balance >= amount
```

Arithmetic operators: `+`, `-`, `*`, `/`, `//` (floor division), `%` (remainder), and `**` (power). For example, `5 / 2` is `2.5`, `5 // 2` is `2`, and `5 % 2` is `1`. Use `type(value)` to inspect a value. Write large numbers without comma separators, such as `100000`.

`input()` returns text. Convert it before numeric comparisons: `mark = int(input("Mark: "))`. Validate input so invalid text or out-of-range values do not crash or mislead the program.

### Conditions, loops, and functions

`if`, `elif`, and `else` choose which code block runs. A colon begins the block and indentation defines it. Comparisons include `==`, `!=`, `<`, `<=`, `>`, and `>=`.

A `for` loop visits items. A `while` loop repeats while a condition is true; make sure that condition can become false, or the loop may run forever. Functions group reusable behavior. `def` defines a function, parameters name its inputs, arguments are values passed at a call, and `return` sends a result back.

```python
def grade(mark):
    if not 0 <= mark <= 100:
        raise ValueError("mark must be from 0 to 100")
    if mark >= 90:
        return "excellent"
    if mark >= 75:
        return "good"
    if mark >= 40:
        return "average"
    return "fail"
```

### Data structures

| Type | Example | Useful property |
|---|---|---|
| List | `["a", "b"]` | Ordered and changeable; access items by index |
| Tuple | `("a", "b")` | Ordered and fixed after creation |
| Set | `{"a", "b"}` | Unique items; supports membership checks |
| Dictionary | `{"port": 443}` | Stores values by key |

List indexes start at zero. Lists can be changed with methods such as `append`. Sets are not indexed. Dictionaries are accessed by key, such as `record["port"]`.

## 3. Files, modules, and web data

Use a context manager to close files automatically. Use write mode carefully: `"w"` replaces the existing file contents.

```python
from pathlib import Path

with Path("sample.txt").open(encoding="utf-8") as file:
    text = file.read()
```

For CSV files, use the `csv` module rather than splitting lines yourself. Check paths before reading or overwriting files, and keep credentials and personal data out of notebooks.

A module is reusable Python code; a package groups modules. Third-party packages must be installed in the environment used by the notebook. The course uses `requests`, Beautiful Soup, and `lxml` for web requests and HTML parsing.

```python
import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/", timeout=10)
response.raise_for_status()
soup = BeautifulSoup(response.text, "html.parser")
quotes = [node.get_text(strip=True) for node in soup.select("span.text")]
```

A timeout prevents waiting forever; `raise_for_status()` surfaces HTTP errors. Respect a site's terms and reasonable request rate. Downloaded content is untrusted data; do not execute it. Use `%pip install package_name` in a notebook so installation targets the active kernel.

## 4. Object-oriented programming

A class is a template; an object is an instance. Attributes store object data; methods are functions attached to the class. `__init__` sets up an instance, and `self` refers to that instance. Inheritance extends a base class. Composition builds an object from other objects.

```python
class Service:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def label(self):
        return f"{self.host}:{self.port}"
```

Classes help organize larger programs, but small scripts do not need classes just because Python supports them.

## 5. Networking and sockets

An IP address identifies a network endpoint; a port identifies a service endpoint on that host. A hostname can be resolved to an address. Ports range from 0 to 65535. Common ranges are 0-1023 (system), 1024-49151 (registered), and 49152-65535 (dynamic/private). One course slide shows `46,152`; that is a typo for `49,152`.

| Port | Common service | Reminder |
|---:|---|---|
| 22 | SSH | Secure remote access; restrict and protect credentials |
| 25 | SMTP | Email transfer |
| 53 | DNS | Name resolution |
| 80 | HTTP | Web traffic without TLS |
| 123 | NTP | Clock synchronization |
| 443 | HTTPS | HTTP protected by TLS |

Port-to-service values are conventions, not proof of which service a host runs. An open port alone does not prove a vulnerability.

A socket is a software endpoint for network communication. A TCP client connects to a host and port. `connect_ex()` returns `0` for a successful connection and a nonzero code otherwise. A nonzero result may mean closed, blocked, timed out, or unavailable; it does not always prove the port is closed.

```python
import socket

host = "127.0.0.1"  # this computer only
port = 5000
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.settimeout(1.0)
    result = sock.connect_ex((host, port))
    print("open" if result == 0 else "closed or unavailable")
```

The `with` block closes the socket on success and failure. The class scanner example closes only on one branch, which can leave a successful socket open.

**Authorization rule:** Scan only your own device, an approved lab, or a system for which you have explicit permission. Limit scans to the agreed host, ports, rate, and time. `netstat -a` lists local network connections/listeners; it does not scan the internet.

## 6. Debugging and safe habits

- Syntax errors: code cannot be parsed (for example, missing quotes or a colon).
- Runtime errors: code starts but fails (for example, division by zero or missing files).
- Logic errors: code runs but produces the wrong result (for example, using assignment instead of comparison).
- Read the traceback, check the named line, and isolate the smallest failing example.
- Use least privilege and validate input.
- Keep source data unchanged unless overwriting is deliberate.
- Do not commit secrets or personal information in code and notebooks.
- Use official documentation when old course slides conflict with current behavior.

## Quick review

1. How are `=` and `==` different?
2. What are the results of `/`, `//`, and `%` for `5` and `2`?
3. Which structure is best for unique values or key-value records?
4. Why use a context manager for files and sockets?
5. What do an IP address and port each identify?
6. Why might a nonzero socket result not mean “definitely closed”?
7. What must be authorized before scanning?

## References

- [MDN: Basic HTML syntax](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax)
- [MDN: HTML forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/HTML_forms)
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Python socket documentation](https://docs.python.org/3/library/socket.html) and [Socket Programming HOWTO](https://docs.python.org/3/howto/sockets.html)
- [Python `pathlib`](https://docs.python.org/3/library/pathlib.html), [CSV module](https://docs.python.org/3/library/csv.html), and [error handling](https://docs.python.org/3/tutorial/errors.html)
- [IANA service and port registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)
