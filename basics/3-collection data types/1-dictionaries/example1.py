

#Get the ip addresses when user click the button and save it into the dictionary
#And show them all in the table

#fot this we need

import tkinter as tkk
import socket

#These are two main module/library we need for

gui = tkk.Tk()
#We created a gui form for create an gui environment

listbox1 = tkk.Listbox(gui)
listbox1.pack()
#created a listbox and imported it into the gui

gui.title("Ip adresi alma uygulaması")
gui.geometry("500x600")
#We adjusted size of gui and title of gui

def get_ip_adresses():
    counter = 1
    hostname = socket.gethostname() 
    local_ip = socket.gethostbyname(hostname)
    listbox1.insert(counter , local_ip)
    counter += 1
    return local_ip
    #This function gets user local ip address using by their hostname and writes it into listbox 1 by 1 with the help of counter

button1 = tkk.Button(gui , fg= "blue" , bg = "green" , text = "İp adresini al", command = get_ip_adresses)
button1.pack()
#We created a button for activate the get_ip_adresses function



gui.mainloop()
#This always loops the gui so it doesnt close 


#How could we improve this program?
