#!/usr/bin/env python

import sys
import rospy

from ros_basics_tutorials.srv import RectangleAreaService
from ros_basics_tutorials.srv import RectangleAreaServiceRequest
from ros_basics_tutorials.srv import RectangleAreaServiceResponse

def rectangle_area_service_client(h, w):
    rospy.wait_for_service('rectangle_area_service')
    try:
        rectangle_area_service = rospy.ServiceProxy('rectangle_area_service', RectangleAreaService)
        respl = rectangle_area_service(h, w)
        return respl.area

    except rospy.ServiceException(e):
        print("Service call failed: %s"%e)
    
def usage():
    return

if __name__ == "__main__":
        if len(sys.argv) == 3:
            h = float(sys.argv[1])
            w = float(sys.argv[2])

        else:
            print ("%s [h w]"%sys.argv[0])
            sys.exit(1)
        print("Requesting %sx%s"%(h, w))
        area = rectangle_area_service_client(h, w)
        print("%s * %s = %s"%(h, w, area))
