#!/usr/bin/env python


"""
Librerias necesarias para trabajar con imagenes
"""
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

#Se toma la camara por defecto para la captura de imagenes
camera_image = cv2.VideoCapture(2)
#Puente para la conexion con ROS
bridge = CvBridge()

#Parametros de la camara
camera_image.set(cv2.CAP_PROP_FRAME_WIDTH, 3000)
camera_image.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)
camera_image.set(cv2.CAP_PROP_FPS, 30)


#Funcion de publicador
def talker():

    #Nodo con el nombre de "camera_publisher" que publicara en el topico de "camera"
    publisher_node = rospy.Publisher('camera', Image, queue_size=1) 
    rospy.init_node('camera_publisher', anonymous=False)
    rate = rospy.Rate(30)

    while not rospy.is_shutdown():

        #Boolean es una bandera que indica si se pudo tomar el frame
        #Frame es la imagen en si
        boolean, frame = camera_image.read()    

        if not boolean:
            break

        #Conversion de la imagen para la comunicacion con demas nodos
        #Publicacion de la imagen
        msg = bridge.cv2_to_imgmsg(frame, "bgr8")
        publisher_node.publish(msg)


        

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass