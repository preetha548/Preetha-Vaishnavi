# ============================================================
# COMPANY IT TRAINING ANALYSIS & PREDICTION
# 30 DIFFERENT CHARTS - SINGLE PROGRAM
# NumPy + Pandas + Seaborn + Matplotlib + Scikit-learn
# ============================================================

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import LabelEncoder

# ------------------------------------------------------------
# 1. CREATE COMPANY IT TRAINING DATA USING NUMPY
# ------------------------------------------------------------

np.random.seed(42)

n = 200

departments = np.random.choice(
    ["IT", "HR", "Finance", "Marketing", "Sales"],
    n
)

training_type = np.random.choice(
    ["Python", "Java", "Cloud", "Cyber Security", "Data Science"],
    n
)

training_hours = np.random.randint(1, 21, n)
attendance = np.random.randint(50, 101, n)
pre_test = np.random.randint(30, 81, n)
post_test = np.clip(
    pre_test + np.random.randint(5, 30, n),
    0,
    100
)

projects_completed = np.random.randint(0, 11, n)
experience = np.random.randint(1, 16, n)

performance = np.clip(
    (training_hours * 2)
    + (attendance * 0.25)
    + (post_test * 0.35)
    + np.random.normal(0, 5, n),
    0,
    100
)

result = np.where(
    performance >= np.median(performance),
    "Pass",
    "Fail"
)

employee_id = np.arange(1, n + 1)

df = pd.DataFrame({
    "Employee_ID": employee_id,
    "Department": departments,
    "Training_Type": training_type,
    "Training_Hours": training_hours,
    "Attendance": attendance,
    "Pre_Test": pre_test,
    "Post_Test": post_test,
    "Projects_Completed": projects_completed,
    "Experience": experience,
    "Performance": performance,
    "Training_Result": result
})

print("\nCOMPANY IT TRAINING DATA")
print(df.head())

# ------------------------------------------------------------
# 2. BASIC DATA ANALYSIS
# ------------------------------------------------------------

print("\nDataset Information:")
print(df.info())

print("\nStatistical Analysis:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# ------------------------------------------------------------
# 3. SET SEABORN STYLE
# ------------------------------------------------------------

sns.set_theme(style="whitegrid")

# ============================================================
# CHART 1 - DEPARTMENT COUNT
# ============================================================

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Department")
plt.title("1. Employees by Department")
plt.xticks(rotation=30)
plt.show()

# ============================================================
# CHART 2 - TRAINING TYPE COUNT
# ============================================================

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Training_Type")
plt.title("2. Employees by Training Type")
plt.xticks(rotation=30)
plt.show()

# ============================================================
# CHART 3 - AVERAGE PERFORMANCE BY DEPARTMENT
# ============================================================

plt.figure(figsize=(8, 5))
sns.barplot(
    data=df,
    x="Department",
    y="Performance",
    estimator=np.mean
)
plt.title("3. Average Performance by Department")
plt.xticks(rotation=30)
plt.show()

# ============================================================
# CHART 4 - AVERAGE TRAINING HOURS
# ============================================================

plt.figure(figsize=(8, 5))
sns.barplot(
    data=df,
    x="Training_Type",
    y="Training_Hours",
    estimator=np.mean
)
plt.title("4. Average Training Hours by Training Type")
plt.xticks(rotation=30)
plt.show()

# ============================================================
# CHART 5 - TRAINING HOURS vs PERFORMANCE
# ============================================================

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Training_Hours",
    y="Performance",
    hue="Department"
)
plt.title("5. Training Hours vs Performance")
plt.show()

# ============================================================
# CHART 6 - ATTENDANCE vs PERFORMANCE
# ============================================================

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Attendance",
    y="Performance",
    hue="Training_Result"
)
plt.title("6. Attendance vs Performance")
plt.show()

# ============================================================
# CHART 7 - PRE TEST vs POST TEST
# ============================================================

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Pre_Test",
    y="Post_Test",
    hue="Training_Type"
)
plt.title("7. Pre-Test vs Post-Test Scores")
plt.show()

# ============================================================
# CHART 8 - PERFORMANCE DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))
sns.histplot(
    data=df,
    x="Performance",
    kde=True
)
plt.title("8. Performance Distribution")
plt.show()

# ============================================================
# CHART 9 - TRAINING HOURS DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))
sns.histplot(
    data=df,
    x="Training_Hours",
    kde=True
)
plt.title("9. Training Hours Distribution")
plt.show()

# ============================================================
# CHART 10 - ATTENDANCE DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))
sns.histplot(
    data=df,
    x="Attendance",
    kde=True
)
plt.title("10. Attendance Distribution")
plt.show()

# ============================================================
# CHART 11 - PERFORMANCE BY DEPARTMENT
# ============================================================

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="Department",
    y="Performance"
)
plt.title("11. Performance Distribution by Department")
plt.xticks(rotation=30)
plt.show()

# ============================================================
# CHART 12 - TRAINING HOURS BY DEPARTMENT
# ============================================================

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="Department",
    y="Training_Hours"
)
plt.title("12. Training Hours by Department")
plt.xticks(rotation=30)
plt.show()

# ============================================================
# CHART 13 - PERFORMANCE BY TRAINING TYPE
# ============================================================

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="Training_Type",
    y="Performance"
)
plt.title("13. Performance by Training Type")
plt.xticks(rotation=30)
plt.show()

# ============================================================
# CHART 14 - VIOLIN PLOT
# ============================================================

plt.figure(figsize=(8, 5))
sns.violinplot(
    data=df,
    x="Training_Type",
    y="Performance"
)
plt.title("14. Performance Distribution by Training Type")
plt.xticks(rotation=30)
plt.show()

