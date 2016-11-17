from PiStorms import PiStorms
import os,sys,inspect,time,thread, random
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
#sys.path.insert(0,parentdir) 

#starts an instance of PiStorms 
psm = PiStorms ()

#exit variable will be used later to exit the program and return to PiStorms 
exit = False

#clears the screen of any unwanted text by displaying a white rectangle
#psm.screen.fillRect(0, 0, 320, 240)
psm.screen.clearScreen()
#displays Sam's greeting of "Hello, I am Sam"
#psm.screen.drawAutoText("Test 1", 80, 30, fill=(255, 0, 0), size = 70)
#psm.screen.drawAutoText("Lets see what this can do", 70, 140, fill=(255, 0, 0), size = 45)
psm.screen.termPrintln("")
psm.screen.termPrintln("Lets Drive")

#psm.BBM2.runSecs(1,20,True);
#psm.BAM2.runSecs(1,20,True);

count = 0
#main loop
while(not exit and count < 3):
#	psm.BBM1.runSecs(1,20,True);
#	psm.BAM2.runSecs(1,20,True);
	count+= 1
	time.sleep(5)
        
        
    if(psm.isKeyPressed() == True): # if the GO button is pressed
        psm.screen.clearScreen()
        psm.screen.termPrintln("") 
        psm.screen.termPrintln("Exiting to menu")
        time.sleep(0.5) 
        exit = True 
