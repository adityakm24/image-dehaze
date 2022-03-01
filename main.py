import tkinter
import os
import subprocess


root = tkinter.Tk()

input = tkinter.Entry(root, text="Enter image path...")
input.grid(column=0, row=0)

browse = tkinter.Button(root, text="Browse")
browse.grid(column=1, row=0)

submit = tkinter.Button(root, text="Submit")
submit.grid(column=0, row=1)

test = tkinter.Button()
test.pack()

root.mainloop()