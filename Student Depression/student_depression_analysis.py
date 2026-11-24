
# ============================================================
# STUDENT DEPRESSION DATASET - PYTHON DATA ANALYSIS
# Dataset: Student Depression Dataset.csv
# ============================================================

import os
import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# ------------------------------------------------------------
# 1. SETTINGS
# ------------------------------------------------------------

sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

OUTPUT_DIR = "Student_Depression_Results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------------------------------------------------
# 2. LOAD DATASET
# ------------------------------------------------------------

df = pd.read_csv("Student Depression Dataset.csv")

print("\n========== DATASET INFORMATION ==========")

print("Dataset Shape:", df.shape)
print("\nFirst Five Records:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Description:")
print(df.describe(include="all"))

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:", df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

# ------------------------------------------------------------
# 3. DATA CLEANING
# ------------------------------------------------------------

df.columns = df.columns.str.strip()

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

print("\nCleaned Dataset Shape:", df.shape)

# Depression distribution
print("\nDepression Distribution:")
print(df["Depression"].value_counts())

# ------------------------------------------------------------
# 4. SAVE DATA SUMMARY
# ------------------------------------------------------------

df.describe(include="all").to_csv(
    os.path.join(OUTPUT_DIR, "dataset_summary.csv")
)

df.isnull().sum().to_csv(
    os.path.join(OUTPUT_DIR, "missing_values.csv")
)

# ------------------------------------------------------------
# 5. VISUALIZATION FUNCTION
# ------------------------------------------------------------

def save_plot(filename):
    plt.tight_layout()
    plt.savefig(
        os.path.join(OUTPUT_DIR, filename),
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()
    plt.close()

# ------------------------------------------------------------
# CHART 1 - Gender Distribution
# ------------------------------------------------------------

plt.figure()
sns.countplot(data=df, x="Gender")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Students")
save_plot("chart_01_gender.png")

# ------------------------------------------------------------
# CHART 2 - Age Distribution
# ------------------------------------------------------------

plt.figure()
sns.histplot(df["Age"], bins=30, kde=True)
plt.title("Student Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
save_plot("chart_02_age.png")

# ------------------------------------------------------------
# CHART 3 - Depression Distribution
# ------------------------------------------------------------

plt.figure()
sns.countplot(data=df, x="Depression")
plt.title("Depression Distribution")
plt.xlabel("Depression (0 = No, 1 = Yes)")
plt.ylabel("Number of Students")
save_plot("chart_03_depression.png")

# ------------------------------------------------------------
# CHART 4 - Academic Pressure
# ------------------------------------------------------------

plt.figure()
sns.countplot(data=df, x="Academic Pressure")
plt.title("Academic Pressure Among Students")
plt.xlabel("Academic Pressure")
plt.ylabel("Student Count")
save_plot("chart_04_academic_pressure.png")

# ------------------------------------------------------------
# CHART 5 - Study Satisfaction
# ------------------------------------------------------------

plt.figure()
sns.countplot(data=df, x="Study Satisfaction")
plt.title("Study Satisfaction Level")
plt.xlabel("Study Satisfaction")
plt.ylabel("Student Count")
save_plot("chart_05_study_satisfaction.png")

# ------------------------------------------------------------
# CHART 6 - Sleep Duration
# ------------------------------------------------------------

plt.figure()
sns.countplot(
    data=df,
    y="Sleep Duration",
    order=df["Sleep Duration"].value_counts().index
)
plt.title("Sleep Duration Analysis")
plt.xlabel("Number of Students")
plt.ylabel("Sleep Duration")
save_plot("chart_06_sleep.png")

# ------------------------------------------------------------
# CHART 7 - Dietary Habits
# ------------------------------------------------------------

plt.figure()
sns.countplot(
    data=df,
    x="Dietary Habits",
    order=df["Dietary Habits"].value_counts().index
)
plt.title("Dietary Habits Distribution")
plt.xticks(rotation=20)
save_plot("chart_07_diet.png")

# ------------------------------------------------------------
# CHART 8 - Financial Stress
# ------------------------------------------------------------

plt.figure()
sns.countplot(data=df, x="Financial Stress")
plt.title("Financial Stress Among Students")
plt.xlabel("Financial Stress")
plt.ylabel("Student Count")
save_plot("chart_08_financial_stress.png")

# ------------------------------------------------------------
# CHART 9 - CGPA Distribution
# ------------------------------------------------------------

plt.figure()
sns.histplot(df["CGPA"], bins=30, kde=True)
plt.title("CGPA Distribution")
plt.xlabel("CGPA")
plt.ylabel("Frequency")
save_plot("chart_09_cgpa.png")

# ------------------------------------------------------------
# CHART 10 - Work and Study Hours
# ------------------------------------------------------------

plt.figure()
sns.histplot(df["Work/Study Hours"], bins=20, kde=True)
plt.title("Work and Study Hours")
plt.xlabel("Hours")
plt.ylabel("Frequency")
save_plot("chart_10_work_study_hours.png")

# ------------------------------------------------------------
# CHART 11 - Depression by Gender
# ------------------------------------------------------------

plt.figure()
sns.countplot(data=df, x="Gender", hue="Depression")
plt.title("Depression Distribution by Gender")
plt.ylabel("Student Count")
save_plot("chart_11_gender_depression.png")

# ------------------------------------------------------------
# CHART 12 - Depression by Sleep Duration
# ------------------------------------------------------------

plt.figure()
sns.countplot(
    data=df,
    x="Sleep Duration",
    hue="Depression"
)
plt.title("Depression by Sleep Duration")
plt.xticks(rotation=25)
save_plot("chart_12_sleep_depression.png")

# ------------------------------------------------------------
# CHART 13 - Depression by Academic Pressure
# ------------------------------------------------------------

plt.figure()
sns.countplot(
    data=df,
    x="Academic Pressure",
    hue="Depression"
)
plt.title("Academic Pressure vs Depression")
save_plot("chart_13_pressure_depression.png")

# ------------------------------------------------------------
# CHART 14 - Depression by Dietary Habits
# ------------------------------------------------------------

plt.figure()
sns.countplot(
    data=df,
    x="Dietary Habits",
    hue="Depression"
)
plt.title("Dietary Habits vs Depression")
plt.xticks(rotation=20)
save_plot("chart_14_diet_depression.png")

# ------------------------------------------------------------
# CHART 15 - Family Mental Health History
# ------------------------------------------------------------

plt.figure()
sns.countplot(
    data=df,
    x="Family History of Mental Illness",
    hue="Depression"
)
plt.title("Family History vs Depression")
save_plot("chart_15_family_history.png")

# ------------------------------------------------------------
# CHART 16 - Suicidal Thoughts Distribution
# ------------------------------------------------------------

plt.figure()
sns.countplot(
    data=df,
    x="Have you ever had suicidal thoughts ?",
    hue="Depression"
)
plt.title("Suicidal Thoughts and Depression Labels")
save_plot("chart_16_suicidal_thoughts.png")

# ------------------------------------------------------------
# CHART 17 - Financial Stress vs Depression
# ------------------------------------------------------------

plt.figure()
sns.countplot(
    data=df,
    x="Financial Stress",
    hue="Depression"
)
plt.title("Financial Stress vs Depression")
save_plot("chart_17_financial_depression.png")

# ------------------------------------------------------------
# CHART 18 - CGPA vs Depression
# ------------------------------------------------------------

plt.figure()
sns.boxplot(
    data=df,
    x="Depression",
    y="CGPA"
)
plt.title("CGPA vs Depression")
save_plot("chart_18_cgpa_depression.png")

# ------------------------------------------------------------
# CHART 19 - Age vs Depression
# ------------------------------------------------------------

plt.figure()
sns.boxplot(
    data=df,
    x="Depression",
    y="Age"
)
plt.title("Age vs Depression")
save_plot("chart_19_age_depression.png")

# ------------------------------------------------------------
# CHART 20 - Correlation Heatmap
# ------------------------------------------------------------

numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(14, 10))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Student Depression Dataset Correlation Heatmap")
save_plot("chart_20_correlation.png")

# ------------------------------------------------------------
# 6. DEPRESSION PERCENTAGE ANALYSIS
# ------------------------------------------------------------

print("\n========== DEPRESSION PERCENTAGE ==========")

print(
    df["Depression"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

# ------------------------------------------------------------
# 7. MACHINE LEARNING MODEL
# ------------------------------------------------------------

print("\n========== MACHINE LEARNING ==========")

# Remove ID because it is an identifier
X = df.drop(columns=["Depression", "id"], errors="ignore")
y = df["Depression"]

numeric_features = X.select_dtypes(
    include=np.number
).columns.tolist()

categorical_features = X.select_dtypes(
    exclude=np.number
).columns.tolist()

numeric_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

categorical_transformer = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("num", numeric_transformer, numeric_features),
    ("cat", categorical_transformer, categorical_features)
])

model = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        class_weight="balanced",
        n_jobs=-1
    ))
])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# ------------------------------------------------------------
# 8. CONFUSION MATRIX
# ------------------------------------------------------------

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["No Depression", "Depression"]
)

