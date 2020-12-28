from configparser import ConfigParser
import time
import adafruit_dht
import board

config = ConfigParser()
config.read("setting.ini")
PIN_TEMP = config.get("pins", "pin_thermometer")
PIN_WATER_PUMP = config.get("pins", "pin_water_pump")
PIN_SOIL_MOISTURE_SENSOR = config.get("pins", "pin_mcp_soil_moisture_sensor")
print(PIN_TEMP)
print(PIN_WATER_PUMP)
print(PIN_SOIL_MOISTURE_SENSOR)
