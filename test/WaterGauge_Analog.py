import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pin = 12

GPIO.setup(pin, GPIO.IN)

try:
    while True:
        input = GPIO.input(pin)
        print(input)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()