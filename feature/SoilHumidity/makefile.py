import RPi.GPIO as GPIO
import spidev
import time
import csv


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

csv_file = "./feature/SoilHumidity/soil_humidity_3_3.csv"

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([
        "Channel 0 Raw Value", "Channel 0 Converted Value",
        "Channel 1 Raw Value", "Channel 1 Converted Value",
        "Channel 2 Raw Value", "Channel 2 Converted Value"
    ])

try:
  while True:
    row_data = []

    for i in range(3):
        val = readChannel(i)
        if val != 0:
            percent_val = convertSoilPercent(val)
            row_data.extend([val, percent_val])
            print(f"Channel {i}: Raw Value = {val}, Converted Value = {percent_val}")
        else:
            row_data.extend(["no_data", "no_data"])
            print(f"Channel {i}: no data")

        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row_data)

    time.sleep(3)
except KeyboardInterrupt:
  print("Keyboard Interrupt!!!!")
finally:
   spi.close()
   GPIO.cleanup