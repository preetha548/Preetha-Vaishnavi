
import os
import pandas as pd
import numpy as np
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns

# =====================================
# FILE CONFIGURATION
# =====================================

FILE_PATH = r"C:\Users\USER PC\Desktop\Resume Screening\resume_dataset_200k_enhanced.csv"

OUTPUT = r"C:\Users\USER PC\Desktop\Resume Screening\Visualizations"

os.makedirs(OUTPUT, exist_ok=True)

sns.set_theme(style="whitegrid")

# =====================================
# LOAD DATASET
# =====================================

df = pd.read_csv(FILE_PATH, low_memory=False)

print("Dataset loaded:", df.shape)
print("Columns:", df.columns.tolist())

# =====================================
# AUTOMATIC COLUMN DETECTION
# =====================================

numeric_cols = df.select_dtypes(
    include=np.number
).columns.tolist()

categorical_cols = df.select_dtypes(
    exclude=np.number
).columns.tolist()

print("Numeric:", numeric_cols)
print("Categorical:", categorical_cols)

# =====================================
# CHART FUNCTION
# =====================================

chart_no = 0

def save_chart(title):

    global chart_no

    chart_no += 1

    plt.title(title, fontsize=14, fontweight="bold")
    plt.tight_layout()

    plt.savefig(
        os.path.join(
            OUTPUT,
            f"Chart_{chart_no:02d}.png"
        ),
        dpi=130,
        bbox_inches="tight"
    )

    plt.close()

    print("Created:", title)


def bar_chart(column, title):

    plt.figure(figsize=(10, 5))

    values = df[column].value_counts().head(20)

    sns.barplot(
        x=values.values,
        y=values.index.astype(str)
    )

    save_chart(title)


def histogram(column, title):

    plt.figure(figsize=(10, 5))

    values = pd.to_numeric(
        df[column], errors="coerce"
    ).dropna()

    if len(values) == 0:
        plt.text(0.5, 0.5, "No numeric values",
                 ha="center")
    else:
        sns.histplot(values, bins=30, kde=True)

    save_chart(title)


def unavailable(title):

    plt.figure(figsize=(10, 5))
    plt.text(
        0.5, 0.5,
        "Required data unavailable",
        ha="center",
        va="center"
    )
    plt.axis("off")
    save_chart(title)


# =====================================
# 1-10: GENERAL DATA VISUALIZATION
# =====================================

# 1 Dataset row distribution
plt.figure(figsize=(8, 5))
plt.bar(
    ["Records"],
    [len(df)],
    color="steelblue"
)
save_chart("Total Resume Records")

# 2 Numeric columns distribution
if numeric_cols:
    histogram(numeric_cols[0], "First Numeric Feature Distribution")
else:
    unavailable("First Numeric Feature Distribution")

# 3 Category distribution
if categorical_cols:
    bar_chart(categorical_cols[0], "Category Distribution")
else:
    unavailable("Category Distribution")

# 4 Missing values
plt.figure(figsize=(12, 5))
missing = df.isnull().sum().sort_values(
    ascending=False
).head(20)

sns.barplot(
    x=missing.values,
    y=missing.index.astype(str)
)
save_chart("Missing Values Analysis")

# 5 Numeric correlation
if len(numeric_cols) >= 2:
    plt.figure(figsize=(12, 8))
    sns.heatmap(
        df[numeric_cols].corr(),
        cmap="coolwarm"
    )
    save_chart("Numeric Feature Correlation")
else:
    unavailable("Numeric Feature Correlation")

# 6 First numeric feature boxplot
if numeric_cols:
    plt.figure(figsize=(10, 5))
    sns.boxplot(x=pd.to_numeric(
        df[numeric_cols[0]], errors="coerce"
    ))
    save_chart("Numeric Feature Boxplot")
else:
    unavailable("Numeric Feature Boxplot")

# 7 Second numeric feature
if len(numeric_cols) > 1:
    histogram(numeric_cols[1], "Second Numeric Feature Distribution")
else:
    unavailable("Second Numeric Feature Distribution")

# 8 Third numeric feature
if len(numeric_cols) > 2:
    histogram(numeric_cols[2], "Third Numeric Feature Distribution")
else:
    unavailable("Third Numeric Feature Distribution")

# 9 Categorical distribution
if len(categorical_cols) > 1:
    bar_chart(categorical_cols[1], "Second Category Distribution")
else:
    unavailable("Second Category Distribution")

# 10 Fourth numeric feature
if len(numeric_cols) > 3:
    histogram(numeric_cols[3], "Fourth Numeric Feature Distribution")
else:
    unavailable("Fourth Numeric Feature Distribution")


# =====================================
# 11-20: FEATURE ANALYSIS
# =====================================

# 11-15 numeric feature histograms
for i in range(5):
    if i < len(numeric_cols):
        histogram(
            numeric_cols[i],
            f"Numeric Feature {i+1} Analysis"
        )
    else:
        unavailable(f"Numeric Feature {i+1} Analysis")

# 16-18 categorical charts
for i in range(3):
    if i < len(categorical_cols):
        bar_chart(
            categorical_cols[i],
            f"Categorical Feature {i+1} Analysis"
        )
    else:
        unavailable(f"Categorical Feature {i+1} Analysis")

