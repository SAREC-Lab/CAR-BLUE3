#!/usr/bin/env python

import rospy
import smach


# a mapping from the command in `plan_file` to its corresponding state outcome
mapping = {
    "drive": "driving",
    "turn": "turning",
    "stop": "stopping",
    "circle": "circle",
    "three_point": "three_point"
}

class Parser(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                            outcomes=['driving','turning','circle','three_point','stopping'])

    def execute(self, userdata):
        if len(userdata.input_plan) > 0:
            rospy.loginfo('Parsing command')
            userdata.inst = userdata.input_plan.pop(0)  
            return mapping[userdata.inst["command"]]
        else:
            return 'success'