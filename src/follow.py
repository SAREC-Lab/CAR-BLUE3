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
        del PLAN
    else:
        PLAN.append(msg.data)


def use_plan(move_pub, PLAN=PLAN):

    # TODO check how many drives before a turn
    # one drive command equates to 0.04 m to travel 
    # use that with straight and move_pub
    # then at a turn, simply turn_circle
    if len(PLAN) == 0: return

    new_plan = list()
    drive = 0
    while PLAN:
        cmd = PLAN.pop(0)
        if cmd == "Drive":
            drive += 0.04
        elif cmd == "Turn":
            new_plan.append(drive)
            drive = 0
            new_plan.append(cmd)

    for cmd in new_plan:
        if cmd == "Turn":
            tb_turn(move_pub, 1)
        else:
            if cmd < 0:
                straight(move_pub, cmd, 0)
            else:
                straight(move_pub, cmd, 1)

def tb_turn(move_pub,left):
    """
    left: 1 --> going left; 0 --> going right
    Do a TurtleBot style turn on the car.
    1. The car will first move backward (in case there is a wall right in front of it).
    2. The car then will do a turn by a quarterly circle.
    3. The car will move backward 
    """
    RADIUS = 0.4 # Might need to tune this to make a turn in the hall way
    NUMBER_OF_CIRCLE = 0.25 # Theoretically it should only turn 1/4 circle. but may require change in practice
    straight(move_pub,RADIUS,0)
    turn_circle(move_pub,RADIUS,left,1,NUMBER_OF_CIRCLE)
    straight(move_pub,RADIUS,0)

def main():

    rospy.init_node("follow")

    rospy.Subscriber("comms", String, call_back)

    move_topic = rospy.get_param("~move_topic", "/car/mux/ackermann_cmd_mux/input/navigation")
    move_pub = rospy.Publisher(move_topic, AckermannDriveStamped, queue_size=1)

    while not rospy.is_shutdown():
        continue
    move_pub.publish(AckermannDriveStamped())


if __name__ == '__main__':
    main()
