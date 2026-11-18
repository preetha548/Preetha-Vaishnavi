

from pathlib import Path
import sys

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# ------------------------------------------------------------
# 1. LOAD DATASET
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR / "india_crime_dataset_2026_synthetic.csv"

if not CSV_FILE.exists():
    print("Dataset file not found:")
    print(CSV_FILE)
    print("\nKeep india_crime_dataset_2026_synthetic.csv in the same folder")
    print("as this Python file.")
    sys.exit(1)

df = pd.read_csv(CSV_FILE)

required_columns = [
    "Crime_ID", "State", "District", "Crime_Type", "Crime_Category",
    "Year", "Month", "Time", "Cases_Registered",
    "Crime_Severity", "Case_Status"
]

missing = [column for column in required_columns if column not in df.columns]
if missing:
    print("Dataset is missing required columns:", missing)
    sys.exit(1)

print("=" * 65)
print("          INDIA CRIME DATASET 2026 - ANALYSIS")
print("=" * 65)
print(f"\nNumber of records : {len(df)}")
print(f"Number of columns : {len(df.columns)}")
print("\nFirst 10 records:")
print(df.head(10).to_string(index=False))

print("\nDataset information:")
df.info()

print("\nMissing values in each column:")
print(df.isnull().sum())

# ------------------------------------------------------------
# 2. BASIC STATISTICAL ANALYSIS
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("                    CRIME SUMMARY")
print("=" * 65)

print("\nCrime type counts:")
print(df["Crime_Type"].value_counts())

print("\nState-wise record counts:")
print(df["State"].value_counts())

print("\nCrime severity counts:")
print(df["Crime_Severity"].value_counts())

print("\nCase status counts:")
print(df["Case_Status"].value_counts())

print("\nTotal sample cases registered:",
      int(df["Cases_Registered"].sum()))

# Save summary reports
df["Crime_Type"].value_counts().rename_axis("Crime_Type").reset_index(
    name="Record_Count"
).to_csv(BASE_DIR / "crime_type_summary_2026.csv", index=False)

df.groupby("State")["Cases_Registered"].sum().sort_values(
    ascending=False
).rename("Sample_Cases_Registered").reset_index().to_csv(
    BASE_DIR / "state_summary_2026.csv", index=False
)

# ------------------------------------------------------------
# 3. CHART 1 - CRIME TYPE DISTRIBUTION
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))
sns.countplot(
    data=df,
    y="Crime_Type",
    order=df["Crime_Type"].value_counts().index
)
plt.title("Crime Type Distribution - Synthetic 2026 Dataset")
plt.xlabel("Number of Sample Records")
plt.ylabel("Crime Type")
plt.tight_layout()
plt.savefig(BASE_DIR / "crime_type_distribution_2026.png", dpi=150)
plt.show()

# ------------------------------------------------------------
# 4. CHART 2 - STATE-WISE SAMPLE CASE COUNTS
# ------------------------------------------------------------

state_totals = (
    df.groupby("State")["Cases_Registered"]
    .sum()
    .sort_values(ascending=False)
    .head(15)
)

plt.figure(figsize=(11, 7))
state_totals.sort_values().plot(kind="barh")
plt.title("Top 15 States/UTs by Sample Cases Registered")
plt.xlabel("Sum of Synthetic Cases_Registered Values")
plt.ylabel("State / Union Territory")
plt.tight_layout()
plt.savefig(BASE_DIR / "state_wise_sample_cases_2026.png", dpi=150)
plt.show()

# ------------------------------------------------------------
# 5. CHART 3 - MONTH-WISE SAMPLE RECORDS
# ------------------------------------------------------------

monthly = df.groupby("Month").size().reindex(range(1, 13), fill_value=0)

plt.figure(figsize=(10, 5))
monthly.plot(kind="line", marker="o")
plt.title("Month-wise Sample Crime Records - 2026")
plt.xlabel("Month")
plt.ylabel("Number of Sample Records")
plt.xticks(range(1, 13))
plt.grid(True)
plt.tight_layout()
plt.savefig(BASE_DIR / "monthly_crime_records_2026.png", dpi=150)
plt.show()

# ------------------------------------------------------------
# 6. CHART 4 - CRIME SEVERITY
# ------------------------------------------------------------

severity_order = ["Low", "Medium", "High", "Critical"]
severity_counts = df["Crime_Severity"].value_counts().reindex(
    severity_order, fill_value=0
)

plt.figure(figsize=(8, 5))
severity_counts.plot(kind="bar")
plt.title("Sample Records by Crime Severity")
plt.xlabel("Severity")
plt.ylabel("Number of Sample Records")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(BASE_DIR / "crime_severity_2026.png", dpi=150)
plt.show()

# ------------------------------------------------------------
# 7. MACHINE LEARNING: CRIME CATEGORY CLASSIFICATION
# ------------------------------------------------------------
# This is a demonstration of classifying the synthetic crime
# category labels. It does NOT forecast real crime or people.

features = df[["State", "District", "Crime_Type", "Month", "Year"]].copy()
target = df["Crime_Category"].astype(str)

# One-hot encode categorical input columns.
X = pd.get_dummies(
    features,
    columns=["State", "District", "Crime_Type"],
    dtype=int
)

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(target)

# Use stratification only when every class has at least two rows.
class_counts = pd.Series(y).value_counts()
stratify_values = y if class_counts.min() >= 2 else None

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=stratify_values
)

model = RandomForestClassifier(
    n_estimators=150,
    random_state=42,
    class_weight="balanced"
)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("\n" + "=" * 65)
print("          SYNTHETIC DATA CLASSIFICATION RESULTS")
print("=" * 65)
print(f"Model accuracy on held-out synthetic records: {accuracy * 100:.2f}%")
print("\nClassification report:")
print(
    classification_report(
        y_test,
        predictions,
        labels=list(range(len(label_encoder.classes_))),
        target_names=label_encoder.classes_,
        zero_division=0
    )
)

cm = confusion_matrix(
    y_test,
    predictions,
    labels=list(range(len(label_encoder.classes_)))
)

plt.figure(figsize=(8, 6))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=label_encoder.classes_,
    yticklabels=label_encoder.classes_
)
plt.title("Confusion Matrix - Synthetic Data Classification")
plt.xlabel("Predicted Category")
plt.ylabel("Actual Category")
plt.tight_layout()
plt.savefig(BASE_DIR / "confusion_matrix_2026.png", dpi=150)
plt.show()

# ------------------------------------------------------------
# 8. OPTIONAL USER QUERY: FILTER THE DATASET
# ------------------------------------------------------------

print("\n" + "=" * 65)
print("                 FILTER CRIME RECORDS")
print("=" * 65)

print("\nAvailable states/UTs:")
for state in sorted(df["State"].dropna().unique()):
    print(" -", state)

selected_state = input(
    "\nEnter a state/UT name to view its sample records "
    "(or press Enter to skip): "
).strip()

if selected_state:
    state_rows = df[
        df["State"].str.casefold() == selected_state.casefold()
    ]

    if state_rows.empty:
        print("No matching state/UT found. Check the spelling.")
    else:
        print(f"\nSample records for {selected_state}:")
        print(state_rows.head(20).to_string(index=False))
        print(f"\nMatching sample records: {len(state_rows)}")

        output_file = BASE_DIR / "filtered_crime_records_2026.csv"
        state_rows.to_csv(output_file, index=False)
        print("Filtered records saved to:", output_file)

print("\nAnalysis completed.")
print("Charts and summary CSV files are saved in:", BASE_DIR)
print("\nReminder: All input records in this project are synthetic samples.")
