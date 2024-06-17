import RPi.GPIO as GPIO
import spidev
import time

# unit : seconds
delay = 2

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
  val = spi.xfer2([6, (channel) >> 2, (channel & 3) << 6, 0])
  data = ((val[1]&15) << 8) + val[2]
  return data

def readChannel2(channel):
  val = spi.xfer2([6|((channel&7)>>2), ((channel&7)<<6), 0])
  data = ((val[1]&15)<<8)|val[2]
  return data

def readChannel3(channel):
  buff=spi.xfer2([1,(8+channel)<<4,0])
  adcValue=((buff[1]&3)<<8)+buff[2]
  return adcValue

# 0~1023 value? ???. 1023? ???? min?
def convertPercent(data):
  return 100.0-round(((data*100)/float(1023)),1)

# 4095
def map(x, in_min=1023, in_max=0, out_min=0, out_max=100):
    out_val = (((x - in_min) * (out_max - out_min)) / (in_max - in_min)) + out_min
    return out_val

try:
  while True:
    val = readChannel3(1)
    if (val != 0) : # filtering for meaningless num
      print(val, "/", map(val),"%")
    else:
      print("no data")
    time.sleep(delay)
except KeyboardInterrupt:
  spi.close()
  print("Keyboard Interrupt!!!!")