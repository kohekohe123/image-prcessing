import cv2
import numpy as np

def myfunc(i):
    pass # do nothing

cv2.namedWindow('gray') # create win with win name

cv2.createTrackbar("ON/OFF","gray", 0, 1, myfunc)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while(True):
    ret, frame = cap.read()
    v=cv2.getTrackbarPos("ON/OFF","gray")
    cv2.imshow('gray',frame)
    if v==1:
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imshow('gray',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
