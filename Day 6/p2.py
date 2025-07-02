import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Value1': ['A', 'B', 'C']
})

df2 = pd.DataFrame({
    'ID': [2, 3, 4],
    'Value2': ['X', 'Y', 'Z']
})

inner_merge = pd.merge(df1, df2, on='ID', how='inner')
print("Inner Merge:\n", inner_merge)

left_join = pd.merge(df1, df2, on='ID', how='left')
print("\nLeft Join:\n", left_join)

right_merge = pd.merge(df1, df2, on='ID', how='right')
print("\nRight Join (merge):\n", right_merge)

df1_indexed = df1.set_index('ID')
df2_indexed = df2.set_index('ID')
index_join = df1_indexed.join(df2_indexed, how='right')
print("\nRight Join (index-based join):\n", index_join)