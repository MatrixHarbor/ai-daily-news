import pandas as pd

df = pd.read_csv("nfl_suspensions.csv")

print(f"{df}\n")
# print(df.columns) # extract the headers

print(f"{df["team"]}\n")

print(df.loc[2]) # extract the row. Use the loc() method to access by row index
print(df["team"])# extract the column

# NaN is an empty