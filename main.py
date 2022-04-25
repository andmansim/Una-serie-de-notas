import pandas as pd
import numpy as np
import funciones as jmp

df = pd.read_csv('StudentsPerformance.csv', delimiter= ',', encoding= 'UTF-8' )
print(df)
#Separar datos importantes
df_new = pd.DataFrame({'math score': df['math score'], 'reading score': df['reading score'], 'writing score': df['writing score']})
print(df_new)

#--- ANALISIS DE UNA CARACTERISTICA ---
stats = jmp.JMPEstadisticas(df_new['math score'])
stats.analisisCaracteristica()