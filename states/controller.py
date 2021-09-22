#!/usr/bin/env python

import rospy
import smach
import time
from geometry_msgs.msg import Twist

class Controller(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Exit'])
        self.counter = 0

    def execute(self, userdata):
        return 'Exit'
