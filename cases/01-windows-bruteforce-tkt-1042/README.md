# Case 01 — Windows + FTP Brute Force (TKT-1042)

| Field | Value |
|-------|-------|
| Ticket | TKT-1042 |
| Severity | High |
| Source | SIEM (simulated) |
| Alert time | 2026-09-01 22:14 CT |
| Disposition | **True positive** |
| MITRE | Credential Access — Brute Force **T1110** |

**Short finding:** Same external IP (`185.220.101.47`) sprayed failed Windows logons (4625, Logon Type 3) against `jsmith`, then a successful 4624 from that IP. Matching cleartext FTP credential stuffing in Wireshark ended in `230` with password `Welcome1`.

**Full writeup:** [investigation.md](investigation.md)

**Artifacts:** [artifacts/](artifacts/) — `failed_logins.txt`, `ftp_bruteforce.pcap`, `search_ticket.py`

> Lab / simulated incident for portfolio. Not production SOC data.
