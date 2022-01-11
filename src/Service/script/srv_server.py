#! /usr/bin/env python

import rospy
import time

from ros_basics_tutorials.srv import AddTwoInt
from ros_basics_tutorials.srv import AddTwoIntRequest
from ros_basics_tutorials.srv import AddTwoIntResponse

def handle_add_two_int(req):
    print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    time.sleep(5)
    sum_res = AddTwoIntResponse(req.a + req.b)
    return sum_res

def add_two_int_server():
    rospy.init_node('add_two_int_server')
    s = rospy.Service('add_two_int', AddTwoInt, handle_add_two_int)
    print("Ready to Add two int. ")
    rospy.spin()

if __name__=="__main__":
    add_two_int_server()
