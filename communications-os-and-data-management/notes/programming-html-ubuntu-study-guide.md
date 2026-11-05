# Python HTML and Ubuntu Command Line Study Guide

> **Type:** Study write-up. **Status:** Reference notes adapted from course materials; no lab completion is claimed.

This guide reviews foundational Python, HTML, and Ubuntu command-line concepts from the supplied course files. It paraphrases those materials, corrects common errors, and separates reference knowledge from work that would need to be run and documented independently.

## Python fundamentals

### Names, values, and expressions

Python distinguishes uppercase and lowercase letters in identifiers. `score`, `Score`, and `SCORE` are different names. A name cannot start with a digit. Variables can refer to values such as integers, strings, and Boolean values.

The operators `//` and `%` answer different questions. Integer division returns the whole-number quotient (`21 // 2` is `10`); modulo returns the remainder (`17 % 4` is `1`). Standard arithmetic precedence applies, so multiplication and division are evaluated before addition and subtraction unless parentheses change the order.

Adding strings joins their text: `'2' + '3'` gives `'23'`. This is different from adding the integer values `2 + 3`, which gives `5`. Convert values deliberately when combining text and numbers.

### Conditions, loops, and functions

A `for` loop can repeat an action over a sequence. `range(10)` supplies the integers from 0 through 9; its endpoint is excluded. A function groups reusable behavior. `return` sends a value back to the caller, while `print` displays text. A function can do both, but they are not interchangeable.

Use matching quotation marks around strings. To include a quote inside a string, choose the other quote style or escape the embedded character. Use ordinary keyboard quotes and hyphens in code. Curly quotation marks and typographic dashes copied from rich text can cause syntax errors.

### Errors and packages

Syntax errors prevent code from being parsed. Runtime errors occur while a program runs. A program can also run and still produce the wrong result; that is a logic error. Read the line and character named in the error, then check punctuation, indentation, spelling, and the type of each value.

Python packages are installed with a package installer such as `python -m pip install package-name` in the intended Python environment. A command such as `python get-pip.py` is not the general command for installing an arbitrary library. Prefer a virtual environment for projects so package versions do not unexpectedly affect other work.

## HTML fundamentals

HTML describes the structure and meaning of web content. Elements are written with tags; many elements have an opening tag, content, and a closing tag. Elements can be nested, but they must close in the correct order. Attributes provide additional information, such as a link destination in an anchor element.

A basic page uses a document declaration, an `html` root, a `head` for metadata, and a `body` for visible page content. Headings range from `h1` through `h6`. Choose a heading level by document structure rather than by the visual size you want. Use elements for their meaning, keep nesting valid, and provide useful alternative text for informative images.

## Ubuntu command line reference

| Goal | Common command | Notes |
|---|---|---|
| Show the current directory | `pwd` | Prints the working directory. |
| List files | `ls -la` | Includes hidden entries and details. |
| Move between directories | `cd path` | `cd ..` moves to the parent. |
| Create a directory | `mkdir name` | Add `-p` for nested paths. |
| Copy or rename | `cp source destination`; `mv source destination` | Check paths before overwriting. |
| Read a file | `less file`; `head file`; `tail file` | `less` is paginated; `tail -f` follows updates. |
| Search text | `grep 'pattern' file` | Quote patterns with shell metacharacters. |
| Inspect disk and memory | `df -h`; `free -h` | Human-readable units. |
| Inspect a service | `systemctl status name` | Use `sudo` only when elevated rights are needed. |
| Read service logs | `journalctl -u name` | Add `-f` to follow new entries. |
| Inspect addresses and sockets | `ip addr`; `ss -lntup` | Some process details may require elevated rights. |
| Check UFW status | `sudo ufw status verbose` | Review rules before changing them. |
| Update package metadata | `sudo apt update` | This refreshes indexes; it does not install upgrades. |
| Install a package | `sudo apt install package-name` | Confirm the package source and name. |
| Connect with SSH | `ssh user@host` | Verify the host identity before trusting a first connection. |

The supplied cheat sheet also covers file permissions, users and groups, cron, Snap, LXD, and Ubuntu Pro. Treat placeholders such as `<username>` as values to replace, not literal text. Commands that change users, firewall rules, services, or files can disrupt a system; inspect the target and understand the effect first.

## Networking concepts to remember

Port numbers identify transport-layer services, but a port assignment alone does not prove which application is actually using the traffic. IANA groups ports into System Ports (0–1023), User Ports (1024–49151), and Dynamic/Private Ports (49152–65535). A socket connection check that returns zero indicates success for `connect_ex`; a nonzero result indicates an error code. Test only systems you own or have permission to assess.

## Troubleshooting checklist

### Python and HTML

- **Syntax error near punctuation:** Replace curly quotes and typographic dashes with ordinary code characters; check parentheses, colons, and quotes.
- **Unexpected output:** Check value types, operator precedence, and whether string concatenation or numeric addition is intended.
- **Loop misses the last value:** Remember that `range(stop)` excludes `stop`.
- **Function displays `None`:** Check whether the function prints a value but does not return it.
- **Package import fails:** Confirm the active interpreter and virtual environment, then install the package into that same environment.
- **HTML renders incorrectly:** Check closing tags, nesting order, attribute quotes, and whether visible content is inside `body`.

### Ubuntu

- **“Permission denied”:** Confirm the file owner and permissions. Use elevated rights only when required; do not make broad permission changes to silence an error.
- **Command not found:** Check spelling and whether the package or command is installed. Identify whether the command is provided by the shell, a package, or a service.
- **Service fails to start:** Inspect `systemctl status` and `journalctl -u`; check the service name, configuration, and dependencies.
- **Package installation fails:** Run `sudo apt update`, read the full error, and check network access, repository configuration, and package name.
- **Unexpected network behavior:** Check `ip addr`, routes, DNS settings, firewall rules, and whether the destination is reachable.
- **LXD command does not work:** Confirm LXD is installed and initialized, the user has the needed access, and the instance name and command syntax are correct.

## Source and attribution

Adapted and paraphrased from the supplied *Python and HTML Quiz Review* (four pages) and *ubuntu_cli_cheat_sheet_2025* (three pages). These materials are course study sources, not original work by this guide's author. Port range details are checked against the [IANA Service Name and Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml); the remaining examples are study references, not evidence of a completed lab.
