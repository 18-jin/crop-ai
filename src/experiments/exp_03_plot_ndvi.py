import numpy as np
import matplotlib
matplotlib.use("Agg")  # ⭐ 强制无 GUI 后端
import matplotlib.pyplot as plt

from cropharvest.datasets import CropHarvest
from cropharvest.bands import BANDS

print("Loading dataset...")

DATA_DIR = "../../data"
datasets = CropHarvest.create_benchmark_datasets(DATA_DIR, download=False)
togo = datasets[-1]

X, y = togo.as_array(flatten_x=False)

print("X shape:", X.shape)
print("y shape:", y.shape)

ndvi_idx = BANDS.index("NDVI")
X_ndvi = X[:, :, ndvi_idx]

crop_ndvi = X_ndvi[y == 1]
noncrop_ndvi = X_ndvi[y == 0]

months = np.arange(1, 13)

plt.figure(figsize=(8, 5))
plt.plot(months, crop_ndvi.mean(axis=0), label="Crop")
plt.plot(months, noncrop_ndvi.mean(axis=0), label="Non-crop")

plt.xlabel("Month")
plt.ylabel("NDVI")
plt.title("Togo NDVI Seasonal Curve")
plt.legend()
plt.grid(True)

output_path = "ndvi_togo.png"
plt.savefig(output_path, dpi=150)
plt.close()

print(f"✅ Saved figure to {output_path}")

