
import pandas as pd
import matplotlib.pyplot as plt
import os

print("=" * 65)
print("       FUNERAL SERVICES AND EVENT DATA ANALYSIS")
print("=" * 65)

# --------------------------------------------------
# 1. LOAD THREE DATASETS
# --------------------------------------------------

try:
    arrangement = pd.read_csv("Arrangement Info.csv")
    branch = pd.read_csv("Branch Info.csv")
    events = pd.read_csv("Master_Event.csv")

    print("\nAll three datasets loaded successfully!")

except FileNotFoundError as e:
    print("\nERROR: Dataset file not found!")
    print(e)
    raise SystemExit

# --------------------------------------------------
# 2. DATASET INFORMATION
# --------------------------------------------------

print("\nARRANGEMENT DATASET:", arrangement.shape)
print("BRANCH DATASET:", branch.shape)
print("MASTER EVENT DATASET:", events.shape)

print("\nArrangement Columns:")
print(arrangement.columns.tolist())

print("\nBranch Columns:")
print(branch.columns.tolist())

print("\nMaster Event Columns:")
print(events.columns.tolist())

# --------------------------------------------------
# 3. DATA CLEANING
# --------------------------------------------------

# Remove unnecessary index columns
for df in [arrangement, branch, events]:
    df.drop(
        columns=[c for c in df.columns if c.startswith("Unnamed")],
        inplace=True,
        errors="ignore"
    )

# Convert dates
arrangement['day_date_arrangement_date'] = pd.to_datetime(
    arrangement['day_date_arrangement_date'],
    dayfirst=True,
    errors='coerce'
)

events['Day_Date_Event_Date'] = pd.to_datetime(
    events['Day_Date_Event_Date'],
    dayfirst=True,
    errors='coerce'
)

# Clean text columns
for df in [arrangement, branch, events]:
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype('string').str.strip()

# Convert revenue columns
events['Funeral_Rev'] = pd.to_numeric(
    events['Funeral_Rev'], errors='coerce'
).fillna(0)

events['Cremation_Rev'] = pd.to_numeric(
    events['Cremation_Rev'], errors='coerce'
).fillna(0)

events['Total_Revenue'] = (
    events['Funeral_Rev'] + events['Cremation_Rev']
)

# --------------------------------------------------
# 4. MERGE DATASETS
# --------------------------------------------------

df = pd.merge(
    events,
    arrangement,
    left_on='Event_Id',
    right_on='Event_id',
    how='left'
)

df = pd.merge(
    df,
    branch,
    left_on='Branch Number',
    right_on='Branch_Number',
    how='left'
)

print("\nMerged Dataset Shape:", df.shape)

# --------------------------------------------------
# 5. GENERAL STATISTICS
# --------------------------------------------------

print("\nFIRST FIVE RECORDS")
print(df.head())

print("\nDATASET INFORMATION")
print(df.info())

print("\nSTATISTICAL SUMMARY")
print(df.describe(include='all').to_string())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nDUPLICATE RECORDS:", df.duplicated().sum())

# --------------------------------------------------
# 6. CREATE CHART FOLDER
# --------------------------------------------------

os.makedirs("funeral_charts", exist_ok=True)

chart_count = 0

def save_chart(title):
    global chart_count

    chart_count += 1

    plt.title(title)
    plt.tight_layout()

    plt.savefig(
        f"funeral_charts/chart_{chart_count:02d}.png",
        dpi=150,
        bbox_inches='tight'
    )

    plt.show()
    plt.close()

# --------------------------------------------------
# 30 DATA VISUALIZATION CHARTS
# --------------------------------------------------

# 1. Business Type Distribution
plt.figure(figsize=(9, 5))
df['Business'].value_counts().plot(kind='bar')
plt.xlabel("Business Type")
plt.ylabel("Number of Events")
save_chart("1. Business Type Distribution")

