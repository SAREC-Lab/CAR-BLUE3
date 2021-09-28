#!/usr/bin/env python

import rospy
import smach
import time
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped

METER_CONVERSION = 0.3048
SPEED = 1 # default 1 m/s 

class Drive(smach.State):
    def __init__(self,publisher):
        smach.State.__init__(self,input_keys=["plan_counter_in","input_plan_in"],outcomes=['complete'])
        self.pub = publisher

    def execute(self, userdata):
        rospy.loginfo("Start Driving")
        counter = userdata.plan_counter_in
        distance = float(userdata.input_plan_in[counter]["value"][0]) # distance in feet
        direction = float(userdata.input_plan_in[counter]["value"][1]) # forward = 0 or reverse = 1

        distance = distance * METER_CONVERSION - 0.15 # convert from feet to meters 
        current_distance = 0
        t0 = rospy.Time.now().to_sec()

        rate = rospy.Rate(10)

        speed = SPEED
        if direction: 
            speed = speed*(-1) # check reverse or forward
            # distance = distance*(-1)

        drive = AckermannDrive(steering_angle=0, speed=speed)

        # loop until distance is reached, publishing the message 
        while abs(current_distance) < distance:
            self.pub.publish(AckermannDriveStamped(drive=drive))
            t1 = rospy.Time.now().to_sec()
            current_distance = speed * (t1 - t0)
            rate.sleep()

        rospy.sleep(1)

        return 'complete'
