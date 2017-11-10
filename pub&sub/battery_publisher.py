
#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
import rospy
from pycreate2 import Create2
import time

from std_msgs.msg import Int32
#define the sensor_state Publisher
def battery_state_publisher():
    rospy.init_node('battery_state')
    pub=rospy.Publisher('battery_values',Int32, queue_size=10)
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
    chargeb = 0;
    capacityb=0;
    while not rospy.is_shutdown():

        # Packet 100 contains all sensor data.
        chargeb = bot.get_sensors().battery_charge
        capacityb= bot.get_sensors().battery_capacity
        battery_state=chargeb/capacityb*100
        rospy.loginfo(battery_state)
        pub.publish(battery_state)
        rate.sleep()

if __name__=='__main__':
    try:
        battery_state_publisher()
    except rospy.ROSInterruptException:
        pass

