


import requests
import json


response1 = requests.get(
    "https://www.youtube.com/watch?v=qjiAac_8oRA"
    #if we send et request to a server directly it responses source code back
)#get code works like this

print(response1.content)