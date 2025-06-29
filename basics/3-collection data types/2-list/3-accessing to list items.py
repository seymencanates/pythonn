

#How do we access to the list items?
#There is a few way to access to an item



#The first way is calling it with its items.
#Example:

fruits = ["apple","strawberries","orange"]

fruit1 = fruits[2]
#in here we chose 3. item of the list because indexs begin from zero

#NEGATIVE INDEXING
# If we use -1 , -2 as an index it will begin the choose from the end of list
# -1 is the last item
# -2 is the second last item etc

fruitNegative = fruits[-1]


#The third way is showing the range of indexes 
#examples

newFruitList = fruits[0:1]
#in here we chose from 0 to 1 for create a new list
# (in the python when u use range of list it will create a new list)

#last item (2. item) wont include in the python code

#There are some details about the range of indexes

#first one is:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
a = thislist[:4]

#Here will choose from the start index until the "kiwi" but not including "kiwi"

#second one is 
b = thislist[2:]
#This range will start from "cherry" and goes until the end of list

#third one is
c = thislist[-4:-1]
#we can use negative indexes too as a range of indexes
#Make examples for the learn these structures all



#How do we check if item exists in list
#Same as dictionary we use "if else" statement

if "apple" in thislist:
    print("Yes 'apple' is in the list")

