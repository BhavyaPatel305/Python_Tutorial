import pandas as pd

data = pd.read_csv("./ipl.csv")
data.dropna(inplace=True)
data["Name"] = data["Name"].str.upper()
data["Name"] = data["Name"].str.replace("A","@")
print(data)
