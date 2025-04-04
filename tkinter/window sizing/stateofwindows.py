


import tkinter as tkn

form = tkn.Tk()
form.geometry('500x500+350+250')
form.Title('Ders 4')

form.state('normal')
#state function 

#normal
#zoomed is full screen
#iconic is on the subscreen

#if want transparent form

form.wm_attributes('-alpha',0.3)
#this function gets 2 parameter 

#second parameter adjust transparent level
#1 is 0 transparent when it get lower value it will be more transparent
#0 is full transparent level



form.mainloop()