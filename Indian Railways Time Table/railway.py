
import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore")
sns.set_theme(style="whitegrid")

# ==========================================
# 1. DATASET LOADING
# ==========================================

FILE_PATH = r"C:\Users\USER PC\Desktop\Indian Railways Time Table\isl_wise_train_detail_03082015_v1.csv"

OUTPUT_DIR = os.path.join(
    os.path.dirname(FILE_PATH),
    "Railway_Analysis_Results"
)

os.makedirs(OUTPUT_DIR, exist_ok=True)

if not os.path.exists(FILE_PATH):
    raise FileNotFoundError(
        f"Dataset not found: {FILE_PATH}"
    )

# Automatic encoding detection
try:
    df = pd.read_csv(FILE_PATH, encoding="utf-8-sig", low_memory=False)
except UnicodeDecodeError:
    df = pd.read_csv(FILE_PATH, encoding="latin1", low_memory=False)

df.columns = df.columns.astype(str).str.strip()

print("\n====================================")
print("INDIAN RAILWAYS DATA ANALYSIS")
print("====================================")

print("\nDataset Shape:", df.shape)
print("\nColumn Names:\n", df.columns.tolist())
print("\nFirst 10 Records:\n", df.head(10))
print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe(include="all").T)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:", df.duplicated().sum())

# ==========================================
# 2. DATA CLEANING
# ==========================================

df = df.drop_duplicates().copy()

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].replace(r"^\s*$", np.nan, regex=True)
    df[col] = df[col].str.strip()

numeric_cols = df.select_dtypes(
    include=np.number
).columns.tolist()

categorical_cols = df.select_dtypes(
    include=["object", "category"]
).columns.tolist()

# Use actual columns from dataset
print("\nNumeric Columns:", numeric_cols)
print("\nCategorical Columns:", categorical_cols)

# ==========================================
# 3. CHART SAVING FUNCTION
# ==========================================

chart_count = 0

def save_chart(title):
    global chart_count

    chart_count += 1

    plt.title(title, fontsize=14, fontweight="bold")
    plt.tight_layout()

    output_file = os.path.join(
        OUTPUT_DIR,
        f"Chart_{chart_count:02d}.png"
    )

    plt.savefig(
        output_file,
        dpi=250,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()

    print("Saved:", output_file)


def empty_chart(title, message):
    plt.figure(figsize=(9, 5))
    plt.text(
        0.5, 0.5, message,
        ha="center", va="center",
        fontsize=13
    )
    plt.axis("off")
    save_chart(title)


# ==========================================
# 4. CHART 1 - DATASET OVERVIEW
# ==========================================

plt.figure(figsize=(8, 5))
plt.bar(
    ["Rows", "Columns"],
    [df.shape[0], df.shape[1]]
)
save_chart("Dataset Overview")

# ==========================================
# CHART 2 - MISSING VALUES
# ==========================================

missing = df.isnull().sum().sort_values(
    ascending=False
)

missing = missing[missing > 0]

if len(missing):
    plt.figure(figsize=(12, 6))
    sns.barplot(x=missing.index, y=missing.values)
    plt.xticks(rotation=60)
    save_chart("Missing Values Analysis")
else:
    empty_chart(
        "Missing Values Analysis",
        "No missing values found"
    )

# ==========================================
# CHART 3 - DATA TYPES
# ==========================================

plt.figure(figsize=(7, 5))
df.dtypes.astype(str).value_counts().plot(
    kind="pie", autopct="%1.1f%%"
)
save_chart("Data Type Distribution")

# ==========================================
# CHART 4 - NUMERIC FEATURES
# ==========================================

if numeric_cols:
    plt.figure(figsize=(12, 5))
    df[numeric_cols].count().plot(kind="bar")
    plt.xticks(rotation=45)
    save_chart("Numeric Feature Count")
else:
    empty_chart("Numeric Feature Count", "No numeric columns")

# ==========================================
# CHART 5 - FEATURE TYPE COMPARISON
# ==========================================

plt.figure(figsize=(7, 5))
plt.bar(
    ["Numeric", "Categorical"],
    [len(numeric_cols), len(categorical_cols)]
)
save_chart("Feature Type Comparison")

# ==========================================
# CHART 6 - DUPLICATE ANALYSIS
# ==========================================

plt.figure(figsize=(7, 5))
duplicates = pd.read_csv(
    FILE_PATH, encoding="latin1", low_memory=False
).duplicated().sum()

unique = len(pd.read_csv(
    FILE_PATH, encoding="latin1", low_memory=False
)) - duplicates

plt.pie(
    [unique, duplicates],
    labels=["Unique Records", "Duplicate Records"],
    autopct="%1.1f%%"
)
save_chart("Duplicate Record Analysis")

# ==========================================
# CHART 7 - NUMERIC HISTOGRAM
# ==========================================

if numeric_cols:
    plt.figure(figsize=(9, 5))
    sns.histplot(df[numeric_cols[0]].dropna(), kde=True)
    save_chart("Numeric Histogram")
else:
    empty_chart("Numeric Histogram", "No numeric data")

# ==========================================
# CHART 8 - BOX PLOT
# ==========================================

if numeric_cols:
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df[numeric_cols[:10]])
    plt.xticks(rotation=45)
    save_chart("Numeric Box Plot")
