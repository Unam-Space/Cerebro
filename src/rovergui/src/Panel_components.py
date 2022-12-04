#!/usr/bin/env python3
from tkinter import *
import tkinter
import ROS

def Char(mainWindow, xloc, yloc, char): 
    charLabel = Label(mainWindow, text = char)
    charLabel.config(font = ('Helvetica bold', 50))
    charLabel.place(x = xloc, y = yloc)

def Label_(mainWindow, xloc, yloc, text):
    textLabel = Label(mainWindow, text = text)
    textLabel.config(font = ('Helvetica bold', 15))
    textLabel.place(x = xloc, y = yloc)


class Button():
    #Definicion de laccion que debe tomar el boton
    def RosListener(mainWindow, xloc, yloc):
        listenerBtn = tkinter.Button(text = "Activar Listener", command = lambda : Action.Listen(mainWindow, xloc, yloc))
        listenerBtn.place(x = xloc, y = yloc)


#Clase separada por el uso de comandos lamda 
class Action():
    def Listen(mainWindow, xloc, yloc):
        data = ROS.ROS_node.listener()
        Label_(mainWindow, xloc + 200, yloc, data)
        print("Botón activado")
