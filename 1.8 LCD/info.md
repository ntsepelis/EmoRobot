# 1.8 inch OLED

## ΕΙΣΑΓΩΓΗ
### Προδιαγραφές

- Τάση Λειτουργίας: 3.3V/5V (όταν χρησιμοποιούνται τα 5V, το λογικό 1 είναι τα 5V, ενώ όταν χρησιμοποιούνται τα 3.3V, το λογικό 1 είναι τα 3.3V)
- Διασύνδεση: SPI
- Τύπος LCD: TFT
- Πρόγραμμα Οδήγησης: ST7735S
- Ανάλυση: 128 x 160 (Pixel)
- Μέγεθος Οθόνης: 35.04mm x 28.03mm (Πλάτος x Ύψος)
- Μέγεθος Pixel: 0.219mm * 0.219mm (Πλάτος x Ύψος)
- Διάσταση: 56.5mm x 34mm

## ΠΕΡΙΓΡΑΦΗ ΔΙΑΤΑΞΗΣ

### Raspberry Pi hardware connection

Please connect the LCD to your Raspberry Pi by the 8PIN cable according to the table below.
Use the pin header or PH2.0 8PIN interface, you need to connect according to the following table.
Connect to Raspberry Pi
LCD	Raspberry Pi
	BCM2835	Board
VCC	3.3V	3.3V
GND	GND	GND
DIN	MOSI	19
CLK	SCLK	23
CS	CE0	24
DS	25	22
RST	27	13
BL	18	12
The 1.8inch LCD uses the PH2.0 8PIN interface, which can be connected to the Raspberry Pi according to the above table: (Please connect according to the pin definition table. The color of the wiring in the picture is for reference only, and the actual color shall prevail.)
 
Working with Raspberry Pi
Enable SPI interface
PS: If you are using the system of the Bullseye branch, you need to change "apt-get" to "apt", the system of the Bullseye branch only supports Python3. 
Open terminal, use command to enter the configuration page
sudo raspi-config
Choose Interfacing Options -> SPI -> Yes  to enable SPI interface
 
 
 
Reboot Raspberry Pi：
sudo reboot
Please make sure the SPI is not occupied by other devices, you can check in the middle of /boot/config.txt
Install Library
If you use bookworm system, only the lgpio library is available, bcm2835 and wiringPi libarary cannot be installed or used. Please note that the python library does not need to install, you can directly run the demo. 
BCM2835
#Open the Raspberry Pi terminal and run the following command
wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.71.tar.gz
tar zxvf bcm2835-1.71.tar.gz 
cd bcm2835-1.71/
sudo ./configure && sudo make && sudo make check && sudo make install
# For more, you can refer to the official website at: http://www.airspayce.com/mikem/bcm2835/
WiringPi
#Open the Raspberry Pi terminal and run the following command
cd
sudo apt-get install wiringpi
#For Raspberry Pi systems after May 2019 (earlier than that can be executed without), an upgrade may be required:
wget https://project-downloads.drogon.net/wiringpi-latest.deb
sudo dpkg -i wiringpi-latest.deb
gpio -v
# Run gpio -v and version 2.52 will appear, if it doesn't it means there was an installation error

