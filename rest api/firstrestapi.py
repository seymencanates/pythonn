

import requests
import pyodbc


API_KEY = "c64a9ef0bb2f356dc442fd87b3b4e519"
#we mostly uses keys for access into the 

page=1


response = requests.get(
    "https://api.themoviedb.org/3/movie/popular",#this is url parameter of get method
    #get method has 1 required parameter. 
    # It's url parameter,we use this parametere to determine address
    params={"api_key":API_KEY
            #params is optional, it helps to send data as a query string.
            #this means we send these lines to the server as a data.
            #we should understand how these lines processes on the other side
            , "page":page}
    )
    #get method of requests library provides to get response from the server
    

movie_data = response.json()
print(movie_data)
page +=1