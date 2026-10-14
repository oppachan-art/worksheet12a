import sys
from collections import Counter

if len(sys.argv) != 2:
    print("Usage: python3 count_logs.py <logfile>")
    sys.exit(1)

with open(sys.argv[1], encoding="utf-8", errors="replace") as f:
    lines = f.readlines()

print("Total lines:", len(lines))

counts = Counter()
for line in lines:
    for word in ("error", "failed", "timeout"):
        if word in line.lower():
            counts[word] += 1

for word, count in counts.items():
    print(f"{word}: {count}")
