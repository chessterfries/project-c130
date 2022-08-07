import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")
print(list(df))

del df["Luminosity"]
del df["Star_name.1"]
del df["Distance.1"]
del df["Mass.1"]
del df["Radius.1"]
del df["Unnamed: 6"]
del df["Unnamed: 0"]
del df['Star_name'].isna()
del df['Distance'].isna()
del df['Mass'].isna()
del df['Radius'].isna()

df.to_csv('cleaned.csv')