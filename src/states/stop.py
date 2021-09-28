#!/usr/bin/env python

import rospy
import smach
import time
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped

class Stop(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Parser'])
        self.counter = 0

    def execute(self, userdata):
        return 'Parser'
