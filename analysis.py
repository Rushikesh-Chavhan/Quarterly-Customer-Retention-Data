import pandas as pd
import matplotlib.pyplot as plt

# Your email for verification
email = "24f3002795@ds.study.iitm.ac.in"

# Load dataset
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Retention Rate": [70.51, 67.55, 74.07, 72.64]
}
df = pd.DataFrame(data)

# Calculate average retention rate
average_rate = df["Retention Rate"].mean()
print(f"Average retention rate: {average_rate:.2f}")

# Benchmark
benchmark = 85

# Plot
plt.figure(figsize=(8,6))
plt.plot(df["Quarter"], df["Retention Rate"], marker="o", label="Retention Rate", linewidth=2)
plt.axhline(y=benchmark, color="red", linestyle="--", label="Industry Benchmark (85)")
plt.title("Customer Retention Rate - 2024")
plt.xlabel("Quarter")
plt.ylabel("Retention Rate (%)")
plt.legend()
plt.grid(True)

# Save plot
plt.savefig("retention_trend.png", dpi=100)
plt.show()
