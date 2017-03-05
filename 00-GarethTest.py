import time
from PiStorms  import PiStorms
from Projects.Camera import cameraModule

psm = PiStorms()
exit = False

psm.screen.clearScreen()
psm.screen.termPrintln("")
psm.screen.termPrintln("Photo Test x3")

count = 0

while not exit and count < 3:

    psm.screen.clearScreen()
    psm.screen.termPrintln("Taking Photo " +  str(count+1))

    cameraModule.take_photo('/home/pi/PiStormsprograms/images/', 'image01.png')
    psm.screen.clearScreen()
    psm.screen.fillBmp(30, 0, 240, 240, path='/home/pi/PiStormsprograms/images/image01.png')
    count += 1
    time.sleep(5)
    if psm.isKeyPressed():
        psm.screen.clearScreen()
        psm.screen.termPrintln("") 
        psm.screen.termPrintln("Exiting to menu")
        time.sleep(0.5) 
        exit = True
