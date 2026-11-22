
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("Ice Cream Sales - temperatures.csv")

df.columns = ["Temperature", "Ice Cream Profits"]

df = df.dropna()

temperature = df["Temperature"]
profits = df["Ice Cream Profits"]

sns.set_theme(style="whitegrid")

print("Dataset Loaded Successfully!")
print("Total Records:", len(df))
print(df.describe())

# ==========================================
# CHART 1 - Scatter Plot
# ==========================================
plt.figure(figsize=(8, 5))
plt.scatter(temperature, profits)
plt.title("1. Temperature vs Ice Cream Profits")
plt.xlabel("Temperature")
plt.ylabel("Ice Cream Profits")
plt.show()

# ==========================================
# CHART 2 - Line Chart
# ==========================================
plt.figure(figsize=(8, 5))
plt.plot(temperature, profits, marker="o")
plt.title("2. Temperature and Profit Trend")
plt.xlabel("Temperature")
plt.ylabel("Profits")
plt.show()

# ==========================================
# CHART 3 - Regression Plot
# ==========================================
plt.figure(figsize=(8, 5))
sns.regplot(data=df, x="Temperature",
            y="Ice Cream Profits")
plt.title("3. Linear Regression Plot")
plt.show()

# ==========================================
# CHART 4 - Histogram
# ==========================================
plt.figure(figsize=(8, 5))
plt.hist(profits, bins=15)
plt.title("4. Profit Distribution")
plt.xlabel("Profits")
plt.ylabel("Frequency")
plt.show()

# ==========================================
# CHART 5 - Box Plot
# ==========================================
plt.figure(figsize=(8, 5))
sns.boxplot(y=profits)
plt.title("5. Profit Box Plot")
plt.show()

# ==========================================
# CHART 6 - Violin Plot
# ==========================================
plt.figure(figsize=(8, 5))
sns.violinplot(y=profits)
plt.title("6. Profit Violin Plot")
plt.show()

# ==========================================
# CHART 7 - KDE Plot
# ==========================================
plt.figure(figsize=(8, 5))
sns.kdeplot(profits, fill=True)
plt.title("7. Profit Density Distribution")
plt.show()

# ==========================================
# CHART 8 - Hexbin Plot
# ==========================================
plt.figure(figsize=(8, 5))
plt.hexbin(temperature, profits, gridsize=15)
plt.colorbar(label="Record Density")
plt.title("8. Temperature vs Profit Hexbin")
plt.show()

# ==========================================
# CHART 9 - Joint Plot
# ==========================================
sns.jointplot(data=df, x="Temperature",
              y="Ice Cream Profits", kind="scatter")
plt.show()

# ==========================================
# CHART 10 - Pair Plot
# ==========================================
sns.pairplot(df)
plt.show()

# ==========================================
# CHART 11 - Bar Chart
# ==========================================
avg = df.groupby("Temperature")["Ice Cream Profits"].mean()
plt.figure(figsize=(10, 5))
avg.plot(kind="bar")
plt.title("11. Average Profit by Temperature")
plt.xlabel("Temperature")
plt.ylabel("Average Profit")
plt.show()

# ==========================================
# CHART 12 - Horizontal Bar Chart
# ==========================================
plt.figure(figsize=(10, 5))
avg.plot(kind="barh")
plt.title("12. Horizontal Average Profit Chart")
plt.show()

# ==========================================
# CHART 13 - Area Chart
# ==========================================
plt.figure(figsize=(8, 5))
avg.plot(kind="area", alpha=0.5)
plt.title("13. Average Profit Area Chart")
plt.show()

# ==========================================
# CHART 14 - Step Chart
# ==========================================
plt.figure(figsize=(8, 5))
plt.step(avg.index, avg.values, where="mid")
plt.title("14. Step Chart")
plt.xlabel("Temperature")
plt.ylabel("Average Profit")
plt.show()

# ==========================================
# CHART 15 - Stem Plot
# ==========================================
plt.figure(figsize=(8, 5))
plt.stem(avg.index, avg.values)
plt.title("15. Stem Plot")
plt.show()

# ==========================================
# CHART 16 - Error Bar Chart
# ==========================================
group = df.groupby("Temperature")["Ice Cream Profits"]
mean = group.mean()
std = group.std().fillna(0)

plt.figure(figsize=(9, 5))
plt.errorbar(mean.index, mean.values,
             yerr=std.values, fmt="o")
plt.title("16. Profit Mean with Standard Deviation")
plt.xlabel("Temperature")
plt.ylabel("Profit")
plt.show()

