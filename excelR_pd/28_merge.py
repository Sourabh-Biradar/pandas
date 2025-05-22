# merge : 2 or more DF using common column
# on = "common col"   (better to use all the time)
# how = inner,outer,left,right

import pandas as pd

df1 = pd.DataFrame(
    {"name" : ['Abc','Mno','Rst','Xyz'],
    'age'  : [32,19,26,55],
    'city' : ['Pune','Bluru','Manali','Mardas']}
)

df2 = pd.DataFrame(
    {"name" : ['abc','Mno','xyz'],
    'occp'  : ['Doctor','Student','Retd.'],
    'phone' : ['iPhone','Samsung','Nokia']},
)

# inner (default) : common keys
df3 = pd.merge(df1,df2,on="name")
print(df3)

# outer : everything
df4 = pd.merge(df1,df2,on="name",how="outer")
print(df4)

# left : all from left , common from right
df5 = pd.merge(df1,df2,on="name",how="left")
print(df5)

# right : all from right , common from left
df6 = pd.merge(df1,df2,on="name",how="right")
print(df6)