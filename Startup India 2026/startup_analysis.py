
import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore")

# ==========================================
# 1. PROJECT CONFIGURATION
# ==========================================

BASE_DIR = r"C:\Users\USER PC\Desktop\Startup India 2026"

DATA_FILE = os.path.join(BASE_DIR, "startups.csv")

OUTPUT_DIR = os.path.join(BASE_DIR, "Startup_30_Charts")

os.makedirs(OUTPUT_DIR, exist_ok=True)

sns.set_theme(style="whitegrid", palette="viridis")

# ==========================================
# 2. LOAD DATASET
# ==========================================

print("=" * 60)
print("       STARTUP INDIA 2026 - DATA ANALYSIS")
print("=" * 60)

df = pd.read_csv(DATA_FILE)

print("\nDataset Loaded Successfully!")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nDataset Information:")
print(df.info())

print("\nFirst Five Records:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================================
# 3. DATA PREPROCESSING
# ==========================================

df.columns = df.columns.str.strip()

numeric_cols = df.select_dtypes(
    include=np.number
).columns.tolist()

categorical_cols = df.select_dtypes(
    include=["object", "category", "bool"]
).columns.tolist()

# Detect date columns
for col in categorical_cols.copy():
    converted = pd.to_datetime(df[col], errors="coerce")
    if converted.notna().mean() > 0.75:
        df[col] = converted
        categorical_cols.remove(col)

date_cols = df.select_dtypes(
    include=["datetime"]
).columns.tolist()

# Clean categorical values
for col in categorical_cols:
    df[col] = df[col].fillna("Unknown").astype(str)

# Clean numeric values
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Identify useful columns
def find_column(keywords, columns):
    for keyword in keywords:
        for col in columns:
            if keyword in col.lower():
                return col
    return None

industry_col = find_column(
    ["industry", "sector", "domain"],
    categorical_cols
)

city_col = find_column(
    ["city", "location", "district"],
    categorical_cols
)

state_col = find_column(
    ["state", "region"],
    categorical_cols
)

funding_col = find_column(
    ["funding", "investment", "raised", "amount"],
    numeric_cols
)

year_col = find_column(
    ["year", "founded"],
    numeric_cols
)

status_col = find_column(
    ["status", "stage", "startup_status"],
    categorical_cols
)

category_col = industry_col or (
    categorical_cols[0] if categorical_cols else None
)

numeric_col = funding_col or (
    numeric_cols[0] if numeric_cols else None
)

if not category_col:
    df["Category"] = "All Startups"
    category_col = "Category"

if not numeric_col:
    df["Record_Count"] = 1
    numeric_col = "Record_Count"

# ==========================================
# 4. CHART SAVING FUNCTION
# ==========================================

chart_count = 0

def save_chart(title, filename):
    global chart_count

    plt.title(title, fontsize=14, fontweight="bold")
    plt.tight_layout()

    chart_count += 1

    path = os.path.join(OUTPUT_DIR, filename)

    plt.savefig(path, dpi=300, bbox_inches="tight")

    plt.close()

    print(f"Chart {chart_count:02d}/30 saved: {filename}")


# ==========================================
# 5. CHART 1 - STARTUP DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x=numeric_col,
    bins=30,
    kde=True
)

save_chart(
    "Startup Numeric Distribution",
    "01_Startup_Distribution.png"
)

# ==========================================
# 6. CHART 2 - INDUSTRY DISTRIBUTION
# ==========================================

plt.figure(figsize=(12, 7))

df[category_col].value_counts().head(15).plot(
    kind="bar",
    edgecolor="black"
)

plt.xlabel(category_col)
plt.ylabel("Number of Startups")
plt.xticks(rotation=45, ha="right")

save_chart(
    "Startup Industry Distribution",
    "02_Industry_Distribution.png"
)

# ==========================================
# 7. CHART 3 - FUNDING DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))

sns.boxplot(data=df, y=numeric_col)

save_chart(
    "Startup Funding Distribution",
    "03_Funding_Distribution.png"
)

