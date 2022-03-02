import tkinter
import os
import subprocess
from tkinter import NW, filedialog

import haze_removal
from PIL import Image, ImageTk

def open_image():
    global img
    global img_name

    img_name = filedialog.askopenfilename(initialdir=".", title="Select Image", filetypes=(("images", "*.jpg"), ("images", "*.png"),("images", "*.jpeg")))
    print(img_name)

    img = ImageTk.PhotoImage(Image.open(img_name).resize((250, 250)))
    l1 = tkinter.Label(root, image=img)
    l1.grid(column=0,row=2, padx=50)

def call_haze():
    hr = haze_removal.HazeRemoval()
    hr.open_image(img_name)
    hr.get_dark_channel()
    hr.get_air_light()
    hr.get_transmission()
    hr.guided_filter()
    hr.recover()
    hr.show()

    msg = tkinter.Label(root, text="Dehazing complete! Image stored in dehazed folder.")
    msg.grid(column=0, row=4)
    

root = tkinter.Tk()
root.title = "Dehaze"

label = tkinter.Label(root, text="Enter image path:")
label.grid(column=0, row=0)

input = tkinter.Entry(root)
input.grid(column=0, row=1, padx=10, pady=10)

browse = tkinter.Button(root, text="Browse", command=open_image)
browse.grid(column=1, row=1)

submit = tkinter.Button(root, text="Submit", command=call_haze)
submit.grid(column=0, row=3)


root.mainloop()