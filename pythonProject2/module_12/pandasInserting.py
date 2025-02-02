import pandas as pd

df = pd.read_csv("flight_safety.csv")

print("total_fatalities" in df) # False

df["total_fatalities"] = df["fatalities_85_99"]+df["fatalities_00_14"]

print("total_fatalities" in df) # True
print(df[df["total_fatalities"] < 15])

