#!/usr/bin/env python

"""
Librerias necesarias para trabajar con imagenes
"""
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

#Puente necesario para la comunicacion entre ROS y OpenCV
bridge = CvBridge()




#Funcion a ejecutar por cada mensaje de ROS 
def callback(msg):
    try:
        #Conversion de mensje de ROS a Cv2 para la visualizacion
        camera_frame = bridge.imgmsg_to_cv2(msg, "bgr8")
        
    except CvBridgeError:
        print("Error")

    #Funciones para la visualizacion de frame por frame
    cv2.imshow("camera", camera_frame)
    cv2.waitKey(1)


    


#Nodo suscriptor de nombre "camera_suscriber" que escuchara el topico de "camera"
def listener():

    #Funciones para el inicio del nodo en ros
    rospy.init_node('camera_suscriber')
    rospy.Subscriber('camera', Image, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass