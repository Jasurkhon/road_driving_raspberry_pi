import cv2 as cv
import numpy as np
import math
from motor import Motors
from ultra import *


slope = 0
motor = Motors()
motor.initDCMotor()

cap = cv.VideoCapture(0)
while True:
    ret, img = cap.read()
    if ret:
        h = img.shape[0]
        w = img.shape[1]
        img = img[int(h-h/7):int(h), 0:w]
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        blur = cv.GaussianBlur(gray, (5, 5), 0)
        canny = cv.Canny(blur, 60, 130)
        linesP = cv.HoughLinesP(canny, 1, np.pi/180, 10, 5, 10)
# creating two lines in each frame after hough transform
        if(linesP is not None):
            for i in range(0, len(linesP)):
                for x1, y1, x2, y2 in linesP[i]:
                    cv.line(img,(x1,y1),(x2,y2),(0,0,255),5)
                    slope = slope+np.arctan((y2-y1)/(x2-x1))
                    
        
        if(slope>-1.8 and slope<0.3):
            motor.moveForward()
        elif(slope<=-1.8):
            motor.moveLeft()
        elif(slope>0.3):
            motor.moveRight()
        slope = 0
        if cv.waitKey(1) & 0xFF == ord("q"):
            break
    else: 
        break
cap.release()
cv.destroyAllWindows()



