#!/usr/bin/env python3
from std_msgs.msg import String
import rospy
import Component

class Simple():
    def talker(): #Sends a message to the roscore
        pub = rospy.Publisher('chatter', String, queue_size = 10)
        rospy.init_node('talker', anonymous = True)
        rate = rospy.Rate(1) # 1 Hz frequency 
        
        i = 0
        while not rospy.is_shutdown():
            hello_str = "hello world " + str(i)
            i += 1
            rospy.loginfo(hello_str)
            pub.publish(hello_str)
            rate.sleep()

    def callback(data): #Retuns the data collected from a ROS node (!)
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
        dataStr = "I heard " + str(data.data)
        print("Hello:" + dataStr)
        return  str(data.data)#(!) I may need to create a single function to return data
        
    def listener(): #This node 'listens' to roscore nodes
        rospy.init_node('listener', anonymous = True)
        rospy.Subscriber("chatter", String, Simple.callback)
        print("I'm here")

""" ROS lines
>> roscore
>> rosrun ros_essentials_cpp talker_node
>> ...
"""