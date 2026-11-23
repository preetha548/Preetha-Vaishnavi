
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("BOOK DATASET ANALYSIS STARTED")

# 1. Load Dataset
try:
    df = pd.read_csv(
        "books.csv",
        engine="python",
        on_bad_lines="warn"
    )
    print("Dataset loaded successfully!")
except FileNotFoundError:
    print("ERROR: books.csv not found!")
    raise SystemExit

# 2. Clean Column Names
df.columns = df.columns.str.strip()

# 3. Data Preprocessing
numeric_cols = [
    "average_rating",
    "num_pages",
    "ratings_count",
    "text_reviews_count"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["publication_date"] = pd.to_datetime(
    df["publication_date"], errors="coerce"
)

df["publication_year"] = df["publication_date"].dt.year

df["language_code"] = df["language_code"].astype(str).str.strip()

sns.set_theme(style="whitegrid")

print("\nDataset Shape:", df.shape)
print("\nDataset Information:")
print(df.info())

print("\nStatistical Description:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# 4. Chart Function
def create_chart(number, title):
    plt.title(title)
    plt.tight_layout()
    plt.savefig(f"chart_{number:02d}.png", dpi=150)
    plt.show()
    plt.close()

# CHART 1: Average Rating Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["average_rating"].dropna(), bins=20)
create_chart(1, "Average Book Rating Distribution")

# CHART 2: Number of Pages Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["num_pages"].dropna(), bins=30)
create_chart(2, "Distribution of Book Pages")

# CHART 3: Ratings Count Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["ratings_count"].dropna(), bins=30)
create_chart(3, "Ratings Count Distribution")

# CHART 4: Text Reviews Distribution
plt.figure(figsize=(8, 5))
plt.hist(df["text_reviews_count"].dropna(), bins=30)
create_chart(4, "Text Reviews Distribution")

# CHART 5: Books by Language
plt.figure(figsize=(10, 5))
df["language_code"].value_counts().head(15).plot(kind="bar")
create_chart(5, "Top 15 Languages by Book Count")

# CHART 6: Top 15 Publishers
plt.figure(figsize=(10, 5))
df["publisher"].value_counts().head(15).plot(kind="bar")
create_chart(6, "Top 15 Publishers")

# CHART 7: Top 15 Authors
plt.figure(figsize=(10, 5))
df["authors"].value_counts().head(15).plot(kind="bar")
create_chart(7, "Top 15 Authors")

# CHART 8: Rating Boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(y=df["average_rating"])
create_chart(8, "Average Rating Boxplot")

# CHART 9: Pages Boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(y=df["num_pages"])
create_chart(9, "Book Pages Boxplot")

# CHART 10: Ratings Boxplot
plt.figure(figsize=(8, 5))
sns.boxplot(y=df["ratings_count"])
create_chart(10, "Ratings Count Boxplot")

# CHART 11: Rating vs Pages
plt.figure(figsize=(8, 5))
plt.scatter(df["num_pages"], df["average_rating"], alpha=0.4)
plt.xlabel("Number of Pages")
plt.ylabel("Average Rating")
create_chart(11, "Rating vs Number of Pages")

# CHART 12: Ratings vs Text Reviews
plt.figure(figsize=(8, 5))
plt.scatter(df["ratings_count"], df["text_reviews_count"], alpha=0.4)
plt.xlabel("Ratings Count")
plt.ylabel("Text Reviews Count")
create_chart(12, "Ratings Count vs Text Reviews")

# CHART 13: Rating vs Ratings Count
plt.figure(figsize=(8, 5))
plt.scatter(df["ratings_count"], df["average_rating"], alpha=0.4)
plt.xlabel("Ratings Count")
plt.ylabel("Average Rating")
create_chart(13, "Average Rating vs Ratings Count")

# CHART 14: Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    df[numeric_cols].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
create_chart(14, "Book Dataset Correlation Heatmap")

# CHART 15: Average Rating by Language
plt.figure(figsize=(10, 5))
sns.barplot(
    data=df[df["language_code"].isin(
        df["language_code"].value_counts().head(10).index
    )],
    x="language_code",
    y="average_rating"
)
create_chart(15, "Average Rating by Language")

# CHART 16: Average Pages by Language
plt.figure(figsize=(10, 5))
sns.barplot(
    data=df[df["language_code"].isin(
        df["language_code"].value_counts().head(10).index
    )],
    x="language_code",
    y="num_pages"
)
create_chart(16, "Average Pages by Language")

# CHART 17: Average Rating by Publisher
plt.figure(figsize=(12, 5))
top_publishers = df["publisher"].value_counts().head(10).index
sns.barplot(
    data=df[df["publisher"].isin(top_publishers)],
    x="publisher",
    y="average_rating"
)
plt.xticks(rotation=45)
create_chart(17, "Average Rating by Top Publishers")

# CHART 18: Total Pages by Publisher
plt.figure(figsize=(10, 5))
df.groupby("publisher")["num_pages"].sum().nlargest(15).plot(kind="bar")
create_chart(18, "Top Publishers by Total Pages")

# CHART 19: Total Ratings by Publisher
plt.figure(figsize=(10, 5))
df.groupby("publisher")["ratings_count"].sum().nlargest(15).plot(kind="bar")
create_chart(19, "Top Publishers by Ratings")

# CHART 20: Top 15 Highest Rated Books
plt.figure(figsize=(12, 6))
top_rated = df.nlargest(15, "average_rating")
plt.barh(top_rated["title"], top_rated["average_rating"])
plt.gca().invert_yaxis()
create_chart(20, "Top 15 Highest Rated Books")

# CHART 21: Most Rated Books
plt.figure(figsize=(12, 6))
popular = df.nlargest(15, "ratings_count")
plt.barh(popular["title"], popular["ratings_count"])
plt.gca().invert_yaxis()
create_chart(21, "Top 15 Most Rated Books")

# CHART 22: Longest Books
plt.figure(figsize=(12, 6))
longest = df.nlargest(15, "num_pages")
plt.barh(longest["title"], longest["num_pages"])
plt.gca().invert_yaxis()
create_chart(22, "Top 15 Longest Books")

# CHART 23: Rating Density
plt.figure(figsize=(8, 5))
sns.kdeplot(data=df, x="average_rating", fill=True)
create_chart(23, "Book Rating Density")

# CHART 24: Pages vs Ratings Regression
plt.figure(figsize=(8, 5))
sns.regplot(
    data=df.sample(min(2000, len(df)), random_state=42),
    x="num_pages",
    y="ratings_count",
    scatter_kws={"alpha": 0.3}
)
create_chart(24, "Pages vs Ratings Regression")

# CHART 25: Rating vs Reviews Regression
plt.figure(figsize=(8, 5))
sns.regplot(
    data=df.sample(min(2000, len(df)), random_state=42),
    x="average_rating",
    y="text_reviews_count",
    scatter_kws={"alpha": 0.3}
)
create_chart(25, "Rating vs Text Reviews Regression")

# CHART 26: Publication Year Distribution
plt.figure(figsize=(12, 5))
df["publication_year"].value_counts().sort_index().plot(kind="line")
plt.xlabel("Publication Year")
plt.ylabel("Number of Books")
create_chart(26, "Books Published by Year")

# CHART 27: Average Rating by Publication Year
year_rating = df.groupby("publication_year")["average_rating"].mean()
plt.figure(figsize=(12, 5))
year_rating.plot(kind="line", marker="o")
plt.ylabel("Average Rating")
create_chart(27, "Average Rating by Publication Year")

# CHART 28: Ratings vs Reviews by Language
plt.figure(figsize=(9, 6))
sample = df.sample(min(2000, len(df)), random_state=42)
sns.scatterplot(
    data=sample,
    x="ratings_count",
    y="text_reviews_count",
    hue="language_code"
)
create_chart(28, "Ratings and Reviews by Language")

# CHART 29: Average Rating Pie Chart by Language
plt.figure(figsize=(8, 8))
df["language_code"].value_counts().head(8).plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.ylabel("")
create_chart(29, "Language Distribution of Books")

# CHART 30: Pair Plot
pair_data = df[numeric_cols].dropna()

if len(pair_data) > 2000:
    pair_data = pair_data.sample(2000, random_state=42)

g = sns.pairplot(pair_data, diag_kind="hist")
g.figure.suptitle("Book Dataset Pair Plot", y=1.02)
g.figure.savefig("chart_30.png", dpi=150)
plt.show()
plt.close()

# 5. Final Analysis
print("\n========== FINAL BOOK ANALYSIS ==========")

print("Total Books:", len(df))
print("Average Rating:", round(df["average_rating"].mean(), 2))
print("Average Pages:", round(df["num_pages"].mean(), 2))
print("Total Ratings:", int(df["ratings_count"].sum()))
print("Total Text Reviews:", int(df["text_reviews_count"].sum()))

print("\nHighest Rated Book:")
print(df.loc[df["average_rating"].idxmax(), "title"])

print("\nMost Popular Book:")
print(df.loc[df["ratings_count"].idxmax(), "title"])

print("\nMost Common Language:")
print(df["language_code"].mode()[0])

# 6. Export Results
df.to_csv("book_analysis_output.csv", index=False)

print("\n30 CHARTS GENERATED SUCCESSFULLY!")
print("Book Dataset Analysis Completed!")
