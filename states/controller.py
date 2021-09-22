#!/usr/bin/env python

import rospy
import smach
from instruction import Instruction

class Controller(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['driving','turning','circle','three_point','stopping'],
                                    input_keys=['inst_in'])

    def execute(self, userdata):
        cmd = userdata.inst_in.command

        if cmd == 'drive':
            return 'driving'
        elif cmd == 'turn':
            return 'turning'
        elif cmd == 'stop':
            return 'stopping'
        elif cmd == 'circle':
            return 'circle'
        elif cmd == 'three_point':
            return 'three_point'
