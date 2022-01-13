from CounterModule import *
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as font
import time
from PIL import Image, ImageTk

root = tk.Tk(className='Main MENU')
root.geometry("620x1000")
root.minsize(620,1000)
root.maxsize(620,1000)

image = Image.open("Image File Path")


introFrame = tk.Frame(root, bg= "#F3F5FC" )
introFrame.place(height=1000, width=630, x=0, y=0)

root.mainloop()
