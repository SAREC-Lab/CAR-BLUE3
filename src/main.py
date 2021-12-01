#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point

def main():

    rospy.init_node("master")

    coordinates_pub = rospy.Publisher("coordinates", Point, queue_size=10)

    # TODO Get point from input and publish
    p = Point()
    p.x = 3
    p.y = 3
    coordinates_pub.publish(p)

if __name__ == '__main__':
    main()
