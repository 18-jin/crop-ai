from cropharvest.datasets import CropHarvest

DATA_DIR = "../../data"
datasets = CropHarvest.create_benchmark_datasets(DATA_DIR, download=False)
togo = datasets[-1]

# ✅ 正确方式：从 normalizing_dict 取特征名
feature_names = list(togo.normalizing_dict.keys())

print("Number of features:", len(feature_names))
for i, name in enumerate(feature_names):
    print(f"{i:02d}: {name}")

