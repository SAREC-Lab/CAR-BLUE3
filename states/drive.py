#!/usr/bin/env python

import rospy
import smach
import time
from geometry_msgs.msg import Twist
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped

METER_CONVERSION = 0.3048
SPEED = 1 # default 1 m/s 

class Drive(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Parser'])
        self.counter = 0

    def execute(self, userdata):
        distance = float(userdata.inst_in.value) # distance in feet
        direction = float(userdata.inst_in.direction) # forward = 0 or reverse = 1

        distance = distance * METER_CONVERSION - 0.15 # convert from feet to meters 
        current_distance = 0
        t0 = rospy.Time.now().to_sec()

        rate = rospy.Rate(10)

        if direction: 
            SPEED = SPEED*(-1) # check reverse or forward

        drive = AckermannDrive(steering_angle=0, speed=SPEED)

        # loop until distance is reached, publishing the message 
        while abs(current_distance) < distance:
            $PUBLISHER.publish(AckermannDriveStamped(drive=drive))
            t1 = rospy.Time.now().to_sec()
            current_distance = SPEED * (t1 - t0)

        rospy.sleep(1)

        return 'Parser'
