
import os
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score
)

# ==========================================
# 1. PROJECT CONFIGURATION
# ==========================================

DATASET = "smoke_detection_iot.csv"

OUTPUT_DIR = "Smoke_Detection_Results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

sns.set_theme(style="whitegrid")

print("=" * 60)
print("       IOT SMOKE DETECTION SYSTEM")
print("=" * 60)

# ==========================================
# 2. LOAD DATASET
# ==========================================

df = pd.read_csv(DATASET)

print("\nDataset Loaded Successfully!")

print("\nDataset Shape:", df.shape)

print("\nFirst Five Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Description:")
print(df.describe())

# ==========================================
# 3. DATA PREPROCESSING
# ==========================================

df = df.drop_duplicates()

df = df.drop(
    columns=["Unnamed: 0", "UTC", "CNT"],
    errors="ignore"
)

df = df.replace([np.inf, -np.inf], np.nan)

df = df.dropna(subset=["Fire Alarm"])

df = df.fillna(df.median(numeric_only=True))

print("\nMissing Values:")
print(df.isnull().sum())

print("\nClass Distribution:")
print(df["Fire Alarm"].value_counts())

# ==========================================
# 4. EXPLORATORY DATA ANALYSIS
# ==========================================

# Chart 1: Fire Alarm Distribution

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Fire Alarm"
)

plt.title("Fire Alarm Distribution")
plt.xlabel("Fire Alarm (0 = No, 1 = Yes)")
plt.ylabel("Number of Records")

plt.savefig(
    f"{OUTPUT_DIR}/01_fire_alarm_distribution.png"
)

plt.show()

# Chart 2: Temperature Distribution

plt.figure(figsize=(8, 5))

sns.histplot(
    df["Temperature[C]"],
    kde=True
)

plt.title("Temperature Distribution")
plt.savefig(
    f"{OUTPUT_DIR}/02_temperature.png"
)

plt.show()

# Chart 3: Humidity Distribution

plt.figure(figsize=(8, 5))

sns.histplot(
    df["Humidity[%]"],
    kde=True
)

plt.title("Humidity Distribution")
plt.savefig(
    f"{OUTPUT_DIR}/03_humidity.png"
)

plt.show()

# Chart 4: TVOC Distribution

plt.figure(figsize=(8, 5))

sns.histplot(
    df["TVOC[ppb]"],
    kde=True
)

plt.title("TVOC Distribution")
plt.savefig(
    f"{OUTPUT_DIR}/04_tvoc.png"
)

plt.show()

# Chart 5: CO2 Distribution

plt.figure(figsize=(8, 5))

sns.histplot(
    df["eCO2[ppm]"],
    kde=True
)

plt.title("eCO2 Distribution")
plt.savefig(
    f"{OUTPUT_DIR}/05_co2.png"
)

plt.show()

# Chart 6: PM2.5 Distribution

plt.figure(figsize=(8, 5))

sns.histplot(
    df["PM2.5"],
    kde=True
)

plt.title("PM2.5 Distribution")
plt.savefig(
    f"{OUTPUT_DIR}/06_pm25.png"
)

plt.show()

# Chart 7: Correlation Heatmap

plt.figure(figsize=(14, 10))

sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Sensor Feature Correlation")

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_DIR}/07_correlation.png"
)

plt.show()

# Chart 8: Temperature vs Fire Alarm

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Fire Alarm",
    y="Temperature[C]"
)

plt.title("Temperature vs Fire Alarm")

plt.savefig(
    f"{OUTPUT_DIR}/08_temperature_alarm.png"
)

plt.show()

# Chart 9: Humidity vs Fire Alarm

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Fire Alarm",
    y="Humidity[%]"
)

plt.title("Humidity vs Fire Alarm")

plt.savefig(
    f"{OUTPUT_DIR}/09_humidity_alarm.png"
)

plt.show()

# Chart 10: TVOC vs Fire Alarm

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Fire Alarm",
    y="TVOC[ppb]"
)

plt.title("TVOC vs Fire Alarm")

plt.savefig(
    f"{OUTPUT_DIR}/10_tvoc_alarm.png"
)

plt.show()

# ==========================================
# 5. FEATURE SELECTION
# ==========================================

X = df.drop(columns=["Fire Alarm"])

y = df["Fire Alarm"].astype(int)

print("\nInput Features:")
print(X.columns.tolist())

print("\nTarget Variable: Fire Alarm")

# ==========================================
# 6. TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))

# ==========================================
# 7. RANDOM FOREST MODEL
# ==========================================

print("\nTraining Random Forest...")

