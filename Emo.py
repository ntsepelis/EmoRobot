#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_1inch8
from PIL import Image,ImageDraw,ImageFont

from datetime import datetime
import pandas as pd

# --- CAMERA START

import random
import time
import json
from huskylib import HuskyLensLibrary

hl = HuskyLensLibrary("I2C","", address=0x32)

# Ανάγνωση Αρχείου Ημερολογίου
# Ο τύπος της μεταβλητής είναι DataFrame
df = pd.read_csv('cal.csv')

# Εμφάνιση των Περιεχομένων του Αρχείου
print("\n----- Υποχρεώσεις -----\n") # Τίτλος
print(df) # Περιεχόμενα 


now = datetime.now() # Μεταβλητή σ ημερινής Ημερομηνίας
today = now.strftime("%d/%m/%Y") # Μετατροπή σε οικία μορφή
print("\nΣήμερα:",today) # Εμφάνιση σημερινής Ημερομηνίας
print() # Αλλαγή Σειράς


# Ερώτηση σημερινής υποχρέωσης
# Εμφάνιση αυριανών υποχρεώσεων
for i in range(len(df)):
    day = df['Ημερομηνία'][i]
    #print("Today: " + dates)
    if (day == today):
        print(df['Υποχρέωση'][i] +" σήμερα! Πώς τα πήγες;")
        if (i + 1 < len(df)):
            print("\n- Ετοιμάστηκες για το αυριανό " + df['Υποχρέωση'][i+1] +";")
        

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)

def printBlink():
    blink = Image.new("RGB", (disp.width, disp.height), "BLACK")
    drawBlink = ImageDraw.Draw(blink)
    drawBlink.line([(35, 50),(65,50)], fill = "WHITE",width = 5)
    drawBlink.line([(95, 50),(125,50)], fill = "WHITE",width = 5)
    #drawBlink.arc((35,85,125,105),0, 180, fill =(0,255,0))
    drawBlink.arc((65,85,95,105),0, 180, fill ="WHITE",width = 5)
    disp.ShowImage(blink)
    time.sleep(1)

def printEyes():
    eyes = Image.new("RGB", (disp.width, disp.height), "BLACK")
    drawEyes = ImageDraw.Draw(eyes)
    font18 = ImageFont.truetype("../Font/Font00.ttf",18) 
    drawEyes.rectangle((35,35,65,65), fill = "WHITE")
    drawEyes.rectangle((45,45,55,55), fill = (0,0,0)) # Stroggyla
    drawEyes.rectangle((95,35,125,65), fill = "WHITE")
    drawEyes.rectangle((105,45,115,55), fill = (0,0,0)) # Stroggyla
    drawEyes.arc((65,85,95,105),0, 180, fill ="WHITE",width = 5)
    disp.ShowImage(eyes)
    time.sleep(2)

def printLookRight():
    blackeyes = Image.new("RGB", (disp.width, disp.height), "BLACK")
    drawBlackEyes = ImageDraw.Draw(blackeyes)
    font18 = ImageFont.truetype("../Font/Font00.ttf",18) 
    drawBlackEyes.rectangle((35,35,65,65), fill = "WHITE")
    drawBlackEyes.rectangle((55,45,65,55), fill = (0,0,0)) # Stroggyla
    drawBlackEyes.rectangle((95,35,125,65), fill = "WHITE")
    drawBlackEyes.rectangle((115,45,125,55), fill = (0,0,0)) # Stroggyla
    drawBlackEyes.arc((65,85,95,105),0, 180, fill ="WHITE",width = 5)
    disp.ShowImage(blackeyes)
    time.sleep(1)

def printLookLeft():
    blackeyes = Image.new("RGB", (disp.width, disp.height), "BLACK")
    drawBlackEyes = ImageDraw.Draw(blackeyes)
    font18 = ImageFont.truetype("../Font/Font00.ttf",18) 
    drawBlackEyes.rectangle((35,35,65,65), fill = "WHITE")
    drawBlackEyes.rectangle((35,45,45,55), fill = (0,0,0)) # Stroggyla
    drawBlackEyes.rectangle((95,35,125,65), fill = "WHITE")
    drawBlackEyes.rectangle((95,45,105,55), fill = (0,0,0)) # Stroggyla
    drawBlackEyes.arc((65,85,95,105),0, 180, fill ="WHITE",width = 5)
    disp.ShowImage(blackeyes)
    time.sleep(1)
   

def printMessage():
    now = datetime.now() # Μεταβλητή σ ημερινής Ημερομηνίας
    today = now.strftime("%d/%m/%Y") # Μετατροπή σε οικία μορφή

    todaysMessage = Image.new("RGB", (disp.width, disp.height), "BLACK")
    drawMessage = ImageDraw.Draw(todaysMessage)
    Font0 = ImageFont.truetype("../Font/Font00.ttf",30)
    drawMessage.text((0,0), today +"\n Pame\n dynata!", fill = "WHITE",font=Font0)
    disp.ShowImage(todaysMessage)
    time.sleep(5)
            
import RPi.GPIO as GPIO

def button_callback(channel):
    #GPIO.cleanup
    print("Button Pressed!")
    printMessage()
    #GPIO.cleanup
    time.sleep(2)
    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(7,GPIO.RISING,callback=button_callback)
GPIO.cleanup
    
try:
    # display with hardware SPI:
    ''' Warning!!!Don't  creation of multiple displayer objects!!! '''
    #disp = LCD_1inch8.LCD_1inch8(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
    disp = LCD_1inch8.LCD_1inch8()
    Lcd_ScanDir = LCD_1inch8.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    # Initialize library.
    disp.Init()
    # Clear display.
    disp.clear()
    #Set the backlight to 100
    disp.bl_DutyCycle(50)
    
    while(True):
        #GPIO.cleanup
        printEyes()    # eyes
        printLookRight()
        printEyes()    # eyes
        printLookLeft()
        printEyes()    # eyes
        printBlink()   # blink
        printEyes()    # eyes
        printMessage()
       
        #GPIO.cleanup
        #printSmile()
        #printSmiley()
        #printCalendar()#calendar
        
        
    disp.module_exit()
    logging.info("quit:")
    
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    logging.info("quit:")
    exit()
