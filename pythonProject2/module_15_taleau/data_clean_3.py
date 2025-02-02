# import pandas as pd
#
# # 读取Excel数据
# file_path = '3.csv'  # 替换为您的文件路径
# df = pd.read_csv(file_path)
#
# # 保留的基础列
# columns_to_keep = ['RegionID', 'SizeRank', 'RegionName', 'RegionType', 'StateName']
#
# # 筛选符合季度和年份范围的列
# columns_to_keep += [col for col in df.columns if col.startswith(('1/31', '4/30', '7/31', '10/31')) and any(year in col for year in ['15', '16', '17', '18', '19', '20', '21', '22', '23', '24'])]
#
# # 筛选所需列
# df_filtered = df[columns_to_keep]
#
# # 保存筛选后的数据
# output_path = '3_1.csv'
# df_filtered.to_csv(output_path, index=False)
#
# print(f"数据已筛选并保存到 {output_path}")

