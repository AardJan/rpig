import time
from configparser import ConfigParser

import adafruit_dht
import board
import RPi.GPIO as GPIO
import helper as h


config = ConfigParser()
config.read("settings.ini")
PIN_TEMP = config.get("pins", "pin_thermometer")

dht = adafruit_dht.DHT22(h.get_pin_board(PIN_TEMP))

while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        print(f"Temp {temperature} C \t Humitity: {humidity}%")
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)

    time.sleep(10)
