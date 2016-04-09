'''
Created on 6 avr. 2016

@author: Emmanuel
'''
import cv2
import time

print "\n importing treatment functions :"
print "  - Face Detection"
def faceDetection(image):
    start = time.time()
    face_cascade = cv2.CascadeClassifier('../resources/classifier/haarcascade_frontalface_alt.xml')
    #eye_cascade = cv2.CascadeClassifier('../resources/classifier/haarcascade_eye.xml')
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        #eyes = eye_cascade.detectMultiScale(roi_gray)
        #for (ex,ey,ew,eh) in eyes:
            #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    print(time.time() - start)
