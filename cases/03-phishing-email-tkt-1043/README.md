# Case 03 — Phishing email triage (TKT-1043)

**Lab / simulated.** User-reported email spoofing Microsoft 365.

| Field | Value |
|-------|-------|
| Ticket | TKT-1043 |
| Finding | True positive phishing — spoofed From, SPF/DMARC fail, malicious href to attacker IP |
| MITRE | Initial Access / Spearphishing Link **T1566.002** |

## Quick story
From claimed `security@microsoft.com`, but Reply-To was `secure-notify.net`, SPF and DMARC failed, and the link text showed Microsoft login while `href` pointed to `http://185.220.101.99/...`.

## Evidence
- `artifacts/TKT-1043_phishing_email.eml`
- `TKT-1043_L1_closeout.txt`
- `investigation.md`
