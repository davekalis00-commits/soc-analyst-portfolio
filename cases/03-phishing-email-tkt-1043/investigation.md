# TKT-1043 — Phishing investigation writeup

> Lab / simulated incident for portfolio. Not production mail.

## Alert summary
User `finance@corp.example.com` reported an urgent "Microsoft 365" mailbox-deletion email (2026-09-03 09:14 CT).

## Header analysis
| Check | Result |
|-------|--------|
| From | `Microsoft 365 Security <security@microsoft.com>` (spoofed brand) |
| Reply-To | `helpdesk-reset@secure-notify.net` (mismatch) |
| SPF | **fail** — sender IP `185.220.101.99` |
| DKIM | none |
| DMARC | **fail** for `header.from=microsoft.com` |

## URL analysis
| What user sees | Real destination (`href`) |
|----------------|---------------------------|
| `https://login.microsoftonline.com/common/oauth2/verify` | `http://185.220.101.99/microsoft-verify/login.html` |

Do not browse the href in a real browser for this lab — read the `.eml` only.

## Disposition
**True positive** phishing / credential harvest attempt.

## MITRE ATT&CK
- Tactic: Initial Access
- Technique: Phishing: Spearphishing Link
- ID: **T1566.002**

## L1 actions
User guidance + credential reset if clicked; block domains/IP/URL; hunt other recipients; escalate if credentials entered.
