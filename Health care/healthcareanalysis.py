
import os
import warnings
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

warnings.filterwarnings("ignore")
sns.set_theme(style="whitegrid", palette="Set2")

# ==========================================
# 1. PATH SETTINGS
# ==========================================

BASE_DIR = r"C:\Users\USER PC\Desktop\Health care"

FILE_PATH = os.path.join(BASE_DIR, "healthcare_dataset.csv")

OUTPUT_DIR = os.path.join(BASE_DIR, "Healthcare_30_Unique_Charts")

os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(FILE_PATH)
df.columns = df.columns.str.strip()

df = df.drop_duplicates()

# ==========================================
# 2. AUTOMATIC COLUMN DETECTION
# ==========================================

def find_col(words):
    for col in df.columns:
        if any(w in col.lower() for w in words):
            return col
    return None

age = find_col(["age"])
gender = find_col(["gender", "sex"])
condition = find_col(["medical condition", "disease", "diagnosis"])
blood = find_col(["blood type", "blood group"])
hospital = find_col(["hospital"])
billing = find_col(["billing amount", "bill amount", "cost"])
admission = find_col(["admission type"])
medication = find_col(["medication"])
insurance = find_col(["insurance provider"])
test = find_col(["test results", "test result"])
date = find_col(["date of admission", "admission date"])
discharge = find_col(["discharge date"])
room = find_col(["room number"])

numeric = df.select_dtypes(include=np.number).columns.tolist()
categorical = df.select_dtypes(include=["object", "category"]).columns.tolist()

if age:
    df[age] = pd.to_numeric(df[age], errors="coerce")

if billing:
    df[billing] = pd.to_numeric(df[billing], errors="coerce")

if date:
    df[date] = pd.to_datetime(df[date], errors="coerce")

# ==========================================
# 3. CHART SAVE FUNCTION
# ==========================================

chart_count = 0

def save_chart(name):
    global chart_count

    plt.tight_layout()
    plt.savefig(
        os.path.join(OUTPUT_DIR, name + ".png"),
        dpi=300,
        bbox_inches="tight"
    )
    plt.close()

    chart_count += 1
    print("Generated:", name)

def no_data(message="Required columns not available"):
    plt.figure(figsize=(8, 4))
    plt.text(0.5, 0.5, message,
             ha="center", va="center")
    plt.axis("off")

# ==========================================
# 4. CHART 1 - AGE DISTRIBUTION
# ==========================================

if age:
    plt.figure(figsize=(9, 5))
    sns.histplot(df[age].dropna(), bins=25, kde=True)
    plt.title("01 - Patient Age Distribution")
    plt.xlabel("Age")
    save_chart("01_Age_Distribution")

# ==========================================
# 5. CHART 2 - VIOLIN PLOT
# ==========================================

if age and gender:
    plt.figure(figsize=(9, 5))
    sns.violinplot(data=df, x=gender, y=age)
    plt.title("02 - Age Distribution by Gender")
    save_chart("02_Violin_Plot")

# ==========================================
# 6. CHART 3 - POPULATION PYRAMID
# ==========================================

if age and gender:
    temp = df[[age, gender]].dropna().copy()
    temp["Age_Group"] = pd.cut(
        temp[age],
        bins=[0, 18, 30, 45, 60, 75, 120],
        labels=["0-18", "19-30", "31-45",
                "46-60", "61-75", "76+"]
    )

    pivot = pd.crosstab(temp["Age_Group"], temp[gender])

    if pivot.shape[1] >= 2:
        plt.figure(figsize=(9, 6))
        plt.barh(pivot.index.astype(str),
                 -pivot.iloc[:, 0], label=str(pivot.columns[0]))
        plt.barh(pivot.index.astype(str),
                 pivot.iloc[:, 1], label=str(pivot.columns[1]))
        plt.axvline(0, color="black")
        plt.title("03 - Patient Population Pyramid")
        plt.xlabel("Patient Count")
        plt.legend()
        save_chart("03_Population_Pyramid")

# ==========================================
# 7. CHART 4 - DISEASE LOLLIPOP
# ==========================================

if condition:
    counts = df[condition].value_counts().head(12).sort_values()

    plt.figure(figsize=(10, 6))
    plt.hlines(counts.index, 0, counts.values)
    plt.scatter(counts.values, counts.index, s=100)
    plt.title("04 - Disease Lollipop Chart")
    plt.xlabel("Patient Count")
    save_chart("04_Disease_Lollipop")

# ==========================================
# 8. CHART 5 - PARETO ANALYSIS
# ==========================================

