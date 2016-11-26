import picamera
import os
import inspect
import time
from PiStorms  import PiStorms

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

psm = PiStorms()
exit = False

psm.screen.clearScreen()
psm.screen.termPrintln("")
psm.screen.termPrintln("Photo Test x3")


count = 0

while not exit and count < 3:
    
    psm.screen.clearScreen()
    psm.screen.termPrintln("Taking Photo " +  str(count+1))

    with picamera.PiCamera() as camera:
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        camera.capture(currentdir+'/'+'im2.png',format='png')
        psm.screen.clearScreen()
        psm.screen.fillBmp(30, 0, 240, 240, path=currentdir+'/'+"im2.png")
    count += 1
    time.sleep(5)
    if psm.isKeyPressed():
        psm.screen.clearScreen()
        psm.screen.termPrintln("") 
        psm.screen.termPrintln("Exiting to menu")
        time.sleep(0.5) 
        exit = True
