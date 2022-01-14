from CounterModule import *
from tkinter import *
# from tkinter.ttk import *
# import tkinter.ttk as ttk
import tkinter as tk
import tkinter.font as font
import time
from PIL import Image, ImageTk

'''def imageFunction():
    img = (Image.open("C:\Programming\Aiwa\Assets\image 1.png"))
    img = img.resize((620,712), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    label = Label(introFrame, image = img)
    label.place(x=int(0), y=(0))'''

def lol():
    print("Hello")

root = tk.Tk(className='Main MENU')
root.geometry("620x1000")
root.minsize(620,1000)
root.maxsize(620,1000)

introFrame = tk.Frame(root, bg= "#F5F7FD" )
introFrame.place(height=1000, width=630, x=0, y=0)

homeFrame = tk.Frame(root, bg= "#F5F7FD" )
homeFrame.place(height=1000, width=630, x=1000, y=0)

workoutFrame = tk.Frame(root, bg= "#F5F7FD" )
workoutFrame.place(height=1000, width=630, x=1000, y=0)

difficultyFrame = tk.Frame(root, bg= "#F5F7FD" )
difficultyFrame.place(height=1000, width=630, x=1000, y=0)



def introFrameOpen():
    introFrame.place(x=0,y=0) 
    homeFrame.place(x=-630,y=0)
    workoutFrame.place(x=-630,y=0)
    difficultyFrame.place(x=-630,y=0)

def homeFrameOpen():
    homeFrame.place(x=0,y=0)
    introFrame.place(x=-630,y=0)
    workoutFrame.place(x=-630,y=0)
    difficultyFrame.place(x=-630,y=0)

def workoutFrameOpen():
    workoutFrame.place(x=0,y=0)
    homeFrame.place(x=-630,y=0)
    introFrame.place(x=-630,y=0)
    difficultyFrame.place(x=-630,y=0)

def difficultyFrameOpen():
    difficultyFrame.place(x=0,y=0)
    workoutFrame.place(x=-630,y=0)
    homeFrame.place(x=-630,y=0)
    introFrame.place(x=-630,y=0)


#######################################
# Sign in frame

landingImage = (Image.open("C:\Programming\Aiwa\Assets\image 1.png"))
landingImage = landingImage.resize((620,813), Image.ANTIALIAS)
landingImage = ImageTk.PhotoImage(landingImage)
label = Label(introFrame, image = landingImage)
label.place(x=int(0), y=(0))

signupImage = Image.open("C:\Programming\Aiwa\Assets\image 3.png")
signupImage = signupImage.resize((339,114), Image.ANTIALIAS)
signupImage = ImageTk.PhotoImage(signupImage)
startButton = Button(introFrame,image = signupImage ,bg='#F5F7FD',command = homeFrameOpen ,borderwidth = 0)
startButton.place(x=141.15, y=707)

startimage = Image.open("C:\Programming\Aiwa\Assets\image 4.png")
startimage = startimage.resize((339,114), Image.ANTIALIAS)
startimage = ImageTk.PhotoImage(startimage)
startButton = Button(introFrame,image = startimage ,bg='#F5F7FD',command = homeFrameOpen ,borderwidth = 0)
startButton.place(x=140 ,y=827)


################################################################################
#home Frame

topimage = (Image.open("C:\Programming\Aiwa\Assets\page1_1.png"))
topimage = topimage.resize((620,222), Image.ANTIALIAS)
topimage = ImageTk.PhotoImage(topimage)
label = Label(homeFrame, image = topimage,borderwidth = 0)
label.place(x=0, y=0)

buttonHome1 = Image.open("C:\Programming\Aiwa\Assets\page1_2.png")
buttonHome1 = buttonHome1.resize((525,191), Image.ANTIALIAS)
buttonHome1 = ImageTk.PhotoImage(buttonHome1)
startButton = Button(homeFrame,image = buttonHome1 ,command = workoutFrameOpen ,borderwidth = 0)
startButton.place(x=47 ,y=259)

