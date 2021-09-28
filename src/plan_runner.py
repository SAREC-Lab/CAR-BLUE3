import rospy
import smach
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped
import json
from states import Parser, Drive


def main():
    rospy.init_node('plan_runner')

    # TODO: Add plan file name, either hard-coded, through a ROS launch param, or command line arg parsing 
    plan_file = rospy.get_param("~plan_file")
    with open(plan_file,'r') as f:
        plan = json.load(f)

    # TODO: Figure out what to publish to
    control_topic = rospy.get_param("~control_topic", "/car/mux/ackermann_cmd_mux/input/navigation")
    
    sm = smach.StateMachine(outcomes=['success'])
    sm.userdata.plan_counter = 0
    sm.userdata.input_plan = plan # a list of plans waiting to be executed
    sm.userdata.inst = None # the plan that is under execution
    #TODO: Check if this is correct publisher setup
    sm.userdata.pub = rospy.Publisher(control_topic, AckermannDriveStamped, queue_size=1)

    with sm:
        smach.StateMachine.add('PARSER', Parser(),
                            transitions={'driving':'DRIVE'}) # TODO: add map to all different states
        
        # # TODO: Add transitions/states for every possible instruction 
        # smach.StateMachine.add('CONTROLLER', Controller(),
        #                         transitions={'forward':'FORWARD',
        #                             'exit':'EXIT'},
        #                         remapping={'inst_in':'inst'})
        
        # This provides a rough outline of how all the instruction states should look
        # TODO: Check if pub_out is necessary
        smach.StateMachine.add('DRIVE', Drive(),
                                transitions={'complete':'PARSER'},
                                remapping={'inst_in':'inst'})