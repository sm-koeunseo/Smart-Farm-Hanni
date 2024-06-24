import RPi.GPIO as GPIO
import time
import random

# Define motor pins
MOTER_A_A1 = 17
MOTER_A_B1 = 27
MOTER_B_A1 = 22
MOTER_B_B1 = 23

MOTER_C_A1 = 12  # New motor C
MOTER_C_B1 = 16  # New motor C
MOTER_D_A1 = 20  # New motor D
MOTER_D_B1 = 21  # New motor D

# Setup GPIO mode and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(MOTER_A_A1, GPIO.OUT)
GPIO.setup(MOTER_A_B1, GPIO.OUT)
GPIO.setup(MOTER_B_A1, GPIO.OUT)
GPIO.setup(MOTER_B_B1, GPIO.OUT)
GPIO.setup(MOTER_C_A1, GPIO.OUT)  # Setup new motor C
GPIO.setup(MOTER_C_B1, GPIO.OUT)  # Setup new motor C
GPIO.setup(MOTER_D_A1, GPIO.OUT)  # Setup new motor D
GPIO.setup(MOTER_D_B1, GPIO.OUT)  # Setup new motor D

# Setup PWM for the motors
MOTER_A_A1_PWM = GPIO.PWM(MOTER_A_A1, 20)
MOTER_B_A1_PWM = GPIO.PWM(MOTER_B_A1, 20)
MOTER_C_A1_PWM = GPIO.PWM(MOTER_C_A1, 20)  # New motor C PWM
MOTER_D_A1_PWM = GPIO.PWM(MOTER_D_A1, 20)  # New motor D PWM

MOTER_A_A1_PWM.start(0)
MOTER_B_A1_PWM.start(0)
MOTER_C_A1_PWM.start(0)  # Start new motor C PWM
MOTER_D_A1_PWM.start(0)  # Start new motor D PWM

# Functions to set motor directions
def set_motor_a_direction(forward):
    if forward:
        GPIO.output(MOTER_A_A1, GPIO.HIGH)
        GPIO.output(MOTER_A_B1, GPIO.LOW)
    else:
        GPIO.output(MOTER_A_A1, GPIO.LOW)
        GPIO.output(MOTER_A_B1, GPIO.HIGH)

def set_motor_b_direction(forward):
    if forward:
        GPIO.output(MOTER_B_A1, GPIO.HIGH)
        GPIO.output(MOTER_B_B1, GPIO.LOW)
    else:
        GPIO.output(MOTER_B_A1, GPIO.LOW)
        GPIO.output(MOTER_B_B1, GPIO.HIGH)

def set_motor_c_direction(forward):
    if forward:
        GPIO.output(MOTER_C_A1, GPIO.HIGH)
        GPIO.output(MOTER_C_B1, GPIO.LOW)
    else:
        GPIO.output(MOTER_C_A1, GPIO.LOW)
        GPIO.output(MOTER_C_B1, GPIO.HIGH)

def set_motor_d_direction(forward):
    if forward:
        GPIO.output(MOTER_D_A1, GPIO.HIGH)
        GPIO.output(MOTER_D_B1, GPIO.LOW)
    else:
        GPIO.output(MOTER_D_A1, GPIO.LOW)
        GPIO.output(MOTER_D_B1, GPIO.HIGH)

# Function to start motors
def start_motors():
    set_motor_a_direction(True)
    set_motor_b_direction(True)
    set_motor_c_direction(True)
    set_motor_d_direction(True)
    duty = 100
    MOTER_A_A1_PWM.ChangeDutyCycle(duty)
    MOTER_B_A1_PWM.ChangeDutyCycle(duty)
    MOTER_C_A1_PWM.ChangeDutyCycle(duty)
    MOTER_D_A1_PWM.ChangeDutyCycle(duty)

# Function to stop motors
def stop_motors():
    duty = 0
    MOTER_A_A1_PWM.ChangeDutyCycle(duty)
    MOTER_B_A1_PWM.ChangeDutyCycle(duty)
    MOTER_C_A1_PWM.ChangeDutyCycle(duty)
    MOTER_D_A1_PWM.ChangeDutyCycle(duty)

try:
    while True:
        # Generate virtual temperature data
        temp = random.randint(1, 36)
        print(f"Current temperature: {temp}占쏙옙C")
        
        # Control motors based on temperature
        if temp >= 26:
            start_motors()
        else:
            stop_motors()
        
        time.sleep(30)  # Update every minute

finally:
    MOTER_A_A1_PWM.stop()
    MOTER_B_A1_PWM.stop()
    MOTER_C_A1_PWM.stop()
    MOTER_D_A1_PWM.stop()
    GPIO.cleanup()
