#!/usr/bin/env python
import rospy
from ros_basics_tutorials.msg import sensor
import random

pub = rospy.Publisher('sensor_topic', sensor, queue_size=10)

rospy.init_node('sensor_pub_node', anonymous= True)

rate = rospy.Rate(1)

i=0
while not rospy.is_shutdown():
    iot_sensor = sensor()
    iot_sensor.id = 1
    iot_sensor.name="iot_parking"
    iot_sensor.temp=24.33+(random.random()*2)
    iot_sensor.hum=33.41+(random.random()*2)
    rospy.loginfo("I Publish: ")
    rospy.loginfo(iot_sensor)
    pub.publish(iot_sensor)
    rate.sleep()
    i=i+1

if __name__ == '__main__':
    try:
        sensor()
    except rospy.ROSInterruptException:
        pass