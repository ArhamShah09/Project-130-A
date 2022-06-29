import pandas as pd

df = pd.read_csv("total_stars.csv")
print(df.shape)
print(list(df))

del df['Unnamed: 0']
del df['Luminosity']
del df['Unnamed: 6']
del df['Star_name_']
del df['Distance_']
del df['Mass_']
del df['Radius_']

print(df.shape)
print(list(df))

df.to_csv('cleaned.csv')