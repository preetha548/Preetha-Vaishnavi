
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os
import warnings

warnings.filterwarnings('ignore')

# ==========================================
# 1. LOAD DATASET
# ==========================================

file_path = r"C:\Users\USER PC\Desktop\Housing Real Estate from Indian Cities\Real Estate Data V21.csv"

df = pd.read_csv(file_path)

print("DATASET OVERVIEW")
print("=" * 50)
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())
print("\nFirst 5 Rows:")
print(df.head())
print("\nDataset Information:")
df.info()

# ==========================================
# 2. DATA PREPROCESSING
# ==========================================

sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 11

numeric_cols = df.select_dtypes(include=np.number).columns.tolist()

categorical_cols = df.select_dtypes(
    include=['object', 'category']
).columns.tolist()

city_cols = [
    col for col in df.columns
    if 'city' in col.lower()
]

location_cols = [
    col for col in df.columns
    if 'location' in col.lower()
]

price_cols = [
    col for col in df.columns
    if any(word in col.lower()
           for word in ['price', 'cost', 'amount', 'value'])
]

area_cols = [
    col for col in numeric_cols
    if any(word in col.lower()
           for word in ['area', 'size', 'sqft', 'square'])
]

print("\nNumerical Columns:", numeric_cols)
print("Categorical Columns:", categorical_cols)
print("Price Columns:", price_cols)

# Output folder
output_folder = "Real_Estate_Visualizations"
os.makedirs(output_folder, exist_ok=True)

# ==========================================
# 3. MISSING VALUES HEATMAP
# ==========================================

plt.figure(figsize=(14, 6))
sns.heatmap(df.isnull(), cmap='viridis', cbar=False)
plt.title("Missing Values Heatmap")
plt.tight_layout()
plt.savefig(output_folder + "/01_Missing_Values.png", dpi=300)
plt.show()

# ==========================================
# 4. NUMERICAL FEATURES DISTRIBUTION
# ==========================================

if numeric_cols:
    df[numeric_cols].hist(
        figsize=(16, 12),
        bins=30,
        color='skyblue',
        edgecolor='black'
    )
    plt.suptitle("Numerical Features Distribution")
    plt.tight_layout()
    plt.savefig(output_folder + "/02_Numerical_Distribution.png", dpi=300)
    plt.show()

# ==========================================
# 5. BOXPLOTS
# ==========================================

for col in numeric_cols:
    plt.figure(figsize=(10, 5))
    sns.boxplot(x=df[col], color='lightgreen')
    plt.title(f"Boxplot of {col}")
    plt.tight_layout()
    plt.savefig(
        output_folder + f"/03_Boxplot_{col}.png",
        dpi=300
    )
    plt.show()
    plt.close()

# ==========================================
# 6. CATEGORICAL FEATURES ANALYSIS
# ==========================================

for col in categorical_cols:
    if df[col].nunique() <= 20:
        plt.figure(figsize=(12, 6))

        df[col].value_counts().head(20).plot(
            kind='bar',
            color='coral',
            edgecolor='black'
        )

        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(
            output_folder + f"/04_Category_{col}.png",
            dpi=300
        )
        plt.show()
        plt.close()

# ==========================================
# 7. CITY-WISE PROPERTY COUNT
# ==========================================

if city_cols:
    city_col = city_cols[0]

    plt.figure(figsize=(13, 6))

    df[city_col].value_counts().head(15).plot(
        kind='bar',
        color='orange',
        edgecolor='black'
    )

    plt.title("Top 15 Cities by Property Count")
    plt.xlabel("City")
    plt.ylabel("Number of Properties")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(output_folder + "/05_City_Property_Count.png", dpi=300)
    plt.show()

# ==========================================
# 8. CORRELATION HEATMAP
# ==========================================

if len(numeric_cols) >= 2:
    plt.figure(figsize=(14, 10))

    correlation = df[numeric_cols].corr()

    sns.heatmap(
        correlation,
        annot=True,
        cmap='coolwarm',
        fmt='.2f',
        linewidths=0.5
    )

    plt.title("Real Estate Feature Correlation Heatmap")
    plt.tight_layout()
    plt.savefig(output_folder + "/06_Correlation_Heatmap.png", dpi=300)
    plt.show()

# ==========================================
# 9. SCATTER PLOTS
# ==========================================

if len(numeric_cols) >= 2:
    for i in range(min(5, len(numeric_cols) - 1)):

        plt.figure(figsize=(9, 6))

        sns.scatterplot(
            data=df,
            x=numeric_cols[i],
            y=numeric_cols[i + 1],
            alpha=0.6,
            color='blue'
        )

        plt.title(
            f"{numeric_cols[i]} vs {numeric_cols[i+1]}"
        )

        plt.tight_layout()
        plt.savefig(
            output_folder + f"/07_Scatter_{i}.png",
            dpi=300
        )
        plt.show()
        plt.close()