if condition:
    counts = df[condition].value_counts().head(10)
    percentage = counts.cumsum() / counts.sum() * 100

    fig, ax1 = plt.subplots(figsize=(10, 5))
    ax1.bar(counts.index.astype(str), counts.values)
    ax1.set_ylabel("Patient Count")
    ax1.tick_params(axis="x", rotation=45)

    ax2 = ax1.twinx()
    ax2.plot(counts.index.astype(str), percentage,
             marker="o", color="red")
    ax2.set_ylabel("Cumulative Percentage")
    ax2.set_ylim(0, 110)

    plt.title("05 - Disease Pareto Analysis")
    save_chart("05_Pareto_Chart")

# ==========================================
# 9. CHART 6 - BLOOD GROUP DONUT
# ==========================================

if blood:
    counts = df[blood].value_counts()

    plt.figure(figsize=(8, 7))
    plt.pie(counts, labels=counts.index,
            autopct="%1.1f%%", wedgeprops={"width": 0.4})
    plt.title("06 - Blood Group Donut Chart")
    save_chart("06_Blood_Donut")

# ==========================================
# 10. CHART 7 - ADMISSION TYPE
# ==========================================

if admission:
    plt.figure(figsize=(9, 5))
    counts = df[admission].value_counts()
    plt.barh(counts.index.astype(str), counts.values)
    plt.title("07 - Admission Type Ranking")
    plt.xlabel("Patients")
    save_chart("07_Admission_Ranking")

# ==========================================
# 11. CHART 8 - HOSPITAL RANKING
# ==========================================

if hospital:
    counts = df[hospital].value_counts().head(15)

    plt.figure(figsize=(11, 6))
    sns.barplot(x=counts.values, y=counts.index)
    plt.title("08 - Top 15 Hospital Ranking")
    plt.xlabel("Patient Records")
    save_chart("08_Hospital_Ranking")

# ==========================================
# 12. CHART 9 - BILLING VIOLIN
# ==========================================

if billing and condition:
    plt.figure(figsize=(12, 6))
    sns.violinplot(data=df, x=condition, y=billing,
                   inner="quartile")
    plt.title("09 - Billing Distribution by Disease")
    plt.xticks(rotation=35)
    save_chart("09_Billing_Violin")

# ==========================================
# 13. CHART 10 - BILLING BOX PLOT
# ==========================================

if billing and admission:
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=df, x=admission, y=billing)
    plt.title("10 - Billing by Admission Type")
    save_chart("10_Billing_Boxplot")

# ==========================================
# 14. CHART 11 - BUBBLE CHART
# ==========================================

if age and billing:
    temp = df[[age, billing]].dropna()

    plt.figure(figsize=(9, 6))
    plt.scatter(temp[age], temp[billing],
                s=35, alpha=0.5)
    plt.title("11 - Age vs Healthcare Billing Bubble Chart")
    plt.xlabel("Patient Age")
    plt.ylabel("Billing Amount")
    save_chart("11_Bubble_Chart")

# ==========================================
# 15. CHART 12 - HEXBIN
# ==========================================

if age and billing:
    temp = df[[age, billing]].dropna()

    plt.figure(figsize=(9, 6))
    plt.hexbin(temp[age], temp[billing],
               gridsize=25, cmap="viridis", mincnt=1)
    plt.colorbar(label="Record Density")
    plt.title("12 - Patient Billing Hexbin Analysis")
    plt.xlabel("Age")
    plt.ylabel("Billing")
    save_chart("12_Hexbin_Chart")

# ==========================================
# 16. CHART 13 - CORRELATION HEATMAP
# ==========================================