else:
    empty_chart("Numeric Box Plot", "No numeric data")

# ==========================================
# CHART 9 - CORRELATION HEATMAP
# ==========================================

if len(numeric_cols) >= 2:
    plt.figure(figsize=(12, 8))
    sns.heatmap(
        df[numeric_cols].corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )
    save_chart("Correlation Heatmap")
else:
    empty_chart("Correlation Heatmap", "Not enough numeric columns")

# ==========================================
# CHART 10 - PAIR PLOT
# ==========================================

if len(numeric_cols) >= 2:
    pair_data = df[numeric_cols[:4]].dropna()

    if len(pair_data) > 0:
        pair_data = pair_data.sample(
            min(500, len(pair_data)),
            random_state=42
        )

        sns.pairplot(pair_data)
        plt.savefig(
            os.path.join(OUTPUT_DIR, "Chart_10.png"),
            dpi=200
        )
        plt.show()
        plt.close()
        chart_count += 1
    else:
        empty_chart("Pair Plot", "No complete numeric records")
else:
    empty_chart("Pair Plot", "Not enough numeric columns")

# ==========================================
# CHART 11 - CATEGORY BAR CHART
# ==========================================

if categorical_cols:
    col = categorical_cols[0]
    plt.figure(figsize=(12, 6))
    df[col].value_counts().head(15).plot(kind="bar")
    plt.xticks(rotation=60)
    save_chart("Category Distribution")
else:
    empty_chart("Category Distribution", "No categorical columns")

# ==========================================
# CHART 12 - SECOND CATEGORY
# ==========================================

if len(categorical_cols) >= 2:
    col = categorical_cols[1]
    plt.figure(figsize=(12, 6))
    df[col].value_counts().head(15).plot(kind="bar")
    plt.xticks(rotation=60)
    save_chart("Second Category Distribution")
else:
    empty_chart("Second Category Distribution", "Second category unavailable")

# ==========================================
# CHART 13 - PIE CHART
# ==========================================

if categorical_cols:
    counts = df[categorical_cols[0]].value_counts().head(10)
    plt.figure(figsize=(8, 7))
    plt.pie(
        counts.values,
        labels=counts.index.astype(str),
        autopct="%1.1f%%"
    )
    save_chart("Category Percentage Distribution")
else:
    empty_chart("Category Percentage Distribution", "No category data")

# ==========================================
# CHART 14 - HORIZONTAL BAR
# ==========================================

if categorical_cols:
    plt.figure(figsize=(10, 6))
    df[categorical_cols[-1]].value_counts().head(10).plot(
        kind="barh"
    )
    save_chart("Top 10 Categories")
else:
    empty_chart("Top 10 Categories", "No category data")

# ==========================================
# CHART 15 - NUMERIC MEAN
# ==========================================

if numeric_cols:
    plt.figure(figsize=(12, 5))
    df[numeric_cols].mean().plot(kind="bar")
    plt.xticks(rotation=45)
    save_chart("Numeric Mean Comparison")
else:
    empty_chart("Numeric Mean Comparison", "No numeric data")

# ==========================================
# CHART 16 - VARIANCE
# ==========================================

if numeric_cols:
    plt.figure(figsize=(12, 5))
    df[numeric_cols].var().plot(kind="bar")
    plt.xticks(rotation=45)
    save_chart("Variance Analysis")
else:
    empty_chart("Variance Analysis", "No numeric data")

# ==========================================
# CHART 17 - STANDARD DEVIATION
# ==========================================

if numeric_cols:
    plt.figure(figsize=(12, 5))
    df[numeric_cols].std().plot(kind="bar")
    plt.xticks(rotation=45)
    save_chart("Standard Deviation Analysis")
else:
    empty_chart("Standard Deviation Analysis", "No numeric data")

# ==========================================
# CHART 18 - NUMERIC SUM
# ==========================================

if numeric_cols:
    plt.figure(figsize=(12, 5))
    df[numeric_cols].sum().plot(kind="bar")
    plt.xticks(rotation=45)
    save_chart("Numeric Sum Analysis")
else:
    empty_chart("Numeric Sum Analysis", "No numeric data")

# ==========================================
# CHART 19 - MINIMUM VALUES
# ==========================================

if numeric_cols:
    plt.figure(figsize=(12, 5))
    df[numeric_cols].min().plot(kind="bar")
    plt.xticks(rotation=45)
    save_chart("Minimum Value Analysis")
else:
    empty_chart("Minimum Value Analysis", "No numeric data")

# ==========================================
# CHART 20 - MAXIMUM VALUES
# ==========================================

if numeric_cols:
    plt.figure(figsize=(12, 5))
    df[numeric_cols].max().plot(kind="bar")
    plt.xticks(rotation=45)
    save_chart("Maximum Value Analysis")
else:
    empty_chart("Maximum Value Analysis", "No numeric data")

# ==========================================
# CHART 21 - SCATTER PLOT
# ==========================================

