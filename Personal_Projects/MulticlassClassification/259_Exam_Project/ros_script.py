#!/usr/bin/env python2.7

import sys
import roslib
import rospy
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import String
import cv2
from cv_bridge import CvBridge, CvBridgeError
import matplotlib
import os

rospy.init_node("reading_images")

image_counter = 0
images_per_second = 1
   
def callback(image):
   bridge = CvBridge()

   # Sjekker bildet ved raten som er gitt images_per_second
   global image_counter
   global images_per_second
   image_counter += 1
   if (image_counter % (30/images_per_second) == 0):
      try:
         # Konverterer bildet til en numpy-array
         cv_image = bridge.imgmsg_to_cv2(image, "bgr8")
         # Lagrer bildet i mappen "images"
         np.save(os.path.join("/home/ros/catkin_ws/src/reading_images/images", "image01"), cv_image)

      except CvBridgeError as e:
         print(e)

      # Viser hvert bilde som sjekkes 
      (rows,cols,channels) = cv_image.shape
      if cols > 60 and rows > 60 :
         cv2.circle(cv_image, (50,50), 10, 255)
         cv2.imshow("Image window", cv_image)
         cv2.waitKey(3)

# Subscriber til topicet "/camera/rgb/image_raw", som
# Kinect-kameraet sender bilder til. 
sub = rospy.Subscriber("/camera/rgb/image_raw", Image, callback)

rospy.spin()
