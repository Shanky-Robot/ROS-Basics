// #include "ros/ros.h"
// #include "ros_basics_tutorials/AddTwoInt.h"

// bool add(ros_basics_tutorials::RectangleAreaService::Request  &req,
//          ros_basics_tutorials::RectangleAreaService::Response &res)
// {
//   res.sum = req.a + req.b;
//   ROS_INFO("request: x= %ld , y= %ld", req.a, req.b);
//   ROS_INFO("sending back response: [%ld]", (long int)res.sum);
//   return true;
// }

// int main(int argc, char **argv)
// {
//     ros::init(argc, argv, "add_two_int_server");
//     ros::NodeHandle n;

//     ros::ServiceServer service = n.advertiseService("add_two_int", add);
//     ROS_INFO("Ready to add_two_int");
//     ros::spin();

//     return 0;

// }