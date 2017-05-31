#!flask/bin/python
from flask import Flask, Response

app = Flask(__name__)

@app.route('/backend')
def backend():
    print("halasdakshdlaks")
    return "Hello, World!"

@app.route('/')
def index():
    return Response(open("index.html").read(), mimetype="text/html")


if __name__ == '__main__':
    app.run(debug=True)