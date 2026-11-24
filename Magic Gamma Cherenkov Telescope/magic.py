
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("=" * 60)
print("       MAGIC GAMMA TELESCOPE DATA ANALYSIS")
print("=" * 60)

# 1. Load Dataset
df = pd.read_csv("magic04_gamma.csv")

# Remove unnecessary index column
if "Unnamed: 0" in df.columns:
    df.drop("Unnamed: 0", axis=1, inplace=True)

print("\n1. DATASET INFORMATION")
print("-" * 60)
print("Dataset Shape:", df.shape)
print("\nFirst Five Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

# 2. Statistical Analysis
print("\n2. STATISTICAL SUMMARY")
print(df.describe())

print("\n3. MISSING VALUES")
print(df.isnull().sum())

print("\n4. DUPLICATE RECORDS")
print("Duplicates:", df.duplicated().sum())

# 3. Class Distribution
print("\n5. CLASS DISTRIBUTION")
print(df["class"].value_counts())

print("\nClass Percentage:")
print(df["class"].value_counts(normalize=True) * 100)

# 4. Data Cleaning
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)

# 5. Feature Information
features = df.select_dtypes(include=np.number).columns.tolist()

print("\n6. NUMERICAL FEATURES")
print(features)

# 6. Correlation Analysis
print("\n7. CORRELATION MATRIX")
print(df[features].corr())

# Visualization Settings
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# CHART 1: Class Distribution
plt.figure()
sns.countplot(data=df, x="class")
plt.title("Gamma and Hadron Class Distribution")
plt.xlabel("Class")
plt.ylabel("Count")
plt.show()

# CHART 2: Class Percentage
plt.figure()
df["class"].value_counts().plot.pie(
    autopct="%1.1f%%",
    startangle=90
)
plt.title("Class Percentage Distribution")
plt.ylabel("")
plt.show()

# CHART 3: Feature Correlation Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(
    df[features].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Feature Correlation Heatmap")
plt.show()

# CHART 4: Feature Histograms
df[features].hist(
    bins=30,
    figsize=(15, 12),
    edgecolor="black"
)
plt.suptitle("Distribution of Numerical Features")
plt.tight_layout()
plt.show()

# CHART 5: Feature Boxplots
plt.figure(figsize=(15, 7))
sns.boxplot(data=df[features])
plt.xticks(rotation=45)
plt.title("Numerical Feature Boxplots")
plt.show()

# CHART 6: Feature Pairplot
sns.pairplot(
    df,
    vars=features[:5],
    hue="class",
    corner=True
)
plt.suptitle("Pairwise Feature Relationships", y=1.02)
plt.show()

# CHART 7: fLength Distribution
plt.figure()
sns.histplot(data=df, x="fLength", hue="class", kde=True)
plt.title("fLength Distribution by Class")
plt.show()

# CHART 8: fWidth Distribution
plt.figure()
sns.histplot(data=df, x="fWidth", hue="class", kde=True)
plt.title("fWidth Distribution by Class")
plt.show()

# CHART 9: fSize Distribution
plt.figure()
sns.histplot(data=df, x="fSize", hue="class", kde=True)
plt.title("fSize Distribution by Class")
plt.show()

# CHART 10: fConc Distribution
plt.figure()
sns.histplot(data=df, x="fConc", hue="class", kde=True)
plt.title("fConc Distribution by Class")
plt.show()

# CHART 11: fConc1 Distribution
plt.figure()
sns.histplot(data=df, x="fConc1", hue="class", kde=True)
plt.title("fConc1 Distribution by Class")
plt.show()

# CHART 12: fAsym Distribution
plt.figure()
sns.histplot(data=df, x="fAsym", hue="class", kde=True)
plt.title("fAsym Distribution by Class")
plt.show()

# CHART 13: fM3Long Distribution
plt.figure()
sns.histplot(data=df, x="fM3Long", hue="class", kde=True)
plt.title("fM3Long Distribution by Class")
plt.show()

# CHART 14: fM3Trans Distribution
plt.figure()
sns.histplot(data=df, x="fM3Trans", hue="class", kde=True)
plt.title("fM3Trans Distribution by Class")
plt.show()

