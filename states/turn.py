#!/usr/bin/env python

import rospy
import smach
import time
from geometry_msgs.msg import Twist
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped

METER_CONVERSION = 0.3048

# default globals
SPEED = 1
STEERING_ANGLE = 0.3
STEERING_ANGLE_VELOCITY = 0.2 
DISTANCE = 0.85

class Turn(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Parser'])
        self.counter = 0

    def execute(self, userdata):
        direction = float(userdata.inst_in.direction) # left = 0 or right = 1

        current_distance = 0
        t0 = rospy.Time.now().to_sec()

        rate = rospy.Rate(10)

        if direction: 
            STEERING_ANGLE = STEERING_ANGLE*(-1)
            STEERING_ANGLE_VELOCITY = STEERING_ANGLE_VELOCITY*(-1)


        drive = AckermannDrive(steering_angle=STEERING_ANGLE, steering_angle_velocity=STEERING_ANGLE_VELOCITY, speed=SPEED)

        # loop until distance is reached, publishing the message 
        while abs(current_distance) < DISTANCE:
            $PUBLISHER.publish(AckermannDriveStamped(drive=drive))
            t1 = rospy.Time.now().to_sec()
            current_distance = SPEED * (t1 - t0)

        rospy.sleep(1)

        return 'Parser'
