#!/usr/bin/env python3
import rospy

class ROSf():
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
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

        dataStr = "I heard " + str(data.data)
            
        listenerLabel = Label(mainWindow, text = dataStr)
        listenerLabel.config(font = ('Helvetica bold', 15))
        listenerLabel.place(x = frameWdth[0] + frameWdth[1] / 4, y = frameWdth[0] + frameHght[0] / 4)

        return data.data

    def listener():
        listenerButton = SetButtons()
        listenerButton.config(state = DISABLED)

        rospy.init_node('listener', anonymous = True)
        rospy.Subscriber("chatter", String, callback)

""" ROS lines
>> roscore
>> rosrun "talker_node"
>> ...
"""