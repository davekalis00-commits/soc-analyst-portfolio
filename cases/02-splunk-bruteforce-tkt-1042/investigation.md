# TKT-1042 — Splunk investigation writeup (Case 02)

> Lab / simulated. Author: David Kaliszczak. Accounts in the log are lab placeholders (`jsmith`, `labuser01`).

## Goal
Show the same L1 triage as Case 01 using **Splunk search**, with screenshots from a local Splunk instance (Splunk Core Certified User skill).

## Ingest
- File: `TKT-1042_SIEM_report.txt`
- Sourcetype: `win_security_lab`
- Index: `main` (lab)

## Searches run

### Failures (4625)
```
sourcetype="win_security_lab" (Account=jsmith OR Account=labuser01) EventCode=4625
| stats count by Account SrcIP
```
Expected: 8 failures total — mostly `jsmith`, one spray hit on `labuser01`, all from `185.220.101.47`.

### Successes (4624)
```
sourcetype="win_security_lab" (Account=jsmith OR Account=labuser01) EventCode=4624
| stats count by Account SrcIP
```
Expected: attack success `jsmith` from `185.220.101.47`; separate internal success `labuser01` from `10.18.4.22`.

## Screenshots
- [x] `TKT-1042_splunk_4625.png`
- [ ] `TKT-1042_splunk_4624.png` (optional add)

## MITRE
Credential Access — Brute Force — **T1110**

## Disposition / next steps
True positive. Disable/reset `jsmith`, block `185.220.101.47`, escalate to L2 after successful network logon.
