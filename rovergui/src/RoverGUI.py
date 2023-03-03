#!/usr/bin/env python3
#UNAM Space, RoverGUI
#Version 1.6

#Si PIL da error: sudo apt-get install python3-pil python3-pil.imagetk en Ubuntu
from cProfile import label
from pprint import pp
from PIL import ImageTk, Image, ImageShow
from click import command
#from std_msgs.msg import String
import PIL.Image
from tkinter import *
import tkinter 
#import rospy
import time 

import math as m
from geopy.geocoders import Nominatim
import time
#Dibujar mapas
from mpl_toolkits.basemap.test import Basemap
import matplotlib.pyplot as plt


#ROS functions
#DEPRECATED
""""
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
"""
"""
def callback(data):
    frameWdth, frameHght =  FrameControl()

    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    dataStr = "I heard " + str(data.data)
        
    listenerLabel = Label(mainWindow, text = dataStr)
    listenerLabel.config(font = ('Helvetica bold', 15))
    listenerLabel.place(x = frameWdth[0] + frameWdth[1] / 4, y = frameWdth[0] + frameHght[0] / 4)
"""
"""
def listener(): #(!)
    listenerButton = SetButtons()
    listenerButton.config(state = DISABLED)
    print("HEy")
    rospy.init_node('listener', anonymous = True)
    rospy.Subscriber("chatter", String, callback)
"""
#ROS lines
#roscore
#rosrun "talker_node"


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


def creatre_table(total_rows,total_columns, values,root):
    """
    values[0] latitud
    values[1] longitud
    values[2] altitud
    values[3] angulo
    """
    frameWdth, frameHght = FrameControl()
    screen_widht=root.winfo_screenwidth()
    frameWdth, frameHght = FrameControl() 


    
    for i in range(total_rows):
        for j in range(total_columns):
            tabla_datos_superior = Entry(root, width=int ((screen_widht/25)/total_columns), fg='white', background='#181E36',font=('Arial',13 ,'bold'),)
            tabla_datos_superior.grid(row=i, column=j, )
            tabla_datos_superior.insert(END, values[i])

    return tabla_datos_superior
    
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
    """"
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
    """

def SetImages():
    global UNAMSpaceLogo 
    global temporaRover
    frameWdth, frameHght = FrameControl()
    imageSize = 200

    logoSize = int(imageSize * scaleNumber)
    imgOffset = (frameWdth[0] - logoSize)/2

    UNAMSpaceLogo = ImageTk.PhotoImage(PIL.Image.open("Images/US-White.png").resize((logoSize,logoSize)))
    labelLogo = tkinter.Label(mainWindow, bg = "#181E36", image = UNAMSpaceLogo, width = logoSize , height = logoSize)
    labelLogo.place(x = imgOffset, y = imgOffset)


    temporalsize = logoSize+200
    temporaRover = ImageTk.PhotoImage(PIL.Image.open("Images/rover.jpg").resize((temporalsize+550,temporalsize+30)))
    labeltemporal = tkinter.Label(mainWindow, image = temporaRover, width = temporalsize+550 , height = temporalsize+30)
    labeltemporal.place(x = imgOffset+300, y = imgOffset+30)

"""
Cuando  se presiona el boton de activacion de listener
"""
def publish_reception_():
    i=0
    while True:
        values_serial=[i*2, i-2*i, i, i+1]
        print(values_serial)
        creatre_table(len(values_serial), 1, values_serial, mainWindow)
    #while True:
        #i+=1
        #values_serial=[i*2, i-2*i, i, i+1]
        #creatre_table(len(values_serial), 1,values_serial,  mainWindow)
 
    

def disconnect():
    frameWdth, frameHght = FrameControl()
    create_rectangle() 
    #dataStr="ROVER IS DISCONNECTED"
    #listenerLabel = Label(mainWindow, text = dataStr)
    #listenerLabel.config(font = ('Helvetica bold', 15))
    #listenerLabel.place(x = frameWdth[0] + frameWdth[1] / 4, y = frameWdth[0] + frameHght[0] / 4)

def connect():
    frameWdth, frameHght = FrameControl() 
    create_rectangle()
    dataStr="ROVER IS CONNECTED"
    listenerLabel = Label(mainWindow, text = dataStr)
    listenerLabel.config(font = ('Helvetica bold', 15))
    listenerLabel.place(x = frameWdth[0] + frameWdth[1] / 4, y = frameWdth[0] + frameHght[0] / 4)

    #disconnectButton = tkinter.Button(text = "Connect to ROVER", command = disconnect(listenerLabel))#Boton para activar el listener
   # = tkinter.Button(text = "Disconnect from Rover", command = SetButtons)#Boton para activar el listener

