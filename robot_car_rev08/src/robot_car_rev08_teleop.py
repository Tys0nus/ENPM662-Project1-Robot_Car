#!/usr/bin/env python
import rospy

from std_msgs.msg import Float64

import sys, select, termios, tty

msg = """
Control Your Robot Car
---------------------------
Moving around:
        w
   a    s    d
        x

w/x : increase/decrease linear velocity 
a/d : increase/decrease angular velocity

space key, s : force stop

CTRL-C to quit
"""
e = """
Communications Failed
"""

def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

if __name__=="__main__":
    settings = termios.tcgetattr(sys.stdin)
    
    rospy.init_node('turtlebot_teleop')

    pub_right = rospy.Publisher('/robot_car_rev08/front_right_steering_controller/command', Float64, queue_size=10) # Add your topic here between ''. Eg '/my_robot/steering_controller/command'
    pub_left = rospy.Publisher('/robot_car_rev08/front_left_steering_controller/command', Float64, queue_size=10)
    pub_move = rospy.Publisher('/robot_car_rev08/rear_wheel_controller/command', Float64, queue_size=10) # Add your topic for move here '' Eg '/my_robot/longitudinal_controller/command'

    steer = 0
    vel = 0
    try:
        print (msg)
        while(1):
            key = getKey()
            if key == 'w':
                vel += 0.5
                pub_left.publish(steer)
                pub_right.publish(steer)
                pub_move.publish(vel)
            elif key == 's':
                vel -= 0.5
                pub_left.publish(steer)
                pub_right.publish(steer)
                pub_move.publish(vel)
            elif key == 'a':
                steer += 0.5
                pub_left.publish(steer)
                pub_right.publish(steer)
            elif key == 'd':
                steer -= 0.5
                pub_left.publish(steer)
                pub_right.publish(steer)
            elif key == ' ':
                vel = 0.0
                steer = 0.0
                pub_left.publish(steer)
                pub_right.publish(steer)
                pub_move.publish(vel)
            else:
                if (key == '\x03'):
                    break
            
            if key in ['w','s','a','d',' ']:
                print("heading velocity: ", vel)
                print("steering angle: ", steer)

    except:
        print (e)

    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)