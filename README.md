# poject 3
*this project is to communcate with irobot roomba using Ros in raspberrypi, so after you install ros kinetic follow the instructions below:

First you need to creat a 'worck space' and a ' package', to do so please follow steps (4.1 ,4.2) in the link below:
https://www.intorobotics.com/ros-kinetic-publisher-and-subscriber-in-python/

Then put the files found in folder pub&sub inside /your_work_space/src/your_pakage_name/src/

Then go to /your_work_spase directory and type:


```
$rosdep update

$rosdep install --from-paths src -i -y

$catkin_make

$source ./devel/setup.bash

$pip install pycreate2
```
In a new session type to intiate roscore:
```
$cd /your_work_space
$source ./devel/setup.bash
$export ROS_MASTER_URI=http://[pi_ip_address]:11311
$export ROS_IP=[pi_ip_address]
$roscore
```
Now in the original session type to run the publishers:
```
$cd /your_work_space/src/your_pakage_name/src/
$chmod u+x 'file_names.py'
$sudo usermod -a -G dialout $USER  #give permission to the USB port to serial
$rosrun 'your_pakage_name' 'file_name.py'
```
For subscriber you will need a publisher, in the code wheel_subscriber change the rospy.subscriber topic name to your publisher topic name(you publisher need to publish int values -500 500)




