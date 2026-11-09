# Linux Challenges Lab Report

**Student:** Russel Danao  
**Status:** Draft — challenge execution could not be verified because the lab container timed out.

## Scope and status

This report records procedures for three Linux challenges in a temporary practice lab. The lab container did not accept an SSH connection while this draft was being prepared, so results, screenshots, and observations are left blank. Complete the marked fields after running the commands in the lab container.

Run commands only in the temporary lab container and check `pwd` before creating or deleting files. Do not run cleanup commands against `/`, `/tmp`, or other shared system paths. The container is reported to reset daily, so save evidence outside it. This public report intentionally omits passwords, recovered credentials, and encoded credential strings.

## Environment and evidence

| Item | Record |
| --- | --- |
| Student | Russel Danao |
| Username | `student` |
| SSH port | `2233` |
| Container hostname | _Fill in from `hostname`_ |
| OS and version | _Fill in from `/etc/os-release`_ |
| Date completed | _Fill in_ |
| Evidence location | _Add safe screenshots or terminal transcript; redact secrets_ |

Connect using the lab-provided SSH endpoint and port. Keep the password out of this repository, screenshots, shell history, and terminal transcripts. The lab instructions provide a default password; it is not repeated here.

Start in the challenge directory and confirm the location before proceeding:

```bash
cd /linux-challenges
pwd
ls -la
```

Expected working directory: `/linux-challenges`. If it differs, stop and confirm the correct challenge path before using any relative-path file operation.

## Challenge 1 — files, scripts, and sorting

Run these steps from `/linux-challenges` unless the instructor's setup indicates otherwise.

| # | Task | Command / procedure | Observed result |
| --- | --- | --- | --- |
| 1 | Create `file0.txt` | `touch file0.txt` | _Complete after running_ |
| 2 | Create directory `dir` | `mkdir -p dir` | _Complete after running_ |
| 3 | Copy `file0.txt` into `dir` | `cp -- file0.txt dir/` | _Complete after running_ |
| 4 | Go into `dir` and delete its copy | `cd dir && rm -- file0.txt && cd ..` | _Complete after running_ |
| 5 | Move the original into `dir` | `mv -- file0.txt dir/` | _Complete after running_ |
| 6 | Show the file is in `dir` | `ls -l -- dir/file0.txt` | _Complete after running_ |
| 7 | Write `test` into it | `printf '%s\n' test > dir/file0.txt` | _Complete after running_ |
| 8 | Show its contents | `cat -- dir/file0.txt` | _Complete after running_ |
| 9 | Run `for-loop.sh` | `bash ./for-loop.sh` | _Record exact output_ |
| 10 | Show `file1.txt` | `cat -- file1.txt` | _Record relevant output_ |
| 11 | Show only `cybersecurity` | `grep -oF 'cybersecurity' file1.txt` | _Record whether it matched_ |
| 12 | Run `random.sh` and inspect generated `file2.txt` | `bash ./random.sh` then `cat -- file2.txt` | _Record what the script generated_ |
| 13 | Numerically sort and remove duplicate entries in `file2.txt` | `sort -n -u file2.txt -o file2.txt` then `cat -- file2.txt` | _Record sorted, unique output_ |

If a script is not executable, invoking it with `bash ./script-name.sh` avoids changing its permissions. Inspect a provided script with `sed -n '1,200p' ./script-name.sh` if its behavior or generated output needs explanation.

## Challenge 2 — system information, search, compression, and permissions

Record system information before installing anything. Installing `htop` is one of the lab tasks; use the package manager identified by `/etc/os-release` inside the lab container only.

