import os,sys,inspect,time
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from PiStorms import PiStorms

psm = PiStorms()

psm.screen.termPrintln("EV3 RemoteTest readout (BAS1):")
#psm.screen.termPrintln(" ")
#print psm.BAS1.SE_None
exit = False
while(not exit):

#    psm.screen.termPrintAt(3,"Distance: " +str(psm.BAS1.distanceRemoteIREV3(1)))
#    psm.screen.termPrintAt(4,"Heading: " + str(psm.BAS1.headingIREV3(1)))
    psm.screen.termPrintAt(3,"Right buttons: " + str(psm.BAS1.remoteRight(1)))

    psm.screen.termPrintAt(5,"Left buttons: " + str(psm.BAS1.remoteLeft(1)))
    time.sleep(.05)
#    '''
#    if psm.BAS1.remoteLeft(1)  == 1 :
#        psm.screen.termPrintAt(5,"Left Forward Pressed")
 #   if psm.BAS1.SumoEyes(True) == psm.BAS1.SE_Front :
 #       psm.screen.termPrintAt(4," SumoEyes something infront")
 #   if psm.BAS1.SumoEyes(True) == psm.BAS1.SE_Left :
 #       psm.screen.termPrintAt(4," SumoEyes something on Left")
 #   if psm.BAS1.SumoEyes(True) == psm.BAS1.SE_Right :
 #       psm.screen.termPrintAt(4," SumoEyes something on Right")
#    '''
    if(psm.screen.checkButton(0,0,320,320)):
		psm.screen.termPrintln("")
		psm.screen.termPrintln("Exiting to menu")
		exit = True
        
