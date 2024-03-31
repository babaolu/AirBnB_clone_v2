#!/usr/bin/python3
""" A Flask application """
from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception=None):
    """ Cleanup procedures """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def list_states():
    """ Display States and their assoiciate cities """
    state_list = [v for k, v in storage.all("State").items()]
    return render_template('8-cities_by_states.html', states=state_list)


if __name__ == "__main__":
    app.run(debug=True)
