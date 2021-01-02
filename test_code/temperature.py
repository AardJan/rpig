import time
from configparser import ConfigParser

import adafruit_dht
import board
import RPi.GPIO as GPIO

dht = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        print(f"Temp {temperature} C \t Humitity: {humidity}%")
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)

    time.sleep(10)
