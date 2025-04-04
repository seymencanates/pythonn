
import os
import sys
import json
    #we appointed json library into pyton file
parentRotation = os.path.dirname(__file__)
connectionToJsonLocation = os.path.join(parentRotation, '..' , '..')
sys.path.append(os.path.abspath(connectionToJsonLocation))
import connectionToJson
    #the first question we asked for about listing python is How do we read and list by 1 by from the data?

data = connectionToJson.connection()
    #this line assigns connection function from connectionToJson file to data object

    #here ir is reply for question u ask:


for person_head ,person_information in data['people'].items():  
    #data['people'] is a list on the json file. And items() metod returns keys and informations 1 by 1
    #cause of for loop
    print(f'{person_head}',f'{person_information}')

