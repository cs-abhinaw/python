""" 
1.select specific column
2. filter rows 
3.column multiple condition

 1.square brackets
 2.boolean condition

 selecting column
 1. a series returnd by single 
 2. dataframe multiple column of data 

 column =df("column Name")
 subset=df("column1","column2","...")

 filtering rows 
 boolean indexing

 #based on the single condition
 filtered_Rows= df[df["salary]>50000]

 #combined multiple conditions
 filtered_Rows=  df[(df["salary]>5000)&(df["column2]<80000)]
 """


import pandas as pd

data = {
    "name":['ram','shyam','dev','suraj','aishu'],
    "age":[10,23,12,12,23],
    "salary":[12000,23000,34000,450000,54000],
    "performance":[34,45,56,67,34]

}
df=pd.DataFrame(data)

#displaying the dataframe
print("sample Dataframe")
print(df)
print("names (single column returned series)")
name=df['age']
print(name)

#selecting multiple columns
subset=df[["name","age"]]
print("\n seubset with the name and salary")
print(subset)