# 2. Attendance Basis Distribution
plt.figure(figsize=(8, 5))
df['Attend_Basis'].value_counts().plot(kind='bar')
plt.xlabel("Attendance Basis")
plt.ylabel("Number of Events")
save_chart("2. Attendance Basis Distribution")

# 3. Service Type Distribution
plt.figure(figsize=(12, 6))
df['Service_Type'].value_counts().head(15).plot(kind='bar')
plt.xlabel("Service Type")
plt.ylabel("Number of Events")
plt.xticks(rotation=60, ha='right')
save_chart("3. Top 15 Service Types")

# 4. Branch Type Distribution
plt.figure(figsize=(8, 5))
branch['Branch_type'].value_counts().plot(kind='bar')
plt.xlabel("Branch Type")
plt.ylabel("Number of Branches")
save_chart("4. Branch Type Distribution")

# 5. Regional Branch Distribution
plt.figure(figsize=(10, 5))
branch['Region'].value_counts().plot(kind='bar')
plt.xlabel("Region")
plt.ylabel("Number of Branches")
save_chart("5. Branch Distribution by Region")

# 6. Brand Distribution
plt.figure(figsize=(12, 6))
branch['Brand_Name'].value_counts().head(15).plot(kind='bar')
plt.xlabel("Brand")
plt.ylabel("Number of Branches")
plt.xticks(rotation=60, ha='right')
save_chart("6. Top 15 Funeral Service Brands")

# 7. Funeral Revenue Histogram
plt.figure(figsize=(8, 5))
plt.hist(df['Funeral_Rev'], bins=30, edgecolor='black')
plt.xlabel("Funeral Revenue")
plt.ylabel("Frequency")
save_chart("7. Funeral Revenue Distribution")

# 8. Cremation Revenue Histogram
plt.figure(figsize=(8, 5))
plt.hist(df['Cremation_Rev'], bins=30, edgecolor='black')
plt.xlabel("Cremation Revenue")
plt.ylabel("Frequency")
save_chart("8. Cremation Revenue Distribution")

# 9. Total Revenue Histogram
plt.figure(figsize=(8, 5))
plt.hist(df['Total_Revenue'], bins=30, edgecolor='black')
plt.xlabel("Total Revenue")
plt.ylabel("Frequency")
save_chart("9. Total Revenue Distribution")

# 10. Funeral Revenue Boxplot
plt.figure(figsize=(8, 5))
plt.boxplot(df['Funeral_Rev'])
save_chart("10. Funeral Revenue Boxplot")

# 11. Cremation Revenue Boxplot
plt.figure(figsize=(8, 5))
plt.boxplot(df['Cremation_Rev'])
save_chart("11. Cremation Revenue Boxplot")

# 12. Total Revenue Boxplot
plt.figure(figsize=(8, 5))
plt.boxplot(df['Total_Revenue'])
save_chart("12. Total Revenue Boxplot")

# 13. Funeral Revenue vs Cremation Revenue
plt.figure(figsize=(8, 5))
plt.scatter(
    df['Funeral_Rev'],
    df['Cremation_Rev'],
    alpha=0.4
)
plt.xlabel("Funeral Revenue")
plt.ylabel("Cremation Revenue")
save_chart("13. Funeral vs Cremation Revenue")

# 14. Revenue by Business Type
plt.figure(figsize=(9, 5))
df.groupby('Business')['Total_Revenue'].sum().plot(kind='bar')
plt.ylabel("Total Revenue")
save_chart("14. Revenue by Business Type")

# 15. Average Revenue by Business
plt.figure(figsize=(9, 5))
df.groupby('Business')['Total_Revenue'].mean().plot(kind='bar')
plt.ylabel("Average Revenue")
save_chart("15. Average Revenue by Business")

# 16. Revenue by Attendance Basis
plt.figure(figsize=(8, 5))
df.groupby('Attend_Basis')['Total_Revenue'].sum().plot(kind='bar')
plt.ylabel("Total Revenue")
save_chart("16. Revenue by Attendance Basis")

