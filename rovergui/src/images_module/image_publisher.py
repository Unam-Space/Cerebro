#!/usr/bin/env python

"""
Librerias necesarias para trabajar con imagenes
"""

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

#Punte necesario para la comunicacion con ROS
bridge = CvBridge()


#Funcion de publicador
def talker():

    #Nodo con el nombre de "image_publisher" que publicara en el topico de "image_topic"
    publisher_node = rospy.Publisher('image_topic', Image, queue_size=1) 
    rospy.init_node('image_publisher', anonymous=False)
    rate = rospy.Rate(30)

    while not rospy.is_shutdown():

        #Se toma del teclado la imagen a mosrar
        image_file = input()
        print(image_file)
        #Lectura de la imagen
        image = cv2.imread(image_file)

        #Conveeersion de la imagen para la comunicacion con demas nodos
        msg = bridge.cv2_to_imgmsg(image, "bgr8")
        #Publicacion de la imagen
        publisher_node.publish(msg)


        

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass