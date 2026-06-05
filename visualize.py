import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/diabetes.csv")

df["Outcome"].value_counts().plot(kind="bar")

plt.title("Diabetes Distribution")
plt.xlabel("Outcome")
plt.ylabel("Count")

plt.show()