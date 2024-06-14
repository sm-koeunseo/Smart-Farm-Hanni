import RPi.GPIO as GPIO
import time
import spidev

GPIO.setmode(GPIO.BCM)

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 50000

def read_spi_adc(adcChannel):
    adcValue = 0
    buff = spi.xfer2([1, (8+adcChannel)<<4, 0])
    adcValue = ((buff[1]&3)<<8) + buff[2]
    return adcValue

def get_moisture_level(value):
    return (value/4095.0)*100

try:
    while True:
        adcValue = read_spi_adc(1)
        print("moisture: %d, %f" % (adcValue, get_moisture_level(adcValue)))
        time.sleep(5)
finally:
    GPIO.cleanup()
    spi.close()