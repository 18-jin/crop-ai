from cropharvest.datasets import CropHarvest

DATA_DIR = "../../data"

print("Loading benchmark datasets (no download)...")
datasets = CropHarvest.create_benchmark_datasets(
    DATA_DIR,
    download=False
)

print("Number of benchmark datasets:", len(datasets))

for i, ds in enumerate(datasets):
    print(f"{i}: {ds.task}")

