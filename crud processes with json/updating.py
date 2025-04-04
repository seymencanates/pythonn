import os
import sys
import json

# You need to import the connection and writing functions from your connectionToJson module
currentFolderLocation = os.path.dirname(__file__)
dataJsonLocation = os.path.join(currentFolderLocation,'..')
sys.path.append(os.path.abspath(dataJsonLocation))
import connectionToJson

# Load the data from data.json using the connection function
transferedData = connectionToJson.connection()

# Collect all the heads (keys) and their corresponding contents
dataheads = list(transferedData['people'].keys())
datacontents = list(transferedData['people'].values())

# Display the available data
counter2 = 0
for head, content in zip(dataheads, datacontents):
    print(f"{counter2 + 1}. Data head: {head}")
    print(content)
    counter2 += 1

# Ask the user for the index of the data they want to update
userChose = int(input('Please give us chosen index for update: '))

# Update the chosen data
if 1 <= userChose <= len(dataheads):
    # Get the corresponding data head and content
    head_to_update = dataheads[userChose - 1]
    content_to_update = datacontents[userChose - 1]

    # Ask the user for new values for name, surname, and age
    name = input(f"Enter the new name (current: {content_to_update['name']}): ")
    surname = input(f"Enter the new surname (current: {content_to_update['surname']}): ")
    age = input(f"Enter the new age (current: {content_to_update['age']}): ")

    # Use the writing function to update the data
    connectionToJson.writing(head_to_update, name, surname, age)
    print(f"Data for {head_to_update} updated successfully!")
else:
    print("Invalid index chosen.")
