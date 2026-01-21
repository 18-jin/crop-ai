from cropharvest.datasets import CropHarvest
from sklearn.ensemble import RandomForestClassifier

DATA_DIR = "../../data"

print("Creating benchmark datasets...")
datasets = CropHarvest.create_benchmark_datasets(
    DATA_DIR,
    download=False
)

print("Number of benchmark datasets:", len(datasets))

# 官方 demo：最后一个是 Togo
togo = datasets[-1]

print("Loading Togo dataset as array...")
X, y = togo.as_array(flatten_x=True)

print("X shape:", X.shape)
print("y shape:", y.shape)

print("Training RandomForest...")
model = RandomForestClassifier(
    n_estimators=200,
    random_state=0,
    n_jobs=-1
)
model.fit(X, y)

print("Evaluating on test data...")
test_preds = []
test_instances = []

for _, test_instance in togo.test_data(flatten_x=True):
    probs = model.predict_proba(test_instance.x)[:, 1]
    test_preds.append(probs)
    test_instances.append(test_instance)

metrics = test_instances[0].evaluate_predictions(test_preds[0])

print("Evaluation metrics:")
for k, v in metrics.items():
    print(f"  {k}: {v:.4f}")

print("\nTraining RandomForest on Togo dataset...")
print("Training done.")

