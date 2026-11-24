from pathlib import Path
import os
import re
import warnings
from collections import Counter

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore", category=FutureWarning)

CSV_FILE = "Cartoon_datasets.csv"
OUTPUT_DIR = "Cartoon_30_Charts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------- Load and prepare data --------------------
df = pd.read_csv(CSV_FILE)
df.columns = df.columns.str.strip()

required = {"Name", "Span", "Description", "Rating"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"CSV is missing required columns: {sorted(missing)}")

df["Name"] = df["Name"].astype(str).str.strip()
df["Span"] = df["Span"].fillna("").astype(str).str.strip()
df["Description"] = df["Description"].fillna("").astype(str)
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
df = df.dropna(subset=["Name", "Rating"]).copy()
df = df[df["Name"].ne("")].copy()

def parse_span(value):
    years = [int(x) for x in re.findall(r"\d{4}", str(value))]
    if not years:
        return pd.Series([np.nan, np.nan, False])
    start = years[0]
    # A single year is treated as a one-year run.
    end = years[-1] if len(years) > 1 else start
    ongoing = "– )" in value or "–)" in value or re.search(r"\d{4}\s*[–-]\s*$", value) is not None
    return pd.Series([start, end, ongoing])

df[["Start_Year", "End_Year", "Ongoing"]] = df["Span"].apply(parse_span)
df["Start_Year"] = pd.to_numeric(df["Start_Year"], errors="coerce")
df["End_Year"] = pd.to_numeric(df["End_Year"], errors="coerce")
df["Duration"] = (df["End_Year"] - df["Start_Year"] + 1).clip(lower=1)
df["Decade"] = (df["Start_Year"] // 10 * 10).astype("Int64")
df["Rating_Category"] = pd.cut(
    df["Rating"],
    bins=[0, 6, 7, 8, 9, 10],
    labels=["Below 6", "6–7", "7–8", "8–9", "9–10"],
    include_lowest=True
)
df["Description_Length"] = df["Description"].str.len()
df["Word_Count"] = df["Description"].str.split().str.len()
df["Name_Length"] = df["Name"].str.len()

sns.set_theme(style="whitegrid", context="notebook")
plt.rcParams["figure.figsize"] = (12, 7)
plt.rcParams["axes.titleweight"] = "bold"

chart_number = 0

def save_chart(title, filename):
    global chart_number
    chart_number += 1
    plt.title(title, pad=14)
    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, filename)
    plt.savefig(path, dpi=250, bbox_inches="tight")
    plt.show()
    plt.close()
    print(f"Saved chart {chart_number:02d}: {path}")

def top_n(column, n=15):
    return df.nlargest(n, column).sort_values(column)

# 01. Rating histogram
plt.figure()
sns.histplot(df["Rating"], bins=12, kde=True)
plt.xlabel("Rating")
plt.ylabel("Number of cartoons")
save_chart("01. Cartoon Rating Distribution", "01_rating_distribution.png")

# 02. Rating density
plt.figure()
sns.kdeplot(data=df, x="Rating", fill=True)
plt.xlabel("Rating")
save_chart("02. Rating Density", "02_rating_density.png")

# 03. Top 15 rated cartoons
plot_df = top_n("Rating", 15)
plt.figure(figsize=(12, 8))
sns.barplot(data=plot_df, x="Rating", y="Name")
save_chart("03. Top 15 Highest-Rated Cartoons", "03_top_15_rated.png")

# 04. Bottom 15 rated cartoons
plot_df = df.nsmallest(15, "Rating").sort_values("Rating", ascending=False)
plt.figure(figsize=(12, 8))
sns.barplot(data=plot_df, x="Rating", y="Name")
save_chart("04. Bottom 15 Lowest-Rated Cartoons", "04_bottom_15_rated.png")

# 05. Rating category count
plt.figure()
sns.countplot(data=df, x="Rating_Category", order=["Below 6", "6–7", "7–8", "8–9", "9–10"])
plt.xlabel("Rating category")
plt.ylabel("Number of cartoons")
save_chart("05. Cartoon Count by Rating Category", "05_rating_category_count.png")

# 06. Rating category percentage
counts = df["Rating_Category"].value_counts().sort_index().dropna()
plt.figure()
plt.pie(counts, labels=counts.index.astype(str), autopct="%1.1f%%", startangle=90)
plt.ylabel("")
save_chart("06. Rating Category Percentage", "06_rating_category_pie.png")

# 07. Box plot of ratings
plt.figure()
sns.boxplot(x=df["Rating"])
save_chart("07. Rating Box Plot", "07_rating_boxplot.png")

# 08. Violin plot of ratings
plt.figure()
sns.violinplot(y=df["Rating"], inner="quartile")
save_chart("08. Rating Violin Plot", "08_rating_violin.png")

