#!/usr/bin/env python

import rospy
from autoware_msgs.msg import ControlCommand
from autoware_msgs.msg import ControlCommandStamped
from geometry_msgs.msg import Twist
from geometry_msgs.msg import TwistStamped
from std_msgs.msg import Header


def main():
    rospy.init_node('pure_pursuit', log_level=rospy.DEBUG)
    rospy.loginfo("Initialized ROS Node pure_pursuit")

    # Ctrl raw topic
    ctrl_raw_publisher = rospy.Publisher('ctrl_raw', ControlCommandStamped, queue_size=10)
    rospy.loginfo("Publishing to topic ctrl_raw...")

    # Twist Raw topic
    twist_raw_publisher = rospy.Publisher('twist_raw', TwistStamped, queue_size=10)
    rospy.loginfo("Publishing to topic twist_raw...")
    rate = rospy.Rate(20)

    while not rospy.is_shutdown():
        header_msg = Header()
        header_msg.stamp = rospy.Time.now()

        control_command_msg = ControlCommand()
        control_command_msg.linear_velocity = 0
        control_command_msg.linear_acceleration = 0
        control_command_msg.steering_angle = 0

        control_command_stamped_msg = ControlCommandStamped()
        control_command_stamped_msg.header = header_msg
        control_command_stamped_msg.cmd = control_command_msg
        ctrl_raw_publisher.publish(control_command_stamped_msg)
        rospy.logdebug(control_command_stamped_msg, logger_name="ctrl_raw_msg")

        twist_msg = Twist()
        twist_msg.linear.x = 0.0
        twist_msg.linear.y = 0.0
        twist_msg.linear.z = 0.0
        twist_msg.angular.x = 0.0
        twist_msg.angular.y = 0.0
        twist_msg.angular.z = 0.0

        twist_stamped_msg = TwistStamped()
        twist_stamped_msg.twist = twist_msg
        twist_stamped_msg.header = header_msg
        twist_raw_publisher.publish(twist_stamped_msg)
        rospy.logdebug(twist_stamped_msg, logger_name="twist_raw_msg")
        rate.sleep()


if __name__ == "__main__":
    main()
