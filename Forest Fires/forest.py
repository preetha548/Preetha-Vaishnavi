import warnings
warnings.filterwarnings("ignore")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from scipy import stats

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (9, 5)

# ==========================================================
# 1. LOAD DATASET
# ==========================================================

file_path = r"C:\Users\USER PC\Desktop\Forest Fires\forestfires.csv"

df = pd.read_csv(file_path)
df.drop_duplicates(inplace=True)

print("Dataset Loaded Successfully!")
print(df.head())
print("\nDataset Shape:", df.shape)

# ==========================================================
# 2. DATA PREPROCESSING
# ==========================================================

df.fillna(df.median(numeric_only=True), inplace=True)

original_df = df.copy()

month_order = [
    "jan", "feb", "mar", "apr", "may", "jun",
    "jul", "aug", "sep", "oct", "nov", "dec"
]

df["month"] = pd.Categorical(
    df["month"],
    categories=month_order,
    ordered=True
)

df = pd.get_dummies(
    df,
    columns=["month", "day"],
    drop_first=True,
    dtype=int
)

X = df.drop("area", axis=1)
y = np.log1p(df["area"])

# ==========================================================
# 3. TRAIN TEST SPLIT
# ==========================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Shape:", X_train.shape)
print("Testing Shape:", X_test.shape)

# ==========================================================
# 4. LINEAR REGRESSION
# ==========================================================

lr_model = LinearRegression()

lr_model.fit(X_train, y_train)

lr_pred = lr_model.predict(X_test)

# ==========================================================
# 5. RANDOM FOREST
# ==========================================================

rf_model = RandomForestRegressor(
    n_estimators=300,
    random_state=42,
    min_samples_leaf=2,
    max_features=0.8,
    n_jobs=-1
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

# ==========================================================
# 6. GRADIENT BOOSTING
# ==========================================================

gb_model = GradientBoostingRegressor(
    n_estimators=150,
    learning_rate=0.05,
    max_depth=2,
    random_state=42
)

gb_model.fit(X_train, y_train)

gb_pred = gb_model.predict(X_test)

# ==========================================================
# 7. PREDICTION DATA
# ==========================================================

actual = np.expm1(y_test)

lr_actual_pred = np.expm1(lr_pred)
rf_actual_pred = np.expm1(rf_pred)
gb_actual_pred = np.expm1(gb_pred)

errors = actual - rf_actual_pred

numeric_df = original_df.select_dtypes(include=np.number)

# ==========================================================
# 30 DIFFERENT VISUALIZATIONS
# ==========================================================

# 1. HISTOGRAM
plt.figure()
sns.histplot(original_df["temp"], kde=True, color="orange")
plt.title("1. Temperature Distribution")
plt.show()

# 2. KDE PLOT
plt.figure()
sns.kdeplot(data=original_df, x="RH", fill=True, color="blue")
plt.title("2. Relative Humidity Distribution")
plt.show()

# 3. BOX PLOT
plt.figure()
sns.boxplot(data=original_df, x="month", y="temp", order=month_order)
plt.title("3. Monthly Temperature Boxplot")
plt.xticks(rotation=45)
plt.show()

# 4. VIOLIN PLOT
plt.figure()
sns.violinplot(data=original_df, x="month", y="wind", order=month_order)
plt.title("4. Monthly Wind Distribution")
plt.xticks(rotation=45)
plt.show()

# 5. SCATTER PLOT
plt.figure()
plt.scatter(original_df["temp"], original_df["area"], alpha=0.6)
plt.xlabel("Temperature")
plt.ylabel("Burned Area")
plt.title("5. Temperature vs Burned Area")
plt.show()

# 6. HEXBIN PLOT
plt.figure()
plt.hexbin(original_df["temp"], original_df["wind"],
           C=original_df["area"], gridsize=20,
           reduce_C_function=np.mean, cmap="inferno")
plt.colorbar(label="Mean Burned Area")
plt.title("6. Temperature and Wind Density")
plt.show()

# 7. BAR CHART
plt.figure()
original_df.groupby("month")["area"].mean().reindex(month_order).plot(
    kind="bar", color="teal"
)
plt.title("7. Average Burned Area by Month")
plt.xticks(rotation=45)
plt.show()

# 8. LINE CHART
plt.figure()
original_df.groupby("month")["temp"].mean().reindex(month_order).plot(
    marker="o", color="red"
)
plt.title("8. Monthly Average Temperature")
plt.show()

# 9. PIE CHART
plt.figure()
original_df["month"].value_counts().reindex(month_order).dropna().plot(
    kind="pie", autopct="%1.1f%%"
)
plt.title("9. Monthly Fire Record Distribution")
plt.ylabel("")
plt.show()

# 10. STACKED BAR
plt.figure()
pd.crosstab(original_df["month"], original_df["day"]).reindex(
    month_order
).plot(kind="bar", stacked=True, figsize=(10, 5))
plt.title("10. Monthly and Daily Fire Records")
plt.show()

# 11. CORRELATION HEATMAP
plt.figure(figsize=(10, 8))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("11. Correlation Heatmap")
plt.show()

# 12. PAIR PLOT
sns.pairplot(
    original_df[["temp", "RH", "wind", "rain", "area"]].sample(
        min(200, len(original_df)), random_state=42
    )
)
plt.suptitle("12. Weather Feature Pair Plot", y=1.02)
plt.show()

# 13. JOINT PLOT
sns.jointplot(data=original_df, x="temp", y="RH", kind="reg")
plt.suptitle("13. Temperature and Humidity Relationship", y=1.02)
plt.show()

# 14. ECDF PLOT
plt.figure()
sns.ecdfplot(data=original_df, x="temp", hue="month")
plt.title("14. Cumulative Temperature Distribution")
plt.show()

# 15. SWARM PLOT
plt.figure()
sns.stripplot(
    data=original_df, x="month", y="wind",
    order=month_order, alpha=0.5
)
plt.title("15. Monthly Wind Distribution")
plt.xticks(rotation=45)
plt.show()

# 16. LOLLIPOP CHART
monthly_area = original_df.groupby("month")["area"].mean().reindex(month_order)

plt.figure()
plt.stem(range(len(monthly_area)), monthly_area.fillna(0).values)
plt.xticks(range(len(monthly_area)), month_order, rotation=45)
plt.title("16. Monthly Average Burned Area")
plt.show()

# 17. ERROR BAR CHART
monthly_stats = original_df.groupby("month")["temp"].agg(["mean", "std"]).reindex(
    month_order
)

plt.figure()
plt.errorbar(
    monthly_stats.index,
    monthly_stats["mean"],
    yerr=monthly_stats["std"].fillna(0),
    fmt="o",
    capsize=5
)
plt.title("17. Monthly Temperature with Standard Deviation")
plt.xticks(rotation=45)
plt.show()

# 18. DUMBBELL CHART
monthly_range = original_df.groupby("month")["temp"].agg(["min", "max"])

plt.figure()
for i, (month, row) in enumerate(monthly_range.iterrows()):
    plt.plot([row["min"], row["max"]], [i, i], color="steelblue")
plt.yticks(range(len(monthly_range)), monthly_range.index)
plt.title("18. Monthly Temperature Range")
plt.show()

# 19. AREA CHART
monthly_count = original_df["month"].value_counts().reindex(
    month_order
).fillna(0)

plt.figure()
monthly_count.plot(kind="area", color="lightgreen")
plt.title("19. Monthly Fire Frequency")
plt.show()

# 20. POLAR CHART
polar_data = monthly_area.fillna(0)

angles = np.linspace(0, 2*np.pi, len(polar_data), endpoint=False)

fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
ax.plot(angles, polar_data.values, marker="o")
ax.fill(angles, polar_data.values, alpha=0.25)
ax.set_xticks(angles)
ax.set_xticklabels(month_order)
ax.set_title("20. Polar Monthly Burned Area")
plt.show()

# 21. FEATURE IMPORTANCE
importance = pd.Series(
    rf_model.feature_importances_,
    index=X.columns
).nlargest(10).sort_values()

plt.figure()
importance.plot(kind="barh", color="seagreen")
plt.title("21. Random Forest Feature Importance")
plt.show()

# 22. ACTUAL VS PREDICTED
plt.figure()
plt.scatter(actual, rf_actual_pred, alpha=0.6, color="purple")
limit = max(actual.max(), rf_actual_pred.max())
plt.plot([0, limit], [0, limit], "r--")
plt.xlabel("Actual Area")
plt.ylabel("Predicted Area")
plt.title("22. Actual vs Predicted Burned Area")
plt.show()

# 23. RESIDUAL BOXPLOT
plt.figure()
sns.boxplot(x=errors, color="salmon")
plt.title("23. Residual Boxplot")
plt.show()

# 24. RESIDUAL VIOLIN
plt.figure()
sns.violinplot(y=errors, color="lightblue")
plt.title("24. Residual Violin Plot")
plt.show()

# 25. RESIDUAL HISTOGRAM
plt.figure()
sns.histplot(errors, kde=True, bins=25)
plt.title("25. Residual Distribution")
plt.show()

# 26. RESIDUAL SCATTER
plt.figure()
plt.scatter(rf_actual_pred, errors, alpha=0.6)
plt.axhline(0, color="red", linestyle="--")
plt.xlabel("Predicted Area")
plt.ylabel("Residual")
plt.title("26. Residual vs Predicted Area")
plt.show()

# 27. RESIDUAL LINE
plt.figure()
plt.plot(np.asarray(errors), color="purple")
plt.axhline(0, color="red", linestyle="--")
plt.title("27. Residual Error by Test Record")
plt.show()

# 28. Q-Q PLOT
plt.figure()
stats.probplot(errors, dist="norm", plot=plt)
plt.title("28. Residual Q-Q Plot")
plt.show()

# 29. MODEL COMPARISON
model_results = pd.DataFrame({
    "Model": ["Linear Regression", "Random Forest", "Gradient Boosting"],
    "MAE": [
        mean_absolute_error(y_test, lr_pred),
        mean_absolute_error(y_test, rf_pred),
        mean_absolute_error(y_test, gb_pred)
    ],
    "RMSE": [
        np.sqrt(mean_squared_error(y_test, lr_pred)),
        np.sqrt(mean_squared_error(y_test, rf_pred)),
        np.sqrt(mean_squared_error(y_test, gb_pred))
    ],
    "R2": [
        r2_score(y_test, lr_pred),
        r2_score(y_test, rf_pred),
        r2_score(y_test, gb_pred)
    ]
})

plt.figure()
model_results.set_index("Model")["RMSE"].plot(
    kind="bar", color=["orange", "green", "blue"]
)
plt.title("29. Machine Learning Model Comparison")
plt.ylabel("RMSE (Log Scale)")
plt.xticks(rotation=20)
plt.show()

# 30. ACTUAL VS PREDICTED DENSITY
plt.figure()
plt.hexbin(
    actual, rf_actual_pred,
    gridsize=25, cmap="viridis", mincnt=1
)
plt.colorbar(label="Number of Records")

limit = max(actual.max(), rf_actual_pred.max())
plt.plot([0, limit], [0, limit], "r--")

plt.xlabel("Actual Burned Area")
plt.ylabel("Predicted Burned Area")
plt.title("30. Actual vs Predicted Density")
plt.show()

# ==========================================================
# 8. MODEL EVALUATION
# ==========================================================

print("\n==========================================")
print("ALL 30 VISUALIZATIONS GENERATED")
print("==========================================")

print("\nMODEL PERFORMANCE COMPARISON")
print(model_results.to_string(index=False))

# Evaluate models in original burned-area units

print("\nRANDOM FOREST PERFORMANCE (ORIGINAL AREA SCALE)")

print("MAE:",
      mean_absolute_error(actual, rf_actual_pred))

print("MSE:",
      mean_squared_error(actual, rf_actual_pred))

print("RMSE:",
      np.sqrt(mean_squared_error(actual, rf_actual_pred)))

print("R2 Score:",
      r2_score(actual, rf_actual_pred))

print("\nTOP 10 IMPORTANT FEATURES")

print(
    pd.Series(
        rf_model.feature_importances_,
        index=X.columns
    ).nlargest(10)
)

print("\nPROJECT EXECUTED SUCCESSFULLY!")