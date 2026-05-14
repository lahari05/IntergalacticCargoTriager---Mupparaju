'''
Task 1: Intergalactic Cargo Manifest Parser
- Parses manifest.txt into a clean JSON array
- Business Rule 1: Sector-7 destinations → weight × 1.45
- Business Rule 2: Round weight; if prime → discard record
'''

import json
import math
import sys


def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def parse_manifest(filepath: str) -> list:
    records = []

    with open(filepath, "r") as f:
        lines = [line.strip() for line in f if line.strip()]

    for line in lines:
        # Format: [DATE] || CARGO_ID :: WEIGHT >> DESTINATION
        date_part, rest = line.split(" || ")
        date = date_part.strip("[]")
        id_weight, destination = rest.split(" >> ")
        cargo_id, weight_str = id_weight.split(" :: ")

        cargo_id = cargo_id.strip()
        destination = destination.strip()
        weight = float(weight_str.strip())

        # Business Rule 1: Sector-7 multiplier
        if "Sector-7" in destination:
            weight *= 1.45

        # Business Rule 2: Round then check prime
        weight_rounded = round(weight)

        if is_prime(weight_rounded):
            print(
                f"[DISCARDED - Prime] {cargo_id} | {destination} | {weight_rounded} kg",
                file=sys.stderr,
            )
            continue

        records.append(
            {
                "cargo_id": cargo_id,
                "date": date,
                "destination": destination,
                "weight_kg": weight_rounded,
            }
        )

    return records


if __name__ == "__main__":
    filepath = sys.argv[1] if len(sys.argv) > 1 else "manifest.txt"
    data = parse_manifest(filepath)

    output_file = "Task 1 - Parser.json"
    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Parsed {len(data)} valid records → {output_file}")
    print(json.dumps(data, indent=2))
