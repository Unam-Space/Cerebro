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
import Panel
import Animations
import Panel_components
import KeyboardControl as key


scaleNumber = 1.2
percentage = 100

print("Proceso iniciado")
global mainWindow 
mainWindow = tkinter.Tk()

mainWindow.title("Interfaz Grafica Rover V1.6")
mainWindow.configure(bg = '#2E3349')
frameWdth, frameHght = Panel.FrameControl(scaleNumber)
mainWindow.geometry(str(int(frameWdth[3])) + "x" + str(int(frameHght[3])) + "+200+100")


Panel.SetFrames(mainWindow, frameWdth, frameHght)
Panel.SetImage(mainWindow, frameWdth, frameHght, scaleNumber)
Animations.Battery(mainWindow, frameWdth, frameHght, scaleNumber, percentage) #(!)

Panel_components.Button.RosListener(mainWindow, 300, 300)



#(!) ROS needed

control = key.Actions(mainWindow)

mainWindow.bind("<Key>", control.KeyboardControl) #Tracks the keyboard actions
mainWindow.mainloop()
print("Fin del proceso!")