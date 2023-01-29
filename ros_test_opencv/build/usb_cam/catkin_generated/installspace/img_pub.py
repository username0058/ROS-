import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge , CvBridgeError
def img_pub():
    bridge = CvBridge()
    capture = cv2.VideoCapture(0) # 定义摄像头
    rospy.init_node('camera_node', anonymous=True) #定义节点
    image_pub=rospy.Publisher('/image_view/image_raw', Image, queue_size = 10) #定义话题
    rate = rospy.Rate(15)
    while not rospy.is_shutdown():   
        ret, frame = capture.read()
        if ret: # 如果有画面再执行
            frame = cv2.flip(frame,1)   #水平镜像操作
            try:  
                image_pub.publish(bridge.cv2_to_imgmsg(frame, "bgr8"))
                rospy.loginfo("Great!Running img_pub node.")
            except CvBridgeError as e:
                print (e)
    capture.release()
    cv2.destroyAllWindows()
    print ("You quit it successfully!Waiting for your next use!Bye!")
if __name__=="__main__":
    try:
        img_pub()
    except KeyboardInterrupt:
        print ("Oh,NO!Something is wrong!Shutting down img_pub node.")
        cv2.destroyAllWindows()
