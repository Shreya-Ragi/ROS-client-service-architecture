#!/usr/bin/env python3

import rospy

from sm_lab.srv import concatStr
if __name__ == '__main__':
    rospy.init_node("concat_str_client")
    rospy.wait_for_service("/concat_str")
    try:
        concat_str = rospy.ServiceProxy("/concat_str", concatStr)
        response = concat_str("Shreya","Ragi")
        rospy.loginfo("String is :" +str(response))
    except rospy.ServiceException as e:
        rospy.logwarn("Service failed:" +str(e))