# ==========================================
# 8. CHART 4 - INDUSTRY PIE CHART
# ==========================================

plt.figure(figsize=(9, 9))

df[category_col].value_counts().head(10).plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.ylabel("")

save_chart(
    "Industry Percentage Distribution",
    "04_Industry_Pie_Chart.png"
)

# ==========================================
# 9. CHART 5 - TOP 10 INDUSTRIES
# ==========================================

plt.figure(figsize=(10, 6))

sns.barplot(
    x=df[category_col].value_counts().head(10).values,
    y=df[category_col].value_counts().head(10).index
)

save_chart(
    "Top 10 Startup Industries",
    "05_Top_10_Industries.png"
)

# ==========================================
# 10. CHART 6 - STARTUP STATUS
# ==========================================

plt.figure(figsize=(10, 6))

if status_col:
    sns.countplot(
        data=df,
        x=status_col,
        order=df[status_col].value_counts().index
    )
else:
    sns.countplot(data=df, x=category_col)

plt.xticks(rotation=45)

save_chart(
    "Startup Status Analysis",
    "06_Startup_Status.png"
)

# ==========================================
# 11. CHART 7 - STATE DISTRIBUTION
# ==========================================

plt.figure(figsize=(12, 6))

if state_col:
    df[state_col].value_counts().head(15).plot(kind="bar")
else:
    df[category_col].value_counts().head(15).plot(kind="bar")

plt.xticks(rotation=45)

save_chart(
    "Startup State Distribution",
    "07_State_Distribution.png"
)

# ==========================================
# 12. CHART 8 - CITY DISTRIBUTION
# ==========================================

plt.figure(figsize=(12, 6))

if city_col:
    df[city_col].value_counts().head(15).plot(kind="barh")
else:
    df[category_col].value_counts().head(15).plot(kind="barh")

save_chart(
    "Startup City Distribution",
    "08_City_Distribution.png"
)

# ==========================================
# 13. CHART 9 - FUNDING HISTOGRAM
# ==========================================

plt.figure(figsize=(10, 6))

sns.histplot(
    df[numeric_col].dropna(),
    bins=25,
    color="teal"
)

save_chart(
    "Startup Funding Histogram",
    "09_Funding_Histogram.png"
)

# ==========================================
# 14. CHART 10 - FUNDING KDE
# ==========================================

plt.figure(figsize=(10, 6))

sns.kdeplot(
    df[numeric_col].dropna(),
    fill=True
)

save_chart(
    "Funding Density Distribution",
    "10_Funding_KDE.png"
)

# ==========================================
# 15. CHART 11 - VIOLIN PLOT
# ==========================================

plt.figure(figsize=(10, 6))

sns.violinplot(
    data=df,
    y=numeric_col
)

save_chart(
    "Startup Numeric Violin Plot",
    "11_Violin_Plot.png"
)

# ==========================================
# 16. CHART 12 - STRIP PLOT
# ==========================================

plt.figure(figsize=(10, 6))

sns.stripplot(
    data=df.sample(min(len(df), 1000)),
    y=numeric_col,
    jitter=True
)

save_chart(
    "Startup Numeric Strip Plot",
    "12_Strip_Plot.png"
)

# ==========================================
# 17. CHART 13 - SWARM PLOT
# ==========================================

plt.figure(figsize=(10, 6))

sns.swarmplot(
    data=df.sample(min(len(df), 300)),
    y=numeric_col,
    size=3
)

save_chart(
    "Startup Numeric Swarm Plot",
    "13_Swarm_Plot.png"
)

# ==========================================
# 18. CHART 14 - ECDF PLOT
# ==========================================

plt.figure(figsize=(10, 6))

sns.ecdfplot(data=df, x=numeric_col)

save_chart(
    "Startup ECDF Distribution",
    "14_ECDF_Plot.png"
)

# ==========================================
# 19. CHART 15 - CUMULATIVE DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))

values = df[numeric_col].dropna().sort_values()

