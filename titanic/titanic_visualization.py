
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# TITANIC DATASET - 30 CHART VISUALIZATION
# ==========================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "train.csv")
CHART_DIR = os.path.join(BASE_DIR, "Titanic_Charts")

os.makedirs(CHART_DIR, exist_ok=True)

sns.set_theme(style="whitegrid")

# Load dataset
if not os.path.exists(DATA_FILE):
    print("ERROR: train.csv not found!")
    print("Place train.csv in the same folder as this Python file.")
    raise SystemExit

df = pd.read_csv(DATA_FILE)

print("=" * 50)
print("TITANIC DATA VISUALIZATION PROJECT")
print("=" * 50)

print("\nDataset loaded successfully!")
print("\nFirst five records:")
print(df.head())

print("\nDataset information:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

print("\nTotal passengers:", len(df))

# Prepare additional columns
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(
    df["Embarked"].mode()[0]
)
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 12, 18, 35, 60, 100],
    labels=["Child", "Teenager", "Young Adult", "Adult", "Senior"]
)

# Function to save charts
def save_chart(number, title):
    plt.title(title, fontsize=14)
    plt.tight_layout()

    filename = f"{number:02d}_{title.lower().replace(' ', '_')}.png"
    filepath = os.path.join(CHART_DIR, filename)

    plt.savefig(filepath, dpi=300, bbox_inches="tight")
    plt.close()

    print("Chart saved:", filename)


# 1. Survival Count Bar Chart
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Survived")
plt.xlabel("Survived (0 = No, 1 = Yes)")
plt.ylabel("Passengers")
save_chart(1, "Survival Count Bar Chart")


# 2. Survival Pie Chart
plt.figure(figsize=(7, 5))
df["Survived"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    labels=["Not Survived", "Survived"],
    startangle=90
)
plt.ylabel("")
save_chart(2, "Survival Pie Chart")


# 3. Gender Distribution Count Plot
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Sex")
plt.xlabel("Gender")
plt.ylabel("Passengers")
save_chart(3, "Gender Distribution")


# 4. Gender Distribution Pie Chart
plt.figure(figsize=(7, 5))
df["Sex"].value_counts().plot(
    kind="pie", autopct="%1.1f%%"
)
plt.ylabel("")
save_chart(4, "Gender Pie Chart")


# 5. Passenger Class Count Plot
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Pclass")
plt.xlabel("Passenger Class")
plt.ylabel("Passengers")
save_chart(5, "Passenger Class Distribution")


# 6. Grouped Bar Chart - Survival by Gender
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Sex", hue="Survived")
plt.xlabel("Gender")
plt.ylabel("Passengers")
save_chart(6, "Survival by Gender")


# 7. Grouped Bar Chart - Survival by Class
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Pclass", hue="Survived")
plt.xlabel("Passenger Class")
plt.ylabel("Passengers")
save_chart(7, "Survival by Class")


# 8. Age Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Age"], bins=25, edgecolor="black")
plt.xlabel("Age")
plt.ylabel("Frequency")
save_chart(8, "Age Histogram")


# 9. Age Density Plot
plt.figure(figsize=(8, 5))
sns.kdeplot(data=df, x="Age", fill=True)
plt.xlabel("Age")
save_chart(9, "Age Density Plot")


# 10. Fare Histogram
plt.figure(figsize=(8, 5))
plt.hist(df["Fare"], bins=30, edgecolor="black")
plt.xlabel("Fare")
plt.ylabel("Frequency")
save_chart(10, "Fare Histogram")


# 11. Age Box Plot by Survival
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="Survived", y="Age")
plt.xlabel("Survived")
plt.ylabel("Age")
save_chart(11, "Age Box Plot")


# 12. Fare Box Plot by Class
plt.figure(figsize=(7, 5))
sns.boxplot(data=df, x="Pclass", y="Fare")
plt.xlabel("Passenger Class")
plt.ylabel("Fare")
save_chart(12, "Fare Box Plot")


# 13. Age Violin Plot
plt.figure(figsize=(7, 5))
sns.violinplot(data=df, x="Sex", y="Age")
plt.xlabel("Gender")
plt.ylabel("Age")
save_chart(13, "Age Violin Plot")


# 14. Age Strip Plot
plt.figure(figsize=(8, 5))
sns.stripplot(
    data=df, x="Survived", y="Age",
    jitter=True, alpha=0.5
)
plt.xlabel("Survived")
plt.ylabel("Age")
save_chart(14, "Age Strip Plot")


# 15. Age Swarm Plot
plt.figure(figsize=(8, 5))
sns.swarmplot(
    data=df, x="Sex", y="Age",
    hue="Survived", size=3
)
plt.xlabel("Gender")
plt.ylabel("Age")
save_chart(15, "Age Swarm Plot")


# 16. Scatter Plot - Age vs Fare
plt.figure(figsize=(8, 5))
plt.scatter(df["Age"], df["Fare"], alpha=0.5)
plt.xlabel("Age")
plt.ylabel("Fare")
save_chart(16, "Age Fare Scatter Plot")


# 17. Hexbin Plot
plt.figure(figsize=(8, 5))
plt.hexbin(
    df["Age"], df["Fare"],
    gridsize=25, cmap="viridis"
)
plt.colorbar(label="Passenger Count")
plt.xlabel("Age")
plt.ylabel("Fare")
save_chart(17, "Age Fare Hexbin Plot")


