


import pandas
import pandas._version

print(pandas._version)

data = {
    "animals" : ["owl","bird","parrot"],
    "vegetables" : ["onion","tomato","carrot"]
}

df = pandas.DataFrame(data , index = ["day1","day2","day3"])
#with index argument 

print(df)


#how do we locate the rows and columns?

print(df.loc[0])
#This will return the first row of the dataFrame


#return the first and second row

print(df.loc[0,1])

