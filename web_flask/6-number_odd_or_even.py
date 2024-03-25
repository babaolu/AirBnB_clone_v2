#!/usr/bin/python3
""" A Flask application """
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """ Root url """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def world():
    """ Path to hbnb """
    return "HBNB"


@app.route("/c/<name>", strict_slashes=False)
def c_is_fun(name):
    """ Adding custom name to path """
    return "C {}".format(escape(name).replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<name>", strict_slashes=False)
def p_is_cool(name="is cool"):
    """ Adding custom name to path with default value"""
    return "Python {}".format(escape(name).replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def display_num(n):
    """ Displaying custom number """
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def html_num(n):
    """ Display html with custom number """
    return render_template('5-number.html', name=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def html_odd_or_even(n):
    """ Display whether custom number is even or odd """
    return render_template('6-number_odd_or_even.html', name=n)


if __name__ == "__main__":
    app.run(debug=True)
