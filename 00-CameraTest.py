#!/usr/bin/env python
#
# Copyright (c) 2015 mindsensors.com
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.    See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
#mindsensors.com invests time and resources providing this open source code, 
#please support mindsensors.com  by purchasing products from mindsensors.com!
#Learn more product option visit us @  http://www.mindsensors.com/
#
# History:
# Date      Author      Comments
#  August 20, 2015  Andrew Miller     Initial Authoring 

from PiStorms import PiStorms
import picamera
#Demo Code for the PiStorms and Raspberry Pi


#initial setup code
import os,sys,inspect,time,thread, random
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
#sys.path.insert(0,parentdir) 
from PiStorms  import PiStorms 

#starts an instance of PiStorms 
psm = PiStorms ()

#exit variable will be used later to exit the program and return to PiStorms 
exit = False

#clears the screen of any unwanted text by displaying a white rectangle
psm.screen.fillRect(0, 0, 320, 240)

#displays Sam's greeting of "Hello, I am Sam"
psm.screen.drawAutoText("Test 1", 80, 30, fill=(255, 0, 0), size = 70)
psm.screen.drawAutoText("Lets see what this can do", 70, 140, fill=(255, 0, 0), size = 45)
psm.BBM2.runSecs(1,20,True);
psm.BAM2.runSecs(1,20,True);


#main loop
while(not exit):
    
    if(psm.BBS2.distanceUSEV3() < 200): #if ultrasonic sensor reading is <200 (~6")
        #camera = picamera.PiCamera()
	#camera.capture('image.jpg')
#	with picamera.PiCamera() as camera:
    #		camera.resolution = (1024, 768)
    #		camera.start_preview()
   #		# Camera warm-up time
    #		time.sleep(2)
    #		camera.capture('image.jpg')
	sleep(5)
        psm.screen.fillRect(0, 0, 320, 240)
        #display scared emoticon
        psm.screen.fillBmp(30, 0, 240, 240, path = currentdir+'/'+"im2.png")
        
        
        #wait one second
        time.sleep(10)
        
        #clear screen of scared emoticon
        psm.screen.fillRect(0, 0, 320, 240)
#        psm.screen.fillBmp(30, 0, 240, 240, path = currentdir+'/'+"marshmallow.png")
        time.sleep(10)
        
        
        
        
    if(psm.isKeyPressed() == True): # if the GO button is pressed
        psm.screen.clearScreen()
        psm.screen.termPrintln("") 
        psm.screen.termPrintln("Exiting to menu")
        time.sleep(0.5) 
        exit = True 
