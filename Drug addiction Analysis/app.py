import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# SUICIDE PREVENTION ANALYSIS
# ==========================================

# Sample dataset
data = {
    "Age_Group": [
        "15-20", "21-30", "21-30", "31-40", "15-20",
        "41-50", "21-30", "31-40", "15-20", "51+"
    ],
    "Awareness_Level": [
        "High", "Medium", "Low", "High", "Medium",
        "High", "Low", "Medium", "High", "Medium"
    ],
    "Support_Access": [
        "Yes", "Yes", "No", "Yes", "No",
        "Yes", "No", "Yes", "Yes", "No"
    ],
    "Counselling": [
        "Yes", "Yes", "No", "Yes", "Yes",
        "No", "No", "Yes", "Yes", "No"
    ],
    "Intervention_Outcome": [
        "Improved", "Improved", "No Change", "Improved",
        "Improved", "No Change", "No Change",
        "Improved", "Improved", "No Change"
    ]
}

df = pd.DataFrame(data)

# ==========================================
# DISPLAY DATA
# ==========================================

print("\n==========================================")
print("       SUICIDE PREVENTION ANALYSIS")
print("==========================================")

print("\nDataset:")
print(df)

# ==========================================
# BASIC ANALYSIS
# ==========================================

print("\n--- Awareness Level ---")
print(df["Awareness_Level"].value_counts())

print("\n--- Support Access ---")
print(df["Support_Access"].value_counts())

print("\n--- Counselling ---")
print(df["Counselling"].value_counts())

print("\n--- Intervention Outcome ---")
print(df["Intervention_Outcome"].value_counts())

# ==========================================
# CALCULATE PERCENTAGES
# ==========================================

total = len(df)

support_yes = (df["Support_Access"] == "Yes").sum()
counselling_yes = (df["Counselling"] == "Yes").sum()
improved = (df["Intervention_Outcome"] == "Improved").sum()

print("\n--- RESULTS ---")

print("Support Access:",
      round((support_yes / total) * 100, 2), "%")

print("Counselling:",
      round((counselling_yes / total) * 100, 2), "%")

print("Improved After Intervention:",
      round((improved / total) * 100, 2), "%")

# ==========================================
# CREATE FOUR CHARTS
# ==========================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# ------------------------------------------
# Chart 1: Age Group Distribution
# ------------------------------------------

age_counts = df["Age_Group"].value_counts()

axes[0, 0].bar(
    age_counts.index,
    age_counts.values,
    color="skyblue"
)

axes[0, 0].set_title("Age Group Distribution")
axes[0, 0].set_xlabel("Age Group")
axes[0, 0].set_ylabel("Number of Participants")

# ------------------------------------------
# Chart 2: Awareness Level
# ------------------------------------------

awareness_counts = df["Awareness_Level"].value_counts()

axes[0, 1].pie(
    awareness_counts.values,
    labels=awareness_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

axes[0, 1].set_title("Suicide Prevention Awareness Level")

# ------------------------------------------
# Chart 3: Support Access
# ------------------------------------------

support_counts = df["Support_Access"].value_counts()

axes[1, 0].bar(
    support_counts.index,
    support_counts.values,
    color=["green", "red"]
)

axes[1, 0].set_title("Access to Mental Health Support")
axes[1, 0].set_xlabel("Support Access")
axes[1, 0].set_ylabel("Number of Participants")

# ------------------------------------------
# Chart 4: Intervention Outcome
# ------------------------------------------

outcome_counts = df["Intervention_Outcome"].value_counts()

axes[1, 1].bar(
    outcome_counts.index,
    outcome_counts.values,
    color=["green", "orange"]
)

axes[1, 1].set_title("Intervention Outcomes")
axes[1, 1].set_xlabel("Outcome")
axes[1, 1].set_ylabel("Number of Participants")

# ==========================================
# DISPLAY ALL CHARTS
# ==========================================

plt.suptitle(
    "Suicide Prevention Analysis",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()
plt.show()

# ==========================================
# SAVE CHARTS AS IMAGE
# ==========================================

fig.savefig(
    "suicide_prevention_analysis.png",
    dpi=300,
    bbox_inches="tight"
)

print("\nCharts saved as:")
print("suicide_prevention_analysis.png")