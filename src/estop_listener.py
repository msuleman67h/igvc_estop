#!/usr/bin/env python

import subprocess

import rospy
from std_msgs.msg import Bool


def estop_btn_event(msg):
    global launched_pure_pursuit

    if msg.data:
        rospy.loginfo("Received E Stop Event from Arduino.")
        if not launched_pure_pursuit:
            rospy.loginfo("Launched pure_pursuit from igvc_estop.")
            subprocess.Popen(["roslaunch", "igvc_estop", "estop_pure_pursuit_node.launch"])
            launched_pure_pursuit = True


def main():
    estop_btn_topic = rospy.get_param("estop_topic_name")
    rospy.init_node('estop_listener', log_level=rospy.DEBUG)
    rospy.Subscriber(estop_btn_topic, Bool, callback=estop_btn_event)
    rospy.spin()


if __name__ == "__main__":
    launched_pure_pursuit = False
    main()
