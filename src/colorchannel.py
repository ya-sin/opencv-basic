'''
Convert BGR to RGB.

Sample shows how cv.split and cv.merge function can be used
to change the channel in images.

Usage:
    colorchannel.py
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv

if __name__ == '__main__':

  # read image from source file
  import sys
  try:
    fn = sys.argv[1]
  except:
    fn = '../data/HappyFish.jpg'

  src = cv.imread(fn, cv.IMREAD_COLOR)

  if src is None:
    print('Failed to load image file:', fn)
    sys.exit(1)

  # # main code # #
  b,g,r = cv.split(src)
  RGB = cv.merge([r,g,b])

  # show images with opencv
  cv.imshow('BGR', src)
  cv.imshow('RGB', RGB)

  # a keyboard binding function.(in milliseconds)
  cv.waitKey(0)
  cv.destroyAllWindows()
