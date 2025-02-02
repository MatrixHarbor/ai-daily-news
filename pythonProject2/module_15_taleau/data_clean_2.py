import pandas as pd

# 读取房租数据
rent_file = 'ZORI_2015_2024.csv'  # 替换为您的房租文件路径
rent_data = pd.read_csv(rent_file)

# 读取房价数据
price_file = '3_3.csv'  # 替换为您的房价文件路径
price_data = pd.read_csv(price_file)

# 将房租数据从宽表转换为长表
rent_long = rent_data.melt(
    id_vars=['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName'],
    var_name='Quarter',
    value_name='Rent'
)

# 将房价数据从宽表转换为长表
price_long = price_data.melt(
    id_vars=['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName'],
    var_name='Quarter',
    value_name='Price'
)

# 合并房租和房价数据
merged_data = pd.merge(
    rent_long,
    price_long,
    on=['RegionID', 'RegionName', 'RegionType', 'StateName', 'Quarter'],
    how='inner'
)

# 保存合并后的数据
output_path = 'price_rent_2015_2024.csv'
merged_data.to_csv(output_path, index=False)

print(f"数据已成功合并并保存到 {output_path}")