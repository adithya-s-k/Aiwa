from CounterModule import *
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.font as font
import time
from PIL import Image, ImageTk
from game import*
from threading import Thread

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

takeRestFrame1 = tk.Frame(root, bg= "#F5F7FD" )
takeRestFrame1.place(height=1000, width=630, x=0, y=1500)

takeRestFrame2 = tk.Frame(root, bg= "#F5F7FD" )
takeRestFrame2.place(height=1000, width=630, x=0, y=1500)

takeRestFrame3 = tk.Frame(root, bg= "#F5F7FD" )
takeRestFrame3.place(height=1000, width=630, x=0, y=1500)

takeRestFrame4 = tk.Frame(root, bg= "#F5F7FD" )
takeRestFrame4.place(height=1000, width=630, x=0, y=1500)

takeRestFrame5 = tk.Frame(root, bg= "#F5F7FD" )
takeRestFrame5.place(height=1000, width=630, x=0, y=1500)

def takerest5():
    introFrame.place(x=-630,y=0) 
    homeFrame.place(x=-630,y=0)
    workoutFrame.place(x=-630,y=0)
    difficultyFrame.place(x=-630,y=0)

    # takeRestFrame1.place(x=0,y=0)
    # takeRestFrame2.place(x=0,y=0)
    # takeRestFrame3.place(x=0,y=0)
    # takeRestFrame4.place(x=0,y=0)
    # takeRestFrame5.place(x=0,y=0)
    # root.after(1000,takeRestFrame5.place(x=0,y=1500))
    # root.after(1000,takeRestFrame4.place(x=0,y=1500))
    # root.after(1000,takeRestFrame3.place(x=0,y=1500))
    # root.after(1000,takeRestFrame2.place(x=0,y=1500))
    # # root.after(1000,takeRestFrame1.place(x=0,y=1500))

def second5():
    introFrame.place(x=-630,y=0) 
    homeFrame.place(x=-630,y=0)
    workoutFrame.place(x=-630,y=0)
    difficultyFrame.place(x=-630,y=0)
    takeRestFrame1.place(x=0,y=1500)
    takeRestFrame2.place(x=0,y=1500)
    takeRestFrame3.place(x=0,y=1500)
    takeRestFrame4.place(x=0,y=1500)
    takeRestFrame5.place(x=0,y=0)

def second4():
    introFrame.place(x=-630,y=0) 
    homeFrame.place(x=-630,y=0)
    workoutFrame.place(x=-630,y=0)
    difficultyFrame.place(x=-630,y=0)
    takeRestFrame1.place(x=0,y=1500)
    takeRestFrame2.place(x=0,y=1500)
    takeRestFrame3.place(x=0,y=1500)
    takeRestFrame4.place(x=0,y=0)
    takeRestFrame5.place(x=0,y=1500)

def second3():
    introFrame.place(x=-630,y=0) 
    homeFrame.place(x=-630,y=0)
    workoutFrame.place(x=-630,y=0)
    difficultyFrame.place(x=-630,y=0)
    takeRestFrame1.place(x=0,y=1500)
    takeRestFrame2.place(x=0,y=1500)
    takeRestFrame3.place(x=0,y=0)
    takeRestFrame4.place(x=0,y=1500)
    takeRestFrame5.place(x=0,y=1500)

def second2():
    introFrame.place(x=-630,y=0) 
    homeFrame.place(x=-630,y=0)
    workoutFrame.place(x=-630,y=0)
    difficultyFrame.place(x=-630,y=0)
    takeRestFrame1.place(x=0,y=1500)
    takeRestFrame2.place(x=0,y=0)
    takeRestFrame3.place(x=0,y=1500)
    takeRestFrame4.place(x=0,y=1500)
    takeRestFrame5.place(x=0,y=1500)

def second1():
    introFrame.place(x=-630,y=0) 
    homeFrame.place(x=-630,y=0)
    workoutFrame.place(x=-630,y=0)
    difficultyFrame.place(x=-630,y=0)
    takeRestFrame1.place(x=0,y=0)
    takeRestFrame2.place(x=0,y=1500)
    takeRestFrame3.place(x=0,y=1500)
    takeRestFrame4.place(x=0,y=1500)
    takeRestFrame5.place(x=0,y=1500)


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