# 09. Start year frequency
start_counts = df["Start_Year"].dropna().astype(int).value_counts().sort_index()
plt.figure()
plt.plot(start_counts.index, start_counts.values, marker="o")
plt.xlabel("Starting year")
plt.ylabel("Number of cartoons")
save_chart("09. Cartoon Starts by Year", "09_start_year_frequency.png")

# 10. End year frequency
end_counts = df["End_Year"].dropna().astype(int).value_counts().sort_index()
plt.figure()
plt.plot(end_counts.index, end_counts.values, marker="o")
plt.xlabel("Ending year")
plt.ylabel("Number of cartoons")
save_chart("10. Cartoon Endings by Year", "10_end_year_frequency.png")

# 11. Starts by decade
decade_counts = df["Decade"].dropna().astype(int).value_counts().sort_index()
plt.figure()
sns.barplot(x=decade_counts.index.astype(str), y=decade_counts.values)
plt.xlabel("Starting decade")
plt.ylabel("Number of cartoons")
save_chart("11. Cartoon Starts by Decade", "11_start_decade.png")

# 12. Average rating by starting decade
decade_rating = df.dropna(subset=["Decade"]).groupby("Decade", observed=True)["Rating"].mean()
plt.figure()
sns.barplot(x=decade_rating.index.astype(str), y=decade_rating.values)
plt.xlabel("Starting decade")
plt.ylabel("Average rating")
save_chart("12. Average Rating by Decade", "12_average_rating_decade.png")

# 13. Number of ongoing vs completed shows
ongoing_counts = df["Ongoing"].map({True: "Ongoing", False: "Completed"}).value_counts()
plt.figure()
plt.pie(ongoing_counts, labels=ongoing_counts.index, autopct="%1.1f%%", startangle=90)
plt.ylabel("")
save_chart("13. Ongoing vs Completed Shows", "13_ongoing_completed.png")

# 14. Duration distribution
plt.figure()
sns.histplot(df["Duration"].dropna(), bins=12, kde=True)
plt.xlabel("Recorded duration (years)")
plt.ylabel("Number of cartoons")
save_chart("14. Cartoon Duration Distribution", "14_duration_distribution.png")

# 15. Duration box plot
plt.figure()
sns.boxplot(x=df["Duration"].dropna())
plt.xlabel("Recorded duration (years)")
save_chart("15. Duration Box Plot", "15_duration_boxplot.png")

# 16. Rating vs duration
plot_df = df.dropna(subset=["Duration"])
plt.figure()
sns.scatterplot(data=plot_df, x="Duration", y="Rating", hue="Ongoing", alpha=0.8)
plt.xlabel("Recorded duration (years)")
save_chart("16. Rating vs Duration", "16_rating_vs_duration.png")

# 17. Average rating by duration
duration_rating = df.dropna(subset=["Duration"]).groupby("Duration")["Rating"].mean()
plt.figure()
sns.lineplot(x=duration_rating.index, y=duration_rating.values, marker="o")
plt.xlabel("Recorded duration (years)")
plt.ylabel("Average rating")
save_chart("17. Average Rating by Duration", "17_average_rating_duration.png")

# 18. Rating vs start year
plot_df = df.dropna(subset=["Start_Year"])
plt.figure()
sns.scatterplot(data=plot_df, x="Start_Year", y="Rating", alpha=0.8)
plt.xlabel("Starting year")
save_chart("18. Rating vs Starting Year", "18_rating_vs_start_year.png")

# 19. Rating vs end year
plot_df = df.dropna(subset=["End_Year"])
plt.figure()
sns.scatterplot(data=plot_df, x="End_Year", y="Rating", alpha=0.8)
plt.xlabel("Ending year")
save_chart("19. Rating vs Ending Year", "19_rating_vs_end_year.png")

# 20. Description length distribution
plt.figure()
sns.histplot(df["Description_Length"], bins=15, kde=True)
plt.xlabel("Description length (characters)")
save_chart("20. Description Length Distribution", "20_description_length.png")

# 21. Word count distribution
plt.figure()
sns.histplot(df["Word_Count"], bins=15, kde=True)
plt.xlabel("Words in description")
save_chart("21. Description Word Count Distribution", "21_word_count.png")

# 22. Description length vs rating
plt.figure()
sns.scatterplot(data=df, x="Description_Length", y="Rating")
plt.xlabel("Description length (characters)")
save_chart("22. Description Length vs Rating", "22_description_length_vs_rating.png")

# 23. Word count vs rating
plt.figure()
sns.regplot(data=df, x="Word_Count", y="Rating", scatter_kws={"alpha": 0.65})
plt.xlabel("Words in description")
save_chart("23. Description Word Count vs Rating", "23_word_count_vs_rating.png")

