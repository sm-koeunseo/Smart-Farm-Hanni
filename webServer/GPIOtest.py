from flask import Flask
import RPi.GPIO as GPIO
import threading
import time
import atexit

app = Flask(__name__)

def initialize_GPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17,GPIO.OUT)

def cleanup():
    GPIO.cleanup()

atexit.register(cleanup)

@app.route('/on')
def ligthOn():
    GPIO.output(17,True)
    return "Lingt On!"

@app.route('/off')
def ligthOff():
    GPIO.output(17,False)
    return "Lingt Off!"

@app.route('/')
def main():
    return 'Hello, World!'


if __name__ == '__main__':
    initialize_GPIO()
    app.debug = True
    app.run(host="0.0.0.0", port="3000") # port open