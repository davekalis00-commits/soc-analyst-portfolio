# TKT-1042 — Investigation Writeup (L1 close-out)

> **Lab / simulated incident.** Practice SIEM export + pcap for portfolio. Not production data.

## Alert summary

| Field | Value |
|-------|-------|
| Ticket | TKT-1042 |
| Time | 2026-09-01 22:14 CT |
| Severity | High |
| Source | SIEM |
| Alert text | Multiple failed logons then a success. User `jsmith`. Source IP `185.220.101.47`. |

## What I checked

1. **Windows Security events** in `failed_logins.txt` (treated as Splunk-style export).
2. Filtered for `EventCode=4625` (failed logon) and `EventCode=4624` (successful logon).
3. Confirmed **Logon Type 3** (network / remote) on the attack events vs **Logon Type 2** (interactive / console) on a later unrelated success.
4. Pivoted on **SrcIP `185.220.101.47`** and account **`jsmith`**.
5. Opened `ftp_bruteforce.pcap` in Wireshark for cleartext FTP `USER`/`PASS` and response codes.

## Counts (from `failed_logins.txt` via `search_ticket.py`)

```
4625 failures: 8
failures by account: {'jsmith': 7, 'labuser01': 1}
failures by src IP: {'185.220.101.47': 8}
4624 successes: 2
```

Breakdown of the two successes:

| Time (CT) | Event | Logon Type | Account | SrcIP | Notes |
|-----------|-------|------------|---------|-------|-------|
| 22:15:36 | 4624 | **3** (network) | jsmith | **185.220.101.47** | Attack success — same IP after the 4625 spray |
| 22:22:00 | 4624 | 2 (interactive) | labuser01 | 10.18.4.22 | Separate internal console logon — not part of the attack |

Timeline of failures: eight 4625s from `185.220.101.47` between 22:14:00 and 22:15:24 (~12s apart), mostly `jsmith` (7) plus one spray hit on `labuser01` (1). Immediate 4624 Type 3 for `jsmith` from that IP at 22:15:36.

## Wireshark — FTP cleartext credential stuffing

Same account story over FTP (cleartext):

- Multiple `USER jsmith` + `PASS …` attempts
- Four `530 Login incorrect` responses (`Winter2020!`, `Password1`, `Company123`, `Summer2024!`)
- Final attempt: `PASS Welcome1` → **`230 User jsmith logged in.`**

This is cleartext credential stuffing against FTP — same pattern as the Windows 4625→4624 sequence (fail spray, then success).

### Screenshots

- [ ] Add Wireshark Follow TCP Stream screenshot here
- [ ] (Optional) Add Wireshark filter view: `ftp` or `ftp.response.code == 530` / `230`

## MITRE ATT&CK

| Field | Value |
|-------|-------|
| Tactic | Credential Access |
| Technique | Brute Force |
| ID | **T1110** |

## Disposition

**True positive.**

Remote brute force from `185.220.101.47` against `jsmith`, followed by a successful network logon (4624 Logon Type 3). FTP pcap independently shows the same account cracking to `Welcome1`. Attacker obtained valid credentials and successfully authenticated.

## Containment / escalate (L1)

1. **Disable account `jsmith` or force password reset** (coordinate with identity / helpdesk per playbook).
2. **Block source IP `185.220.101.47`** at firewall / edge (and check for other hosts hit by this IP).
3. **Escalate to L2** for possible compromise — successful 4624 means session may already exist; ask L2 to check for lateral movement, new local accounts, persistence, and outbound connections from `WIN-JSMITH` after 22:15:36.
4. Document ticket with counts, SrcIP, account, Logon Type, MITRE T1110, and link to pcap evidence.

## Tools used

- Splunk-style log search (`search_ticket.py` against `failed_logins.txt` — EventCode / Account / SrcIP filters)
- Wireshark (`ftp_bruteforce.pcap` — FTP USER/PASS, 530/230, Follow TCP Stream)
- MITRE ATT&CK (Credential Access / Brute Force T1110)

## Reproduce locally

```bash
cd cases/01-windows-bruteforce-tkt-1042/artifacts
python3 search_ticket.py
# Wireshark: open ftp_bruteforce.pcap → filter ftp → Follow TCP Stream
```
