
firstDictIsAboutAnimals = {

      "animal1" : "zebra",
      "animal2" : "lion",
      "animal3" : "carrot"
}

#dict is created by python programmers its for storing data with key value pair features.
#dict is changeable and do not allow duplicates.

#What is a duplicate on programming?
#A duplicate situation is repeating data on the stored value.So with this "doesnt allowing" feature
#python programmers makes right



#If we want to learn how many items a dictionary has , we should use len() function for the learn the lenght of
#dictionary
print(len(firstDictIsAboutAnimals))
#as we see when we print the lenght we might see cause of len() function


#dictionaries can get any type of data. No limit or restrictions about this.
secondDictionaryIsMixedDictionaryForShowDictionariesCanGetEveryTypeOfData = {

        "carBrand" : "Ford",
        "electric" : False,
        "gas/oil" : True,
        "yearOfProduction" : 1999,
        "colorsUMightHaveBuy" : ["blue","orange","pink","green"]
}
#as we see the dictionaries can get any type of data including lists

#when we try to print a dict's type with type function we get <class 'dict'> value back



#We can convert to data to a dict basically with the dict() function 

creatingADictDynamically = dict(name = "John",sex="Male",age=45,country="New Zealand")
print(creatingADictDynamically)



#how do we access to the Items with using Python?


#we should use the key as a indexer inside square brackets
#for example
print(creatingADictDynamically["sex"])

#also there is another option we might use
#get function does same job
print(creatingADictDynamically.get("sex"))


#How can we get all the keys in the dictionary?
#we should use keys() method for this

print(firstDictIsAboutAnimals.keys())

#for the values instead of keys we should use values()

print(firstDictIsAboutAnimals.values())


#But what if we want to get both key/value in same time?
#we can of course use items() method for this.

print(firstDictIsAboutAnimals.items())

#these three function creates a wiev of dictionary. So any change may be done by us will effect also functions
#result.

#check if the key exist

#we will use "in" for this aim

if "sex" in creatingADictDynamically:
    print(f"Sex is in the dictionary of {creatingADictDynamically["sex"]}") 






#How To update?

#u can change the value with the key feature

firstDictIsAboutAnimals["animal1"] = "crocodile"

print(firstDictIsAboutAnimals["animal1"])

#or else u can use update method
firstDictIsAboutAnimals.update({"animal1" : "hipopotam"})

print(firstDictIsAboutAnimals["animal1"])

#U can use these two alternative way also for add to a dict. Only 1 difference is
#u should determine an unassigned value into it


#How to Remove?
#u can remove the key/value with a few way
#u can use pop() method , it erases value with specified key name
firstDictIsAboutAnimals.pop("animal1")


#There is also another opportunity
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
firstDictIsAboutAnimals.popitem()

#there is del method that does same job with the pop() method
del firstDictIsAboutAnimals["animal2"]

#there is a method that erases all the data inside the dictionary.Its clear() method
firstDictIsAboutAnimals.clear()


