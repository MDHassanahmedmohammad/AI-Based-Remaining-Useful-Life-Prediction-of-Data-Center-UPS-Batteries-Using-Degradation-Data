import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("outputs/ml_dataset_cycles.csv")

# Use only batteries with RUL available
df = df.dropna(subset=["rul"]).copy()

X = df[["cycle", "capacity_ah", "soh"]]
y = df["rul"]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=300,
    random_state=42
)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# ---------- FIGURE 1: Actual vs Predicted ----------
plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_pred, alpha=0.6)
plt.plot([0, max(y_test)], [0, max(y_test)], "r--")
plt.xlabel("Actual RUL (cycles)")
plt.ylabel("Predicted RUL (cycles)")
plt.title("Actual vs Predicted RUL")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/fig_actual_vs_predicted_rul.png", dpi=300)
plt.close()

# ---------- FIGURE 2: Error Distribution ----------
errors = y_pred - y_test

plt.figure(figsize=(6, 4))
plt.hist(errors, bins=25, edgecolor="black")
plt.xlabel("Prediction Error (cycles)")
plt.ylabel("Frequency")
plt.title("RUL Prediction Error Distribution")
plt.grid(True)
plt.tight_layout()
plt.savefig("outputs/fig_rul_error_distribution.png", dpi=300)
plt.close()

print("✅ Step 5 completed.")
print("Saved:")
print(" - outputs/fig_actual_vs_predicted_rul.png")
print(" - outputs/fig_rul_error_distribution.png")