def takerestFrameOpen():
    difficultyFrame.place(x=-630,y=0)
    workoutFrame.place(x=-630,y=0)
    homeFrame.place(x=-630,y=0)
    introFrame.place(x=-630,y=0)
    takeRestFrame1.place(x=0,y=0)

def easy():
    entry1 = 3
    difficulty = entry1
    homeFrameOpen()
    running_counter(difficulty)
    take_rest()
    toeTouch_counter(difficulty)
    take_rest()
    jump_counter(5)
    take_rest()
    crunches_counter(difficulty)
    homeFrameOpen()

def moderate():
    entry1 = 3
    difficulty = entry1  
    curl_counter(difficulty)
    take_rest()
    squat_counter(difficulty)
    take_rest()
    tricep_counter(difficulty)
    take_rest()
    homeFrameOpen()

def hard():
    entry1 = 15
    difficulty = entry1  
    curl_counter(difficulty)
    running_counter(difficulty)
    squat_counter(difficulty)
    push_up_counter(difficulty)
    homeFrameOpen()

def posture_detector_callback():
    posture_detector_advanced()
    homeFrameOpen()

def counter_time_callback():
    if __name__ == '__main__':
        Thread(target = Zenitsu_Run).start()
        Thread(target = game_detection).start()


#######################################
# Sign in frame

landingImage = (Image.open("Assets\image 1.png"))
landingImage = landingImage.resize((620,813), Image.ANTIALIAS)
landingImage = ImageTk.PhotoImage(landingImage)
label = Label(introFrame, image = landingImage)
label.place(x=int(0), y=(0))

signupImage = Image.open("Assets\image 3.png")
signupImage = signupImage.resize((339,114), Image.ANTIALIAS)
signupImage = ImageTk.PhotoImage(signupImage)
startButton = Button(introFrame,image = signupImage ,bg='#F5F7FD',command = homeFrameOpen ,borderwidth = 0)
startButton.place(x=141.15, y=707)

startimage = Image.open("Assets\image 4.png")
startimage = startimage.resize((339,114), Image.ANTIALIAS)
startimage = ImageTk.PhotoImage(startimage)
startButton = Button(introFrame,image = startimage ,bg='#F5F7FD',command = homeFrameOpen ,borderwidth = 0)
startButton.place(x=140 ,y=827)


################################################################################
#home Frame

topimage = (Image.open("Assets\page1_1.png"))
topimage = topimage.resize((620,222), Image.ANTIALIAS)
topimage = ImageTk.PhotoImage(topimage)
label = Label(homeFrame, image = topimage,borderwidth = 0)
label.place(x=0, y=0)

buttonHome1 = Image.open("Assets\page1_2.png")
buttonHome1 = buttonHome1.resize((525,191), Image.ANTIALIAS)
buttonHome1 = ImageTk.PhotoImage(buttonHome1)
startButton = Button(homeFrame,image = buttonHome1 ,command = workoutFrameOpen ,borderwidth = 0)
startButton.place(x=47 ,y=259)

buttonHome2 = Image.open("Assets\page1_3.png")
buttonHome2 = buttonHome2.resize((525,191), Image.ANTIALIAS)
buttonHome2 = ImageTk.PhotoImage(buttonHome2)
startButton = Button(homeFrame,image = buttonHome2 ,command = posture_detector_callback ,borderwidth = 0)
startButton.place(x=47 ,y=487)

buttonHome3 = Image.open("Assets\page1_4.png")
buttonHome3 = buttonHome3.resize((525,191), Image.ANTIALIAS)
buttonHome3 = ImageTk.PhotoImage(buttonHome3)
startButton = Button(homeFrame,image = buttonHome3 ,command = counter_time_callback ,borderwidth = 0)
startButton.place(x=47 ,y=715)

################################################################################
#workout Frame

topimage1 = (Image.open("Assets\page2_1.png"))
topimage1 = topimage1.resize((620,222), Image.ANTIALIAS)
topimage1 = ImageTk.PhotoImage(topimage1)
label = Label(workoutFrame, image = topimage,borderwidth = 0)
label.place(x=0, y=0)

buttonWorkout1 = Image.open("Assets\page2_2.png")
buttonWorkout1 = buttonWorkout1.resize((525,191), Image.ANTIALIAS)
buttonWorkout1 = ImageTk.PhotoImage(buttonWorkout1)
startButton = Button(workoutFrame,image = buttonWorkout1 ,command = difficultyFrameOpen ,borderwidth = 0)
startButton.place(x=47 ,y=259)

buttonWorkout2 = Image.open("Assets\page2_3.png")
buttonWorkout2 = buttonWorkout2.resize((525,191), Image.ANTIALIAS)
buttonWorkout2 = ImageTk.PhotoImage(buttonWorkout2)
startButton = Button(workoutFrame,image = buttonWorkout2 ,command = difficultyFrameOpen ,borderwidth = 0)
startButton.place(x=47 ,y=487)

buttonWorkout3 = Image.open("Assets\page2_4.png")
buttonWorkout3 = buttonWorkout3.resize((525,191), Image.ANTIALIAS)
buttonWorkout3 = ImageTk.PhotoImage(buttonWorkout3)
startButton = Button(workoutFrame,image = buttonWorkout3 ,command = difficultyFrameOpen ,borderwidth = 0)
startButton.place(x=47 ,y=715)


################################################################################
#difficulty Frame

topimage2 = (Image.open("Assets\page3_1.png"))
topimage2 = topimage2.resize((620,222), Image.ANTIALIAS)
topimage2 = ImageTk.PhotoImage(topimage2)
label = Label(difficultyFrame, image = topimage,borderwidth = 0)
label.place(x=0, y=0)

buttonDifficulty1 = Image.open("Assets\page3_2.png")
buttonDifficulty1 = buttonDifficulty1.resize((525,191), Image.ANTIALIAS)
buttonDifficulty1 = ImageTk.PhotoImage(buttonDifficulty1)
startButton = Button(difficultyFrame,image = buttonDifficulty1 ,command = easy ,borderwidth = 0)
startButton.place(x=47 ,y=259)

buttonDifficulty2 = Image.open("Assets\page3_3.png")
buttonDifficulty2 = buttonDifficulty2.resize((525,191), Image.ANTIALIAS)
buttonDifficulty2 = ImageTk.PhotoImage(buttonDifficulty2)
startButton = Button(difficultyFrame,image = buttonDifficulty2 ,command = moderate ,borderwidth = 0)
startButton.place(x=47 ,y=487)

buttonDifficulty3 = Image.open("Assets\page3_4.png")
buttonDifficulty3 = buttonDifficulty3.resize((525,191), Image.ANTIALIAS)
buttonDifficulty3 = ImageTk.PhotoImage(buttonDifficulty3)
startButton = Button(difficultyFrame,image = buttonDifficulty3 ,command = hard ,borderwidth = 0)
startButton.place(x=47 ,y=715)

################################################################
#Take rest frame

takeRestimage1 = (Image.open("Assets\image 29.png"))
takeRestimage1 = takeRestimage1.resize((620,1000), Image.ANTIALIAS)
takeRestimage1 = ImageTk.PhotoImage(takeRestimage1)
label1 = Label(takeRestFrame1, image = takeRestimage1 , borderwidth = 0)
label1.place(x=0, y=0)

takeRestimage2 = (Image.open("Assets\image 28.png"))
takeRestimage2 = takeRestimage2.resize((620,1000), Image.ANTIALIAS)
takeRestimage2 = ImageTk.PhotoImage(takeRestimage2)
label2 = Label(takeRestFrame2, image = takeRestimage2 , borderwidth = 0)
label2.place(x=0, y=0)

takeRestimage3 = (Image.open("Assets\image 27.png"))
takeRestimage3 = takeRestimage3.resize((620,1000), Image.ANTIALIAS)
takeRestimage3 = ImageTk.PhotoImage(takeRestimage3)
label3 = Label(takeRestFrame3, image = takeRestimage3 , borderwidth = 0)
label3.place(x=0, y=0)

takeRestimage4 = (Image.open("Assets\image 26.png"))
takeRestimage4 = takeRestimage4.resize((620,1000), Image.ANTIALIAS)
takeRestimage4 = ImageTk.PhotoImage(takeRestimage4)
label4 = Label(takeRestFrame4, image = takeRestimage4 , borderwidth = 0)
label4.place(x=0, y=0)

takeRestimage5 = (Image.open("Assets\image 25.png"))
takeRestimage5 = takeRestimage5.resize((620,1000), Image.ANTIALIAS)
takeRestimage5 = ImageTk.PhotoImage(takeRestimage5)
label5 = Label(takeRestFrame5, image = takeRestimage5 , borderwidth = 0)
label5.place(x=0, y=0)

root.mainloop()