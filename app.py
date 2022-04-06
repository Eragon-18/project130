import pandas as pd 
import csv

df = pd.read_csv('merged_stars.csv')

df = df.dropna()
df.rename(columns={'Unnamed: 0':'Sr_no'}, inplace=True)

del df['Luminosity']

df.to_csv('final.csv', index=False)