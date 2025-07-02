import pandas as pd

df = pd.DataFrame({
    "Name": ["Kushal", "Vishnu", "Krishna", "David"],
    "Age": [25, 30, 35, 28],
    "Score": [85, 90, 95, 88]
})
print(df)

print("\nUsing iterrows():")
for idx, row in df.iterrows():
    print(f"Index {idx} - Name: {row['Name']}, Age: {row['Age']}")

print("\nUsing itertuples():")
for row in df.itertuples():
    print(f"Index {row.Index} - Name: {row.Name}, Age: {row.Age}")

adults = df[df["Age"] >= 30]
print("\nRows where Age >= 30:\n", adults)

third_row = df.iloc[2]
print("\nThird row using iloc[]:\n", third_row)

limited = df.loc[1:3, ["Name", "Score"]]
print("\nRows 1 to 3 with only 'Name' and 'Score' columns:\n", limited)

df_dropped = df[df["Age"] != 30]
print("\nDataFrame after dropping rows where Age == 30:\n", df_dropped)

new_row = pd.DataFrame({"Name": ["Eva"], "Age": [27], "Score": [92]})
df_inserted = pd.concat([df.iloc[:2], new_row, df.iloc[2:]]).reset_index(drop=True)
print("\nDataFrame after inserting a new row after index 1:\n", df_inserted)

list_of_rows = df.to_dict("records")
print("\nList of rows as dictionaries:\n", list_of_rows)