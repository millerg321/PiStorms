from PiStorms import PiStorms
import os
import inspect
import time

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)

# starts an instance of PiStorms
psm = PiStorms()

# exit variable will be used later to exit the program and return to PiStorms
exit_program = False

psm.screen.clearScreen()
psm.screen.termPrintln("")
psm.screen.termPrintln("Driving Ms Daisy")

count = 0
while not exit_program:

    # rightMultiple = psm.BAS1.remoteRight(1)
    # leftMultiple = psm.BAS1.remoteLeft(1)
    distanceRemote = psm.BAS1.distanceRemoteIREV3(1)
    headingRemote = psm.BAS1.headingIREV3(1)

    # if rightMultiple == 0:
    #     psm.BBM1.float()
    # elif rightMultiple:
    #     psm.BBM1.setSpeed(rightMultiple * -80)
    # if leftMultiple == 0:
    #     psm.BAM1.float()
    # elif leftMultiple:
    #     psm.BAM1.setSpeed(leftMultiple * -80)
    #
    # psm.screen.termPrintAt(3, "Left Reading " + str(leftMultiple))
    # psm.screen.termPrintAt(4, "Right Reading " + str(rightMultiple))
    psm.screen.termPrintAt(5, "Distance Reading " + str(distanceRemote))
    psm.screen.termPrintAt(6, "Heading Reading " + str(headingRemote))

    time.sleep(.1)

    if psm.isKeyPressed():
        psm.screen.clearScreen()
        psm.screen.termPrintln("") 
        psm.screen.termPrintln("Exiting to menu")
        time.sleep(0.5)
        exit_program = True
