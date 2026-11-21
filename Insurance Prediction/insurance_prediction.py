
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# ==========================================
# 1. CREATE INSURANCE CLAIM DATASET 2026
# ==========================================

np.random.seed(42)

n = 1000

age = np.random.randint(18, 70, n)
gender = np.random.choice(["Male", "Female"], n)
income = np.random.randint(15000, 150000, n)

policy_type = np.random.choice(
    ["Health", "Vehicle", "Life", "Home"], n
)

premium = np.random.randint(3000, 50000, n)
previous_claims = np.random.randint(0, 5, n)
policy_years = np.random.randint(1, 20, n)
accidents = np.random.randint(0, 4, n)

# Calculate sample claim probability

risk = (
    -2.0
    + previous_claims * 0.65
    + accidents * 0.55
    + (age > 55) * 0.35
    + (policy_type == "Vehicle") * 0.25
    + (policy_type == "Health") * 0.20
    - (policy_years > 10) * 0.20
)

probability = 1 / (1 + np.exp(-risk))

claim_status = np.random.binomial(1, probability)

df = pd.DataFrame({
    "Age": age,
    "Gender": gender,
    "Income": income,
    "Policy_Type": policy_type,
    "Premium": premium,
    "Previous_Claims": previous_claims,
    "Policy_Years": policy_years,
    "Accidents": accidents,
    "Claim_Status": claim_status
})

df.to_csv(
    "insurance_claim_dataset_2026.csv",
    index=False
)

print("Dataset Created Successfully!")
print(df.head(10))

# ==========================================
# 2. DATA PREPROCESSING
# ==========================================

X = df.drop("Claim_Status", axis=1)
y = df["Claim_Status"]

X = pd.get_dummies(
    X,
    columns=["Gender", "Policy_Type"],
    dtype=int
)

# ==========================================
# 3. SPLIT DATASET
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))

# ==========================================
# 4. RANDOM FOREST MODEL
# ==========================================

model = RandomForestClassifier(
    n_estimators=150,
    max_depth=10,
    random_state=42,
    class_weight="balanced"
)

model.fit(X_train, y_train)

print("\nModel Training Completed!")

# Save model and column names

joblib.dump(
    {
        "model": model,
        "columns": list(X.columns)
    },
    "insurance_claim_model.pkl"
)

# ==========================================
# 5. MODEL EVALUATION
# ==========================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\nMODEL PERFORMANCE")
print("--------------------------------")

print("Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    zero_division=0
))

# ==========================================
# 6. CONFUSION MATRIX
# ==========================================

cm = confusion_matrix(y_test, y_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["No Claim", "Claim"]
)

disp.plot(cmap="Blues")

plt.title("Insurance Claim Confusion Matrix")
plt.tight_layout()

plt.savefig("claim_confusion_matrix.png")
plt.close()

# ==========================================
# 7. FEATURE IMPORTANCE
# ==========================================

importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values()

plt.figure(figsize=(9, 6))

importance.plot(kind="barh")

plt.title("Insurance Claim Feature Importance")
plt.xlabel("Importance")

plt.tight_layout()

plt.savefig("claim_feature_importance.png")
plt.close()

# ==========================================
# 8. CLAIM DISTRIBUTION
# ==========================================

plt.figure(figsize=(7, 5))

df["Claim_Status"].value_counts().sort_index().plot(
    kind="bar",
    color=["skyblue", "orange"]
)

plt.title("Insurance Claim Distribution")
plt.xlabel("Claim Status (0 = No Claim, 1 = Claim)")
plt.ylabel("Number of Customers")

plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig("claim_distribution.png")
plt.close()

# ==========================================
# 9. CUSTOMER CLAIM PREDICTION
# ==========================================

print("\n====================================")
print(" INSURANCE CLAIM PREDICTION SYSTEM")
print("====================================")

try:

    user_age = int(input("Enter Age: "))

    user_gender = input(
        "Enter Gender (Male/Female): "
    ).capitalize()

    user_income = int(input("Enter Annual Income: "))

    user_policy = input(
        "Enter Policy Type (Health/Vehicle/Life/Home): "
    ).capitalize()

    user_premium = int(input("Enter Insurance Premium: "))

    user_previous = int(
        input("Enter Previous Claims: ")
    )

    user_years = int(
        input("Enter Policy Years: ")
    )

    user_accidents = int(
        input("Enter Number of Accidents: ")
    )

    # Input validation

    if not 18 <= user_age <= 100:
        raise ValueError("Age must be between 18 and 100.")

    if user_gender not in ["Male", "Female"]:
        raise ValueError("Enter Male or Female.")

    if user_income <= 0 or user_premium <= 0:
        raise ValueError("Income and premium must be positive.")

    if user_policy not in ["Health", "Vehicle", "Life", "Home"]:
        raise ValueError("Invalid policy type.")

    if not 0 <= user_previous <= 20:
        raise ValueError("Previous claims must be 0 to 20.")

    if not 1 <= user_years <= 50:
        raise ValueError("Policy years must be 1 to 50.")

    if not 0 <= user_accidents <= 20:
        raise ValueError("Accidents must be 0 to 20.")

    # Prepare customer input

    new_customer = pd.DataFrame([{
        "Age": user_age,
        "Gender": user_gender,
        "Income": user_income,
        "Policy_Type": user_policy,
        "Premium": user_premium,
        "Previous_Claims": user_previous,
        "Policy_Years": user_years,
        "Accidents": user_accidents
    }])

    new_customer = pd.get_dummies(
        new_customer,
        columns=["Gender", "Policy_Type"],
        dtype=int
    )

    new_customer = new_customer.reindex(
        columns=X.columns,
        fill_value=0
    )

    # Prediction

    prediction = model.predict(new_customer)[0]

    claim_probability = model.predict_proba(
        new_customer
    )[0][1]

    print("\n========== PREDICTION RESULT ==========")

    if prediction == 1:
        print("Claim Prediction: CLAIM LIKELY")
    else:
        print("Claim Prediction: CLAIM NOT LIKELY")

    print(
        "Estimated Claim Probability:",
        round(claim_probability * 100, 2), "%"
    )

    print("=======================================")

except ValueError as error:
    print("Invalid Input:", error)

# ==========================================
# 10. FINAL OUTPUT
# ==========================================

print("\nPROJECT OUTPUT")
print("--------------------------------")
print("1. Dataset Created")
print("2. Machine Learning Model Trained")
print("3. Insurance Claim Prediction Completed")
print("4. Confusion Matrix Generated")
print("5. Feature Importance Generated")
print("6. Claim Distribution Generated")

print("\nAll Files Saved Successfully!")
print("Project Completed!")
