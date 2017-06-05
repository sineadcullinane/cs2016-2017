"""Import tkinter from python library
"""
from tkinter import *

"""Create a top level container
"""
root = Tk()

"""Configure layout of the interface
"""
root.configure(width = 300)
root.configure(height = 200)
root.configure(bg='lightgray')
root.minsize(width=300, height=200)

"""Assign labels to the interface
"""
label1 = Label(root, text="Hello", fg="blue")
label1.pack(side=TOP)

label2 = Label(root, text="Goodbye", fg="red")
label2.pack(side=BOTTOM)

"""Run the interface and handle events
"""
root.mainloop()