# 17. Revenue by Service Type
plt.figure(figsize=(12, 6))
df.groupby('Service_Type')['Total_Revenue'].sum().nlargest(15).plot(kind='bar')
plt.ylabel("Total Revenue")
plt.xticks(rotation=60, ha='right')
save_chart("17. Top 15 Service Types by Revenue")

# 18. Average Revenue by Service Type
plt.figure(figsize=(12, 6))
df.groupby('Service_Type')['Total_Revenue'].mean().nlargest(15).plot(kind='bar')
plt.ylabel("Average Revenue")
plt.xticks(rotation=60, ha='right')
save_chart("18. Top 15 Service Types by Average Revenue")

# 19. Regional Revenue
plt.figure(figsize=(10, 5))
df.groupby('Region')['Total_Revenue'].sum().sort_values(
    ascending=False
).plot(kind='bar')
plt.ylabel("Total Revenue")
save_chart("19. Revenue by Region")

# 20. Branch Type Revenue
plt.figure(figsize=(9, 5))
df.groupby('Branch_type')['Total_Revenue'].sum().plot(kind='bar')
plt.ylabel("Total Revenue")
save_chart("20. Revenue by Branch Type")

# 21. Monthly Event Count
monthly = df.dropna(subset=['Day_Date_Event_Date']).copy()
monthly['Month'] = monthly['Day_Date_Event_Date'].dt.to_period('M').astype(str)

plt.figure(figsize=(12, 5))
monthly.groupby('Month').size().plot(kind='line', marker='o')
plt.xlabel("Month")
plt.ylabel("Number of Events")
plt.xticks(rotation=60)
save_chart("21. Monthly Event Trends")

# 22. Monthly Revenue
plt.figure(figsize=(12, 5))
monthly.groupby('Month')['Total_Revenue'].sum().plot(
    kind='line', marker='o'
)
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=60)
save_chart("22. Monthly Revenue Trends")

# 23. Funeral Arrangements by Coffin
plt.figure(figsize=(12, 6))
df['Coffin_Used'].value_counts().head(15).plot(kind='bar')
plt.xlabel("Coffin Type")
plt.ylabel("Number of Arrangements")
plt.xticks(rotation=60, ha='right')
save_chart("23. Top 15 Coffin Types")

# 24. Coroner Involvement
plt.figure(figsize=(10, 5))
df['Coroner_Involvement'].value_counts().head(10).plot(kind='bar')
plt.xlabel("Coroner Involvement")
plt.ylabel("Number of Arrangements")
save_chart("24. Coroner Involvement Analysis")

# 25. Embalming Distribution
plt.figure(figsize=(8, 5))
df['Embalming'].fillna(0).value_counts().plot(kind='bar')
plt.xlabel("Embalming Value")
plt.ylabel("Number of Arrangements")
save_chart("25. Embalming Distribution")

# 26. Hearse Availability
plt.figure(figsize=(8, 5))
df['HasHearse'].fillna(0).value_counts().plot(kind='bar')
plt.xlabel("Hearse Availability Value")
plt.ylabel("Number of Arrangements")
save_chart("26. Hearse Availability Analysis")

# 27. Limo Availability
plt.figure(figsize=(8, 5))
df['HasLimo'].fillna(0).value_counts().plot(kind='bar')
plt.xlabel("Limo Availability Value")
plt.ylabel("Number of Arrangements")
save_chart("27. Limo Availability Analysis")

# 28. Number of Bearers Distribution
plt.figure(figsize=(8, 5))
df['No_of_Bearers'].dropna().value_counts().sort_index().plot(kind='bar')
plt.xlabel("Number of Bearers")
plt.ylabel("Number of Arrangements")
save_chart("28. Number of Bearers Analysis")

