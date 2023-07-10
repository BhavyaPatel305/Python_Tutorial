import pandas as pd
data = pd.read_csv("./data.csv",index_col="Name")
first = data.loc["Lyle"]
second = data.loc["Ralf"]
print(first)
print(second)