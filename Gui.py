from Tkinter import *
import Tkinter
import tkMessageBox
import os

import time
body = Tkinter.Tk()
body.configure(background='blue')
def BRAKE():
    os.system('python stop.py') 
B1= Tkinter.Button(text="BRAKES",command=BRAKE,fg="white",bg="black")
B1.pack(side=TOP)

def FRONT():
    os.system('python rightfront.py') 
    os.system('python leftfront.py') 
B2= Tkinter.Button(text="GO FRONT",command=FRONT,fg="green",bg="red")
B2.pack(side=BOTTOM)

def BACK():
    os.system('python rightback.py') 
    os.system('python leftback.py') 

B3= Tkinter.Button(text="GO BACK",command=BACK,fg="purple",bg="yellow")
B3.pack(side=BOTTOM)

def LEFT():
    os.system('python stop.py') 
    os.system('python rightfront.py') 
B4= Tkinter.Button(text="RIGHT",command=LEFT,fg="pink",bg="brown")
B4.pack(side='left')

def RIGHT():
    os.system('python stop.py') 

    os.system('python leftfront.py') 
B5= Tkinter.Button(text="LEFT",command=RIGHT,fg="black",bg="white")
B5.pack(side='right')

def UTURN():
    os.system('python stop.py') 
    os.system('python leftfront.py')
    os.system('python rightback.py') 
B6= Tkinter.Button(text="U-TURN",command=UTURN,fg="violet",bg="brown")
B6.pack()

def SMART():
    os.system('python 1.py')
    time.sleep(1)
    os.system('python stop.py')
     
B7= Tkinter.Button(text="SMART",command=SMART,fg="lawngreen",bg="grey")
B7.pack()
body.mainloop()