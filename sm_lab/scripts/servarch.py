#!/usr/bin/env python3

import rospy

from sm_lab.srv import concatStr

def handle_concat_str(req):
    result = req.s1+req.s2
    rospy.loginfo("Concatenation of " +req.s1+ " and " +req.s2 + " is " + result)
    return result

if __name__ == '__main__':
    rospy.init_node("concat_str_server")
    rospy.loginfo("Concatenate server node created")
    service = rospy.Service("/concat_str", concatStr, handle_concat_str)
    rospy.loginfo("Service server has been started")
    rospy.spin()
