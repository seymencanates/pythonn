


import tkinter as tk

form = tk.Tk()
#we called Tk library.

form.title("Tkinter Dersleri 1")
#It determines title

etiket = tk.Label(text='Tkinter Python')

etiket.pack()#provides visibility on the form

etiket2 = tk.Label(form,text='Python Tkinter Dersleri')

etiket2.pack()
#etiket2 is the right version of the co"de because:
#if we had one or more than 1 form in same page and
#if we didnt show to the tag which mainform it will be located
#it would be some trouble like going into the wrong form

#later these we are entering into the details

label = tk.Label(form,text='Python Tkinter')
label.pack()

label2 = tk.Label(form,text='Ders 2',fg='red')
#fg means foreground color
label2.pack()

label3 = tk.Label(form,text='Ders 2 background color',fg='black',bg='green')
#bg means background color
label3.pack()

label4 = tk.Label(form,text='yeni Label',fg='red',bg='green',font='Times 15 italic')

label4.pack()

label5 = tk.Label(form,text='En son Label',fg='green',bg='red',font='Times 17 bold')

label5.pack()

form.mainloop()
#it loops eternity times over and over