disp.plot(cmap="Blues")
plt.title("Random Forest Confusion Matrix")
save_plot("chart_21_confusion_matrix.png")

# ------------------------------------------------------------
# 9. FEATURE IMPORTANCE
# ------------------------------------------------------------

feature_names = model.named_steps[
    "preprocessor"
].get_feature_names_out()

importance = model.named_steps[
    "classifier"
].feature_importances_

importance_df = pd.DataFrame({
    "Feature": feature_names,
    "Importance": importance
}).sort_values(
    by="Importance",
    ascending=False
)

print("\nTop 15 Important Features:")
print(importance_df.head(15))

importance_df.head(15).to_csv(
    os.path.join(OUTPUT_DIR, "feature_importance.csv"),
    index=False
)

plt.figure(figsize=(12, 7))
sns.barplot(
    data=importance_df.head(15),
    x="Importance",
    y="Feature"
)
plt.title("Top 15 Feature Importance")
save_plot("chart_22_feature_importance.png")

# ------------------------------------------------------------
# 10. SAVE MODEL
# ------------------------------------------------------------

import joblib

joblib.dump(
    model,
    os.path.join(OUTPUT_DIR, "student_depression_model.pkl")
)

# ------------------------------------------------------------
# 11. FINAL OUTPUT
# ------------------------------------------------------------

print("\n======================================")
print("STUDENT DEPRESSION ANALYSIS COMPLETED")
print("======================================")
print("Total Records:", len(df))
print("Total Columns:", len(df.columns))
print("Generated Charts: 22")
print("Machine Learning: Random Forest")
print("Model Accuracy:", round(accuracy * 100, 2), "%")
print("Output Folder:", OUTPUT_DIR)
print("======================================")
