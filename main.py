# pip install tkinter
# pip install pillow

import tkinter as tk
from tkinter import filedialog
from PIL import Image

root = tk.Tk()
root.title("Conversion PNG To JPG in Python")

canvas1 = tk.Canvas(root,width=300,height=280, bg='#006699',relief='sunken')
canvas1.pack()

label1 = tk.Label(root, text = 'Image File Conversion Tool',bd=7,bg='#006699',fg='#000066')
label1.config(font=('Helvetica',16,'bold'))
canvas1.create_window(150,40,window=label1)

def getPNG():
    global im1

    import_file_path= filedialog.askopenfilename()
    im1 = Image.open(import_file_path)

browseButton_PNG = tk.Button(text="Import PNG File",command = getPNG,bg='#6666ff',fg='white',bd=8,font=('Helvetica',18,'bold'))
canvas1.create_window(150,130,window=browseButton_PNG)


def convertToJPG():
    global im1
    export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg')
    im1.save(export_file_path)


saveAsButton_JPG = tk.Button(text='Convert PNG to JPG', command= convertToJPG,bg='#0066cc',bd=7,fg = 'white',font=('Helvetica',12,'bold'))
canvas1.create_window(150,190,window=saveAsButton_JPG)

root.mainloop()
