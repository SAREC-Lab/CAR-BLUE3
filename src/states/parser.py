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
                            input_keys=["input_plan_in", "plan_counter_in"],
                            output_keys=["plan_counter_out"],
                            outcomes=["driving","success"]) # list(mapping.values())

    def execute(self, userdata):
        rospy.loginfo('Start Parsing')
        if len(userdata.input_plan_in) > userdata.plan_counter_in + 1:
            rospy.loginfo('Parsing command')
            userdata.plan_counter_out = userdata.plan_counter_in + 1
            return mapping[userdata.input_plan_in[0]["command"]]
        else:
            rospy.loginfo('No More plan to execute')
            return 'success'