# location

# loc : label based indexing
# iloc : integer based indexing

import pandas as pd

# loc
df = pd.read_excel("IPL.xlsx")

print(df.loc[2])    # row = 2 

print(df.loc[1:3])   # row 1 to 3 (incld. 3)

print(df.loc[2,'Team'])   # row = 2 ; col = Team

print(df.loc[1:3,"Points"])  # row 1 to 3 ; points

print(df.loc[0:2,['Team','Points']])  # row 0 to 2 & Teams & Points only

# iloc
# same as loc but instead of column names we need to pass column index

print(df.iloc[2])    # row = 2 

print(df.iloc[1:3])   # row 1 to 2 (Not 3)

print(df.iloc[2, 1])   # row = 2 ; col = Team

print(df.iloc[1:3, 2])  # row 1 to 2 ; points

print(df.iloc[0:2, [1,3]])