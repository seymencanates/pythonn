

import tkinter as tk
import DatabaseConnection as dbconnection
mainForm = tk.Tk()

listbox = tk.Listbox(mainForm)
listbox.pack()
mainForm.geometry('1000x1000')

connection , cursor = dbconnection.create_connection()

squery = 'SELECT * FROM testAndEducationalPurpose'
cursor.execute(squery)

oneRow = cursor.fetchone()
 
while oneRow:
    for item in oneRow:
        listbox.insert(tk.END, item)
    oneRow = cursor.fetchone()


mainForm.mainloop()