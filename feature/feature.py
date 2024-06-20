import RPi.GPIO as GPIO
import spidev
import time
import statistics

# pin number
motorA1R = 17
motorA1B = 18
motorA2R = 22
motorA2B = 23

motorB1R = 12
motorB1B = 16
motorB2R = 20
motorB2B = 21

pump1R = 5
pump1B = 6
pump2R = 13
pump2B = 19

guage = 26

outlet = 25

# GPIO Settings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

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

def fMotor():
  GPIO.output(pump1R, GPIO.HIGH)
  GPIO.output(pump1B, GPIO.LOW)
  GPIO.output(pump2R, GPIO.HIGH)
  GPIO.output(pump2B, GPIO.LOW)
  time.sleep(1)
  GPIO.output(pump1R, GPIO.LOW)
  GPIO.output(pump1B, GPIO.LOW)
  GPIO.output(pump2R, GPIO.LOW)
  GPIO.output(pump2B, GPIO.LOW)
  time.sleep(1)

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

try:
  # fMotor()
  # time.sleep(1)
  # fMoisture()
  # time.sleep(1)
  # fGuage()
  # time.sleep(1)
  fLED()

except KeyboardInterrupt:
    GPIO.cleanup()