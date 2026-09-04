# How to share this portfolio

One-page checklist to get this repo in front of hiring managers.

## 1. Push to GitHub

```bash
cd /workspace/soc-portfolio   # or wherever you cloned/copied this folder
git init
git add .
git commit -m "Add SOC portfolio: TKT-1042 Windows + FTP brute force lab case"
# Create an empty public repo on GitHub named: soc-analyst-portfolio
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/soc-analyst-portfolio.git
git push -u origin main
```

Suggested public repo name: **`soc-analyst-portfolio`**

After the Wireshark screenshot is added under the case writeup, commit again:

```bash
git add cases/01-windows-bruteforce-tkt-1042/
git commit -m "Add Wireshark Follow TCP Stream evidence for TKT-1042"
git push
```

## 2. LinkedIn

**About (one line you can paste):**  
SOC Analyst I candidate (Chicago) — Security+ ce, Splunk Core Certified User. Lab portfolio of L1 triage writeups (Windows 4625/4624 brute force + Wireshark FTP credential stuffing → MITRE T1110).

**Featured:** Add the GitHub repo link (`https://github.com/<YOUR_USERNAME>/soc-analyst-portfolio`) so recruiters open the case writeup in one click.

## 3. Resume — Projects (one sentence)

**SOC Analyst Lab Portfolio** — Investigated simulated SIEM alert TKT-1042: correlated Windows 4625/4624 brute force with Wireshark FTP cleartext credential stuffing, mapped to MITRE T1110, and documented L1 contain/escalate steps (Security+, Splunk Core).

Keep the word **lab / simulated** so it stays honest.
