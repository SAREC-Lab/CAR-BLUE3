#!/usr/bin/env python

import rospy
import smach
import time
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped

class Stop(smach.State):
    """
        {
        "command": "stop",
        "value":[
            10 # stop for 10 sec
        ]
    }
    """
    def __init__(self,publisher=None):
        smach.State.__init__(self,input_keys=["plan_counter_in","input_plan_in"],outcomes=['complete'])
        self.pub = publisher

    def execute(self, userdata):
        counter = userdata.plan_counter_in
        secs = userdata.input_plan_in[counter]["value"][0]
        # rospy.loginfo(f"Stop for {secs} seconds")
        rospy.sleep(secs)
        return 'complete'

