# Python & HTML Fundamentals — Notes

Status: **Final** (conceptual notes, no lab evidence required)

Rewritten as study notes rather than a graded quiz transcript — scores and submission metadata removed. A few answers from the original review were wrong or contradicted by their own script's output; corrected below, with the mistake explained so it's useful as a reference.

## Python basics
- Python identifiers (variable names, function names) are **case-sensitive** — `Question` and `question` are different variables.
- A variable name **cannot start with a digit**.
- `#` starts a comment.
- `17 % 4` → `1` (remainder of integer division).
- `21 // 2` → `10` (floor division, discards the remainder).
- `'2' + '3'` → `'23'` — `+` on two strings concatenates, it doesn't add numbers.
- `for i in range(10): print(i)` → prints `0` through `9`, one per line.
- `a = 20; print(type(a))` → `<class 'int'>`.

## Common beginner syntax traps
These come from pasting code out of Word/Google Docs/PDF rather than typing it directly — worth knowing because they produce confusing errors:
- **Smart/curly quotes** (`‘ ’ “ ”`) instead of straight quotes (`' "`) — Python raises `SyntaxError: invalid character`. Always type quotes in a plain-text editor or IDE, never paste from a word processor.
- **En dash/em dash** (`–`/`—`) swapped in for a minus sign — same failure mode, e.g. `return x – 5` instead of `return x - 5`.
- **Unescaped nested quotes** — `print("I am so "Excited" to be here")` breaks because the string closes at the second `"`. Use a different quote style for the outer string (`'...'`) or escape the inner ones (`\"`).

Worked example, assuming straight quotes and no stray dashes:
```python
def func(x):
    return x - 5

print(func(7) * func(2))   # func(7)=2, func(2)=-3 → 2 * -3 = -6
```

```python
x = 6
y = x + 3      # 9
x = x - 1      # 5
z = 20
x = x + z * y  # 5 + (20*9) = 185
print(f"x: {x}, y: {y}, z: {z}")  # x: 185, y: 9, z: 20
```

- A **semantic error** is code that runs without crashing but produces the wrong result — different from a **syntax error** (code that won't parse at all) and a **runtime error** (crashes mid-execution, e.g. dividing by zero).
- **Boolean expressions** evaluate to `True` or `False`. In Python, `bool` is actually a subclass of `int` — `True` behaves as `1` and `False` as `0` in numeric contexts (`True + True == 2`), even though `type(True)` reports `<class 'bool'>`, not `<class 'int'>`.
- **Installing a third-party library**: `pip install <package>` (or `python -m pip install <package>`). Running `python get-pip.py` installs *pip itself* — it's not how you install a library once pip is already present.

## HTML basics
- HTML tags can be nested inside one another.
- Links use the `<a>` tag (anchor), typically with an `href` attribute: `<a href="https://example.com">text</a>`.
- There are six heading levels: `<h1>` through `<h6>`.

## Python networking basics
- `socket.connect_ex()` returns an **error indicator**, not a boolean — `0` means the connection succeeded; any non-zero value is an errno code for the failure. This is the basis for a basic Python port scanner.
- **Registered ports** (IANA): **1024–49151**. Well-known ports are 0–1023; dynamic/private ports are 49152–65535.
