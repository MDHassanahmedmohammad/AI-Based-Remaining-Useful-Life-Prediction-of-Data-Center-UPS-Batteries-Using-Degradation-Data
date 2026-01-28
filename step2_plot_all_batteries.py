from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import traceback

FILES = ["B0005.mat", "B0006.mat", "B0007.mat", "B0018.mat"]
EOL_SOH = 0.70  # 70% of initial capacity

def load_battery(file_name):
    data = loadmat(file_name, squeeze_me=True, struct_as_record=False)
    for key, value in data.items():
        if key.startswith("__"):
            continue
        if hasattr(value, "cycle"):
            return value, key
    raise Exception(f"Battery struct not found in {file_name}")

def get_discharge_capacities(battery):
    caps = []
    for c in np.atleast_1d(battery.cycle):
        if str(c.type).strip().lower() == "discharge":
            cap = c.data.Capacity
            if isinstance(cap, np.ndarray):
                cap = float(cap.flatten()[0])
            else:
                cap = float(cap)
            caps.append(cap)
    return np.array(caps, dtype=float)

def main():
    print("SCRIPT STARTED ✅")
    print("Python exe:", sys.executable)
    print("Working dir:", os.getcwd())
    print("Files visible here:", os.listdir("."))  # shows if .mat files are in the same folder
    print("-" * 50)

    results = []

    plt.figure(figsize=(9, 6))

    for f in FILES:
        print(f"Loading {f} ...")
        if not os.path.exists(f):
            raise FileNotFoundError(f"❌ File not found in this folder: {f}")

        battery, key = load_battery(f)
        caps = get_discharge_capacities(battery)

        cap0 = caps[0]
        thr = EOL_SOH * cap0

        eol = None
        for i, cap in enumerate(caps):
            if cap <= thr:
                eol = i + 1
                break

        results.append((f.replace(".mat", ""), len(caps), cap0, thr, eol))
        plt.plot(range(1, len(caps) + 1), caps, label=f"{f.replace('.mat','')} (EOL={eol})")

        print(f"  ✅ discharge_cycles={len(caps)}, cap0={cap0:.3f}, thr={thr:.3f}, eol={eol}")

    plt.xlabel("Discharge Cycle Number")
    plt.ylabel("Capacity (Ah)")
    plt.title("Capacity Degradation Curves (NASA Battery Dataset)")
    plt.grid(True)
    plt.legend()

    os.makedirs("outputs", exist_ok=True)
    out_path = os.path.join("outputs", "capacity_all_batteries.png")
    plt.savefig(out_path, dpi=200)
    print(f"\n✅ PLOT SAVED: {out_path}")

    print("\n--- Summary ---")
    for bid, n, cap0, thr, eol in results:
        print(f"{bid}: discharge_cycles={n}, initial_cap={cap0:.3f} Ah, "
              f"70%_threshold={thr:.3f} Ah, EOL_cycle={eol}")

    print("\nDONE ✅")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("\n❌ ERROR OCCURRED:")
        print(e)
        traceback.print_exc()
