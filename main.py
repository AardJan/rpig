from configparser import ConfigParser
import time
import adafruit_dht
import board
import RPi.GPIO as GPIO

config = ConfigParser()
config.read("settings.ini")
PIN_TEMP = config.get("pins", "pin_thermometer")
PIN_WATER_PUMP = config.getint("pins", "pin_water_pump")
PIN_SOIL_MOISTURE_SENSOR = config.get("pins", "pin_mcp_soil_moisture_sensor")
WATER_TIME = config.getint("settings", "water_time")
print(PIN_WATER_PUMP)
print(PIN_TEMP)
print(PIN_SOIL_MOISTURE_SENSOR)
print("Test PUMP")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_WATER_PUMP, GPIO.OUT, initial=1)

GPIO.output(PIN_WATER_PUMP, 0)
time.sleep(WATER_TIME)
GPIO.output(PIN_WATER_PUMP, 1)
print("End test")
