#!/usr/bin/env python3
from cProfile import label
from pprint import pp
from PIL import ImageTk, Image, ImageShow
from click import command
from std_msgs.msg import String
import PIL.Image
from tkinter import *
import tkinter 
import rospy
#Modulos
import Window
import Gadgets
import Component
import KeyboardControl

#I cannot figure out how to make this code work inside a module (KeyboardControl.py)
def KeyboardControl(event): #Perhaps a lambda function
    key = event.keysym
    if(key == "W" or key == "w" or key == "Up"):
        Component.Text.Char(mainWindow, 1350, 700, "W")
    elif(key == "A" or key == "a" or key == "Left"):
        Component.Text.Char(mainWindow, 1350, 700, "A")
    elif(key == "S" or key == "s" or key == "Right"):
        Component.Text.Char(mainWindow, 1350, 700, "S")
    elif(key == "D" or key == "d" or key == "Down"): 
        Component.Text.Char(mainWindow, 1350, 700, "D")

scaleNumber = 1.2
percentage = 100

print("Proceso iniciado")
global mainWindow
mainWindow = tkinter.Tk()

mainWindow.title("Interfaz Grafica Rover V1.6")
mainWindow.configure(bg = '#2E3349')
frameWdth, frameHght = Window.Panel.FrameControl(scaleNumber)
mainWindow.geometry(str(int(frameWdth[3])) + "x" + str(int(frameHght[3])) + "+200+100")


Window.Panel.SetFrames(mainWindow, frameWdth, frameHght)
Window.Utilities.SetImage(mainWindow, frameWdth, frameHght, scaleNumber)
Gadgets.Animations.Battery(mainWindow, frameWdth, frameHght, scaleNumber, percentage) #(!)

Component.Btn.RosListener(mainWindow, 300, 300)



#(!) ROS needed
mainWindow.bind("<Key>", KeyboardControl) #Tracks the keyboard actions
mainWindow.mainloop()
print("Fin del proceso!")