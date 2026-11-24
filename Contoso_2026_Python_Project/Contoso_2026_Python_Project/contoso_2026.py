import os
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore")
sns.set_theme(style="whitegrid")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "Contoso_Output")
CHART_DIR = os.path.join(OUTPUT_DIR, "Charts")
os.makedirs(CHART_DIR, exist_ok=True)

GEO_FILE = os.path.join(BASE_DIR, "Geography.xlsx")
STORE_FILE = os.path.join(BASE_DIR, "Stores.xlsx")

print("=" * 65)
print("CONTOSO GEOGRAPHY + STORES ANALYSIS (2026 PROJECT)")
print("Excel/Python only - NO Microsoft Access required")
print("=" * 65)

# 1. Read the provided Excel workbooks
if not os.path.exists(GEO_FILE) or not os.path.exists(STORE_FILE):
    raise FileNotFoundError(
        "Place Geography.xlsx and Stores.xlsx beside this Python script."
    )

geo_book = pd.ExcelFile(GEO_FILE)
geo_sheet = "COMPLETED" if "COMPLETED" in geo_book.sheet_names else (
    "Merged" if "Merged" in geo_book.sheet_names else geo_book.sheet_names[0]
)
geography = pd.read_excel(GEO_FILE, sheet_name=geo_sheet)

store_book = pd.ExcelFile(STORE_FILE)
store_sheet = "Stores" if "Stores" in store_book.sheet_names else store_book.sheet_names[0]
stores = pd.read_excel(STORE_FILE, sheet_name=store_sheet)

# 2. Basic cleaning
def clean_frame(df):
    df = df.copy()
    df.columns = df.columns.astype(str).str.strip()
    df = df.dropna(how="all").drop_duplicates()
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].map(
                lambda x: x.strip() if isinstance(x, str) else x
            )
    return df

geography = clean_frame(geography)
stores = clean_frame(stores)

for col in ["LoadDate", "UpdateDate", "OpenDate", "CloseDate", "LastRemodelDate"]:
    if col in geography.columns:
        geography[col] = pd.to_datetime(geography[col], errors="coerce")
    if col in stores.columns:
        stores[col] = pd.to_datetime(stores[col], errors="coerce")

# 3. Prepare joined data using GeographyKey
if "GeographyKey" in geography.columns and "GeographyKey" in stores.columns:
    merged = stores.merge(
        geography,
        on="GeographyKey",
        how="left",
        suffixes=("_Store", "_Geo")
    )
else:
    merged = stores.copy()

print(f"\nGeography sheet used: {geo_sheet}")
print(f"Geography records: {len(geography):,}")
print(f"Store records: {len(stores):,}")
print(f"Joined store records: {len(merged):,}")
print("\nGeography columns:", list(geography.columns))
print("Store columns:", list(stores.columns))

# 4. Chart helper
chart_no = 0
def save_plot(title, filename=None):
    global chart_no
    chart_no += 1
    plt.title(title, fontsize=12, fontweight="bold")
    plt.tight_layout()
    name = filename or f"Chart_{chart_no:02d}.png"
    plt.savefig(os.path.join(CHART_DIR, name), dpi=150, bbox_inches="tight")
    plt.close()

def bar_counts(df, col, title, top=15, horizontal=True):
    if col not in df.columns:
        return
    values = df[col].fillna("Missing").astype(str).value_counts().head(top)
    if values.empty:
        return
    plt.figure(figsize=(10, 5))
    if horizontal:
        sns.barplot(x=values.values, y=values.index, color="steelblue")
        plt.xlabel("Number of records")
    else:
        sns.barplot(x=values.index, y=values.values)
        plt.xticks(rotation=40, ha="right")
        plt.ylabel("Number of records")
    save_plot(title)

def numeric_hist(df, col, title):
    if col not in df.columns:
        return
    values = pd.to_numeric(df[col], errors="coerce").dropna()
    if len(values) < 2:
        return
    plt.figure(figsize=(9, 5))
    sns.histplot(values, bins=25, kde=True, color="steelblue")
    plt.xlabel(col)
    save_plot(title)

