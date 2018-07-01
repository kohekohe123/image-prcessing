import cv2
import numpy as np
from scipy.ndimage.filters import convolve
from numpy import uint8,float32,float64,log,pi,sin,cos,abs,sqrt

def myfunc(i):
    pass # do nothing

cv2.namedWindow('filter')

cv2.createTrackbar("ON/OFF","filter", 0, 1, myfunc)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while(True):
    ret, frame = cap.read()
    lf=np.array([[0,1,0],
                [1,-4,1],
                [0,1,0]])
    v=cv2.getTrackbarPos("ON/OFF","filter")
    cv2.imshow('filter',frame)
    if v==1:
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        lframe=convolve(gray,lf)
        frame=lframe
        cv2.imshow('filter',frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
