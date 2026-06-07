"""Generate README figures for algorithms."""

from pathlib import Path
import sys
import time

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent / "figures"
OUT.mkdir(exist_ok=True)
sys.path.insert(0, str(ROOT / "sorting"))
import mergeSort as ms  # noqa: E402
import bubbleSort as bs  # noqa: E402

sizes = [500, 1000, 2000, 4000, 8000]
merge_times, bubble_times = [], []
for n in sizes:
    arr = list(np.random.randint(0, 10000, n))
    t0 = time.perf_counter()
    ms.mergeSort(arr.copy())
    merge_times.append(time.perf_counter() - t0)
    if n <= 4000:
        t0 = time.perf_counter()
        bs.bubble_sort(arr.copy())
        bubble_times.append(time.perf_counter() - t0)
    else:
        bubble_times.append(np.nan)

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(sizes, merge_times, "o-", label="Merge sort O(n log n)", color="#2563eb", lw=2)
bubble_sizes = sizes[:4]
ax.plot(bubble_sizes, bubble_times[:4], "s-", label="Bubble sort O(n²)", color="#ef4444", lw=2)
ax.set_xlabel("Array size")
ax.set_ylabel("Time (seconds)")
ax.set_title("Sorting algorithm complexity — empirical benchmark")
ax.legend()
fig.tight_layout()
fig.savefig(OUT / "sorting_benchmark.png", dpi=150)
plt.close()

print(f"Saved figure to {OUT}")
