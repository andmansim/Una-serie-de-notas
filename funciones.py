import pandas as pd

df = pd.read_csv('StudentsPerformance.csv', delimiter= ',', encoding= 'UTF-8' )
print(df)
df_new = pd.DataFrame({'math score': df['math score'], 'reading score': df['reading score'], 'writing score': df['writing score']})
print(df_new)