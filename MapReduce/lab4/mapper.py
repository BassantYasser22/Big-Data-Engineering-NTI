#!/usr/bin/env python3
import sys

for line in sys.stdin:
    parts = line.strip().split("***")

    if len(parts) != 4:
        continue

    location = parts[1]
    value = parts[3]

    print(f"{location}\t{value}")
