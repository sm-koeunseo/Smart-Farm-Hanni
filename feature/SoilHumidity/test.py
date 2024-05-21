import RPi.GPIO as GPIO
import spidev
import time
import statistics

# define
delay = 60 * 10 # 10min
motor1 = 5
motor2 = 6

# GPIO Settings
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(motor1, GPIO.OUT)
GPIO.output(motor1, GPIO.LOW)
GPIO.setup(motor2, GPIO.OUT)
GPIO.output(motor2, GPIO.LOW)

# Open Spi Bus
# SPI bus and device
# max speed 1MHz
spi = spidev.SpiDev()

# check spi pin num (ls /dev/spi*)
spi.open(0,0) # open(bus, device)
spi.max_speed_hz = 500000 # set transfer speed

# To read SPI data from MCP3008 chip
# Channel must be 0~7 integer
def readChannel(channel):
  val = spi.xfer2([1, (8+channel)<<4, 0])
  data = ((val[1]&3) << 8) + val[2]
  return data

# 0~1023 -> 0~100%
def convertSoilPercent(data):
  return 100.0-round(((data*100)/float(1023)),1)

try:
  while True:
    humi_og = []

    for i in range(3):
        val = readChannel(i)
        if (val != 0):
            humi_og.append[convertSoilPercent(val)]
    humi = statistics.mean(val)

    if humi < 25:
        GPIO.output(motor1, GPIO.HIGH)
        GPIO.output(motor2, GPIO.LOW)
        time.sleep(60 * 2)
        GPIO.output(motor1, GPIO.LOW)
        GPIO.output(motor2, GPIO.LOW)
        time.sleep(60 * 8)

        # check the water bucket
        if readChannel(3) < 550:
            print("water lack!!")
            # push message
    else:
        time.sleep(delay)
except KeyboardInterrupt:
  spi.close()
  print("Keyboard Interrupt!!!!")