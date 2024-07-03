import pandas as pd

csvData = pd.read_csv('data.csv')
fillNaData = pd.read_csv('data.csv')
fillcalories = pd.read_csv('data.csv')
medianDS = pd.read_csv('data.csv')
meanDS = pd.read_csv('data.csv')
 
print("Loading info about the dataset")
print(csvData.info())
print("loading all data")
print(csvData.to_string())
print("loading the first and last 5 rows")
print(csvData)
print("Loading the first 10 rows")
print(csvData.head(10))
print("Loading the last 10 rows")
print(csvData.tail(10))

fillNaData.fillna(130,inplace=True )
print(fillNaData.to_string())

fillcalories["Calories"].fillna(130, inplace=True)
print(fillcalories.to_string())

meanval = csvData["Calories"].mean()
meanDS["Calories"].fillna(meanval, inplace=True)

medianval = csvData["Calories"].median()
medianDS["Calories"].fillna(medianval, inplace=True)

new_csvData = csvData.dropna()
print(new_csvData.to_string())


