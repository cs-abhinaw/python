# """ undersatnd the dataset
#     identify the problem
#     plan next steps

#     head() show first 5 rows default
#     and tail() shows 5 bottom rows default


#  """

# import pandas as pd
# df=pd.read_json("sample_data.json")

# print("Display 10 rows of first")
# print(df.head(10))

# print("display 10 dataset from bottom")
# print(df.tail())


#to get the information of the data in file of jsonor any other file
import pandas as pd
data = {
    "Name": ['ram', 'shyam', 'Ghanshyam'],
    "Age": [10, 20, 30],
    "City": ['Nagpur', 'mumbai', 'Delhi']
}
# df=pd.read_json("sample_Data.json")
df=pd.DataFrame(data)
print('displaying the info of dataset')
print(df.info())