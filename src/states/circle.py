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
        """
            {
                "command": "circle",
                "value":[
                    4, # radius
                    0, # left circle = 1 or right circle = 0
                    1, # 1-->forward, 0--> backward
                    2, # number of circles to travel
                ]
            }
        """
        counter = userdata.plan_counter_in
        radius = userdata.input_plan_in[counter]["value"][0]
        direction = userdata.input_plan_in[counter]["value"][1]
        forward = userdata.input_plan_in[counter]["value"][2]
        num_circle = userdata.input_plan_in[counter]["value"][3]

        turn_circle(self.pub,radius, direction, forward, num_circle)
        return 'complete'
