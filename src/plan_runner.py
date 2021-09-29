#!/usr/bin/env python

import rospy
import smach
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped
import json
from states import Parser, Drive, Circle, Stop


def main():
    rospy.init_node("plan_runner")
    # TODO: Add plan file name, either hard-coded, through a ROS launch param, or command line arg parsing 
    plan_file = rospy.get_param("~plan_file")
    with open(plan_file,'r') as f:
        plan = json.load(f)

    # init_pose_topic = rospy.get_param("~init_pose_topic", "/initialpose")
    # pub_init_pose = rospy.Publisher(init_pose_topic, PoseWithCovarianceStamped, queue_size=1)
    # TODO: Figure out what to publish to
    control_topic = rospy.get_param("~control_topic", "/car/mux/ackermann_cmd_mux/input/navigation")
    
    sm = smach.StateMachine(outcomes=['success'])
    sm.userdata.plan_counter = -1 # the index of plan that is running
    sm.userdata.input_plan = plan # a list of plans waiting to be executed
    #TODO: Check if this is correct publisher setup
    publisher = rospy.Publisher(control_topic, AckermannDriveStamped, queue_size=1) # userdata can only pass basic data types (immutable)

    with sm:
        rospy.loginfo("Build State Machine")
        smach.StateMachine.add('PARSER', Parser(),
                            remapping={
                                'input_plan_in':'input_plan',
                                'plan_counter_in' : 'plan_counter',
                                'plan_counter_out' : 'plan_counter'
                            },
                            transitions={
                                'driving':'DRIVE',
                                'circle':'CIRCLE',
                                'stop':'STOP',
                                }) # TODO: add map to all different states
        
        smach.StateMachine.add('DRIVE', Drive(publisher),
                            remapping={
                                'plan_counter_in' : 'plan_counter',
                                'input_plan_in' : 'input_plan'
                            },
                            transitions={'complete':'PARSER'})
        smach.StateMachine.add('STOP', Stop(publisher),
                            remapping={
                                'plan_counter_in' : 'plan_counter',
                                'input_plan_in' : 'input_plan'
                            },
                            transitions={'complete':'PARSER'})                    
        smach.StateMachine.add('CIRCLE', Circle(publisher),
                            remapping={
                                'plan_counter_in' : 'plan_counter',
                                'input_plan_in' : 'input_plan'
                            },
                            transitions={'complete':'PARSER'})

    # Execute SMACH plan
    outcome = sm.execute()

if __name__ == "__main__":
    main()