plt.plot(
    values,
    np.arange(1, len(values) + 1) / len(values)
)

plt.xlabel(numeric_col)
plt.ylabel("Cumulative Probability")

save_chart(
    "Cumulative Startup Distribution",
    "15_Cumulative_Distribution.png"
)

# ==========================================
# 20. CHART 16 - TOP INDUSTRY FUNDING
# ==========================================

plt.figure(figsize=(12, 6))

if industry_col and funding_col:
    temp = df.groupby(industry_col)[funding_col].mean()
    temp.nlargest(10).sort_values().plot(kind="barh")
else:
    df[numeric_col].nlargest(10).plot(kind="bar")

save_chart(
    "Average Funding by Industry",
    "16_Industry_Funding.png"
)

# ==========================================
# 21. CHART 17 - INDUSTRY COUNT AREA
# ==========================================

plt.figure(figsize=(10, 6))

df[category_col].value_counts().head(15).sort_values().plot(
    kind="area",
    alpha=0.6
)

save_chart(
    "Industry Area Distribution",
    "17_Industry_Area.png"
)

# ==========================================
# 22. CHART 18 - FUNDING LINE CHART
# ==========================================

plt.figure(figsize=(10, 6))

df[numeric_col].reset_index(drop=True).plot(
    kind="line"
)

plt.xlabel("Record Number")

save_chart(
    "Startup Funding Trend by Record",
    "18_Funding_Line.png"
)

# ==========================================
# 23. CHART 19 - FUNDING SCATTER
# ==========================================

plt.figure(figsize=(10, 6))

plt.scatter(
    range(len(df)),
    df[numeric_col],
    alpha=0.5
)

plt.xlabel("Startup Record")
plt.ylabel(numeric_col)

save_chart(
    "Startup Funding Scatter Plot",
    "19_Funding_Scatter.png"
)

# ==========================================
# 24. CHART 20 - NUMERIC COLUMN PAIR PLOT
# ==========================================

if len(numeric_cols) >= 2:
    sample_cols = numeric_cols[:5]

    sns.pairplot(
        df[sample_cols].dropna().sample(
            min(len(df.dropna(subset=sample_cols)), 500)
        ) if len(df.dropna(subset=sample_cols)) else df[sample_cols].dropna()
    )

    chart_count += 1
    plt.savefig(
        os.path.join(OUTPUT_DIR, "20_Pair_Plot.png"),
        dpi=300
    )
    plt.close()
    print("Chart 20/30 saved: 20_Pair_Plot.png")
else:
    plt.figure(figsize=(8, 5))
    sns.histplot(df[numeric_col].dropna())
    save_chart("Pair Plot Alternative", "20_Pair_Plot.png")

# ==========================================
# 25. CHART 21 - REGRESSION PLOT
# ==========================================

plt.figure(figsize=(10, 6))

if len(numeric_cols) >= 2:
    sns.regplot(
        data=df,
        x=numeric_cols[0],
        y=numeric_cols[1],
        scatter_kws={"alpha": 0.5}
    )
else:
    sns.regplot(
        x=np.arange(len(df)),
        y=df[numeric_col]
    )

save_chart(
    "Startup Regression Analysis",
    "21_Regression_Plot.png"
)

# ==========================================
# 26. CHART 22 - HEXBIN PLOT
# ==========================================

plt.figure(figsize=(10, 6))

if len(numeric_cols) >= 2:
    plt.hexbin(
        df[numeric_cols[0]],
        df[numeric_cols[1]],
        gridsize=25,
        cmap="viridis"
    )
    plt.colorbar(label="Record Density")
else:
    plt.hexbin(
        range(len(df)),
        df[numeric_col],
        gridsize=25
    )
    plt.colorbar()

save_chart(
    "Startup Hexbin Density",
    "22_Hexbin_Plot.png"
)

# ==========================================
# 27. CHART 23 - CATEGORY BOXPLOT
# ==========================================

plt.figure(figsize=(12, 6))

sns.boxplot(
    data=df,
    x=category_col,
    y=numeric_col,
    showfliers=False
)

