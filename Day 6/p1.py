import pandas as pd

date_series = pd.Series([
    '2023-01-01',
    '2023-02-15',
    '2023-03-10'
])

print("Original date_series:")
print(date_series)

time_series = pd.to_datetime(date_series)

print("\nConverted time_series:")
print(time_series)