
import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

warnings.filterwarnings("ignore")
sns.set_theme(style="whitegrid", palette="viridis")

# ==========================================
# HEART DISEASE DATASET
# ==========================================

FILE_PATH = r"C:\Users\USER PC\Desktop\Silent Killer\heart_disease.csv"

OUTPUT_DIR = r"C:\Users\USER PC\Desktop\Silent Killer\Heart_Analysis_Results"
CHART_DIR = os.path.join(OUTPUT_DIR, "Charts")

os.makedirs(CHART_DIR, exist_ok=True)

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv(FILE_PATH)

df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

df = df.replace(["?", "NA", "N/A", ""], np.nan)

for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

if "target" not in df.columns:
    raise ValueError(
        "The dataset must contain a 'target' column. "
        "Check your CSV column names."
    )

df = df.dropna(subset=["target"]).copy()
df["target"] = df["target"].astype(int)

print("\n========== HEART DISEASE DATASET ==========")
print("\nFirst Five Records:")
print(df.head())

print("\nDataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nMissing Values:\n", df.isnull().sum())
print("\nStatistical Summary:\n", df.describe())

# Save cleaned data
df.to_csv(
    os.path.join(OUTPUT_DIR, "cleaned_heart_disease.csv"),
    index=False
)

# ==========================================
# CHECK COLUMNS
# ==========================================

