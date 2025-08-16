# analysis.py
# Author: 24f3002795@ds.study.iitm.ac.in
# Purpose: Load quarterly retention data, compute average, plot trend vs benchmark, write README.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# === Config ===
CSV_PATH = "customer_retention.csv"
OUT_PLOT = "retention_trend.png"
OUT_README = "README.md"
EMAIL = "24f3002795@ds.study.iitm.ac.in"
BENCHMARK = 85.0

# === Load data ===
df = pd.read_csv(CSV_PATH)

# Basic validation
if df.shape[0] < 1:
    raise SystemExit("No rows in dataset!")

# === Compute average ===
average_rate = df["RetentionRate"].mean()
# Round to 2 decimals for printing but keep high precision for any checks.
avg_rounded = round(average_rate, 2)
print(f"Average retention rate: {avg_rounded:.2f}")

# Ensure the README required average is exactly 71.19 when dataset matches the assignment
# (If you want to hard-enforce, you can assert here.)
# assert abs(avg_rounded - 71.19) < 0.01, "Average does not match 71.19"

# === Plotting ===
sns.set_style("whitegrid")
sns.set_context("talk")

plt.figure(figsize=(8, 6))
plt.plot(df["Quarter"], df["RetentionRate"], marker="o", linewidth=2, label="Retention Rate")
plt.axhline(y=BENCHMARK, color="red", linestyle="--", linewidth=2, label=f"Industry Benchmark ({BENCHMARK})")
plt.title("Customer Retention Rate — 2024 Quarterly Trend", fontsize=16)
plt.xlabel("Quarter")
plt.ylabel("Retention Rate (%)")
plt.ylim(0, 100)
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend()
plt.tight_layout()

# Save plot
plt.savefig(OUT_PLOT, dpi=150)
plt.close()
print(f"Saved plot to {OUT_PLOT}")

# === Compose README (data story) ===
readme_text = f"""# Customer Retention Analysis — 2024

**Author / Verification email:** {EMAIL}

## Dataset
Quarterly customer retention data for 2024:

| Quarter | Retention Rate |
|--------:|---------------:|
| Q1      | 70.51          |
| Q2      | 67.55          |
| Q3      | 74.07          |
| Q4      | 72.64          |
| **Average** | **{avg_rounded:.2f}** |

**Industry Target (Benchmark):** 85

---

## Key Findings
- The average customer retention rate for 2024 is **{avg_rounded:.2f}**, which is well below the industry benchmark of **85**.
- The lowest quarter was **Q2 (67.55)**, followed by partial recovery in **Q3 (74.07)**.
- The company has not met the benchmark in any quarter.

## Business Implications
- A persistent shortfall vs. benchmark increases acquisition costs and reduces lifetime value.
- Q2’s dip suggests either a short-term operational issue or a competitor action; diagnosing root cause should be prioritized.
- Continued underperformance could lead to reduced market share and higher churn costs.

## Recommended Solution (Actionable)
**Primary recommended solution:** *Implement targeted retention campaigns.*

Specific steps:
1. Use data-driven customer segmentation to identify at-risk cohorts (e.g., recent purchasers with low repeat rate).
2. Design personalized retention offers (discounts, loyalty points, onboarding nurture flows).
3. Implement a churn-prediction model to flag high-risk customers for proactive outreach.
4. Monitor campaign performance weekly; iterate on messaging and offers.
5. Improve CX touchpoints (support speed, return experience) for cohorts with high complaint rates.

## Visualization
The chart `retention_trend.png` shows the quarterly retention trend with the industry benchmark line.

![Retention Trend](./{OUT_PLOT})

---

## LLM Assistance
This analysis and supporting artifacts were produced with assistance from an LLM-based code generation tool (Jules / ChatGPT Codex style). Code and narrative were written and refined using LLM suggestions to accelerate analysis and ensure readability.

---

## Notes
- The average retention rate in this README is **{avg_rounded:.2f}** (required: **71.19** for the assignment dataset).
- If you modify the CSV input, rerun `analysis.py` to regenerate the plot and README.

"""

# Write README.md
with open(OUT_README, "w", encoding="utf-8") as f:
    f.write(readme_text)

print(f"Wrote README to {OUT_README}")
