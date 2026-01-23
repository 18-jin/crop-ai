import numpy as np
import matplotlib.pyplot as plt
from cropharvest.datasets import CropHarvest
from cropharvest.bands import BANDS

DATA_DIR = "../../data"

# 1️⃣ Load dataset
datasets = CropHarvest.create_benchmark_datasets(DATA_DIR, download=False)
togo = datasets[-1]

X, y = togo.as_array(flatten_x=False)  # (N, 12, 18)

print("X shape:", X.shape)
print("y shape:", y.shape)

# 2️⃣ Split crop / non-crop
X_crop = X[y == 1]
X_non = X[y == 0]

print("Crop samples:", X_crop.shape[0])
print("Non-crop samples:", X_non.shape[0])

# 3️⃣ Mean over samples
mean_crop = X_crop.mean(axis=0)      # (12, 18)
mean_non = X_non.mean(axis=0)         # (12, 18)

# 4️⃣ Plot helper
def plot_heatmap(data, title, filename, vmin, vmax):
    plt.figure(figsize=(14, 6))
    im = plt.imshow(data.T, aspect="auto", cmap="viridis", vmin=vmin, vmax=vmax)

    plt.yticks(range(len(BANDS)), BANDS)
    plt.xticks(range(12), [f"M{i+1}" for i in range(12)])
    plt.xlabel("Month")
    plt.ylabel("EO Feature")
    plt.title(title)

    plt.colorbar(im)
    plt.tight_layout()
    plt.savefig(filename, dpi=150)
    plt.close()
    print(f"Saved: {filename}")

# 5️⃣ Use same color scale (important!)
vmin = min(mean_crop.min(), mean_non.min())
vmax = max(mean_crop.max(), mean_non.max())

plot_heatmap(
    mean_crop,
    "Togo Crop: Feature × Time Mean Response",
    "feature_time_heatmap_togo_crop.png",
    vmin,
    vmax,
)

plot_heatmap(
    mean_non,
    "Togo Non-Crop: Feature × Time Mean Response",
    "feature_time_heatmap_togo_non_crop.png",
    vmin,
    vmax,
)

