#!/usr/bin/env python3
# coding:utf-8

import cv2
import numpy as np
import rospy
from std_msgs.msg import Header
from sensor_msgs.msg import Image
from cv_bridge import CvBridge , CvBridgeError
# import time
### this is reference code
### a straight way:define message
if __name__=="__main__":
    capture = cv2.VideoCapture(0) # 定义摄像头
    rospy.init_node('camera_node', anonymous=True) #定义节点
    image_pub=rospy.Publisher('/image_view/image_raw', Image, queue_size = 1) #定义话题

    while not rospy.is_shutdown():    
        # start = time.time()
        ret, frame = capture.read()
        if ret: # 如果有画面再执行
            # frame = cv2.flip(frame,0)   #垂直镜像操作
            frame = cv2.flip(frame,1)   #水平镜像操作   
            ros_frame = Image()
            header = Header(stamp = rospy.Time.now())
            header.frame_id = "Camera"
            ros_frame.header=header
            ros_frame.width = 1280
            ros_frame.height = 720
            ros_frame.encoding = "bgr8"
            ros_frame.step = 1920
            ros_frame.data = np.array(frame).tostring() #图片格式转换
            image_pub.publish(ros_frame) #发布消息
            # end = time.time()  
            # print("cost time:", end-start ) # 看一下每一帧的执行时间，从而确定合适的rate,roughly use 15
            rate = rospy.Rate(15) 

    capture.release()
    cv2.destroyAllWindows() 
    print("quit successfully!")

