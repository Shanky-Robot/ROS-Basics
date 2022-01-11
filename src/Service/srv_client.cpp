#include "ros/ros.h"
#include "ros_basics_tutorials/AddTwoInt.h"
#include <cstdlib>

int main(int argc, char **argv)
{
   ros::init(argc, argv, "add_two_int_client");
   if (argc !=3)
   {
       ROS_INFO("Usage: add_two_int_client X Y");
       return 1;
   }

   ros::NodeHandle n;
   ros::ServiceClient client = n.serviceClient<ros_basics_tutorials::AddTwoInt>("add_two_int");
   ros_basics_tutorials::AddTwoInt srv;
   srv.request.a = atoll(argv[1]);
   srv.request.b = atoll(argv[2]);
   if (client.call(srv))
   {
       ROS_INFO("Sum: %ld",(long int)srv.response.sum);
   }
   else
   {
       ROS_ERROR("Failed to call service add_two_ints");
       return 1;
   }

    return 0;
}
