

import tkinter as tkn

form= tkn.Tk()

form.title("Tkinter Dersleri ders-3")

form.geometry('500x250+500+350')
#first number is on the x side
#second side is on the y side
#third and fort parameters are for 
#show the form where we want to show

form.minsize(450,400)
form.maxsize(550,550)

#if we dont want to change the size of
#form
#what would we do?
form.resizable(False,False)
#We declared that x and y coordinats of form
#are unresizable




label=tkn.Label(form,text='Ders3')
label.pack()





form.mainloop()