# 19 Numeric correlation heatmap
if len(numeric_cols) >= 2:
    plt.figure(figsize=(12, 8))
    sns.heatmap(
        df[numeric_cols].corr(),
        annot=False,
        cmap="viridis"
    )
    save_chart("Feature Correlation Heatmap")
else:
    unavailable("Feature Correlation Heatmap")

# 20 Pairplot of first four numeric features
if len(numeric_cols) >= 2:
    sample_cols = numeric_cols[:4]

    sample = df[sample_cols].sample(
        min(500, len(df)),
        random_state=42
    )

    sns.pairplot(sample)
    plt.savefig(
        os.path.join(OUTPUT, "Chart_20.png"),
        dpi=120
    )
    plt.close()

    chart_no += 1
    print("Created: Numeric Pairplot")
else:
    unavailable("Numeric Pairplot")


# =====================================
# 21-30: ADVANCED VISUALIZATION
# =====================================

# 21 Scatter plot
if len(numeric_cols) >= 2:
    plt.figure(figsize=(10, 5))

    sns.scatterplot(
        data=df.sample(min(3000, len(df)), random_state=42),
        x=numeric_cols[0],
        y=numeric_cols[1],
        alpha=0.5
    )

    save_chart("Feature Relationship Scatterplot")
else:
    unavailable("Feature Relationship Scatterplot")

# 22 Violin plot
if numeric_cols and categorical_cols:
    plt.figure(figsize=(12, 6))

    temp = df[[categorical_cols[0], numeric_cols[0]]].copy()
    temp[numeric_cols[0]] = pd.to_numeric(
        temp[numeric_cols[0]], errors="coerce"
    )
    temp = temp.dropna()

    top_categories = temp[categorical_cols[0]].value_counts().head(10).index
    temp = temp[temp[categorical_cols[0]].isin(top_categories)]

    sns.violinplot(
        data=temp,
        x=categorical_cols[0],
        y=numeric_cols[0]
    )

    plt.xticks(rotation=45)
    save_chart("Category Violin Plot")
else:
    unavailable("Category Violin Plot")

# 23 KDE plot
if numeric_cols:
    plt.figure(figsize=(10, 5))

    sns.kdeplot(
        pd.to_numeric(df[numeric_cols[0]], errors="coerce").dropna(),
        fill=True
    )

    save_chart("Feature Density Distribution")
else:
    unavailable("Feature Density Distribution")

# 24 Pie chart
if categorical_cols:
    plt.figure(figsize=(8, 8))

    df[categorical_cols[0]].value_counts().head(10).plot(
        kind="pie",
        autopct="%1.1f%%"
    )

    plt.ylabel("")
    save_chart("Category Percentage Distribution")
else:
    unavailable("Category Percentage Distribution")

# 25 Count plot
if categorical_cols:
    plt.figure(figsize=(12, 5))

    sns.countplot(
        data=df,
        y=categorical_cols[0],
        order=df[categorical_cols[0]].value_counts().head(15).index
    )

    save_chart("Category Count Plot")
else:
    unavailable("Category Count Plot")

# 26 Area chart
if numeric_cols:
    plt.figure(figsize=(10, 5))

    values = pd.to_numeric(
        df[numeric_cols[0]], errors="coerce"
    ).dropna().head(1000)

    plt.fill_between(
        range(len(values)),
        values,
        alpha=0.4,
        color="green"
    )

    save_chart("Feature Area Chart")
else:
    unavailable("Feature Area Chart")

# 27 Numeric feature boxplots
if numeric_cols:
    plt.figure(figsize=(12, 6))

    sample = df[numeric_cols[:10]].apply(
        pd.to_numeric, errors="coerce"
    )

    sns.boxplot(data=sample)
    plt.xticks(rotation=45)

    save_chart("Multiple Feature Boxplots")
else:
    unavailable("Multiple Feature Boxplots")

# 28 Categorical stacked chart
if len(categorical_cols) >= 2:
    cross = pd.crosstab(
        df[categorical_cols[0]],
        df[categorical_cols[1]]
    )

    cross = cross.head(10).iloc[:, :8]

    cross.plot(
        kind="bar",
        stacked=True,
        figsize=(12, 6)
    )

    save_chart("Categorical Stacked Bar Chart")
else:
    unavailable("Categorical Stacked Bar Chart")

# 29 Correlation bar chart
if len(numeric_cols) >= 2:
    corr = df[numeric_cols].corr()

    values = corr.abs().mean().sort_values(
        ascending=False
    ).head(15)

    plt.figure(figsize=(10, 5))

    sns.barplot(
        x=values.values,
        y=values.index.astype(str)
    )

    save_chart("Feature Correlation Ranking")
else:
    unavailable("Feature Correlation Ranking")

# 30 Missing value heatmap
plt.figure(figsize=(12, 6))

sns.heatmap(
    df.sample(min(500, len(df)), random_state=42).isnull(),
    cbar=False
)

save_chart("Missing Data Heatmap")


# =====================================
# EXPORT DATA
# =====================================

df.describe(include="all").to_csv(
    os.path.join(OUTPUT, "Dataset_Summary.csv")
)

print("\n=================================")
print("30 VISUALIZATIONS COMPLETED")
print("Charts created:", chart_no)
print("Saved location:", OUTPUT)
print("=================================")

