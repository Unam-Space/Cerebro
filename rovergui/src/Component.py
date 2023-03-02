#!/usr/bin/env python3
from tkinter import *
import tkinter
import ROS

class Text():
    def Char(mainWindow, xloc, yloc, char): 
        charLabel = Label(mainWindow, text = char)
        charLabel.config(font = ('Helvetica bold', 50))
        charLabel.place(x = xloc, y = yloc)

    def Lbl(mainWindow, xloc, yloc, text):
        textLabel = Label(mainWindow, text = text)
        textLabel.config(font = ('Helvetica bold', 15))
        textLabel.place(x = xloc, y = yloc)

class Btn():
    def RosListener(mainWindow, xloc, yloc):
        listenerBtn = tkinter.Button(text = "Activar Listener", command = lambda : Action.Listen(mainWindow, xloc, yloc))
        listenerBtn.place(x = xloc, y = yloc)

class Action():
    def Listen(mainWindow, xloc, yloc):
        data = ROS.Simple.listener()
        Text.Lbl(mainWindow, xloc + 200, yloc, data)
        print("Botón activado")
