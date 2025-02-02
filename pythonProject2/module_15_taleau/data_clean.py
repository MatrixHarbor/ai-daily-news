import pandas as pd
file_path = '3_1.csv'
df = pd.read_csv(file_path)
df['RegionName'] = df['RegionName'].str.split(',').str[0]
output_path = '3_2.csv'
df.to_csv(output_path, index=False)
print(f"{output_path}")
file_path = '3_2.csv'
df = pd.read_csv(file_path)
df_cleaned = df.dropna()
output_path = '3_3.csv'
df_cleaned.to_csv(output_path, index=False)
print(f" {output_path}")
file_path = '2_1.csv'
df = pd.read_csv(file_path)
columns_to_keep = ['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName']
columns_to_keep += [col for col in df.columns if col.startswith(('1/31', '4/30', '7/31', '10/31')) and any(year in col for year in ['15', '16', '17', '18', '19', '20', '21', '22', '23', '24'])]
df_filtered = df[columns_to_keep]
output_path = '2_2.csv'
df_filtered.to_csv(output_path, index=False)
print(f"data saved in {output_path}")
