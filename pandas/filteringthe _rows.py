import pandas as pd

data = {
    "name":['ram','shyam','dev','suraj','aishu'],
    "age":[10,23,12,12,23],
    "salary":[12000,23000,34000,450000,54000],
    "performance":[34,45,56,67,34]

}
df=pd.DataFrame(data)

#single conditions
high_salary=df[df['salary']>50000]
print("employee with the salary grater than 50k")
print(high_salary)

#mutiple conditions
filtered = df[(df['age'] > 10) & (df['salary'] > 50000)]
print("Salary greater than 50k and age greater than 30")
print(filtered)
