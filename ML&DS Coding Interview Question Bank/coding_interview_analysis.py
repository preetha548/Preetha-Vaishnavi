
import os
import re
import warnings
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

warnings.filterwarnings("ignore")

# ==========================================
# 1. FILE PATHS
# ==========================================

FILE_PATH = (
    r"C:\Users\USER PC\Desktop\ML&DS Coding Interview Question Bank"
    r"\coding_interview_question_bank.csv"
)

BASE_DIR = os.path.dirname(FILE_PATH)

OUTPUT_DIR = os.path.join(
    BASE_DIR, "ML_DS_Analysis"
)

CHART_DIR = os.path.join(
    OUTPUT_DIR, "Interview_30_Unique_Charts"
)

os.makedirs(CHART_DIR, exist_ok=True)

sns.set_theme(style="whitegrid", palette="viridis")

# ==========================================
# 2. LOAD DATASET
# ==========================================

if not os.path.exists(FILE_PATH):
    raise FileNotFoundError(
        f"CSV file not found: {FILE_PATH}"
    )

df = pd.read_csv(FILE_PATH)

if df.empty:
    raise ValueError("The CSV dataset is empty.")

df.columns = (
    df.columns.astype(str)
    .str.strip()
    .str.replace(r"\s+", "_", regex=True)
)

print("\n========== ML & DS INTERVIEW QUESTION BANK ==========")
print("\nDataset Shape:", df.shape)
print("\nColumn Names:\n", df.columns.tolist())
print("\nFirst Five Records:\n", df.head())

# ==========================================
# 3. DETECT DATA TYPES
# ==========================================

numeric_df = df.copy()

for col in numeric_df.columns:
    numeric_df[col] = pd.to_numeric(
        numeric_df[col], errors="coerce"
    )

numeric_cols = [
    col for col in numeric_df.columns
    if numeric_df[col].notna().sum() > 0
]

categorical_cols = [
    col for col in df.columns
    if col not in numeric_cols
]

# Find columns using their names
def find_column(keywords):
    for col in df.columns:
        name = col.lower().replace("_", " ")
        if any(word in name for word in keywords):
            return col
    return None

category_col = find_column([
    "category", "domain", "subject", "field"
])

difficulty_col = find_column([
    "difficulty", "level", "complexity"
])

topic_col = find_column([
    "topic", "concept", "technology", "skill"
])

question_col = find_column([
    "question", "problem", "description", "title"
])

company_col = find_column([
    "company", "organization", "employer"
])

language_col = find_column([
    "language", "programming_language"
])

# ==========================================
# 4. HELPER FUNCTIONS
# ==========================================

chart_number = 0
summary = []

