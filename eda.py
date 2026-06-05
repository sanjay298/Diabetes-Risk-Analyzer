import pandas as pd

df = pd.read_csv("data/diabetes.csv")

print("Dataset Shape:", df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())
print("\nMissing Values:")
print(df.isnull().sum())

print("\nZero Values Count")

columns = [
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI"
]

for col in columns:
    print(col, (df[col] == 0).sum())

