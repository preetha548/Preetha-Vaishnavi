
import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore")
sns.set_theme(style="whitegrid")

# ==========================================
# 1. LOAD DATASET
# ==========================================

folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder, "cure_data.csv")

print("Dataset path:", file_path)

if not os.path.exists(file_path):
    print("ERROR: cure_data.csv not found!")
    print("Files in project folder:", os.listdir(folder))
    raise SystemExit

df = pd.read_csv(file_path, header=None)

if df.shape[1] != 3:
    raise ValueError(
        "Expected 3 columns: Feature_1, Feature_2, Target. "
        f"Found {df.shape[1]} columns."
    )

df.columns = ["Feature_1", "Feature_2", "Target"]

for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

if df.empty:
    raise ValueError("Dataset contains no valid numeric records.")

print("\nDATASET LOADED SUCCESSFULLY")
print(df.head())
print("\nDataset Shape:", df.shape)
print("\nDataset Description:")
print(df.describe())
print("\nTarget Distribution:")
print(df["Target"].value_counts().sort_index())

# ==========================================
# 2. OUTPUT FOLDER
# ==========================================

output_folder = os.path.join(folder, "Cure_30_Charts")
os.makedirs(output_folder, exist_ok=True)

sample = df.sample(
    n=min(2000, len(df)),
    random_state=42
)

chart_count = 0

def save_chart(name):
    global chart_count

    chart_count += 1

    filename = f"{chart_count:02d}_{name}.png"
    path = os.path.join(output_folder, filename)

    plt.tight_layout()
    plt.savefig(path, dpi=150, bbox_inches="tight")
    print(f"Saved {chart_count}/30: {filename}")

    plt.show()
    plt.close()


# ==========================================
# 01. COUNT PLOT
# ==========================================

plt.figure(figsize=(9, 5))
sns.countplot(
    data=df, x="Target",
    hue="Target", palette="viridis",
    legend=False
)
plt.title("01. Target Class Distribution")
plt.xlabel("Target")
plt.ylabel("Count")
save_chart("count_plot")


# ==========================================
# 02. PIE CHART
# ==========================================

counts = df["Target"].value_counts().sort_index()

plt.figure(figsize=(8, 8))
plt.pie(
    counts.values,
    labels=counts.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("02. Target Class Pie Chart")
save_chart("pie_chart")


# ==========================================
# 03. DONUT CHART
# ==========================================

plt.figure(figsize=(8, 8))
plt.pie(
    counts.values,
    labels=counts.index,
    autopct="%1.1f%%",
    wedgeprops={"width": 0.4},
    startangle=90
)
plt.title("03. Donut Chart")
save_chart("donut_chart")


# ==========================================
# 04. FEATURE 1 HISTOGRAM
# ==========================================

plt.figure(figsize=(9, 5))
plt.hist(df["Feature_1"], bins=40, edgecolor="black")
plt.title("04. Feature 1 Histogram")
plt.xlabel("Feature 1")
plt.ylabel("Frequency")
save_chart("feature1_histogram")


# ==========================================
# 05. FEATURE 2 HISTOGRAM
# ==========================================

plt.figure(figsize=(9, 5))
plt.hist(df["Feature_2"], bins=40, edgecolor="black")
plt.title("05. Feature 2 Histogram")
plt.xlabel("Feature 2")
plt.ylabel("Frequency")
save_chart("feature2_histogram")


# ==========================================
# 06. FEATURE 1 KDE
# ==========================================

plt.figure(figsize=(9, 5))
sns.kdeplot(data=df, x="Feature_1", fill=True)
plt.title("06. Feature 1 Density Plot")
save_chart("feature1_kde")


# ==========================================
# 07. FEATURE 2 KDE
# ==========================================

plt.figure(figsize=(9, 5))
sns.kdeplot(data=df, x="Feature_2", fill=True)
plt.title("07. Feature 2 Density Plot")
save_chart("feature2_kde")


# ==========================================
# 08. SCATTER PLOT
# ==========================================

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=sample,
    x="Feature_1",
    y="Feature_2",
    hue="Target",
    palette="tab10",
    alpha=0.7
)
plt.title("08. Feature Scatter Plot")
save_chart("scatter_plot")


# ==========================================
# 09. HEXBIN PLOT
# ==========================================

