#!/usr/bin/env python

import rospy
import smach
import time
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped
from .utils import straight

METER_CONVERSION = 0.3048

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
        straight(self.pub, distance,direction,None)

        return 'complete'
