
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# LOAN APPROVAL DATA VISUALIZATION
# ==========================================

print("=" * 50)
print("       LOAN APPROVAL PREDICTION SYSTEM")
print("=" * 50)

# 1. Load Dataset

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET = os.path.join(
    BASE_DIR,
    "train_u6lujuX_CVtuZ9i.csv"
)

if not os.path.exists(DATASET):
    raise FileNotFoundError("CSV dataset not found!")

if os.path.getsize(DATASET) == 0:
    raise ValueError("CSV dataset is empty!")

df = pd.read_csv(DATASET)

print("\nDataset Loaded Successfully!")
print("Total Records:", len(df))
print("Total Columns:", len(df.columns))

print("\nDataset Preview:")
print(df.head())

# 2. Create Chart Folder

OUTPUT_FOLDER = os.path.join(BASE_DIR, "Loan_Charts")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

sns.set_theme(style="whitegrid")

# Helper function to save charts

def save_chart(filename):
    path = os.path.join(OUTPUT_FOLDER, filename)
    plt.tight_layout()
    plt.savefig(path, dpi=300, bbox_inches="tight")
    print("Saved:", filename)
    plt.show()
    plt.close()

# ==========================================
# CHART 1: LOAN STATUS
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Loan_Status",
    hue="Loan_Status",
    palette="Set2",
    legend=False
)

plt.title("Loan Approval vs Rejection")
plt.xlabel("Loan Status")
plt.ylabel("Number of Applicants")
plt.xticks([0, 1], ["Rejected", "Approved"])

save_chart("loan_status.png")

# ==========================================
# CHART 2: GENDER DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Gender",
    hue="Gender",
    palette="pastel",
    legend=False
)

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Applicants")

save_chart("gender_distribution.png")

# ==========================================
# CHART 3: EDUCATION DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Education",
    hue="Education",
    palette="viridis",
    legend=False
)

plt.title("Education Distribution")
plt.xlabel("Education")
plt.ylabel("Number of Applicants")

save_chart("education_distribution.png")

# ==========================================
# CHART 4: APPLICANT INCOME
# ==========================================

plt.figure(figsize=(9, 5))

sns.histplot(
    df["ApplicantIncome"].dropna(),
    bins=30,
    kde=True,
    color="blue"
)

plt.title("Applicant Income Distribution")
plt.xlabel("Applicant Income")
plt.ylabel("Frequency")

save_chart("applicant_income.png")

# ==========================================
# CHART 5: LOAN AMOUNT
# ==========================================

plt.figure(figsize=(9, 5))

sns.histplot(
    df["LoanAmount"].dropna(),
    bins=30,
    kde=True,
    color="green"
)

plt.title("Loan Amount Distribution")
plt.xlabel("Loan Amount")
plt.ylabel("Frequency")

save_chart("loan_amount.png")

# ==========================================
# CHART 6: PROPERTY AREA
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Property_Area",
    hue="Property_Area",
    palette="Set1",
    legend=False
)

plt.title("Property Area Distribution")
plt.xlabel("Property Area")
plt.ylabel("Number of Applicants")

save_chart("property_area.png")

# ==========================================
# CHART 7: CREDIT HISTORY
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Credit_History",
    hue="Loan_Status",
    palette="Set2"
)

plt.title("Credit History vs Loan Approval")
plt.xlabel("Credit History")
plt.ylabel("Number of Applicants")
plt.legend(title="Loan Status")

save_chart("credit_history.png")

# ==========================================
# CHART 8: MARRIED STATUS
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Married",
    hue="Loan_Status",
    palette="coolwarm"
)

plt.title("Marital Status vs Loan Approval")
plt.xlabel("Married Status")
plt.ylabel("Number of Applicants")

save_chart("married_status.png")

# ==========================================
# CHART 9: INCOME VS LOAN AMOUNT
# ==========================================

plt.figure(figsize=(9, 5))

sns.scatterplot(
    data=df,
    x="ApplicantIncome",
    y="LoanAmount",
    hue="Loan_Status",
    palette="Set1",
    alpha=0.7
)

plt.title("Income vs Loan Amount")
plt.xlabel("Applicant Income")
plt.ylabel("Loan Amount")

save_chart("income_vs_loan.png")

# ==========================================
# CHART 10: CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(10, 7))

numeric_df = df.select_dtypes(include=["number"])

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Loan Dataset Correlation Heatmap")

save_chart("correlation_heatmap.png")

# ==========================================
# CHART 11: PROPERTY AREA VS LOAN STATUS
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Property_Area",
    hue="Loan_Status",
    palette="Set2"
)

plt.title("Property Area vs Loan Approval")
plt.xlabel("Property Area")
plt.ylabel("Number of Applicants")
plt.legend(title="Loan Status")

save_chart("property_loan_status.png")

# ==========================================
# FINAL RESULT
# ==========================================

print("\n" + "=" * 50)
print("VISUALIZATION COMPLETED SUCCESSFULLY!")
print("=" * 50)

print("Dataset Records:", len(df))
print("Charts Generated: 11")
print("Output Folder:", OUTPUT_FOLDER)

print("\nAll 11 charts saved successfully!")
