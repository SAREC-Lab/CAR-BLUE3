import rospy
import smach
import smach_ros
import json
from states import Parser, Controller, Drive, Turn, Stop, Circle, ThreePoint


def main():
    rospy.init_node('plan_runner')

    # TODO: Add plan file name, either hard-coded, through a ROS launch param, or command line arg parsing 
    plan_file = open("")
    plan = json.load(plan_file)

    # TODO: Figure out what to publish to
    control_topic = rospy.get_param("~control_topic", "/car/mux/ackermann_cmd_mux/input/navigation")
    
    sm = smach.StateMachine(outcomes=['success'])
    sm.userdata.plan_counter = 0
    sm.userdata.input_plan = plan
    sm.userdata.inst = None 
    #TODO: Check if this is correct publisher setup
    sm.userdata.pub = rospy.Publisher(control_topic, AckermannDriveStamped, queue_size=1)

    with sm:
        smach.StateMachine.add('PARSER', Parser(),
                            transitions={'parsed':'CONTROLLER'},
                            remapping={'task_plan_in':'input_plan',
                                    'counter_in':'plan_counter',
                                    'counter_out':'plan_counter',
                                    'inst_out':'inst'})
        
        # TODO: Add transitions/states for every possible instruction 
        smach.StateMachine.add('CONTROLLER', Controller(),
                                transitions={'forward':'FORWARD',
                                    'exit':'EXIT'},
                                remapping={'inst_in':'inst'})
        
        # This provides a rough outline of how all the instruction states should look
        # TODO: Check if pub_out is necessary
        smach.StateMachine.add('DRIVE', Drive(),
                                transitions={'complete':'PARSER'},
                                remapping={'inst_in':'inst',
                                    'pub_in':'pub',
                                    'pub_out':'pub'})
        
        smach.StateMachine.add('EXIT', Exit(),
                                transitions={'out':'success'})