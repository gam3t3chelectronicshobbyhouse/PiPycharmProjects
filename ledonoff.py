import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)  ##you can use GPIO.BOARD  instead to use the actual pin number 1-40##
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
print("LED on")
GPIO.output(18, GPIO.HIGH)
time.sleep(1)
GPIO.output(18, GPIO.LOW)
