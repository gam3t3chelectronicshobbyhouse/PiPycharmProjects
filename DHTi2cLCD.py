
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import I2C_LCD_driver

GPIO.setmode(GPIO.BCM)  ##you can use GPIO.BOARD  instead to use the actual pin number 1-40##
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)i2

mylcd = I2C_LCD_driver.lcd()


DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 17  ##GPIO17 or Pin 11


while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is None or temperature is None:
        mylcd.lcd_display_string("Sensor failure.", 2);
        mylcd.lcd_display_string("I2C LCD & DHT11", 3)
        mylcd.lcd_display_string("Gam3t3ch Electronics", 4)
        print("Sensor failure. Check wiring.");
        GPIO.output(18, GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(18, GPIO.LOW)


    else:
        mylcd.lcd_display_string("T={0:0.1f}C H={1:0.1f}%".format(temperature, humidity), 1)
        mylcd.lcd_display_string("Sensor OK!     ", 2)
        time.sleep(1)
        mylcd.lcd_display_string("I2C LCD & DHT11", 3)
        mylcd.lcd_display_string("Gam3t3ch Electronics", 4)
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        GPIO.output(18, GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(18, GPIO.LOW)
        time.sleep(.5)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(.5)
        GPIO.output(18, GPIO.LOW)
        time.sleep(.5)
    time.sleep(10);

