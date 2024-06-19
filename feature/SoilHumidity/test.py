import RPi.GPIO as GPIO
import spidev
import time
import statistics

# define
delay = 1 #60 * 10 # 10min
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

# 0~1023 -> 0~100%
def convertSoilPercent(data):
  return 100.0-round(((data*100)/float(1023)),1)

try:
  while True:

    humi_og = []
    val = readChannel2(1)
    while not val:
       print("val1:", val)
       val = readChannel2(1)
    humi_og.append(val)
    val = readChannel2(2)
    while not val:
       print("val2:", val)
       val = readChannel2(2)
    humi_og.append(val)
    print("val1:",humi_og[0]," val2:",humi_og[1])

    if (statistics.mean(humi_og) < 720):
      GPIO.output(motorA1_A, GPIO.HIGH)
      GPIO.output(motorA1_B, GPIO.LOW)
      time.sleep(1)
      GPIO.output(motorA1_A, GPIO.LOW)
      GPIO.output(motorA1_B, GPIO.LOW)
    time.sleep(1)

    humi_og = []
    val = readChannel2(3)
    while not val:
       print("val3:", val)
       val = readChannel2(3)
    humi_og.append(val)
    val = readChannel2(4)
    while not val:
       print("val4:", val)
       val = readChannel2(4)
    humi_og.append(val)
    print("val3:",humi_og[0]," val4:",humi_og[1])

    if (statistics.mean(humi_og) < 720):
      GPIO.output(motorB1_A, GPIO.HIGH)
      GPIO.output(motorB2_A, GPIO.LOW)
      time.sleep(1)
      GPIO.output(motorB1_A, GPIO.LOW)
      GPIO.output(motorB2_A, GPIO.LOW)
    time.sleep(1)

    # check the water bucket
    if readChannel1(0) < 550:
        print("water lack!!")
        # push message

except KeyboardInterrupt:
  spi.close()
  print("Keyboard Interrupt!!!!")