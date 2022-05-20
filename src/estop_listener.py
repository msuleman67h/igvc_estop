#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool


def estop_btn_event(msg):
    global launched_pure_pursuit

    if msg.data:
        rospy.loginfo("Received E Stop Event from Arduino.")
        pure_pursuit_flag_publisher.publish(False)
    else:
        pure_pursuit_flag_publisher.publish(True)


def main():
    estop_btn_topic = rospy.get_param("estop_topic_name")
    rospy.init_node('estop_listener', log_level=rospy.DEBUG)
    rospy.Subscriber(estop_btn_topic, Bool, callback=estop_btn_event)
    rospy.spin()


if __name__ == "__main__":
    launched_pure_pursuit = False
    pure_pursuit_flag_publisher = rospy.Publisher('purepursuit/stop', Bool, queue_size=10)
    main()
