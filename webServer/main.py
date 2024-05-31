from flask import Flask
import RPi.GPIO as GPIO
import threading
import time
import atexit

app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

running = threading.Event()
running.set()
terminate = threading.Event()

def cleanup():
    GPIO.cleanup()
atexit.register(cleanup)

def background_task():
    while not terminate.is_set():
        running.wait()
        GPIO.output(17,True)
        time.sleep(1);
        GPIO.output(17,False)
        time.sleep(1);

@app.route('/')
def main():
    return 'Hello, World!'

@app.route('/on')
def ligthOn():
    #GPIO.output(17,True)
    running.set()
    return "Lingt On!"

@app.route('/off')
def ligthOff():
    #GPIO.output(17,False)
    running.clear()
    return "Lingt Off!"

@app.route('/stop')
def lightStop():
    running.set()
    terminate.set()
    bg_thread.join()
    return "background thread stopped"

bg_thread = threading.Thread(target=background_task)
# bg_thread.daemon = True
# bg_thread.start()



if __name__ == '__main__':
    app.debug = True
    app.run(host="127.0.0.1", port="3000")