# Bullseye branch system using the following command:
git clone https://github.com/WiringPi/WiringPi
cd WiringPi
. /build
gpio -v
# Run gpio -v and version 2.70 will appear, if it doesn't it means there was an installation error
lgpio
wget https://github.com/joan2937/lg/archive/master.zip
unzip master.zip
cd lg-master
sudo make install 
#for more details, you can refer to https://github.com/gpiozero/lg
Python
sudo apt-get update
sudo apt-get install python3-pip
sudo apt-get install python3-pil
sudo apt-get install python3-numpy
sudo pip3 install spidev
Download Examples
Open the Raspberry Pi terminal and run the following command:
sudo apt-get install unzip -y
sudo wget https://files.waveshare.com/upload/8/8d/LCD_Module_RPI_code.zip
sudo unzip ./LCD_Module_RPI_code.zip 
cd LCD_Module_RPI_code/RaspberryPi/
Run the demo codes
Please go into the RaspberryPi directory (demo codes) first and run the commands in the terminal.
C codes
Re-compile the demo codes.
cd c
sudo make clean
sudo make -j 8
The test demo of all screens can be called directly by entering the corresponding size:
sudo ./main Screen Size
Depending on the LCD, one of the following commands should be entered: 
#0.96inch LCD Module
sudo ./main 0.96
#1.14inch LCD Module
sudo ./main 1.14
#1.28inch LCD Module
sudo ./main 1.28
#1.3inch LCD Module
sudo ./main 1.3
#1.47inch LCD Module
sudo ./main 1.47
#1.54inch LCD Module
sudo ./main 1.54
#1.8inch LCD Module
sudo ./main 1.8
#2inch LCD Module
sudo ./main 2
#2.4inch LCD Module
sudo ./main 2.4
python
Enter the Python program directory and run the command ls -l.
cd python/examples
ls -l
 
Test programs for all screens can be viewed, sorted by size:
0inch96_LCD_test.py: 0.96inch LCD test program
1inch14_LCD_test.py: 1.14inch LCD test program
1inch28_LCD_test.py: 1.28inch LCD test program
1inch3_LCD_test.py: 1.3inch LCD test program
1inch47_LCD_test.py: 1.47inch LCD test program
1inch54_LCD_test.py: 1.54inchLCD test program
1inch8_LCD_test.py: 1.8inch LCD test program
2inch_LCD_test.py: 2inch LCD test program
2inch4_LCD_test.py: 2inch4 LCD test program
Just run the program corresponding to the screen, the program supports python2/3.
# python2
sudo python 0inch96_LCD_test.py
sudo python 1inch14_LCD_test.py
sudo python 1inch28_LCD_test.py
sudo python 1inch3_LCD_test.py
sudo python 1inch47_LCD_test.py
sudo python 1inch54_LCD_test.py
sudo python 1inch8_LCD_test.py
sudo python 2inch_LCD_test.py
sudo python 2inch4_LCD_test.py
# python3
sudo python3 0inch96_LCD_test.py
sudo python3 1inch14_LCD_test.py
sudo python3 1inch28_LCD_test.py
sudo python3 1inch3_LCD_test.py
sudo python3 1inch47_LCD_test.py
sudo python3 1inch54_LCD_test.py
sudo python3 1inch8_LCD_test.py
sudo python3 2inch_LCD_test.py
sudo python3 2inch4_LCD_test.py

API Description
The RaspberryPi series can share a set of programs, because they are all embedded systems, and the compatibility is relatively strong.
The program is divided into bottom-layer hardware interface, middle-layer LCD screen driver, and upper-layer application; 
Python (for Raspberry Pi)
Works with python and python3.
For python, his calls are not as complicated as C.
Raspberry Pi: RaspberryPi\python\lib\
 
lcdconfig.py
Module initialization and exit processing.
def module_init()
def module_exit()
Note:
1. Here is some GPIO processing before and after using the LCD screen.
2. The module_init() function is automatically called in the INIT () initializer on the LCD, but the module_exit() function needs to be called by itself.
GPIO read and write:
def  digital_write(pin, value)
def  digital_read(pin)
SPI write data.
def spi_writebyte(data)
xxx_LCD_test.py (xxx indicates the size, if it is a 0.96inch LCD, it is 0inch96_LCD_test.py, and so on)
python is in the following directory:
Raspberry Pi: RaspberryPi\python\examples\ 
 
If your python version is python2 and you need to run the 0.96inch LCD test program, re-execute it as follows in linux command mode: 
sudo python 0inch96_LCD_test.py
If your python version is python3 and you need to run the 0.96inch LCD test program, re-execute the following in linux command mode: 
sudo python3 0inch96_LCD_test.py
About Rotation Settings
If you need to set the screen rotation in the python program, you can set it by the statement im_r= image1.rotate(270). 
im_r= image1.rotate(270)
Rotation effect, take 1.54 as an example, the order is 0°, 90°, 180°, 270°
 
