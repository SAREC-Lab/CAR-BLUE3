#!/usr/bin/env python

import rospy
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String
from states.utils import straight, turn_circle

PLAN=list()

def call_back(msg, PLAN=PLAN):

    move_topic = rospy.get_param("~move_topic", "/car/mux/ackermann_cmd_mux/input/navigation")
    move_pub = rospy.Publisher(move_topic, AckermannDriveStamped, queue_size=1)

    movement = msg.data

    # use util functions to move car
    if movement == "Stop":
        use_plan()
        move_pub.publish(AckermannDriveStamped())

    rospy.loginfo(msg.data)
    PLAN.append(msg.data)
'''
    if movement == "Drive":
        rospy.loginfo(msg.data)
        PLAN.append(msg.data)
#        straight(move_pub, 0.18, 1)
    elif movement == "Left":
#        turn_circle(move_pub, 0.4, 1, 1, 0.25)
    elif movement == "Right":
#        turn_circle(move_pub, 0.4, 0, 1, 0.25)
    elif movement == "Stop":
        use_plan()
        move_pub.publish(AckermannDriveStamped())
    else:
        rospy.loginfo("Invalid message received")
'''

def use_plan(PLAN=PLAN):

    # TODO check how many drives before a turn
    # one drive command equates to 0.04 m to travel 
    # use that with straight and move_pub
    # then at a turn, simply turn_circle


def main():

    rospy.init_node("follow")

    rospy.Subscriber("comms", String, call_back)

    move_topic = rospy.get_param("~move_topic", "/car/mux/ackermann_cmd_mux/input/navigation")
    move_pub = rospy.Publisher("move_topic", AckermannDriveStamped, queue_size=1)

    while not rospy.is_shutdown():
        continue
    move_pub.publish(AckermannDriveStamped())


if __name__ == '__main__':
    main()
