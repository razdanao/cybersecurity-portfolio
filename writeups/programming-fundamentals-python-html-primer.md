# Programming Fundamentals for Cybersecurity: A Python and HTML Primer

## Platform
Study guide built from my coursework — Toronto School of Management, Cybersecurity Specialist Co-op (Module: Programming Languages for Cybersecurity). Every code example below was run, and the outputs shown are the real ones.

## Goal
To consolidate the programming theory that security work rests on. Security professionals read and write scripts to automate tasks, parse logs, probe networks, and understand how web pages are built, and they can't do any of it without the basics. This guide covers Python, a little network programming, and HTML, with a note on why each matters for security.

---

## Part 1: Python Fundamentals

### 1.1 How Python reads code: syntax, semantics, and errors
Python is an **interpreted** language: the interpreter reads your code, checks its syntax, and then runs it. **Syntax** is the set of grammar rules (where quotes, colons, and brackets go). **Semantics** is what the code actually means and does. Code can be grammatically perfect and still do the wrong thing.

| Error type | Cause | Example |
|---|---|---|
| **SyntaxError** | Breaks the grammar, caught before the code runs | `print('it's')` |
| **NameError** | Uses a name that doesn't exist | `print(Question2)` |
| **TypeError** | An operation on the wrong type | `"3" + 3` |
| **ZeroDivisionError** | Divides by zero | `5 / 0` |
| **Logic error** | Runs without crashing but gives the wrong answer | Using `>` where `>=` was needed |

Logic errors are the dangerous kind: nothing crashes, so nothing warns you.

### 1.2 Variables and identifiers
A **variable** is a name bound to a value. The rules for **identifiers** (names):
- May contain letters, digits, and underscores
- **Cannot start with a digit** (`2cool = 1` is a SyntaxError)
- **Cannot contain spaces** (`my var = 5` is a SyntaxError)
- **Cannot be a reserved keyword** such as `class`, `for`, `if`, or `def`
- **Are case-sensitive**: `Question` and `question` are two different variables

```python
Question = "What program are you enrolled in?"
question = "What is your name?"
print(question)          # What is your name?  (the lowercase one)
```

Python runs top to bottom, and each assignment uses the *current* values. Tracing that by hand is a core skill:

```python
x = 6
y = x + 3        # y = 9
x = x - 1        # x = 5
z = 20
x = x + z * y    # 5 + 20*9 = 185
print("x: {}, y: {}, z: {}".format(x, y, z))   # x: 185, y: 9, z: 20
```

### 1.3 Data types
Every value has a **type**, and `type()` reveals it.

| Type | Example | Notes |
|---|---|---|
| `int` | `20` | Whole numbers |
| `float` | `20.0` | Decimals |
| `str` | `"20"` | Text, in single or double quotes |
| `bool` | `True` | Only two values |
| `list`, `tuple`, `dict` | `[1]`, `(1,)`, `{"a": 1}` | Collections |

**Strings vs. numbers** is a classic trap. The same `+` does different things:
```python
print('2' + '3')   # 23    (strings are joined: concatenation)
print(2 + 3)       # 5     (numbers are added)
print('2' * 3)     # 222   (a string repeated)
```
Mixing the two (`"3" + 3`) raises a TypeError. Python won't guess what you meant.

**Quotes:** a string can't contain its own delimiter unescaped. Use the other quote style (`'She said "hi"'`) or a backslash (`'It\'s fine'`).

### 1.4 Operators
| Operator | Meaning | Example |
|---|---|---|
| `+ - *` | Add, subtract, multiply | `6 * 7` = `42` |
| `/` | True division (always a float) | `17 / 4` = `4.25` |
| `//` | **Floor division** (drops the fraction) | `17 // 4` = `4`, `21 // 2` = `10` |
| `%` | **Modulo** (the remainder) | `17 % 4` = `1` |
| `**` | Exponent | `2 ** 3` = `8` |

Python **follows the standard order of operations**: `10 - 2 * 3 ** 2` is `-8`, while `(10 - 2) * 3` is `24`. Modulo is useful far beyond maths: checking even or odd, wrapping around a list, and cycling through values.

**Booleans** are expressions that evaluate to `True` or `False`. Comparisons (`==`, `!=`, `<`, `>=`) produce them, and `and`, `or`, `not` combine them. Python treats `True` as `1` and `False` as `0`, so `True + True` is `2`.

### 1.5 Comments
`#` starts a comment. Python ignores everything after it on that line. Good comments explain *why*, not *what*.

### 1.6 Loops
A `for` loop repeats code over a sequence. `range(n)` produces the numbers `0` to `n-1`, not `1` to `n`, a frequent source of **off-by-one errors**.

```python
for i in range(10):
    print(i)           # prints 0 through 9
```
`range(2, 5)` gives `2, 3, 4`. The end is excluded.

### 1.7 Functions
A **function** is reusable code with a name. `def` *defines* it; the function does nothing until you *call* it.

```python
def func():
    print('Yes')

print('No')            # only "No" appears: func() was defined but never called
```

`return` hands a value back to the caller; `print` just displays text. They aren't interchangeable.

```python
def f(x):
    return x - 5

print(f(7) * f(2))     # 2 * -3 = -6
```

### 1.8 Libraries and pip
A **library** is code someone else wrote that you `import`. **pip** is Python's package installer, and the command to install a library is:

```
pip install requests
```
Don't confuse that with `get-pip.py`, which is a script that installs *pip itself*. In practice, install into a **virtual environment** so projects don't conflict.

