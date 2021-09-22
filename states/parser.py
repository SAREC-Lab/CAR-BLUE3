#!/usr/bin/env python

import roslib
import rospy
import smach
import smach_ros
from instruction import Instruction

class Parser(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                            outcomes=['parsed'],
                            input_keys=['task_plan_in', 'counter_in'],
                            output_keys=['counter_out', 'inst_out'])

    def execute(self, userdata):
        rospy.loginfo('Parsing command')
        inst_dict = userdata.task_plan_in[userdata.counter_in]
        userdata.inst_out = Instruction(inst_dict['command'], inst_dict['direction'], inst_dict['value'])
        userdata.counter_out = userdata.counter_in + 1
        return 'parsed' 