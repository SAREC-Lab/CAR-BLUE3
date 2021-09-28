#!/usr/bin/env python

import rospy
import smach
import time
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped

METER_CONVERSION = 0.3048

# default globals
SPEED = 1
STEERING_ANGLE = 0.3
STEERING_ANGLE_VELOCITY = 0.2 
PI = 3.141592653

class Circle(smach.State):
    def __init__(self, publisher):
        smach.State.__init__(self,input_keys=["plan_counter_in","input_plan_in"],outcomes=['complete'])
        self.pub = publisher

    def execute(self, userdata):
        counter = userdata.plan_counter_in
        radius = float(userdata.input_plan_in[counter]["value"][0])
        direction = float(userdata.input_plan_in[counter]["value"][1]) # left = 0 or right = 1

        current_distance = 0
        distance = 2 * PI * radius
        t0 = rospy.Time.now().to_sec()

        rate = rospy.Rate(10)

        if direction: 
            direction_coef = -1
        else:
            direction_coef = 1

        steering_angle = STEERING_ANGLE*direction_coef
        steering_angle_velocity = STEERING_ANGLE_VELOCITY*direction_coef


        drive = AckermannDrive(steering_angle=steering_angle, steering_angle_velocity=steering_angle_velocity, speed=SPEED)

        current_distance = 0
        # loop until distance is reached, publishing the message 
        while abs(current_distance) < distance:
            self.pub.publish(AckermannDriveStamped(drive=drive))
            t1 = rospy.Time.now().to_sec()
            current_distance += SPEED / radius * (t1 - t0)
            rate.sleep()

        rospy.sleep(1)

        return 'complete'