### 1.9 Pitfalls, including ones I hit
- **Curly quotes and long dashes.** Code pasted from documents or web pages often swaps straight quotes for "smart" ones and `-` for `–`. They look right and Python rejects them:
  ```
  SyntaxError: invalid character '‘' (U+2018)
  SyntaxError: invalid character '–' (U+2013)
  ```
  Always paste into a code editor, not a word processor, and read the exact character in the error message.
- **Nested quotes** (`print("I said "hi" there")`) end the string early.
- **Case mismatches** cause NameErrors that look like typos.
- **Confusing `/` with `//`** silently changes results.

---

## Part 2: Network Programming with Sockets

A **socket** is one endpoint of a network connection. **TCP** sockets set up a connection first (the handshake); **UDP** just sends datagrams.

### Ports
A port number identifies a service on a host. The three ranges:

| Range | Name | Examples |
|---|---|---|
| 0 to 1023 | **Well-known** | 22 SSH, 25 SMTP, 53 DNS, 80 HTTP, 123 NTP, 443 HTTPS |
| 1024 to 49151 | **Registered** | Applications and databases |
| 49152 to 65535 | **Dynamic / private** | Temporary client-side ports |

### Testing a port with `connect_ex`
`connect()` raises an exception on failure. `connect_ex()` returns an **error code instead**: `0` means the connection succeeded, and any non-zero number means it failed (the exact number depends on the operating system). That makes it convenient for a simple port check:

```python
import socket

def is_port_open(host: str, port: int, timeout: float = 1.0) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        return s.connect_ex((host, port)) == 0   # 0 = success
```
I tested it against my own machine only: a port with a listener returned `True`, and an unused port returned `False` (the raw code was 111, "connection refused," on Linux).

**Ethics and legality:** only check hosts you own or have written permission to test. Port scanning without authorization can be illegal, and it's noisy: it shows up in logs and triggers alerts. This is the same principle as my Wireshark exercise: a legal tool becomes a problem when used without authorization.

---

## Part 3: HTML Fundamentals

HTML (**HyperText Markup Language**) describes the *structure* of a web page. It isn't a programming language, because it has no logic of its own, but it follows strict rules.

### Building blocks
- **Element:** an opening tag, content, and a closing tag: `<p>Hello</p>`
- **Attribute:** extra information inside the opening tag: `<a href="https://example.com">`
- **Nesting:** tags can contain other tags, but they must close in the reverse order they opened
- **Anchor tag `<a>`:** creates links; the `href` attribute holds the destination
- **Headings:** six levels, `<h1>` (most important) through `<h6>`

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Example</title>
  </head>
  <body>
    <h1>Welcome</h1>
    <p>Read the <a href="https://example.com">full guide</a> here.</p>
    <ul>
      <li>Python</li>
      <li>HTML</li>
    </ul>
  </body>
</html>
```
The **document structure** is `html` containing a `head` (metadata, title) and a `body` (visible content). A browser tolerates mistakes, but valid, properly nested HTML behaves predictably.

### Why HTML matters for security
If a website inserts user-supplied text into a page without **escaping** it, an attacker can supply tags or script instead of text, and the browser will run it. That's **cross-site scripting (XSS)**, one of the most common web vulnerabilities. Understanding that tags are just text the browser interprets is what makes the vulnerability make sense. It's also why my web-scraping exercise worked: scraping is just reading HTML structure programmatically.

---

## Practice Questions
Predict the output before checking the answers.

1. `print(25 % 7)`
2. `print(25 // 7)`
3. `print("5" * 3)`
4. `a = 3` then `A = 4` then `print(a + A)`
5. `for i in range(2, 5): print(i)`
6. `def add(a, b): return a + b`, then `print(add(2, 3) * 2)`
7. `print(type(3 / 1))`
8. `print(2 ** 3 ** 2)`
9. What's wrong with `print('it's')`?
10. Which of `my var`, `2cool`, `class`, `total_1` is a valid variable name?

**Answers:** 1) `4`  2) `3`  3) `555`  4) `7` (case-sensitive, two different variables)  5) `2`, `3`, `4`  6) `10`  7) `<class 'float'>` (`/` always returns a float)  8) `512` (exponents group right to left)  9) The apostrophe ends the string early, causing a SyntaxError  10) Only `total_1`

---

## Keyword Glossary
`Python` · `interpreter` · `syntax` · `semantics` · `runtime error` · `logic error` · `variable` · `identifier` · `case-sensitive` · `reserved keyword` · `data type` · `string concatenation` · `operator` · `modulo` · `floor division` · `order of operations` · `Boolean` · `for loop` · `range()` · `off-by-one` · `function` · `return value` · `library` · `pip` · `virtual environment` · `socket` · `TCP` · `UDP` · `port` · `well-known ports` · `connect_ex` · `HTML` · `tag` · `element` · `attribute` · `nesting` · `anchor tag` · `input validation` · `escaping` · `cross-site scripting (XSS)`

## Key Takeaways
- **Programming is precision.** A single invisible character, like a curly quote, can stop a script, and the error message usually tells you exactly where.
- **Know the difference between "it ran" and "it's right."** Logic errors don't announce themselves; tracing code by hand and testing edge cases is how they're found.
- **These basics are the foundation of security tooling.** Port checkers, log parsers, scrapers, and exploit code are all variables, operators, loops, functions, and libraries combined, and web vulnerabilities come from how HTML and untrusted input interact.
