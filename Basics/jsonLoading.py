import pandas as pd

jsonData = pd.read_json('data.json')

print(jsonData.to_string()) #print all Data
print(jsonData.head(10)) #print the first 10 rows in the data file
print(jsonData.tail(15)) #print the last 15 rows in the data file
print(jsonData.max())  #print the maximum value in the data file
print(jsonData.min())  #print the minimum value in the data file
print(jsonData.info()) #print info of the data file