# ============================================================
# CHART 15 - TRAINING RESULT
# ============================================================

plt.figure(figsize=(7, 5))
sns.countplot(
    data=df,
    x="Training_Result"
)
plt.title("15. Training Result Analysis")
plt.show()

# ============================================================
# CHART 16 - TRAINING RESULT BY DEPARTMENT
# ============================================================

plt.figure(figsize=(8, 5))
sns.countplot(
    data=df,
    x="Department",
    hue="Training_Result"
)
plt.title("16. Training Result by Department")
plt.xticks(rotation=30)
plt.show()

# ============================================================
# CHART 17 - TRAINING RESULT BY TRAINING TYPE
# ============================================================

plt.figure(figsize=(8, 5))
sns.countplot(
    data=df,
    x="Training_Type",
    hue="Training_Result"
)
plt.title("17. Training Result by Training Type")
plt.xticks(rotation=30)
plt.show()

# ============================================================
# CHART 18 - PRE-TEST DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))
sns.histplot(
    data=df,
    x="Pre_Test",
    kde=True
)
plt.title("18. Pre-Test Score Distribution")
plt.show()

# ============================================================
# CHART 19 - POST-TEST DISTRIBUTION
# ============================================================

plt.figure(figsize=(8, 5))
sns.histplot(
    data=df,
    x="Post_Test",
    kde=True
)
plt.title("19. Post-Test Score Distribution")
plt.show()

# ============================================================
# CHART 20 - EXPERIENCE vs PERFORMANCE
# ============================================================

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Experience",
    y="Performance",
    hue="Department"
)
plt.title("20. Experience vs Performance")
plt.show()

# ============================================================
# CHART 21 - PROJECTS vs PERFORMANCE
# ============================================================

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Projects_Completed",
    y="Performance",
    hue="Training_Result"
)
plt.title("21. Projects Completed vs Performance")
plt.show()

# ============================================================
# CHART 22 - ATTENDANCE BY TRAINING TYPE
# ============================================================

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="Training_Type",
    y="Attendance"
)
plt.title("22. Attendance by Training Type")
plt.xticks(rotation=30)
plt.show()

# ============================================================
# CHART 23 - HEATMAP
# ============================================================

plt.figure(figsize=(10, 7))

numeric_df = df.select_dtypes(include=np.number)

correlation = numeric_df.corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("23. Training Data Correlation Heatmap")
plt.show()

# ============================================================
# CHART 24 - PAIR PLOT
# ============================================================

sns.pairplot(
    df[
        [
            "Training_Hours",
            "Attendance",
            "Pre_Test",
            "Post_Test",
            "Performance"
        ]
    ]
)

plt.suptitle(
    "24. Pairwise Training Analysis",
    y=1.02
)

plt.show()

# ============================================================
# CHART 25 - SWARM PLOT
# ============================================================

plt.figure(figsize=(9, 5))

sns.swarmplot(
    data=df.sample(min(100, len(df))),
    x="Training_Result",
    y="Performance"
)

plt.title("25. Performance by Training Result")
plt.show()

# ============================================================
# CHART 26 - STRIP PLOT
# ============================================================

plt.figure(figsize=(9, 5))

sns.stripplot(
    data=df,
    x="Department",
    y="Performance",
    hue="Training_Result",
    jitter=True
)

plt.title("26. Department Performance Distribution")
plt.xticks(rotation=30)
plt.show()

# ============================================================
# CHART 27 - REGRESSION PLOT
# ============================================================

plt.figure(figsize=(8, 5))

sns.regplot(
    data=df,
    x="Training_Hours",
    y="Performance",
    scatter_kws={"alpha": 0.5}
)

plt.title("27. Training Hours and Performance Prediction Trend")
plt.show()

# ============================================================
# CHART 28 - KDE PLOT
# ============================================================

plt.figure(figsize=(8, 5))

sns.kdeplot(
    data=df,
    x="Performance",
    hue="Training_Result",
    fill=True
)

plt.title("28. Performance Density by Training Result")
plt.show()

# ============================================================
# CHART 29 - AREA / LINE TREND
# ============================================================

department_performance = (
    df.groupby("Department")["Performance"]
    .mean()
    .reset_index()
)

plt.figure(figsize=(8, 5))

sns.lineplot(
    data=department_performance,
    x="Department",
    y="Performance",
    marker="o"
)

plt.title("29. Department Performance Trend")
plt.xticks(rotation=30)
plt.show()

# ============================================================
# CHART 30 - PREDICTION RESULT
# ============================================================

# Convert categorical columns to numbers
model_df = df.copy()

encoder = LabelEncoder()

model_df["Department"] = encoder.fit_transform(
    model_df["Department"]
)

model_df["Training_Type"] = encoder.fit_transform(
    model_df["Training_Type"]
)

model_df["Training_Result"] = encoder.fit_transform(
    model_df["Training_Result"]
)

# Features
X = model_df[
    [
        "Department",
        "Training_Type",
        "Training_Hours",
        "Attendance",
        "Pre_Test",
        "Post_Test",
        "Projects_Completed",
        "Experience"
    ]
]

# Target
y = model_df["Training_Result"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Prediction
prediction = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, prediction)

print("\n====================================")
print("COMPANY IT TRAINING PREDICTION")
print("====================================")
print("Prediction Accuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, prediction)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues"
)

plt.title("30. Training Prediction Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# ============================================================
# FEATURE IMPORTANCE
# ============================================================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    "Importance",
    ascending=False
)

print("\nFeature Importance:")
print(importance)

plt.figure(figsize=(9, 5))

sns.barplot(
    data=importance,
    x="Importance",
    y="Feature"
)

plt.title("Important Factors in IT Training Prediction")
plt.show()

# ============================================================
# END
# ============================================================