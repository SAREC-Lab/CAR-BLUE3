#!/usr/bin/env python

import rospy
import Tkinter as tk
from geometry_msgs.msg import Point

def enter():
    l2 = tk.Label(window, text="Submitted. Turtlebot ready to move!")
    l2.pack()
    print(e1.get())
    point = list(map(int, e1.get().strip().split(',')))
    coordinates_pub = rospy.Publisher("coordinates", Point, queue_size=10)
    p = Point()
    p.x = point[0]
    p.y = point[1]
    coordinates_pub.publish(p)

# Main Execution
rospy.init_node("master")

window = tk.Tk()
window.geometry('500x400')
l1 = tk.Label(window, text='Point (Enter as "x,y"):')
l1.pack()
e1 = tk.Entry(window, bd =5)
e1.pack()
b1 = tk.Button(window, text="Enter", command=enter)
b1.pack()

window.mainloop()
