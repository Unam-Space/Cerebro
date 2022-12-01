#!/usr/bin/env python3
#UNAM Space, RoverGUI
#Version 1.6

#Si PIL da error: sudo apt-get install python3-pil python3-pil.imagetk en Ubuntu
from cProfile import label
from pprint import pp
from PIL import ImageTk, Image, ImageShow
from click import command
from std_msgs.msg import String
import PIL.Image
from tkinter import *
import tkinter 
import rospy

#ROS functions
def talker():
    pub = rospy.Publisher('chatter', String, queue_size = 10)
    rospy.init_node('talker', anonymous = True)
    rate = rospy.Rate(1) # 1 Hz
    
    i = 0
    while not rospy.is_shutdown():
        hello_str = "hello world " + str(i)
        i += 1
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

def callback(data):
    frameWdth, frameHght =  FrameControl()

    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    dataStr = "I heard " + str(data.data)
        
    listenerLabel = Label(mainWindow, text = dataStr)
    listenerLabel.config(font = ('Helvetica bold', 15))
    listenerLabel.place(x = frameWdth[0] + frameWdth[1] / 4, y = frameWdth[0] + frameHght[0] / 4)

def listener(): #(!)
    listenerButton = SetButtons()
    listenerButton.config(state = DISABLED)
    print("HEy")
    rospy.init_node('listener', anonymous = True)
    rospy.Subscriber("chatter", String, callback)
"""
ROS lines
roscore
rosrun "talker_node"

"""
#End of ROS functions


def FrameControl():
    frameWdth = 230, 800, 200, 0    #x Size of frames
    frameHght = 475, 200, 0, 0      #y Size of frames
    arrSize = len(frameWdth) - 1

    frameWdth = [item * scaleNumber for item in frameWdth]  #Multiply each value of the array 
    frameHght = [item * scaleNumber for item in frameHght]    

    for i in range(arrSize):        #Set the main window dimension
        frameWdth[arrSize] += frameWdth[i] + 10
        frameHght[arrSize] += frameHght[i] + 10

    return frameWdth, frameHght

def SetFrames():
    frameWdth, frameHght = FrameControl()
    frameQuantity = 5

    nFrame = [Frame] * (frameQuantity) #Set dimensions of each frame
    nFrame[0] = Frame(mainWindow, width = frameWdth[0], height = frameWdth[3], bg = "#181E36", bd = 1, relief = FLAT)
    nFrame[1] = Frame(mainWindow, width = frameWdth[1], height = frameHght[0], bg = "#252A40", bd = 1, relief = FLAT)
    nFrame[2] = Frame(mainWindow, width = frameHght[1], height = frameHght[0], bg = "#252A40", bd = 1, relief = FLAT)
    nFrame[3] = Frame(mainWindow, width = frameWdth[1], height = frameWdth[2], bg = "#252A40", bd = 1, relief = FLAT)
    nFrame[4] = Frame(mainWindow, width = frameHght[1], height = frameHght[1], bg = "#252A40", bd = 1, relief = FLAT)
    
    nFrame[0].place(x = 0, y = 0) #Places frames 
    nFrame[1].place(x = frameWdth[0] + 10, y = 10) ; nFrame[2].place(x = frameWdth[0] + frameWdth[1] + 20, y = 10)
    nFrame[3].place(x = frameWdth[0] + 10, y = frameHght[0] + 20) ; nFrame[4].place(x = frameWdth[0] + frameWdth[1] + 20, y = frameHght[0] + 20)    

def KeyboardControl(event):
    global batteryLevel
    key = event.keysym
    if(key == "W" or key == "w" or key == "Up"):
        SetChar("W")
    elif(key == "A" or key == "a" or key == "Left"):
        SetChar("A")
    elif(key == "S" or key == "s" or key == "Right"):
        SetChar("S")
    elif(key == "D" or key == "d" or key == "Down"): 
        SetChar("D")
    elif(key == "O" or key == "o"):
        batteryLevel -= 10
        if(batteryLevel < 0):
            batteryLevel = 0
            return
        Battery(batteryLevel)
    elif(key == "P" or key == "p"):
        batteryLevel += 10
        if(batteryLevel > 100):
            batteryLevel = 100
            return
        Battery(batteryLevel)
    elif(key == "I" or key == "i"):
        widthValue = mainWindow.winfo_screenwidth()
        print("Screen width: " + str(widthValue))

        widthApp = mainWindow.winfo_width()
        print("App width: " + str(widthApp))

        print("Dimensiones ventana:")
        print(mainWindow.winfo_geometry())

