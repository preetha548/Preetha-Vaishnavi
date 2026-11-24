
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

print("=" * 65)
print("       SLEEP HEALTH AND LIFESTYLE DATA ANALYSIS")
print("=" * 65)

# 1. Load Dataset
try:
    df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
    print("\nDataset loaded successfully!")
except FileNotFoundError:
    print("ERROR: sleep_health.csv not found!")
    print("Place your CSV file in the project folder.")
    raise SystemExit

# 2. Clean column names
df.columns = df.columns.str.strip()

# 3. Dataset Information
print("\n--- DATASET INFORMATION ---")
print(df.head())
print("\nShape:", df.shape)
print("\nColumns:", df.columns.tolist())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DUPLICATE RECORDS ---")
print(df.duplicated().sum())

# 4. Remove duplicates
df = df.drop_duplicates()

# 5. Statistical Analysis
print("\n--- NUMERICAL STATISTICS ---")
print(df.describe())

# 6. Categorical Analysis
categorical_columns = df.select_dtypes(
    include="object"
).columns

for col in categorical_columns:
    print(f"\n--- {col} DISTRIBUTION ---")
    print(df[col].value_counts())

# 7. Numerical Analysis
numeric_columns = df.select_dtypes(
    include=np.number
).columns

print("\n--- CORRELATION ANALYSIS ---")
print(df[numeric_columns].corr())

# 8. Create output directory
os.makedirs("sleep_results", exist_ok=True)

sns.set_theme(style="whitegrid")

# 9. Visualization Function
def save_chart(filename):
    plt.tight_layout()
    plt.savefig(
        f"sleep_results/{filename}",
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()
    plt.close()

# CHART 1: Age Distribution
if "Age" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Age"], bins=15, kde=True)
    plt.title("Age Distribution")
    save_chart("01_age_distribution.png")

# CHART 2: Gender Distribution
if "Gender" in df.columns:
    plt.figure(figsize=(7, 5))
    sns.countplot(data=df, x="Gender")
    plt.title("Gender Distribution")
    save_chart("02_gender_distribution.png")

# CHART 3: Sleep Duration
if "Sleep Duration" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Sleep Duration"], kde=True)
    plt.title("Sleep Duration Distribution")
    save_chart("03_sleep_duration.png")

# CHART 4: Quality of Sleep
if "Quality of Sleep" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Quality of Sleep"], bins=10)
    plt.title("Quality of Sleep Distribution")
    save_chart("04_sleep_quality.png")

# CHART 5: Stress Level
if "Stress Level" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="Stress Level")
    plt.title("Stress Level Distribution")
    save_chart("05_stress_level.png")

# CHART 6: BMI Category
if "BMI Category" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="BMI Category")
    plt.title("BMI Category Distribution")
    plt.xticks(rotation=30)
    save_chart("06_bmi_category.png")

# CHART 7: Sleep Disorder
if "Sleep Disorder" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="Sleep Disorder")
    plt.title("Sleep Disorder Distribution")
    plt.xticks(rotation=30)
    save_chart("07_sleep_disorder.png")

# CHART 8: Occupation
if "Occupation" in df.columns:
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df, y="Occupation")
    plt.title("Occupation Distribution")
    save_chart("08_occupation.png")

# CHART 9: Daily Steps
if "Daily Steps" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Daily Steps"], kde=True)
    plt.title("Daily Steps Distribution")
    save_chart("09_daily_steps.png")

# CHART 10: Heart Rate
if "Heart Rate" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Heart Rate"], kde=True)
    plt.title("Heart Rate Distribution")
    save_chart("10_heart_rate.png")

# CHART 11: Physical Activity
if "Physical Activity Level" in df.columns:
    plt.figure(figsize=(8, 5))
    sns.histplot(df["Physical Activity Level"], kde=True)
    plt.title("Physical Activity Level")
    save_chart("11_physical_activity.png")

# CHART 12: Correlation Heatmap
if len(numeric_columns) > 1:
    plt.figure(figsize=(10, 7))
    sns.heatmap(
        df[numeric_columns].corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )
    plt.title("Feature Correlation Heatmap")
    save_chart("12_correlation_heatmap.png")

# CHART 13: Sleep Duration vs Quality
if {"Sleep Duration", "Quality of Sleep"}.issubset(df.columns):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x="Sleep Duration",
        y="Quality of Sleep"
    )
    plt.title("Sleep Duration vs Sleep Quality")
    save_chart("13_sleep_vs_quality.png")

# CHART 14: Age vs Sleep Duration
if {"Age", "Sleep Duration"}.issubset(df.columns):
    plt.figure(figsize=(8, 5))
    sns.scatterplot(
        data=df,
        x="Age",
        y="Sleep Duration"
    )
    plt.title("Age vs Sleep Duration")
    save_chart("14_age_vs_sleep.png")

# CHART 15: Stress vs Sleep Quality
if {"Stress Level", "Quality of Sleep"}.issubset(df.columns):
    plt.figure(figsize=(8, 5))
    sns.boxplot(
        data=df,
        x="Stress Level",
        y="Quality of Sleep"
    )
    plt.title("Stress Level vs Sleep Quality")
    save_chart("15_stress_vs_quality.png")

# 16. Blood Pressure Analysis
if "Blood Pressure" in df.columns:
    bp = df["Blood Pressure"].astype(str).str.split("/", expand=True)
    if bp.shape[1] >= 2:
        df["Systolic BP"] = pd.to_numeric(bp[0], errors="coerce")
        df["Diastolic BP"] = pd.to_numeric(bp[1], errors="coerce")

        plt.figure(figsize=(8, 5))
        df[["Systolic BP", "Diastolic BP"]].mean().plot(
            kind="bar"
        )
        plt.title("Average Blood Pressure Components")
        plt.ylabel("Blood Pressure (mmHg)")
        save_chart("16_blood_pressure.png")

# 17. Export cleaned data
df.to_csv(
    "sleep_results/cleaned_sleep_data.csv",
    index=False
)

# 18. Final Report
print("\n" + "=" * 65)
print("             FINAL ANALYSIS REPORT")
print("=" * 65)

print("Total Records:", len(df))
print("Total Features:", len(df.columns))

if "Sleep Duration" in df.columns:
    print("Average Sleep Duration:",
          df["Sleep Duration"].mean())

if "Quality of Sleep" in df.columns:
    print("Average Sleep Quality:",
          df["Quality of Sleep"].mean())

if "Age" in df.columns:
    print("Average Age:", df["Age"].mean())

if "Sleep Disorder" in df.columns:
    print("\nSleep Disorder Counts:")
    print(df["Sleep Disorder"].value_counts())

print("\nAnalysis completed!")
print("Results saved in the sleep_results folder.")

