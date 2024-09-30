#!/usr/bin/env python
import rospy
from std_msgs.msg import String

command_history = []

def command_callback(data):
    command_history.append(data.data)
    rospy.loginfo(f"Command received: {data.data}")
    rospy.loginfo(f"Command history: {command_history}")

def command_history_node():
    rospy.init_node('command_history', anonymous=True)
    rospy.Subscriber('/turtlebot_commands', String, command_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        command_history_node()
    except rospy.ROSInterruptException:
        pass