plt.figure(figsize=(9, 6))
plt.hexbin(
    df["Feature_1"],
    df["Feature_2"],
    gridsize=40,
    mincnt=1,
    cmap="viridis"
)
plt.colorbar(label="Frequency")
plt.title("09. Hexbin Plot")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
save_chart("hexbin_plot")


# ==========================================
# 10. 2D HISTOGRAM
# ==========================================

plt.figure(figsize=(9, 6))
hist = plt.hist2d(
    df["Feature_1"],
    df["Feature_2"],
    bins=40,
    cmap="plasma"
)
plt.colorbar(hist[3], label="Frequency")
plt.title("10. Two Dimensional Histogram")
save_chart("2d_histogram")


# ==========================================
# 11. FEATURE 1 BOX PLOT
# ==========================================

plt.figure(figsize=(10, 6))
sns.boxplot(
    data=df,
    x="Target",
    y="Feature_1",
    hue="Target",
    legend=False
)
plt.title("11. Feature 1 Box Plot")
save_chart("feature1_boxplot")


# ==========================================
# 12. FEATURE 2 BOX PLOT
# ==========================================

plt.figure(figsize=(10, 6))
sns.boxplot(
    data=df,
    x="Target",
    y="Feature_2",
    hue="Target",
    legend=False
)
plt.title("12. Feature 2 Box Plot")
save_chart("feature2_boxplot")


# ==========================================
# 13. FEATURE 1 VIOLIN PLOT
# ==========================================

plt.figure(figsize=(10, 6))
sns.violinplot(
    data=df,
    x="Target",
    y="Feature_1",
    hue="Target",
    legend=False
)
plt.title("13. Feature 1 Violin Plot")
save_chart("feature1_violin")


# ==========================================
# 14. FEATURE 2 VIOLIN PLOT
# ==========================================

plt.figure(figsize=(10, 6))
sns.violinplot(
    data=df,
    x="Target",
    y="Feature_2",
    hue="Target",
    legend=False
)
plt.title("14. Feature 2 Violin Plot")
save_chart("feature2_violin")


# ==========================================
# 15. STRIP PLOT
# ==========================================

plt.figure(figsize=(10, 6))
sns.stripplot(
    data=sample,
    x="Target",
    y="Feature_1",
    jitter=True,
    alpha=0.5
)
plt.title("15. Strip Plot")
save_chart("strip_plot")


# ==========================================
# 16. SWARM PLOT
# ==========================================

small_sample = sample.sample(
    n=min(350, len(sample)),
    random_state=42
)

plt.figure(figsize=(10, 6))
sns.swarmplot(
    data=small_sample,
    x="Target",
    y="Feature_2",
    size=3
)
plt.title("16. Swarm Plot")
save_chart("swarm_plot")


# ==========================================
# 17. CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(8, 6))
sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)
plt.title("17. Correlation Heatmap")
save_chart("correlation_heatmap")


# ==========================================
# 18. PAIR PLOT
# ==========================================

pair = sns.pairplot(
    sample,
    hue="Target",
    diag_kind="hist",
    corner=True
)
pair.fig.suptitle("18. Pair Plot", y=1.02)

pair.savefig(
    os.path.join(output_folder, "18_pair_plot.png"),
    dpi=150,
    bbox_inches="tight"
)
plt.show()
plt.close("all")

chart_count += 1
print("Saved 18/30: 18_pair_plot.png")


# ==========================================
# 19. FEATURE 1 ECDF
# ==========================================

plt.figure(figsize=(9, 5))
sns.ecdfplot(data=df, x="Feature_1")
plt.title("19. Feature 1 ECDF")
save_chart("feature1_ecdf")


# ==========================================
# 20. FEATURE 2 ECDF
# ==========================================

plt.figure(figsize=(9, 5))
sns.ecdfplot(data=df, x="Feature_2")
plt.title("20. Feature 2 ECDF")
save_chart("feature2_ecdf")


# ==========================================
# 21. CUMULATIVE HISTOGRAM
# ==========================================

plt.figure(figsize=(9, 5))
plt.hist(
    df["Feature_1"],
    bins=40,
    cumulative=True,
    density=True,
    histtype="step",
    linewidth=2
)
plt.title("21. Cumulative Histogram")
save_chart("cumulative_histogram")


# ==========================================
# 22. CLASS-WISE MEAN
# ==========================================

