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

# --- Camera HUSKYLENS
import random
import time
import json
from huskylib import HuskyLensLibrary
hl = HuskyLensLibrary("I2C","", address=0x32)

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level=logging.DEBUG)

# Ανάγνωση Αρχείου Αποφθεγμάτων
df = pd.read_csv('motos.csv')

now = datetime.now() # Μεταβλητή σ ημερινής Ημερομηνίας
today = now.strftime("%d/%m/%Y") # Μετατροπή σε οικία μορφή


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
    iris = Image.new("RGB", (disp.width, disp.height), "BLACK")
    drawIris = ImageDraw.Draw(blackeyes)
    font18 = ImageFont.truetype("../Font/Font00.ttf",18) 
    drawIris.rectangle((35,35,65,65), fill = "WHITE")
    drawIris.rectangle((55,45,65,55), fill = (0,0,0)) # Stroggyla
    drawIris.rectangle((95,35,125,65), fill = "WHITE")
    drawIris.rectangle((115,45,125,55), fill = (0,0,0)) # Stroggyla
    drawIris.arc((65,85,95,105),0, 180, fill ="WHITE",width = 5)
    disp.ShowImage(iris)
    time.sleep(1)

def printLookLeft():
    iris = Image.new("RGB", (disp.width, disp.height), "BLACK")
    drawBlackEyes = ImageDraw.Draw(blackeyes)
    font18 = ImageFont.truetype("../Font/Font00.ttf",18) 
    drawIris.rectangle((35,35,65,65), fill = "WHITE")
    drawIris.rectangle((35,45,45,55), fill = (0,0,0)) # Stroggyla
    drawIris.rectangle((95,35,125,65), fill = "WHITE")
    drawIris.rectangle((95,45,105,55), fill = (0,0,0)) # Stroggyla
    drawIris.arc((65,85,95,105),0, 180, fill ="WHITE",width = 5)
    disp.ShowImage(iris)
    time.sleep(1)
   

def printMotto(): # Ερώτηση Σημερινής Υποχρέωσης-Απόκριση-Αυριανό Πρόγραμμα
        
    Font0 = ImageFont.truetype("../Font/Font00.ttf",18)
    
    msg = Image.new("RGB", (disp.width, disp.height), "BLACK")
    drawMsg = ImageDraw.Draw(msg)
    
    random.seed()
    i = random.randint(1,20)

    thisMsg = df['motos'][i]
    drawMsg.text((0, 0), thisDayMsg, fill = "WHITE",font=Font0)
    disp.ShowImage(msg)
    time.sleep(5)
    
try:
    disp = LCD_1inch8.LCD_1inch8()
    Lcd_ScanDir = LCD_1inch8.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
    disp.Init()
    disp.clear()
    disp.bl_DutyCycle(50)
    
    while(True):
        printEyes()    
        printLookRight()
        printEyes()    
        printLookLeft()
        printEyes()    
        printBlink()   
        printEyes()    
        printMotto()
        
    disp.module_exit()
    
except IOError as e:
    logging.info(e)    
except KeyboardInterrupt:
    disp.module_exit()
    exit()
