
x = True
#Single error catching
try:
    print(x)
except:
    print("An exception occured")

#In this codeline the error code will show by python because x is not defined(we added it for unmistaken code
# erase it while trying code)


#Multi error catching
#We can catch as much as error we wanted for


x = 238

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something went wrong")

#we can also use else too if any error doesnt occurs by program

try:
    print("My friend is a selfish")
except:
    print("A problem have been occured")
else:
    print("Any problem didnt occur")

#there is another code type like finally. This code works even except or try code works

#here is an example

try:
    f = open("data.json" , "r+")
    try:
        f.write("Lorem Ipsum")
    except:
        print("Something went wrong while writing into the file")
    finally:
        f.close()
except:
    print("Something went wrong while opening the file")

#we can also throw an exception like on the other languages
#we uses often raise for this

x = -1

if x< 0:
    raise Exception("Sorry , no numbers below zero")
