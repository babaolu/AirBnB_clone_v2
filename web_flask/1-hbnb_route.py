#!/usr/bin/python3
""" A Flask application """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """ Root url """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def world():
    """ Path to hbnb """
    return "HBNB"


if __name__ == "__main__":
    app.run()
