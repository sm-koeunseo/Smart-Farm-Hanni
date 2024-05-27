import RPi.GPIO as GPIO
import time

# define
outlet = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(outlet,GPIO.OUT)
time.sleep(1)

try:
    while True:
        GPIO.output(outlet,True)
        time.sleep(2)
        GPIO.output(outlet,False)
        time.sleep(2)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()