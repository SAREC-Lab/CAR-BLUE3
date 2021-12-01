#!/usr/bin/env python

import rospy
import numpy as np
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, Point, Pose
from nav_msgs.msg import Odometry
from std_msgs.msg import String

SCAN_TOPIC="/scan"
MOVE_TOPIC="/cmd_vel"
COMMANDS=list()
x_coord=0
y_coord=0
TARGET_RANGE = .1
TARGET=False

def call_back_scan(msg, COMMANDS=COMMANDS):

    move_pub = rospy.Publisher(MOVE_TOPIC, Twist, queue_size=1)

    range = list(msg.ranges[0:45])
    range.extend(list(msg.ranges[315:360]))

    safe = 0
    for val in range:
        if val < 0.4 and val > 0:
            safe += 1

    move_cmd = Twist()
    if TARGET:
        rospy.loginfo("Target reached")
        COMMANDS.append("Stop")
    elif safe > (90 * 3 // 4):
        move_cmd.angular.z = 0.2
        rospy.loginfo("Wall. Stop and turn")
        if COMMANDS[-1] is not "Turn": 
            COMMANDS.append("Turn")
    else:
        move_cmd.linear.x = 0.2
        rospy.loginfo("Drive forward")
        COMMANDS.append("Drive")

    move_pub.publish(move_cmd) # Might need to send the message with some constant frequency


def call_back_pose(msg):

    global TARGET
    point = msg.pose.pose
    current = np.array([point.x,point.y])
    target = np.array([x_coord,y_coord])

    if np.linalg.norm(current-target) <= TARGET_RANGE and not TARGET: # Euclidean distance
        COMMANDS.append("Stop")
        send_plan()
        TARGET = True


def send_plan(COMMANDS=COMMANDS):

    comms_pub = rospy.Publisher("comms", String, queue_size=10)
    for cmd in COMMANDS:
        comms_pub.publish(cmd)
    del COMMANDS[:] # clean the COMMANDS list


def get_coordinates(point):

    global TARGET
    global x_coord
    global y_coord
    x_coord = point.x
    y_coord = point.y
    TARGET = False # Once get new coordinate, set it to False


def main():

    rospy.init_node("navigate")

    coordinates_sub = rospy.Subscriber("coordinates", Point, get_coordinates)
    scan_sub = rospy.Subscriber(SCAN_TOPIC, LaserScan, call_back_scan)
    point_sub = rospy.Subscriber('/odom', Odometry, call_back_pose)

    move_pub = rospy.Publisher(MOVE_TOPIC, Twist, queue_size=1)

    while not rospy.is_shutdown():
        continue
    move_pub.publish(Twist())


if __name__ == '__main__':
    main()
