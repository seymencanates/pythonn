
import tkinter as tk
import tensorflow as tf
print(tf.__version__)

form1 = tk.Tk()


form1.title('Entry Dersi')

form1.geometry('500x400+250+250')

entry = tk.Entry(form1,fg='black',bg='green')
entry.pack(side=tk.RIGHT)
entry2 = tk.Entry(form1,fg='red',bg='blue')
entry2.pack(side=tk.LEFT)
form1.mainloop()