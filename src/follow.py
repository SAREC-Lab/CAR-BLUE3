#!/usr/bin/env python

import rospy
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped
from sensor_msgs.msg import LaserScan
from states.utils import straight, turn_circle

'''
call_back message from turtlebot's post

def call_back(msg):

# TODO read the message data and determine where to move
# use util functions to move car 

'''

def main():

    rospy.init_node("follow")

    # TODO add subscriber to turtlebot topic 

    move_topic = rospy.get_param("~move_topic", "/car/mux/ackermann_cmd_mux/input/navigation")
    move_pub = rospy.Publisher("move_topic", AckermannDriveStamped, queue_size=1)

    while not rospy.is_shutdown():
        rospy.spin()
    move_pub(AckermannDriveStamped())


if __name__ == '__main__':
    main()
