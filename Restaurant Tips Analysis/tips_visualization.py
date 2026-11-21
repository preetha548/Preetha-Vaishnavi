
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# RESTAURANT TIPS DATA VISUALIZATION
# ==========================================

print("=" * 55)
print("       RESTAURANT TIPS ANALYSIS PROJECT")
print("=" * 55)

# Create output directory
OUTPUT_DIR = "Tips_Charts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Load dataset
df = pd.read_csv("tips.csv")

# Clean dataset
df = df.dropna()

# Visualization style
sns.set_theme(style="whitegrid")

print("\nDataset loaded successfully!")
print("\nDataset Shape:", df.shape)

print("\nFirst Five Records:")
print(df.head())

print("\nDataset Statistics:")
print(df.describe())

# ==========================================
# 1. TOTAL BILL DISTRIBUTION
# ==========================================

plt.figure(figsize=(9, 5))

sns.histplot(
    data=df,
    x="total_bill",
    bins=20,
    kde=True
)

plt.title("Total Bill Distribution", fontsize=16)
plt.xlabel("Total Bill")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/total_bill_distribution.png")
plt.show()

# ==========================================
# 2. TIP DISTRIBUTION
# ==========================================

plt.figure(figsize=(9, 5))

sns.histplot(
    data=df,
    x="tip",
    bins=20,
    kde=True
)

plt.title("Tip Amount Distribution", fontsize=16)
plt.xlabel("Tip Amount")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/tip_distribution.png")
plt.show()

# ==========================================
# 3. GENDER DISTRIBUTION
# ==========================================

plt.figure(figsize=(7, 5))

gender = df["sex"].value_counts()

plt.pie(
    gender,
    labels=gender.index,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

plt.title("Customer Gender Distribution")

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/gender_distribution.png")
plt.show()

# ==========================================
# 4. SMOKER DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="smoker",
    hue="smoker"
)

plt.title("Smoker vs Non-Smoker Distribution")
plt.xlabel("Smoking Status")
plt.ylabel("Customer Count")
plt.legend([], [], frameon=False)

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/smoker_distribution.png")
plt.show()

# ==========================================
# 5. DAY DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="day",
    order=["Thur", "Fri", "Sat", "Sun"],
    hue="day"
)

plt.title("Customer Visits by Day")
plt.xlabel("Day")
plt.ylabel("Number of Customers")
plt.legend([], [], frameon=False)

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/day_distribution.png")
plt.show()

# ==========================================
# 6. LUNCH AND DINNER DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="time",
    hue="time"
)

plt.title("Lunch vs Dinner Distribution")
plt.xlabel("Meal Time")
plt.ylabel("Number of Customers")
plt.legend([], [], frameon=False)

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/time_distribution.png")
plt.show()

# ==========================================
# 7. GROUP SIZE DISTRIBUTION
# ==========================================

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="size",
    hue="size"
)

plt.title("Restaurant Group Size Distribution")
plt.xlabel("Group Size")
plt.ylabel("Frequency")
plt.legend([], [], frameon=False)

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/group_size.png")
plt.show()

# ==========================================
# 8. TOTAL BILL VS TIP
# ==========================================

plt.figure(figsize=(9, 6))

sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex",
    size="size",
    sizes=(40, 180)
)

plt.title("Total Bill vs Tip Amount")
plt.xlabel("Total Bill")
plt.ylabel("Tip Amount")

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/bill_vs_tip.png")
plt.show()

# ==========================================
# 9. AVERAGE TIPS BY DAY
# ==========================================

plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="day",
    y="tip",
    hue="day",
    order=["Thur", "Fri", "Sat", "Sun"],
    errorbar=None
)

plt.title("Average Tips by Day")
plt.xlabel("Day")
plt.ylabel("Average Tip")
plt.legend([], [], frameon=False)

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/tips_by_day.png")
plt.show()

# ==========================================
# 10. CORRELATION HEATMAP
# ==========================================

plt.figure(figsize=(9, 6))

numeric_df = df.select_dtypes(include=np.number)

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Restaurant Tips Correlation Heatmap")

plt.tight_layout()
plt.savefig(f"{OUTPUT_DIR}/correlation_heatmap.png")
plt.show()

# ==========================================
# 11. COMBINED DASHBOARD
# ==========================================

fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# Bill distribution
sns.histplot(
    data=df,
    x="total_bill",
    kde=True,
    ax=axes[0, 0]
)
axes[0, 0].set_title("Total Bill Distribution")

# Tip distribution
sns.histplot(
    data=df,
    x="tip",
    kde=True,
    ax=axes[0, 1]
)
axes[0, 1].set_title("Tip Distribution")

# Day distribution
sns.countplot(
    data=df,
    x="day",
    order=["Thur", "Fri", "Sat", "Sun"],
    hue="day",
    ax=axes[1, 0]
)
axes[1, 0].set_title("Customer Visits by Day")
axes[1, 0].legend([], [], frameon=False)

# Bill vs tip
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex",
    ax=axes[1, 1]
)
axes[1, 1].set_title("Total Bill vs Tip")

plt.suptitle(
    "RESTAURANT TIPS ANALYSIS DASHBOARD",
    fontsize=18,
    fontweight="bold"
)

plt.tight_layout()

plt.savefig(
    f"{OUTPUT_DIR}/tips_dashboard.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================
# 12. FINAL ANALYSIS REPORT
# ==========================================

print("\n" + "=" * 55)
print("             FINAL ANALYSIS REPORT")
print("=" * 55)

print("\nTotal Records:", len(df))

print("Average Total Bill:",
      round(df["total_bill"].mean(), 2))

print("Average Tip:",
      round(df["tip"].mean(), 2))

print("Maximum Bill:",
      round(df["total_bill"].max(), 2))

print("Maximum Tip:",
      round(df["tip"].max(), 2))

print("Minimum Bill:",
      round(df["total_bill"].min(), 2))

print("Most Popular Day:",
      df["day"].mode()[0])

print("Most Popular Meal:",
      df["time"].mode()[0])

print("Average Group Size:",
      round(df["size"].mean(), 2))

print("\nAverage Tips by Gender:")
print(df.groupby("sex")["tip"].mean().round(2))

print("\nAverage Tips by Day:")
print(df.groupby("day")["tip"].mean().round(2))

print("\nAverage Tips by Smoking Status:")
print(df.groupby("smoker")["tip"].mean().round(2))

print("\nAverage Bill by Meal Time:")
print(df.groupby("time")["total_bill"].mean().round(2))

# ==========================================
# COMPLETED
# ==========================================

print("\n" + "=" * 55)
print("ALL 11 CHARTS GENERATED SUCCESSFULLY!")
print("Charts saved in:", OUTPUT_DIR)
print("=" * 55)
