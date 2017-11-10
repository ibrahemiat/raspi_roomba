#!/usr/bin/env python
from __future__ import print_function
import rospy
from pycreate2 import Create2
import time

from std_msgs.msg import Int32
#define the sensor_state Publisher
def sensor_state_publisher():
    rospy.init_node('sensor_state')
    pub=rospy.Publisher('sensor_values',Int32, queue_size=10)
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
    sensor_state=[0,0,0,0,0,0];
    while not rospy.is_shutdown():

        # Packet 100 contains all sensor data.
        sensor_state[0] = bot.get_sensors().light_bumper_left
        sensor_state[1]= bot.get_sensors().light_bumper_front_left
        sensor_state[2]= bot.get_sensors().light_bumper_center_left
        sensor_state[3]= bot.get_sensors().light_bumper_center_right
        sensor_state[4]= bot.get_sensors().light_bumper_front_right
        sensor_state[5]= bot.get_sensors().light_bumper_right
        rospy.loginfo(sensor_state)
        pub.publish(sensor_state)
        rate.sleep()

if __name__=='__main__':
    try:
        sensor_state_publisher()
    except rospy.ROSInterruptException:
        pass

