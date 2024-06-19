import RPi.GPIO as GPIO
import time

# define
motorA1_A = 5
motorA1_B = 6
motorB1_A = 13
motorB2_A = 19

# GPIO Settings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(motorA1_A, GPIO.OUT)
GPIO.output(motorA1_A, GPIO.LOW)
GPIO.setup(motorA1_B, GPIO.OUT)
GPIO.output(motorA1_B, GPIO.LOW)

GPIO.setup(motorB1_A, GPIO.OUT)
GPIO.output(motorB1_A, GPIO.LOW)
GPIO.setup(motorB2_A, GPIO.OUT)
GPIO.output(motorB2_A, GPIO.LOW)

while True:
    # GPIO.output(motorA1_A, GPIO.HIGH)
    # GPIO.output(motorA1_B, GPIO.LOW)
    # time.sleep(1)
    # GPIO.output(motorA1_A, GPIO.LOW)
    # GPIO.output(motorA1_B, GPIO.LOW)
    # time.sleep(1)
    GPIO.output(motorB1_A, GPIO.HIGH)
    GPIO.output(motorB2_A, GPIO.LOW)
    time.sleep(1)
    GPIO.output(motorB1_A, GPIO.LOW)
    GPIO.output(motorB2_A, GPIO.LOW)
    time.sleep(1)

