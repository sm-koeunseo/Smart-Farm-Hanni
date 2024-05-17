import spidev
import time

delay = 1 

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


try:
  while True:
    val = readChannel(1)
    voltage = val * 3.3 / 1024
    print("Reading=%d\tVoltage=%f" % (val, voltage))
    time.sleep(1)
except KeyboardInterrupt:
  spi.close()
  print("Keyboard Interrupt!!!!")