def SetChar(char):
    frameWdth, frameHght = FrameControl()

    testLabel = Label(mainWindow, text = char)
    testLabel.config(font = ('Helvetica bold', 50))
    testLabel.place(x = frameWdth[3] - (2.7 * frameWdth[2]/4), y = frameHght[3] - (2.7 * frameHght[1]/4))

def Battery(percentage):
    frameWdth, frameHght = FrameControl()

    bSize = 125, 42 ; tipSize = 62.5, 25
    cellQuantity = 6

    bSize = [item * scaleNumber for item in bSize]
    tipSize = [item * scaleNumber for item in tipSize]

    xloc = 20 + frameWdth[0] + frameWdth[1] + ((frameWdth[2] - bSize[0])/2)
    yloc = 50

    cell = [Frame] * cellQuantity

    for i in range(cellQuantity):
        if(i == 0): 
            cell[i] = Frame(mainWindow, width = tipSize[0], height = tipSize[1], bg = 'lime', bd = 2, relief = GROOVE)
            cell[i].place(x = xloc + bSize[0]/4, y = yloc + (bSize[1] - tipSize[1]))
        else:
            cell[i] = Frame(mainWindow, width = bSize[0], height = bSize[1], bg = 'lime', bd = 2, relief = GROOVE)
            cell[i].place(x = xloc, y = yloc + i * bSize[1])

    def batteryLoop(lvl):
        for i in range(lvl):
                cell[i].config(bg = '#252A40')
        if(lvl == 5):
            cell[lvl].config(bg = "red")

    print("BatteryLevel is: " + str(percentage) + "%")

    if(percentage >= 90): 
        batteryLoop(0)
    elif(75 <= percentage < 90):
        batteryLoop(1)
    elif(60 <= percentage < 75):
        batteryLoop(2)
    elif(40 <= percentage < 60):
        batteryLoop(3)
    elif(20 <= percentage < 40):
        batteryLoop(4)
    elif(5 < percentage < 20):
        batteryLoop(5)
    else:
        print("Battery is empty!")
        batteryLoop(6)

def SetImages():
    global UNAMSpaceLogo 
    frameWdth, frameHght = FrameControl()
    imageSize = 200

    logoSize = int(imageSize * scaleNumber)
    imgOffset = (frameWdth[0] - logoSize)/2

    UNAMSpaceLogo = ImageTk.PhotoImage(PIL.Image.open("Images/US-White.png").resize((logoSize,logoSize)))
    labelLogo = tkinter.Label(mainWindow, bg = "#181E36", image = UNAMSpaceLogo, width = logoSize , height = logoSize)
    labelLogo.place(x = imgOffset, y = imgOffset)

def SetButtons():
    frameWdth, framHght = FrameControl()
    print("Esto va a pasar por aqui siempre")
    listenerButton = tkinter.Button(text = "Activar Listener", command = listener)
    listenerButton.place(x = frameWdth[0] + frameWdth[1] / 4, y = frameWdth[0] + frameWdth[1] / 4)

    return listenerButton

def SetUp():
    mainWindow.title("Interfaz Grafica Rover V 1.5")
    mainWindow.configure(bg = '#2E3349')
    frameWdth, frameHght = FrameControl()
    mainWindow.geometry(str(int(frameWdth[3])) + "x" + str(int(frameHght[3])) + "+0+0")
    #mainWindow.iconbitmap('Images\RocketIcon.ico')

    SetFrames()
    SetButtons()
    SetImages()
    Battery(batteryLevel)

    mainWindow.bind("<Key>", KeyboardControl)
    mainWindow.mainloop()

batteryLevel = 100
scaleNumber = 1.3

print("Proceso iniciado")
mainWindow = tkinter.Tk()
SetUp()
print("Fin del proceso!")

#*Nota para el manco* width == ancho, height == altura
