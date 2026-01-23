import numpy as np
import matplotlib.pyplot as plt
from cropharvest.datasets import CropHarvest
from cropharvest.bands import BANDS

DATA_DIR = "../../data"

# 1️⃣ 加载数据
datasets = CropHarvest.create_benchmark_datasets(DATA_DIR, download=False)
togo = datasets[-1]

X, y = togo.as_array(flatten_x=False)
print("X shape:", X.shape)
print("y shape:", y.shape)

# 2️⃣ 找 NDVI 索引
ndvi_index = BANDS.index("NDVI")
print("NDVI index:", ndvi_index)

# 3️⃣ 取 NDVI 序列
ndvi = X[:, :, ndvi_index]          # (N, 12)

# 4️⃣ 计算 ΔNDVI
delta_ndvi = ndvi[:, 1:] - ndvi[:, :-1]   # (N, 11)

# 5️⃣ Crop / Non-Crop 均值
crop_delta_mean = delta_ndvi[y == 1].mean(axis=0)
non_crop_delta_mean = delta_ndvi[y == 0].mean(axis=0)

months = np.arange(2, 13)  # ΔNDVI 从 M2-M12

# 6️⃣ 画折线图（不依赖颜色）
plt.figure(figsize=(10, 5))
plt.plot(months, crop_delta_mean, marker="o", label="Crop ΔNDVI")
plt.plot(months, non_crop_delta_mean, marker="s", label="Non-Crop ΔNDVI")
plt.axhline(0, color="gray", linestyle="--", linewidth=1)

plt.xlabel("Month")
plt.ylabel("ΔNDVI (Month-to-Month Change)")
plt.title("Togo NDVI Change Rate (ΔNDVI)")
plt.legend()
plt.grid(True)

# 7️⃣ 保存
out_path = "delta_ndvi_togo_crop_vs_non_crop.png"
plt.tight_layout()
plt.savefig(out_path, dpi=150)
plt.close()

print(f"Saved: {out_path}")