| # | Task | Command / procedure | Observed result |
| --- | --- | --- | --- |
| 1 | Identify installed OS | `cat /etc/os-release` | _Record distribution and version_ |
| 2 | Install `htop` | Debian/Ubuntu: `apt-get update && apt-get install -y htop`; Fedora/RHEL family: `dnf install -y htop`; Alpine: `apk add htop` | _Record package manager and outcome_ |
| 3 | Inspect CPU, memory, and I/O | `lscpu`; `free -h`; `iostat -xz 1 2` (if available), otherwise `cat /proc/diskstats` | _Summarize CPU count, memory, and I/O evidence_ |
| 4 | Record RAM amount | `free -h` | _Record total RAM shown_ |
| 5 | Show current user | `whoami` | _Record output_ |
| 6 | Show hostname | `hostname` | _Record output_ |
| 7 | Show current directory | `pwd` | _Record output_ |
| 8 | Find `find.txt` containing `565656` | `find / -type f -name find.txt -exec grep -lF -- '565656' {} + 2>/dev/null` | _Record the matching path, without unrelated file contents_ |
| 9 | Show only the matching string | `grep -oF -- '565656' /path/to/find.txt` | _Record output_ |
| 10 | Count file lines | `wc -l < /path/to/find.txt` | _Record line count_ |
| 11 | Compress the discovered file | `gzip -k -- /path/to/find.txt` | _Record generated `.gz` path_ |
| 12 | Create `compress-dir` | `mkdir -p compress-dir` | _Complete after running_ |
| 13 | Move compressed file into it | `mv -- /path/to/find.txt.gz compress-dir/` | _Record final path_ |
| 14 | Run `username-password.sh` | `bash ./username-password.sh` | _Do not paste credentials into this public report_ |
| 15 | Show username and password | Run the script as directed; record only that both appeared, not their values | _Redacted in public report_ |
| 16 | Show only username | Extract the username locally according to the script's output format | _Redacted in public report_ |
| 17 | Show only password | Extract the password locally according to the script's output format | _Redacted in public report_ |
| 18 | Base64-encode `username:password` | Locally: `base64 <(printf '%s' 'username:password')`; replace the placeholder only in the terminal | _Do not commit the encoded credential_ |
| 19 | Create directory `store` | `mkdir -p store` | _Complete after running_ |
| 20 | Create `permission.txt` | `touch store/permission.txt` | _Complete after running_ |
| 21 | Set maximally permissive file mode | `chmod 777 store/permission.txt`; verify with `stat -c '%A %a %n' store/permission.txt` | _Record mode; this intentionally grants all users read/write/execute on this challenge file_ |
| 22 | Delete the created `store` directory | From `/linux-challenges`, verify `pwd`, then run `rm -r -- store` | _Confirm only the created directory was removed_ |

For task 8, the search is read-only but may take time. Use the discovered path in place of `/path/to/find.txt` in tasks 9–11. The `-k` option keeps the original file while creating its compressed copy.

## Challenge 3 — hidden files, text processing, and credential handling

The credential exercises are part of the supplied CTF practice. Keep recovered values in the lab environment and redact them from any public commit, screenshot, or terminal transcript.

