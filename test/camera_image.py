# camera_image.py : capture test
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()

sleep(5)

camera.capture('/pics/capture.jpg')

camera.stop_preview()