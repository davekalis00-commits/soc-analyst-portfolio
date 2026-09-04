# Case 02 — Splunk triage of TKT-1042

**Lab / simulated.** Same brute-force story as Case 01, investigated in **Splunk** (not just a text export).

| Field | Value |
|-------|-------|
| Ticket | TKT-1042 |
| Tool | Splunk Enterprise (local lab) |
| Sourcetype | `win_security_lab` |
| Finding | True positive — Credential Access / Brute Force **T1110** |

## What I did
1. Ingested the Windows Security practice export into Splunk
2. Searched failed logons (`EventCode=4625`) and summarized by account + source IP
3. Searched successes (`EventCode=4624`) and separated attack vs normal logon
4. Confirmed disposition matches Case 01: public SrcIP spray, then Type 3 success on `jsmith`

## Key SPL

```
sourcetype="win_security_lab" (Account=jsmith OR Account=labuser01) EventCode=4625
| stats count by Account SrcIP
```

```
sourcetype="win_security_lab" (Account=jsmith OR Account=labuser01) EventCode=4624
| stats count by Account SrcIP
```

## Evidence
- `TKT-1042_splunk_4625.png` — Splunk stats for failures
- `artifacts/TKT-1042_SIEM_report.txt` — ingested source log (lab accounts only)

## Disposition
True positive. Escalate after successful auth from attacker IP. See Case 01 close-out for full L1 next steps.
