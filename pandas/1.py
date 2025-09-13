# import pandas as pd

# #read data from csv file into dataframe use latin1 or utf-8
# # df=pd.read_csv("sales_data_sample.csv",encoding="latin1")
# #to read file in excel file
# # df=pd.read_excel("file path")
# #for json file

# # df=pd.read_json("file path")
# print(df)



""" to save file in csv """

import pandas as pd

data = {
    "Name": ['ram', 'shyam', 'Ghanshyam'],
    "Age": [10, 20, 30],
    "City": ['Nagpur', 'mumbai', 'Delhi']
}

df = pd.DataFrame(data)
print(df)

# Save the DataFrame to Excel
df.to_excel("output.xlsx", index=False)

# Now read the saved Excel file
df_read = pd.read_excel("output.xlsx")

# Now read the saved json file
df_read1 = pd.read_json("output.xlsx")

print(df_read1)
