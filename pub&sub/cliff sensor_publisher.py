#!/usr/bin/env python
from __future__ import print_function
import rospy
from pycreate2 import Create2
import time

from std_msgs.msg import Int32
#define the sensor_state Publisher
def cliff_state_publisher():
    rospy.init_node('cliff_state')
    pub=rospy.Publisher('cliff_values',Int32, queue_size=10)
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
    cliff_state=[0,0,0,0];
    while not rospy.is_shutdown():

        # Packet 100 contains all sensor data.
        cliff_state[0] = bot.get_sensors().cliff_left
        cliff_state[1]= bot.get_sensors().cliff_front_left
        cliff_state[2]= bot.get_sensors().cliff_front_right
        cliff_state[3]= bot.get_sensors().cliff_right

        rospy.loginfo(cliff_state)
        pub.publish(cliff_state)
        rate.sleep()

if __name__=='__main__':
    try:
        cliff_state_publisher()
    except rospy.ROSInterruptException:
        pass

