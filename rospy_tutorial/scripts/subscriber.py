import rospy
from turtlesim.msg import Pose

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'Position x is %f and y is %f, Orientation is %f', data.x, data.y, data.theta)

def listener():
    #Initiate the node
    rospy.init_node('subscriber', anonymous=True)
    #Initiate the subscriber
    rospy.Subscriber('/turtle1/pose', Pose, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
