

#Single error catching
try:
    print(x)
except:
    print("An exception occured")

#In this codeline the error code will show by python because x is not defined


#Multi error catching
#We can catch as much as error we wanted for


x = 23

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something went wrong")

