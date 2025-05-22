# pandas 

import pandas as pd

# series 
data = [10,20,30,40,50]

ds = pd.Series(data)
print(ds)

# DataFrame
data2 = {
    "Team" :["RCB","GT","MI","DC"],
    "Points" : [14,12,12,10],
    "NRR" : [0.65,0.22,1.09,-0.34] 
}

df = pd.DataFrame(data2)
print(df)

# csv to df
df1 = pd.read_csv("path/file.csv")

# df to xlsx
df2 = df.to_excel("IPL.xlsx")
print(df2)