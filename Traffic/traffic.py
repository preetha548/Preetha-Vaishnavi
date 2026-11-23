
import pandas as pd
import matplotlib.pyplot as plt
import os

print("=" * 60)
print("       TRAFFIC DATASET ANALYSIS")
print("=" * 60)

# 1. Load Dataset
try:
    df = pd.read_csv("traffic_dataset.csv")
    print("\nDataset loaded successfully!")
except FileNotFoundError:
    print("ERROR: traffic_dataset.csv not found!")
    raise SystemExit

# 2. Remove Unnecessary Index Column
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# 3. Dataset Information
print("\nDataset Shape:", df.shape)
print("\nDataset Columns:")
print(df.columns.tolist())

print("\nFirst Five Records:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Description:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# 4. Handle Missing Values
numeric_cols = df.select_dtypes(include='number').columns
categorical_cols = df.select_dtypes(include='object').columns

for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

for col in categorical_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# 5. Create Output Folder
os.makedirs("traffic_charts", exist_ok=True)

chart_number = 0

def save_chart(title):
    global chart_number
    chart_number += 1
    plt.title(title)
    plt.tight_layout()
    plt.savefig(
        f"traffic_charts/chart_{chart_number:02d}.png",
        dpi=150
    )
    plt.show()
    plt.close()

# =====================================================
# 30 DATA VISUALIZATION CHARTS
# =====================================================

# 1. Vehicle Count Histogram
plt.figure(figsize=(8, 5))
plt.hist(df['vehicle_count'], bins=30, edgecolor='black')
save_chart("1. Vehicle Count Distribution")

# 2. Average Speed Histogram
plt.figure(figsize=(8, 5))
plt.hist(df['average_speed'], bins=30, edgecolor='black')
save_chart("2. Average Speed Distribution")

# 3. Lane Occupancy Histogram
plt.figure(figsize=(8, 5))
plt.hist(df['lane_occupancy'], bins=30, edgecolor='black')
save_chart("3. Lane Occupancy Distribution")

# 4. Flow Rate Histogram
plt.figure(figsize=(8, 5))
plt.hist(df['flow_rate'], bins=30, edgecolor='black')
save_chart("4. Traffic Flow Rate Distribution")

# 5. Waiting Time Histogram
plt.figure(figsize=(8, 5))
plt.hist(df['waiting_time'], bins=30, edgecolor='black')
save_chart("5. Vehicle Waiting Time Distribution")

# 6. Time of Day Bar Chart
plt.figure(figsize=(8, 5))
df['time_of_day'].value_counts().plot(kind='bar')
plt.xlabel("Time of Day")
plt.ylabel("Number of Records")
save_chart("6. Traffic Records by Time of Day")

# 7. Vehicle Count Boxplot
plt.figure(figsize=(8, 5))
plt.boxplot(df['vehicle_count'])
save_chart("7. Vehicle Count Boxplot")

# 8. Average Speed Boxplot
plt.figure(figsize=(8, 5))
plt.boxplot(df['average_speed'])
save_chart("8. Average Speed Boxplot")

# 9. Lane Occupancy Boxplot
plt.figure(figsize=(8, 5))
plt.boxplot(df['lane_occupancy'])
save_chart("9. Lane Occupancy Boxplot")

# 10. Waiting Time Boxplot
plt.figure(figsize=(8, 5))
plt.boxplot(df['waiting_time'])
save_chart("10. Waiting Time Boxplot")

# 11. Vehicle Count vs Average Speed
plt.figure(figsize=(8, 5))
plt.scatter(df['vehicle_count'], df['average_speed'], alpha=0.5)
plt.xlabel("Vehicle Count")
plt.ylabel("Average Speed")
save_chart("11. Vehicle Count vs Average Speed")

# 12. Vehicle Count vs Waiting Time
plt.figure(figsize=(8, 5))
plt.scatter(df['vehicle_count'], df['waiting_time'], alpha=0.5)
plt.xlabel("Vehicle Count")
plt.ylabel("Waiting Time")
save_chart("12. Vehicle Count vs Waiting Time")

# 13. Flow Rate vs Average Speed
plt.figure(figsize=(8, 5))
plt.scatter(df['flow_rate'], df['average_speed'], alpha=0.5)
plt.xlabel("Flow Rate")
plt.ylabel("Average Speed")
save_chart("13. Flow Rate vs Average Speed")

# 14. Lane Occupancy vs Vehicle Count
plt.figure(figsize=(8, 5))
plt.scatter(df['lane_occupancy'], df['vehicle_count'], alpha=0.5)
plt.xlabel("Lane Occupancy")
plt.ylabel("Vehicle Count")
save_chart("14. Lane Occupancy vs Vehicle Count")

# 15. Flow Rate vs Waiting Time
plt.figure(figsize=(8, 5))
plt.scatter(df['flow_rate'], df['waiting_time'], alpha=0.5)
plt.xlabel("Flow Rate")
plt.ylabel("Waiting Time")
save_chart("15. Flow Rate vs Waiting Time")

# 16. Average Speed by Time of Day
plt.figure(figsize=(8, 5))
df.groupby('time_of_day')['average_speed'].mean().plot(kind='bar')
plt.ylabel("Average Speed")
save_chart("16. Average Speed by Time of Day")

# 17. Vehicle Count by Time of Day
plt.figure(figsize=(8, 5))
df.groupby('time_of_day')['vehicle_count'].mean().plot(kind='bar')
plt.ylabel("Average Vehicle Count")
save_chart("17. Vehicle Count by Time of Day")

# 18. Waiting Time by Time of Day
plt.figure(figsize=(8, 5))
df.groupby('time_of_day')['waiting_time'].mean().plot(kind='bar')
plt.ylabel("Average Waiting Time")
save_chart("18. Waiting Time by Time of Day")

# 19. Flow Rate by Time of Day
plt.figure(figsize=(8, 5))
df.groupby('time_of_day')['flow_rate'].mean().plot(kind='bar')
plt.ylabel("Average Flow Rate")
save_chart("19. Flow Rate by Time of Day")

# 20. Lane Occupancy by Time of Day
plt.figure(figsize=(8, 5))
df.groupby('time_of_day')['lane_occupancy'].mean().plot(kind='bar')
plt.ylabel("Average Lane Occupancy")
save_chart("20. Lane Occupancy by Time of Day")

# 21. Correlation Heatmap
plt.figure(figsize=(9, 6))
correlation = df[numeric_cols].corr()
plt.imshow(correlation, cmap='coolwarm', aspect='auto')
plt.colorbar()
plt.xticks(range(len(correlation.columns)),
           correlation.columns, rotation=45, ha='right')
plt.yticks(range(len(correlation.columns)),
           correlation.columns)
save_chart("21. Traffic Parameter Correlation Heatmap")

# 22. Average Traffic Parameter Comparison
plt.figure(figsize=(9, 5))
df[numeric_cols].mean().plot(kind='bar')
plt.ylabel("Mean Value")
save_chart("22. Average Traffic Parameter Comparison")

# 23. Vehicle Count Line Chart
plt.figure(figsize=(10, 5))
plt.plot(df['vehicle_count'].head(100))
plt.xlabel("Record Number")
plt.ylabel("Vehicle Count")
save_chart("23. Vehicle Count Trend")

# 24. Average Speed Line Chart
plt.figure(figsize=(10, 5))
plt.plot(df['average_speed'].head(100))
plt.xlabel("Record Number")
plt.ylabel("Average Speed")
save_chart("24. Average Speed Trend")

# 25. Waiting Time Line Chart
plt.figure(figsize=(10, 5))
plt.plot(df['waiting_time'].head(100))
plt.xlabel("Record Number")
plt.ylabel("Waiting Time")
save_chart("25. Waiting Time Trend")

# 26. Flow Rate Line Chart
plt.figure(figsize=(10, 5))
plt.plot(df['flow_rate'].head(100))
plt.xlabel("Record Number")
plt.ylabel("Flow Rate")
save_chart("26. Traffic Flow Rate Trend")

# 27. Traffic Time Distribution Pie Chart
plt.figure(figsize=(7, 7))
df['time_of_day'].value_counts().plot(
    kind='pie', autopct='%1.1f%%'
)
plt.ylabel("")
save_chart("27. Traffic Distribution by Time of Day")

# 28. Vehicle Count by Time of Day Boxplot
plt.figure(figsize=(8, 5))
df.boxplot(column='vehicle_count', by='time_of_day')
plt.suptitle("")
plt.xlabel("Time of Day")
save_chart("28. Vehicle Count Comparison")

# 29. Waiting Time by Time of Day Boxplot
plt.figure(figsize=(8, 5))
df.boxplot(column='waiting_time', by='time_of_day')
plt.suptitle("")
plt.xlabel("Time of Day")
save_chart("29. Waiting Time Comparison")

# 30. Traffic Parameter Pairwise Scatter Matrix
from pandas.plotting import scatter_matrix

scatter_matrix(
    df[numeric_cols],
    figsize=(12, 10),
    diagonal='hist',
    alpha=0.5
)
plt.suptitle("30. Traffic Parameter Pairwise Relationships")
plt.tight_layout()
chart_number += 1
plt.savefig(
    f"traffic_charts/chart_{chart_number:02d}.png",
    dpi=150
)
plt.show()
plt.close()

# =====================================================
# FINAL ANALYSIS
# =====================================================

print("\n" + "=" * 60)
print("           TRAFFIC ANALYSIS RESULTS")
print("=" * 60)

print("\nTotal Records:", len(df))

print("\nAverage Vehicle Count:",
      round(df['vehicle_count'].mean(), 2))

print("Average Speed:",
      round(df['average_speed'].mean(), 2))

print("Average Lane Occupancy:",
      round(df['lane_occupancy'].mean(), 2))

print("Average Flow Rate:",
      round(df['flow_rate'].mean(), 2))

print("Average Waiting Time:",
      round(df['waiting_time'].mean(), 2))

print("\nTraffic Distribution:")
print(df['time_of_day'].value_counts())

print("\nHighest Traffic Vehicle Count:",
      df['vehicle_count'].max())

print("Maximum Waiting Time:",
      round(df['waiting_time'].max(), 2))

print("\nTotal Charts Generated:", chart_number)
print("Charts saved in traffic_charts folder.")

print("\nTRAFFIC DATASET ANALYSIS COMPLETED!")
