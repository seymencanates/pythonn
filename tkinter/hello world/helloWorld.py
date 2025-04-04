import tkinter as tk
#this is importer that imports all classes , functions and variables from the package of tkinter

root=tk.Tk()
#this creates grapical window to append elements inside it

a = tk.Label(root, text="Hello, world!")
a.grid()
#we created a label on here and append text on the second parameter


# adding Entry Field
txt = tk.Entry(root, width=10)
txt.grid(column =1, row =0)

# function to display user text when 

# button is clicked
def clicked():

    res = "You wrote" + txt.get()
    a.configure(text = res)

# button widget with red color text inside
btn = tk.Button(root, text = "Click me" ,
             fg = "red", command=clicked)
# Set Button Grid
btn.grid(column=2, row=0)

# root window title and dimension
root.title("Welcome to My Page")
# Set geometry (widthxheight)
root.geometry('1000x600')

# a.pack()
#This tells it to size itself to fit the given text, and make itself visible

root.mainloop()
# The application window does not appear 
# before you enter the main loop. 
# This method says to take all the widgets and 
# objects we created, render them on our screen, 
# and respond to any interactions. 
# The program stays in the loop until we close the window.