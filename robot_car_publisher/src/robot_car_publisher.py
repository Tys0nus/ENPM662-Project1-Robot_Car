from ast import Str
import rospy
from std_msgs.msg import Float64

class opencontrol_robot_car():
    def __init__(self):
        rospy.init_node('robot_car_opencontrol')#, anonymous=True
        
        rospy.loginfo("Robot Car Stop Sequence: CTRL + C")
        rospy.on_shutdown(self.shutdown)
    
    def heading(self, velocity, steer):
        
        self.pub_right= rospy.Publisher('/robot_car_rev08/front_right_steering_controller/command', Float64, queue_size=10)
        self.pub_left= rospy.Publisher('/robot_car_rev08/front_left_steering_controller/command', Float64, queue_size=10)  
        self.pub_move= rospy.Publisher('/robot_car_rev08/rear_wheel_controller/command', Float64, queue_size=10) 

        
        r = rospy.Rate(100)
        while not rospy.is_shutdown():
            print("velocity: ",velocity," steer: ", steer)
            self.pub_move.publish(velocity)
            self.pub_right.publish(steer)
            self.pub_left.publish(steer)
            r.sleep()

    
    def shutdown(self):
        rospy.sleep(1)
 
        
if __name__ == '__main__':
    try:
        vel = 5
        steer = 1
        obj = opencontrol_robot_car()
        obj.heading(vel, steer)

    except rospy.ROSInterruptException:
        pass
    except:
        rospy.loginfo('Robot Car Node Terminated')