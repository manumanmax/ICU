'''
Created on 5 avr. 2016

@author: Emmanuel
'''

import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (100, 100)
    camera.start_preview()
    time.sleep(2)
    camera.capture('image.data', 'raw')