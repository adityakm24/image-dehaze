from ipaddress import collapse_addresses
import tkinter
import os
import subprocess
from tkinter import NW, filedialog

from numpy import pad
import haze_removal
from PIL import Image, ImageTk

def open_image():
    global img

    img_name = filedialog.askopenfilename(initialdir=".", title="Select Image", filetypes=(("images", "*.jpg"), ("images", "*.png"),("images", "*.jpeg")))
    print(img_name)

    img = ImageTk.PhotoImage(Image.open(img_name).resize((250, 250)))
    l1 = tkinter.Label(root, image=img)
    l1.grid(column=0,row=2, padx=50)

root = tkinter.Tk()
root.title = "Dehaze"

label = tkinter.Label(root, text="Enter image path:")
label.grid(column=0, row=0)

input = tkinter.Entry(root)
input.grid(column=0, row=1, padx=10, pady=10)

browse = tkinter.Button(root, text="Browse", command=open_image)
browse.grid(column=1, row=1)

submit = tkinter.Button(root, text="Submit")
submit.grid(column=0, row=3)


root.mainloop()