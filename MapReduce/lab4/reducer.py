#!/usr/bin/env python3
import sys
import math

current_key = None
values = []

def calculate_stats(vals):
    n = len(vals)
    mean = sum(vals) / n

    variance = sum((x - mean) ** 2 for x in vals) / n
    std = math.sqrt(variance)

    return n, mean, std

for line in sys.stdin:
    key, value = line.strip().split("\t")
    value = float(value)

    if current_key == key:
        values.append(value)
    else:
        if current_key:
            n, mean, std = calculate_stats(values)
            print(f"{current_key}\tCount={n}\tMean={mean:.2f}\tStd={std:.2f}")

        current_key = key
        values = [value]

# last group
if current_key:
    n, mean, std = calculate_stats(values)
    print(f"{current_key}\tCount={n}\tMean={mean:.2f}\tStd={std:.2f}")
