'''
Draw different geometric shapes with OpenCV.

cv.line(), cv.circle() , cv.rectangle(), cv.ellipse(), cv.putText().

Usage:
    drawing.py
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv

if __name__ == '__main__':

  # Create a black image
  img = np.zeros((512,512,3), np.uint8)

  # Draw a diagonal blue line with thickness of 5 px
  # give starting and ending points
  cv.line(img,(0,0),(511,511),(255,0,0),5)

  # Draw a green rectangl
  # give  top-left corner and bottom-right points
  cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

  # Draw a red circle
  # give center point and radius
  cv.circle(img,(447,63), 63, (0,0,255), -1)

  # Draw a red ellipse
  # -1 means filled the shape
  # !mind the angles used in ellipse
  cv.ellipse(img,(256,256),(100,50),45,45,270,(0,0,255),-1)

  # Draw a red polygon
  # ROWSx1x2
  pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
  pts = pts.reshape((-1,1,2))
  cv.polylines(img,[pts],False,(0,255,255))# False means start point and end point won't joint

  # Add text
  font = cv.FONT_HERSHEY_SIMPLEX
  cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

  cv.imshow('painting',img)

  # a keyboard binding function.(in milliseconds)
  cv.waitKey(0)
  cv.destroyAllWindows()