rf_model = RandomForestClassifier(
    n_estimators=150,
    max_depth=20,
    min_samples_split=2,
    random_state=42,
    n_jobs=-1,
    class_weight="balanced"
)

rf_model.fit(X_train, y_train)

rf_predictions = rf_model.predict(X_test)

rf_accuracy = accuracy_score(
    y_test,
    rf_predictions
)

print("\nRandom Forest Accuracy:",
      round(rf_accuracy * 100, 2), "%")

print("\nRandom Forest Classification Report:")

print(
    classification_report(
        y_test,
        rf_predictions,
        zero_division=0
    )
)

# ==========================================
# 8. DECISION TREE MODEL
# ==========================================

print("\nTraining Decision Tree...")

dt_model = DecisionTreeClassifier(
    max_depth=15,
    random_state=42,
    class_weight="balanced"
)

dt_model.fit(X_train, y_train)

dt_predictions = dt_model.predict(X_test)

dt_accuracy = accuracy_score(
    y_test,
    dt_predictions
)

print("\nDecision Tree Accuracy:",
      round(dt_accuracy * 100, 2), "%")

# ==========================================
# 9. MODEL COMPARISON
# ==========================================

comparison = pd.DataFrame({
    "Model": [
        "Random Forest",
        "Decision Tree"
    ],

    "Accuracy": [
        rf_accuracy,
        dt_accuracy
    ],

    "Precision": [
        precision_score(y_test, rf_predictions),
        precision_score(y_test, dt_predictions)
    ],

    "Recall": [
        recall_score(y_test, rf_predictions),
        recall_score(y_test, dt_predictions)
    ],

    "F1 Score": [
        f1_score(y_test, rf_predictions),
        f1_score(y_test, dt_predictions)
    ]
})

print("\nMODEL COMPARISON")
print(comparison)

comparison.to_csv(
    f"{OUTPUT_DIR}/model_comparison.csv",
    index=False
)

# Chart 11: Model Accuracy Comparison

plt.figure(figsize=(8, 5))

sns.barplot(
    data=comparison,
    x="Model",
    y="Accuracy"
)

plt.title("Model Accuracy Comparison")

plt.ylim(0, 1)

plt.savefig(
    f"{OUTPUT_DIR}/11_model_accuracy.png"
)

plt.show()

# ==========================================
# 10. CONFUSION MATRIX
# ==========================================

cm = confusion_matrix(
    y_test,
    rf_predictions
)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.title("Random Forest Confusion Matrix")

plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.savefig(
    f"{OUTPUT_DIR}/12_confusion_matrix.png"
)

plt.show()

# ==========================================
# 11. FEATURE IMPORTANCE
# ==========================================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFEATURE IMPORTANCE:")
print(importance)

plt.figure(figsize=(10, 7))

sns.barplot(
    data=importance,
    x="Importance",
    y="Feature"
)

plt.title("Random Forest Feature Importance")

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_DIR}/13_feature_importance.png"
)

plt.show()

# ==========================================
# 12. SAVE TRAINED MODELS
# ==========================================

joblib.dump(
    rf_model,
    f"{OUTPUT_DIR}/random_forest_model.pkl"
)

joblib.dump(
    dt_model,
    f"{OUTPUT_DIR}/decision_tree_model.pkl"
)

joblib.dump(
    list(X.columns),
    f"{OUTPUT_DIR}/feature_columns.pkl"
)

# ==========================================
# 13. NEW SENSOR DATA PREDICTION
# ==========================================

sample = X_test.iloc[[0]]

prediction = rf_model.predict(sample)[0]

probability = rf_model.predict_proba(sample)[0][1]

print("\nNEW SENSOR DATA PREDICTION")

print(sample)

if prediction == 1:
    print("\nRESULT: FIRE ALARM DETECTED")
else:
    print("\nRESULT: NO FIRE ALARM DETECTED")

print(
    "Predicted Fire Alarm Probability:",
    round(probability * 100, 2), "%"
)

# ==========================================
# 14. SAVE PREDICTION RESULTS
# ==========================================

results = X_test.copy()

results["Actual"] = y_test

results["Predicted"] = rf_predictions

results.to_csv(
    f"{OUTPUT_DIR}/prediction_results.csv",
    index=False
)

# ==========================================
# 15. FINAL OUTPUT
# ==========================================

print("\n" + "=" * 60)

print("       PROJECT EXECUTION COMPLETED")

print("=" * 60)

print("\nGenerated Files:")

print("1. Random Forest Model")
print("2. Decision Tree Model")
print("3. Model Comparison")
print("4. Prediction Results")
print("5. Feature Importance")
print("6. 13 Visualization Charts")

print("\nOutput Folder:", OUTPUT_DIR)

print("\nThank You!")
