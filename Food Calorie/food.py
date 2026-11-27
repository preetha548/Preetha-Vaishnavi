
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================
# FOOD AND CALORIES DATA ANALYSIS
# ==========================================

# Load Dataset
file_path = "Food and Calories - Sheet1.csv"
df = pd.read_csv(file_path)

# Create output folder
os.makedirs("Food_Calorie_Charts", exist_ok=True)

# Data Cleaning
df.columns = df.columns.str.strip()
df["Food"] = df["Food"].astype(str).str.strip()
df["Serving"] = df["Serving"].astype(str)

df["Calories_Value"] = pd.to_numeric(
    df["Calories"].astype(str).str.extract(r"([\d.]+)")[0],
    errors="coerce"
)

df = df.dropna(subset=["Calories_Value"])
df = df[df["Calories_Value"] >= 0]

sns.set_theme(style="whitegrid")

print("\n========== FOOD CALORIE DATASET ==========")
print(df.head())
print("\nDataset Shape:", df.shape)
print("\nDataset Information:")
print(df.info())
print("\nStatistical Summary:")
print(df["Calories_Value"].describe())

# Sort data
sorted_df = df.sort_values("Calories_Value", ascending=False)
top10 = sorted_df.head(10)
bottom10 = sorted_df.tail(10)

# Chart saving function
def save_chart(number, title):
    plt.title(title, fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(
        f"Food_Calorie_Charts/Chart_{number:02d}.png",
        dpi=300,
        bbox_inches="tight"
    )
    plt.show()
    plt.close()

# 1. Top 10 Highest Calorie Foods
plt.figure(figsize=(12, 6))
sns.barplot(data=top10, x="Calories_Value", y="Food")
save_chart(1, "Top 10 Highest Calorie Foods")

# 2. Top 10 Lowest Calorie Foods
plt.figure(figsize=(12, 6))
sns.barplot(data=bottom10, x="Calories_Value", y="Food")
save_chart(2, "Top 10 Lowest Calorie Foods")

# 3. Calories Distribution Histogram
plt.figure(figsize=(10, 6))
plt.hist(df["Calories_Value"], bins=30, edgecolor="black")
save_chart(3, "Calories Distribution Histogram")

# 4. Calories Density Plot
plt.figure(figsize=(10, 6))
sns.kdeplot(data=df, x="Calories_Value", fill=True)
save_chart(4, "Calories Density Distribution")

# 5. Calories Box Plot
plt.figure(figsize=(10, 6))
sns.boxplot(y=df["Calories_Value"])
save_chart(5, "Food Calories Box Plot")

# 6. Calories Violin Plot
plt.figure(figsize=(10, 6))
sns.violinplot(y=df["Calories_Value"])
save_chart(6, "Calories Violin Plot")

# 7. Calories Strip Plot
plt.figure(figsize=(12, 6))
sns.stripplot(y=df["Calories_Value"], jitter=True)
save_chart(7, "Calories Strip Plot")

# 8. Calories Swarm Plot (sample)
plt.figure(figsize=(12, 6))
sns.swarmplot(y=df.sample(min(150, len(df)), random_state=42)["Calories_Value"])
save_chart(8, "Calories Swarm Plot")

# 9. Food Calories Line Chart
plt.figure(figsize=(14, 6))
plt.plot(df["Food"], df["Calories_Value"], marker="o")
plt.xticks(rotation=90, fontsize=6)
save_chart(9, "Food Calories Line Chart")

# 10. Food Calories Area Chart
plt.figure(figsize=(12, 6))
plt.fill_between(range(len(df)), df["Calories_Value"], alpha=0.5)
plt.xlabel("Food Index")
plt.ylabel("Calories")
save_chart(10, "Food Calories Area Chart")

# 11. Top 20 Food Pie Chart
plt.figure(figsize=(10, 10))
pie_data = sorted_df.head(20)
plt.pie(
    pie_data["Calories_Value"],
    labels=pie_data["Food"],
    autopct="%1.1f%%"
)
save_chart(11, "Top 20 Food Calorie Pie Chart")

# 12. Top 20 Food Donut Chart
plt.figure(figsize=(10, 10))
plt.pie(
    sorted_df.head(20)["Calories_Value"],
    labels=sorted_df.head(20)["Food"],
    autopct="%1.1f%%",
    wedgeprops={"width": 0.4}
)
save_chart(12, "Food Calories Donut Chart")

# 13. Calories Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(range(len(df)), df["Calories_Value"], alpha=0.6)
plt.xlabel("Food Index")
plt.ylabel("Calories")
save_chart(13, "Food Calories Scatter Plot")

# 14. Calories Step Plot
plt.figure(figsize=(12, 6))
plt.step(range(len(df)), df["Calories_Value"], where="mid")
plt.xlabel("Food Index")
plt.ylabel("Calories")
save_chart(14, "Food Calories Step Plot")

# 15. Calories Stem Plot
plt.figure(figsize=(12, 6))
plt.stem(range(len(df)), df["Calories_Value"])
plt.xlabel("Food Index")
plt.ylabel("Calories")
save_chart(15, "Food Calories Stem Plot")

# 16. Top 25 Food Horizontal Bar Chart
plt.figure(figsize=(12, 8))
sns.barplot(
    data=sorted_df.head(25),
    x="Calories_Value",
    y="Food"
)
save_chart(16, "Top 25 Calorie Foods")

# 17. Bottom 25 Food Bar Chart
plt.figure(figsize=(12, 8))
sns.barplot(
    data=bottom10,
    x="Calories_Value",
    y="Food"
)
save_chart(17, "Lowest Calorie Foods")

# 18. Calories Frequency Count
plt.figure(figsize=(12, 6))
plt.hist(df["Calories_Value"], bins=15, edgecolor="black")
plt.yscale("log")
save_chart(18, "Calories Frequency Log Scale")

# 19. Cumulative Calories Plot
plt.figure(figsize=(12, 6))
values = np.sort(df["Calories_Value"].values)
plt.plot(values, np.cumsum(values))
plt.xlabel("Sorted Food Index")
plt.ylabel("Cumulative Calories")
save_chart(19, "Cumulative Calories Plot")

# 20. Calories Percentage Distribution
plt.figure(figsize=(10, 6))
percentages = df["Calories_Value"] / df["Calories_Value"].sum() * 100
plt.hist(percentages, bins=20, edgecolor="black")
plt.xlabel("Percentage of Total Calories")
save_chart(20, "Calories Percentage Distribution")

# 21. Calories Boxen Plot
plt.figure(figsize=(10, 6))
sns.boxenplot(y=df["Calories_Value"])
save_chart(21, "Calories Boxen Plot")

# 22. Calories ECDF Plot
plt.figure(figsize=(10, 6))
sns.ecdfplot(data=df, x="Calories_Value")
save_chart(22, "Calories Empirical Distribution")

# 23. Calories Rug Plot
plt.figure(figsize=(12, 6))
sns.rugplot(data=df, x="Calories_Value", height=0.5)
save_chart(23, "Calories Rug Plot")

# 24. Calories Lollipop Chart
sample = sorted_df.head(20).sort_values("Calories_Value")
plt.figure(figsize=(12, 8))
plt.hlines(
    y=sample["Food"],
    xmin=0,
    xmax=sample["Calories_Value"]
)
plt.scatter(sample["Calories_Value"], sample["Food"], s=60)
save_chart(24, "Food Calories Lollipop Chart")

# 25. Calories Stem-and-Leaf Style Plot
plt.figure(figsize=(12, 6))
plt.scatter(
    df["Calories_Value"],
    np.zeros(len(df)),
    alpha=0.5
)
plt.yticks([])
plt.xlabel("Calories")
save_chart(25, "Calories Distribution Dot Plot")

# 26. Calories Moving Average
plt.figure(figsize=(12, 6))
plt.plot(df["Calories_Value"], label="Original")
plt.plot(
    df["Calories_Value"].rolling(10, min_periods=1).mean(),
    linewidth=2,
    label="10 Food Moving Average"
)
plt.legend()
save_chart(26, "Calories Moving Average")

# 27. Calories Rank Chart
ranked = sorted_df.reset_index(drop=True)
plt.figure(figsize=(12, 6))
plt.plot(
    ranked.index + 1,
    ranked["Calories_Value"],
    marker="."
)
plt.xlabel("Food Rank")
plt.ylabel("Calories")
save_chart(27, "Food Calorie Ranking")

# 28. Calories Frequency Bar Chart
frequency = pd.cut(
    df["Calories_Value"],
    bins=10,
    include_lowest=True
).value_counts().sort_index()

plt.figure(figsize=(12, 6))
frequency.plot(kind="bar")
plt.xticks(rotation=45, ha="right")
plt.xlabel("Calorie Range")
plt.ylabel("Number of Foods")
save_chart(28, "Food Calories Range Frequency")

# 29. Calories Q-Q Plot
plt.figure(figsize=(8, 8))
from scipy import stats
stats.probplot(
    df["Calories_Value"],
    dist="norm",
    plot=plt
)
save_chart(29, "Calories Normal Q-Q Plot")

# 30. Calories Summary Dashboard
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

axes[0, 0].hist(df["Calories_Value"], bins=20, edgecolor="black")
axes[0, 0].set_title("Calories Histogram")

sns.boxplot(y=df["Calories_Value"], ax=axes[0, 1])
axes[0, 1].set_title("Calories Box Plot")

axes[1, 0].bar(
    top10["Food"],
    top10["Calories_Value"]
)
axes[1, 0].set_title("Top 10 Foods")
axes[1, 0].tick_params(axis="x", rotation=70)

axes[1, 1].plot(
    sorted_df["Calories_Value"].values
)
axes[1, 1].set_title("Sorted Calorie Values")

plt.tight_layout()
plt.savefig(
    "Food_Calorie_Charts/Chart_30.png",
    dpi=300
)
plt.show()
plt.close()

# Export cleaned dataset
df.to_csv(
    "Food_Calorie_Charts/Cleaned_Food_Calories.csv",
    index=False
)

# Final Report
print("\n========== FINAL ANALYSIS ==========")
print("Total Food Items:", len(df))
print("Average Calories:", round(df["Calories_Value"].mean(), 2))
print("Maximum Calories:", df["Calories_Value"].max())
print("Minimum Calories:", df["Calories_Value"].min())
print("Median Calories:", df["Calories_Value"].median())
print("Standard Deviation:", round(df["Calories_Value"].std(), 2))

print("\nHighest Calorie Food:")
print(sorted_df.iloc[0])

print("\nLowest Calorie Food:")
print(bottom10.sort_values("Calories_Value").iloc[0])

print("\nSUCCESS: All 30 charts generated!")
print("Charts saved in Food_Calorie_Charts folder.")

