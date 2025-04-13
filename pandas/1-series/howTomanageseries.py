

import pandas as pd


#a series is like a column in a table

a = [1,4,5,5,5,6,7,9,0,23,45,65,786,5,44,32,21,4,123,4545,65543,4535232,24557665,2112,12,4,34]
#in here we created a list from numbers

series = pd.Series(a)
#Series is for create 1 dimensional array.
#Here series turned datas in list to columns


print(series)


#we can access to the specific value with using labels
print(series[0])


#we can also create our own labels 

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

#when we create ouw own label we should access it with referring label we created for

print(myvar["y"])


#we can also use key/value pairs like dict as a series column
#in this situation keys are labels and values are column objects 

#example

arabicLetters = {"elif" : "ا" , "be" :  " بـ" , "te":"تـ"}

mySeries = pd.Series(arabicLetters)

print(mySeries)


#we can specify which datas we want to include in the Series. We will use index argument for this.

mySeries2 = pd.Series(arabicLetters,index=["elif","be"])

print(mySeries2)

#for the two dimensional and multi dimensional series look at the dataframes. Here is used for single dimensional
# datas