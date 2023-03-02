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


#Funcion a ejecutar por cada mensaje de ROS 
def callback(msg):
    try:
        #Conversion de mensje de ROS a Cv2 para la visualizacion
        image = bridge.imgmsg_to_cv2(msg, "bgr8")
        
    except CvBridgeError:
        print("Error")
    
    #Se muestra la imagen que se envio
    cv2.imshow("Sent_image", image)
    cv2.waitKey(0)



#Nodo suscriptor de nombre "image_suscriber" que escuchara el topico de "image_topic"
def listener():

    #Funciones para el inicio del nodo en ROS
    rospy.init_node('image_suscriber')
    rospy.Subscriber('image_topic', Image, callback)

    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass