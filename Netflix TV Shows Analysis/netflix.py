
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("=" * 60)
print("       NETFLIX TV SHOWS DATA ANALYSIS")
print("=" * 60)

# 1. Load Dataset
df = pd.read_csv("TV Shows - Netflix.csv")

# 2. Data Cleaning
df = df.drop_duplicates()
df = df.dropna(subset=[
    "Titles", "Year", "Rating", "IMDB_Rating", "Netflix"
])

df["Netflix_Status"] = df["Netflix"].map({
    1: "Available",
    0: "Not Available"
})

df["Decade"] = (df["Year"] // 10) * 10

print("\nDataset Loaded Successfully!")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nTotal TV Shows:", len(df))
print("Average IMDb Rating:", round(df["IMDB_Rating"].mean(), 2))

# Prepare common data
top10 = df.nlargest(10, "IMDB_Rating")
recent10 = df.nlargest(10, "Year")
rating_counts = df["Rating"].value_counts()
year_counts = df["Year"].value_counts().sort_index()
decade_counts = df["Decade"].value_counts().sort_index()
netflix_counts = df["Netflix_Status"].value_counts()
avg_rating_year = df.groupby("Year")["IMDB_Rating"].mean()
avg_rating_category = df.groupby("Rating")["IMDB_Rating"].mean()

# =====================================================
# CHART 1: Top 10 Highest Rated Shows
# =====================================================
plt.figure(figsize=(12, 6))
plt.barh(top10["Titles"], top10["IMDB_Rating"])
plt.title("1. Top 10 Highest Rated TV Shows")
plt.xlabel("IMDb Rating")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# =====================================================
# CHART 2: Release Year Distribution
# =====================================================
plt.figure(figsize=(10, 5))
plt.hist(df["Year"], bins=10, edgecolor="black")
plt.title("2. TV Shows Release Year Distribution")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows")
plt.tight_layout()
plt.show()

# =====================================================
# CHART 3: Age Rating Distribution
# =====================================================
plt.figure(figsize=(9, 5))
rating_counts.plot(kind="bar")
plt.title("3. TV Shows by Age Rating")
plt.xlabel("Age Rating")
plt.ylabel("Number of Shows")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =====================================================
# CHART 4: Netflix Availability Pie Chart
# =====================================================
plt.figure(figsize=(7, 7))
netflix_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)
plt.title("4. Netflix Availability Percentage")
plt.ylabel("")
plt.tight_layout()
plt.show()

# =====================================================
# CHART 5: IMDb Rating Distribution
# =====================================================
plt.figure(figsize=(9, 5))
plt.hist(df["IMDB_Rating"], bins=10, edgecolor="black")
plt.title("5. IMDb Rating Distribution")
plt.xlabel("IMDb Rating")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# =====================================================
# CHART 6: Average IMDb Rating by Year
# =====================================================
plt.figure(figsize=(11, 5))
plt.plot(avg_rating_year.index, avg_rating_year.values, marker="o")
plt.title("6. Average IMDb Rating by Release Year")
plt.xlabel("Year")
plt.ylabel("Average IMDb Rating")
plt.grid(True)
plt.tight_layout()
plt.show()

# =====================================================
# CHART 7: Netflix vs Non-Netflix Shows
# =====================================================
plt.figure(figsize=(8, 5))
netflix_counts.plot(kind="bar")
plt.title("7. Netflix vs Non-Netflix Shows")
plt.xlabel("Netflix Availability")
plt.ylabel("Number of Shows")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# =====================================================
# CHART 8: IMDb Rating by Netflix Availability
# =====================================================
plt.figure(figsize=(8, 5))
df.boxplot(column="IMDB_Rating", by="Netflix_Status")
plt.title("8. IMDb Rating by Netflix Availability")
plt.suptitle("")
plt.xlabel("Netflix Status")
plt.ylabel("IMDb Rating")
plt.tight_layout()
plt.show()

# =====================================================
# CHART 9: Top 10 Recent TV Shows
# =====================================================
plt.figure(figsize=(11, 6))
plt.barh(recent10["Titles"], recent10["Year"])
plt.title("9. Top 10 Recent TV Shows")
plt.xlabel("Release Year")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# =====================================================
# CHART 10: TV Shows by Decade
# =====================================================
plt.figure(figsize=(9, 5))
decade_counts.plot(kind="bar")
plt.title("10. TV Shows by Decade")
plt.xlabel("Decade")
plt.ylabel("Number of Shows")
plt.tight_layout()
plt.show()

