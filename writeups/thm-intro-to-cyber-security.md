# Offensive Security Intro — TryHackMe

## Platform
TryHackMe — Pre Security Path → Introduction to Cyber Security

## Goal
To understand the mindset behind offensive security — simulating an attacker's approach to find weaknesses before real attackers do — through a hands-on, legal practice environment.

## What I Did
Completed a 4-task room (100%) covering the basics of offensive security thinking:
- **Task 1 — Think Like a Hacker:** Learned the distinction between offensive security (simulating attacks to find weaknesses) and defensive security (protecting against them)
- **Task 2 — Starting the Lab:** Set up and accessed the practice environment
- **Task 3 — Find Hidden Pages:** Used `dirb`, a directory brute-forcing tool, to scan a target site for pages not linked anywhere in its normal navigation. The scan tested thousands of common directory/file names against the server and returned two real, unlisted paths.
- **Task 4 — Attack the Admin Page:** Applied what was learned to interact with a website's admin-facing page in a safe, sandboxed environment

## Key Takeaways
Before this room, I assumed "finding hidden pages" meant guessing manually or already knowing what to look for. Seeing `dirb` scan thousands of possibilities automatically and return real, working paths in seconds made it clear why unlisted-but-unprotected pages are such a common real-world vulnerability — a page doesn't need to be linked anywhere to be discoverable if it's not properly access-controlled. It reframed "hidden" for me: hidden from casual browsing is not the same as actually secured.

## Screenshot
<img width="950" height="667" alt="2" src="https://github.com/user-attachments/assets/c0df0cc8-5aa1-4571-8fe8-ebb2a7e2c01b" />
<img width="961" height="877" alt="1" src="https://github.com/user-attachments/assets/0fb92f10-b668-477a-821c-b8682445ff17" />
