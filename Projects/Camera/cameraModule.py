import picamera
import time
import os
import inspect

def take_photo(location='/home/pi/PiStormsprograms/images/', imgName='image01.png'):
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture(location + imgName, format='png')
