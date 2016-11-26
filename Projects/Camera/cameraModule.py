import picamera
import time
import os
import inspect

def take_photo(location = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))):
    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture(location + '/' + 'imgTest.png', format='png')
