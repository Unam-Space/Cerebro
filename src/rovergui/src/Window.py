#!/usr/bin/env python3
from pickle import FRAME
from PIL import ImageTk, Image, ImageShow
import PIL.Image
from tkinter import *
import tkinter 

class Panel():
    def FrameControl(scaleNumber):
        #Creates arrays with the width and height value of the panels
        frameWdth = 230, 800, 200, 0    #x Size of frames
        frameHght = 475, 200, 0, 0      #y Size of frames
        arrSize = len(frameWdth) - 1

        frameWdth = [item * scaleNumber for item in frameWdth]  #Scales each value of the array 
        frameHght = [item * scaleNumber for item in frameHght]  #(To be compatible with different screen sizes)

        for i in range(arrSize):        #Set the main window dimension
            frameWdth[arrSize] += frameWdth[i] + 10
            frameHght[arrSize] += frameHght[i] + 10

        return frameWdth, frameHght

    def SetFrames(mainWindow, frameWdth, frameHght):
        frameQuantity = 5

        nFrame = [Frame] * (frameQuantity) #Set dimensions of each frame (!)
        nFrame[0] = Frame(mainWindow, width = frameWdth[0], height = frameWdth[3], bg = "#181E36", bd = 1, relief = FLAT)
        nFrame[1] = Frame(mainWindow, width = frameWdth[1], height = frameHght[0], bg = "#252A40", bd = 1, relief = FLAT)
        nFrame[2] = Frame(mainWindow, width = frameWdth[2], height = frameHght[0], bg = "#252A40", bd = 1, relief = FLAT)
        nFrame[3] = Frame(mainWindow, width = frameWdth[1], height = frameWdth[2], bg = "#252A40", bd = 1, relief = FLAT)
        nFrame[4] = Frame(mainWindow, width = frameWdth[2], height = frameHght[1], bg = "#252A40", bd = 1, relief = FLAT)
        
        nFrame[0].place(x = 0, y = 0) #Places frames 
        nFrame[1].place(x = frameWdth[0] + 10, y = 10) ; nFrame[2].place(x = frameWdth[0] + frameWdth[1] + 20, y = 10)
        nFrame[3].place(x = frameWdth[0] + 10, y = frameHght[0] + 20) ; nFrame[4].place(x = frameWdth[0] + frameWdth[1] + 20, y = frameHght[0] + 20)    

class Utilities():
    def SetImage(mainWindow, frameWdth, frameHght, scaleNumber):
        global UNAMSpaceLogo
        imageSize = 200

        logoSize = int(imageSize * scaleNumber)
        imgOffset = (frameWdth[0] - logoSize)/2 #Space used to center the logo in the first panel

        UNAMSpaceLogo = ImageTk.PhotoImage(PIL.Image.open("Images/US-White.png").resize((logoSize,logoSize)))
        labelLogo = tkinter.Label(mainWindow, bg = "#181E36", image = UNAMSpaceLogo, width = logoSize , height = logoSize)
        labelLogo.place(x = imgOffset, y = imgOffset)


#Width == ancho && Height == Altura

