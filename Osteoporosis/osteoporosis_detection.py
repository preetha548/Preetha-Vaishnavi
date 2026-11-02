
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

print("=" * 50)
print(" OSTEOPOROSIS DETECTION USING ADABOOST")
print("=" * 50)

# Step 1: Load dataset
data = pd.read_csv("osteoporosis_dataset.csv")

print("\nDataset Loaded Successfully")
print("Total Records:", len(data))

# Step 2: Clean dataset
data.columns = data.columns.str.strip()

data = data.dropna()

# Step 3: Encode categorical columns
encoders = {}

categorical_columns = [
    "Gender",
    "Calcium_Intake",
    "Vitamin_D",
    "Physical_Activity",
    "Smoking",
    "Family_History",
    "Osteoporosis"
]

for col in categorical_columns:

    encoder = LabelEncoder()

    data[col] = encoder.fit_transform(
        data[col].astype(str).str.strip()
    )

    encoders[col] = encoder

# Step 4: Separate features and target
X = data.drop("Osteoporosis", axis=1)
y = data["Osteoporosis"]

# Step 5: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))

# Step 6: Create AdaBoost model
model = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=1),
    n_estimators=50,
    learning_rate=1.0,
    random_state=42
)

# Step 7: Train model
model.fit(X_train, y_train)

print("\nModel Trained Successfully!")

# Step 8: Test model
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 50)
print(" MODEL PERFORMANCE")
print("=" * 50)

print("Accuracy: {:.2f} %".format(accuracy * 100))

# Classification report
print("\nCLASSIFICATION REPORT")

target_encoder = encoders["Osteoporosis"]

print(
    classification_report(
        y_test,
        y_pred,
        labels=list(range(len(target_encoder.classes_))),
        target_names=target_encoder.classes_,
        zero_division=0
    )
)

# Confusion matrix
print("\nCONFUSION MATRIX")

print(confusion_matrix(y_test, y_pred))

# Step 9: New patient prediction
print("\n" + "=" * 50)
print(" NEW PATIENT DETAILS")
print("=" * 50)

age = float(input("Enter Age: "))

gender = input("Enter Gender (Male/Female): ").strip().title()

bmi = float(input("Enter BMI: "))

calcium = input(
    "Calcium Intake (Low/Medium/High): "
).strip().title()

vitamin_d = input(
    "Vitamin D (Low/Medium/High): "
).strip().title()

activity = input(
    "Physical Activity (Low/Medium/High): "
).strip().title()

smoking = input("Smoking (Yes/No): ").strip().title()

family = input("Family History (Yes/No): ").strip().title()

# Step 10: Create patient data
patient_values = {
    "Age": age,
    "Gender": gender,
    "BMI": bmi,
    "Calcium_Intake": calcium,
    "Vitamin_D": vitamin_d,
    "Physical_Activity": activity,
    "Smoking": smoking,
    "Family_History": family
}

patient = pd.DataFrame([patient_values])

# Step 11: Encode patient data
for col in categorical_columns[:-1]:

    encoder = encoders[col]

    value = str(patient.loc[0, col])

    if value not in encoder.classes_:
        raise ValueError(
            f"Invalid {col}: {value}. "
            f"Allowed values: {list(encoder.classes_)}"
        )

    patient[col] = encoder.transform([value])

# Step 12: Maintain feature order
patient = patient[X.columns]

# Step 13: Predict result
prediction = model.predict(patient)[0]

result = target_encoder.inverse_transform([prediction])[0]

# Step 14: Display result
print("\n" + "=" * 50)
print(" PREDICTION RESULT")
print("=" * 50)

print("Patient Prediction:", result)

if result == "Yes":
    print("Result: Osteoporosis Risk Detected")
else:
    print("Result: Osteoporosis Risk Not Detected")

print("=" * 50)
print(" PROGRAM COMPLETED")
print("=" * 50)
