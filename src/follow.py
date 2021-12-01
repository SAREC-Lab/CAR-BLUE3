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
    rospy.loginfo(msg.data)

    # use util functions to move car
    if movement == "Stop":
        use_plan(move_pub)
        move_pub.publish(AckermannDriveStamped())

    PLAN.append(msg.data)


def use_plan(move_pub, PLAN=PLAN):

    # TODO check how many drives before a turn
    # one drive command equates to 0.04 m to travel 
    # use that with straight and move_pub
    # then at a turn, simply turn_circle
    new_plan = list()
    drive = 0
    while PLAN:
        cmd = PLAN.pop(0)
        if cmd == "Drive":
            drive += 0.04
        elif cmd == "Turn":
            drive -= 0.4
            new_plan.append(drive)
            drive = 0
            new_plan.append(cmd)

    for cmd in new_plan:
        if cmd == "Turn":
            turn_circle(move_pub, 0.4, 1, 1, 0.25)
        else:
            if cmd < 0:
                straight(move_pub, cmd, 0)
            else:
                straight(move_pub, cmd, 1)


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
