#!/usr/bin/env python3
import sys

current_ip = None
current_count = 0

for line in sys.stdin:
    ip, count = line.strip().split("\t")
    count = int(count)

    if current_ip == ip:
        current_count += count
    else:
        if current_ip:
            print(f"{current_ip}\t{current_count}")

        current_ip = ip
        current_count = count

if current_ip:
    print(f"{current_ip}\t{current_count}")
