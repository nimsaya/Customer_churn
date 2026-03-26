"""Generate a synthetic customer churn dataset."""

import random
import csv
import os

random.seed(42)

ROWS = 500
CONTRACTS = ["month-to-month", "one-year", "two-year"]

header = ["tenure", "monthly_charges", "contract_type", "support_calls", "is_active", "churned"]

rows = []
for _ in range(ROWS):
    tenure = random.randint(1, 72)
    monthly_charges = round(random.uniform(20, 120), 2)
    contract_type = random.choice(CONTRACTS)
    support_calls = random.randint(0, 10)
    is_active = random.choice([True, False])

    # Simple churn logic: short tenure + high charges + month-to-month + many calls → churn
    score = 0
    score += (72 - tenure) / 72 * 0.3
    score += monthly_charges / 120 * 0.2
    score += 0.25 if contract_type == "month-to-month" else 0
    score += support_calls / 10 * 0.15
    score += 0.1 if not is_active else 0
    churned = 1 if random.random() < score else 0

    rows.append([tenure, monthly_charges, contract_type, support_calls, is_active, churned])

out_path = os.path.join(os.path.dirname(__file__), "churn.csv")
with open(out_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Wrote {ROWS} rows to {out_path}")
