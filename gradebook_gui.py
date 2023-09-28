import tkinter as tk
from tkinter import ttk
from tkinter import *

#Create a frame and add it to the root module
m = tk.Tk(); 
m.title ('Python GUI Gradebook')
m.geometry ('900x700')
menubar = Menu(m)
#Add the 2 frames to my window to display the calculation results.

def newWindow():
    m = tk.Tk(); 
    m.title ('New Window - Python GUI Gradebook')
    m.geometry ('600x600')

def closeWindow():
    m.destroy() 


def createMenu():
    file_menu = Menu(menubar, tearoff=0)
    file_menu.add_command(label= 'New Window' , command=newWindow)
    file_menu.add_command(label= 'Open File' , command=newWindow)
    file_menu.add_command(label= 'Save File' , command=newWindow)
    file_menu.add_command(label= 'Print' , command=newWindow)
    file_menu.add_separator()
    file_menu.add_command(label= 'Exit Program' , command=closeWindow)
    menubar.add_cascade(label="File", menu=file_menu)

createMenu()
m.config(menu=menubar)
m.mainloop()