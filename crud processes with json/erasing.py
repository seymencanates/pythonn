
import connectionToJson

listing = connectionToJson.connection()

dataheads = list(listing['people'].keys())
datacontents = list(listing['people'].values())

counter = 0
for head, content in zip(dataheads, datacontents):
    print(f"{counter + 1}. Data head: {head}")
    print(content)
    counter += 1

userInput = int(input('Which person u want to erase?: '))

if 1 <= userInput <= len(dataheads):
    connectionToJson.erasing(dataheads[userInput - 1])
else:
    print('Invalid User Have been chosen')