# ==========================================
# CHART 17 - Temperature Frequency
# ==========================================
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x="Temperature")
plt.title("17. Temperature Frequency")
plt.xticks(rotation=90)
plt.show()

# ==========================================
# CHART 18 - ECDF Plot
# ==========================================
plt.figure(figsize=(8, 5))
sns.ecdfplot(data=df, x="Ice Cream Profits")
plt.title("18. Cumulative Profit Distribution")
plt.show()

# ==========================================
# CHART 19 - Rug Plot
# ==========================================
plt.figure(figsize=(8, 5))
sns.rugplot(data=df, x="Temperature",
            y="Ice Cream Profits")
plt.title("19. Temperature and Profit Rug Plot")
plt.show()

# ==========================================
# CHART 20 - Hexagonal Density
# ==========================================
plt.figure(figsize=(8, 5))
plt.hexbin(temperature, profits, gridsize=25,
           cmap="viridis")
plt.colorbar()
plt.title("20. Hexagonal Density Plot")
plt.show()

# ==========================================
# CHART 21 - 2D Histogram
# ==========================================
plt.figure(figsize=(8, 5))
plt.hist2d(temperature, profits, bins=20)
plt.colorbar(label="Frequency")
plt.title("21. Two Dimensional Histogram")
plt.show()

# ==========================================
# CHART 22 - KDE Joint Plot
# ==========================================
sns.jointplot(data=df, x="Temperature",
              y="Ice Cream Profits", kind="kde")
plt.show()

# ==========================================
# CHART 23 - Residual Plot
# ==========================================
from sklearn.linear_model import LinearRegression

X = df[["Temperature"]]
y = profits

model = LinearRegression()
model.fit(X, y)

predictions = model.predict(X)
residuals = y - predictions

plt.figure(figsize=(8, 5))
plt.scatter(predictions, residuals)
plt.axhline(0, linestyle="--")
plt.title("23. Regression Residual Plot")
plt.xlabel("Predicted Profits")
plt.ylabel("Residuals")
plt.show()

# ==========================================
# CHART 24 - Actual vs Predicted
# ==========================================
plt.figure(figsize=(8, 5))
plt.scatter(y, predictions)
plt.plot([y.min(), y.max()],
         [y.min(), y.max()], linestyle="--")
plt.title("24. Actual vs Predicted Profits")
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.show()

# ==========================================
# CHART 25 - Rolling Average
# ==========================================
rolling = df.sort_values("Temperature")[
    "Ice Cream Profits"
].rolling(window=10).mean()

plt.figure(figsize=(8, 5))
plt.plot(temperature.sort_values().values,
         rolling.values)
plt.title("25. Rolling Average Profit")
plt.xlabel("Temperature")
plt.ylabel("Rolling Average")
plt.show()

# ==========================================
# CHART 26 - Profit by Temperature Range
# ==========================================
df["Temperature Range"] = pd.cut(
    df["Temperature"],
    bins=[30, 50, 60, 70, 80, 90, 110]
)

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Temperature Range",
            y="Ice Cream Profits")
plt.title("26. Profit by Temperature Range")
plt.xticks(rotation=30)
plt.show()

# ==========================================
# CHART 27 - Bubble Chart
# ==========================================
counts = df.groupby("Temperature").size()

plt.figure(figsize=(9, 5))
plt.scatter(avg.index, avg.values,
            s=counts.values * 15, alpha=0.6)
plt.title("27. Bubble Chart - Average Profit")
plt.xlabel("Temperature")
plt.ylabel("Average Profit")
plt.show()

# ==========================================
# CHART 28 - Mean Profit Line Chart
# ==========================================
plt.figure(figsize=(8, 5))
plt.plot(mean.index, mean.values,
         marker="o", linestyle="-")
plt.title("28. Mean Profit by Temperature")
plt.xlabel("Temperature")
plt.ylabel("Mean Profit")
plt.show()

# ==========================================
# CHART 29 - Standard Deviation Chart
# ==========================================
plt.figure(figsize=(8, 5))
plt.plot(std.index, std.values,
         marker="o")
plt.title("29. Profit Standard Deviation")
plt.xlabel("Temperature")
plt.ylabel("Standard Deviation")
plt.show()

# ==========================================
# CHART 30 - Correlation Heatmap
# ==========================================
plt.figure(figsize=(7, 5))
sns.heatmap(
    df[["Temperature", "Ice Cream Profits"]].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("30. Correlation Heatmap")
plt.show()

# ==========================================
# COMPLETION
# ==========================================

print("\n" + "=" * 50)
print("ALL 30 CHARTS GENERATED SUCCESSFULLY!")
print("=" * 50)