# 18. Regression Plot
plt.figure(figsize=(8, 5))
sns.regplot(
    data=df, x="Age", y="Fare",
    scatter_kws={"alpha": 0.4}
)
plt.xlabel("Age")
plt.ylabel("Fare")
save_chart(18, "Age Fare Regression Plot")


# 19. Embarkation Count Plot
plt.figure(figsize=(7, 5))
sns.countplot(data=df, x="Embarked")
plt.xlabel("Embarkation Port")
plt.ylabel("Passengers")
save_chart(19, "Embarkation Distribution")


# 20. Family Size Count Plot
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="FamilySize")
plt.xlabel("Family Size")
plt.ylabel("Passengers")
save_chart(20, "Family Size Distribution")


# 21. Survival by Embarkation Port
plt.figure(figsize=(8, 5))
sns.countplot(
    data=df, x="Embarked", hue="Survived"
)
plt.xlabel("Embarkation Port")
plt.ylabel("Passengers")
save_chart(21, "Survival by Embarkation")


# 22. Stacked Bar Chart - Gender and Survival
gender_survival = pd.crosstab(
    df["Sex"], df["Survived"]
)

gender_survival.plot(
    kind="bar", stacked=True, figsize=(8, 5)
)
plt.xlabel("Gender")
plt.ylabel("Passengers")
save_chart(22, "Stacked Gender Survival Chart")


# 23. 100% Stacked Bar Chart - Class and Survival
class_survival = pd.crosstab(
    df["Pclass"], df["Survived"], normalize="index"
) * 100

class_survival.plot(
    kind="bar", stacked=True, figsize=(8, 5)
)
plt.xlabel("Passenger Class")
plt.ylabel("Percentage")
save_chart(23, "Percentage Stacked Class Chart")


# 24. Correlation Heatmap
plt.figure(figsize=(10, 7))
numeric_df = df.select_dtypes(include="number")

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
save_chart(24, "Correlation Heatmap")


# 25. Pair Plot
pair_data = df[
    ["Age", "Fare", "Pclass", "Survived"]
].sample(
    min(300, len(df)), random_state=42
)

pair_plot = sns.pairplot(
    pair_data,
    hue="Survived",
    diag_kind="hist"
)

pair_plot.fig.suptitle(
    "Titanic Pair Plot", y=1.02
)

pair_plot.savefig(
    os.path.join(CHART_DIR, "25_pair_plot.png"),
    dpi=300,
    bbox_inches="tight"
)
plt.close("all")
print("Chart saved: 25_pair_plot.png")


# 26. Joint Plot - Age and Fare
joint_plot = sns.jointplot(
    data=df,
    x="Age",
    y="Fare",
    kind="scatter",
    height=7
)

joint_plot.fig.suptitle(
    "Age and Fare Joint Plot", y=1.02
)

joint_plot.savefig(
    os.path.join(CHART_DIR, "26_joint_plot.png"),
    dpi=300,
    bbox_inches="tight"
)
plt.close("all")
print("Chart saved: 26_joint_plot.png")


# 27. ECDF Plot - Fare
plt.figure(figsize=(8, 5))
sns.ecdfplot(data=df, x="Fare")
plt.xlabel("Fare")
plt.ylabel("Cumulative Proportion")
save_chart(27, "Fare ECDF Plot")


# 28. Line Chart - Survival Rate by Age Group
age_survival = df.groupby(
    "AgeGroup", observed=False
)["Survived"].mean() * 100

plt.figure(figsize=(9, 5))
plt.plot(
    age_survival.index.astype(str),
    age_survival.values,
    marker="o",
    linewidth=2
)
plt.xlabel("Age Group")
plt.ylabel("Survival Rate (%)")
save_chart(28, "Age Group Survival Line Chart")


# 29. Bubble Chart - Age, Fare and Family Size
plt.figure(figsize=(9, 5))

plt.scatter(
    df["Age"],
    df["Fare"],
    s=(df["FamilySize"] * 12),
    c=df["Survived"],
    alpha=0.5,
    cmap="coolwarm"
)

plt.colorbar(label="Survived")
plt.xlabel("Age")
plt.ylabel("Fare")
save_chart(29, "Passenger Bubble Chart")


# 30. Horizontal Bar Chart - Survival Rate by Gender
gender_rate = df.groupby("Sex")["Survived"].mean() * 100

plt.figure(figsize=(8, 5))
plt.barh(
    gender_rate.index,
    gender_rate.values
)

plt.xlabel("Survival Rate (%)")
plt.ylabel("Gender")
save_chart(30, "Gender Survival Rate Horizontal Bar")


# ==========================================
# FINAL PROJECT SUMMARY
# ==========================================

print("\n" + "=" * 50)
print("TITANIC VISUALIZATION COMPLETED!")
print("=" * 50)

print("Total Passengers:", len(df))
print("Total Survived:", (df["Survived"] == 1).sum())
print("Total Not Survived:", (df["Survived"] == 0).sum())

print("\nTotal Charts Generated: 30")
print("Saved Location:", CHART_DIR)

print("\nProject executed successfully!")