if len(numeric_cols) >= 2:
    plt.figure(figsize=(9, 6))
    sns.scatterplot(
        data=df,
        x=numeric_cols[0],
        y=numeric_cols[1],
        alpha=0.5
    )
    save_chart("Numeric Scatter Plot")
else:
    empty_chart("Numeric Scatter Plot", "Not enough numeric columns")

# ==========================================
# CHART 22 - LINE PLOT
# ==========================================

if numeric_cols:
    plt.figure(figsize=(10, 5))
    df[numeric_cols[0]].dropna().head(1000).reset_index(
        drop=True
    ).plot()
    save_chart("Numeric Line Plot")
else:
    empty_chart("Numeric Line Plot", "No numeric data")

# ==========================================
# CHART 23 - KDE
# ==========================================

if numeric_cols:
    plt.figure(figsize=(9, 5))
    sns.kdeplot(
        x=df[numeric_cols[0]].dropna(),
        fill=True
    )
    save_chart("Kernel Density Estimation")
else:
    empty_chart("Kernel Density Estimation", "No numeric data")

# ==========================================
# CHART 24 - VIOLIN PLOT
# ==========================================

if numeric_cols:
    plt.figure(figsize=(8, 5))
    sns.violinplot(y=df[numeric_cols[0]].dropna())
    save_chart("Violin Plot")
else:
    empty_chart("Violin Plot", "No numeric data")

# ==========================================
# CHART 25 - ECDF
# ==========================================

if numeric_cols:
    plt.figure(figsize=(9, 5))
    sns.ecdfplot(x=df[numeric_cols[0]].dropna())
    save_chart("Cumulative Distribution Plot")
else:
    empty_chart("Cumulative Distribution Plot", "No numeric data")

# ==========================================
# CHART 26 - CATEGORY FREQUENCY
# ==========================================

if categorical_cols:
    plt.figure(figsize=(10, 5))
    df[categorical_cols[0]].value_counts().head(15).plot(
        kind="line", marker="o"
    )
    plt.xticks(rotation=60)
    save_chart("Category Frequency Analysis")
else:
    empty_chart("Category Frequency Analysis", "No category data")

# ==========================================
# CHART 27 - HISTOGRAM COMPARISON
# ==========================================

if numeric_cols:
    cols = numeric_cols[:4]
    df[cols].hist(figsize=(12, 8), bins=20)
    plt.suptitle("Numeric Feature Histograms")
    plt.tight_layout()
    plt.savefig(
        os.path.join(OUTPUT_DIR, "Chart_27.png"),
        dpi=250
    )
    plt.show()
    plt.close()
    chart_count += 1
else:
    empty_chart("Histogram Comparison", "No numeric data")

# ==========================================
# CHART 28 - TOP RECORDS
# ==========================================

if categorical_cols:
    counts = df[categorical_cols[-1]].value_counts().head(10)

    plt.figure(figsize=(10, 5))
    plt.bar(
        counts.index.astype(str),
        counts.values
    )
    plt.xticks(rotation=60)
    save_chart("Top Record Frequency")
else:
    empty_chart("Top Record Frequency", "No category data")

# ==========================================
# CHART 29 - RELATIONSHIP HEATMAP
# ==========================================

if len(numeric_cols) >= 2:
    plt.figure(figsize=(10, 6))
    sns.heatmap(
        df[numeric_cols[:10]].corr(),
        cmap="viridis",
        annot=True,
        fmt=".2f"
    )
    save_chart("Feature Relationship Heatmap")
else:
    empty_chart("Feature Relationship Heatmap", "Not enough numeric columns")

# ==========================================
# CHART 30 - DATASET SUMMARY
# ==========================================

summary = {
    "Total Rows": len(df),
    "Total Columns": len(df.columns),
    "Numeric Columns": len(numeric_cols),
    "Categorical Columns": len(categorical_cols),
    "Missing Values": int(df.isnull().sum().sum()),
    "Duplicate Records Removed": int(
        pd.read_csv(
            FILE_PATH,
            encoding="latin1",
            low_memory=False
        ).duplicated().sum()
    )
}

plt.figure(figsize=(11, 6))
plt.bar(
    list(summary.keys()),
    list(summary.values())
)
plt.xticks(rotation=35, ha="right")
save_chart("Indian Railways Dataset Summary")

# ==========================================
# 5. EXPORT REPORTS
# ==========================================

df.describe(include="all").T.to_csv(
    os.path.join(OUTPUT_DIR, "statistical_summary.csv")
)

df.isnull().sum().to_csv(
    os.path.join(OUTPUT_DIR, "missing_values.csv")
)

df.to_csv(
    os.path.join(OUTPUT_DIR, "cleaned_railway_data.csv"),
    index=False
)

pd.DataFrame(
    list(summary.items()),
    columns=["Metric", "Value"]
).to_csv(
    os.path.join(OUTPUT_DIR, "dataset_summary.csv"),
    index=False
)

print("\n====================================")
print("ANALYSIS COMPLETED SUCCESSFULLY")
print("====================================")
print("Charts generated:", chart_count)
print("Total records:", len(df))
print("Total columns:", len(df.columns))
print("Output folder:", OUTPUT_DIR)