# ==========================================
# 10. PRICE DISTRIBUTION
# ==========================================

if price_cols:
    price_col = price_cols[0]

    plt.figure(figsize=(10, 6))

    sns.histplot(
        df[price_col].dropna(),
        bins=30,
        kde=True,
        color='teal'
    )

    plt.title("Real Estate Price Distribution")
    plt.xlabel(price_col)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(output_folder + "/08_Price_Distribution.png", dpi=300)
    plt.show()

    # Price boxplot
    plt.figure(figsize=(10, 5))
    sns.boxplot(x=df[price_col], color='gold')
    plt.title("Property Price Outlier Analysis")
    plt.tight_layout()
    plt.savefig(output_folder + "/09_Price_Boxplot.png", dpi=300)
    plt.show()

# ==========================================
# 11. CITY-WISE AVERAGE PROPERTY PRICE
# ==========================================

if price_cols and city_cols:
    city_col = city_cols[0]
    price_col = price_cols[0]

    city_price = (
        df.groupby(city_col)[price_col]
        .mean()
        .sort_values(ascending=False)
        .head(15)
    )

    plt.figure(figsize=(13, 7))

    sns.barplot(
        x=city_price.values,
        y=city_price.index,
        color='cornflowerblue'
    )

    plt.title("Top 15 Cities by Average Property Price")
    plt.xlabel("Average Property Price")
    plt.ylabel("City")
    plt.tight_layout()
    plt.savefig(output_folder + "/10_City_Average_Price.png", dpi=300)
    plt.show()

# ==========================================
# 12. AREA VS PROPERTY PRICE
# ==========================================

if price_cols and area_cols:
    price_col = price_cols[0]
    area_col = area_cols[0]

    plt.figure(figsize=(10, 6))

    sns.scatterplot(
        data=df,
        x=area_col,
        y=price_col,
        alpha=0.6,
        color='purple'
    )

    plt.title("Property Area vs Property Price")
    plt.xlabel("Property Area")
    plt.ylabel("Property Price")
    plt.tight_layout()
    plt.savefig(output_folder + "/11_Area_vs_Price.png", dpi=300)
    plt.show()

# ==========================================
# 13. PRICE BY CATEGORICAL FEATURES
# ==========================================

if price_cols:
    price_col = price_cols[0]

    for col in categorical_cols:
        if df[col].nunique() <= 15:

            plt.figure(figsize=(12, 6))

            sns.boxplot(
                data=df,
                x=col,
                y=price_col,
                palette='Set2'
            )

            plt.title(f"{price_col} by {col}")
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig(
                output_folder + f"/12_Price_by_{col}.png",
                dpi=300
            )
            plt.show()
            plt.close()

# ==========================================
# 14. INTERACTIVE SCATTER PLOT
# ==========================================

if len(numeric_cols) >= 2:
    fig = px.scatter(
        df,
        x=numeric_cols[0],
        y=numeric_cols[1],
        color=categorical_cols[0] if categorical_cols else None,
        title="Interactive Real Estate Analysis",
        hover_data=df.columns[:5].tolist()
    )

    fig.write_html(output_folder + "/13_Interactive_Scatter.html")
    fig.show()

# ==========================================
# 15. INTERACTIVE CORRELATION HEATMAP
# ==========================================

if len(numeric_cols) >= 2:
    fig = px.imshow(
        df[numeric_cols].corr(),
        text_auto=True,
        color_continuous_scale='RdBu_r',
        title="Interactive Correlation Heatmap"
    )

    fig.write_html(output_folder + "/14_Interactive_Heatmap.html")
    fig.show()

# ==========================================
# 16. INTERACTIVE CITY-WISE PRICE CHART
# ==========================================

if price_cols and city_cols:
    city_summary = (
        df.groupby(city_cols[0])[price_cols[0]]
        .mean()
        .reset_index()
        .sort_values(price_cols[0], ascending=False)
        .head(20)
    )

    fig = px.bar(
        city_summary,
        x=city_cols[0],
        y=price_cols[0],
        color=price_cols[0],
        title="Interactive City-wise Average Property Price",
        labels={
            city_cols[0]: "City",
            price_cols[0]: "Average Price"
        }
    )

    fig.write_html(output_folder + "/15_City_Price.html")
    fig.show()

# ==========================================
# 17. FINAL SUMMARY
# ==========================================

print("\n" + "=" * 55)
print("REAL ESTATE DATA VISUALIZATION COMPLETED")
print("=" * 55)

print("Total Records:", df.shape[0])
print("Total Features:", df.shape[1])
print("Numerical Features:", len(numeric_cols))
print("Categorical Features:", len(categorical_cols))
print("Missing Values:", df.isnull().sum().sum())
print("Duplicate Records:", df.duplicated().sum())

print("\nAll charts saved in:", output_folder)

print("\nVisualization Process Completed Successfully!")
