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


@app.route("/states", strict_slashes=False)
def list_states():
    """ Display States and their assoiciate cities """
    state_list = [v for k, v in storage.all("State").items()]
    return render_template('7-states_list.html', states=state_list)


@app.route("/states/<id>", strict_slashes=False)
def cities_by_state(id):
    """ Display the assoiciates cities of the given state """
    fstate = storage.all().get("State." + id)
    return render_template('9-states.html', state=fstate)


if __name__ == "__main__":
    app.run(debug=True)
