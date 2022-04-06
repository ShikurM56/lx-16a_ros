#!/usr/bin/env python3

#Declare libraries
import rospy
from lx16a import *
from math import sin, cos
from std_msgs.msg import Int64


"""Lets move a motor to a desired position using
a value (deg) sent by a program in ROS"""

def callback(data):
	# Print the received data
	print("Im hearing: ", data.data)

	# Put the value in the function.
	servo1.moveTimeWrite(data.data)


def program_init():
	# Init the node
	rospy.init_node('main', anonymous=True)

	# Subscribe to a topic named "Received Angle" and call the function "callback"
	rospy.Subscriber("lx_angle", Int64, callback)

	#Spin the program
	rospy.spin()

if __name__ == '__main__':
	# Select the correct port, otherwise, the program wont continue
	LX16A.initialize("/dev/ttyUSB0")

	# Define the servos, remember you had to set the ID before.
	servo1 = LX16A(0)

	# Define the mode, in this case, servoMode
	servo1.servoMode()

	# Start the program
	program_init()


