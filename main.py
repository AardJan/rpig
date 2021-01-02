from configparser import ConfigParser
import time

import board
import RPi.GPIO as GPIO
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import busio
import digitalio

import helper as h

# Read config.ini
config = ConfigParser()
config.read("settings.ini")
PIN_WATER_PUMP = config.getint("pins", "pin_water_pump")
PIN_SM_SENSOR = config.get("pins", "pin_mcp_SM_sensor")
WATER_TIME = config.getint("settings", "water_time")
SM_VOLTAGE_MIN = config.getfloat("settings", "v_min")
SM_VOLTAGE_ROUND = config.getint("settings", "v_round")
SM_SLEEP_TIME = config.getint("settings", "SM_sleep_time")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_WATER_PUMP, GPIO.OUT,
            initial=1)
# Create the spi bus
spi = busio.SPI(clock=board.SCK,MISO=board.MISO,
                MOSI=board.MOSI)
# Create the cs (chip select CE0 or CE1)
cs = digitalio.DigitalInOut(board.CE0)
# Create the mcp object
mcp = MCP.MCP3008(spi, cs)
# Create an analog input channel on pin from config
chan = AnalogIn(mcp, h.get_pin_MCP(PIN_SM_SENSOR))

# Setup GPIO for water pump and init with hight value
GPIO.setup(PIN_WATER_PUMP, GPIO.OUT, initial=1)

# Set default value for soil moisture sensor, max value
voltage = round(chan.voltage, SM_VOLTAGE_ROUND)
while voltage>SM_VOLTAGE_MIN:
    GPIO.output(PIN_WATER_PUMP, 0)
    time.sleep(WATER_TIME)
    GPIO.output(PIN_WATER_PUMP, 1)
    time.sleep(SM_SLEEP_TIME)
    voltage = round(chan.voltage, SM_VOLTAGE_ROUND)
