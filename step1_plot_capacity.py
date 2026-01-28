from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load the .mat file
# -----------------------------
FILE_NAME = "B0005.mat"

data = loadmat(FILE_NAME, squeeze_me=True, struct_as_record=False)

# -----------------------------
# 2. Find the battery structure
# -----------------------------
battery = None
for key, value in data.items():
    if key.startswith("__"):
        continue
    if hasattr(value, "cycle"):
        battery = value
        print(f"Battery data found under key: {key}")
        break

if battery is None:
    raise Exception("Battery structure not found in the .mat file")

# -----------------------------
# 3. Extract discharge capacities
# -----------------------------
capacities = []
cycle_numbers = []

for cycle in np.atleast_1d(battery.cycle):
    if str(cycle.type).strip().lower() == "discharge":
        cap = cycle.data.Capacity

        # Capacity may be scalar or array
        if isinstance(cap, np.ndarray):
            cap = float(cap.flatten()[0])
        else:
            cap = float(cap)

        capacities.append(cap)
        cycle_numbers.append(len(capacities))

capacities = np.array(capacities)

print("Total discharge cycles:", len(capacities))
print("First 5 capacities:", capacities[:5])
print("Last 5 capacities:", capacities[-5:])

# -----------------------------
# 4. Define failure threshold
# -----------------------------
initial_capacity = capacities[0]
failure_threshold = 0.70 * initial_capacity

# Find End-of-Life (first cycle below threshold)
eol_cycle = None
for i, cap in enumerate(capacities):
    if cap <= failure_threshold:
        eol_cycle = i + 1
        break

# -----------------------------
# 5. Plot capacity degradation
# -----------------------------
plt.figure(figsize=(8, 5))
plt.plot(cycle_numbers, capacities, label="Capacity (Ah)", linewidth=2)
plt.axhline(
    y=failure_threshold,
    color="red",
    linestyle="--",
    label="70% Failure Threshold"
)

if eol_cycle is not None:
    plt.axvline(
        x=eol_cycle,
        color="black",
        linestyle=":",
        label=f"EOL at cycle {eol_cycle}"
    )

plt.xlabel("Discharge Cycle Number")
plt.ylabel("Capacity (Ah)")
plt.title("Battery Capacity Degradation – B0005 (NASA Dataset)")
plt.legend()
plt.grid(True)

plt.show(block=True)
