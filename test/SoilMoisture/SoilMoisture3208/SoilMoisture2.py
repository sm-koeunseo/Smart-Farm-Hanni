import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1260870

CHANNEL_SOIL_MOISTURE = 0

def analog_read(channel):
    r = spi.xfer2([4 | 2 | (channel >> 2), (channel & 3) << 6, 0])
    adc_out = ((r[1] & 15) << 8) + r[2]
    return adc_out

def map(x, in_min, in_max, out_min, out_max):
    out_val = (((x - in_min) * (out_max - out_min)) / (in_max - in_min)) + out_min
    return out_val

def read_soil_moisture(channel):
    analog_value = analog_read(channel)
    soil_moisture_percentage = map(analog_value, 4095, 1500, 0, 100)
    return soil_moisture_percentage

try:
    while True:
        soil_moisture = read_soil_moisture(CHANNEL_SOIL_MOISTURE)
        print("val: {:.2f}%".format(soil_moisture))
        
        time.sleep(1)
        
except KeyboardInterrupt:
    spi.close()
