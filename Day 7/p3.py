import pandas as pd

file_path = r"C:\Users\user\OneDrive\Desktop\Summer internship\Day 7\data.csv"

df = pd.read_csv(file_path)

print("First 5 rows:")
print(df.head())

print("\nDataFrame Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())