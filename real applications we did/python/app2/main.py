

import tkinter as tk

import datetime

dates = {

}
date = datetime.datetime.now()

dateFunctions = [date.strftime("%S"),date.strftime("%M"),date.strftime("%H"),date.strftime("%d"),
                 date.strftime("%B"),date.strftime("%Y")]
form = tk.Tk()



def getDate():

    global dates
    global date
    global dateFunctions
    #here is a basic passive storage like ram before we save the whole data into the json or database

    


    if dates is None or not dates:
        dates = dict(savedDatek1=dict(second=dateFunctions[0],minute=dateFunctions[1],
                                        hour=dateFunctions[2],day=dateFunctions[3],month=dateFunctions[4],
                                        year=dateFunctions[5]))
        print(dates)
    else:
        #in here we need a basic nlp function that understands which data we are in if we use the coverer dict name
        #full of string
        #or else we can determine the  structure of coverer like this : savedDate+number
        #this is easier to determine

        #we will use "k" letter to seperate the line.
        lister = list(dates.keys())
        
        #we got all the keys in the dict and converted them into a list
        lengthOflist = len(lister)
        
        #and in here we determined the lenght of list
        indexer = str(lister[lengthOflist-1]).split("k")
        
        #we seperated code based on k letter
        newindexer = int(indexer[1])+1
        
        #we assigned new indexer
        
        newNestedDictName = indexer[0] + "k" + str(newindexer)

        dates[newNestedDictName] = dict(second=dateFunctions[0],minute=dateFunctions[1],
                                        hour=dateFunctions[2],day=dateFunctions[3],month=dateFunctions[4],
                                        year=dateFunctions[5])
        print(dates)


button = tk.Button(form,text='Tıkla',fg='black',
                    bg='red',
                    command=getDate)



button.pack()
form.mainloop()




