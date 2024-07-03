import pandas as pd

pd.options.display.max_rows = 9999
# csvData = pd.read_csv('data.csv')
# print(csvData)

jsonData = pd.read_json('data.json')
# print(jsonData.max())
# print(jsonData.min())
# print(jsonData.head(10))
# print(jsonData.tail(12))

print(jsonData.info())



#print(pd.options.display.max_rows)

