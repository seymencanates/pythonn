

people = { "people":{
        "firstPerson": 
            {   
                "name": "iclal", 
                "surname": "akÃ§a", 
                "age": "12"
            }, 
        "secondPerson": 
        {
            "name": "iclall", 
            "surname": "akÃ§a",
             "age": "12"
        }, 
        "thirdPerson": {
            "name": "ali", 
            "surname": "yÄ±lmaz", 
            "age": "15"
        }, 
        "fourthPerson": {
            "name": "ayÅŸe", 
            "surname": "Ã§elik", 
            "age": "18"
        }, 
        "fifthPerson": {
            "name": "mehmet", 
            "surname": "kara", 
            "age": "20"
        }
}} 

#here is an example to the nested dictionaries. Dictionary inside another dictionary.


#How do we access to the dictionaries?

#The first way is:
print(people["people"]["firstPerson"])

#second way is the looping for the choose right data




#how do we loop nested dictionaries?

for x , object in people.items():
    print(x)
    for y,in object:
        print(y+" : ",object[y])

#U can access any item u wanted with this way inside a nested dictionary.

#Of course this for loop is nor right with the structure of nested dictionary we used for now but lets solve it