# =====================================================
# CHART 11: IMDb Rating vs Release Year
# =====================================================
plt.figure(figsize=(9, 5))
plt.scatter(df["Year"], df["IMDB_Rating"])
plt.title("11. IMDb Rating vs Release Year")
plt.xlabel("Release Year")
plt.ylabel("IMDb Rating")
plt.grid(True)
plt.tight_layout()
plt.show()

# =====================================================
# CHART 12: Average Rating by Age Category
# =====================================================
plt.figure(figsize=(9, 5))
avg_rating_category.plot(kind="bar")
plt.title("12. Average IMDb Rating by Age Category")
plt.xlabel("Age Rating")
plt.ylabel("Average IMDb Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =====================================================
# CHART 13: Netflix Availability by Age Rating
# =====================================================
plt.figure(figsize=(10, 5))
pd.crosstab(
    df["Rating"], df["Netflix_Status"]
).plot(kind="bar")
plt.title("13. Netflix Availability by Age Rating")
plt.xlabel("Age Rating")
plt.ylabel("Number of Shows")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =====================================================
# CHART 14: IMDb Rating Frequency
# =====================================================
plt.figure(figsize=(9, 5))
df["IMDB_Rating"].value_counts().sort_index().plot(kind="bar")
plt.title("14. IMDb Rating Frequency")
plt.xlabel("IMDb Rating")
plt.ylabel("Number of Shows")
plt.tight_layout()
plt.show()

# =====================================================
# CHART 15: Netflix Shows by Release Year
# =====================================================
plt.figure(figsize=(10, 5))
df[df["Netflix"] == 1]["Year"].value_counts().sort_index().plot(
    kind="line", marker="o"
)
plt.title("15. Netflix Shows by Release Year")
plt.xlabel("Year")
plt.ylabel("Number of Shows")
plt.grid(True)
plt.tight_layout()
plt.show()

# =====================================================
# CHART 16: IMDb Rating Pie Distribution
# =====================================================
plt.figure(figsize=(8, 8))
rating_groups = pd.cut(
    df["IMDB_Rating"],
    bins=[0, 5, 6, 7, 8, 10],
    labels=["Below 5", "5-6", "6-7", "7-8", "8-10"]
)
rating_groups.value_counts().sort_index().plot(
    kind="pie", autopct="%1.1f%%"
)
plt.title("16. IMDb Rating Group Distribution")
plt.ylabel("")
plt.tight_layout()
plt.show()

# =====================================================
# CHART 17: Average IMDb Rating by Netflix Status
# =====================================================
plt.figure(figsize=(8, 5))
df.groupby("Netflix_Status")["IMDB_Rating"].mean().plot(
    kind="bar"
)
plt.title("17. Average IMDb Rating by Netflix Status")
plt.xlabel("Netflix Status")
plt.ylabel("Average IMDb Rating")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

# =====================================================
# CHART 18: Release Year Area Chart
# =====================================================
plt.figure(figsize=(10, 5))
plt.fill_between(year_counts.index, year_counts.values, alpha=0.5)
plt.plot(year_counts.index, year_counts.values, marker="o")
plt.title("18. TV Shows Release Year Area Chart")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows")
plt.tight_layout()
plt.show()

# =====================================================
# CHART 19: IMDb Rating Box Plot
# =====================================================
plt.figure(figsize=(8, 5))
plt.boxplot(df["IMDB_Rating"])
plt.title("19. Overall IMDb Rating Box Plot")
plt.ylabel("IMDb Rating")
plt.tight_layout()
plt.show()

# =====================================================
# CHART 20: IMDb Rating Violin Plot
# =====================================================
plt.figure(figsize=(8, 5))
plt.violinplot(df["IMDB_Rating"], showmeans=True)
plt.title("20. IMDb Rating Violin Plot")
plt.ylabel("IMDb Rating")
plt.tight_layout()
plt.show()

# =====================================================
# CHART 21: TV Shows by Age Rating - Horizontal Bar
# =====================================================
plt.figure(figsize=(9, 5))
rating_counts.sort_values().plot(kind="barh")
plt.title("21. Age Rating Horizontal Comparison")
plt.xlabel("Number of Shows")
plt.ylabel("Age Rating")
plt.tight_layout()
plt.show()

# =====================================================
# CHART 22: Netflix Availability by Decade
# =====================================================
plt.figure(figsize=(10, 5))
pd.crosstab(
    df["Decade"], df["Netflix_Status"]
).plot(kind="bar", stacked=True)
plt.title("22. Netflix Availability by Decade")
plt.xlabel("Decade")
plt.ylabel("Number of Shows")
plt.tight_layout()
plt.show()

# =====================================================
# CHART 23: Top 10 Lowest Rated Shows
# =====================================================
plt.figure(figsize=(11, 6))
lowest10 = df.nsmallest(10, "IMDB_Rating")
plt.barh(lowest10["Titles"], lowest10["IMDB_Rating"])
plt.title("23. Top 10 Lowest Rated TV Shows")
plt.xlabel("IMDb Rating")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# =====================================================
# CHART 24: IMDb Rating by Age Rating - Box Plot
# =====================================================
plt.figure(figsize=(10, 5))
df.boxplot(column="IMDB_Rating", by="Rating")
plt.title("24. IMDb Rating Comparison by Age Rating")
plt.suptitle("")
plt.xlabel("Age Rating")
plt.ylabel("IMDb Rating")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =====================================================
# CHART 25: Average IMDb Rating by Decade
# =====================================================
plt.figure(figsize=(9, 5))
df.groupby("Decade")["IMDB_Rating"].mean().plot(
    kind="line", marker="o"
)
plt.title("25. Average IMDb Rating by Decade")
plt.xlabel("Decade")
plt.ylabel("Average IMDb Rating")
plt.grid(True)
plt.tight_layout()
plt.show()

# =====================================================
# CHART 26: IMDb Rating Density
# =====================================================
plt.figure(figsize=(9, 5))
df["IMDB_Rating"].plot(kind="kde")
plt.title("26. IMDb Rating Density Distribution")
plt.xlabel("IMDb Rating")
plt.tight_layout()
plt.show()

# =====================================================
# CHART 27: Yearly Shows Count - Step Chart
# =====================================================
plt.figure(figsize=(10, 5))
plt.step(year_counts.index, year_counts.values, where="mid")
plt.title("27. Yearly TV Shows Count")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows")
plt.grid(True)
plt.tight_layout()
plt.show()

# =====================================================
# CHART 28: IMDb Rating Bubble Chart
# =====================================================
plt.figure(figsize=(10, 6))
plt.scatter(
    df["Year"],
    df["IMDB_Rating"],
    s=df["IMDB_Rating"] * 30,
    alpha=0.5
)
plt.title("28. IMDb Rating Bubble Chart")
plt.xlabel("Release Year")
plt.ylabel("IMDb Rating")
plt.grid(True)
plt.tight_layout()
plt.show()

# =====================================================
# CHART 29: Netflix Status by Age Rating - Percentage
# =====================================================
plt.figure(figsize=(10, 5))
availability_pct = pd.crosstab(
    df["Rating"],
    df["Netflix_Status"],
    normalize="index"
) * 100

availability_pct.plot(kind="bar", stacked=True)
plt.title("29. Netflix Availability Percentage by Age Rating")
plt.xlabel("Age Rating")
plt.ylabel("Percentage (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# =====================================================
# CHART 30: Correlation Heatmap
# =====================================================
plt.figure(figsize=(8, 6))

correlation = df[
    ["Year", "IMDB_Rating", "Netflix"]
].corr()

plt.imshow(correlation, cmap="coolwarm", aspect="auto")
plt.colorbar(label="Correlation")

plt.xticks(
    range(len(correlation.columns)),
    correlation.columns,
    rotation=45
)
plt.yticks(
    range(len(correlation.columns)),
    correlation.columns
)

for i in range(len(correlation.columns)):
    for j in range(len(correlation.columns)):
        plt.text(
            j, i,
            f"{correlation.iloc[i, j]:.2f}",
            ha="center",
            va="center"
        )

plt.title("30. Netflix Dataset Correlation Heatmap")
plt.tight_layout()
plt.show()

# =====================================================
# FINAL ANALYSIS REPORT
# =====================================================
print("\n" + "=" * 60)
print("          FINAL NETFLIX ANALYSIS REPORT")
print("=" * 60)

print("Total TV Shows:", len(df))
print("Highest IMDb Rating:", df["IMDB_Rating"].max())
print("Lowest IMDb Rating:", df["IMDB_Rating"].min())
print("Average IMDb Rating:", round(df["IMDB_Rating"].mean(), 2))
print("Oldest Release Year:", df["Year"].min())
print("Newest Release Year:", df["Year"].max())
print("Netflix Available:", (df["Netflix"] == 1).sum())
print("Not Available:", (df["Netflix"] == 0).sum())

print("\nTop 5 TV Shows:")
print(top10[["Titles", "Year", "IMDB_Rating"]].head())

print("\nAge Rating Summary:")
print(rating_counts)

print("\nAnalysis Completed Successfully!")
print("Total Charts: 30")
