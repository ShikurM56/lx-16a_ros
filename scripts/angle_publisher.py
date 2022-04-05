#!/usr/bin/env python

import rospy
from std_msgs.msg import Int64

def angle_publisher():
    pub = rospy.Publisher('lx_angle', Int64, queue_size=10)
    rospy.init_node('angle_publisher', anonymous=True)

    # Define the new INT64 message 
    msg = Int64()

    # The message will be published every second (1 Hz = 1 time per second)
    rate = rospy.Rate(1)

    # While ROS is running
    while not rospy.is_shutdown():

        # Assign the value to the message
        msg.data = 0

        # Print the message
        print ("publishing ", msg.data)

        # Publish the message
        pub.publish(msg)

        # Wait for a second
        rate.sleep()
        
        # Repeat
        msg.data = 90
        print ("publishing ", msg.data)
        pub.publish(msg)
        rate.sleep()

        # Repeat
        msg.data = 180
        print ("publishing ", msg.data)
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        angle_publisher()
    except rospy.ROSInterruptException:
        pass

