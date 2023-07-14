import pandas as pd
import numpy as np
data = [1,2,3,4,5]
ser = pd.Series(data)
print(ser)


data1 = np.array(['a','b','c','d'])
print(pd.Series(data1))
print(data1[:3])