import RPi.GPIO as GPIO
import spidev
import time
import statistics

# pin number
MOTER_A_A1 = 17
MOTER_A_B1 = 27
MOTER_B_A1 = 22
MOTER_B_B1 = 23

MOTER_C_A1 = 12  # New motor C
MOTER_C_B1 = 16  # New motor C
MOTER_D_A1 = 20  # New motor D
MOTER_D_B1 = 21  # New motor D

pump1R = 5
pump1B = 6
pump2R = 13
pump2B = 19

guage = 26

outlet = 18

# GPIO Settings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(MOTER_A_A1, GPIO.OUT)
GPIO.setup(MOTER_A_B1, GPIO.OUT)
GPIO.setup(MOTER_B_A1, GPIO.OUT)
GPIO.setup(MOTER_B_B1, GPIO.OUT)
GPIO.setup(MOTER_C_A1, GPIO.OUT)  # Setup new motor C
GPIO.setup(MOTER_C_B1, GPIO.OUT)  # Setup new motor C
GPIO.setup(MOTER_D_A1, GPIO.OUT)  # Setup new motor D
GPIO.setup(MOTER_D_B1, GPIO.OUT)  # Setup new motor D

GPIO.setup(pump1R, GPIO.OUT)
GPIO.output(pump1R, GPIO.LOW)
GPIO.setup(pump1B, GPIO.OUT)
GPIO.output(pump1B, GPIO.LOW)
GPIO.setup(pump2R, GPIO.OUT)
GPIO.output(pump2R, GPIO.LOW)
GPIO.setup(pump2B, GPIO.OUT)
GPIO.output(pump2B, GPIO.LOW)

GPIO.setup(guage, GPIO.IN)

GPIO.setup(outlet, GPIO.OUT)
GPIO.output(outlet, GPIO.LOW)

# Open Spi Bus
# SPI bus and device
# max speed 1MHz
spi = spidev.SpiDev()

# check spi pin num (ls /dev/spi*)
spi.open(0,0) # open(bus, device)
spi.max_speed_hz = 500000 # set transfer speed

# To read SPI data from MCP3208 chip
# Channel must be 0~7 integer
def readChannel1(channel):
  buff=spi.xfer2([1,(8+channel)<<4,0])
  adcValue=((buff[1]&3)<<8)+buff[2]
  return adcValue

def readChannel2(channel):
  val = spi.xfer2([6, (channel) >> 2, (channel & 3) << 6, 0])
  data = ((val[1]&15) << 8) + val[2]
  return data

# def fMotor():
#   GPIO.output(pump1R, GPIO.HIGH)
#   GPIO.output(pump1B, GPIO.LOW)
#   GPIO.output(pump2R, GPIO.HIGH)
#   GPIO.output(pump2B, GPIO.LOW)
#   time.sleep(1)

#   GPIO.output(pump1R, GPIO.LOW)
#   GPIO.output(pump1B, GPIO.LOW)
#   GPIO.output(pump2R, GPIO.LOW)
#   GPIO.output(pump2B, GPIO.LOW)
#   time.sleep(1)

def fMoisture():
  print("val1:", readChannel1(1))
  print("val2:", readChannel1(2))
  print("val3:", readChannel1(3))

def fGuage():
  print(GPIO.input(guage))

def fLED():
  GPIO.output(outlet,True)
  time.sleep(5)
  GPIO.output(outlet,False)

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

# Setup PWM for the motors
MOTER_A_A1_PWM = GPIO.PWM(MOTER_A_A1, 20)
MOTER_B_A1_PWM = GPIO.PWM(MOTER_B_A1, 20)
MOTER_C_A1_PWM = GPIO.PWM(MOTER_C_A1, 20)  # New motor C PWM
MOTER_D_A1_PWM = GPIO.PWM(MOTER_D_A1, 20)  # New motor D PWM

MOTER_A_A1_PWM.start(0)
MOTER_B_A1_PWM.start(0)
MOTER_C_A1_PWM.start(0)  # Start new motor C PWM
MOTER_D_A1_PWM.start(0)  # Start new motor D PWM

def start():
  set_motor_a_direction(True)
  set_motor_b_direction(True)
  set_motor_c_direction(True)
  set_motor_d_direction(True)
  duty = 100
  MOTER_A_A1_PWM.ChangeDutyCycle(duty)
  MOTER_B_A1_PWM.ChangeDutyCycle(duty)
  MOTER_C_A1_PWM.ChangeDutyCycle(duty)
  MOTER_D_A1_PWM.ChangeDutyCycle(duty)

  GPIO.output(pump1R, GPIO.HIGH)
  GPIO.output(pump1B, GPIO.LOW)
  GPIO.output(pump2R, GPIO.HIGH)
  GPIO.output(pump2B, GPIO.LOW)

  GPIO.output(outlet,True)

  time.sleep(10)

  duty = 0
  MOTER_A_A1_PWM.ChangeDutyCycle(duty)
  MOTER_B_A1_PWM.ChangeDutyCycle(duty)
  MOTER_C_A1_PWM.ChangeDutyCycle(duty)
  MOTER_D_A1_PWM.ChangeDutyCycle(duty)

  GPIO.output(pump1R, GPIO.LOW)
  GPIO.output(pump1B, GPIO.LOW)
  GPIO.output(pump2R, GPIO.LOW)
  GPIO.output(pump2B, GPIO.LOW)

  GPIO.output(outlet,False)

  MOTER_A_A1_PWM.stop()
  MOTER_B_A1_PWM.stop()
  MOTER_C_A1_PWM.stop()
  MOTER_D_A1_PWM.stop()
  GPIO.cleanup()

start()

# try:
#   fMotor()
#   time.sleep(1)
#   fMoisture()
#   time.sleep(1)
#   fGuage()
#   time.sleep(1)
#   fLED()

# except KeyboardInterrupt:
#     GPIO.cleanup()