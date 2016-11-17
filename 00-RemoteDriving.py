from PiStorms import PiStorms
import os,sys,inspect,time,thread, random
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)

#starts an instance of PiStorms 
psm = PiStorms ()

#exit variable will be used later to exit the program and return to PiStorms 
exit = False

psm.screen.clearScreen()
psm.screen.termPrintln("")
psm.screen.termPrintln("Driving Ms Daisy")

count = 0
#main loop
while(not exit and count < 60):
#    distanceInFront = psm.BAS1.distanceUSEV3()    
#    if distanceInFront < 15:
#        psm.BBM1.brake()
#	psm.BAM1.brake()
#	time.sleep(1)
    #elif x > 15:
#	psm.BBM1.runSecs(5,-60,True);
#	psm.BAM1.runSecs(5,-60,True);
    rightMultiple = psm.BAS1.remoteRight(1)
    leftMultiple = psm.BAS1.remoteLeft(1)
    if (rightMultiple == 0):
	   psm.BBM1.float()
    elif (rightMultiple):
#	if (rightMultiple != 0):
        psm.BBM1.setSpeed(rightMultiple*-80)
#	else:
#	    psm.BBM1.float()
    if (leftMultiple == 0):
        psm.BAM1.float()
    elif (leftMultiple):
#	if (leftMultiple != 0):
        psm.BAM1.setSpeed(leftMultiple*-80)
#	else:
#            psm.BAM1.float()
        #psm.screen.fillRect(0, 0, 320, 240)
        #display scared emoticon
#    psm.screen.clearScreen()	        
    psm.screen.termPrintAt(3,"Left Reading " +  str(leftMultiple))
    psm.screen.termPrintAt(4,"Right Reading " +  str(rightMultiple))

#    count+= 1
    time.sleep(.1)
        
        
    if(psm.isKeyPressed() == True): # if the GO button is pressed
        psm.screen.clearScreen()
        psm.screen.termPrintln("") 
        psm.screen.termPrintln("Exiting to menu")
        time.sleep(0.5) 
        exit = True 
