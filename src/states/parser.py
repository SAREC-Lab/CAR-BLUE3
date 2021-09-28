#!/usr/bin/env python

import rospy
import smach


# a mapping from the command in `plan_file` to its corresponding state outcome
mapping = {
    "drive": "driving",
    "circle": "circle",
    # "turn": "turning",
    # "stop": "stopping",
    # "three_point": "three_point"
}

class Parser(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                            input_keys=["input_plan_in", "plan_counter_in"],
                            output_keys=["plan_counter_out"],
                            outcomes=list(mapping.values())+["success"])

    def execute(self, userdata):
        if len(userdata.input_plan_in) > userdata.plan_counter_in + 1:
            counter = userdata.plan_counter_in + 1
            userdata.plan_counter_out = counter
            return mapping[userdata.input_plan_in[counter]["command"]]
        else:
            rospy.loginfo('No More plan to execute')
            return 'success'