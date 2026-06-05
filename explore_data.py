import pandas as pd

df = pd.read_csv("data/diabetes.csv")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nOutcome Counts:")
print(df["Outcome"].value_counts())