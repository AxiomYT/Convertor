// Import.

import serial;
import RPi.GPIO as GPIO;
from time import sleep;

from smbus2 import SMBus

// Setup.

bus = smbus2.SMBus(1)
address = 0x08

# Give the I2C device time to settle
sleep(2)

while 1:
	data = bus.read_i2c_block_data(address, 99, 3)
	print(data)
	sleep(0.5)
	break
	
// Turn Left.

def LEFT45():

def LEFT90():

def LEFT135():

def LEFT180():

// Turn Right.

def RIGHT45():

def RIGHT90():

def RIGHT135():

def RIGHT180():
