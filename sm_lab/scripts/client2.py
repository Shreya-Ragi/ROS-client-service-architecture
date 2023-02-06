#!/usr/bin/env python3

import rospy
from rospy_tutorials.srv import AddTwoInts
if __name__ == '__main__':
    rospy.init_node("add_two_ints_client2")
    rospy.wait_for_service("/add_two_ints")
    try:
        add_two_ints = rospy.ServiceProxy("/add_two_ints", AddTwoInts)
        response = add_two_ints(23,46)
        rospy.loginfo("Sum is :" +str(response.sum))
    except rospy.ServiceException as e:
        rospy.logwarn("Service failed:" +str(e))