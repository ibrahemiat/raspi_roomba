#!/usr/bin/env python
from __future__ import print_function
import rospy
from pycreate2 import Create2
import time

from std_msgs.msg import Int32
#define the sensor_state Publisher
def angle_state_publisher():
    rospy.init_node('angle_state')
    pub=rospy.Publisher('angle_values',Int32, queue_size=10)
    rate= rospy.Rate(2)
    #read sensor range at every 2 seconds
    port = '/dev/ttyUSB0'
    baud = {
        'default': 115200,
        'alt': 19200  # shouldn't need this unless you accident$
    }
    bot = Create2(port=port, baud=baud['default'])

    bot.start()

    bot.full()

    print('Starting ...')
    angle_state = 0;
    while not rospy.is_shutdown():

        # Packet 100 contains all sensor data.
        angle_state = bot.get_sensors().angle

        rospy.loginfo(angle_state)
        pub.publish(angle_state)
        rate.sleep()

if __name__=='__main__':
    try:
        angle_state_publisher()
    except rospy.ROSInterruptException:
        pass


