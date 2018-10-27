'''
Read, display,and write images..

Sample shows how cv.read, cv.imshow,and cv.imwrite function can be used
to show/write images.

Usage:
    readwriteImg.py
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv
# from matplotlib import pyplot as plt

if __name__ == '__main__':

  # read image from source file
  import sys
  try:
    fn = sys.argv[1]
  except:
    fn = '../data/home.jpg'

  img_unchange = cv.imread(fn, cv.IMREAD_UNCHANGED)# unknown square on the image
  img_default = cv.imread(fn, cv.IMREAD_COLOR)
  img_gray = cv.imread(fn, cv.IMREAD_GRAYSCALE)
  if img_unchange is None:
    print('Failed to load image file:', fn)
    sys.exit(1)

  # # main code # #

  # make a window
  cv.namedWindow('img_default', cv.WINDOW_NORMAL)
  # show images with matplotlib
  # plt.imshow(img_unchange, cmap = 'gray', interpolation = 'bicubic')
  # plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
  # plt.show()

  # show images with opencv
  cv.imshow('img_unchange', img_unchange)
  cv.imshow('img_default', img_default)
  cv.imshow('img_gray', img_gray)

  # a keyboard binding function.(in milliseconds)
  k = cv.waitKey(0) & 0xFF

  # write images
  if k == 27: # wait for ESC key to exit
    cv.destroyAllWindows()
  elif k == ord('s'): # wait for 's' key to save and exit
    cv.imwrite('homeGray.jpg',img_gray)