if len(numeric) >= 2:
    plt.figure(figsize=(11, 8))
    sns.heatmap(df[numeric].corr(),
                annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("13 - Healthcare Correlation Heatmap")
    save_chart("13_Correlation_Heatmap")

# ==========================================
# 17. CHART 14 - PAIR PLOT
# ==========================================

if len(numeric) >= 2:
    cols = numeric[:4]
    sample = df[cols].dropna().sample(
        min(500, len(df[cols].dropna())),
        random_state=42
    )

    if len(sample) > 1:
        g = sns.pairplot(sample, corner=True)
        g.figure.suptitle("14 - Healthcare Pair Plot", y=1.02)
        g.figure.savefig(
            os.path.join(OUTPUT_DIR, "14_Pair_Plot.png"),
            dpi=300, bbox_inches="tight"
        )
        plt.close(g.figure)
        chart_count += 1

# ==========================================
# 18. CHART 15 - MONTHLY ADMISSION TREND
# ==========================================

if date:
    temp = df.dropna(subset=[date]).copy()
    monthly = temp.groupby(temp[date].dt.month).size()

    plt.figure(figsize=(10, 5))
    plt.plot(monthly.index, monthly.values,
             marker="o", linewidth=2)
    plt.title("15 - Monthly Admission Trend")
    plt.xlabel("Month")
    plt.ylabel("Admissions")
    plt.xticks(range(1, 13))
    save_chart("15_Monthly_Trend")

# ==========================================
# 19. CHART 16 - WEEKDAY ANALYSIS
# ==========================================

if date:
    temp = df.dropna(subset=[date]).copy()
    weekdays = temp[date].dt.day_name().value_counts()

    order = ["Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday"]

    weekdays = weekdays.reindex(order).fillna(0)

    plt.figure(figsize=(10, 5))
    plt.bar(weekdays.index, weekdays.values)
    plt.title("16 - Weekday Admission Pattern")
    plt.xticks(rotation=30)
    save_chart("16_Weekday_Analysis")

# ==========================================
# 20. CHART 17 - MONTH HEATMAP
# ==========================================

if date:
    temp = df.dropna(subset=[date]).copy()
    temp["Year"] = temp[date].dt.year
    temp["Month"] = temp[date].dt.month

    pivot = temp.pivot_table(
        index="Year", columns="Month",
        values=date, aggfunc="count"
    )

    plt.figure(figsize=(11, 5))
    sns.heatmap(pivot, annot=True, fmt=".0f", cmap="YlGnBu")
    plt.title("17 - Yearly Monthly Admission Heatmap")
    save_chart("17_Admission_Heatmap")

# ==========================================
# 21. CHART 18 - MEDICATION FREQUENCY
# ==========================================

if medication:
    counts = df[medication].value_counts().head(12)

    plt.figure(figsize=(10, 5))
    sns.barplot(x=counts.values, y=counts.index)
    plt.title("18 - Medication Frequency Analysis")
    save_chart("18_Medication_Analysis")

# ==========================================
# 22. CHART 19 - INSURANCE ANALYSIS
# ==========================================

if insurance:
    counts = df[insurance].value_counts().head(12)

    plt.figure(figsize=(10, 5))
    plt.pie(counts, labels=counts.index,
            autopct="%1.1f%%")
    plt.title("19 - Insurance Provider Distribution")
    save_chart("19_Insurance_Analysis")

# ==========================================
# 23. CHART 20 - TEST RESULT STACKED CHART
# ==========================================

if test and condition:
    cross = pd.crosstab(df[condition], df[test])

    plt.figure(figsize=(11, 6))
    cross.plot(kind="bar", stacked=True,
               figsize=(11, 6))
    plt.title("20 - Disease vs Test Results")
    plt.ylabel("Patient Count")
    plt.xticks(rotation=35)
    save_chart("20_Test_Result_Stacked")

# ==========================================
# 24. CHART 21 - ECDF
# ==========================================

if billing:
    values = df[billing].dropna()

    plt.figure(figsize=(9, 5))
    sns.ecdfplot(values)
    plt.title("21 - Cumulative Billing Distribution")
    plt.xlabel("Billing Amount")
    plt.ylabel("Cumulative Probability")
    save_chart("21_Billing_ECDF")

# ==========================================
# 25. CHART 22 - BILLING DENSITY
# ==========================================

if billing:
    plt.figure(figsize=(9, 5))
    sns.kdeplot(df[billing].dropna(), fill=True)
    plt.title("22 - Healthcare Billing Density")
    save_chart("22_Billing_Density")

# ==========================================
# 26. CHART 23 - JOINT DISTRIBUTION
# ==========================================

if age and billing:
    temp = df[[age, billing]].dropna()

    if len(temp) > 1:
        g = sns.jointplot(
            data=temp, x=age, y=billing,
            kind="reg", height=7
        )
        g.figure.suptitle(
            "23 - Age and Billing Joint Distribution",
            y=1.02
        )
        g.figure.savefig(
            os.path.join(OUTPUT_DIR, "23_Joint_Distribution.png"),
            dpi=300, bbox_inches="tight"
        )
        plt.close(g.figure)
        chart_count += 1

# ==========================================
# 27. CHART 24 - ROOM NUMBER DISTRIBUTION
# ==========================================

if room:
    values = pd.to_numeric(df[room], errors="coerce").dropna()

    if len(values) > 0:
        plt.figure(figsize=(9, 5))
        sns.histplot(values, bins=20, kde=True)
        plt.title("24 - Hospital Room Number Distribution")
        save_chart("24_Room_Distribution")

# ==========================================
# 28. CHART 25 - RADAR CHART
# ==========================================

if age and billing and condition:
    temp = df[[age, billing, condition]].dropna()

    groups = temp.groupby(condition)[[age, billing]].mean().head(5)

    if len(groups) >= 2:
        normalized = groups.copy()

        for col in normalized.columns:
            maximum = normalized[col].max()
            normalized[col] = (
                normalized[col] / maximum if maximum != 0 else 0
            )

        labels = normalized.columns.tolist()
        angles = np.linspace(0, 2*np.pi, len(labels),
                             endpoint=False).tolist()
        angles += angles[:1]

        fig, ax = plt.subplots(figsize=(8, 8),
                               subplot_kw={"polar": True})

        for idx, row in normalized.iterrows():
            values = row.tolist()
            values += values[:1]
            ax.plot(angles, values, marker="o", label=str(idx))
            ax.fill(angles, values, alpha=0.08)

        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels)
        ax.set_title("25 - Disease Comparison Radar Chart")
        ax.legend(loc="upper right", bbox_to_anchor=(1.4, 1.1))

        save_chart("25_Radar_Chart")