bandera_conexion=False
def create_rectangle():
    frameWdth, frameHght = FrameControl() 
    x=frameWdth[0] + frameWdth[1] / 4
    canvas = Canvas()
    if not bandera_conexion:
        canvas.create_rectangle(x,x,x+20,x+20,outline ="black",fill ="red",width = 2)
        bandera_conexion=True
    else:
        canvas.create_rectangle(10,10,110,110,outline ="black",fill ="green",width = 2)
        bandera_conexion=False

def SetButtons():
    frameWdth, framHght = FrameControl()
    #print("Esto va a pasar por aqui siempre")
    listenerButton = tkinter.Button(text = "Connect to ROVER", command = connect)#Boton para activar el listener
    listenerButton.place(x = frameWdth[0] + frameWdth[1] / 4, y = frameWdth[0] + frameWdth[1] / 4)
    disconnect_button=tkinter.Button(text ="Disconnect to Rover", command=disconnect)
    disconnect_button.place(x = (frameWdth[0] + frameWdth[1] / 4) +150, y = (frameWdth[0] + frameWdth[1] / 4))
    return listenerButton, disconnect_button

def update_table(table, values):
    dataStr="Connected"
    #listenerLabel = Label(mainWindow, text = dataStr)
    #listenerLabel.config(font = ('Arial', 16), fg='white', background='#181E36')
    #listenerLabel.place(x = 5 , y = 5)
    data = ["Latitud: ", "Longitud: ", "Altitud: " ,"Angulo: "]
    
    frameWdth, frameHght = FrameControl()
    screen_widht= mainWindow.winfo_screenwidth()
    frameWdth, frameHght = FrameControl() 
    
    for i in range(4):
        table = Entry( mainWindow, width=int ((screen_widht/25)/4), fg='white', background='#181E36',font=('Arial',13 ,'bold'),)
        table.grid(row=0, column=i)
        table.insert(END, data[i]+str(values[i]))
    
def getting_communication(tabla,i):
    """
    Actualizamos la tabla de valores recibidos por el Rover
    Los params data solo serán auxiliares para algún otro caso.
    El serial de arduino deberá ser leído desde está función
    """
    x = m.radians(0.1) 
    altitud_cu=2280
    grado=-90.0000
    update_table(tabla,[19.341690+(0.5*i),-99.180362*m.cos (x),altitud_cu*m.sin(x), grado+m.cos(x)]) 
    print("Comunicando con el rover")
    #Mapa
    geolocator = Nominatim(user_agent="AppMap")

    location = geolocator.geocode("Copilco Ciudad de Mexico")
    print(location.address)

    #Dimensiónd de la figura
    plt.figure(figsize=(16,12))

    #Distribución lines costeras
    eq_map=Basemap(projection='robin',lon_0=019.341690,lat_0= -89.2123)

    #Dibujar lineas costeras y paises
    eq_map.drawcoastlines()
    eq_map.drawcountries()

    #Definir colores
    eq_map.fillcontinents(color="brown")
    eq_map.drawmapboundary(fill_color="aqua")

    #Situo el lugar en el mapa
    x,y = eq_map(location.longitude,location.latitude)
    eq_map.plot(x,y, "ro", markersize=17, alpha=0.8)

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
    empty_list=["Esperando"]*4
    tabla = creatre_table(1, 4,empty_list,  mainWindow)
    mainWindow.bind("<Key>", KeyboardControl)
    return tabla

batteryLevel = 100
scaleNumber = 1.3

print("Proceso iniciado")
mainWindow = tkinter.Tk()
tabla_datos_superior = SetUp()

i=0
#while True:



"""
#Latitud,Longitud
#19.341690, -99.180362

[]
getting_communication(tabla_datos_superior,variador)

"""
"""
RECIBO = GPS(Rover Position)[Latitud, Longitud, Altitud]
RECIBO = BRUJULA (angulo respecto al norte)

ENVIO = Movimiento (adelante, atras,  izquierda, derecha, detener) (control de velocidad izq, derecha)
""""""


"""
n=-1
while i>n:
    print("Comunicando con el rover")
    i+=1
    #update_table(tabla_datos_superior,[3.002+m.sqrt(m.pi*i),m.sqrt(7.002+i),5.002+i,(6.002+i)**i]) #Longitud
    getting_communication(tabla_datos_superior,i)
    time.sleep(2)
    mainWindow.update()

mainWindow.mainloop()
#*Nota para el manco* width == ancho, height == altura
