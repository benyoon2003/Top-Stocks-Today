#Import the required library
from tkinter import *

#Create an instance of tkinter frame or window
win = Tk()

#Define the geometry
win.geometry("750x400")

#Create a listbox
listbox= Listbox(win)
listbox.pack(side =LEFT, fill = BOTH)

#Create a Scrollbar
scrollbar = Scrollbar(win)
scrollbar.pack(side = RIGHT, fill = BOTH)

#Insert Values in listbox
for i in range(150):
   listbox.insert(END, 'Hey')

listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)
win.mainloop()