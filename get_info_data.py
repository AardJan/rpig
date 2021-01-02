import time
from configparser import ConfigParser

import adafruit_dht
import adafruit_mcp3xxx.mcp3008 as MCP
import board
import busio
import digitalio
import RPi.GPIO as GPIO
from adafruit_mcp3xxx.analog_in import AnalogIn

import helper as h

config = ConfigParser()
config.read("settings.ini")
PIN_TEMP = config.get("pins", "pin_thermometer")
PIN_SM_SENSOR = config.get("pins", "pin_mcp_SM_sensor")
SM_VOLTAGE_ROUND = config.getint("settings", "v_round")

dht = adafruit_dht.DHT22(h.get_pin_board(PIN_TEMP))
spi = busio.SPI(clock=board.SCK,MISO=board.MISO,
                MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.CE0)
mcp = MCP.MCP3008(spi, cs)
chan = AnalogIn(mcp, h.get_pin_MCP(PIN_SM_SENSOR))

def get_temp_and_humidity():
    correct = False
    while not correct:
        try:
            temperature = dht.temperature
            humidity = dht.humidity
            correct = True
            return temperature, humidity
        except RuntimeError as e:
            # Reading doesn't always work! Just print error and we'll try again
            print("Reading from DHT failure: ", e.args)


def get_soil_moisture():
    return round(chan.voltage, SM_VOLTAGE_ROUND)
