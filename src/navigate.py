#!/usr/bin/env python

import rospy
#from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
from std_msgs.msg import String
#from states.utils import straight, turn_circle

SCAN_TOPIC="/scan"
MOVE_TOPIC="/cmd_vel"


def call_back(msg):

    comms_pub = rospy.Publisher("comms", String, queue_size=10)
    move_pub = rospy.Publisher(MOVE_TOPIC, Twist, queue_size=1)

    # TODO check for obstacle based on msg.ranges
    # what ranges[i] is front of turtlebot 
    range = list(msg.ranges[0:45])
    range.extend(list(msg.ranges[315:360]))

    # TODO publish movement for turtlebot
    safe = 0
    for val in range:
        if val < 0.4 and val > 0:
            safe += 1
    move_cmd = Twist()
    if safe > (90 * 3 // 4):
        comms_pub.publish("Stop")
        move_pub.publish(move_cmd)
    else:
        move_cmd.linear.x = 0.2
        move_pub.publish(move_cmd)
        rospy.loginfo("moving")
        comms_pub.publish("Drive")

#    rospy.sleep(1)
#    move_pub.publish(move_cmd)
    # else
    # turn left or right

    # TODO publish message to car topic based on obstacle/tbot movement
    # comms_pub.Publish("Drive")
    # comms_pub.Publish("Stop")
    # comms_pub.Publish("Left")
    # comms_pub.Publish("Right")


def main():

    rospy.init_node("navigate")

    scan_sub = rospy.Subscriber(SCAN_TOPIC, LaserScan, call_back)

    move_pub = rospy.Publisher(MOVE_TOPIC, Twist, queue_size=1)

    while not rospy.is_shutdown():
        continue
    move_pub.publish(Twist())


if __name__ == "__main__":
    main()
