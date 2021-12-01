#!/usr/bin/env python

import rospy
#from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import String
#from states.utils import straight, turn_circle

SCAN_TOPIC="/scan"
MOVE_TOPIC="/cmd_vel"
COMMANDS = list()
x_coordinate=0
y_coordinate=0

'''
Setup pub/sub from laptop to turtlebot with Point message 
At beginning of call_back check if at desired point
If there is a wall try to turn in the appropriate direction
If there send Twist() (stop message) and sleep maybe?
Then iterate over commands to publish them to car 
'''

'''
I don't think this is necessary because of COMMANDS=COMMANDS

def call_back_wrapper(msg):

    call_back_scan(msg, COMMANDS)
'''

def call_back_scan(msg, COMMANDS=COMMANDS):

#    comms_pub = rospy.Publisher("comms", String, queue_size=10)
    move_pub = rospy.Publisher(MOVE_TOPIC, Twist, queue_size=1)

    # what ranges[i] is in front of turtlebot 
    range = list(msg.ranges[0:45])
    range.extend(list(msg.ranges[315:360]))

    # TODO publish movement for turtlebot
    safe = 0
    for val in range:
        if val < 0.4 and val > 0:
            safe += 1
    move_cmd = Twist()
    if safe > (90 * 3 // 4):
        COMMANDS.append("Stop")
#        comms_pub.publish("Stop")
        move_pub.publish(move_cmd)
    else:
        move_cmd.linear.x = 0.2
        move_pub.publish(move_cmd)
        rospy.loginfo("moving")
        COMMANDS.append("Drive")
#        comms_pub.publish("Drive")

    # TODO publish message to car topic based on obstacle/tbot movement


def call_back_pose(msg):

    point = msg.pose.pose
    # TODO determine when Turtlebot reaches destination
    # and then send plan to car 
   
    if (point.x - 0.1 < x_coordinate < point.x + 0.1) and (point.y - 0.1
    < y_coordinate < point.y + 0.1):
        send_plan()
        comms_pub = rospy.Publisher("comms", String, queue_size=10)
        for cmd in COMMANDS: 
            comms_pub.publish(cmd)
    

def send_plan(COMMANDS=COMMANDS):

    comms_pub = rospy.Publisher("comms", String, queue_size=10)
    for cmd in COMMANDS:
        comms_pub.publish(cmd)


def get_coordinates(point):

    global x_coordinate
    global y_coordinate
    x_coordinate = point.x
    y_coordinate = point.y


def main():

    rospy.init_node("navigate")

    coordinates_sub = rospy.Subscriber("coordinates", Point, get_coordinates)
    scan_sub = rospy.Subscriber(SCAN_TOPIC, LaserScan, call_back_scan)
    point_sub = rospy.Subscriber('/odom', Odometry, call_back_pose)

    move_pub = rospy.Publisher(MOVE_TOPIC, Twist, queue_size=1)

    while not rospy.is_shutdown():
        continue
    move_pub.publish(Twist())


if __name__ == "__main__":
    main()
