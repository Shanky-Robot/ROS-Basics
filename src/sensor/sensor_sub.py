#!/usr/bin/env python
import rospy
from ros_basics_tutorials.msg import sensor

def sensor_callback(sensor_message):
    rospy.loginfo("New IoT data received: (%d, %s, %.2f, %.2f)", 
        sensor_message.id, sensor_message.name,
        sensor_message.temp, sensor_message.hum)

rospy.init_node('sensor_sub_node', anonymous= True)

rospy.Subscriber("sensor_topic", sensor, sensor_callback)

rospy.spin()

