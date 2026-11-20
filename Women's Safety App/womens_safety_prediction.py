
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix

# --------------------------------
# 1. Create Women's Safety Dataset
# --------------------------------

np.random.seed(42)

n = 1000

data = {
    "Age": np.random.randint(18, 60, n),
    "Hour": np.random.randint(0, 24, n),
    "Lighting": np.random.choice(
        ["Good", "Moderate", "Poor"], n
    ),
    "Crowd": np.random.choice(
        ["High", "Medium", "Low"], n
    ),
    "Police": np.random.choice(
        ["Yes", "No"], n
    ),
    "Transport": np.random.choice(
        ["Available", "Limited", "Unavailable"], n
    ),
    "Previous_Incidents": np.random.randint(0, 10, n)
}

df = pd.DataFrame(data)

# --------------------------------
# 2. Generate Safety Risk Labels
# --------------------------------

risk_score = (
    (df["Lighting"] == "Poor") * 2
    + (df["Crowd"] == "Low") * 2
    + (df["Police"] == "No") * 2
    + (df["Transport"] == "Unavailable") * 2
    + ((df["Hour"] >= 20) | (df["Hour"] <= 5)) * 2
    + df["Previous_Incidents"] * 0.5
)

df["Safety_Risk"] = np.where(
    risk_score < 5, "Low Risk",
    np.where(risk_score < 9, "Medium Risk", "High Risk")
)

# Save CSV dataset
df.to_csv("womens_safety_dataset_2026.csv", index=False)

print("Dataset created successfully!")
print(df.head(10))

# --------------------------------
# 3. Convert Text into Numbers
# --------------------------------

encoders = {}

for col in ["Lighting", "Crowd", "Police", "Transport"]:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

risk_encoder = LabelEncoder()
df["Safety_Risk"] = risk_encoder.fit_transform(
    df["Safety_Risk"]
)

# --------------------------------
# 4. Split Dataset
# --------------------------------

X = df.drop("Safety_Risk", axis=1)
y = df["Safety_Risk"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# --------------------------------
# 5. Train Random Forest Model
# --------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# --------------------------------
# 6. Model Prediction
# --------------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nWomen's Safety Prediction")
print("-------------------------")
print("Model Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=risk_encoder.classes_
))

# --------------------------------
# 7. User Input Prediction
# --------------------------------

print("\nEnter Location Safety Details")

age = int(input("Enter Age: "))
hour = int(input("Enter Time (0-23): "))

lighting = input("Lighting (Good/Moderate/Poor): ").title()
crowd = input("Crowd (High/Medium/Low): ").title()
police = input("Police Presence (Yes/No): ").title()
transport = input(
    "Transport (Available/Limited/Unavailable): "
).title()

incidents = int(input("Previous Incidents: "))

new_data = pd.DataFrame([{
    "Age": age,
    "Hour": hour,
    "Lighting": lighting,
    "Crowd": crowd,
    "Police": police,
    "Transport": transport,
    "Previous_Incidents": incidents
}])

for col in ["Lighting", "Crowd", "Police", "Transport"]:
    new_data[col] = encoders[col].transform(new_data[col])

prediction = model.predict(new_data)

result = risk_encoder.inverse_transform(prediction)[0]

print("\n-------------------------")
print("WOMEN'S SAFETY RESULT")
print("-------------------------")
print("Predicted Safety Level:", result)

# --------------------------------
# 8. Safety Risk Distribution
# --------------------------------

plt.figure(figsize=(8, 5))

sns.countplot(
    x=risk_encoder.inverse_transform(y),
    order=["Low Risk", "Medium Risk", "High Risk"]
)

plt.title("Women's Safety Risk Distribution")
plt.xlabel("Safety Risk")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.show()

# --------------------------------
# 9. Confusion Matrix
# --------------------------------

cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=risk_encoder.classes_,
    yticklabels=risk_encoder.classes_
)

plt.title("Women's Safety Prediction - Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.tight_layout()
plt.show()

# --------------------------------
# 10. Feature Importance
# --------------------------------

importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

plt.figure(figsize=(9, 5))

importance.plot(kind="bar")

plt.title("Women's Safety - Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance Score")
plt.tight_layout()
plt.show()

print("\nAll graphs generated successfully!")
print("Dataset saved as womens_safety_dataset_2026.csv")
