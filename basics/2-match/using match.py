


# The syntax of this code is like switch/case methods in python
# we can use it for match values like weekdays or weekends or spesific characthers we wanna catch
#Where can we use this?


listOfNumbers = [1,2,3,4,5,6,7,8,9,0]

for i in listOfNumbers:
    match i:
        case 1:
            print(f"This number{i} is equal to the 'one' ")
        case 2:
            print(f"This number {i} is equal to the 'two' ")
        case 3 | 4 :
            print ("This is combined case , so if even numbers match 3 or 4 it is gonna work on same case")
        case 5 if listOfNumbers[i] ==5:
            print("This is added pattern to the case. It will check with more detail in adddition to case")
        case _:
            print("This is default value so always write this bottom of cases because it is gonna always work")



        