| # | Task | Command / procedure | Observed result |
| --- | --- | --- | --- |
| 1 | List `/tmp` entries | `ls -la /tmp` | _Record relevant filenames only_ |
| 2 | Inspect filenames containing unusual characters | `ls -lab /tmp` | _Describe the unusual filename without exposing credentials_ |
| 3 | Identify the file containing a username and password | Inspect the suspicious challenge file read-only; use `file -- /tmp/<filename>` and `cat -v -- /tmp/<filename>` after safely quoting its name | _Record filename and format only_ |
| 4 | Display the plaintext locally | Use `cat` on the identified challenge file in the terminal | _Do not include values in this report_ |
| 5 | Create `ctf.txt` in the challenge directory | `cd /linux-challenges && touch ctf.txt` | _Complete after running_ |
| 6.0 | Store the discovered `user:password` pair in `ctf.txt` | `printf '%s\n' 'user:password' > ctf.txt`; substitute real values only locally | _Do not commit this file with real values_ |
| 6.1 | Create directory `CTF` | `mkdir -p CTF` | _Complete after running_ |
| 7 | Move `ctf.txt` into `CTF` | `mv -- ctf.txt CTF/` | _Complete after running_ |
| 8 | Show the stored line locally | `cat -- CTF/ctf.txt` | _Verify locally; redact in public evidence_ |
| 9 | Show only username locally | `cut -d: -f1 CTF/ctf.txt` | _Do not include value_ |
| 10 | Show only password locally | `cut -d: -f2- CTF/ctf.txt` | _Do not include value_ |
| 11 | Write username to `CTF/user.txt` | `cut -d: -f1 CTF/ctf.txt > CTF/user.txt` | _Verify locally; keep file out of public commits_ |
| 12 | Write password to `CTF/password.txt` | `cut -d: -f2- CTF/ctf.txt > CTF/password.txt` | _Verify locally; keep file out of public commits_ |
| 13 | Compress directory `CTF` | `tar -czf CTF.tar.gz CTF` | _Record archive path; ensure it does not contain real credentials before sharing_ |
| 14 | Find `challenge3.txt` | `find / -type f -name challenge3.txt -print 2>/dev/null` | _Record path_ |
| 15 | Go to the file's location | `cd /path/to/containing/directory` | _Record directory_ |
| 16 | Count its lines | `wc -l < /path/to/challenge3.txt` | _Record count_ |
| 17 | Show the specified user and password locally | Read them into shell variables with `read -r -p 'Username: ' challenge_user` and `read -rs -p 'Password: ' challenge_password; printf '\n'`, then run `printf '%s %s\n' "$challenge_user" "$challenge_password"` | _Do not include any credential values in public evidence_ |
| 18 | Base64-encode `user:password` | `base64 <(printf '%s:%s' "$challenge_user" "$challenge_password")` | _Do not commit the encoded credential_ |
| 19 | Save base64 output to `iatek.txt` | `base64 <(printf '%s:%s' "$challenge_user" "$challenge_password") > iatek.txt` | _Keep this credential-bearing file private_ |
| 20 | Decode the saved value locally | `base64 --decode iatek.txt` | _Verify locally; redact output_ |
| 21 | Find the `/tmp` file containing the required phrase | `grep -RIlF -- 'hidden file to make more interesting the learning' /tmp 2>/dev/null` | _Record matching path_ |
| 22 | Show the phrase locally | `grep -aF -- 'hidden file to make more interesting the learning' /tmp/<matching-file>` | _Record that it matched_ |
| 23 | Write only `hard` to `hard.txt` | `printf '%s\n' hard > hard.txt` | _Complete after running_ |
| 24 | Show the file | `cat -- hard.txt` | _Record output_ |
| 25 | Replace `hard` with `HARD` using a command | `sed -i 's/hard/HARD/g' hard.txt` then `cat -- hard.txt` | _Record output_ |
| 26 | Investigate the CTF credential file whose username starts with `la` | Inspect files under `/files/challenge3` read-only; e.g. `find /files/challenge3 -maxdepth 3 -type f -print` and search candidate text files for `la` | _Record method and success only; do not publish recovered credentials_ |

**Note:** Challenge 3 item numbering follows the lab handout, including its `6.0` and `6.1` labels.

## Results and reflection

Fill these in after completing the work. Use your own verified observations and redact passwords, tokens, base64 credential strings, and credential-bearing files.

- **Overall outcome:** _Pending execution in the assigned container._
- **Most challenging part:** _Describe the step that required the most troubleshooting and why._
- **What I learned:** _Summarize what you learned about Linux files, permissions, processes, search, compression, scripts, or text processing._
- **Evidence captured:** _List safe screenshots or command output files; confirm secrets are redacted._

## Publication checklist

- [ ] Replace all pending fields with verified results.
- [ ] Remove or redact usernames/passwords, base64 credential strings, private keys, and credential-bearing files.
- [ ] Check screenshots and terminal transcripts for passwords and secrets.
- [ ] Confirm no temporary challenge files or archives containing secrets are staged for commit.
- [ ] Confirm the report describes only work actually performed.
