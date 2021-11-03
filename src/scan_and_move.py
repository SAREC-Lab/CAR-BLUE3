#!/usr/bin/env python

import rospy
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped
from sensor_msgs.msg import LaserScan
from states.utils import straight, turn_circle

THRESHOLD=1

def call_back(msg):

    move_topic = rospy.get_param("~move_topic", "/car/mux/ackermann_cmd_mux/input/navigation")
    move_pub = rospy.Publisher("move_topic", AckermannDriveStamped, queue_size=1)

    ranges = msg.ranges[315..405]
    rospy.loginfo(ranges)

    check = 0
    for val in ranges:
        if val < THRESHOLD:
            check += 1

    if check > len(ranges) / 2:
        # Turn car, there is a wall
        rospy.loginfo("There is a wall")
        turn_circle(move_pub, 0.4, 1, 1, 0.25)
    else:
        # continue straight
        rospy.loginfo("Continue straight")
        straight(move_pub, 1, 1)

def main():

    rospy.init_node("scan_and_move")

    scan_sub = rospy.Subscriber("/car/scan", LaserScan, call_back)

    move_topic = rospy.get_param("~move_topic", "/car/mux/ackermann_cmd_mux/input/navigation")
    move_pub = rospy.Publisher("move_topic", AckermannDriveStamped, queue_size=1)

    while not rospy.is_shutdown():
        continue
    move_pub(AckermannDriveStamped())


if __name__ == "__main__":
    main()