def require(*columns):
    missing = [c for c in columns if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in CSV: {missing}")

require(
    "age", "sex", "cp", "trestbps", "chol",
    "fbs", "restecg", "thalach", "exang",
    "oldpeak", "slope", "ca", "thal", "target"
)

# ==========================================
# CHART FUNCTION
# ==========================================

chart_number = 0

def save_chart(title):
    global chart_number

    chart_number += 1

    plt.title(title, fontsize=14, fontweight="bold")
    plt.tight_layout()

    filename = f"Chart_{chart_number:02d}.png"

    plt.savefig(
        os.path.join(CHART_DIR, filename),
        dpi=160,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()

    print("Generated:", filename)


# ==========================================
# 1. AGE HISTOGRAM
# ==========================================

plt.figure(figsize=(9, 5))
sns.histplot(df["age"].dropna(), bins=15, kde=True)
plt.xlabel("Age")
plt.ylabel("Frequency")
save_chart("1. Age Histogram")


# ==========================================
# 2. AGE KDE PLOT
# ==========================================

plt.figure(figsize=(9, 5))
sns.kdeplot(data=df, x="age", fill=True)
save_chart("2. Age Density Plot")


# ==========================================
# 3. GENDER PIE CHART
# ==========================================

plt.figure(figsize=(7, 7))
df["sex"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)
plt.ylabel("")
save_chart("3. Gender Distribution Pie Chart")


# ==========================================
# 4. TARGET DONUT CHART
# ==========================================

plt.figure(figsize=(7, 7))
values = df["target"].value_counts().sort_index()

plt.pie(
    values,
    labels=values.index,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={"width": 0.4}
)
save_chart("4. Heart Disease Donut Chart")


# ==========================================
# 5. CHEST PAIN BAR CHART
# ==========================================

plt.figure(figsize=(9, 5))
sns.countplot(data=df, x="cp")
save_chart("5. Chest Pain Type Bar Chart")


# ==========================================
# 6. CHOLESTEROL HISTOGRAM
# ==========================================

plt.figure(figsize=(9, 5))
sns.histplot(data=df, x="chol", bins=20, kde=True)
save_chart("6. Cholesterol Histogram")


# ==========================================
# 7. BLOOD PRESSURE KDE
# ==========================================

plt.figure(figsize=(9, 5))
sns.kdeplot(data=df, x="trestbps", fill=True)
save_chart("7. Blood Pressure Density Plot")


# ==========================================
# 8. HEART RATE HISTOGRAM
# ==========================================

plt.figure(figsize=(9, 5))
sns.histplot(data=df, x="thalach", bins=20, color="orange")
save_chart("8. Maximum Heart Rate Histogram")


# ==========================================
# 9. OLDPEAK VIOLIN PLOT
# ==========================================

plt.figure(figsize=(9, 5))
sns.violinplot(data=df, x="target", y="oldpeak")
save_chart("9. Oldpeak Violin Plot")


# ==========================================
# 10. AGE BOX PLOT
# ==========================================

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, y="age")
save_chart("10. Age Box Plot")


# ==========================================
# 11. CHOLESTEROL BOX PLOT BY TARGET
# ==========================================

plt.figure(figsize=(9, 5))
sns.boxplot(data=df, x="target", y="chol")
save_chart("11. Cholesterol Box Plot")


# ==========================================
# 12. AGE VS CHOLESTEROL SCATTER
# ==========================================

plt.figure(figsize=(9, 5))
sns.scatterplot(
    data=df,
    x="age",
    y="chol",
    hue="target",
    size="thalach"
)
save_chart("12. Age vs Cholesterol Scatter Plot")


# ==========================================
# 13. AGE VS HEART RATE
# ==========================================

plt.figure(figsize=(9, 5))
sns.regplot(
    data=df,
    x="age",
    y="thalach",
    scatter_kws={"alpha": 0.5}
)
save_chart("13. Age vs Heart Rate Regression")


# ==========================================
# 14. BLOOD PRESSURE VS CHOLESTEROL
# ==========================================

plt.figure(figsize=(9, 5))
sns.scatterplot(
    data=df,
    x="trestbps",
    y="chol",
    hue="target"
)
save_chart("14. Blood Pressure vs Cholesterol")


# ==========================================
# 15. AGE VS TARGET SWARM PLOT
# ==========================================

plt.figure(figsize=(9, 5))
sns.swarmplot(
    data=df,
    x="target",
    y="age",
    size=3
)
save_chart("15. Age vs Target Swarm Plot")


# ==========================================
# 16. CHEST PAIN VS TARGET
# ==========================================

plt.figure(figsize=(9, 5))
sns.countplot(data=df, x="cp", hue="target")
save_chart("16. Chest Pain vs Target")


# ==========================================
# 17. GENDER VS TARGET
# ==========================================

plt.figure(figsize=(9, 5))
sns.countplot(data=df, x="sex", hue="target")
save_chart("17. Gender vs Target")


# ==========================================
# 18. EXERCISE ANGINA VS TARGET
# ==========================================

plt.figure(figsize=(9, 5))
sns.countplot(data=df, x="exang", hue="target")
save_chart("18. Exercise Angina vs Target")


# ==========================================
# 19. FASTING BLOOD SUGAR VS TARGET
# ==========================================

plt.figure(figsize=(9, 5))
sns.countplot(data=df, x="fbs", hue="target")
save_chart("19. Fasting Blood Sugar vs Target")


# ==========================================
# 20. RESTING ECG VS TARGET
# ==========================================

plt.figure(figsize=(9, 5))
sns.countplot(data=df, x="restecg", hue="target")
save_chart("20. Resting ECG vs Target")


# ==========================================
# 21. SLOPE VS TARGET
# ==========================================

plt.figure(figsize=(9, 5))
sns.countplot(data=df, x="slope", hue="target")
save_chart("21. Slope vs Target")


# ==========================================
# 22. THAL VS TARGET
# ==========================================

plt.figure(figsize=(9, 5))
sns.countplot(data=df, x="thal", hue="target")
save_chart("22. Thal vs Target")


# ==========================================
# 23. CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(13, 9))
sns.heatmap(
    df.corr(numeric_only=True),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)
save_chart("23. Correlation Heatmap")


# ==========================================
# 24. PAIR PLOT
# ==========================================

pair = sns.pairplot(
    df[["age", "trestbps", "chol", "thalach", "target"]].dropna(),
    hue="target",
    diag_kind="hist"
)

pair.fig.suptitle("24. Heart Disease Pair Plot", y=1.02)

chart_number += 1
pair.savefig(
    os.path.join(CHART_DIR, f"Chart_{chart_number:02d}.png"),
    dpi=130
)
plt.show()
plt.close("all")
print("Generated: Chart_24.png")


# ==========================================
# 25. NUMERICAL FEATURE BOXPLOT
# ==========================================

plt.figure(figsize=(11, 6))
sns.boxplot(
    data=df[["age", "trestbps", "chol", "thalach"]]
)
plt.xticks(rotation=15)
save_chart("25. Numerical Features Comparison")


# ==========================================
# 26. AGE GROUP ANALYSIS
# ==========================================

df["age_group"] = pd.cut(
    df["age"],
    bins=[0, 30, 40, 50, 60, 70, 100],
    labels=[
        "Below 30", "30-40", "40-50",
        "50-60", "60-70", "Above 70"
    ]
)

plt.figure(figsize=(10, 5))
sns.countplot(
    data=df,
    x="age_group",
    hue="target"
)
save_chart("26. Age Group Analysis")


# ==========================================
# 27. OLDPEAK VS HEART RATE
# ==========================================

plt.figure(figsize=(9, 5))
sns.scatterplot(
    data=df,
    x="oldpeak",
    y="thalach",
    hue="target"
)
save_chart("27. Oldpeak vs Heart Rate")


# ==========================================
# 28. AVERAGE AGE BY CHEST PAIN TYPE
# ==========================================

plt.figure(figsize=(9, 5))
sns.barplot(
    data=df,
    x="cp",
    y="age",
    errorbar=None
)
save_chart("28. Average Age by Chest Pain Type")


# ==========================================
# 29. TARGET CORRELATION BAR CHART
# ==========================================

target_corr = (
    df.corr(numeric_only=True)["target"]
    .drop("target")
    .sort_values()
)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=target_corr.values,
    y=target_corr.index
)
plt.xlabel("Correlation with Target")
save_chart("29. Target Correlation Ranking")


# ==========================================
# 30. RANDOM FOREST FEATURE IMPORTANCE
# ==========================================

X = df.drop(
    columns=["target", "age_group"],
    errors="ignore"
)

y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("rf", RandomForestClassifier(
        n_estimators=200,
        random_state=42
    ))
])

model.fit(X_train, y_train)

importance = pd.Series(
    model.named_steps["rf"].feature_importances_,
    index=X.columns
).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=importance.values,
    y=importance.index
)
plt.xlabel("Feature Importance")
save_chart("30. Random Forest Feature Importance")

# ==========================================
# MODEL EVALUATION
# ==========================================

predictions = model.predict(X_test)

print("\n========== MODEL EVALUATION ==========")
print("Test Accuracy:", model.score(X_test, y_test))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

importance.to_csv(
    os.path.join(OUTPUT_DIR, "feature_importance.csv")
)

# ==========================================
# FINAL RESULT
# ==========================================

print("\n======================================")
print("HEART DISEASE ANALYSIS COMPLETED")
print("Total Charts:", chart_number)
print("Charts Folder:", CHART_DIR)
print("======================================")
