import Adafruit_DHT as dht
import spidev
import time
import RPi.GPIO as GPIO

DO_PIN = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(DO_PIN, GPIO.IN)

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=1260870

def analog_read_3208(channel):
    r = spi.xfer2([4 | 2 |(channel>>2), (channel &3) << 6,0])    
    adc_out = ((r[1]&15) << 8) + r[2]
    return adc_out

# def Water_DO_callback(channel):
#     reading = analog_read_3208(channel)
#     Water_Percentage = map(reading, 4095, 1500, 0, 100)
#     print("water : %0.1f" % (Water_Percentage))    
# GPIO.add_event_detect(DO_PIN, GPIO.FALLING,
#                       callback=Water_DO_callback, bouncetime=10)

def map(x, in_min, in_max, out_min, out_max):
    out_val = (((x - in_min) * (out_max - out_min)) / (in_max - in_min)) + out_min
    return out_val

try:
    while True:
        print(time.strftime("%Y/%m/%d %H:%M:%S"))
        
        reading = analog_read_3208(1)     # read Channel 1
        voltage = reading * 3.3 / 4096    # MCP3208: 12bit
        print("MCP3208: Reading=%d\tVoltage=%f" % (reading, voltage)) 

        Water_Percentage = map(reading, 4095, 1360, 0, 100)
        print("Water%%: %0.1f\n" % (Water_Percentage))         
        
        time.sleep(2)                                               #10�� ���� ����

except RuntimeError:
    pass

finally:
    GPIO.cleanup()
