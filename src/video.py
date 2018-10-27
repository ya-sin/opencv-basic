'''
Capturing Video from Webcam,Playing video,and saving video.

cv.VideoCapture cv.VideoWriter_fourcc cv.VideoWriter out.write.

Usage:
    video.py
'''

# Python 2/3 compatibility
from __future__ import print_function

import numpy as np
import cv2 as cv

if __name__ == '__main__':
  # # main code # #
    # 0 means open the webcam,"path" mean open a video
    cap = cv.VideoCapture(0)

    # set the property of video, fail!
    # ret = cap.set(cv.CAP_PROP_FRAME_WIDTH,320)
    # ret = cap.set(cv.CAP_PROP_FRAME_HEIGHT,180)

    # get the property of video
    width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
    height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
    size = (int(width), int(height))

    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc('S', 'V', 'Q', '3') # specify the video codec
    out = cv.VideoWriter('output.avi',fourcc, 15.0, size)# mind the size!

    # check webcam opened or not
    if cap.isOpened():
        print("cap is opened!")
    else:
        cap.open()

    while(True):
        # Capture frame-by-frame
        # If frame is read correctly,ret = true
        ret, frame = cap.read()
        if(ret):
            # Our operations on the frame come here
            RGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            frame = cv.flip(RGB,0)
            # write the flipped frame
            out.write(frame)
            # Display the resulting frame
            cv.imshow('frame',frame)
            # waitKey() is about the playing rate
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # When everything done, release the capture and out
    cap.release()
    out.release()
    cv.destroyAllWindows()