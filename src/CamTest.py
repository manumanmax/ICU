'''
Created on 5 avr. 2016

@author: Emmanuel
'''

import numpy as np
import socket
import time

import cv2
import TreatmentFunctions as tf
import io

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
    import picamera



    #stream = io.BytesIO()
    with picamera.PiCamera() as camera:
    
        '''camera.resolution = (640, 480)
        camera.framerate = 24
        camera.start_preview()
        time.sleep(2)
        camera.capture(stream, format='jpeg')

    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    image = cv2.imdecode(data,1)
    image = image[:,:,::-1]
    cv.imshow('Capture', image)
'''
    
        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            image = frame.array
            #tf.faceDetection(image)
            cv2.imshow('Capture',image)
            rawCapture.truncate(0)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                break
'''
