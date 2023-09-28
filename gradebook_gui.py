import tkinter as tk
from tkinter import ttk

#Create a frame and add it to the root module
m = tk.Tk(); 
m.title ('Python GUI Gradebook')
m.geometry ('900x700')
#Add the 2 frames to my window to display the calculation results.
frame1= ttk.Frame(m, padding=" 5 5 5 5" )
frame2= ttk.Frame(m, padding=" 5 5 5 5" )

m.mainloop()