GUI Functions
Python has an image library PIL official library link, it does not need to write code from the logical layer like C and can directly call to the image library for image processing. The following will take a 1.54-inch LCD as an example, we provide a brief description of the demo. 
It needs to use the image library and install the library.
sudo apt-get install python3-pil  
And then import the library
from PIL import Image,ImageDraw,ImageFont.
Among them, Image is the basic library, ImageDraw is the drawing function, and ImageFont is the text function. 
Define an image cache to facilitate drawing, writing, and other functions on the picture.
image1 = Image.new("RGB", (disp.width, disp.height), "WHITE")
The first parameter defines the color depth of the image, which is defined as "1" to indicate the bitmap of one-bit depth. The second parameter is a tuple that defines the width and height of the image. The third parameter defines the default color of the buffer, which is defined as "WHITE". 
Create a drawing object based on Image1 on which all drawing operations will be performed on here.
draw = ImageDraw.Draw(image1)
Draw a line.
draw.line([(20, 10),(70, 60)], fill = "RED",width = 1)
The first parameter is a four-element tuple starting at (0, 0) and ending at (127,0). Draw a line. Fill ="0" means the color of the line is white. 
Draw a rectangle.
draw.rectangle([(20,10),(70,60)],fill = "WHITE",outline="BLACK")
The first argument is a tuple of four elements. (20,10) is the coordinate value in the upper left corner of the rectangle, and (70,60) is the coordinate value in the lower right corner of the rectangle. Fill =" WHITE" means BLACK inside, and outline="BLACK" means the color of the outline is black. 
Draw a circle.
draw.arc((150,15,190,55),0, 360, fill =(0,255,0)
Draw an inscribed circle in the square, the first parameter is a tuple of 4 elements, with (150, 15) as the upper left corner vertex of the square, (190, 55) as the lower right corner vertex of the square, specifying the level median line of the rectangular frame is the angle of 0 degrees, the second parameter indicates the starting angle, the third parameter indicates the ending angle, and fill = 0 indicates that the color of the line is white. If the figure is not square according to the coordination, you will get an ellipse. 
Besides the arc function, you can also use the chord function for drawing a solid circle. 
draw.ellipse((150,65,190,105), fill = 0)
The first parameter is the coordination of the enclosing rectangle. The second and third parameters are the beginning and end degrees of the circle. The fourth parameter is the fill color of the circle. 
Character.
The ImageFont module needs to be imported and instantiated: 
Font1 = ImageFont.truetype("../Font/Font01.ttf",25)
Font2 = ImageFont.truetype("../Font/Font01.ttf",35)
Font3 = ImageFont.truetype("../Font/Font02.ttf",32)
You can use the fonts of Windows or other fonts which is in ttc format..
Note: Each character library contains different characters; If some characters cannot be displayed, it is recommended that you can refer to the encoding set ro used. To draw English characters, you can directly use the fonts; for Chinese characters, you need to add a symbol u: 
draw.text((40, 50), 'WaveShare', fill = (128,255,128),font=Font2)
text= u"微雪电子"
draw.text((74, 150),text, fill = "WHITE",font=Font3)
The first parameter is a tuple of 2 elements, with (40, 50) as the left vertex, the font is Font2, and the fill is the font color. You can directly make fill = "WHITE", because the regular color value is already defined Well, of course, you can also use fill = (128,255,128), the parentheses correspond to the values of the three RGB colors so that you can precisely control the color you want. The second sentence shows Waveshare Electronics, using Font3, the font color is white.
read local image
image = Image.open('../pic/LCD_1inch28.jpg')
The parameter is the image path. 
Other functions.
For more information, you can refer to http://effbot.org/imagingbook pil 


