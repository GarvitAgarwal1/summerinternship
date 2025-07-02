import pandas as pd

df1 = pd.DataFrame({
    'ID': [1, 2],
    'Value1': ['A', 'B']
})
df2 = pd.DataFrame({
    'ID': [3, 4],
    'Value2': ['C', 'D']
})
df3 = pd.DataFrame({
    'ID': [2, 3, 5],
    'Value3': ['E', 'F', 'G']
})

concat_df = pd.concat([df1, df2], axis=0, ignore_index=True)
print("Concatenated DataFrame:\n", concat_df)

merged_df = pd.merge(concat_df, df3, on='ID', how='outer')
print("\nMerged DataFrame:\n", merged_df)