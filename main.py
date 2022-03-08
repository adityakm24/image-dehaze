import tkinter
import os
import sys
import subprocess
import haze_removal
from tkinter import NW, filedialog, ttk
from PIL import Image, ImageTk

def open_image():
    global img
    global img_name

    img_name = filedialog.askopenfilename(initialdir=".", title="Select Image", filetypes=(("images", "*.jpg"), ("images", "*.bmp"),("images", "*.jpeg"), ("images", "*.jfif")))
    print(img_name)
    input.insert(0, img_name)

    l1 = tkinter.Label(root, text="Original Image:")
    l1.grid(column=0, row=2)

    img = ImageTk.PhotoImage(Image.open(img_name).resize((250, 250)))
    l2 = tkinter.Label(root, image=img)
    l2.grid(column=0,row=3)


def call_haze():
    global dehazed
    global progress_bar
    global l_percent
    # subprocess.call(f"python haze_removal.py {img_name}", shell=True)

    submit.destroy()
    progress_bar = ttk.Progressbar(root, orient="horizontal", length="300", mode="determinate", maximum=100)
    progress_bar.grid(column=0, row=4)

    msg = "Opening image"

    l_percent = tkinter.Label(root, text=update_progress_label)
    l_percent.grid(column=1, row=4)

    l_msg = tkinter.Label(root, textvariable=msg)
    l_msg.grid(column=0, row=5, columnspan=2)

    progress_bar.start()

    hr = haze_removal.HazeRemoval()
    hr.open_image(img_name)

    msg = "Calculating Dark Channel"
    hr.get_dark_channel()
    progress()

    msg = "Calculating air light"
    hr.get_air_light()
    progress()

    msg = "Calculating transmission"
    hr.get_transmission()
    progress()

    msg = "Undergoing guided filter"
    hr.guided_filter()
    progress()

    hr.recover()
    hr.show()
    msg = "Dehazing complete! Image stored in dehazed folder."
    progress_bar.stop()

    msg = tkinter.Label(root, text="Dehazing complete! Image stored in dehazed folder.")
    msg.grid(column=0, row=5, columnspan=2)

    l3 = tkinter.Label(root, text="Dehazed Image:")
    l3.grid(column=1, row=2)

    dehazed = ImageTk.PhotoImage(Image.open("img/dst.jpg").resize((250, 250)))
    l4 = tkinter.Label(root, image=dehazed)
    l4.grid(column=1, row=3, padx=10)

    retry = tkinter.Button(root, text="Retry", command=restart_program)
    retry.grid(column=0, row=6)

    quit = tkinter.Button(root, text="Quit", command=quit_program)
    quit.grid(column=1, row=6)

def restart_program():
    os.execl(sys.executable, sys.executable, *sys.argv)  

def quit_program():
    sys.exit()


def update_progress_label():
    return f"{progress_bar['value']}%"


def progress():
    if progress_bar['value'] < 100:
        progress_bar['value'] += 20
        l_percent['text'] = update_progress_label()
        progress_bar.update_idletasks()
        l_percent.update_idletasks()


def stop():
    progress_bar.stop()
    l_percent['text'] = update_progress_label()


root = tkinter.Tk()
root.title = "Dehaze"
root.update_idletasks()

label = tkinter.Label(root, text="Enter image path:")
label.grid(column=0, row=0)

input = tkinter.Entry(root, width=50)
input.grid(column=0, row=1, padx=10, pady=10)

browse = tkinter.Button(root, text="Browse", command=open_image)
browse.grid(column=1, row=1)

submit = tkinter.Button(root, text="Submit", command=call_haze)
submit.grid(column=0, row=4)


root.mainloop()