# 24. Cartoon title length distribution
plt.figure()
sns.histplot(df["Name_Length"], bins=12, kde=True)
plt.xlabel("Cartoon title length (characters)")
save_chart("24. Cartoon Title Length", "24_title_length.png")

# 25. Top 15 longest-running cartoons (recorded span)
plot_df = df.nlargest(15, "Duration").sort_values("Duration")
plt.figure(figsize=(12, 8))
sns.barplot(data=plot_df, x="Duration", y="Name")
plt.xlabel("Recorded duration (years)")
save_chart("25. Top 15 Longest Recorded Runs", "25_longest_runs.png")

# 26. Top 15 shortest recorded runs
plot_df = df.nsmallest(15, "Duration").sort_values("Duration", ascending=False)
plt.figure(figsize=(12, 8))
sns.barplot(data=plot_df, x="Duration", y="Name")
plt.xlabel("Recorded duration (years)")
save_chart("26. 15 Shortest Recorded Runs", "26_shortest_runs.png")

# 27. Correlation heatmap
numeric_cols = ["Rating", "Start_Year", "End_Year", "Duration",
                "Description_Length", "Word_Count", "Name_Length"]
corr = df[numeric_cols].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", square=True)
save_chart("27. Numeric Feature Correlation Heatmap", "27_correlation_heatmap.png")

# 28. Pair plot of numeric variables
pair_cols = ["Rating", "Duration", "Description_Length", "Word_Count"]
pair = sns.pairplot(df[pair_cols].dropna(), diag_kind="hist")
pair.fig.suptitle("28. Pairwise Relationships", y=1.02)
pair.savefig(os.path.join(OUTPUT_DIR, "28_pairplot.png"), dpi=200, bbox_inches="tight")
plt.show()
plt.close("all")
chart_number += 1
print(f"Saved chart {chart_number:02d}: {OUTPUT_DIR}/28_pairplot.png")

# 29. Most frequent words in descriptions
stop_words = {
    "this", "that", "with", "from", "their", "they", "them", "when",
    "where", "while", "into", "over", "after", "before", "about",
    "have", "been", "will", "must", "once", "also", "than", "which",
    "young", "team", "world", "story", "series", "show", "life"
}
tokens = []
for description in df["Description"]:
    tokens.extend(re.findall(r"\b[a-zA-Z]{4,}\b", description.lower()))
word_counts = Counter(word for word in tokens if word not in stop_words)
common_words = word_counts.most_common(20)
word_df = pd.DataFrame(common_words, columns=["Word", "Frequency"]).sort_values("Frequency")
plt.figure(figsize=(12, 8))
sns.barplot(data=word_df, x="Frequency", y="Word")
plt.xlabel("Frequency")
save_chart("29. Most Common Description Words", "29_common_description_words.png")

# 30. Rating ranking curve across all cartoons
ranked = df.sort_values("Rating", ascending=False).reset_index(drop=True)
plt.figure(figsize=(12, 7))
plt.plot(np.arange(1, len(ranked) + 1), ranked["Rating"], marker=".", linewidth=1)
plt.xlabel("Cartoon rank (highest to lowest)")
plt.ylabel("Rating")
save_chart("30. Cartoon Rating Ranking Curve", "30_rating_ranking_curve.png")

# -------------------- Summary and exports --------------------
summary = pd.DataFrame({
    "Metric": [
        "Number of cartoons",
        "Average rating",
        "Median rating",
        "Highest rating",
        "Lowest rating",
        "Highest-rated cartoon",
        "Lowest-rated cartoon",
        "Ongoing cartoons",
        "Completed cartoons"
    ],
    "Value": [
        len(df),
        round(df["Rating"].mean(), 2),
        round(df["Rating"].median(), 2),
        df["Rating"].max(),
        df["Rating"].min(),
        df.loc[df["Rating"].idxmax(), "Name"],
        df.loc[df["Rating"].idxmin(), "Name"],
        int(df["Ongoing"].sum()),
        int((~df["Ongoing"]).sum())
    ]
})

df.to_csv(os.path.join(OUTPUT_DIR, "cleaned_cartoon_dataset.csv"), index=False)
summary.to_csv(os.path.join(OUTPUT_DIR, "cartoon_analysis_summary.csv"), index=False)

print("\n" + "=" * 55)
print("CARTOON DATASET ANALYSIS COMPLETED")
print("=" * 55)
print(summary.to_string(index=False))
print(f"\nCharts generated: {chart_number}")
print(f"Output folder: {os.path.abspath(OUTPUT_DIR)}")
print("Note: Duration is calculated from the years written in Span.")
print("For ongoing titles, the listed start year is not extended to the present.")
path = Path("/mnt/data/cartoon_analysis_30_charts.py")
path.write_text(code, encoding="utf-8")
print(f"Created: {path}")
