import pandas as pd

dates = pd.Series(pd.date_range(start="2023-01-01", periods=3, freq='D'))
print("Original dates:")
print(dates)

print("\nYear:\n",dates.dt.year)
print("Month:\n",dates.dt.month)
print("Weekday:\n",dates.dt.day_name())

dates_plus7 = dates + pd.Timedelta(days=7)
print("\nDates + 7 days:")
print(dates_plus7)

filtered = dates[dates > '2023-01-03']
print(filtered)