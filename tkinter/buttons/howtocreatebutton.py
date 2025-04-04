



import tkinter as tkn

form = tkn.Tk()
#we included a form element into the python file

form.title('Ders 5')
#adds a title for the form



form.geometry('500x400')



def topla():
    print('topla')

button = tkn.Button(form,text='Tıkla',
                    fg='black',
                    bg='red',
                    command=topla)
button.pack(side=tkn.LEFT)

#side has a few parameter
#first is left : aligns to the left
#second is right : aligns to the right

button2=tkn.Button(form,text='Tıkla2'
                   ,command=topla)

button2.pack(side=tkn.LEFT)

form.mainloop()