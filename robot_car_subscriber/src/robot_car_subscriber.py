from turtle import st
import rospy
from std_msgs.msg import Float64

def velocity_callback(velocity_data):
    rospy.loginfo("velocity data: %.1f", velocity_data.data)
    
def steering_callback(steer_data):
    rospy.loginfo("steering data : %.1f", steer_data.data)

    
def listener():
    rospy.init_node('robot_car_subscriber_topic', anonymous=True)
    sub_vel = rospy.Subscriber('/robot_car_rev08/rear_wheel_controller/command', Float64, velocity_callback)
    sub_steer_left = rospy.Subscriber('/robot_car_rev08/front_left_steering_controller/command', Float64, steering_callback)
    sub_steer_right = rospy.Subscriber('/robot_car_rev08/front_right_steering_controller/command', Float64, steering_callback)
    rospy.spin()
 
if __name__ == '__main__':
    try:
        listener()

    except rospy.ROSInterruptException:
        pass
#    except:
#        rospy.loginfo('Robot Car Node Terminated')