import pandas as pd

df = pd.read_csv("https://www.sololearn.com/uploads/ca-covid.csv")
df.set_index("date", inplace=True)

print(df.head())