import pandas as pd

mydataset  = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passing': [3,7,2]
}
myvar = pd.DataFrame(mydataset)
#print(myvar)

data = {
    "calories":  [420, 285, 658],
    "duration": [50, 80, 45]
}
myvar4 = pd.DataFrame(data, index=["day 1", "day 2", "day 3"])
#print(myvar4)
print(myvar4.loc["day 2"])

mydataset2 = [1,2,8,5,4]
myvar2 = pd.Series(mydataset2, index=["X" , "Y" , "Z" , "A" , "B"])
#print(myvar2)

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar3 = pd.Series(calories)
#print(myvar3)







#print(myvar2 [3])
#print(myvar2["Y"])

#print(pd.__version__)