buttonHome2 = Image.open("C:\Programming\Aiwa\Assets\page1_3.png")
buttonHome2 = buttonHome2.resize((525,191), Image.ANTIALIAS)
buttonHome2 = ImageTk.PhotoImage(buttonHome2)
startButton = Button(homeFrame,image = buttonHome2 ,command = workoutFrameOpen ,borderwidth = 0)
startButton.place(x=47 ,y=487)

buttonHome3 = Image.open("C:\Programming\Aiwa\Assets\page1_4.png")
buttonHome3 = buttonHome3.resize((525,191), Image.ANTIALIAS)
buttonHome3 = ImageTk.PhotoImage(buttonHome3)
startButton = Button(homeFrame,image = buttonHome3 ,command = workoutFrameOpen ,borderwidth = 0)
startButton.place(x=47 ,y=715)

################################################################################
#workout Frame

topimage1 = (Image.open("C:\Programming\Aiwa\Assets\page2_1.png"))
topimage1 = topimage1.resize((620,222), Image.ANTIALIAS)
topimage1 = ImageTk.PhotoImage(topimage1)
label = Label(workoutFrame, image = topimage,borderwidth = 0)
label.place(x=0, y=0)

buttonWorkout1 = Image.open("C:\Programming\Aiwa\Assets\page2_2.png")
buttonWorkout1 = buttonWorkout1.resize((525,191), Image.ANTIALIAS)
buttonWorkout1 = ImageTk.PhotoImage(buttonWorkout1)
startButton = Button(workoutFrame,image = buttonWorkout1 ,command = difficultyFrameOpen ,borderwidth = 0)
startButton.place(x=47 ,y=259)

buttonWorkout2 = Image.open("C:\Programming\Aiwa\Assets\page2_3.png")
buttonWorkout2 = buttonWorkout2.resize((525,191), Image.ANTIALIAS)
buttonWorkout2 = ImageTk.PhotoImage(buttonWorkout2)
startButton = Button(workoutFrame,image = buttonWorkout2 ,command = difficultyFrameOpen ,borderwidth = 0)
startButton.place(x=47 ,y=487)

buttonWorkout3 = Image.open("C:\Programming\Aiwa\Assets\page2_4.png")
buttonWorkout3 = buttonWorkout3.resize((525,191), Image.ANTIALIAS)
buttonWorkout3 = ImageTk.PhotoImage(buttonWorkout3)
startButton = Button(workoutFrame,image = buttonWorkout3 ,command = difficultyFrameOpen ,borderwidth = 0)
startButton.place(x=47 ,y=715)


################################################################################
#difficulty Frame

topimage2 = (Image.open("C:\Programming\Aiwa\Assets\page3_1.png"))
topimage2 = topimage2.resize((620,222), Image.ANTIALIAS)
topimage2 = ImageTk.PhotoImage(topimage2)
label = Label(difficultyFrame, image = topimage,borderwidth = 0)
label.place(x=0, y=0)

buttonDifficulty1 = Image.open("C:\Programming\Aiwa\Assets\page3_2.png")
buttonDifficulty1 = buttonDifficulty1.resize((525,191), Image.ANTIALIAS)
buttonDifficulty1 = ImageTk.PhotoImage(buttonDifficulty1)
startButton = Button(difficultyFrame,image = buttonDifficulty1 ,command = workoutFrameOpen ,borderwidth = 0)
startButton.place(x=47 ,y=259)

buttonDifficulty2 = Image.open("C:\Programming\Aiwa\Assets\page3_3.png")
buttonDifficulty2 = buttonDifficulty2.resize((525,191), Image.ANTIALIAS)
buttonDifficulty2 = ImageTk.PhotoImage(buttonDifficulty2)
startButton = Button(difficultyFrame,image = buttonDifficulty2 ,command = workoutFrameOpen ,borderwidth = 0)
startButton.place(x=47 ,y=487)

buttonDifficulty3 = Image.open("C:\Programming\Aiwa\Assets\page3_4.png")
buttonDifficulty3 = buttonDifficulty3.resize((525,191), Image.ANTIALIAS)
buttonDifficulty3 = ImageTk.PhotoImage(buttonDifficulty3)
startButton = Button(difficultyFrame,image = buttonDifficulty3 ,command = workoutFrameOpen ,borderwidth = 0)
startButton.place(x=47 ,y=715)


root.mainloop()