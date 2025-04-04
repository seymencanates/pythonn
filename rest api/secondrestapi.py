import requests
import json

# Define the URL and the API key
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"
api_key = "AIzaSyCxXXYxPN0agn5d1TW5QuzbOjiJ4Mxzs8U"

# Define the headers
headers = {
    "Content-Type": "application/json"
}

# Define the data to send in the POST request



# Sending a POST request with the API key in the URL
while True:
    #while we are working on calling gemini api , we have encountered basically with 2 problem
    #The first problem is when we send a request to ai , it processes it. Btw when we send 
    #another request it sends request as another request and ai forgots elder chat like an alzheimer
    #how do we handle this problem?
    #the second problem is we cant out of chat while we are on the console because the loop of while
    # always continue to loops , add some if block to make exitable from the loop
    inputs = input("Please enter an input for interact with ai: ")
    data = {
    "contents": [
        {
            "parts": [
                {"text": f"{inputs}"}
                    ]
        }
                ]
    }   
    response = requests.post(
        f"{url}?key={api_key}",  # Append the API key as a query parameter
        headers=headers,
        json=data  # Use json= to directly pass the data as JSON
    )


    #decode the json and reach the messaje that gemini sends on your own

# Print the response content

