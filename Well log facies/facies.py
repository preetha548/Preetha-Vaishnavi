
import os
import warnings
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA

warnings.filterwarnings("ignore")

# ==========================================
# WELL LOG FACIES ANALYSIS - 30 CHARTS
# ==========================================

FILE_PATH = r"C:\Users\USER PC\Desktop\Well log facies\facies_data.csv"

OUTPUT_DIR = r"C:\Users\USER PC\Desktop\Well log facies\30_Charts_Output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

sns.set_theme(style="whitegrid", palette="viridis")

print("=" * 60)
print("       WELL LOG FACIES ANALYSIS")
print("       30 CHARTS VISUALIZATION")
print("=" * 60)

# 1. LOAD DATASET
df = pd.read_csv(FILE_PATH)

print("\nDataset Loaded Successfully!")
print("Dataset Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 Rows:\n", df.head())

# 2. DATA CLEANING
df = df.drop_duplicates()

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

if len(numeric_cols) == 0:
    raise ValueError("No numerical columns found in dataset.")

df[numeric_cols] = df[numeric_cols].replace(
    [np.inf, -np.inf], np.nan
)

df[numeric_cols] = df[numeric_cols].fillna(
    df[numeric_cols].median()
)

facies_col = next(
    (c for c in df.columns if c.lower() in
     ["facies", "facies_label", "class", "label"]),
    None
)

depth_col = next(
    (c for c in df.columns if c.lower() in
     ["depth", "dept", "depth_m", "depth_ft"]),
    None
)

# Select useful log features
log_cols = [
    c for c in numeric_cols
    if c != depth_col
]

if not log_cols:
    raise ValueError("No numerical well-log features available.")

if facies_col:
    df[facies_col] = df[facies_col].fillna("Unknown")

# CHART MANAGEMENT
chart_number = 0

def save_chart(title, filename):
    global chart_number

    chart_number += 1
    plt.title(title, fontsize=13, fontweight="bold")
    plt.tight_layout()

    plt.savefig(
        os.path.join(
            OUTPUT_DIR,
            f"{chart_number:02d}_{filename}.png"
        ),
        dpi=150,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()

    print(f"Chart {chart_number}/30: {title}")


# ==========================================
# CHART 1: DATASET OVERVIEW
# ==========================================

plt.figure(figsize=(10, 6))
plt.bar(
    ["Rows", "Columns", "Numeric Features"],
    [len(df), len(df.columns), len(numeric_cols)]
)
save_chart("Dataset Overview", "dataset_overview")


# ==========================================
# CHART 2: MISSING VALUES
# ==========================================

plt.figure(figsize=(12, 6))
df.isnull().sum().plot(kind="bar")
plt.ylabel("Missing Values")
save_chart("Missing Values Analysis", "missing_values")


# ==========================================
# CHART 3: FACIES DISTRIBUTION
# ==========================================

if facies_col:
    plt.figure(figsize=(10, 6))
    sns.countplot(
        data=df,
        x=facies_col,
        order=df[facies_col].value_counts().index
    )
    plt.xticks(rotation=45)
    save_chart("Facies Distribution", "facies_distribution")
else:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[log_cols[0]], kde=True)
    save_chart("First Well Log Distribution", "log_distribution")


# ==========================================
# CHART 4-9: HISTOGRAMS
# ==========================================

for i in range(6):
    col = log_cols[i % len(log_cols)]

    plt.figure(figsize=(9, 5))
    sns.histplot(df[col], kde=True, bins=30)
    plt.xlabel(col)
    save_chart(
        f"Histogram of {col}",
        f"histogram_{i+1}"
    )


# ==========================================
# CHART 10-15: BOXPLOTS
# ==========================================

for i in range(6):
    col = log_cols[i % len(log_cols)]

    plt.figure(figsize=(9, 5))
    sns.boxplot(x=df[col])
    plt.xlabel(col)
    save_chart(
        f"Boxplot of {col}",
        f"boxplot_{i+1}"
    )


# ==========================================
# CHART 16-19: SCATTER PLOTS
# ==========================================

for i in range(4):
    x_col = log_cols[i % len(log_cols)]
    y_col = log_cols[(i + 1) % len(log_cols)]

    if x_col == y_col:
        plt.figure(figsize=(9, 5))
        sns.scatterplot(x=df[x_col], y=df[x_col])
    else:
        plt.figure(figsize=(9, 5))

        sns.scatterplot(
            data=df,
            x=x_col,
            y=y_col,
            hue=facies_col if facies_col else None,
            legend="auto" if facies_col else False
        )

    save_chart(
        f"Scatter Plot: {x_col} vs {y_col}",
        f"scatter_{i+1}"
    )


