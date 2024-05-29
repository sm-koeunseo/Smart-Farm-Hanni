import RPi.GPIO as GPIO
import spidev
import time

# unit : seconds
delay = 10

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

# 0~1023 value? ???. 1023? ???? min?
def convertPercent(data):
  return 100.0-round(((data*100)/float(1023)),1)

try:
  while True:
    val = readChannel(0)
    if (val != 0) : # filtering for meaningless num
      print(val, "/", convertPercent(val),"%")
    else:
      print("no data")
    time.sleep(delay)
except KeyboardInterrupt:
  spi.close()
  print("Keyboard Interrupt!!!!")