# 29. Hearse Count Distribution
plt.figure(figsize=(8, 5))
df['Hearses'].dropna().value_counts().sort_index().head(15).plot(kind='bar')
plt.xlabel("Number of Hearses")
plt.ylabel("Number of Arrangements")
save_chart("29. Hearse Count Distribution")

# 30. Revenue Correlation Heatmap
plt.figure(figsize=(9, 6))

numeric_data = df[
    ['Funeral_Rev', 'Cremation_Rev', 'Total_Revenue']
].corr()

plt.imshow(numeric_data, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()

plt.xticks(
    range(len(numeric_data.columns)),
    numeric_data.columns,
    rotation=30
)

plt.yticks(
    range(len(numeric_data.columns)),
    numeric_data.columns
)

for i in range(len(numeric_data.columns)):
    for j in range(len(numeric_data.columns)):
        plt.text(
            j, i,
            f"{numeric_data.iloc[i, j]:.2f}",
            ha='center',
            va='center'
        )

save_chart("30. Revenue Correlation Heatmap")

# --------------------------------------------------
# 7. FINAL ANALYSIS REPORT
# --------------------------------------------------

print("\n" + "=" * 65)
print("             FINAL ANALYSIS REPORT")
print("=" * 65)

print("\nTOTAL EVENTS:", len(events))
print("TOTAL ARRANGEMENTS:", len(arrangement))
print("TOTAL BRANCHES:", len(branch))

print("\nTOTAL FUNERAL REVENUE:",
      round(events['Funeral_Rev'].sum(), 2))

print("TOTAL CREMATION REVENUE:",
      round(events['Cremation_Rev'].sum(), 2))

print("TOTAL COMBINED REVENUE:",
      round(events['Total_Revenue'].sum(), 2))

print("\nAVERAGE FUNERAL REVENUE:",
      round(events['Funeral_Rev'].mean(), 2))

print("AVERAGE CREMATION REVENUE:",
      round(events['Cremation_Rev'].mean(), 2))

print("\nMOST COMMON BUSINESS:")
print(events['Business'].value_counts().head(1))

print("\nMOST COMMON ATTENDANCE BASIS:")
print(events['Attend_Basis'].value_counts().head(1))

print("\nMOST COMMON SERVICE TYPE:")
print(events['Service_Type'].value_counts().head(1))

print("\nBRANCHES BY REGION:")
print(branch['Region'].value_counts())

print("\nTOP 10 SERVICE TYPES BY REVENUE:")
print(
    df.groupby('Service_Type')['Total_Revenue']
    .sum()
    .nlargest(10)
)

print("\nTOP 10 BRANCHES BY REVENUE:")
print(
    df.groupby('Location_name')['Total_Revenue']
    .sum()
    .nlargest(10)
)

print("\nTOTAL CHARTS GENERATED:", chart_count)

# --------------------------------------------------
# 8. EXPORT MERGED DATASET AND REPORT
# --------------------------------------------------

df.to_csv("funeral_merged_dataset.csv", index=False)

summary = pd.DataFrame({
    'Metric': [
        'Total Events',
        'Total Arrangements',
        'Total Branches',
        'Total Funeral Revenue',
        'Total Cremation Revenue',
        'Total Combined Revenue',
        'Average Funeral Revenue',
        'Average Cremation Revenue'
    ],
    'Value': [
        len(events),
        len(arrangement),
        len(branch),
        events['Funeral_Rev'].sum(),
        events['Cremation_Rev'].sum(),
        events['Total_Revenue'].sum(),
        events['Funeral_Rev'].mean(),
        events['Cremation_Rev'].mean()
    ]
})

summary.to_csv("funeral_analysis_report.csv", index=False)

print("\nMerged dataset saved successfully!")
print("Analysis report saved successfully!")
print("30 charts saved in funeral_charts folder.")

print("\nFUNERAL SERVICES DATA ANALYSIS COMPLETED!")
print("=" * 65)
