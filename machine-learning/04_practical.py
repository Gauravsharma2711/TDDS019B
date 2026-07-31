import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

data = {
    "Age": [18, 19, 20, 21, 22],
    "Marks": [45, 60, 75, 85, 95],
    "Income": [15000, 25000, 35000, 45000, 55000]
}

df = pd.DataFrame(data)

print("Original Dataset")
print(df)

# Normalization
minmax = MinMaxScaler()
normalized_df = pd.DataFrame(
    minmax.fit_transform(df),
    columns=df.columns
)

print("\nNormalized Dataset")
print(normalized_df)

# Standardization
standard = StandardScaler()
standardized_df = pd.DataFrame(
    standard.fit_transform(df),
    columns=df.columns
)

print("\nStandardized Dataset")
print(standardized_df)

# Comparison
comparison = pd.concat([
    df,
    normalized_df.add_prefix("Norm_"),
    standardized_df.add_prefix("Std_")
], axis=1)

print("\nComparison")
print(comparison)

# Plot
plt.figure(figsize=(8, 5))
plt.plot(df["Marks"], marker='o', label="Original")
plt.plot(normalized_df["Marks"], marker='s', label="Normalized")
plt.plot(standardized_df["Marks"], marker='^', label="Standardized")

plt.title("Original vs Normalized vs Standardized Marks")
plt.xlabel("Student Index")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()