import pandas as pd

data = {
    "name":['ram','shyam','dev','suraj','aishu'],
    "age":[10,23,12,12,23],
    "salary":[12000,23000,34000,450000,54000],
    "performance":[34,45,56,67,34]

}
df=pd.DataFrame(data)
print("Sample data frame")
print(df)
# print('descriptive Statistisc')
# print(df.describe())

#to see shape
print(f'shape{df.shape}')
print(f'column number{df.columns}')