def numeric_box(df, col, title):
    if col not in df.columns:
        return
    values = pd.to_numeric(df[col], errors="coerce").dropna()
    if len(values) < 2:
        return
    plt.figure(figsize=(9, 5))
    sns.boxplot(x=values, color="steelblue")
    plt.xlabel(col)
    save_plot(title)

def grouped_mean(df, category, metric, title, top=12):
    if category not in df.columns or metric not in df.columns:
        return
    temp = df[[category, metric]].copy()
    temp[metric] = pd.to_numeric(temp[metric], errors="coerce")
    temp = temp.dropna()
    if temp.empty:
        return
    temp[category] = temp[category].astype(str)
    keep = temp[category].value_counts().head(top).index
    temp = temp[temp[category].isin(keep)]
    if temp.empty:
        return
    values = temp.groupby(category)[metric].mean().sort_values(ascending=False)
    plt.figure(figsize=(10, 5))
    sns.barplot(x=values.values, y=values.index, color="steelblue")
    plt.xlabel(f"Average {metric}")
    save_plot(title)

def date_trend(df, date_col, metric, title):
    if date_col not in df.columns or metric not in df.columns:
        return
    temp = df[[date_col, metric]].copy()
    temp[date_col] = pd.to_datetime(temp[date_col], errors="coerce")
    temp[metric] = pd.to_numeric(temp[metric], errors="coerce")
    temp = temp.dropna()
    if temp.empty:
        return
    series = temp.groupby(temp[date_col].dt.to_period("Y"))[metric].mean()
    if series.empty:
        return
    plt.figure(figsize=(9, 5))
    plt.plot(series.index.astype(str), series.values, marker="o")
    plt.xticks(rotation=35)
    plt.ylabel(f"Average {metric}")
    save_plot(title)

# 5. Generate 30 meaningful charts from the supplied records
# Geography charts
bar_counts(geography, "Continent Name", "01 - Geography Records by Continent")
bar_counts(geography, "GeographyType", "02 - Geography Records by Geography Type")
bar_counts(geography, "Status", "03 - Geography Status Distribution")
numeric_hist(geography, "Locations", "04 - Distribution of Locations")
numeric_box(geography, "Locations", "05 - Locations Box Plot")
numeric_hist(geography, "Employees", "06 - Distribution of Geography Employees")
numeric_box(geography, "Employees", "07 - Geography Employees Box Plot")
numeric_hist(geography, "Projected Revenue", "08 - Projected Revenue Distribution")
numeric_hist(geography, "Actual Revenue", "09 - Actual Revenue Distribution")
numeric_box(geography, "Difference", "10 - Revenue Difference Box Plot")
grouped_mean(geography, "Continent Name", "Actual Revenue", "11 - Average Actual Revenue by Continent")
grouped_mean(geography, "GeographyType", "Actual Revenue", "12 - Average Actual Revenue by Geography Type")
grouped_mean(geography, "Continent Name", "Locations", "13 - Average Locations by Continent")
grouped_mean(geography, "Continent Name", "Employees", "14 - Average Employees by Continent")
if {"Projected Revenue", "Actual Revenue"}.issubset(geography.columns):
    temp = geography[["Projected Revenue", "Actual Revenue"]].apply(pd.to_numeric, errors="coerce").dropna()
    if not temp.empty:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=temp, x="Projected Revenue", y="Actual Revenue", alpha=0.6, color="steelblue")
        save_plot("15 - Projected vs Actual Revenue")

# Store charts
bar_counts(stores, "StoreType", "16 - Store Type Distribution")
bar_counts(stores, "Status", "17 - Store Operating Status")
numeric_hist(stores, "EmployeeCount", "18 - Store Employee Count Distribution")
numeric_box(stores, "EmployeeCount", "19 - Store Employee Count Box Plot")
numeric_hist(stores, "SellingAreaSize", "20 - Store Selling Area Distribution")
numeric_box(stores, "SellingAreaSize", "21 - Store Selling Area Box Plot")
bar_counts(stores, "StoreManager", "22 - Stores by Store Manager", top=15)
date_trend(stores, "OpenDate", "EmployeeCount", "23 - Average Store Employees by Opening Year")
date_trend(stores, "LastRemodelDate", "SellingAreaSize", "24 - Average Selling Area by Remodel Year")

