import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore")

# ==========================================
# 1. LOAD DATASET
# ==========================================

file_path = r"C:\Users\USER PC\Desktop\Fish\fish.csv"

df = pd.read_csv(file_path)

print("\n========== FISH DATASET ANALYSIS ==========")
print("\nFirst Five Records:")
print(df.head())

print("\nDataset Shape:", df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe(include="all"))

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================================
# 2. DATA CLEANING
# ==========================================

df.columns = df.columns.str.strip()

for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include="object").columns:
    if df[col].isnull().any():
        df[col] = df[col].fillna(
            df[col].mode().iloc[0]
            if not df[col].mode().empty else "Unknown"
        )

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
categorical_cols = df.select_dtypes(
    include=["object", "category", "bool"]
).columns.tolist()

if not numeric_cols:
    raise ValueError("The dataset must contain at least one numeric column.")

# ==========================================
# 3. OUTPUT FOLDER
# ==========================================

output_dir = os.path.join(
    os.path.dirname(file_path), "Fish_30_Charts"
)

os.makedirs(output_dir, exist_ok=True)

sns.set_theme(style="whitegrid", palette="viridis")

chart_count = 0

def save_chart(title):
    global chart_count

    chart_count += 1
    plt.title(title, fontsize=14, fontweight="bold")
    plt.tight_layout()

    plt.savefig(
        os.path.join(output_dir, f"Chart_{chart_count:02d}.png"),
        dpi=300,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()


# ==========================================
# CHART 1 - Fish Category Count
# ==========================================

if categorical_cols:
    col = categorical_cols[0]
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=col, order=df[col].value_counts().index)
    plt.xticks(rotation=45)
    save_chart("1. Fish Category Distribution")

# ==========================================
# CHART 2 - First Numerical Column Histogram
# ==========================================

col = numeric_cols[0]

plt.figure(figsize=(9, 6))
sns.histplot(df[col], kde=True, bins=20)
save_chart("2. Numerical Data Distribution")

# ==========================================
# CHART 3 - Density Plot
# ==========================================

plt.figure(figsize=(9, 6))
sns.kdeplot(data=df, x=col, fill=True)
save_chart("3. Fish Data Density Plot")

# ==========================================
# CHART 4 - Box Plot
# ==========================================

plt.figure(figsize=(9, 6))
sns.boxplot(y=df[col])
save_chart("4. Numerical Feature Box Plot")

# ==========================================
# CHART 5 - Violin Plot
# ==========================================

plt.figure(figsize=(9, 6))
sns.violinplot(y=df[col])
save_chart("5. Violin Distribution Plot")

# ==========================================
# CHART 6 - Strip Plot
# ==========================================

plt.figure(figsize=(9, 6))
sns.stripplot(y=df[col], jitter=True)
save_chart("6. Strip Plot")

# ==========================================
# CHART 7 - Swarm Plot
# ==========================================

plt.figure(figsize=(9, 6))
sample = df[[col]].dropna().head(500)
sns.swarmplot(data=sample, y=col, size=3)
save_chart("7. Swarm Plot")

# ==========================================
# CHART 8 - Bar Chart
# ==========================================

plt.figure(figsize=(10, 6))
df[col].value_counts().head(15).plot(kind="bar")
save_chart("8. Numerical Value Frequency")

# ==========================================
# CHART 9 - Pie Chart
# ==========================================

if categorical_cols:
    cat = categorical_cols[0]
    plt.figure(figsize=(8, 8))
    df[cat].value_counts().head(10).plot(
        kind="pie", autopct="%1.1f%%"
    )
    plt.ylabel("")
    save_chart("9. Fish Category Percentage")

# ==========================================
# CHART 10 - Line Chart
# ==========================================

plt.figure(figsize=(10, 6))
plt.plot(df[col].reset_index(drop=True), marker="o")
save_chart("10. Numerical Trend Line")

# ==========================================
# CHART 11 - Area Chart
# ==========================================

plt.figure(figsize=(10, 6))
df[col].reset_index(drop=True).plot(kind="area", alpha=0.5)
save_chart("11. Area Chart")

# ==========================================
# CHART 12 - Scatter Plot
# ==========================================

if len(numeric_cols) >= 2:
    x, y = numeric_cols[:2]
    plt.figure(figsize=(9, 6))
    sns.scatterplot(data=df, x=x, y=y)
    save_chart("12. Fish Feature Scatter Plot")

# ==========================================
# CHART 13 - Regression Plot
# ==========================================

if len(numeric_cols) >= 2:
    plt.figure(figsize=(9, 6))
    sns.regplot(data=df, x=x, y=y)
    save_chart("13. Regression Analysis")

# ==========================================
# CHART 14 - Hexbin Plot
# ==========================================

if len(numeric_cols) >= 2:
    plt.figure(figsize=(9, 6))
    plt.hexbin(df[x], df[y], gridsize=25, cmap="viridis")
    plt.colorbar(label="Observations")
    plt.xlabel(x)
    plt.ylabel(y)
    save_chart("14. Hexbin Distribution")

# ==========================================
# CHART 15 - 2D KDE Plot
# ==========================================

if len(numeric_cols) >= 2:
    plt.figure(figsize=(9, 6))
    sns.kdeplot(data=df, x=x, y=y, fill=True)
    save_chart("15. Two Dimensional KDE")

# ==========================================
# CHART 16 - Correlation Heatmap
# ==========================================

if len(numeric_cols) >= 2:
    plt.figure(figsize=(11, 8))
    sns.heatmap(
        df[numeric_cols].corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )
    save_chart("16. Correlation Heatmap")

