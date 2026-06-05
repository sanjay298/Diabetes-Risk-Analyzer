import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
# Load dataset
df = pd.read_csv("data/diabetes.csv")

print(df.head())
columns = [
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI"
]

for col in columns:
    median = df[col].replace(0, pd.NA).median()
    df[col] = df[col].replace(0, median)

X = df.drop("Outcome", axis=1)
y = df["Outcome"]

print("Features Shape:", X.shape)
print("Target Shape:", y.shape)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Data:", X_train.shape)
print("Testing Data:", X_test.shape)


model = LogisticRegression(max_iter=1000)

model.fit(X_train, y_train)

print("Model Trained Successfully")

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print("Accuracy:", accuracy)
sample = [[
    2,      # Pregnancies
    130,    # Glucose
    70,     # BloodPressure
    25,     # SkinThickness
    100,    # Insulin
    28,     # BMI
    0.5,    # DiabetesPedigreeFunction
    30      # Age
]]
prediction = model.predict(sample)
print("Prediction:", prediction)

joblib.dump(model, "model/diabetes_model.pkl")
print("Model Saved Successfully")