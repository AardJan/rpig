from configparser import ConfigParser
import time

import board
import RPi.GPIO as GPIO
import adafruit_dht
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import busio
import digitalio

# Read config.ini
config = ConfigParser()
config.read("settings.ini")
PIN_TEMP = config.get("pins", "pin_thermometer")
PIN_WATER_PUMP = config.getint("pins", "pin_water_pump")
PIN_SOIL_MOISTURE_SENSOR = config.get("pins", "pin_mcp_soil_moisture_sensor")
WATER_TIME = config.getint("settings", "water_time")

# Test iterator
i = 5
v = 0
# Test 1
print("TEST 1 PUMP")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_WATER_PUMP, GPIO.OUT, initial=1)
while v<=i:
    GPIO.output(PIN_WATER_PUMP, 0)
    time.sleep(WATER_TIME)
    GPIO.output(PIN_WATER_PUMP, 1)
    v = v + 1

v = 0
print("END TEST 1")
print("")

# Test 2
print("TEST 2 SOIL MOISTURE")
# create the spi bus
spi = busio.SPI(clock=board.SCK,
                MISO=board.MISO,
                MOSI=board.MOSI)
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.CE0)
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0)

while v<=i:
   print('Raw ADC Value: ', chan.value)
   print('ADC Voltage: ' + str(chan.voltage) + 'V')
   time.sleep(5)
   v = v + 1

v = 0
print("END TEST 2")

