#!flask/bin/python
from flask import Flask, Response
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
pin = 8
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.LOW)


app = Flask(__name__)

@app.route('/backend')
def backend():
    print("Pulling up")
    GPIO.output(pin, GPIO.HIGH)
    sleep(1)
    GPIO.output(pin, GPIO.LOW)
    return "Successfully triggered"

@app.route('/')
def index():
    return Response(open("index.html").read(), mimetype="text/html")


if __name__ == '__main__':
    app.run(debug=True)