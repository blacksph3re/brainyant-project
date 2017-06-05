#!flask/bin/python
from flask import Flask, Response
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
pin = 8
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.LOW)


app = Flask(__name__)

@app.route('/backend')
def backend():
    print("Pulling up")
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    print("Pulling down")
    GPIO.output(pin, GPIO.LOW)
    return "Successfully triggered"

@app.route('/')
def index():
    return Response(open("index.html").read(), mimetype="text/html")


if __name__ == '__main__':
    app.run(host="::", port=8080, debug=True)