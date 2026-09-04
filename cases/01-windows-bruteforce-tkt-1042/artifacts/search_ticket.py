from collections import Counter
from pathlib import Path
p = Path(__file__).with_name("failed_logins.txt")
fails, wins = [], []
for line in p.read_text().splitlines():
    if line.startswith("#") or not line.strip():
        continue
    if "EventCode=4625" in line:
        fails.append(line)
    if "EventCode=4624" in line:
        wins.append(line)
users = Counter()
ips = Counter()
for line in fails:
    for part in line.split():
        if part.startswith("Account="):
            users[part.split("=",1)[1]] += 1
        if part.startswith("SrcIP="):
            ips[part.split("=",1)[1]] += 1
print("TKT-1042 search results (this is the same idea as a Splunk stats count)")
print(f"4625 failures: {len(fails)}")
print("failures by account:", dict(users))
print("failures by src IP:", dict(ips))
print(f"4624 successes: {len(wins)}")
for line in wins:
    print(" ", line)
print()
print("If failures are fast, same IP, then a 4624 from that IP: brute force then success. Escalate.")
