#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import String

def laser_callback(data):
    if min(data.ranges) < 30.0:  # Check if there's an obstacle within 30 meters
        rospy.loginfo("Obstacle Found")
        pub.publish("Obstacle Found")

def obstacle_identifier():
    rospy.init_node('obstacle_identifier', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, laser_callback)
    global pub
    pub = rospy.Publisher('/obstacle', String, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    try:
        obstacle_identifier()
    except rospy.ROSInterruptException:
        pass