plt.xticks(rotation=45, ha="right")

save_chart(
    "Industry-wise Numeric Comparison",
    "23_Category_Boxplot.png"
)

# ==========================================
# 28. CHART 24 - CATEGORY SWARM ALTERNATIVE
# ==========================================

plt.figure(figsize=(12, 6))

top_categories = df[category_col].value_counts().head(8).index

sns.stripplot(
    data=df[df[category_col].isin(top_categories)].sample(
        min(len(df[df[category_col].isin(top_categories)]), 500)
    ),
    x=category_col,
    y=numeric_col,
    jitter=True
)

plt.xticks(rotation=45)

save_chart(
    "Industry-wise Numeric Strip Comparison",
    "24_Category_Strip.png"
)

# ==========================================
# 29. CHART 25 - CATEGORY BAR DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))

sns.countplot(
    data=df,
    x=category_col,
    order=df[category_col].value_counts().head(10).index
)

plt.xticks(rotation=45)

save_chart(
    "Startup Category Count",
    "25_Category_Count.png"
)

# ==========================================
# 30. CHART 26 - CATEGORY FUNDING VIOLIN
# ==========================================

plt.figure(figsize=(12, 6))

sns.violinplot(
    data=df[df[category_col].isin(
        df[category_col].value_counts().head(8).index
    )],
    x=category_col,
    y=numeric_col,
    cut=0
)

plt.xticks(rotation=45)

save_chart(
    "Industry Funding Violin Analysis",
    "26_Category_Violin.png"
)

# ==========================================
# 31. CHART 27 - STARTUP YEAR DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 6))

if year_col:
    df[year_col].value_counts().sort_index().plot(
        kind="line",
        marker="o"
    )
else:
    df[numeric_col].plot(kind="line")

save_chart(
    "Startup Establishment Year Analysis",
    "27_Year_Analysis.png"
)

# ==========================================
# 32. CHART 28 - MONTHLY TREND
# ==========================================

plt.figure(figsize=(10, 6))

if date_cols:
    months = df[date_cols[0]].dt.month.value_counts().sort_index()
    months.plot(kind="bar")
    plt.xlabel("Month")
else:
    df[category_col].value_counts().head(12).plot(kind="bar")
    plt.xlabel(category_col)

save_chart(
    "Startup Monthly Distribution",
    "28_Monthly_Trend.png"
)

# ==========================================
# 33. CHART 29 - NUMERIC CORRELATION
# ==========================================

plt.figure(figsize=(12, 8))

if len(numeric_cols) >= 2:
    corr = df[numeric_cols].corr()
    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )
else:
    sns.histplot(df[numeric_col].dropna())

save_chart(
    "Startup Numeric Correlation",
    "29_Correlation_Analysis.png"
)

# ==========================================
# 34. CHART 30 - FINAL CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(12, 8))

if len(numeric_cols) >= 2:
    sns.heatmap(
        df[numeric_cols].corr(),
        cmap="Spectral",
        annot=True,
        linewidths=0.5
    )
else:
    sns.histplot(df[numeric_col].dropna(), kde=True)

save_chart(
    "Startup Correlation Heatmap",
    "30_Correlation_Heatmap.png"
)

# ==========================================
# 35. FINAL SUMMARY
# ==========================================

print("\n" + "=" * 60)
print("          STARTUP INDIA 2026 ANALYSIS")
print("=" * 60)

print("Total Startups:", len(df))
print("Total Columns:", len(df.columns))
print("Numerical Columns:", len(numeric_cols))
print("Categorical Columns:", len(categorical_cols))
print("Charts Generated:", chart_count)

print("\nCharts Saved Successfully!")
print("Output Folder:", OUTPUT_DIR)

print("\nTOP INDUSTRIES:")

print(df[category_col].value_counts().head(10))

print("\nNUMERICAL SUMMARY:")

print(df[numeric_col].describe())

print("\nPROJECT COMPLETED SUCCESSFULLY!")

