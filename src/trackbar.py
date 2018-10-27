'''
build trackbar(slider) in OpenCV.

application in BGR color. use funciotn cv.getTrackbarPos(), cv.createTrackbar().

Usage:
    trackbar.py
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv

if __name__ == '__main__':
    def nothing(x):
        # equal to the value of cv.getTrackbarPos()
        print(x)
    # Create a black image, a window
    img = np.zeros((300,512,3), np.uint8)
    cv.namedWindow('image')
    # create trackbars for color change
    cv.createTrackbar('R','image',0,255,nothing)
    cv.createTrackbar('G','image',0,255,nothing)
    cv.createTrackbar('B','image',0,255,nothing)
    # create switch for ON/OFF functionality
    switch = '0 : OFF \n1 : ON'
    cv.createTrackbar(switch, 'image',0,1,nothing)
    # keep updating
    while(1):
        cv.imshow('image',img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break
        # get current positions of four trackbars
        r = cv.getTrackbarPos('R','image')
        g = cv.getTrackbarPos('G','image')
        b = cv.getTrackbarPos('B','image')
        s = cv.getTrackbarPos(switch,'image')
        if s == 0:
            img[:] = 0
        else:
            img[:] = [b,g,r]
    cv.destroyAllWindows()