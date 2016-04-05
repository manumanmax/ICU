'''
Created on 5 avr. 2016

@author: Emmanuel
'''


import numpy as np
import cv2

cap = cv2.VideoCapture(0)
if (cap.isOpened()):
    print "captured" 
ret, frame = cap.read()
cv2.imshow('first capture',frame)
#else
cv2.waitKey(0)
cv2.destroyAllWindows()