# Joined charts
if "Continent Name" in merged.columns:
    bar_counts(merged, "Continent Name", "25 - Stores by Continent")
if "StoreType" in merged.columns and "Continent Name" in merged.columns:
    temp = merged[["Continent Name", "StoreType"]].dropna()
    if not temp.empty:
        cross = pd.crosstab(temp["Continent Name"], temp["StoreType"])
        plt.figure(figsize=(9, 5))
        cross.plot(kind="bar", stacked=True, ax=plt.gca())
        plt.xticks(rotation=30, ha="right")
        save_plot("26 - Store Types by Continent")
if "Continent Name" in merged.columns:
    grouped_mean(merged, "Continent Name", "EmployeeCount", "27 - Average Store Employees by Continent")
    grouped_mean(merged, "Continent Name", "SellingAreaSize", "28 - Average Store Selling Area by Continent")
if {"EmployeeCount", "SellingAreaSize"}.issubset(stores.columns):
    temp = stores[["EmployeeCount", "SellingAreaSize"]].apply(pd.to_numeric, errors="coerce").dropna()
    if len(temp) > 1:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=temp, x="EmployeeCount", y="SellingAreaSize", color="steelblue")
        save_plot("29 - Store Employees vs Selling Area")
if {"Actual Revenue", "Projected Revenue"}.issubset(merged.columns):
    grouped_mean(merged, "StoreType", "Actual Revenue", "30 - Average Actual Revenue by Store Type")

# If an expected field is absent, fill remaining slots with additional real-data
# category/numeric summaries, never generated or random records.
if chart_no < 30:
    candidates = []
    for label, frame in [("Geography", geography), ("Stores", stores), ("Joined", merged)]:
        for col in frame.select_dtypes(include=np.number).columns:
            candidates.append((label, frame, col))
    for label, frame, col in candidates:
        if chart_no >= 30:
            break
        values = pd.to_numeric(frame[col], errors="coerce").dropna()
        if len(values) < 2:
            continue
        plt.figure(figsize=(9, 5))
        sns.histplot(values, bins=20, color="steelblue")
        save_plot(f"Additional {label} analysis - {col}")
if chart_no != 30:
    print(f"\nNote: {chart_no} valid charts could be produced from the available columns.")

# 6. Data-quality and summary tables
summary = pd.DataFrame([
    {
        "Dataset": "Geography",
        "Rows": len(geography),
        "Columns": len(geography.columns),
        "Missing cells": int(geography.isna().sum().sum()),
        "Duplicate rows": int(geography.duplicated().sum())
    },
    {
        "Dataset": "Stores",
        "Rows": len(stores),
        "Columns": len(stores.columns),
        "Missing cells": int(stores.isna().sum().sum()),
        "Duplicate rows": int(stores.duplicated().sum())
    },
    {
        "Dataset": "Joined Stores + Geography",
        "Rows": len(merged),
        "Columns": len(merged.columns),
        "Missing cells": int(merged.isna().sum().sum()),
        "Duplicate rows": int(merged.duplicated().sum())
    }
])

# 7. Export analysis workbook
report_path = os.path.join(OUTPUT_DIR, "Contoso_2026_Analysis_Report.xlsx")
with pd.ExcelWriter(report_path, engine="openpyxl") as writer:
    summary.to_excel(writer, sheet_name="Summary", index=False)
    geography.to_excel(writer, sheet_name="Geography", index=False)
    stores.to_excel(writer, sheet_name="Stores", index=False)
    merged.to_excel(writer, sheet_name="Joined_Data", index=False)
    for label, frame in [("Geography", geography), ("Stores", stores)]:
        numeric = frame.select_dtypes(include=np.number)
        if numeric.shape[1] >= 2:
            numeric.corr().to_excel(writer, sheet_name=f"{label}_Correlation")

print("\n" + "=" * 65)
print("ANALYSIS FINISHED")
print("=" * 65)
print("Geography rows:", len(geography))
print("Stores rows:", len(stores))
print("Joined rows:", len(merged))
print("Charts saved:", chart_no)
print("Charts folder:", CHART_DIR)
print("Excel report:", report_path)
