## will have to run  sudo pip3 install Adafruit_DHT  in terminal.
## original code https://www.thegeekpub.com/236867/using-the-dht11-temperature-sensor-with-the-raspberry-pi/
## Adjusted with LED Code by Gam3t3ch Electronics

import Adafruit_DHT
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 17  ##GPIO17 or Pin 11


while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is None or temperature is None:
        print("Sensor failure. Check wiring.");
        GPIO.output(18, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(18, GPIO.LOW)

    else:
        print("Temp={0:0.1f}C  Humidity={1:0.1f}%".format(temperature, humidity))
    time.sleep(6);
   # if temperature is
    GPIO.output(18, GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(18, GPIO.LOW)
    time.sleep(.5)
    GPIO.output(18, GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(18, GPIO.LOW)
    time.sleep(.5)



