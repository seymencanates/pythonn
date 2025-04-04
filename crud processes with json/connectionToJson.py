
import json

def connection():
#That is a connection who provides to call data.json from other python files


    with open('data.json','r+')as file:
        # we opened data.json and give a shortname to it 'file'
        data = json.load(file)
        #we loaded json data as a dictionary
        file.close()
        #we should close after the process done or else we will have unexpected trouble with it
        return data
        #we returned data object
        
        #we have encountered some problem. When we use this function for read it works.But when we 
        #use this function for write some data into the file or erase update some file it doesnt work.
        #How do we handle this problem?

def writing(head,name,surname,age):
    #we created a writing function with 4 parameter

    with open('data.json', 'r+') as file:
        root = json.load(file)
        #we loaded json data as a dictionary to a variable


        if "people" not in root:
            root["people"] = {}
            #this code creates people json dictionary if its not exist
    
        root["people"][head] = {"name": name, "surname": surname, "age": age}

        file.seek(0)
        #this seek function bring pointer back to the beginning

        json.dump(root, file, indent=4)# Write the updated data to the file
        #The indent=4 argument makes the output pretty-printed for readability.

        file.truncate()
        #ensures that any leftover content from the previous 
        # write (in case the new data is shorter) is removed.

        file.close()
        #closes te file


def erasing(head):

    with open('data.json','r+') as file:

        root = json.load(file)
        

        

        if 'people' in root and head in root['people']:

            del root['people'][head]

        file.seek(0)
            
        json.dump(root, file, indent=4)

            
        file.truncate()
        file.close()