# ==========================================
# CHART 20: CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(12, 8))
sns.heatmap(
    df[numeric_cols].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
save_chart("Well Log Correlation Heatmap", "correlation_heatmap")


# ==========================================
# CHART 21: PAIR PLOT
# ==========================================

pair_cols = log_cols[:min(4, len(log_cols))]

if len(pair_cols) >= 2:
    pair_df = df[pair_cols].copy()

    if facies_col:
        pair_df[facies_col] = df[facies_col]

    pair = sns.pairplot(
        pair_df,
        hue=facies_col if facies_col else None,
        corner=True
    )

    pair.fig.suptitle("Well Log Pair Plot", y=1.02)
    pair.savefig(
        os.path.join(OUTPUT_DIR, "21_pairplot.png"),
        dpi=150
    )
    plt.show()
    plt.close()
else:
    plt.figure(figsize=(9, 5))
    sns.histplot(df[pair_cols[0]])
    save_chart("Pair Plot Alternative", "pairplot_alternative")

chart_number += 1
print("Chart 21/30: Pair Plot")


# ==========================================
# CHART 22: VIOLIN PLOT
# ==========================================

plt.figure(figsize=(12, 6))
sns.violinplot(data=df[log_cols[:min(5, len(log_cols))]])
plt.xticks(rotation=30)
save_chart("Well Log Violin Plot", "violin_plot")


# ==========================================
# CHART 23: FACIES VS WELL LOG
# ==========================================

plt.figure(figsize=(10, 6))

if facies_col:
    sns.boxplot(
        data=df,
        x=facies_col,
        y=log_cols[0]
    )
    plt.xticks(rotation=45)
else:
    sns.boxplot(data=df[log_cols[:min(5, len(log_cols))]])

save_chart("Facies vs Well Log", "facies_vs_log")


# ==========================================
# CHART 24: DEPTH PROFILE
# ==========================================

plt.figure(figsize=(8, 10))

if depth_col:
    plt.plot(df[log_cols[0]], df[depth_col])
    plt.gca().invert_yaxis()
    plt.ylabel(depth_col)
else:
    plt.plot(df[log_cols[0]])
    plt.ylabel("Sample Index")

plt.xlabel(log_cols[0])
save_chart("Well Log Depth Profile", "depth_profile")


# ==========================================
# CHART 25: MULTIPLE LOG PROFILE
# ==========================================

plt.figure(figsize=(10, 10))

if depth_col:
    for col in log_cols[:min(4, len(log_cols))]:
        plt.plot(df[col], df[depth_col], label=col)

    plt.gca().invert_yaxis()
    plt.legend()
    plt.xlabel("Log Measurements")
    plt.ylabel(depth_col)
else:
    for col in log_cols[:min(4, len(log_cols))]:
        plt.plot(df[col].values, label=col)

    plt.legend()
    plt.xlabel("Sample Index")

save_chart("Multiple Well Log Profiles", "multiple_log_profiles")


# ==========================================
# CHART 26: K-MEANS CLUSTERING
# ==========================================

features = log_cols[:]

X = df[features].copy()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

n_clusters = min(5, len(df))

if n_clusters < 2:
    raise ValueError("At least two samples are needed for clustering.")

kmeans = KMeans(
    n_clusters=n_clusters,
    random_state=42,
    n_init=10
)

df["Predicted_Facies"] = kmeans.fit_predict(X_scaled)

pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

plt.figure(figsize=(10, 7))
sns.scatterplot(
    x=X_pca[:, 0],
    y=X_pca[:, 1],
    hue=df["Predicted_Facies"],
    palette="viridis",
    s=60
)
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
save_chart("K-Means Facies Clustering", "kmeans_clustering")


# ==========================================
# CHART 27: CLUSTER DISTRIBUTION
# ==========================================

plt.figure(figsize=(9, 5))
sns.countplot(
    x=df["Predicted_Facies"],
    hue=df["Predicted_Facies"],
    legend=False
)
plt.xlabel("Predicted Cluster")
plt.ylabel("Sample Count")
save_chart("Predicted Facies Cluster Distribution", "cluster_distribution")


# ==========================================
# CHART 28: PCA EXPLAINED VARIANCE
# ==========================================

plt.figure(figsize=(9, 5))
plt.bar(
    ["PC1", "PC2"],
    pca.explained_variance_ratio_ * 100
)
plt.ylabel("Explained Variance (%)")
save_chart("PCA Explained Variance", "pca_variance")


# ==========================================
# CHART 29: ACTUAL VS PREDICTED FACIES
# ==========================================

plt.figure(figsize=(10, 6))

if facies_col:
    comparison = pd.crosstab(
        df[facies_col],
        df["Predicted_Facies"]
    )

    sns.heatmap(comparison, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Predicted Cluster")
    plt.ylabel("Actual Facies")
else:
    sns.countplot(
        data=df,
        x="Predicted_Facies",
        hue="Predicted_Facies",
        legend=False
    )
    plt.xlabel("Predicted Cluster")

save_chart("Actual vs Predicted Facies", "actual_predicted")


# ==========================================
# CHART 30: FEATURE IMPORTANCE PROXY
# ==========================================

# K-Means does not provide supervised feature importance.
# This chart shows standardized cluster-center separation.

center_spread = pd.Series(
    np.ptp(kmeans.cluster_centers_, axis=0),
    index=features
).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=center_spread.values,
    y=center_spread.index
)
plt.xlabel("Cluster Center Range (Standardized)")
save_chart("Feature Separation by Clustering", "feature_separation")


# ==========================================
# SAVE FINAL RESULTS
# ==========================================

df.to_csv(
    os.path.join(OUTPUT_DIR, "facies_analysis_results.csv"),
    index=False
)

df.describe().to_csv(
    os.path.join(OUTPUT_DIR, "statistical_summary.csv")
)

print("\n" + "=" * 60)
print("WELL LOG FACIES ANALYSIS COMPLETED")
print("=" * 60)

print("Total Charts Generated:", chart_number)
print("Output Folder:", OUTPUT_DIR)
print("Results CSV: facies_analysis_results.csv")
print("Statistical Summary: statistical_summary.csv")

print("\nAll 30 charts generated successfully!")
