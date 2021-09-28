#!/usr/bin/env python

import rospy
import smach
import time
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped
from .utils import turn_circle

METER_CONVERSION = 0.3048


class Circle(smach.State):
    def __init__(self, publisher):
        smach.State.__init__(self,input_keys=["plan_counter_in","input_plan_in"],outcomes=['complete'])
        self.pub = publisher

    def execute(self, userdata):
        counter = userdata.plan_counter_in
        radius = float(userdata.input_plan_in[counter]["value"][0])
        direction = float(userdata.input_plan_in[counter]["value"][1]) # left = 0 or right = 1

        turn_circle(self.pub,radius, 1, 1, 1)
        return 'complete'
