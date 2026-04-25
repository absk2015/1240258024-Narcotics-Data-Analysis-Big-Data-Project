import sys

for line in sys.stdin:
    line = line.strip()

    # Skip header or blank lines
    if not line or line.startswith("Year"):
        continue

    try:
        fields    = line.split(",")
        if len(fields) < 6:
            continue

        state     = fields[1].strip()
        drug_type = fields[2].strip()
        cases     = int(fields[3].strip())

        # Emit: drug_type -> number of cases
        print(f"{drug_type}\t{cases}")

        # Emit: state -> number of cases
        print(f"{state}\t{cases}")

    except (ValueError, IndexError):
        continue
