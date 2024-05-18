import RPi.GPIO as GPIO
import time

# define
motor1 = 5
motor2 = 6

# GPIO Settings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1, GPIO.OUT)
GPIO.output(motor1, GPIO.LOW)
GPIO.setup(motor2, GPIO.OUT)
GPIO.output(motor2, GPIO.LOW)

while True:
    GPIO.output(motor1, GPIO.HIGH)
    GPIO.output(motor2, GPIO.LOW)
    time.sleep(1)
    GPIO.output(motor1, GPIO.LOW)
    GPIO.output(motor2, GPIO.LOW)
    time.sleep(1)

