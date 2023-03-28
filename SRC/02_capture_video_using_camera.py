"""
Capture live stream video from the camera

"""

import cv2
# capture the video from the camera here we need to specify the location of camera using 0 or -1

capture = cv2.VideoCapture(0) 
# While loop is used to capture the video 
while (True):
    ret, frame = capture.read() # read capture frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert RBG to GRAY
    cv2.imshow('frame', gray) # Display
    if cv2.waitKey(1) & 0xFF == ord("q"): # wait till the user clicks on "q"
        break
capture.release() # our camera should be released/stopped
cv2.destroyAllWindows() # Close all windows