# CHART 15: fAlpha Distribution
plt.figure()
sns.histplot(data=df, x="fAlpha", hue="class", kde=True)
plt.title("fAlpha Distribution by Class")
plt.show()

# CHART 16: fDist Distribution
plt.figure()
sns.histplot(data=df, x="fDist", hue="class", kde=True)
plt.title("fDist Distribution by Class")
plt.show()

# CHART 17: fLength vs fWidth
plt.figure()
sns.scatterplot(
    data=df,
    x="fLength",
    y="fWidth",
    hue="class",
    alpha=0.6
)
plt.title("fLength vs fWidth")
plt.show()

# CHART 18: fSize vs fConc
plt.figure()
sns.scatterplot(
    data=df,
    x="fSize",
    y="fConc",
    hue="class",
    alpha=0.6
)
plt.title("fSize vs fConc")
plt.show()

# CHART 19: fAlpha vs fDist
plt.figure()
sns.scatterplot(
    data=df,
    x="fAlpha",
    y="fDist",
    hue="class",
    alpha=0.6
)
plt.title("fAlpha vs fDist")
plt.show()

# CHART 20: Feature Mean Comparison
plt.figure(figsize=(13, 6))
df.groupby("class")[features].mean().T.plot(kind="bar")
plt.title("Average Feature Values by Class")
plt.ylabel("Mean Value")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# CHART 21: Feature Median Comparison
plt.figure(figsize=(13, 6))
df.groupby("class")[features].median().T.plot(kind="bar")
plt.title("Median Feature Values by Class")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# CHART 22: Feature Standard Deviation
plt.figure(figsize=(12, 6))
df[features].std().plot(kind="bar")
plt.title("Feature Standard Deviation")
plt.ylabel("Standard Deviation")
plt.xticks(rotation=45)
plt.show()

# CHART 23: Feature Variance
plt.figure(figsize=(12, 6))
df[features].var().plot(kind="bar")
plt.title("Feature Variance")
plt.xticks(rotation=45)
plt.show()

# CHART 24: Feature Skewness
plt.figure(figsize=(12, 6))
df[features].skew().plot(kind="bar")
plt.title("Feature Skewness")
plt.xticks(rotation=45)
plt.show()

# CHART 25: Feature Kurtosis
plt.figure(figsize=(12, 6))
df[features].kurt().plot(kind="bar")
plt.title("Feature Kurtosis")
plt.xticks(rotation=45)
plt.show()

# CHART 26: Violin Plot
plt.figure(figsize=(12, 6))
sns.violinplot(data=df, x="class", y="fLength")
plt.title("fLength Distribution by Class")
plt.show()

# CHART 27: Boxplot of fWidth
plt.figure()
sns.boxplot(data=df, x="class", y="fWidth")
plt.title("fWidth Comparison by Class")
plt.show()

# CHART 28: Boxplot of fAlpha
plt.figure()
sns.boxplot(data=df, x="class", y="fAlpha")
plt.title("fAlpha Comparison by Class")
plt.show()

# CHART 29: KDE Plot
plt.figure()
sns.kdeplot(
    data=df,
    x="fLength",
    hue="class",
    fill=True,
    common_norm=False
)
plt.title("Kernel Density Estimation of fLength")
plt.show()

# CHART 30: Scatter Matrix
pd.plotting.scatter_matrix(
    df[features[:5]],
    figsize=(14, 10),
    diagonal="kde",
    alpha=0.5
)
plt.suptitle("Scatter Matrix of MAGIC Telescope Features")
plt.show()

# 7. Final Report
print("\n" + "=" * 60)
print("             FINAL DATA ANALYSIS REPORT")
print("=" * 60)

print("Total Records:", len(df))
print("Total Features:", len(features))
print("Missing Values:", df.isnull().sum().sum())
print("Duplicate Records:", df.duplicated().sum())

print("\nClass Distribution:")
print(df["class"].value_counts())

print("\nAnalysis Completed Successfully!")
