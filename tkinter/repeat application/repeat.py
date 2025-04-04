

import tkinter as tk
import random as rd

form = tk.Tk()

form.title('Tekrar Uygulaması')
form.geometry('500x400+500+350')

list=[]
for i in range(5):
    while len(list)!=6:
        a = rd.randint(1,50)
        if a not in list:
            list.append(a)

def show():
    label.config(text=list)
    #config uses for the change features of an item dynamically

def transparantize():
    form.wm_attributes('-alpha',0.3)
def untransparantize():
    form.wm_attributes('-alpha',0.9)
def maximumConvert():
    form.state('zoomed')
def minimumConvert():
    form.state('iconic')
label = tk.Label(form,fg='red',bg='green',font='Times 20 bold')
label.pack()
show = tk.Button(form,text='Show Me',fg='Black',bg='yellow',command=show)
show.pack()

transparent = tk.Button(form,text='Convert More Transparent',command=transparantize)
transparent.pack(side = tk.LEFT)
untransparent = tk.Button(form,text='Convert Less Transparent',command=untransparantize)
untransparent.pack(side = tk.LEFT)

maximumConvert = tk.Button(form,text='Convert Page To Maximum Size',fg='Black',bg='yellow',command=maximumConvert)
maximumConvert.pack(side = tk.LEFT)
minimumConvert = tk.Button(form,text='Convert Page To Minimum Size',fg='Black',bg='yellow',command=minimumConvert)
minimumConvert.pack(side = tk.LEFT)
show.pack()#if we pack an element second times it doesnt change anything as we see
form.mainloop()