import tkinter as tk



import DatabaseConnection as conn
import reading as read



root=tk.Tk()
a = tk.Label(root, text="Hello, world!")
a.pack()
root.mainloop()

def erasing():
    cursor , cxcn = conn.create_connection()    
    read.reading()
    chosenData = int(input('Please chose id number that given on the line for erase: '))
    query1 = 'DELETE FROM testAndEducationalPurpose WHERE ogr_no = ?'
    cursor.execute(query1,(chosenData))
    cxcn.commit()
    cursor.close()
    cxcn.close()






erasing()