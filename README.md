# David Kaliszczak — SOC Analyst Portfolio

Chicago-based SOC Analyst I candidate | Per Scholas Cyber graduate (Aug 2026) | CompTIA Security+ ce | Splunk Core Certified User

**LinkedIn:** [linkedin.com/in/david-kaliszczak](https://linkedin.com/in/david-kaliszczak)

## What this repo is

Lab investigations that show how I triage a ticket as L1: read the alert, pull the relevant Windows events, confirm with packet capture when needed, analyze phishing headers/URLs, map to MITRE ATT&CK, call true/false positive, and write clear contain/escalate next steps.

Tools practiced: Splunk, Wireshark, email header analysis, MITRE ATT&CK.

## Cases

| Case | Ticket | Finding | Link |
|------|--------|---------|------|
| 01 — Windows + FTP brute force | TKT-1042 | True positive — remote brute force then successful logon (Logon Type 3) from `185.220.101.47` against `jsmith` | [case card](cases/01-windows-bruteforce-tkt-1042/README.md) · [full writeup](cases/01-windows-bruteforce-tkt-1042/investigation.md) |
| 02 — Splunk triage (same ticket) | TKT-1042 | True positive confirmed in Splunk with SPL + screenshots | [case](cases/02-splunk-bruteforce-tkt-1042/README.md) · [writeup](cases/02-splunk-bruteforce-tkt-1042/investigation.md) |
| 03 — Phishing email triage | TKT-1043 | True positive — spoofed Microsoft mail, SPF/DMARC fail, href to attacker IP (T1566.002) | [case](cases/03-phishing-email-tkt-1043/README.md) · [writeup](cases/03-phishing-email-tkt-1043/investigation.md) |

## Disclaimer

All cases here are **simulated lab / training incidents** built from practice logs, pcaps, and sample email. They are **not** from employer production systems and do **not** claim real SOC tenure. They demonstrate process, tooling, and written triage for hiring review.