means = df.groupby("Target")[
    ["Feature_1", "Feature_2"]
].mean()

means.plot(kind="bar", figsize=(10, 6))
plt.title("22. Class-Wise Mean")
plt.xlabel("Target Class")
plt.ylabel("Mean")
plt.xticks(rotation=0)
save_chart("classwise_mean")


# ==========================================
# 23. CLASS-WISE MEDIAN
# ==========================================

medians = df.groupby("Target")[
    ["Feature_1", "Feature_2"]
].median()

medians.plot(kind="bar", figsize=(10, 6))
plt.title("23. Class-Wise Median")
plt.xlabel("Target Class")
plt.ylabel("Median")
plt.xticks(rotation=0)
save_chart("classwise_median")


# ==========================================
# 24. STANDARD DEVIATION
# ==========================================

std_values = df.groupby("Target")[
    ["Feature_1", "Feature_2"]
].std()

std_values.plot(kind="bar", figsize=(10, 6))
plt.title("24. Class-Wise Standard Deviation")
plt.xlabel("Target Class")
plt.ylabel("Standard Deviation")
plt.xticks(rotation=0)
save_chart("standard_deviation")


# ==========================================
# 25. MEAN LINE CHART
# ==========================================

plt.figure(figsize=(10, 6))
plt.plot(
    means.index, means["Feature_1"],
    marker="o", label="Feature 1"
)
plt.plot(
    means.index, means["Feature_2"],
    marker="s", label="Feature 2"
)
plt.title("25. Class-Wise Mean Line Chart")
plt.xlabel("Target Class")
plt.ylabel("Mean")
plt.legend()
save_chart("mean_line_chart")


# ==========================================
# 26. MEDIAN HEATMAP
# ==========================================

plt.figure(figsize=(9, 5))
sns.heatmap(
    medians.T,
    annot=True,
    cmap="YlGnBu",
    fmt=".2f"
)
plt.title("26. Class-Wise Median Heatmap")
save_chart("median_heatmap")


# ==========================================
# 27. BIVARIATE KDE
# ==========================================

plt.figure(figsize=(9, 6))
sns.kdeplot(
    data=sample,
    x="Feature_1",
    y="Feature_2",
    levels=10
)
plt.title("27. Bivariate KDE")
save_chart("bivariate_kde")


# ==========================================
# 28. JOINT PLOT
# ==========================================

joint = sns.jointplot(
    data=sample,
    x="Feature_1",
    y="Feature_2",
    kind="reg",
    height=8
)
joint.fig.suptitle("28. Joint Distribution Plot", y=1.02)
joint.savefig(
    os.path.join(output_folder, "28_joint_plot.png"),
    dpi=150,
    bbox_inches="tight"
)
plt.show()
plt.close("all")

chart_count += 1
print("Saved 28/30: 28_joint_plot.png")


# ==========================================
# 29. 3D SCATTER PLOT
# ==========================================

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection="3d")

scatter = ax.scatter(
    sample["Feature_1"],
    sample["Feature_2"],
    sample["Target"],
    c=sample["Target"],
    cmap="viridis",
    alpha=0.6
)

ax.set_xlabel("Feature 1")
ax.set_ylabel("Feature 2")
ax.set_zlabel("Target")
ax.set_title("29. Three Dimensional Scatter Plot")

fig.colorbar(scatter, ax=ax, label="Target")
save_chart("3d_scatter")


# ==========================================
# 30. CLASS-WISE MINIMUM AND MAXIMUM
# ==========================================

plt.figure(figsize=(10, 6))

for feature in ["Feature_1", "Feature_2"]:

    grouped = df.groupby("Target")[feature]

    plt.plot(
        grouped.min().index,
        grouped.min().values,
        marker="o",
        label=feature + " Minimum"
    )

    plt.plot(
        grouped.max().index,
        grouped.max().values,
        marker="s",
        label=feature + " Maximum"
    )

plt.title("30. Class-Wise Minimum and Maximum")
plt.xlabel("Target Class")
plt.ylabel("Feature Value")
plt.legend()
save_chart("classwise_range")


# ==========================================
# FINAL RESULT
# ==========================================

print("\n====================================")
print("CURE VISUALIZATION COMPLETED")
print("====================================")
print("Dataset Records:", len(df))
print("Total Charts:", chart_count)
print("Output Folder:", output_folder)
print("All visualizations saved successfully!")
