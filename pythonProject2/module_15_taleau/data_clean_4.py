import pandas as pd
rent_file = 'ZORI_2015_2024.csv'
rent_data = pd.read_csv(rent_file)
price_file = '3_3.csv'
price_data = pd.read_csv(price_file)
rent_long = rent_data.melt(
    id_vars=['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName'],
    var_name='Quarter',
    value_name='Rent'
)
price_long = price_data.melt(
    id_vars=['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName'],
    var_name='Quarter',
    value_name='Price'
)
merged_data = pd.merge(
    rent_long,
    price_long,
    on=['RegionID', 'RegionName', 'RegionType', 'StateName', 'Quarter'],
    how='inner'
)
output_path = 'price_rent_2015_2024.csv'
merged_data.to_csv(output_path, index=False)
print(f"Data was successfully merged and saved to {output_path}")
