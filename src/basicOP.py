'''
Basic Operations on Images.

Access pixel values and modify them
Access image properties
Setting Region of Interest (ROI)
Splitting and Merging images

Usage:
    basicOP.py
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
        fn = '../data/home.jpg'

    img = cv.imread(fn, cv.IMREAD_COLOR)
    img_gray = cv.imread(fn, cv.IMREAD_GRAYSCALE)
    # # slow method to access pixel # #
    # get the bgr of (100,50) pixel
    px = img[100,50]
    print( "[b,g,r]",px )
    # get the b of (100,50) pixel
    # the third column (0,1,2)->(b,g,r)
    b = img[100,50,0]
    print("b",b)
    # modify the pixel values,making a white pixel
    img[100,100] = [255,255,255]
    print("[b,g,r]",img[100,100])
    cv.imshow("image",img)

    # # recommanded method to access pixel # #
    print("Get the r of one pixel.",img.item(100,50,2))
    # modifying RED value
    img.itemset((100,50,2),255)
    img.itemset((100,50,0),0)
    img.itemset((100,50,1),0)
    print("modifying RED value",img.item(100,50,2))
    cv.imshow("image:modifying RED",img)

    # # Accessing Image Properties # #

    # number of rows, columns and channels
    print("img.shape",img.shape)
    print("img_gray.shape",img_gray.shape)# has no the third value

    # Total number of pixels
    print("the number of pixel",img.size)

    # Image datatype
    # print for "debugging"
    print("Image datatype",img.dtype)

    # # Image ROI # #
    # get the certain region of one picture
    ball = img[130:200, 250:330]
    img[273:343, 100:180] = ball
    cv.imshow("ROI",img)

    img = cv.imread(fn, cv.IMREAD_COLOR)
    # # Splitting and Merging Image Channels # #
        # split takes time
        # b,g,r = cv.split(img)
    # Numpy fater 
    b = img[:,:,0]
    g = img[:,:,1]
    r = img[:,:,2]
    img = cv.merge((r,g,b))
    cv.imshow("split and merge(bgr->rgb)",img)
    img[:,:,2] = 0
    cv.imshow("red channel to zero",img)

    # # # Making Borders # # #
    # for convolution!!
    # cv.copyMakeBorder(src,top,bottom,left,right(,value=[b,g,r]))
    img = cv.imread(fn, cv.IMREAD_COLOR)
    replicate = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REPLICATE)
    reflect = cv.copyMakeBorder(img,10,10,10,10,cv.BORDER_REFLECT)
    cv.imshow("replicate",replicate)
    cv.imshow("reflect",reflect)


    # a keyboard binding function.(in milliseconds)
    cv.waitKey(0)
    cv.destroyAllWindows()