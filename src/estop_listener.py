#!/usr/bin/env python

import rospy
from std_msgs.msg import Header
from autoware_msgs.msg import ControlCommand
from autoware_msgs.msg import ControlCommandStamped


def main():
    rospy.init_node('pure_pursuit')
    pub = rospy.Publisher('ctrl_raw', ControlCommandStamped, queue_size=10)
    rate = rospy.Rate(20)

    while not rospy.is_shutdown():
        control_command_msg = ControlCommand()
        control_command_msg.linear_velocity = 0
        control_command_msg.linear_acceleration = 0
        control_command_msg.steering_angle = 0

        control_command_stamped_msg = ControlCommandStamped()
        header_msg = Header()
        header_msg.stamp = rospy.Time.now()
        control_command_stamped_msg.header = header_msg
        control_command_stamped_msg.cmd = control_command_msg
        pub.publish(control_command_stamped_msg)
        rate.sleep()


if __name__ == "__main__":
    main()
