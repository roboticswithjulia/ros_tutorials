import rospy
from geometry_msgs.msg import Twist

def talker():
    #Initiate the node
    rospy.init_node('talker', anonymous=True)
    #Initiate the publisher
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        #Initate a new message
        geometry_message = Twist()
        #Fill the message with custom data
        geometry_message.linear.x = 0.5
        geometry_message.linear.y = 0.1
        hello_str = "Publishing x=0.5 and y=0.1" 
        rospy.loginfo(hello_str)
        #Publish the message
        pub.publish(geometry_message)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
