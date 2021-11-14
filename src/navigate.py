#!/usr/bin/env python

import rospy
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

SCAN_TOPIC="/scan"
MOVE_TOPIC="cmd_vel"


def call_back(msg)

    rospy.loginfo(msg.ranges)
    rospy.loginfo(msg.range_min)
    rospy.loginfo(msg.range_max)

    # TODO check for obstacle based on msg.ranges
    # what ranges[i] is front of turtlebot 

    # TODO publish message to car topic
    # best way to send message?

    # TODO publish movement for turtlebot
    # if no wall 
    # go forward 
    # else
    # turn left or right

def main():

    rospy.init_node("navigate")

    scan_sub = rospy.Subscriber(SCAN_TOPIC, LaserScan, call_back)

    move_pub = rospy.Publisher(MOVE_TOPIC, Twist, queue_size=1)

    while not rospy.is_shutdown():
        continue
    move_pub(Twist())


if __name__ == "__main__":
    main()
