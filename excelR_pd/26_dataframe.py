# DataFrame

import pandas as pd

df = pd.read_excel("IPL.xlsx")
# print(df)

print(f'columns : {df.columns}')

print(f'index : {df.index}')

print(f'dtypes : {df.dtypes}')

print(f'shape : {df.shape}')

print(f'info : {df.info}')

print(f'head : {df.head(2)}')

print(f'tail : {df.tail(1)}')