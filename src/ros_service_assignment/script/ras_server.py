#!/usr/bin/env python

import rospy
import time

from ros_basics_tutorials.srv import RectangleAreaService
from ros_basics_tutorials.srv import RectangleAreaServiceRequest
from ros_basics_tutorials.srv import RectangleAreaServiceResponse

def handle_rectangle_area(req):
    print("Returning [%s * %s = %s]"%(req.h, req.w, (req.h * req.w)))
    time.sleep(5)
    area_res = RectangleAreaServiceResponse(req.h * req.w)
    return area_res

def rectangle_area_service_server():
    rospy.init_node('rectangle_area_service_server')
    s = rospy.Service('rectangle_area_service', RectangleAreaService, handle_rectangle_area)
    print("Ready to calculate Area of Rectangle. ")
    rospy.spin()

if __name__=="__main__":
    rectangle_area_service_server()
