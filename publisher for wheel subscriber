#!/usr/bin/env python
import rospy

from std_msgs.msg import Int32

#define the wheel_speed Publisher
def wheel_speed_publisher():
    rospy.init_node('wheel_speed')
    pub=rospy.Publisher('rand_no', Int32, queue_size=10)
    rate= rospy.Rate(2)
#generate the speed at every 2 seconds
    while not rospy.is_shutdown():
        speed=70
        rospy.loginfo(speed)
        pub.publish(speed)
        rate.sleep()

if __name__=='__main__':
    try:
        random_number_publisher()
    except rospy.ROSInterruptException:
        pass
