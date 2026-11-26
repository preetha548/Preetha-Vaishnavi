
# ============================================
# GLOBAL HISTORICAL HOLIDAYS - DATA ANALYSIS
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# Set visualization style
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (12, 6)

# ============================================
# 1. LOAD DATASET
# ============================================

file_path = r"C:\Users\USER PC\Desktop\Global Historical Holidays\holidays.csv"

df = pd.read_csv(file_path)

print("DATASET LOADED SUCCESSFULLY")
print("=" * 50)

# ============================================
# 2. DATASET OVERVIEW
# ============================================

print("\nFirst 5 Records:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe(include="all"))

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

# ============================================
# 3. DATA CLEANING
# ============================================

df = df.drop_duplicates()

# Remove completely empty rows
df = df.dropna(how="all")

print("\nCleaned Dataset Shape:", df.shape)

# ============================================
# 4. AUTOMATIC COLUMN DETECTION
# ============================================

country_col = next(
    (c for c in df.columns if c.lower() in
     ["country", "country_name", "nation"]),
    None
)

date_col = next(
    (c for c in df.columns if c.lower() in
     ["date", "holiday_date", "day"]),
    None
)

holiday_col = next(
    (c for c in df.columns if c.lower() in
     ["holiday", "holiday_name", "name", "event"]),
    None
)

year_col = next(
    (c for c in df.columns if c.lower() == "year"),
    None
)

# Extract year from date if necessary
if year_col is None and date_col is not None:
    df[date_col] = pd.to_datetime(
        df[date_col], errors="coerce"
    )
    df["Year"] = df[date_col].dt.year
    year_col = "Year"

# ============================================
# 5. TOP COUNTRIES BY HOLIDAY COUNT
# ============================================

if country_col:

    country_counts = df[country_col].value_counts().head(15)

    plt.figure(figsize=(12, 7))

    sns.barplot(
        x=country_counts.values,
        y=country_counts.index,
        hue=country_counts.index,
        palette="viridis",
        legend=False
    )

    plt.title("Top 15 Countries by Number of Holidays")
    plt.xlabel("Number of Holidays")
    plt.ylabel("Country")
    plt.tight_layout()
    plt.savefig("01_country_holidays.png", dpi=300)
    plt.show()

# ============================================
# 6. HOLIDAYS BY YEAR
# ============================================

if year_col:

    yearly_counts = df[year_col].value_counts().sort_index()

    plt.figure(figsize=(14, 6))

    plt.plot(
        yearly_counts.index,
        yearly_counts.values,
        marker="o",
        color="darkblue",
        linewidth=2
    )

    plt.title("Historical Holiday Distribution by Year")
    plt.xlabel("Year")
    plt.ylabel("Number of Holidays")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("02_holidays_by_year.png", dpi=300)
    plt.show()

# ============================================
# 7. TOP 10 MOST COMMON HOLIDAYS
# ============================================

if holiday_col:

    holiday_counts = df[holiday_col].value_counts().head(10)

    plt.figure(figsize=(12, 6))

    sns.barplot(
        x=holiday_counts.values,
        y=holiday_counts.index,
        hue=holiday_counts.index,
        palette="magma",
        legend=False
    )

    plt.title("Top 10 Most Common Holidays Worldwide")
    plt.xlabel("Frequency")
    plt.ylabel("Holiday Name")
    plt.tight_layout()
    plt.savefig("03_top_holidays.png", dpi=300)
    plt.show()

# ============================================
# 8. HOLIDAY DISTRIBUTION BY MONTH
# ============================================

if date_col:

    df["Month"] = df[date_col].dt.month

    month_counts = (
        df["Month"]
        .value_counts()
        .sort_index()
        .reindex(range(1, 13), fill_value=0)
    )

    month_names = [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ]

    plt.figure(figsize=(12, 6))

    sns.barplot(
        x=month_names,
        y=month_counts.values,
        hue=month_names,
        palette="coolwarm",
        legend=False
    )

    plt.title("Holiday Distribution by Month")
    plt.xlabel("Month")
    plt.ylabel("Number of Holidays")
    plt.tight_layout()
    plt.savefig("04_monthly_distribution.png", dpi=300)
    plt.show()

# ============================================
# 9. CORRELATION HEATMAP
# ============================================

numeric_df = df.select_dtypes(include=np.number)

if numeric_df.shape[1] >= 2:

    plt.figure(figsize=(10, 6))

    sns.heatmap(
        numeric_df.corr(),
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )

    plt.title("Correlation Heatmap")
    plt.tight_layout()
    plt.savefig("05_correlation_heatmap.png", dpi=300)
    plt.show()

# ============================================
# 10. INTERACTIVE COUNTRY CHART
# ============================================

if country_col:

    fig = px.bar(
        df[country_col].value_counts().head(20).reset_index(),
        x="count",
        y=country_col,
        orientation="h",
        title="Interactive Global Holiday Distribution",
        color="count",
        color_continuous_scale="Viridis"
    )

    fig.update_layout(
        yaxis={"categoryorder": "total ascending"}
    )

    fig.write_html("06_interactive_holiday_chart.html")
    fig.show()

# ============================================
# 11. SAVE CLEANED DATASET
# ============================================

df.to_csv("cleaned_global_holidays.csv", index=False)

print("\n" + "=" * 50)
print("DATA ANALYSIS COMPLETED SUCCESSFULLY!")
print("Visualization files saved in:", os.getcwd())
print("=" * 50)
