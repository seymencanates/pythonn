firstDictIsAboutAnimals = {

      "animal1" : "zebra",
      "animal2" : "lion",
      "animal3" : "carrot"

}

#we will use for loop for the loop all the keys(as default) in the dict
# But there is some way too for the loop values


#the code below on the comment(here), its writes all the keys to the screen


for x in firstDictIsAboutAnimals:
    print(x)


#We shaped te code as to show values on the screen at the below code

for x in firstDictIsAboutAnimals:
    print(firstDictIsAboutAnimals[x])

#U can also use values() method to print values to the screen as this:

for x in firstDictIsAboutAnimals.values():
    print(x)

#also same for the keys:

for x in firstDictIsAboutAnimals.keys():
    print(x)

#also u can loop both of values and keys using items() method:

for x,y in firstDictIsAboutAnimals.items():
    print(x," " ,y)




