'''
Created on 5 avr. 2016

@author: Emmanuel
'''

    
import socket
import time
import cv2
import TreatmentFunctions as tf

if socket.gethostname() == "comput1":
    print "je tourne sur le PC"
    image = cv2.imread('../resources/images/face.jpg')
    cv2.imshow('Capture',image)
    cv2.waitKey(0)
    tf.faceDetection(image)
    cv2.imshow('Capture',image)
    cv2.waitKey(0)
else:
    from picamera.array import PiRGBArray
    from picamera import PiCamera
    
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 15
    rawCapture = PiRGBArray(camera, size=(640,480))

    time.sleep(0.1)
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        tf.faceDetection(image)
        cv2.imshow('Capture',image)
        rawCapture.truncate(0)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break