import rospy
import math
from ackermann_msgs.msg import AckermannDrive, AckermannDriveStamped

def straight(publisher, distance, forward, time=None):
    """
        Distance: How far to travel in meter. Always positive
        Forward: 1 --> going forward; 0 --> going backward
        time: How fast to accomplish this action
    """
    current_distance = 0
    t0 = rospy.Time.now().to_sec()

    rate = rospy.Rate(10)

    speed = 1 # default 1 m/s 
    if not forward: 
        speed = speed*(-1) # check reverse or forward

    drive = AckermannDrive(steering_angle=0, speed=speed)

    # loop until distance is reached, publishing the message 
    while abs(current_distance) < distance:
        publisher.publish(AckermannDriveStamped(drive=drive))
        t1 = rospy.Time.now().to_sec()
        current_distance = speed * (t1 - t0)
        rate.sleep()

    rospy.sleep(1)


def turn_circle(publisher, radius, left, forward, circle_numbers, time=None):
    """
        radius: The radius of the circle
        left: 1 --> going left; 0 --> going right
        Forward: 1 --> going forward; 0 --> going backward
        circle_numbers : Number of circles to travel. 0.5 means semi-circle. 
            1.25 means 1 full circling following a quarter circling
        time: How fast to accomplish this action
    """
    SPEED = 1
    STEERING_ANGLE = 0.3
    STEERING_ANGLE_VELOCITY = 0.2

    current_distance = 0
    distance = circle_numbers* 2 * math.pi * radius
    t0 = rospy.Time.now().to_sec()

    rate = rospy.Rate(10)

    if left: 
        left_coef = -1
    else:
        left_coef = 1
    
    if forward: 
        forward_coef = -1
    else:
        forward_coef = 1
    
    

    steering_angle = STEERING_ANGLE*left_coef
    steering_angle_velocity = STEERING_ANGLE_VELOCITY*left_coef
    speed = SPEED * forward_coef


    drive = AckermannDrive(steering_angle=steering_angle, steering_angle_velocity=steering_angle_velocity, speed=speed)

    current_distance = 0
    # loop until distance is reached, publishing the message 
    while abs(current_distance) < distance:
        publisher.publish(AckermannDriveStamped(drive=drive))
        t1 = rospy.Time.now().to_sec()
        current_distance += SPEED / radius * (t1 - t0)
        rate.sleep()

    rospy.sleep(1)