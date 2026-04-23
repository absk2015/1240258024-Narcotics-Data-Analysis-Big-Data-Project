#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────
# MAPPER_CODE.py
# Project  : Narcotics Data Analysis using Hadoop MapReduce
# Author   : Abhishek Ray (1240258024)
# University: Babu Banarasi Das University
# ─────────────────────────────────────────────────────────
#
# INPUT FORMAT (CSV):
#   Year, State, Drug_Type, Cases, Quantity_kg, Arrests
#
# MAPPER LOGIC:
#   For each row → emit TWO key-value pairs:
#     1.  Drug_Type  →  Cases
#     2.  State      →  Cases
#
# This lets the Reducer count total cases per Drug Type
# AND total cases per State in a single MapReduce job.
# ─────────────────────────────────────────────────────────

import sys

for line in sys.stdin:
    line = line.strip()

    # Skip header or blank lines
    if not line or line.startswith("Year"):
        continue

    try:
        fields     = line.split(",")
        if len(fields) < 6:
            continue

        year       = fields[0].strip()
        state      = fields[1].strip()
        drug_type  = fields[2].strip()
        cases      = int(fields[3].strip())
        quantity   = float(fields[4].strip())
        arrests    = int(fields[5].strip())

        # Emit: drug_type -> number of cases
        print(f"{drug_type}\t{cases}")

        # Emit: state -> number of cases
        print(f"{state}\t{cases}")

    except (ValueError, IndexError):
        continue