def save_chart(name):
    global chart_number

    chart_number += 1

    filename = (
        f"{chart_number:02d}_{name}.png"
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(CHART_DIR, filename),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    summary.append(filename)
    print("Created:", filename)


def categorical_values(col=None, limit=15):
    if col is not None and col in df.columns:
        return (
            df[col].fillna("Unknown")
            .astype(str)
            .value_counts()
            .head(limit)
        )

    if categorical_cols:
        return (
            df[categorical_cols[0]]
            .fillna("Unknown")
            .astype(str)
            .value_counts()
            .head(limit)
        )

    return pd.Series({"No categorical data": 1})


def numeric_values(col=None):
    if col is not None and col in df.columns:
        values = pd.to_numeric(
            df[col], errors="coerce"
        ).dropna()

        if len(values) > 0:
            return values

    if numeric_cols:
        return numeric_df[numeric_cols[0]].dropna()

    return pd.Series(np.arange(1, len(df) + 1))


def get_question_text():
    if question_col:
        return df[question_col].fillna("").astype(str)

    for col in categorical_cols:
        if df[col].astype(str).str.len().mean() > 15:
            return df[col].fillna("").astype(str)

    return pd.Series([""] * len(df))


question_text = get_question_text()

# ==========================================
# 5. CHART 01 - DATASET OVERVIEW
# ==========================================

plt.figure(figsize=(9, 5))

sns.barplot(
    x=["Rows", "Columns", "Numeric", "Categorical"],
    y=[
        len(df),
        len(df.columns),
        len(numeric_cols),
        len(categorical_cols)
    ]
)

plt.title("Dataset Overview")
plt.ylabel("Count")
save_chart("dataset_overview")

# ==========================================
# 6. CHART 02 - CATEGORY DISTRIBUTION
# ==========================================

values = categorical_values(category_col)

plt.figure(figsize=(10, 6))
sns.barplot(x=values.values, y=values.index)
plt.title("Question Category Distribution")
plt.xlabel("Number of Records")
save_chart("category_distribution")

# ==========================================
# 7. CHART 03 - DIFFICULTY LEVEL
# ==========================================

values = categorical_values(difficulty_col)

plt.figure(figsize=(8, 5))
plt.pie(
    values.values,
    labels=values.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Difficulty Level Distribution")
save_chart("difficulty_distribution")

# ==========================================
# 8. CHART 04 - TOPIC ANALYSIS
# ==========================================

values = categorical_values(topic_col)

plt.figure(figsize=(10, 6))
sns.barplot(x=values.values, y=values.index)
plt.title("Top Interview Topics")
plt.xlabel("Frequency")
save_chart("top_topics")

# ==========================================
# 9. CHART 05 - COMPANY ANALYSIS
# ==========================================

values = categorical_values(company_col)

plt.figure(figsize=(10, 6))
sns.barplot(x=values.values, y=values.index)
plt.title("Company-wise Interview Questions")
plt.xlabel("Number of Questions")
save_chart("company_analysis")

# ==========================================
# 10. CHART 06 - DONUT CHART
# ==========================================

values = categorical_values(category_col)

plt.figure(figsize=(8, 8))
plt.pie(
    values.values,
    labels=values.index,
    autopct="%1.1f%%",
    wedgeprops={"width": 0.4},
    startangle=90
)
plt.title("Question Category Donut Chart")
save_chart("category_donut")

# ==========================================
# 11. CHART 07 - PROGRAMMING LANGUAGE
# ==========================================

values = categorical_values(language_col)

plt.figure(figsize=(10, 5))
sns.barplot(x=values.index, y=values.values)
plt.title("Programming Language Distribution")
plt.xticks(rotation=35, ha="right")
save_chart("programming_language")

# ==========================================
# 12. CHART 08 - HISTOGRAM
# ==========================================

v = numeric_values()

plt.figure(figsize=(9, 5))
sns.histplot(v, bins=20, kde=True)
plt.title("Numeric Feature Distribution")
save_chart("numeric_histogram")

# ==========================================
# 13. CHART 09 - BOX PLOT
# ==========================================

plt.figure(figsize=(9, 5))
sns.boxplot(x=v)
plt.title("Numeric Feature Box Plot")
save_chart("numeric_boxplot")

# ==========================================
# 14. CHART 10 - VIOLIN PLOT
# ==========================================

plt.figure(figsize=(9, 5))
sns.violinplot(x=v)
plt.title("Numeric Feature Violin Plot")
save_chart("numeric_violin")

# ==========================================
# 15. CHART 11 - DENSITY PLOT
# ==========================================

plt.figure(figsize=(9, 5))

if v.nunique() > 1:
    sns.kdeplot(v, fill=True)
else:
    sns.histplot(v, kde=False)

plt.title("Numeric Density Distribution")
save_chart("density_distribution")

# ==========================================
# 16. CHART 12 - CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(10, 7))

if len(numeric_cols) >= 2:
    corr = numeric_df[numeric_cols].corr()
    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        fmt=".2f"
    )
else:
    plt.text(
        0.5, 0.5,
        "At least two numeric columns are required",
        ha="center", va="center"
    )

plt.title("Feature Correlation Heatmap")
save_chart("correlation_heatmap")

# ==========================================
# 17. CHART 13 - MISSING VALUES
# ==========================================

missing = df.isnull().sum()

plt.figure(figsize=(10, 6))
sns.barplot(x=missing.values, y=missing.index)
plt.title("Missing Values by Column")
plt.xlabel("Missing Count")
save_chart("missing_values")

# ==========================================
# 18. CHART 14 - MISSING PERCENTAGE
# ==========================================

missing_pct = (
    df.isnull().mean() * 100
).sort_values(ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x=missing_pct.values, y=missing_pct.index)
plt.title("Missing Data Percentage")
plt.xlabel("Missing Percentage")
save_chart("missing_percentage")

# ==========================================
# 19. CHART 15 - DUPLICATE RECORDS
# ==========================================

duplicate_count = int(df.duplicated().sum())

plt.figure(figsize=(7, 5))
plt.bar(
    ["Unique Records", "Duplicate Records"],
    [len(df) - duplicate_count, duplicate_count]
)
plt.title("Duplicate Record Analysis")
plt.ylabel("Count")
save_chart("duplicate_analysis")

# ==========================================
# 20. CHART 16 - COLUMN CARDINALITY
# ==========================================

cardinality = df.nunique().sort_values(
    ascending=False
)

plt.figure(figsize=(10, 6))
sns.barplot(x=cardinality.values, y=cardinality.index)
plt.title("Unique Values in Each Column")
plt.xlabel("Unique Count")
save_chart("column_cardinality")

# ==========================================
# 21. CHART 17 - STACKED BAR
# ==========================================

first_cat = (
    category_col if category_col else
    categorical_cols[0] if categorical_cols else None
)

second_cat = (
    difficulty_col if difficulty_col else
    categorical_cols[1] if len(categorical_cols) > 1 else None
)

plt.figure(figsize=(10, 6))

if first_cat and second_cat and first_cat != second_cat:
    cross = pd.crosstab(
        df[first_cat].fillna("Unknown"),
        df[second_cat].fillna("Unknown")
    )

    cross.plot(kind="bar", stacked=True, ax=plt.gca())
    plt.legend(title=second_cat, bbox_to_anchor=(1.02, 1))
else:
    plt.text(
        0.5, 0.5,
        "Two different categorical columns are required",
        ha="center", va="center"
    )

plt.title("Category vs Difficulty Stacked Analysis")
save_chart("stacked_bar")

# ==========================================
# 22. CHART 18 - AREA CHART
# ==========================================

plt.figure(figsize=(9, 5))
v.reset_index(drop=True).plot.area()
plt.title("Numeric Feature Area Chart")
plt.xlabel("Record Index")
save_chart("area_chart")

# ==========================================
# 23. CHART 19 - LOLLIPOP CHART
# ==========================================

values = categorical_values(category_col)

plt.figure(figsize=(10, 6))
plt.hlines(
    y=values.index,
    xmin=0,
    xmax=values.values
)
plt.plot(values.values, values.index, "o")
plt.title("Category Lollipop Chart")
plt.xlabel("Frequency")
save_chart("lollipop_chart")

# ==========================================
# 24. CHART 20 - SCATTER PLOT
# ==========================================

plt.figure(figsize=(9, 6))

if len(numeric_cols) >= 2:
    x = numeric_df[numeric_cols[0]]
    y = numeric_df[numeric_cols[1]]
    valid = x.notna() & y.notna()

    plt.scatter(x[valid], y[valid], alpha=0.6)
    plt.xlabel(numeric_cols[0])
    plt.ylabel(numeric_cols[1])
else:
    plt.scatter(range(len(v)), v, alpha=0.6)
    plt.xlabel("Record Index")
    plt.ylabel("Numeric Value")

plt.title("Feature Scatter Plot")
save_chart("scatter_plot")

# ==========================================
# 25. CHART 21 - HEXBIN PLOT
# ==========================================

plt.figure(figsize=(9, 6))

if len(numeric_cols) >= 2:
    x = numeric_df[numeric_cols[0]]
    y = numeric_df[numeric_cols[1]]
    valid = x.notna() & y.notna()

    if valid.sum() > 0:
        plt.hexbin(
            x[valid], y[valid],
            gridsize=20,
            cmap="viridis",
            mincnt=1
        )
        plt.colorbar(label="Record Count")
    else:
        plt.text(0.5, 0.5, "No valid numeric pairs",
                 ha="center", va="center")
else:
    plt.text(
        0.5, 0.5,
        "Two numeric columns are required",
        ha="center", va="center"
    )

plt.title("Numeric Feature Hexbin Plot")
save_chart("hexbin_plot")

# ==========================================
# 26. CHART 22 - ECDF
# ==========================================

plt.figure(figsize=(9, 5))
sns.ecdfplot(v)
plt.title("Empirical Cumulative Distribution")
plt.xlabel("Value")
save_chart("ecdf_plot")

# ==========================================
# 27. CHART 23 - QUESTION LENGTH
# ==========================================

question_lengths = question_text.str.len()

plt.figure(figsize=(9, 5))
sns.histplot(question_lengths, bins=20, kde=True)
plt.title("Interview Question Length Distribution")
plt.xlabel("Characters")

if question_lengths.max() == 0:
    plt.text(
        0.5, 0.5,
        "No question-text column detected",
        transform=plt.gca().transAxes,
        ha="center"
    )

save_chart("question_length")

# ==========================================
# 28. CHART 24 - WORD COUNT
# ==========================================

word_counts = question_text.apply(
    lambda x: len(str(x).split())
)

plt.figure(figsize=(9, 5))
sns.boxplot(x=word_counts)
plt.title("Question Word Count Analysis")
plt.xlabel("Number of Words")
save_chart("question_word_count")

# ==========================================
# 29. CHART 25 - FREQUENT WORDS
# ==========================================

from collections import Counter

all_text = " ".join(
    question_text.astype(str).tolist()
).lower()

words = re.findall(r"\b[a-zA-Z]{3,}\b", all_text)

stop_words = {
    "the", "and", "for", "with", "what",
    "how", "are", "you", "this", "that",
    "from", "can", "use", "using", "write"
}

filtered_words = [
    word for word in words
    if word not in stop_words
]

common_words = Counter(filtered_words).most_common(15)

plt.figure(figsize=(10, 6))

if common_words:
    word_names, word_counts = zip(*common_words)
    sns.barplot(x=list(word_counts), y=list(word_names))
else:
    plt.text(
        0.5, 0.5,
        "No suitable question text detected",
        ha="center", va="center"
    )

plt.title("Most Frequent Interview Question Words")
save_chart("frequent_words")

# ==========================================
# 30. CHART 26 - BUBBLE CHART
# ==========================================

plt.figure(figsize=(9, 6))

if len(numeric_cols) >= 2:
    x = numeric_df[numeric_cols[0]]
    y = numeric_df[numeric_cols[1]]
    valid = x.notna() & y.notna()

    sizes = np.full(valid.sum(), 80)

    plt.scatter(
        x[valid],
        y[valid],
        s=sizes,
        alpha=0.5
    )
    plt.xlabel(numeric_cols[0])
    plt.ylabel(numeric_cols[1])
else:
    plt.scatter(
        range(len(v)),
        v,
        s=np.maximum(np.abs(v), 1) * 10,
        alpha=0.5
    )
    plt.xlabel("Record Index")
    plt.ylabel("Numeric Value")

plt.title("Feature Bubble Chart")
save_chart("bubble_chart")

# ==========================================
# 31. CHART 27 - CUMULATIVE DISTRIBUTION
# ==========================================

sorted_values = np.sort(v)

plt.figure(figsize=(9, 5))
plt.plot(
    sorted_values,
    np.arange(1, len(sorted_values) + 1) / len(sorted_values)
)
plt.title("Cumulative Distribution Curve")
plt.xlabel("Value")
plt.ylabel("Cumulative Proportion")
save_chart("cumulative_distribution")

# ==========================================
# 32. CHART 28 - STEP CHART
# ==========================================

plt.figure(figsize=(9, 5))
plt.step(
    range(len(v)),
    v.values,
    where="mid"
)
plt.title("Numeric Feature Step Chart")
plt.xlabel("Record Index")
plt.ylabel("Value")
save_chart("step_chart")

# ==========================================
# 33. CHART 29 - Q-Q PLOT
# ==========================================

plt.figure(figsize=(8, 6))

if len(v) >= 2 and v.nunique() > 1:
    stats.probplot(v, dist="norm", plot=plt)
else:
    plt.text(
        0.5, 0.5,
        "Insufficient variation for Q-Q plot",
        ha="center", va="center"
    )

plt.title("Normal Distribution Q-Q Plot")
save_chart("qq_plot")

# ==========================================
# 34. CHART 30 - DATASET DASHBOARD
# ==========================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

values = categorical_values(category_col, 8)
sns.barplot(
    x=values.values,
    y=values.index,
    ax=axes[0, 0]
)
axes[0, 0].set_title("Category Overview")

sns.histplot(v, bins=15, ax=axes[0, 1])
axes[0, 1].set_title("Numeric Distribution")

missing.sort_values(ascending=False).head(10).plot(
    kind="bar",
    ax=axes[1, 0]
)
axes[1, 0].set_title("Missing Values")

axes[1, 1].axis("off")
axes[1, 1].text(
    0.05, 0.8,
    f"Total Records: {len(df)}\n"
    f"Total Columns: {len(df.columns)}\n"
    f"Numeric Columns: {len(numeric_cols)}\n"
    f"Categorical Columns: {len(categorical_cols)}\n"
    f"Duplicate Records: {duplicate_count}",
    fontsize=13,
    va="top"
)
axes[1, 1].set_title("Dataset Summary")

fig.suptitle("ML & DS Interview Question Bank Dashboard")
fig.tight_layout()
fig.savefig(
    os.path.join(CHART_DIR, "30_dataset_dashboard.png"),
    dpi=300,
    bbox_inches="tight"
)
plt.close(fig)

summary.append("30_dataset_dashboard.png")
chart_number = 30

# ==========================================
# 35. SAVE CLEANED DATA AND SUMMARY
# ==========================================

df.to_csv(
    os.path.join(
        OUTPUT_DIR,
        "cleaned_interview_dataset.csv"
    ),
    index=False
)

with open(
    os.path.join(OUTPUT_DIR, "analysis_summary.txt"),
    "w",
    encoding="utf-8"
) as file:

    file.write("ML & DS CODING INTERVIEW QUESTION BANK\n")
    file.write("=" * 50 + "\n")
    file.write(f"Total Records: {len(df)}\n")
    file.write(f"Total Columns: {len(df.columns)}\n")
    file.write(f"Numeric Columns: {len(numeric_cols)}\n")
    file.write(f"Categorical Columns: {len(categorical_cols)}\n")
    file.write(f"Duplicate Records: {duplicate_count}\n")
    file.write(f"Charts Generated: {len(summary)}\n\n")

    file.write("GENERATED CHARTS\n")
    for item in summary:
        file.write(item + "\n")

print("\n==========================================")
print("ML & DS ANALYSIS COMPLETED")
print("==========================================")
print("Total Charts:", len(summary))
print("Output Folder:", CHART_DIR)
print("Summary:", os.path.join(OUTPUT_DIR, "analysis_summary.txt"))
print("\nAll tasks completed successfully!")
