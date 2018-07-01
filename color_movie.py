import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,100,nothing)
cv2.createTrackbar('G','image',0,100,nothing)
cv2.createTrackbar('B','image',0,100,nothing)
cv2.createTrackbar('gamma','image',0,300,nothing)

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while(True):
    ret, frame = cap.read()
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    v = cv2.getTrackbarPos('gamma','image')

    B=frame[:,:,0]
    G=frame[:,:,1]
    R=frame[:,:,2]
    B=B/255.0
    G=G/255.0
    R=R/255.0
    B=(B**(v/100.0))
    G=(G**(v/100.0))
    R=(R**(v/100.0))
    if b!=0:
        B=(B**(1/b))
    if g!=0:
        G=(G**(1/g))
    if r!=0:
        R=(R**(1/r))

    frame[:,:,0]=B*255
    frame[:,:,1]=G*255
    frame[:,:,2]=R*255


    cv2.imshow('image',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):   #qで終了
        break


cv2.destroyAllWindows()
