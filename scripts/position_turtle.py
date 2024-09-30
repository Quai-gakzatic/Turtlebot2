#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from std_msgs.msg import String

def odom_callback(data):
    position = data.pose.pose.position
    position_msg = f"Current Position: x = {position.x}, y = {position.y}"
    rospy.loginfo(position_msg)
    pub.publish(position_msg)

def position_turtle():
    rospy.init_node('position_turtle', anonymous=True)
    rospy.Subscriber('/odom', Odometry, odom_callback)
    global pub
    pub = rospy.Publisher('/turtle_pos_xy', String, queue_size=10)
    rospy.spin()

if __name__ == '__main__':
    try:
        position_turtle()
    except rospy.ROSInterruptException:
        pass
