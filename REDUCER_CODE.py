#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────
# REDUCER_CODE.py
# Project  : Narcotics Data Analysis using Hadoop MapReduce
# Author   : Abhishek Ray (1240258024)
# University: Babu Banarasi Das University
# ─────────────────────────────────────────────────────────
#
# INPUT  (sorted key-value pairs from Mapper):
#   Drug_Type / State  \t  Cases
#
# REDUCER LOGIC:
#   Aggregate total cases for each unique key
#   (Hadoop sorts Mapper output by key before Reducer)
#
# OUTPUT:
#   Drug_Type / State  \t  Total_Cases
# ─────────────────────────────────────────────────────────

import sys

current_key   = None
current_total = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        key, value = line.split("\t", 1)
        value = int(value)
    except ValueError:
        continue

    if current_key == key:
        # Same key — keep accumulating
        current_total += value
    else:
        # New key — output previous key's total
        if current_key is not None:
            print(f"{current_key}\t{current_total}")
        current_key   = key
        current_total = value

# Output the final key
if current_key is not None:
    print(f"{current_key}\t{current_total}")
