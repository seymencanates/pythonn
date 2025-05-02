
import tkinter as guiProvider
#we imported tkinter library for access into the gui 
import random as randomChooser
#we imported random library for;
    #determine the random numbers,
    #accessing with randomized way

gui = guiProvider.Tk()
#we created a gui page
gui.title("Randomized App")
#we gave a title to gui page
gui.geometry("500x400")
#we specified sizes of gui page , the height is 500 pixel and the width is 400 pixel


listbox = guiProvider.Listbox(gui, height = 15, 
                  width = 20, 
                  bg = "grey",
                  activestyle = 'dotbox', 
                  font = "Helvetica",
                  fg = "yellow")
#We created a listbox for show the random chosen numbers

listbox.pack()
#we packed and added listbox to the gui

stringCharactherList = ["a","A","b","B","c","C","ç","Ç","d","D","e","E","f","F","g","G","ğ","Ğ","h","H"
,"ı","I","i","İ","j","J","k","K","l","L","m","M","n","N","o","O","ö","Ö","p","P","r","R","s","S","ş","Ş","t","T"
,"u","U","ü","Ü","v","V","y","Y","z","Z"]
#array for the randomized words



def randomize():
    #we created a function that will call by button when its clicked
    #this function does;
        #specifies randomized numbers and strings

    random1 = randomChooser.randint(1,3)
    #This will help us to choose between 3 categories (float , string or int)

    if random1 == 1:
        random2 = randomChooser.randint(0,1000000000000000000)
        listbox.insert(1 ,random2)
        #if random1 chooses 1 number , choose an int number and insert it into the listBox
    elif random1 == 2:
        random2 = randomChooser.uniform(0,1000000000000000000)
        listbox.insert(1 ,random2)
        #if random1 chooses 2 number , choose an float number and insert it into the listBox
    elif random1 == 3:
        random2 = randomChooser.randint(1,30)
        #specify a random number for how many length word will has
        i = 1
        #i is a counter for while loop. It will inrease 1 by 1 until it reach to random number chosen by random2 variable on the elif block
        newWord = ""
        #newWord is a storage for the random word we will create with function
        while i <= random2:
            random3 = stringCharactherList[randomChooser.randint(0,len(stringCharactherList)- 1)]
            #over here we are choosing a random characther on list above function between zero and length of list
            newWord = newWord + random3
            #adding chosen characther to a random word
            i += 1
            #increasing counter until it reach to random2
        listbox.insert(1 ,newWord)   
        #inserting random word to listBox



def closePage():
    gui.destroy()
    #we created a page for close gui

button = guiProvider.Button(gui,
                            text="Click me For the see a random value",
                            command=randomize)
    #created a button for call and work function
button.pack()
    #we packed button

exitButton = guiProvider.Button(gui,text="Exit",command=closePage)
exitButton.pack()
    #we created a button for exit from the gui
 


gui.mainloop()