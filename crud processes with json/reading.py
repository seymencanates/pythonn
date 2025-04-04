
import os
#this library helps us about interacting with operating system. We can create and erase folders and
#files with this library , and we can move a file from a location to another location with tis library
#there is more we can do with this library
import sys
#This library provides to interact with the python interpreter.More detail will be written when we pass
#into this library

parentRotation = os.path.dirname(__file__)

#__file__ : its a special variable that hols's current file's path.
# os.path.dirname : determine's directory path.



connectionToJsonLocation = os.path.join(parentRotation, '..')

#os.path.join function combines one 1 more than 1 component into a single complete path.
#'..' refers parent directory

#this code line helps to go 1 level up directory


sys.path.append(os.path.abspath(connectionToJsonLocation))

#os.path.abspath gives us absolute path of the directory that given into the function
#a question: what is the difference between relative path and absolute path?

#sys.path is a list that contains python module's directories when we use import. So essentially:
#sys.path.append code add's absolute path of parent location for search python module's 
#when we use import


import connectionToJson


#for use the json on the python u should import this library

data = connectionToJson.connection()

    
print(data)
    #this will help u to show data.json content as a dictionary of python