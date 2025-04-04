


import os
import json
import sys

parentDirectionLocation = os.path.dirname(__file__)

connectionToJsonLocation = os.path.join(parentDirectionLocation , "..")

sys.path.append(os.path.abspath(connectionToJsonLocation))

import connectionToJson

insideData = connectionToJson.connection()

print(insideData['people'])

insideData['people']['sixthPerson'] = {"name": 'Ali', "surname": 'Ateş', "age": 45}

connectionToJson.writing(insideData)

print(insideData['people'])




