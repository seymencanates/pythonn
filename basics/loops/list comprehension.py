

#This method makes python easier to write
#list comprehension aim is make easier to creating list with for loop

# with traditional for loop
numbers = []
for i in range(5):
    numbers.append(i * 2)

# with list comprehension
numbers = [i * 2 for i in range(5)]

#list comprehension structure is : variable = [gonna add value , for loop ]

#examples u did

import random

randomNumbers = [int(random.random()*1000) for _ in range(100)]

#range function provides a range for rotate the loop 




print(randomNumbers)