# ==========================================
# 29. CHART 26 - STACKED AREA
# ==========================================

if date and condition:
    temp = df.dropna(subset=[date, condition]).copy()
    temp["Month"] = temp[date].dt.to_period("M").astype(str)

    pivot = pd.crosstab(temp["Month"], temp[condition])

    if len(pivot) > 1:
        pivot = pivot.iloc[:, :5]

        plt.figure(figsize=(12, 6))
        pivot.plot.area(alpha=0.7, figsize=(12, 6))
        plt.title("26 - Monthly Disease Trend Area Chart")
        plt.xlabel("Month")
        plt.ylabel("Records")
        plt.xticks(rotation=45)
        save_chart("26_Disease_Area_Chart")

# ==========================================
# 30. CHART 27 - DUMBBELL COMPARISON
# ==========================================

if billing and condition and admission:
    temp = df.groupby([condition, admission])[billing].mean().unstack()

    if temp.shape[1] >= 2:
        temp = temp.iloc[:, :2].dropna().head(10)

        if len(temp) > 0:
            plt.figure(figsize=(10, 6))

            for i, (label, row) in enumerate(temp.iterrows()):
                plt.plot([row.iloc[0], row.iloc[1]],
                         [i, i], marker="o", linewidth=2)

            plt.yticks(range(len(temp)), temp.index.astype(str))
            plt.title("27 - Billing Dumbbell Comparison")
            plt.xlabel("Average Billing Amount")
            save_chart("27_Dumbbell_Chart")

# ==========================================
# 31. CHART 28 - BOXEN PLOT
# ==========================================

if age and condition:
    plt.figure(figsize=(11, 6))
    sns.boxenplot(data=df, x=condition, y=age)
    plt.title("28 - Patient Age Boxen Analysis")
    plt.xticks(rotation=35)
    save_chart("28_Boxen_Plot")

# ==========================================
# 32. CHART 29 - TREEMAP STYLE
# ==========================================

if condition:
    counts = df[condition].value_counts().head(12)

    fig, ax = plt.subplots(figsize=(11, 7))

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

    total = counts.sum()
    x = 0
    y = 0

    for i, (label, value) in enumerate(counts.items()):
        width = value / total
        height = 0.5 if i % 2 == 0 else 0.5

        rect = plt.Rectangle(
            (x, y), width, height,
            edgecolor="white",
            linewidth=2
        )

        ax.add_patch(rect)

        ax.text(
            x + width / 2,
            y + height / 2,
            f"{label}\n{value}",
            ha="center", va="center",
            fontsize=8
        )

        x += width

        if x >= 0.99:
            break

    ax.set_title("29 - Disease Proportion Treemap-Style Chart")
    ax.axis("off")
    save_chart("29_Disease_Treemap")

# ==========================================
# 33. CHART 30 - TOP FEATURES
# ==========================================

if len(numeric) >= 2:
    correlations = df[numeric].corr().abs()

    scores = correlations.where(
        np.triu(np.ones(correlations.shape), k=1).astype(bool)
    ).stack().sort_values(ascending=False).head(15)

    plt.figure(figsize=(10, 6))

    if len(scores) > 0:
        labels = [f"{a} - {b}" for a, b in scores.index]
        plt.barh(labels[::-1], scores.values[::-1])
        plt.title("30 - Strongest Numerical Feature Relationships")
        plt.xlabel("Absolute Correlation")
    else:
        no_data("Not enough feature relationships")

    save_chart("30_Feature_Relationships")

# ==========================================
# 34. COMPLETION SUMMARY
# ==========================================

summary = os.path.join(
    BASE_DIR,
    "healthcare_unique_charts_summary.txt"
)

with open(summary, "w", encoding="utf-8") as f:
    f.write("HEALTHCARE UNIQUE VISUALIZATION REPORT\n")
    f.write("=" * 45 + "\n")
    f.write(f"Dataset Records: {len(df)}\n")
    f.write(f"Dataset Columns: {len(df.columns)}\n")
    f.write(f"Charts Generated: {chart_count}\n")
    f.write(f"Columns: {df.columns.tolist()}\n")

print("\n====================================")
print(" HEALTHCARE VISUALIZATION COMPLETED")
print("====================================")
print("Charts Generated:", chart_count)
print("Output Folder:", OUTPUT_DIR)
print("Summary File:", summary)
