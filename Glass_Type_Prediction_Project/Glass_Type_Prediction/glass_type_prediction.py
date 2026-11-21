"""
Glass Type Prediction Using Machine Learning
Run: py glass_type_prediction.py
Dependencies: pandas, numpy, matplotlib, scikit-learn, joblib
"""

from pathlib import Path
import warnings
warnings.filterwarnings("ignore")

import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "glass_dataset.csv"
CHART_DIR = BASE_DIR / "Glass_Charts"
CHART_DIR.mkdir(exist_ok=True)

# 1. Load dataset
data = pd.read_csv(DATA_FILE)
print("\\n========== GLASS TYPE PREDICTION ==========")
print("\\nFirst five records:")
print(data.head())
print("\\nDataset shape:", data.shape)
print("\\nMissing values:")
print(data.isnull().sum())

# 2. Separate input features and target
X = data.drop(columns=["Type"])
y = data["Type"].astype(int)

# 3. Dataset distribution chart
counts = y.value_counts().sort_index()
plt.figure(figsize=(8, 5))
plt.bar(counts.index.astype(str), counts.values)
plt.title("Glass Type Distribution")
plt.xlabel("Glass Type")
plt.ylabel("Number of Samples")
plt.tight_layout()
plt.savefig(CHART_DIR / "glass_type_distribution.png", dpi=300)
plt.close()

# 4. Feature distribution charts
for feature in X.columns:
    plt.figure(figsize=(7, 4))
    plt.hist(X[feature].dropna(), bins=20, edgecolor="black")
    plt.title(f"{feature} Distribution")
    plt.xlabel(feature)
    plt.ylabel("Frequency")
    plt.tight_layout()
    filename = {
        "RI": "refractive_index.png",
        "Na": "sodium_distribution.png",
        "Mg": "magnesium_distribution.png",
        "Al": "aluminium_distribution.png",
        "Si": "silicon_distribution.png",
        "K": "potassium_distribution.png",
        "Ca": "calcium_distribution.png",
        "Ba": "barium_distribution.png",
        "Fe": "iron_distribution.png",
    }[feature]
    plt.savefig(CHART_DIR / filename, dpi=300)
    plt.close()

# 5. Chemical composition comparison
means = data.groupby("Type")[list(X.columns)].mean()
ax = means.plot(kind="bar", figsize=(12, 6))
ax.set_title("Average Chemical Composition by Glass Type")
ax.set_xlabel("Glass Type")
ax.set_ylabel("Average Feature Value")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(CHART_DIR / "chemical_composition.png", dpi=300)
plt.close()

# 6. Correlation heatmap (matplotlib only)
corr = data.corr(numeric_only=True)
fig, ax = plt.subplots(figsize=(10, 8))
im = ax.imshow(corr, cmap="coolwarm", aspect="auto", vmin=-1, vmax=1)
ax.set_xticks(range(len(corr.columns)))
ax.set_yticks(range(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=45, ha="right")
ax.set_yticklabels(corr.columns)
ax.set_title("Glass Dataset Correlation Heatmap")
fig.colorbar(im, ax=ax, label="Correlation")
fig.tight_layout()
fig.savefig(CHART_DIR / "correlation_heatmap.png", dpi=300)
plt.close(fig)

# 7. Split data. Stratify is used when every class has enough records.
class_counts = y.value_counts()
stratify = y if class_counts.min() >= 2 else None
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=stratify
)

# 8. Build and train model
model = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("classifier", RandomForestClassifier(
        n_estimators=300, random_state=42, class_weight="balanced"
    ))
])
model.fit(X_train, y_train)

# 9. Evaluate model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"\\nModel Accuracy: {accuracy * 100:.2f}%")
print("\\nClassification Report:")
print(classification_report(y_test, predictions, zero_division=0))

# 10. Confusion matrix
labels = sorted(y.unique())
cm = confusion_matrix(y_test, predictions, labels=labels)
display = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
fig, ax = plt.subplots(figsize=(8, 7))
display.plot(ax=ax, cmap="Blues", colorbar=False)
plt.title("Glass Type Prediction - Confusion Matrix")
plt.tight_layout()
plt.savefig(CHART_DIR / "confusion_matrix.png", dpi=300)
plt.close(fig)

# 11. Feature importance
rf = model.named_steps["classifier"]
importance = pd.Series(rf.feature_importances_, index=X.columns).sort_values()
plt.figure(figsize=(8, 5))
plt.barh(importance.index, importance.values)
plt.title("Feature Importance")
plt.xlabel("Importance")
plt.tight_layout()
plt.savefig(CHART_DIR / "feature_importance.png", dpi=300)
plt.close()

# 12. Save trained model
joblib.dump(model, BASE_DIR / "glass_type_model.pkl")
print("\\nModel saved as glass_type_model.pkl")
print("Charts saved in:", CHART_DIR)

# 13. Predict a new sample
print("\\nEnter chemical composition values for a new glass sample.")
print("Order: RI, Na, Mg, Al, Si, K, Ca, Ba, Fe")
try:
    values = []
    for name in X.columns:
        values.append(float(input(f"Enter {name}: ")))
    sample = pd.DataFrame([values], columns=X.columns)
    result = model.predict(sample)[0]
    print(f"\\nPredicted Glass Type: {result}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