# ==========================================
# CHART 17 - Pair Plot
# ==========================================

if len(numeric_cols) >= 2:
    pair_data = df[numeric_cols[:5]].dropna().head(500)
    if len(pair_data.columns) >= 2:
        g = sns.pairplot(pair_data)
        g.fig.suptitle("17. Pairwise Feature Relationships", y=1.02)
        g.savefig(
            os.path.join(output_dir, "Chart_17.png"),
            dpi=300
        )
        plt.show()
        plt.close(g.fig)
        chart_count += 1

# ==========================================
# CHART 18 - Joint Plot
# ==========================================

if len(numeric_cols) >= 2:
    g = sns.jointplot(data=df, x=x, y=y, kind="scatter")
    g.fig.suptitle("18. Joint Distribution Plot", y=1.02)
    g.savefig(os.path.join(output_dir, "Chart_18.png"), dpi=300)
    plt.show()
    plt.close(g.fig)
    chart_count += 1

# ==========================================
# CHART 19 - Categorical Bar Plot
# ==========================================

if categorical_cols:
    cat = categorical_cols[0]
    plt.figure(figsize=(10, 6))
    sns.barplot(
        x=df[cat].value_counts().index.astype(str),
        y=df[cat].value_counts().values
    )
    plt.xticks(rotation=45)
    save_chart("19. Category Comparison")

# ==========================================
# CHART 20 - Categorical and Numerical Box Plot
# ==========================================

if categorical_cols:
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=df, x=categorical_cols[0], y=numeric_cols[0])
    plt.xticks(rotation=45)
    save_chart("20. Category Wise Numerical Distribution")

# ==========================================
# CHART 21 - Categorical Violin Plot
# ==========================================

if categorical_cols:
    plt.figure(figsize=(10, 6))
    sns.violinplot(data=df, x=categorical_cols[0], y=numeric_cols[0])
    plt.xticks(rotation=45)
    save_chart("21. Category Wise Violin Plot")

# ==========================================
# CHART 22 - Categorical Strip Plot
# ==========================================

if categorical_cols:
    plt.figure(figsize=(10, 6))
    sns.stripplot(
        data=df, x=categorical_cols[0],
        y=numeric_cols[0], jitter=True
    )
    plt.xticks(rotation=45)
    save_chart("22. Category Wise Strip Plot")

# ==========================================
# CHART 23 - Stacked Bar Chart
# ==========================================

if len(categorical_cols) >= 2:
    cross = pd.crosstab(
        df[categorical_cols[0]],
        df[categorical_cols[1]]
    )
    cross.plot(kind="bar", stacked=True, figsize=(10, 6))
    plt.xticks(rotation=45)
    save_chart("23. Stacked Category Comparison")

# ==========================================
# CHART 24 - Count Plot
# ==========================================

if categorical_cols:
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=categorical_cols[0], hue=categorical_cols[0],
                  legend=False)
    plt.xticks(rotation=45)
    save_chart("24. Category Count Comparison")

# ==========================================
# CHART 25 - ECDF Plot
# ==========================================

plt.figure(figsize=(9, 6))
sns.ecdfplot(data=df, x=numeric_cols[0])
save_chart("25. Empirical Cumulative Distribution")

# ==========================================
# CHART 26 - Rug Plot
# ==========================================

plt.figure(figsize=(9, 6))
sns.rugplot(data=df, x=numeric_cols[0])
save_chart("26. Rug Distribution Plot")

# ==========================================
# CHART 27 - Step Histogram
# ==========================================

plt.figure(figsize=(9, 6))
plt.hist(df[numeric_cols[0]], bins=20, histtype="step", linewidth=2)
save_chart("27. Step Histogram")

# ==========================================
# CHART 28 - Horizontal Bar Chart
# ==========================================

plt.figure(figsize=(10, 6))
df[numeric_cols[0]].value_counts().head(15).sort_values().plot(
    kind="barh"
)
save_chart("28. Horizontal Bar Chart")

# ==========================================
# CHART 29 - Bubble Chart
# ==========================================

if len(numeric_cols) >= 3:
    plt.figure(figsize=(10, 6))
    plt.scatter(
        df[numeric_cols[0]],
        df[numeric_cols[1]],
        s=np.clip(df[numeric_cols[2]].abs(), 1, None) * 5,
        alpha=0.5
    )
    plt.xlabel(numeric_cols[0])
    plt.ylabel(numeric_cols[1])
    save_chart("29. Bubble Relationship Chart")
else:
    plt.figure(figsize=(10, 6))
    plt.scatter(
        df.index, df[numeric_cols[0]],
        s=60, alpha=0.6
    )
    plt.xlabel("Record Index")
    plt.ylabel(numeric_cols[0])
    save_chart("29. Bubble Relationship Chart")

# ==========================================
# CHART 30 - Missing Values Heatmap
# ==========================================

original_df = pd.read_csv(file_path)

plt.figure(figsize=(12, 6))
sns.heatmap(
    original_df.isnull(),
    cbar=False,
    cmap="viridis"
)
save_chart("30. Missing Values Analysis")

# ==========================================
# FINAL REPORT
# ==========================================

print("\n====================================")
print("FISH DATASET ANALYSIS COMPLETED")
print("====================================")
print("Total Charts Generated:", chart_count)
print("Output Folder:", output_dir)
print("Dataset Rows:", len(df))
print("Dataset Columns:", len(df.columns))

print("\nAll available charts are saved successfully.")
