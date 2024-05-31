from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

@app.route('/')
def main():
    return 'Hello, World!'

if __name__ == '__main__':
    app.debug = True
    app.run(port="3000", host='0.0.0.0')