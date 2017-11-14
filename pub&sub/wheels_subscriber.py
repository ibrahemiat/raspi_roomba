#!/usr/bin/env python
from __future__ import print_function
import rospy
from pycreate2 import Create2

from std_msgs.msg import Int32
#define the display text
def callback(data):
    m=data.data
    #rospy.loginfo(m)
    print(m)
    port = '/dev/ttyUSB0'
    baud = {
        'default': 115200,
        'alt': 19200  # shouldn't need this unless you accident$
    }
    bot = Create2(port=port, baud=baud['default'])

    bot.start()

    bot.full()
    while not rospy.is_shutdown():

        bot.drive_direct(m,m)


#define the subscriber
def random_subscriber():
    rospy.init_node('wheel_subscriber')
    rospy.Subscriber('rand_no',Int32, callback)

    rospy.spin()

if __name__=='__main__':
    random_subscriber()

